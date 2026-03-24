---
title: Research
date: 2026-03-23
draft: false
description: AI-maintained knowledge base on emerging technology topics.
categories:
  - Research
tags: []
---

{{< steering >}}

## Research Section — Steering Instructions

This block contains editorial and structural guidelines for AI tools maintaining the Research section. Human editors may also refer to it, but it is written primarily as a system spec for automated agents.

**Note for AI tools:** This entire steering block is wrapped in `{{</* steering */>}}` / `{{</* /steering */>}}` shortcode tags. This shortcode renders nothing to the Hugo output — the content is invisible on the live site but fully present in the source file for tool access. Any file that contains AI steering instructions should use the same pattern: wrap them in `{{</* steering */>}}...{{</* /steering */>}}` rather than `<details>` or HTML comments.

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

```
content/research/
  _index.md                      ← this file (section landing)
  energy/
    _index.md                    ← topic area landing
    solar/
      _index.md                  ← subtopic landing
      first-solar.md             ← company entry
      perovskite-cells.md        ← technology entry
      mark-liu.md                ← person entry
    batteries/
      _index.md
      catl.md
      solid-state-overview.md
```

**Naming rules:**
- All filenames: lowercase, hyphenated, no special characters.
- People: `firstname-lastname.md`. For disambiguation, append field: `john-smith-solar.md`.
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
tags: ["solar", "thin-film", "us"]
categories: ["company"]       # person | company | technology | breakthrough | overview
research_area: "energy/solar"
source_urls:
  - "https://example.com"
last_reviewed: 2026-03-01
stale_after_days: 180
---
```

Required fields: `title`, `date`, `lastmod`, `draft`, `description`, `tags`, `categories`, `research_area`, `source_urls`, `last_reviewed`.
Optional but encouraged: `stale_after_days` (default 180 if omitted), `related` (list of relative paths to related entries).

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

---

### Tagging & Cross-Linking

**Tags:** lowercase, consistent.
- Geography: `us`, `china`, `eu`, `india`
- Technology: `solar`, `batteries`, `wind`, `nuclear`, `grid`, `ev`
- Status: `emerging`, `mature`, `discontinued`

**Cross-links:** Use Hugo relrefs where entries exist:


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
- **Chinese-owned public companies:** append `🇨🇳` after the company name and add a note that claims should be treated with additional skepticism (see below)

**Incumbents** — large, diversified public companies (automakers, conglomerates, major battery manufacturers). Include only as context; detailed entries for incumbents should be created only when there is something genuinely novel and specific to document:

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [TICK](https://finance.yahoo.com/quote/TICK) | [Company Name](https://companywebsite.com) | Why they matter to this topic area. |

- Link each company name to its official corporate or investor relations website.

Update all three tables whenever a new entry is added that introduces a new company. Do not list research institutions or universities — only commercial entities.

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

### People Network Mapping

Every company entry must have a **Key People** section. For each named person include:

1. Full name and current role/title
2. LinkedIn profile URL (format: `https://www.linkedin.com/in/[slug]`) — search for the actual URL; if not findable, mark `LinkedIn: not found`
3. Google Scholar or institutional page URL if the person is a researcher
4. Previous employers in reverse-chronological order, with approximate tenure dates
5. Overlap flag: if this person previously worked at any other company already documented in the Research section, or at a company that is a partner/investor of another documented company, call it out explicitly with a note like: "**⚑ Overlap:** Previously at [Company X] overlapping with [Person Y] (approx. [year range])"

Cross-entry overlap notes: if two or more people at different documented companies share a prior employer, add a note to both entries. Format: `**⚑ Shared background:** [Person A] (Company X) and [Person B] (Company Y) both worked at [Shared Employer] [year range if known].`

At the bottom of every Key People section include a subsection: `### People — Last Reviewed: [YYYY-MM-DD]`. Update this date whenever the section is reviewed.

Review cadence for people sections: every 180 days. Fast-moving startups: 90 days.

Source all LinkedIn and employment history information from public web searches. Do not fabricate profile URLs — if unsure, leave a TODO comment.

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
- Note the Chinese ownership explicitly in the **Key Facts** section
- In the **Claim Verification** section, apply a higher bar for verification: prefer sources from independent Western labs, peer-reviewed journals, or credible non-Chinese media; treat company-issued figures as unverified until corroborated
- Add this notice at the top of the entry body, before the Summary:

```
> **Note:** This company is Chinese-owned. Performance claims and publicly reported figures should be treated with additional skepticism until independently verified by non-affiliated third parties.
```

---

### What NOT to Include

- Opinion or advocacy ("X is the future of energy")
- Speculation without attribution — analyst forecasts are fine if attributed
- Press release language — rewrite corporate claims in neutral voice
- Unverified statistics — every number needs a source URL; omit if unsourceable
- Content that belongs in `content/posts/` (essays, commentary, personal takes)
- Personal contact information for individuals
- Thin entries for subjects with no meaningful public information

{{< /steering >}}

# Research

A living, AI-maintained knowledge base on emerging technology topics. Each area collects structured profiles of technologies, companies, and people driving change.
