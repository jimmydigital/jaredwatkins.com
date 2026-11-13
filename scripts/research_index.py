#!/usr/bin/env python3
"""
research_index.py — age and modification index for content/research/.

Frontmatter (date, lastmod, last_reviewed, stale_after_days) is the source of
truth. This tool derives two files from it and never needs hand-editing:

  data/research/index.json     one record per entry (dates, due date, content hash)
  data/research/history.jsonl  append-only event log (added / modified / reviewed /
                               moved / removed / rebuild)

Usage (run from anywhere; paths may be repo-relative or research-relative):

  python3 scripts/research_index.py update              # after creating/editing entries
  python3 scripts/research_index.py stale --limit 10    # refresh queue, most overdue first
  python3 scripts/research_index.py stamp PATH...       # set lastmod + last_reviewed to today
  python3 scripts/research_index.py stamp --modified-only PATH...   # lastmod only
  python3 scripts/research_index.py check               # read-only validation (exit 1 on errors)
  python3 scripts/research_index.py rebuild             # full rebuild + reconcile after a reorg
  python3 scripts/research_index.py show PATH           # one entry's record and history
  python3 scripts/research_index.py stats               # counts and age by topic area

`update` runs a consistency check first and switches to a full rebuild on its
own when the index no longer matches the tree (sections moved or renamed,
index file missing or damaged). Standard library only; Python 3.8+.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict

SCHEMA = 1
DEFAULT_STALE_DAYS = 180
REQUIRED = ["title", "date", "lastmod", "draft", "description", "research_area", "last_reviewed"]
DATE_KEYS = ("date", "lastmod", "last_reviewed")
RECORD_KEYS = ("kind", "title", "research_area", "created", "lastmod", "last_reviewed",
               "stale_after_days", "due", "hash", "first_indexed", "revisions")
SKIP_DIRS = {"_to_delete"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
KEY_RE = re.compile(r"^([A-Za-z_][\w-]*):\s*(.*)$")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Ctx:
    def __init__(self, args):
        self.repo = os.path.abspath(args.root) if args.root else REPO
        self.research = os.path.join(self.repo, "content", "research")
        self.data_dir = os.path.join(self.repo, "data", "research")
        self.index_path = os.path.join(self.data_dir, "index.json")
        self.history_path = os.path.join(self.data_dir, "history.jsonl")
        self.today = dt.date.fromisoformat(args.today) if args.today else dt.date.today()
        if not os.path.isdir(self.research):
            sys.exit(f"error: {self.research} not found (use --root)")


# ---------------------------------------------------------------- scanning

def split_frontmatter(text):
    """Return (frontmatter_lines, body) or (None, text) when there is no YAML block."""
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    nl = text.find("\n", end + 1)
    body = text[nl + 1:] if nl != -1 else ""
    return text[4:end].split("\n"), body


def scalar(v):
    v = v.strip()
    if v[:1] in "\"'" and len(v) >= 2:
        q = v[0]
        close = v.find(q, 1)
        return v[1:close] if close != -1 else v[1:]
    return re.sub(r"\s+#.*$", "", v).strip()


def parse_fm(lines):
    """Top-level scalars plus the item count of top-level lists."""
    fm, lists, cur = {}, Counter(), None
    for line in lines:
        m = KEY_RE.match(line)
        if m:
            cur = m.group(1)
            fm[cur] = scalar(m.group(2))
        elif cur and re.match(r"^\s*-\s+\S", line):
            lists[cur] += 1
    return fm, lists


def content_hash(fm_lines, body):
    """Hash of everything except the lastmod / last_reviewed lines, whitespace-normalised."""
    keep = [l.rstrip() for l in fm_lines if not re.match(r"^(lastmod|last_reviewed):", l)]
    norm = "\n".join(keep) + "\n---\n" + "\n".join(l.rstrip() for l in body.split("\n")).strip()
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()[:16]


def valid_date(s):
    if not s or not DATE_RE.match(s):
        return None
    try:
        return dt.date.fromisoformat(s)
    except ValueError:
        return None


def scan(ctx):
    """Read every research markdown file. Returns {relpath: record} with live values."""
    out = {}
    for d, dirs, files in os.walk(ctx.research):
        dirs[:] = sorted(x for x in dirs if x not in SKIP_DIRS and not x.startswith("."))
        for f in sorted(files):
            if not f.endswith(".md") or f.startswith("."):
                continue
            full = os.path.join(d, f)
            rel = os.path.relpath(full, ctx.research).replace(os.sep, "/")
            with open(full, encoding="utf-8", errors="replace") as fh:
                text = fh.read()
            fm_lines, body = split_frontmatter(text)
            fm, lists = parse_fm(fm_lines or [])
            if rel.startswith("changelog/"):
                kind = "changelog"
            elif f == "_index.md" and ("sitemap" in fm or "source_urls" not in fm):
                kind = "section"
            else:
                kind = "entry"
            try:
                stale = int(fm.get("stale_after_days", ""))
            except ValueError:
                stale = None
            reviewed = valid_date(fm.get("last_reviewed"))
            due = reviewed + dt.timedelta(days=stale or DEFAULT_STALE_DAYS) if reviewed else None
            out[rel] = {
                "kind": kind,
                "title": fm.get("title", ""),
                "research_area": fm.get("research_area", ""),
                "draft": fm.get("draft", "") == "true",
                "created": fm.get("date", ""),
                "lastmod": fm.get("lastmod", ""),
                "last_reviewed": fm.get("last_reviewed", ""),
                "stale_after_days": stale or DEFAULT_STALE_DAYS,
                "due": due.isoformat() if due else "",
                "hash": content_hash(fm_lines or [], body),
                "words": len(body.split()),
                "sources": lists.get("source_urls", 0),
                "_fm": fm, "_has_fm": fm_lines is not None, "_stale_raw": fm.get("stale_after_days"),
            }
    return out


def public(rec):
    return {k: v for k, v in rec.items() if not k.startswith("_")}


# ---------------------------------------------------------------- index io

def load_index(ctx):
    """Returns (entries, problem). problem is a string when the file is unusable."""
    if not os.path.exists(ctx.index_path):
        return {}, "index file does not exist"
    try:
        with open(ctx.index_path, encoding="utf-8") as fh:
            doc = json.load(fh)
    except (ValueError, OSError) as e:
        return {}, f"index file unreadable ({e})"
    if doc.get("schema") != SCHEMA or not isinstance(doc.get("entries"), dict):
        return {}, "index schema mismatch"
    return doc["entries"], None


def save_index(ctx, entries):
    os.makedirs(ctx.data_dir, exist_ok=True)
    doc = {"schema": SCHEMA, "generated": ctx.today.isoformat(), "root": "content/research",
           "count": len(entries), "entries": {k: entries[k] for k in sorted(entries)}}
    payload = json.dumps(doc, indent=1, ensure_ascii=False) + "\n"
    with open(ctx.index_path, "w", encoding="utf-8") as fh:
        fh.write(payload)


def log_events(ctx, events):
    if not events:
        return
    os.makedirs(ctx.data_dir, exist_ok=True)
    with open(ctx.history_path, "a", encoding="utf-8") as fh:
        for e in events:
            fh.write(json.dumps({"date": ctx.today.isoformat(), **e}, ensure_ascii=False) + "\n")


def read_history(ctx):
    if not os.path.exists(ctx.history_path):
        return []
    out = []
    with open(ctx.history_path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except ValueError:
                    pass
    return out


def git_dates(ctx):
    """{relpath: (first_commit_date, last_commit_date)}; empty when git is unavailable."""
    try:
        res = subprocess.run(
            ["git", "-C", ctx.repo, "log", "--format=@%ad", "--date=short", "--name-only",
             "--", "content/research"],
            capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.SubprocessError):
        return {}
    if res.returncode != 0:
        return {}
    out, cur = {}, None
    for line in res.stdout.split("\n"):
        if line.startswith("@"):
            cur = line[1:].strip()
        elif line.startswith("content/research/") and cur:
            rel = line[len("content/research/"):]
            last = out[rel][1] if rel in out else cur   # log is newest first
            out[rel] = (cur, last)
    return out


# ---------------------------------------------------------------- core logic

def find_inconsistencies(old, live):
    """Structural problems that mean the index no longer describes the tree."""
    problems = []
    gone = [p for p in old if p not in live]
    if gone:
        problems.append(f"{len(gone)} indexed path(s) no longer exist (e.g. {gone[0]})")
    bad = [p for p, r in old.items() if any(k not in r for k in RECORD_KEYS)]
    if bad:
        problems.append(f"{len(bad)} index record(s) are incomplete (e.g. {bad[0]})")
    return problems


def new_record(ctx, rec, carry=None, gitmap=None, path=None):
    out = public(rec)
    if carry:
        for k in ("first_indexed", "last_change", "revisions", "git_first", "git_last"):
            if k in carry:
                out[k] = carry[k]
    out.setdefault("first_indexed", ctx.today.isoformat())
    out.setdefault("last_change", "")
    out.setdefault("revisions", 0)
    if gitmap and path in gitmap and "git_first" not in out:
        out["git_first"], out["git_last"] = gitmap[path]
    return out


def diff_in_place(ctx, path, old_rec, rec, events, warnings):
    """Compare one path that exists in both index and tree; returns the new record."""
    out = new_record(ctx, rec, carry=old_rec)
    if rec["hash"] != old_rec.get("hash"):
        out["revisions"] = old_rec.get("revisions", 0) + 1
        out["last_change"] = ctx.today.isoformat()
        events.append({"event": "modified", "path": path, "lastmod": rec["lastmod"],
                       "hash": rec["hash"]})
        if rec["lastmod"] == old_rec.get("lastmod") and rec["lastmod"] != ctx.today.isoformat():
            warnings.append(f"content changed but lastmod not bumped: {path} (lastmod {rec['lastmod']})")
    if rec["last_reviewed"] != old_rec.get("last_reviewed"):
        events.append({"event": "reviewed", "path": path, "last_reviewed": rec["last_reviewed"],
                       "previous": old_rec.get("last_reviewed", "")})
    return out


def do_update(ctx, old, live):
    events, warnings, new = [], [], {}
    for path, rec in live.items():
        if path in old:
            new[path] = diff_in_place(ctx, path, old[path], rec, events, warnings)
        else:
            new[path] = new_record(ctx, rec)
            events.append({"event": "added", "path": path, "hash": rec["hash"]})
    return new, events, warnings


def do_rebuild(ctx, old, live, reason):
    """Rebuild every record from the tree, carrying history across moves and renames.

    Identity matching for paths that vanished, in order of confidence:
      1. identical content hash           (pure move)
      2. same filename and same title     (moved and edited)
      3. same title, unique on both sides (file renamed and moved)
    """
    events, warnings, new = [], [], {}
    gitmap = git_dates(ctx)
    gone = {p: r for p, r in old.items() if p not in live}
    fresh = [p for p in live if p not in old]

    def index_by(keyfn, paths, recs):
        m = defaultdict(list)
        for p in paths:
            k = keyfn(p, recs[p])
            if k:
                m[k].append(p)
        return m

    matched = {}  # new path -> old path
    for keyfn in (lambda p, r: r.get("hash"),
                  lambda p, r: (os.path.basename(p), r.get("title")) if r.get("title") else None,
                  lambda p, r: r.get("title") or None):
        g = index_by(keyfn, [p for p in gone if p not in matched.values()], gone)
        f = index_by(keyfn, [p for p in fresh if p not in matched], live)
        for k, new_paths in f.items():
            if len(new_paths) == 1 and len(g.get(k, [])) == 1:
                matched[new_paths[0]] = g[k][0]

    for path, rec in live.items():
        if path in old and all(k in old[path] for k in RECORD_KEYS):
            new[path] = diff_in_place(ctx, path, old[path], rec, events, warnings)
            if gitmap and path in gitmap and "git_first" not in new[path]:
                new[path]["git_first"], new[path]["git_last"] = gitmap[path]
        elif path in matched:
            src = matched[path]
            events.append({"event": "moved", "path": path, "from": src})
            new[path] = diff_in_place(ctx, path, gone[src], rec, events, warnings)
        else:
            new[path] = new_record(ctx, rec, carry=old.get(path), gitmap=gitmap, path=path)
            if old:
                events.append({"event": "added", "path": path, "hash": rec["hash"]})
    for p in gone:
        if p not in matched.values():
            events.append({"event": "removed", "path": p, "title": gone[p].get("title", "")})
    events.insert(0, {"event": "rebuild", "reason": reason, "entries": len(new),
                      "moved": len(matched), "baseline": not old})
    return new, events, warnings


def area_ok(path, area):
    d = os.path.dirname(path)
    return area == d or (area and d.startswith(area + "/"))


def expected_area(path, rec):
    d = os.path.dirname(path)
    if os.path.basename(path) == "_index.md" and rec["kind"] == "entry":
        return os.path.dirname(d)  # directory-bundle entry belongs to its parent subtopic
    return d


def validate(ctx, live):
    errors, warnings = [], []
    today = ctx.today
    for path, r in live.items():
        if not r["_has_fm"]:
            errors.append(f"no frontmatter: {path}")
            continue
        fm = r["_fm"]
        need = list(REQUIRED) + (["source_urls"] if r["kind"] == "entry" else [])
        missing = [k for k in need if k not in fm]
        if path in ("_index.md", "changelog/index.md"):
            missing = [k for k in missing if k not in ("research_area", "source_urls")]
        if missing:
            errors.append(f"missing {', '.join(missing)}: {path}")
        dates = {}
        for k in DATE_KEYS:
            if k in fm:
                dates[k] = valid_date(fm[k])
                if dates[k] is None:
                    errors.append(f"bad {k} '{fm[k]}': {path}")
                elif dates[k] > today:
                    errors.append(f"{k} {fm[k]} is in the future: {path}")
        if dates.get("date") and dates.get("lastmod") and dates["lastmod"] < dates["date"]:
            errors.append(f"lastmod {fm['lastmod']} is before date {fm['date']}: {path}")
        if r["_stale_raw"] is not None and not re.match(r"^\d+$", r["_stale_raw"]):
            errors.append(f"stale_after_days '{r['_stale_raw']}' is not a whole number: {path}")
        if path not in ("_index.md", "changelog/index.md") and r["research_area"] \
                and not area_ok(path, r["research_area"]):
            warnings.append(f"research_area '{r['research_area']}' does not match location: {path}")
    return errors, warnings


def sync_state(old, live):
    """Differences between the saved index and the tree, without writing anything."""
    notes = []
    for p in live:
        if p not in old:
            notes.append(f"not indexed yet: {p}")
        elif live[p]["hash"] != old[p].get("hash"):
            notes.append(f"changed since last index: {p}")
    for p in old:
        if p not in live:
            notes.append(f"indexed but missing from tree: {p}")
    return notes


# ---------------------------------------------------------------- helpers

def resolve(ctx, raw):
    """Accept repo-relative, research-relative or absolute paths; return research-relative."""
    cands = [raw, os.path.join(ctx.repo, raw), os.path.join(ctx.research, raw)]
    for c in cands:
        if os.path.isdir(c):
            c = os.path.join(c, "_index.md")
        if os.path.isfile(c):
            rel = os.path.relpath(os.path.abspath(c), ctx.research).replace(os.sep, "/")
            if not rel.startswith(".."):
                return rel
    return None


def set_fm_key(text, key, value, after="date"):
    """Replace (or insert) one top-level scalar inside the frontmatter block only."""
    if not text.startswith("---"):
        return text, False
    end = text.find("\n---", 3)
    if end == -1:
        return text, False
    head, rest = text[:end], text[end:]
    pat = re.compile(rf"^{re.escape(key)}:.*$", re.M)
    if pat.search(head):
        new_head = pat.sub(f"{key}: {value}", head, count=1)
    else:
        anchor = re.search(rf"^{re.escape(after)}:.*$", head, re.M)
        if anchor:
            new_head = head[:anchor.end()] + f"\n{key}: {value}" + head[anchor.end():]
        else:
            new_head = head + f"\n{key}: {value}"
    return new_head + rest, new_head != head


def report(events, warnings, limit=25):
    counts = Counter(e["event"] for e in events)
    order = ["added", "modified", "reviewed", "moved", "removed"]
    summary = ", ".join(f"{counts[k]} {k}" for k in order if counts[k]) or "no changes"
    print(summary)
    shown = [e for e in events if e["event"] in order and e["event"] != "reviewed"]
    for e in shown[:limit]:
        extra = f"  (from {e['from']})" if e["event"] == "moved" else ""
        print(f"  {e['event']:<9}{e['path']}{extra}")
    if len(shown) > limit:
        print(f"  ... and {len(shown) - limit} more (see data/research/history.jsonl)")
    for w in warnings:
        print(f"  WARNING  {w}")


# ---------------------------------------------------------------- commands

def cmd_update(ctx, args):
    live = scan(ctx)
    old, problem = load_index(ctx)
    problems = [problem] if problem else find_inconsistencies(old, live)
    if problems:
        reason = "; ".join(problems)
        print(f"index inconsistent — rebuilding: {reason}")
        new, events, warnings = do_rebuild(ctx, old, live, reason)
    else:
        new, events, warnings = do_update(ctx, old, live)
    if new != old or problems:
        save_index(ctx, new)
    log_events(ctx, events)
    report(events, warnings)
    print(f"index: {len(new)} entries")
    return 0


def cmd_rebuild(ctx, args):
    live = scan(ctx)
    old, problem = load_index(ctx)
    if args.fix_areas:
        fixed = 0
        for path, r in live.items():
            if path in ("_index.md", "changelog/index.md") or area_ok(path, r["research_area"]):
                continue
            full = os.path.join(ctx.research, path)
            with open(full, encoding="utf-8") as fh:
                text = fh.read()
            want = expected_area(path, r)
            text2, changed = set_fm_key(text, "research_area", f'"{want}"', after="description")
            if changed:
                text2, _ = set_fm_key(text2, "lastmod", ctx.today.isoformat(), after="date")
                with open(full, "w", encoding="utf-8") as fh:
                    fh.write(text2)
                print(f"  research_area {r['research_area'] or '(none)'} -> {want}: {path}")
                fixed += 1
        if fixed:
            live = scan(ctx)
    reason = problem or "; ".join(find_inconsistencies(old, live)) or "requested"
    new, events, warnings = do_rebuild(ctx, old, live, reason)
    save_index(ctx, new)
    log_events(ctx, events)
    report(events, warnings)
    _, vwarn = validate(ctx, live)
    stray = [w for w in vwarn if "does not match location" in w]
    if stray:
        print(f"  {len(stray)} entries have a research_area that no longer matches their "
              f"location (run: rebuild --fix-areas)")
    print(f"index rebuilt: {len(new)} entries ({reason})")
    return 0


def cmd_stale(ctx, args):
    live = scan(ctx)
    rows = []
    for path, r in live.items():
        if r["kind"] == "changelog" or r["draft"]:
            continue
        if args.kind != "all" and r["kind"] != args.kind:
            continue
        if args.area and not (path == args.area or path.startswith(args.area.rstrip("/") + "/")):
            continue
        if not r["due"]:
            rows.append((10 ** 6, path, r))
            continue
        overdue = (ctx.today - dt.date.fromisoformat(r["due"])).days
        if overdue >= -args.within:
            rows.append((overdue, path, r))
    rows.sort(key=lambda x: (-x[0], x[1]))
    total = len(rows)
    if args.limit:
        rows = rows[:args.limit]
    if args.json:
        print(json.dumps([{"path": "content/research/" + p, "days_overdue": o if o < 10 ** 6 else None,
                           "last_reviewed": r["last_reviewed"], "lastmod": r["lastmod"],
                           "stale_after_days": r["stale_after_days"], "due": r["due"],
                           "kind": r["kind"], "title": r["title"]} for o, p, r in rows], indent=1))
        return 0
    if not rows:
        print("nothing due")
        return 0
    print(f"{'overdue':>7}  {'reviewed':<10}  {'cadence':>7}  path")
    for o, p, r in rows:
        od = "no date" if o >= 10 ** 6 else (f"{o}d" if o >= 0 else f"in {-o}d")
        print(f"{od:>7}  {r['last_reviewed'] or '-':<10}  {r['stale_after_days']:>6}d  content/research/{p}")
    if total > len(rows):
        print(f"({len(rows)} of {total} shown)")
    return 0


def cmd_stamp(ctx, args):
    today = ctx.today.isoformat()
    rc = 0
    for raw in args.paths:
        rel = resolve(ctx, raw)
        if not rel:
            print(f"not found under content/research: {raw}")
            rc = 1
            continue
        full = os.path.join(ctx.research, rel)
        with open(full, encoding="utf-8") as fh:
            text = fh.read()
        text, c1 = set_fm_key(text, "lastmod", today, after="date")
        c2 = False
        if not args.modified_only:
            text, c2 = set_fm_key(text, "last_reviewed", today, after="lastmod")
        if c1 or c2:
            with open(full, "w", encoding="utf-8") as fh:
                fh.write(text)
        what = "lastmod" if args.modified_only else "lastmod + last_reviewed"
        print(f"{'stamped' if (c1 or c2) else 'already current'} ({what} = {today}): {rel}")
    if rc == 0:
        print("run `update` to record these in the index")
    return rc


def cmd_check(ctx, args):
    live = scan(ctx)
    errors, warnings = validate(ctx, live)
    old, problem = load_index(ctx)
    notes = [problem] if problem else sync_state(old, live)
    for e in errors:
        print(f"ERROR    {e}")
    for w in warnings:
        print(f"WARNING  {w}")
    if notes:
        print(f"INDEX    {len(notes)} difference(s) from the tree — run `update`"
              + (f" (e.g. {notes[0]})" if notes else ""))
    print(f"{len(live)} files checked: {len(errors)} errors, {len(warnings)} warnings, "
          f"index {'out of date' if notes else 'in sync'}")
    return 1 if errors or (args.strict and (warnings or notes)) else 0


def cmd_show(ctx, args):
    rel = resolve(ctx, args.path)
    if not rel:
        print(f"not found under content/research: {args.path}")
        return 1
    live = scan(ctx)
    old, _ = load_index(ctx)
    rec = dict(old.get(rel, {}))
    rec.update(public(live[rel]))
    if rec.get("due"):
        rec["days_overdue"] = (ctx.today - dt.date.fromisoformat(rec["due"])).days
    rec["indexed"] = rel in old
    print(json.dumps({"path": "content/research/" + rel, **rec}, indent=1, ensure_ascii=False))
    history = read_history(ctx)
    names = {rel}
    for e in reversed(history):       # follow the entry back through earlier locations
        if e.get("event") == "moved" and e.get("path") in names:
            names.add(e.get("from"))
    mine = [e for e in history if e.get("path") in names]
    print(f"history ({len(mine)} events):")
    for e in mine:
        detail = {k: v for k, v in e.items() if k not in ("date", "event", "path")}
        print(f"  {e['date']}  {e['event']:<9}{e['path'] if e['path'] != rel else ''}"
              f"{'  ' + json.dumps(detail, ensure_ascii=False) if detail else ''}")
    return 0


def cmd_stats(ctx, args):
    live = scan(ctx)
    areas = defaultdict(lambda: {"n": 0, "overdue": 0, "ages": []})
    for path, r in live.items():
        if r["kind"] == "changelog":
            continue
        a = areas[path.split("/")[0] if "/" in path else "(root)"]
        a["n"] += 1
        rv = valid_date(r["last_reviewed"])
        if rv:
            a["ages"].append((ctx.today - rv).days)
        if r["due"] and dt.date.fromisoformat(r["due"]) < ctx.today:
            a["overdue"] += 1
    print(f"{'area':<30}{'files':>6}{'overdue':>9}{'median age':>12}{'oldest':>8}")
    tn = to = 0
    for name in sorted(areas):
        a = areas[name]
        ages = sorted(a["ages"])
        med = f"{ages[len(ages) // 2]}d" if ages else "-"
        print(f"{name:<30}{a['n']:>6}{a['overdue']:>9}{med:>12}{(str(ages[-1]) + 'd') if ages else '-':>8}")
        tn += a["n"]
        to += a["overdue"]
    print(f"{'total':<30}{tn:>6}{to:>9}")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Age and modification index for content/research/.")
    ap.add_argument("--root", help="repository root (default: parent of scripts/)")
    ap.add_argument("--today", help=argparse.SUPPRESS)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("update", help="record new and modified entries (auto-rebuilds if inconsistent)")
    p = sub.add_parser("rebuild", help="rebuild the whole index and reconcile moved entries")
    p.add_argument("--fix-areas", action="store_true",
                   help="rewrite research_area on entries whose location no longer matches it")
    p = sub.add_parser("stale", help="list entries due for review, most overdue first")
    p.add_argument("--limit", type=int, default=0)
    p.add_argument("--area", help="path prefix under content/research, e.g. energy/nuclear")
    p.add_argument("--within", type=int, default=0, help="also include entries due within N days")
    p.add_argument("--kind", choices=["entry", "section", "all"], default="all")
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("stamp", help="set lastmod and last_reviewed to today")
    p.add_argument("paths", nargs="+")
    p.add_argument("--modified-only", action="store_true", help="set lastmod only")
    p = sub.add_parser("check", help="validate frontmatter and index sync without writing")
    p.add_argument("--strict", action="store_true", help="exit 1 on warnings too")
    p = sub.add_parser("show", help="one entry's record and history")
    p.add_argument("path")
    sub.add_parser("stats", help="counts and review age by topic area")
    args = ap.parse_args()
    ctx = Ctx(args)
    sys.exit({"update": cmd_update, "rebuild": cmd_rebuild, "stale": cmd_stale, "stamp": cmd_stamp,
              "check": cmd_check, "show": cmd_show, "stats": cmd_stats}[args.cmd](ctx, args))


if __name__ == "__main__":
    main()
