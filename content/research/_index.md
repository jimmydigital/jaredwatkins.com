---
title: Research
date: 2026-03-23
lastmod: 2026-07-03
draft: false
last_reviewed: 2026-04-07
description: AI-maintained knowledge base on emerging technology topics.
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---

{{<steering>}}

## Research Section — Steering Instructions

This block contains editorial and structural guidelines for AI tools maintaining the Research section. Human editors may also refer to it, but it is written primarily as a system spec for automated agents.

**Note for AI tools:** This entire steering block is wrapped in `{{</* steering */>}}` / `{{</* /steering */>}}` shortcode tags. This shortcode renders nothing to the Hugo output — the content is invisible on the live site but fully present in the source file for tool access. Any file that contains AI steering instructions should use the same pattern: wrap them in `{{</* steering */>}}...{{</* /steering */>}}` rather than `<details>` or HTML comments.

---

### Disclaimer

**Every entry in the Research section may be incomplete, out of date, or inaccurate.** This knowledge base is AI-maintained and updated on a best-effort basis. Do not rely on any entry as a sole or authoritative source. Verify critical facts independently before acting on them. Each entry includes source URLs — consult those primary sources directly.

This disclaimer must appear at the top of every individual entry page, wrapped in a blockquote:

```markdown
> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.
```

---

### Purpose & Editorial Philosophy

The Research section is a living knowledge base on emerging technology topics. It is factual, structured, and continuously updated — not a blog, not opinion writing. Think of each entry as a well-maintained Wikipedia stub: accurate, sourced, and useful to a technically literate reader who wants a fast orientation to a person, company, technology, or breakthrough.

**Tone:** Neutral, informative, third-person. No hype, no advocacy.
**Depth:** Enough to understand what something is, why it matters, and where to learn more. Not exhaustive — link out rather than reproduce.
**Audience:** A technically literate generalist (engineer, analyst, curious professional).

**Editorial focus — startups and development partners first:** The primary interest is in smaller companies, university spinouts, material science startups, and development-stage partners behind the low-level innovations — not the incumbents who eventually adopt them. Blue chip companies (Toyota, Samsung, CATL, etc.) are worth documenting as market context signals, but they should not be the center of gravity. When a large OEM announces a solid-state program, the more interesting entry is the startup supplying their electrolyte, the materials company solving the interface problem, or the research lab that originated the chemistry. Prioritize entries for:

- Early-stage and growth-stage startups with a specific technical differentiation
- University spinouts and research commercialization vehicles
- Materials and component suppliers enabling next-gen technology
- Development partners and contract manufacturers at the frontier

Incumbents belong in tables and as supporting context in other entries, but detailed standalone entries for large public companies should only be created when there is something genuinely novel and specific to document — not just because they are a known player in the space.

---

### Directory & File Naming Conventions

The hierarchy is: `content/research/` → topic area → subtopic → entry.

**Two valid file structures for entries — choose the right one:**

**Flat file** (default for simple entries with no sub-pages or images):
```
content/research/energy/solar/first-solar.md
```
Relref: `{{</* relref "energy/solar/first-solar.md" */>}}`

**Directory bundle** (use when an entry needs sub-pages, images, or embedded assets):
```
content/research/energy/solar/spectrolab/_index.md
```
Relref: `{{</* relref "energy/solar/spectrolab" */>}}` ← **no filename, just the directory path**

**Critical rule — form must match structure:** A `relref` to `"energy/solar/spectrolab"` resolves only if that path is a directory bundle (`_index.md`). A `relref` to `"energy/solar/first-solar.md"` resolves only if that is a flat file. Hugo will throw `REF_NOT_FOUND` if the form doesn't match the actual file structure. Before writing any `relref`, check which structure the target uses and match it exactly.

**Critical rule — `relref` path resolution differs between regular pages and `_index.md` files:**

Hugo's `relref` behavior depends on whether the calling page is a regular content file or a section `_index.md`:

- **Regular content pages** (e.g., `datacenters/cooling/submer.md`): Hugo searches the full content tree for a unique filename match. A bare `relref "ge-vernova-aeroderivative.md"` will find the file even if it's in a completely different subtopic, as long as the filename is unique across the site. This is why changelog and individual entry links mostly work without explicit paths.

- **`_index.md` files**: Hugo resolves paths **relative to the filesystem location of the `_index.md`**, exactly like a Unix path. There is no magic filename search. A `relref "ge-vernova-aeroderivative.md"` inside `datacenters/power-infrastructure/_index.md` looks for a file named that **in the same directory** — and fails if it's actually in `datacenters/behind-meter-power/`.

**The rule for `_index.md` files — always use filesystem-relative paths:**

| Link target | Calling `_index.md` location | Correct relref |
|-------------|------------------------------|----------------|
| Same directory | `datacenters/power-infrastructure/_index.md` → `vertiv.md` | `{{</* relref "vertiv.md" */>}}` |
| Sibling directory | `datacenters/power-infrastructure/_index.md` → `behind-meter-power/ge-vernova-aeroderivative.md` | `{{</* relref "../behind-meter-power/ge-vernova-aeroderivative.md" */>}}` |
| Grandparent then sibling | `datacenters/power-infrastructure/_index.md` → `energy/nuclear/oklo.md` | `{{</* relref "../../energy/nuclear/oklo.md" */>}}` |
| Section index | `datacenters/behind-meter-power/_index.md` → `datacenters/power-infrastructure/_index.md` | `{{</* relref "../power-infrastructure/_index.md" */>}}` |

**Do NOT use a `/research/` prefix** — this is not a valid Hugo relref form and will cause `REF_NOT_FOUND`. Hugo `relref` paths are always relative to the calling page (for `_index.md`) or searched site-wide by unique filename (for regular pages). There is no absolute path mode.

**Quick checklist before writing any relref in an `_index.md`:**
1. What directory is the calling `_index.md` in?
2. What directory is the target file in?
3. Write the relative path from (1) to (2) using `../` to go up, then the path down to the target.
4. For directory bundles, omit `_index.md` from the path end — use the directory name only.

**Which to use:** Prefer flat files unless the entry needs assets (images, data files) co-located with the content. Directory bundles add filesystem overhead. Check what already exists in the subtopic directory before creating a new entry — be consistent with the predominant pattern there.

Full layout:
```
content/research/
  _index.md                          ← this file (section landing)
  energy/
    _index.md                        ← topic area landing
    solar/
      _index.md                      ← subtopic landing
      first-solar.md                 ← flat file entry (simple)
      spectrolab/
        _index.md                    ← directory bundle entry (has assets)
    batteries/
      _index.md
      catl.md
      solid-state-overview.md
```

**Naming rules:**
- All filenames and directory names: lowercase, hyphenated, no special characters.
- People: `firstname-lastname.md` (flat) or `firstname-lastname/` (bundle). For disambiguation, append field: `john-smith-solar.md`.
- Companies: full common name, hyphenated (e.g., `first-solar.md`, `contemporary-amperex.md`).
- Technologies/concepts: descriptive slug (e.g., `perovskite-cells.md`, `flow-batteries.md`).
- Topic area and subtopic `_index.md` files contain only section metadata and a brief description — no entry content.

---

### Hugo Frontmatter Conventions

All entry files must include the following frontmatter:

```yaml
---
title: "First Solar"
date: 2025-01-15
lastmod: 2026-03-01
draft: false
description: "Brief one-sentence summary."
research_area: "energy/solar"
source_urls:
  - "https://example.com"
last_reviewed: 2026-03-01
stale_after_days: 180
---
```

Required fields: `title`, `date`, `lastmod`, `draft`, `description`, `research_area`, `source_urls`, `last_reviewed`.

**Do not add `tags` or `categories` to research entries.** Both generate Hugo taxonomy pages at scale and degrade build/deploy performance. Use `research_area` for all classification and filtering.
Optional but encouraged: `stale_after_days` (default 180 if omitted), `related` (list of relative paths to related entries).

**Section landing pages (`_index.md`)** use a slightly different template — no `source_urls`, but always include the `sitemap` block:

```yaml
---
title: "Section Title"
date: 2026-01-01
lastmod: 2026-01-01
draft: false
description: "Brief one-sentence summary of this section."
research_area: "topic/subtopic"
last_reviewed: 2026-01-01
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---
```

The `sitemap` block is **required on every `_index.md`** — both topic-area landings (e.g., `energy/_index.md`) and subtopic landings (e.g., `energy/solar/_index.md`). Do not omit it when creating new sections. **Do not add it to individual entry files** (company, person, technology, or breakthrough pages) — sitemap control applies only to section landing pages.

---

### Entry Structure

Every entry (person, company, technology, or breakthrough) should follow this template:

```
## Summary
One to three sentences. What is this, and why does it matter?

## Key Facts
- Developed by / Founded / Born: [year or org]
- Type: [technology | company | person | breakthrough]
- Status: [active / emerging / defunct]
- Key metric(s): [efficiency, capacity, funding, etc.]

## What It Is / How It Works
Two to five paragraphs. Clear, neutral explanation of the subject.

## Notable Developments
Reverse-chronological list of milestones. Include dates.

- **2026-01:** [Event]
- **2025-09:** [Event]

## Key People / Key Organizations
(Omit if this entry IS a person or small org.)

## Sources
- [Source Title](URL) — brief annotation if helpful
```

Section landing pages (`_index.md`) contain only `## Overview` and optionally `## Key Themes`. No deep content.

---

### Creating vs. Updating Entries

**Create a new entry when:**
- The subject has no file in the appropriate subtopic directory.
- A new subtopic is needed: first create the subtopic directory and its `_index.md`, then the entry.

**Update an existing entry when:**
- New factual information is available.
- The `last_reviewed` date is older than `stale_after_days`.
- A source URL is broken or outdated.

**Update rules:**
- Always update `lastmod` and `last_reviewed` in frontmatter.
- Prepend to `Notable Developments` (newest first); do not delete prior entries unless factually wrong.
- Revise `What It Is / How It Works` in place — don't overwrite wholesale.
- Add new source URLs; don't remove old ones unless dead and unarchivable.

**Changelog update requirements:**
When creating a new major research section or adding multiple significant entries to the Research knowledge base, update `content/research/changelog/index.md`. Log: new section/entry creation, major rewrites, significant claim corrections, or structural `_index.md` changes. Do not log: minor edits, formatting fixes, link repairs, or routine fact-checking.

**Format rule — one line per entry, no exceptions.**

Each entry is a single markdown bullet on a single line:
`- **YYYY-MM-DD:** Created/Updated [Page Title]({{</* relref "path/to/page.md" */>}}) — [subject, 2–3 key facts max].`

For bulk entries (5+ related additions in a single action), use compound format:
`- **YYYY-MM-DD:** Created [Overview Name]({{</* relref "..." */>}}) + N entries: [Entry 1]({{</* relref "..." */>}}) ([key fact]), [Entry 2]({{</* relref "..." */>}}) ([key fact]), [Entry 3]({{</* relref "..." */>}}) ([key fact]).`

Rules:
- Link page names using Hugo relrefs — never use bare filenames or file paths as the reference text.
- The bullet must fit on one line. Period.
- No semicolon-separated lists of every detail. Pick the 2–3 most important facts and stop.
- No sub-bullets, continuation lines, or parenthetical elaborations.
- For 5+ related entries, combine into a single compound entry with overview link first, then inline summaries.
- The entry file is the authoritative record — the changelog is just a navigable pointer, not a summary.
- If you feel the urge to add more detail, don't. Cut it instead.

**Changelog automation instruction for AI tools:**
After creating or significantly updating research entries, the agent **must** immediately:
1. Determine today's date in YYYY-MM-DD format
2. Compose a single-line changelog entry following the format rules above
3. Insert the entry at the top of the Changelog section (above all other entries, reverse-chronological order)
4. Update the `lastmod` date in the changelog index file frontmatter to today's date
5. Verify the entry fits on one line (no word wrapping in most text editors)
6. Do not wait for user instruction — this is automatic upon entry creation/major update

The changelog entry must be written during the same execution as entry creation. Do not treat changelog updates as a separate task requiring user approval. Every created/updated entry triggers an automatic changelog update.

**Good examples:**
- `- **2026-04-25:** Created [IonQ]({{</* relref "quantum-computing/ionq.md" */>}}) — trapped-ion QPU; Forte 84 qubits; FY2025 $100M+ revenue.`
- `- **2026-04-25:** Created [half-rack embedded compute overview]({{</* relref "datacenters/rugged-edge-compute/half-rack-embedded-compute.md" */>}}) + 4 platform entries: [Neousys SEMIL-1300]({{</* relref "datacenters/rugged-edge-compute/neousys-semil-1300.md" */>}}) (fanless 2U half-rack, IP67), [ASUS RUC-1000]({{</* relref "datacenters/rugged-edge-compute/asus-ruc-1000.md" */>}}) (RUC-1000G 600W GPU; RUC-1000D half-rack fanless).`

**Bad examples (do not do this):**
- `- **2026-04-05:** Created \`quantum-computing/ionq.md\` — full IonQ entry covering Forte/Tempo hardware specs, FY2024/2025 revenue, Skyloom/SkyWater acquisitions, all-founder departures.` (bare filename, too long)
- Multi-line entries or sub-bullets (must be single line)
- Missing date or relref links
- Over 200 characters total (tight constraint forces summarization)

---

### Cross-Linking

**Cross-links:** Use Hugo relrefs where entries exist. Two rules govern correct relref syntax:

1. **Form must match file structure:**
   - Flat file: include `.md` extension — e.g., `{{</* relref "energy/solar/first-solar.md" */>}}`
   - Directory bundle: directory path only, no `_index.md` — e.g., `{{</* relref "energy/solar/spectrolab" */>}}`

2. **Path form depends on calling page type** — see the detailed rules in the Directory & File Naming Conventions section above. In brief:
   - From a **regular content page**: bare unique filenames work site-wide (e.g., `{{</* relref "ge-vernova-aeroderivative.md" */>}}`)
   - From an **`_index.md` file**: always use a filesystem-relative path with `../` traversal (e.g., `{{</* relref "../behind-meter-power/ge-vernova-aeroderivative.md" */>}}`)
   - **Never use a `/research/` prefix** — it is not a valid Hugo relref form

Before writing a relref from an `_index.md`, explicitly work out the relative path using the directory table in the naming conventions section.

Where an entry doesn't exist yet, leave an HTML comment:

```
<!-- TODO: create entry for energy/solar/example-researcher.md -->
```

Do not create stub entries just to satisfy a link.

---

### Review Cadence

- Default: 180 days (`stale_after_days: 180`)
- Fast-moving subjects (active startups, recent breakthroughs): 90 days
- Stable reference entries (established companies, mature tech): 365 days
- On review: update `Notable Developments`, verify key facts, check for broken source URLs, update `last_reviewed` and `lastmod`.

---

### Company Tables on Section Landing Pages

Every topic area `_index.md` (e.g., `energy/_index.md`) must include a **Companies** section. Split into three subsections in this order: **Startups & Development Partners** first, then **Public Companies**, then **Incumbents**. This ordering reflects the editorial priority: the innovation edge lives at the startup layer, incumbents provide market context.

**Startups & Development Partners** — private companies at early-to-growth stage, university spinouts, materials suppliers, and development-stage partners:

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Company Name](https://companywebsite.com) | Country | Seed / Series A-C / Pre-IPO / Private | One-line description of what they do. |

- Link the company name to the company's official website (e.g., `[Factorial Energy](https://factorialenergy.com)`).
- If the official website is not findable, use the company's most authoritative public presence (LinkedIn company page, Crunchbase, etc.) and add a TODO comment to find the official site.

**Public Companies** — independent, publicly traded companies that are primarily technology developers (not diversified conglomerates):

| Ticker | Company | Mission |
|--------|---------|---------|
| [TICK](https://finance.yahoo.com/quote/TICK) | [Company Name](https://companywebsite.com) | One-line description of what they do. |

- Link each ticker to its Yahoo Finance quote page: `https://finance.yahoo.com/quote/TICKER`
- Link each company name to its official investor relations or corporate website.
- For non-US exchanges, use the exchange-qualified ticker (e.g., `300750.SZ` for CATL on Shenzhen)
- **Chinese-owned companies (any tier):** append `🇨🇳` after the company name

**Incumbents** — large, diversified public companies (automakers, conglomerates, major battery manufacturers). Include only as context; detailed entries for incumbents should be created only when there is something genuinely novel and specific to document:

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [TICK](https://finance.yahoo.com/quote/TICK) | [Company Name](https://companywebsite.com) | Why they matter to this topic area. |

- Link each company name to its official corporate or investor relations website.

Update all three tables whenever a new entry is added that introduces a new company. Do not list research institutions or universities — only commercial entities.

**Embedded Market Overview Widget** — Each subsection `_index.md` file with a Public Companies table should include a live TradingView Market Overview widget immediately after the Public Companies table. This widget displays 1-year price performance with a mini chart for each public company in the section, giving readers live market context alongside the static company descriptions.

Use `embed-widget-market-overview.js` with `dateRange: "12M"` and `showChart: true`. Each section uses a single tab titled with the section name. Symbols use the `s`/`d` field format (not `proName`/`title`). Supported exchanges include NYSE, NASDAQ, OSLO, TSE, and others — always qualify symbols with their exchange prefix (e.g., `NYSE:VRT`, `NASDAQ:MRCY`, `TSE:6268`).

Canonical embed template:

```html
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container" style="margin: 20px 0;">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
  {
    "colorTheme": "light",
    "dateRange": "12M",
    "showChart": true,
    "locale": "en",
    "showSymbolLogo": true,
    "showFloatingTooltip": true,
    "width": "100%",
    "height": "500",
    "tabs": [
      {
        "title": "Section Title",
        "symbols": [
          {"s": "NYSE:TICKER1", "d": "Company Name 1"},
          {"s": "NASDAQ:TICKER2", "d": "Company Name 2"}
        ],
        "originalTitle": "Section Title"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->
```

Example placement in markdown:

```
### Public Companies

| Ticker | Company | Mission |
...table...

<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container" style="margin: 20px 0;">
  ...widget code...
</div>
<!-- TradingView Widget END -->

### Incumbents
```

The Hugo config has `unsafe = true` in goldmark, so raw script tags render correctly. For sections with more than 15 public companies, split into multiple tabs within the same widget. For sections with fewer than 2 public companies, omit the widget.

---

### Claim Verification for Company Advancements

When a company entry documents a new product, breakthrough, or performance claim, AI tools must research and include a **Claim Verification** section within the entry. This section should:

1. State each significant claim clearly (e.g., "400 Wh/kg energy density", "100,000-cycle life")
2. List sources that **support** the claim, with URLs and brief descriptions of what they confirm
3. List sources that **refute or question** the claim, with URLs and the specific counterargument
4. Summarize the current verification status: `Verified`, `Partially verified`, `Unverified`, or `Disputed`

Format:

```markdown
## Claim Verification

### Claim: [Specific performance or advancement claim]
**Status:** Unverified / Partially verified / Verified / Disputed

**Supporting sources:**
- [Source](URL) — what it confirms

**Refuting / questioning sources:**
- [Source](URL) — the counterargument or gap it identifies

**Summary:** One sentence on where the evidence stands.
```

If no independent third-party verification exists, state that explicitly. Do not omit the section just because claims are hard to verify — absence of verification is itself notable.

---

### DoD Trusted Foundry and Trusted Supplier Status

When any company entry claims or is described as holding [DoD Trusted Foundry or Trusted Supplier status](https://www.acq.osd.mil/asds/dmea/tapo/docs/tp/AccreditedSuppliers-03NOV2025.pdf), follow these rules:

1. **Always link to the official accreditation list** — use the current [DoD TAPO Accredited Suppliers list](https://www.acq.osd.mil/asds/dmea/tapo/docs/tp/AccreditedSuppliers-03NOV2025.pdf) (last updated November 3, 2025). This is a PDF document maintained by the Defense Microelectronics Activity (DMEA) and is the authoritative source of record.
2. **Verify the company name appears on the list** — do not rely on company self-description or press releases. Check the PDF accreditation list to confirm the company's exact name and accreditation status.
3. **Add to source_urls** — include the official accreditation PDF in the entry's `source_urls` frontmatter list.
4. **Link references inline** — whenever the status is mentioned in the entry text (e.g., "X holds Trusted Foundry status"), make it a hyperlink to the accreditation list so readers can verify independently.
5. **Note the document date** — the current version is dated November 3, 2025. If the accreditation list is updated in the future (DMEA publishes updates periodically), update all references to point to the most current version and refresh entry verification.

This status is a real regulatory credential affecting supply chain access and national security confidence in manufacturing security — it is not a technical performance claim, but an administrative fact that must be verified for accuracy.

---

### Source Verification Rules

These rules apply to every entry created or updated. They exist because the most common errors in this knowledge base have been specific numbers written from training knowledge and attributed to unverified (or nonexistent) URLs.

**Rule 1 — Fetch before you write, not after.**
A URL goes in `source_urls` only after its content has been fetched and read during this session. Do not add URLs to justify claims already written. If a source cannot be fetched and read, the claim it would support must either be omitted or explicitly hedged as unverified.

**Rule 2 — No bare numbers without a fetched source.**
Any specific figure — founding year, acquisition price, net worth, funding amount, headcount, runtime, efficiency percentage, unit count, cycle time — must trace to a URL fetched and confirmed live in this session. If a number cannot be sourced to a confirmed fetch, omit it or mark it as `(unverified estimate)`. Training-data recall of specific figures is not a substitute for a fetched source.

**Rule 3 — Leadership, ownership, and status require a current-dated source.**
"Founder," "CEO," "co-founder," "acquired by," and similar status claims require either the company's own team page or a press release fetched during this session. Leadership changes frequently; training knowledge of who runs a company is not sufficient. If no current source can be confirmed, note: "as of [last review date]; verify current status."

**Rule 4 — Named locations require a verified source.**
Any named city or facility address (headquarters, manufacturing site, lab) must be verified against a fetched source. Do not infer location from company name, brand associations, or region stereotypes.

**Rule 5 — Prefer official press releases over media coverage for funding facts.**
For funding amounts, round names, lead investors, and deal dates, prefer GlobeNewswire, BusinessWire, PRNewswire, or the company's own press release page over TechCrunch, Reuters, or WSJ. Media slugs are fragile and frequently break; official press releases at wire services are stable URLs. TechCrunch URLs may be included as secondary sources but should not be the sole source for a funding fact.

**Rule 6 — Verify all source URLs before filing.**
Before completing any entry, fetch each URL in `source_urls` and confirm it returns content. A URL that returns an empty response, 404, or JS-rendered shell without content is a dead source and must be replaced. Do not include a URL that has not returned readable content in this session.

---

### People Network Mapping

Every company entry must have a **Key People** section. For each named person include:

1. Full name and current role/title
2. LinkedIn profile URL (format: `https://www.linkedin.com/in/[slug]`) — search for the actual URL; if not findable, mark `LinkedIn: not found`
3. Google Scholar or institutional page URL if the person is a researcher
4. Public social media accounts — search for and link the person's other public professional accounts: X/Twitter, Bluesky, Mastodon, GitHub (for engineers/researchers), and personal websites/blogs. Link each with the platform named, e.g. `[X](https://x.com/handle)`, `[GitHub](https://github.com/handle)`. Only link accounts that are clearly the same person (verify via bio, company affiliation, or cross-reference with existing verified accounts like LinkedIn) — do not guess at handles. If no public account is findable for a platform, omit it rather than marking every platform as not found; only note `LinkedIn: not found` per rule 2 above since it's the primary required one.
5. Previous employers in reverse-chronological order, with approximate tenure dates
6. Overlap flag: if this person previously worked at any other company already documented in the Research section, or at a company that is a partner/investor of another documented company, call it out explicitly with a note like: "**⚑ Overlap:** Previously at [Company X] overlapping with [Person Y] (approx. [year range])"

Cross-entry overlap notes: if two or more people at different documented companies share a prior employer, add a note to both entries. Format: `**⚑ Shared background:** [Person A] (Company X) and [Person B] (Company Y) both worked at [Shared Employer] [year range if known].`

At the bottom of every Key People section include a subsection: `### People — Last Reviewed: [YYYY-MM-DD]`. Update this date whenever the section is reviewed.

Review cadence for people sections: every 180 days. Fast-moving startups: 90 days.

Source all LinkedIn, social media, and employment history information from public web searches. Do not fabricate profile URLs — if unsure, leave a TODO comment.

---

### Supply Chain & Shared Infrastructure Mapping

Every topic area landing page (`_index.md`) must include a **Supply Chain** section documenting the known chain from raw materials to finished product for that topic. Structure it as a table or ordered list with layers: Raw Materials → Precursor Chemicals → Electrolyte/Active Materials → Cell Manufacturing → Pack Assembly → OEM Integration.

For each layer, list:
- The key inputs/outputs at that layer
- The known companies operating at that layer (link to entries where they exist)
- Geographic concentration risks (e.g., "lithium: 50%+ from Chile/Argentina/Australia; processing: 60%+ China")

Shared infrastructure flags: if two or more documented companies use the same supplier, mine, manufacturing partner, or raw material source, flag it in both entries: `**⚑ Shared supplier:** [Company X] and [Company Y] both source from [Supplier].`

Create a `content/research/energy/resources/` directory with `_index.md` and individual entries for:
- Key minerals: lithium, cobalt, nickel, sulfur, manganese (one entry each)
- Key mining/processing companies supplying materials to documented battery companies
- Key precursor chemical suppliers

Entry structure for a resource/mineral page: Summary, Key Facts (chemical formula, primary uses, global production volume, top producing countries), Major Producers (company table), Supply Chain Position (how it feeds into documented technologies), Geopolitical Risk Assessment, Sources.

Review cadence for supply chain sections: 180 days.

---

### Chinese-Owned Companies

When a company entry covers a Chinese-owned entity (headquartered in mainland China or majority-owned by Chinese state or private interests):

- Add `chinese-owned: true` to the frontmatter
- Append 🇨🇳 after the company name in every table where it appears
- Note the Chinese ownership in the **Key Facts** section
- In the **Claim Verification** section, apply a higher bar for verification: prefer sources from independent Western labs, peer-reviewed journals, or credible non-Chinese media; treat company-issued figures as unverified until corroborated

---

### Topic-Area Steering: Datacenters (`research/datacenters/`)

**Scope boundaries:**
- IN: Physical datacenter infrastructure — cooling, power, construction, physical automation, rack design, connectivity hardware; companies designing, building, or operating innovative datacenter facilities
- OUT: Cloud computing software, AI model development, chip design (separate sections); routine hyperscaler earnings or campus announcements without a novel infrastructure angle
- BORDERLINE: Rack-scale compute systems (NVIDIA NVL72, HPE Cray EX) — include only when the physical infrastructure or cooling integration is the notable element, not the compute itself

**Datacenter-specific tags** (in addition to global tags):
- Subsection: `cooling`, `robotics-automation`, `design-construction`, `power-infrastructure`
- Technology: `immersion-cooling`, `direct-to-chip`, `liquid-cooling`, `air-cooling`, `blind-mate`, `prefab`, `modular`, `smr`, `fuel-cell`, `behind-the-meter`
- Segment: `hyperscaler`, `colocation`, `edge`, `hpc`, `ai-datacenter`
- Density: `high-density` (>20 kW/rack), `ultra-high-density` (>100 kW/rack)

**Key metrics to document** for cooling technologies and products: PUE (target and measured annualized — not just design); WUE (liters per kWh IT load); rack density supported (kW/rack — air tops out ~15–20 kW, liquid starts at 20 kW); coolant temperature range (supply and return); ERE (Energy Reuse Effectiveness). For construction/design entries: time to power (months greenfield to live), cost per MW (verify whether figure includes land, power infrastructure, fit-out, and redundancy — not just shell-and-core), PUE target, and total MW at full buildout.

**Claim verification flags for datacenters:** Distinguish design PUE from measured annualized PUE. For "supports X kW/rack" claims, verify that figures account for real-world fluid distribution, manifold pressure drops, and redundancy — not just tank theoretical capacity. For autonomous operation claims, establish what fraction of tasks are genuinely automated vs. still requiring human intervention. For "100% renewable" power claims, determine whether the mechanism is RECs (does not change the physical grid mix) or 24/7 matched clean power. For cost per MW claims, see metrics note above.

**Additional entry types for datacenters** (beyond the global company/technology/person/breakthrough types):
- **Design pattern**: a documented approach being adopted by multiple operators (e.g., zoned hybrid cooling)
- **Facility entry**: a specific notable datacenter with documented novel infrastructure elements
- **Standard/specification**: an industry standard relevant to infrastructure (OCP, Open19, ASHRAE thermal guidelines)

---

### Topic-Area Steering: Datacenters — Rugged & Edge Compute (`research/datacenters/rugged-edge-compute/`)

**Scope:** Rugged compute platforms designed for operation in harsh, mobile, or contested environments. In scope: server/rack-level compute for airborne, maritime, and ground vehicle deployment; man-portable and wearable AI inference platforms; VPX/OpenVPX modular compute; MOSA/SOSA-compliant systems; tactical edge AI. Out of scope: standard datacenter servers in controlled environments, consumer ruggedized laptops.

**Key terminology to document in relevant entries:**
- **SWaP / SWaP-C**: Size, Weight, and Power (plus Cost) — the fundamental constraint governing all rugged compute design trade-offs
- **MOSA / SOSA**: Modular Open Systems Approach / Sensor Open Systems Architecture — DoD acquisition policy and the specific technical standard implementing it; SOSA-aligned products are interoperable across vendors
- **VPX / OpenVPX**: VITA 65 — high-speed backplane-based modular compute form factor for rugged environments; 3U and 6U card heights
- **HPEC**: High-Performance Embedded Computing — GPU/FPGA-accelerated rugged compute for signal processing and AI inference
- **MIL-STD-810**: Environmental test standard (temperature, humidity, shock, vibration, altitude) — the benchmark for ruggedization claims; verify which revision (H is current) and which test methods were applied
- **MIL-STD-461**: EMI/EMC standard — critical for airborne and naval platforms
- **ATAK**: Android Team Awareness Kit — DoD tactical situational awareness platform; ATAK compatibility indicates field soldier/operator integration

**Platform tiers** — tag and describe entries by tier: (1) Rack/server tier (1U–4U rackmount for vehicle/aircraft/ship bays); (2) VPX module tier (individual 3U or 6U OpenVPX cards sold to prime contractors); (3) Man-portable/wearable tier (battery-powered, body-worn AI inference, typically NVIDIA Jetson Orin class, ATAK-compatible).

**AI inference metrics:** Track GPU/NPU generation (H100, H200, GB200, RTX PRO 5000 Blackwell, Jetson Orin NX/AGX) and TFLOPS/PetaOPS claims. DoD customers care about INT8/INT4 throughput for inference, not FP64 for training.

**Review cadence:** 90 days for companies with active DoD contracts; 180 days otherwise.

---

### Topic-Area Steering: Energy — Nuclear (`research/energy/nuclear/`)

**Scope:** Fission reactor designs (SMR, microreactor, advanced Gen IV), fuel cycle suppliers, construction and deployment companies, regulatory milestones. Out of scope: nuclear weapons, fusion (track separately if warranted), nuclear medicine.

**Regulatory milestones carry high weight.** NRC Design Certification, Construction Permit, Combined License (COL), and Operating License are discrete verifiable events. Document each with date, document number, and link to the NRC public docket where available. Verify licensing status claims against the NRC docket, not just company press releases.

**Timeline skepticism is essential.** Nuclear construction has a decades-long history of schedule slippage and cost overrun. When a company claims a build time dramatically shorter than industry history, document the claim, the mechanism by which they claim to achieve it, the regulatory preconditions required, and any prior examples of similar claims. Always distinguish design-stage timeline claims from NRC-approved construction schedules.

**SMR-specific flags to track per entry:**
- Reactor design type (LWR, HTGR, molten salt, sodium fast) — each has distinct licensing precedent and supply chain
- Fuel type (LEU vs. HALEU) — HALEU supply chain is a critical dependency; Centrus Energy is the only NRC-licensed US HALEU enricher
- Construction approach (modular/shipyard vs. stick-built)
- Behind-the-meter vs. grid-connected (datacenter-coupled SMRs avoid grid interconnection delays but require dedicated NRC site approvals)

**Datacenter nuclear overlap:** Document any company with a named datacenter or hyperscaler customer or LOI. Cross-reference with `research/datacenters/power-infrastructure`. Key tracked connections: Blue Energy → Crusoe (Port of Victoria TX); Kairos Power → Google (500 MW PPA by 2035); X-energy → Amazon (multiple sites). Note: NuScale's CFPP project was cancelled 2023 — document and do not treat as active.

**Nuclear-specific tags:** `smr`, `microreactor`, `gen-iv`, `haleu`, `behind-the-meter`, `shipyard-construction`, `nrc-licensed` (only after NRC Design Certification or COL is granted).

**Review cadence:** 90 days for active pre-construction companies (NRC milestones can change fast); 180 days for early-stage designs; 365 days for stable operational facilities.

---

### Topic-Area Steering: Robotics (`research/robotics/`)

**Editorial priority:** The component and subsystem layer — motors, gearboxes, LiDAR sensors, radio subsystems, battery packs — not the platform OEMs. Platform OEM entries (DJI, Boston Dynamics, etc.) provide market context, but the more interesting entries are the materials company solving motor efficiency, the startup building a better harmonic drive, or the researcher commercializing a new LiDAR architecture.

**Value chain position** — every company entry must be tagged and described by its position:
- **Platform OEM** — sells a complete, ready-to-use robot to end customers (DJI, Boston Dynamics, Knightscope, AeroVironment)
- **Component/subsystem supplier** — sells components or subsystems to OEMs or integrators (T-Motor, Maxon, Ouster, u-blox, Silvus, Intelligent Energy)
- **Software/AI layer** — sells autonomy software that runs on hardware platforms (Shield AI Hivemind, Skydio AI stack)
- **Integrator** — assembles third-party components into custom platforms for specific verticals

When a company operates at multiple layers (e.g., DJI makes its own motors AND sells complete drones), note both roles and describe the vertical integration explicitly — it is a significant competitive moat worth documenting.

**Robotics-specific tags** (in addition to global tags):
- Platform type: `aerial-drone`, `ugv`, `amr`, `humanoid`, `surgical`, `agricultural`
- Component category: `actuator`, `sensor`, `lidar`, `radar`, `gnss`, `communications`, `battery`, `fuel-cell`, `motor`, `gearbox`
- Market: `defense`, `commercial`, `consumer`, `industrial`, `logistics`
- Technology: `bldc`, `harmonic-drive`, `slam`, `autonomous`, `swarm`, `bvlos`

**Claim verification for robotics — categories requiring scrutiny in every entry:** Endurance claims (confirm test conditions: payload, speed, altitude, temperature — quoted figures almost always assume ideal/unloaded conditions); autonomy claims ("fully autonomous," "zero operator required" — establish human-in-the-loop reality and what regulatory approvals are required and obtained, including FAA Part 107 waivers, BVLOS approvals); unit deployment figures (distinguish units sold vs. units in active service vs. cumulative lifetime deliveries); defense contract claims (verify against USASpending.gov or SAM.gov where possible — press releases routinely overstate contract scope).

**Defense and dual-use notation** for entries with significant defense business: add `defense` tag to frontmatter; note active DoD contracts and programs (public); note ITAR or EAR implications for export; if a UAS platform appears on the Blue UAS framework (DoD-approved drone procurement list), note explicitly — it is a material commercial differentiator in the US government market. For defense UGV programs, reference the relevant Army program office (DEVCOM GVSC, PEO Soldier) when documenting contracts.

**DJI specifically:** DJI is on the US DoD Chinese military company list and the FCC Covered List (as of 2022–present). The American Security Drone Act (signed 2023) prohibits US federal agencies from procuring DJI and other covered drones. Every DJI entry must prominently note these designations and their practical implications — the regulatory overhang is a material risk that must be documented.

**Rare earth dependency** is a pervasive, often underdiscussed supply chain risk throughout the robotics hardware stack. NdFeB permanent magnet BLDC and servo motors depend on neodymium and dysprosium; China controls ~85% of global rare earth mining and ~90% of processing. This affects every motor and actuator regardless of where the final robot was assembled. Note it in any motor or actuator entry.

**People network clusters in robotics** — flag connections to these origin clusters explicitly (in addition to the global people tracking format):
- Carnegie Mellon Robotics Institute (Red Whittaker field robotics lab; AMR company founders)
- MIT CSAIL and AeroAstro (drone and autonomy startups; Russ Tedrake manipulation group)
- Stanford SAIL/ME (manipulation, legged robots; DJI co-founder Frank Wang, Stanford dropout)
- iRobot alumni diaspora (wide spread after Amazon acquisition 2022)
- DJI engineering alumni (several competing drone company founders)
- DARPA PMs who funded foundational robotics programs and later joined portfolio companies — document these explicitly; the DARPA PM → company advisor/board pipeline is common and worth tracking
- Ex-Uber ATG / Waymo / Cruise / Aurora engineers moving into AMR and delivery robot startups

**Subsection review cadence:**
- Aerial drones, Ground drones, Sensors/LiDAR, Power systems: 90 days (fast-moving, regulatory changes)
- Actuators, Communications: 180 days

**What NOT to include (robotics-specific):** Hobbyist or purely recreational products with no commercial or professional market relevance; "announced" products with no hardware prototype publicly demonstrated (document announcement date, mark Key Facts status as "Announced / Undemonstrated"); AV companies not primarily in the robotics market (Waymo, Cruise, Mobileye — separate AV section); humanoid robots (track in dedicated `humanoid/` subsection when the area warrants it — do not fold into ground-drones); traditional fixed-factory industrial robot arms (FANUC, Kuka, ABB, Yaskawa) — incumbents table only; simulation software platforms (Isaac Sim, Gazebo) — context but not primary entries.

---

### What NOT to Include

- Opinion or advocacy ("X is the future of energy")
- Speculation without attribution — analyst forecasts are fine if attributed
- Press release language — rewrite corporate claims in neutral voice
- Unverified statistics — every number needs a source URL; omit if unsourceable
- Content that belongs in `content/posts/` (essays, commentary, personal takes)
- Personal contact information for individuals
- Thin entries for subjects with no meaningful public information

---

### Main Research Page — Topic Area Listing

The main Research page (`content/research/_index.md`) contains a bulleted list of all topic areas, **sorted alphabetically**. This list is automatically generated / manually maintained. When a new topic area is created:

1. Add a new directory under `content/research/` (e.g., `content/research/new-topic/`)
2. Create `content/research/new-topic/_index.md` with full steering and metadata (see template above)
3. Add the new topic to the main Research page list in alphabetical order

**Format for main page topic listing:**

The actual topic listing appears below the closing shortcode, under the `## Topic Areas` heading. Maintain it in strict alphabetical order by topic name. Update it whenever a topic area is added or renamed.

{{</steering>}}

# Research

A living, AI-maintained knowledge base on emerging technology topics. Each area collects structured profiles of technologies, companies, and people driving change.

---

**[📋 View Changelog]({{< relref "changelog/index.md" >}})** — Track recent additions and updates to the knowledge base.

## Topic Areas

- [AI Accelerators]({{< relref "ai-accelerators/_index.md" >}}) — GPU and AI accelerator hardware: AMD Instinct, rack-scale systems, interconnect ecosystems
- [Datacenters]({{< relref "datacenters/_index.md" >}}) — Physical datacenter infrastructure: cooling, power, construction, rugged edge compute
- [Drone Detection]({{< relref "drone-detection/_index.md" >}}) — C-UAS detection methods, hardware, open-source tools, and counter-drone platforms for critical infrastructure protection
- [Energy]({{< relref "energy/_index.md" >}}) — Solar, batteries, nuclear, and energy resources
- [Large Format Additive Manufacturing (LFAM)]({{< relref "lfam/_index.md" >}}) — Industrial-scale 3D printing: gantry and robotic pellet extrusion, WAAM for metal naval components, defense and aerospace applications
- [Local LLM Fine-Tuning]({{< relref "local-llm-finetuning/_index.md" >}}) — Building and fine-tuning specialist LLMs for edge deployment: training data, compute options, and network engineer expert models
- [Post-Quantum Encryption]({{< relref "post-quantum-encryption/_index.md" >}}) — NIST PQC standards adoption across networking hardware and cryptocurrency infrastructure
- [Quantum Computing]({{< relref "quantum-computing/_index.md" >}}) — Quantum computing hardware, software, and the race toward practical quantum advantage
- [Relocation Research]({{< relref "relocation/_index.md" >}}) — City and county relocation profiles evaluated against a consistent set of livability criteria, benchmarked to coastal South Carolina
- [Robotics]({{< relref "robotics/_index.md" >}}) — Robotics platforms, sensors, actuators, and autonomy software; includes [Humanoid Robots]({{< relref "robotics/humanoid/_index.md" >}}) subsection (US and non-US companies, autonomy claims, specialized robot debate)
- [Semiconductors]({{< relref "semiconductors/_index.md" >}}) — Fabrication equipment, materials, and supply chain enabling advanced node chip manufacturing
- [Software Philosophy]({{< relref "software-philosophy/_index.md" >}}) — Foundational ideas shaping how software is designed: Unix philosophy, composability, open source, and their critics
