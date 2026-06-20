---
title: "Public School Enrollment Trends — Relocation Cities"
date: 2026-06-18
lastmod: 2026-06-18
draft: false
description: "County-level public school enrollment by level (elementary, middle, high) for 20 US relocation candidate cities, 2010–11 through 2023–24. NCES Common Core of Data."
tags: ["relocation", "schools", "demographics", "enrollment", "education"]
categories: ["data"]
research_area: "relocation"
source_urls:
  - "https://nces.ed.gov/ccd/"
  - "https://nces.ed.gov/programs/edge/"
last_reviewed: 2026-06-18
stale_after_days: 365
---

County-level public school enrollment for 20 relocation candidate cities, drawn from the NCES Common Core of Data (CCD). Data covers 2010–11 through 2023–24 (2022–23 excluded — anomalous source file). Enrollment is segmented by level: elementary (PK–Grade 5), middle (Grades 6–8), and high school (Grades 9–12). Private schools are not included.

Demographic shifts — particularly the effects of immigration enforcement on K–12 enrollment — should be visible in the elementary tier first, with a 6–8 year lag before propagating to high school.

{{< enrollment-all >}}

{{< steering >}}
## Data Sourcing and Normalization — School Enrollment

### Source
NCES Common Core of Data (CCD), LEA-level membership files. Public schools only; private schools excluded.
- Membership files: https://nces.ed.gov/ccd/ccddata.asp
- EDGE geocode files (LEAID → county FIPS): https://nces.ed.gov/programs/edge/Geographic/SchoolLocations

Processing script: `scripts/fetch_enrollment.py`. Cached source zips: `/tmp/ccd_cache/` (not committed; re-download as needed).
Output: `data/enrollment/<fips>.json` per county. Greenville + Spartanburg merged into `data/enrollment/45045_45083.json`.

### File Format History
Two distinct formats across the time series:

**Wide format (2010–11 through 2015–16):** One row per LEA with per-grade columns PK, KG, G01–G12. County FIPS (CONUM) is embedded in files through 2013–14. Files for 2014–15 and 2015–16 lack CONUM — use EDGE geocode 1617 as a proxy (LEA boundaries are stable year-to-year).

**Long format (2016–17 through 2023–24):** One row per LEA × grade × race × sex combination. Filter to `TOTAL_INDICATOR = 'Subtotal 4 - By Grade'` to get grade-level totals without race/sex breakdown. Join to EDGE geocode file on LEAID to get county FIPS (col 8 = CONUM, pipe-delimited, no header row). File for 2021–22 is double-zipped (outer zip contains `_CSV.ZIP`). File for 2022–23 is anomalously large (~1.3 GB) and is excluded.

### Critical Bug: Grade Substring Matching
**Do not use substring matching** (`"GRADE 1" in grade`) to classify long-format grade labels. "GRADE 1" is a substring of "GRADE 10", "GRADE 11", "GRADE 12", which causes those to be misclassified as Elementary, inflating Elementary ~40% and deflating High ~70% post-2016. Use **exact set membership** instead:

```python
ELEM = {"PRE-KINDERGARTEN","PREKINDERGARTEN","KINDERGARTEN","GRADE 1","GRADE 2","GRADE 3","GRADE 4","GRADE 5"}
MID  = {"GRADE 6","GRADE 7","GRADE 8"}
HIGH = {"GRADE 9","GRADE 10","GRADE 11","GRADE 12"}
if g.strip().upper() in ELEM: return "Elementary"
```

### Grade Level Mapping
- Elementary: PK, Kindergarten, Grades 1–5
- Middle: Grades 6–8
- High: Grades 9–12
- Excluded: "Not Specified", ungraded (UG), adult education (AE), G13

### Validation Check
Total enrollment should be continuous across the 2015–16 → 2016–17 format boundary. If Elementary jumps ~40% and High drops ~70% at that boundary, the substring matching bug has been reintroduced. Austin (Travis Co) reference values:
- 2015–16: E≈85,277 M≈35,195 H≈44,373 Total≈164,845
- 2016–17: E≈85,250 M≈35,611 H≈45,281 Total≈166,142

### Known Data Gaps
- **Nashville (Davidson Co, 47037) 2023–24:** LEAID 4703180 (Davidson County Schools, ~80k students) is absent from `EDGE_GEOCODE_PUBLICLEA_2324.zip` — only 4 state-level agencies remain, making the county total meaningless. 2023–24 is excluded for Nashville; series ends at 2021–22. Check future EDGE releases to see if the LEA reappears.
- **2022–23 (all cities):** CCD LEA membership file is anomalously ~1.3 GB on the NCES server (normal size is 50–65 MB). Excluded entirely. Check periodically for a corrected file.

### Updating
Run `python3 scripts/fetch_enrollment.py` after downloading new CCD LEA membership and EDGE geocode zips to `/tmp/ccd_cache/`. New school years follow the long format. Check NCES for the new fiscal year file at:
`https://nces.ed.gov/ccd/Data/zip/ccd_lea_052_<YYYY>_l_1a_<release>.zip`
and matching EDGE file at:
`https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICLEA_<YYYY>.zip`
{{< /steering >}}
