---
title: "Relocation Research"
date: 2026-06-15
lastmod: 2026-06-18
draft: false
description: "City and county level research evaluating potential relocation destinations against a consistent set of livability criteria."
tags: ["relocation", "cities", "cost-of-living", "demographics"]
categories: ["overview"]
research_area: "relocation"
last_reviewed: 2026-06-15
stale_after_days: 180
sitemap:
  changefreq: "monthly"
  priority: 0.9
  disable: false
---

{{<steering>}}

## Relocation Research Section — Steering Instructions

This block contains editorial and structural guidelines for AI tools maintaining the Relocation Research section. It is invisible on the live site.

---

### Purpose

This section evaluates specific cities and counties as potential long-term relocation destinations. Each entry applies a consistent set of criteria so areas can be compared against each other and against the baseline of coastal South Carolina (the Myrtle Beach / Grand Strand area, approximately). The baseline is used for relative cost comparisons unless otherwise noted.

This is personal research for a potential long-distance relocation with a long time horizon. Entries should be honest, data-driven, and frank about risks — including structural risks (water, power, climate) that most relocation content glosses over.

---

### Evaluation Criteria

Every entry must address all of the following criteria, in this order. Use H2 headings for each.

1. **Cost of Living** — overall index vs. national average; housing (buy and rent); key cost drivers. Compare to coastal SC (Myrtle Beach area ~90 index, median home ~$320K).

2. **Demographics & Trends** — current population (city and metro); 10-year trend; in-migration vs. out-migration; age distribution; key demographic shifts to watch.

3. **Crime** — violent and property crime rates vs. national average; 5-year trend (improving / worsening / flat); neighborhood-level variation context.

4. **Major Employers & Tech Ecosystem** — top 10 employers; tech company presence (established + branch offices); startup culture assessment (VC presence, accelerators, notable exits); remote work infrastructure.

5. **Small Business Climate** — state-level business taxes; state income tax and corporate tax; sales tax; county/city regulatory posture; specific incentive programs; overall friendliness ranking if available.

6. **Utilities & Infrastructure**
   - **Power:** Who supplies it, what % renewable vs. fossil, grid reliability history, extreme weather vulnerability, interconnection to national grid (or isolation like ERCOT).
   - **Water:** Primary water source(s); current supply adequacy; drought risk; aquifer dependency; long-term growth vs. supply projections.
   - **Internet:** Fiber availability; major providers; typical speeds.

7. **Environmental & Natural Hazard Profile** — wildfire, flood, earthquake, tornado, hurricane, extreme heat, extreme cold; historical frequency; projected climate change impacts by 2050; FEMA risk index if available.

8. **Long-Term Growth Limiting Factors** — structural forces that could cap quality of life or economic vitality: water table, aquifer depletion, air quality deterioration, traffic, housing supply constraints, state/local political instability, federal funding dependency, etc.

9. **Firearms & Self-Defense Laws** — concealed carry (permit required vs. permitless/constitutional carry); open carry rules; purchase requirements (background check, waiting period, permit-to-purchase); registration or reporting requirements; magazine capacity restrictions; assault weapon or semi-automatic restrictions; red flag / extreme risk protection order (ERPO) laws; notable ongoing litigation or recent legislative changes. Compare to coastal SC baseline (constitutional carry since March 2024, no registration, no magazine limits, no red flag law, lost/stolen handgun reporting required within 10 days).

10. **Relocation Factors** — anything else materially relevant to a person relocating long-term: airport access, healthcare quality, cultural fit, outdoor recreation, political environment, school quality (if applicable), notable downsides not captured above.

11. **Local Flavor** — quality-of-life and cultural texture subsections. Every entry must include all of the following using H3 subheadings, in this order:

    - **Cat Cafes** — dedicated cat cafes in the metro; if none exist, note that and describe the closest alternative.
    - **Coffee** — noteworthy independent coffee shops; flagship roasters; notable coffee culture; avoid chain-only listings.
    - **Bookstores** — independent bookstores; used book shops; specialty or notable stores.
    - **Furniture Consignment** — established furniture consignment and upscale secondhand shops.
    - **Healthcare** — flagship hospital systems; Level I trauma centers; NCI-designated cancer centers; children's hospitals; notable specialty programs.
    - **Comedy Clubs** — dedicated stand-up clubs; improv theaters; annual comedy festivals; if no dedicated venue, note the broader entertainment context.
    - **Catholic Churches** — notable parishes, cathedrals, basilicas, or historically significant churches; diocese context.
    - **Maker Spaces** — community fab labs, hackerspaces, public-access fabrication facilities; note any library makerspaces or university-affiliated community access.
    - **Seasonal Recreation** — lakes, marinas, skiing, mountains, rivers, beaches, or other geography-specific outdoor recreation within reasonable range of the city.
    - **Annual Festivals & Events** — recurring civic events: music, food, ethnic, religious, harvest, holiday (Christmas, Halloween), or signature community events; note approximate attendance where known.
    - **Tourism** — roughly how many visitors per year and primary reasons they come; economic impact if available.
    - **Event Venues** — major sports stadiums, concert halls, amphitheaters, performing arts centers, arenas; note capacity and primary tenant or use.
    - **Sports Teams & Recreation Organizations** — professional and semi-professional teams from major to obscure (including roller derby, indoor football, minor leagues); Division I college programs; orchestras, ballet, and opera companies.
    - **Motorsports** — race tracks (oval and road course), drag strips, karting facilities; sanctioned series events held locally; notable annual events; proximity to major facilities if none local.
    - **Shooting Ranges & Training Facilities** — indoor and outdoor ranges open to the public; professional training facilities; note any notable specialty (long-range, clay sports, defensive training); note state carry law context briefly.

    **Crime & Controversy — Notable Incidents** should follow Local Flavor as the final subsection before `## Sources`, using the `### Crime & Controversy — Notable Incidents` heading. This subsection covers specific recent incidents, gang activity, notable crimes, or public safety controversies not captured in the main Crime section.

---

### Frontmatter Template for Entries

```yaml
---
title: "Denver, CO — Relocation Profile"
date: YYYY-MM-DD
lastmod: YYYY-MM-DD
draft: false
description: "Relocation evaluation of Denver, Colorado."
tags: ["relocation", "colorado", "denver"]
categories: ["overview"]
research_area: "relocation"
source_urls:
  - "https://example.com"
last_reviewed: YYYY-MM-DD
stale_after_days: 365
---
```

---

### File Naming

All entries are flat files named `city-state.md` in lowercase hyphenated format:
- `denver-co.md`
- `austin-tx.md`
- `boise-id.md`

No directory bundles needed unless an entry grows large enough to warrant sub-pages.

---

### Entry Header Structure

Each entry begins with the disclaimer, then the evaluation criteria sections, then sources:

```
> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Cost of Living
...

## Demographics & Trends
...

## Crime
...

## Major Employers & Tech Ecosystem
...

## Small Business Climate
...

## Utilities & Infrastructure
...

## Environmental & Natural Hazard Profile
...

## Long-Term Growth Limiting Factors
...

## Firearms & Self-Defense Laws
...

## Relocation Factors
...

## Sources
...
```

---

### Baseline Reference

**Coastal SC baseline (Myrtle Beach / Grand Strand area):**
- Cost of living index: ~90 (10% below national average)
- Median home price (2025): ~$320,000
- State income tax: Yes (flat 6.4% above $17,330 in 2024, phasing down to 6% by 2026)
- No county income tax
- Property taxes: Among lowest in US (~0.5% effective rate)
- Environmental risks: Hurricane (primary), coastal flooding, occasional ice storms
- Water: Primarily surface water from the Pee Dee River basin; well water common in rural areas
- Firearms: Constitutional/permitless carry since March 2024 (age 18+); no registration; no magazine limits; no assault weapon ban; no red flag law; lost/stolen handgun reporting required within 10 days (effective December 2025); CWP still available for reciprocity purposes

When comparing cost, always note what the equivalent lifestyle would cost relative to this baseline.

---

### Review Cadence

- `stale_after_days: 365` — annual review is sufficient for most data
- Review trigger: major economic event, natural disaster, or significant policy change in the area
- On review: update housing costs, crime stats, employer list, and any infrastructure status changes

---

### Changelog Instructions

Follow the standard research section changelog rules. Log new entries and major updates to `content/research/changelog/index.md`.

{{</steering>}}

# Relocation Research

Structured evaluation of cities and counties as potential long-term relocation destinations. Each profile applies a consistent set of criteria — cost of living, demographics, crime, employers, small business climate, utilities, environmental risks, and long-term growth factors — benchmarked against coastal South Carolina as a baseline.

This is not a travel guide. The goal is an honest, data-driven read on what it would actually be like to live somewhere for the next 20 years.

## Comparison

- [US City Comparison — Crime, Diversity & Affordability]({{< relref "city-comparison.md" >}}) — Radar chart comparison of all 20 US cities on normalized safety, demographic diversity, and housing affordability scores
- [Public School Enrollment Trends]({{< relref "school-enrollment.md" >}}) — County-level K–12 public school enrollment by level (elementary, middle, high) for all 19 cities, 2010–11 through 2023–24

## Profiles

- [Albuquerque, NM]({{< relref "albuquerque-nm.md" >}}) — Low cost of living with strong Sandia/Kirtland/Intel defense-and-lab economy; serious crime, Rio Grande water stress, and seismic risk are the primary concerns
- [Austin, TX]({{< relref "austin-tx.md" >}}) — Nation's top-ranked business climate; rapid tech growth offset by ERCOT grid vulnerability and water risk
- [Charleston, SC]({{< relref "charleston-sc.md" >}}) — Most culturally compelling SC city; Boeing 787 plant (9,000 jobs), Joint Base, Port expansion, Volvo EV; NOAA gauge shows 13 inches of measured sea level rise since 1921 and 51 tidal floods in 2025; housing 40–55% above Myrtle Beach baseline
- [Charlotte, NC]({{< relref "charlotte-nc.md" >}}) — Most direct SC alternative; #2 US city for corporate HQs; 2nd-largest US banking center; major aviation hub (CLT); above-average crime and banking sector concentration are the primary risks
- [Chattanooga, TN]({{< relref "chattanooga-tn.md" >}}) — Zero income tax; EPB gigabit fiber + IonQ quantum center partnership; VW EV plant retooling; outstanding outdoor access; elevated crime and 9.25% sales tax are the primary offsets
- [Cincinnati, OH]({{< relref "cincinnati-oh.md" >}}) — Eight Fortune 500 HQs including P&G and Kroger; 84.51° data science anchor; strong affordability; Over-the-Rhine urban revival; Duke Energy reliability and Ohio River flooding are the key concerns
- [Columbus, OH]({{< relref "columbus-oh.md" >}}) — Intel $28B fab investment as growth catalyst; OSU anchor; strong cost-to-employment ratio for a Midwest tech market; cold winters and highest property taxes in the series are the tradeoffs
- [Denver, CO]({{< relref "denver-co.md" >}}) — Mountain West tech hub with strong startup scene; water stress and population growth plateau emerging
- [El Paso, TX]({{< relref "el-paso-tx.md" >}}) — Cheapest large city in the series; surprisingly safe; on Western grid not ERCOT; severe heat/dust and slow population growth are the tradeoffs
- [Greenville-Spartanburg, SC]({{< relref "greenville-spartanburg-sc.md" >}}) — Southeast's most established advanced manufacturing corridor (BMW/Michelin/GE Aviation); identical SC tax and gun laws to coastal baseline; lowest coastal/storm environmental risk in the series; not a commercial software hub
- [Herndon, VA (Northern Virginia)]({{< relref "herndon-va.md" >}}) — Deepest defense/intel/cyber job market in the series; Amazon HQ2 anchor; very low crime and top schools; highest cost in the series and significant gun restrictions
- [Huntsville, AL]({{< relref "huntsville-al.md" >}}) — Highest defense/aerospace/national security tech density per capita of any small US market; DC-level cleared salaries at Alabama costs; Dixie Alley tornado risk and PFAS water issue are key concerns
- [Miami, FL]({{< relref "miami-fl.md" >}}) — International financial and Latin American tech hub; no state income tax; sea level rise already measurable and insurance crisis are the defining long-term structural risks
- [Mobile, AL]({{< relref "mobile-al.md" >}}) — Among the cheapest large cities in the series; constitutional carry; Airbus and Austal shipbuilding anchors; population decline and Gulf hurricane/flood risk are the primary concerns
- [Nashville, TN]({{< relref "nashville-tn.md" >}}) — No income tax, abundant water, strong TVA grid; healthcare capital of the US; Dixie Alley tornado risk and severe traffic congestion are the primary concerns
- [New Orleans, LA]({{< relref "new-orleans-la.md" >}}) — Unmatched culture and cuisine; constitutional carry; below-sea-level geography makes flood vulnerability and insurance crisis the defining structural risks
- [Panama City, Panama]({{< relref "panama-city-panama.md" >}}) — **International entry.** USD economy, territorial taxation on foreign income, no hurricane risk, Johns Hopkins-affiliated hospital, Pensionado discounts; FATCA banking friction, restrictive gun laws, dengue risk, and US federal taxes still apply regardless of residence
- [San Antonio, TX]({{< relref "san-antonio-tx.md" >}}) — Strong value among Texas metros; deep military/cybersecurity economy (JBSA); Edwards Aquifer in active depletion crisis
- [Savannah, GA]({{< relref "savannah-ga.md" >}}) — Port of Savannah + Hyundai Metaplant ($7.6B) + Gulfstream Aerospace triple anchor; Georgia income tax declining toward 4.99%; 77% of buildings at significant flood risk and elevated crime are the defining concerns
- [Seattle, WA]({{< relref "seattle-wa.md" >}}) — Tier-1 tech market (Amazon/Microsoft HQ); no state income tax; Cascadia subduction zone earthquake risk, high housing costs, and restrictive gun laws are the key concerns
- [Tampa, FL]({{< relref "tampa-fl.md" >}}) — Leading Florida tech market outside Miami; KnowBe4 and ReliaQuest cybersecurity anchors; no state income tax; post-2024 dual-hurricane season (Helene + Milton) and rising insurance costs are the defining concerns
