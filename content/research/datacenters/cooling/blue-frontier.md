---
title: "Blue Frontier"
date: 2026-07-18
lastmod: 2026-07-18
draft: false
description: "Boca Raton, FL liquid-desiccant air conditioning company (NREL spinout, 2017) whose ESEAC/BF-DOAS technology combines dehumidification, evaporative cooling, and built-in thermal energy storage — a datacenter-adjacent waste-heat-driven cooling technology with no named data-center deployment confirmed as of this review."
research_area: "datacenters/cooling"
source_urls:
  - "https://bluefrontierac.com/"
  - "https://www.technologyreview.com/2023/10/04/1080128/2023-climate-tech-companies-blue-frontier-air-conditioning-energy-storage-climate-technology/"
  - "https://www.coolingpost.com/world-news/bill-gates-joins-20m-investment-in-efficient-ac-concept/"
  - "https://www.facilitiesdive.com/news/desiccant-based-storage-system-nearly-halves-cooling-bills-in-trials/759499/"
  - "https://www.theinvadingsea.com/2024/04/17/blue-frontier-air-conditioning-electricity-global-warming-boca-raton-startup-climate-technology/"
last_reviewed: 2026-07-18
stale_after_days: 90
related:
  - "datacenters/cooling/mojave-energy-systems.md"
  - "datacenters/cooling/_index.md"
  - "datacenters/power-infrastructure/_index.md"
  - "datacenters/distributed-compute/model-for-disco-compute.md"
  - "atmospheric-water-generation/uravu-labs.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Blue Frontier is a Boca Raton, Florida company (founded 2017, exclusively licensing technology developed at the National Renewable Energy Laboratory since 2018) that has commercialized a liquid-desiccant, thermally-driven air conditioner — marketed as ESEAC (Energy Storing and Efficient Air Conditioner) in NREL/DOE materials and BF-DOAS as a packaged commercial product — that separates dehumidification from sensible cooling and stores energy in concentrated brine rather than batteries. Its regeneration process runs on heat rather than electricity, which is the same underlying mechanism [Mojave Energy Systems]({{< relref "mojave-energy-systems.md" >}}) and [Uravu Labs]({{< relref "../../atmospheric-water-generation/uravu-labs.md" >}}) apply to datacenter waste-heat reuse — but unlike those two companies, Blue Frontier has not, as of this review, disclosed a named data-center customer, pilot, or product line; its documented deployments are in commercial, institutional, and defense buildings.

## Key Facts

- **Founded:** 2017; obtained an exclusive license to the underlying liquid-desiccant technology from the National Renewable Energy Laboratory (NREL) in 2018
- **Type:** Company (private)
- **Status:** Active — commercial BF-DOAS units deployed at multiple sites; NREL-led field validation ongoing as of September 2025
- **HQ:** Boca Raton, FL (earlier press describes the company as based in nearby Parkland, FL, as of 2022)
- **Core technology:** Liquid-desiccant dehumidification (a salt-solution desiccant absorbs atmospheric moisture) combined with two-step, single-channel double-indirect evaporative cooling; the desiccant's high-concentration state is thermally regenerated (via a heat pump in the current product) and can be stored without refrigeration, decoupling energy input from cooling delivery and enabling several hours of "cooling from storage" with no compressor draw during peak hours
- **Key metric(s):** Company claims up to 90% reduction in non-fan air-conditioning electricity use and 85% reduction in refrigerant global-warming-potential impact; an independent NREL-modeled year-long Miami simulation of a 20-ton ESEAC system found 38% reduction in cooling-related electricity use, 93% reduction in peak demand, and 45% reduction in annual electricity cost (≈$165,000 savings per unit over 15 years)
- **Funding:** At least $26M raised through grants, prizes, seed funding, and a $20M Series A (July 2022, co-led by Bill Gates' Breakthrough Energy Ventures, the 2150 Urban Tech Sustainability Fund, and VoLo Earth Ventures, with commercialization partner Modern Niagara participating) as of an October 2023 review. Multiple secondary aggregators (Tracxn, PitchBook-style trackers) reference a subsequent ~$16.9M strategic/Series B-class round around December 2023–February 2024 and cumulative funding in the $36–48M range, but a direct primary source for this later round could not be successfully fetched and read during this session — treat the post-2023 funding total as **unverified** pending confirmation.

## What It Is / How It Works

Blue Frontier licenses and commercializes a liquid-desiccant air-conditioning cycle originally developed at NREL, continuing joint development with NREL and (in earlier stages) Oak Ridge National Laboratory and the Wells Fargo Innovation Incubator (IN2) program. The system uses a salt-solution liquid desiccant to strip moisture from incoming air; because that dehumidification step is separated from sensible cooling, the dried air can then be cooled by a two-step, single-channel double-indirect evaporative process (isothermal dehumidification followed by evaporative cooling) rather than a conventional refrigerant compressor cycle for cooling, reaching supply temperatures in the 55–60°F range independent of ambient humidity.

The distinguishing feature — and the reason NREL and DOE materials refer to it as ESEAC, an *Energy Storing* and Efficient Air Conditioner — is that the concentrated, moisture-absorbing desiccant state can be produced and stored ahead of when cooling is actually needed. A heat pump regenerates (concentrates) the desiccant, typically overnight or whenever electricity is cheapest or renewable generation is most available; the concentrated desiccant and the water it releases are then stored separately, and during peak afternoon hours the system runs the discharge cycle — delivering full cooling and dehumidification with no compressor operating and minimal grid draw. Company materials describe this storage as costing roughly a tenth as much as battery-based thermal storage, since it uses only saltwater and water rather than manufactured battery cells. Blue Frontier states its heat-pump regeneration step reaches a coefficient of performance in the 5–7 range (versus 3–3.5 for conventional DX units) and that combined system-level COP ranges from about 11 to over 50 depending on climate, corresponding to the company's claimed 60–90%+ electricity-use reduction. Because regeneration is thermally driven, the system becomes more efficient — not less — as outdoor temperature rises, the inverse of a conventional compressor's behavior under high compressor lift.

Blue Frontier's technology is directly relevant to this section's datacenter waste-heat theme for the same reason as Mojave's AquaDry and Uravu Labs' Clausius platform: any process that regenerates a liquid desiccant with low-grade heat is, in principle, a candidate to run on datacenter waste heat instead of (or supplementing) a dedicated heat pump. However, **this connection is inferential rather than documented** — none of the company's own materials, its NREL/DOE partnership announcements, or its named installation list (below) mention a data-center application, waste-heat feedstock, or data-center customer as of this review. This distinguishes Blue Frontier from Mojave, whose marketing explicitly names data centers as a target application, and from Uravu Labs, whose current positioning is built entirely around data-center waste heat.

Documented deployments to date are in commercial, institutional, and defense buildings: Barry University and Indian Rocks (a community center) in Florida, a Waffle House location in Macon, GA, an office building in Riviera Beach, FL with on-site solar integration, an IMAX theater at the Museum of Discovery and Science (FL), Valencia College, Jackson Memorial Hospital, and multiple U.S. Army and Air Force bases (including Westover Air Reserve Base, per an on-site mechanical engineer's testimonial). Blue Frontier's ESEAC was also one of 17 technologies evaluated under the DOE/GSA Green Proving Ground program, and its BF-DOAS product won AHR Expo's 2026 Product of the Year award and a 2025 R&D 100 Award; a third-party field study by UC Davis under the CalNEXT program independently evaluated real-world performance and peak load-shifting.

## Notable Developments

- **2026-02:** BF-DOAS named 2026 AHR Expo Product of the Year.
- **2025-09:** NREL announced year-long Miami simulation results for a 20-ton ESEAC system (38% cooling-electricity reduction, 93% peak-demand reduction, 45% annual cost reduction, ~$165,000/unit savings over 15 years) and listed active/planned deployments at an IMAX theater, U.S. Army and Air Force bases, Barry University, Valencia College, and Jackson Memorial Hospital.
- **2025 (unspecified):** ESEAC/BF-DOAS won a 2025 R&D 100 Award.
- **2024 (unspecified):** ESEAC one of 17 technologies evaluated in the DOE/GSA Green Proving Ground program; UC Davis CalNEXT program independently field-evaluated BF-DOAS performance.
- **2023-12 / 2024-02 (unverified — secondary sources only):** Multiple funding-tracker sites reference a ~$16.9M strategic funding round in this window; not independently confirmed via a primary source during this review.
- **2023-10:** MIT Technology Review named Blue Frontier to its "15 Climate Tech Companies to Watch" list, reporting at least $26M raised to date and field tests of two units with plans for ~40 units the following year.
- **2022-07:** Closed $20M Series A co-led by Breakthrough Energy Ventures, 2150 Urban Tech Sustainability Fund, and VoLo Earth Ventures, with commercialization partner Modern Niagara participating.
- **2018:** Obtained exclusive license to the underlying liquid-desiccant AC technology from NREL.
- **2017:** Company founded.

## Key People

### Daniel Betts, Ph.D. — CEO and Co-Founder
- **LinkedIn:** [danielbetts](https://www.linkedin.com/in/danielbetts/)
- **Background:** Ph.D. in Mechanical Engineering/thermal sciences and MBA (University of Florida), B.S. Mechanical Engineering (George Washington University); in energy technology since 1997; immediately prior to Blue Frontier was CEO and CTO of **Be Power Tech**, an advanced air-conditioning and distributed-power company, and President of **EnerFuel** (an Ener1 subsidiary developing next-gen batteries and fuel cells); has consulted for Jabil Circuit, Research Triangle Institute, and multiple automotive/engine/materials-handling OEMs.
- **⚑ Shared background:** Betts, CTO **Matt Tilghman**, and VP Engineering **Matt Graham** all previously worked together at **Be Power Tech** and/or **EnerFuel**, and Tilghman additionally overlapped with **Phil Farese** (CEO of [Mojave Energy Systems]({{< relref "mojave-energy-systems.md" >}})) at **Advantix Systems** — Blue Frontier's founding team and Mojave's CEO both trace through the same small cluster of prior liquid-desiccant/waste-heat HVAC companies (Advantix Systems, Be Power Tech, EnerFuel), even though Blue Frontier and Mojave are unaffiliated, direct competitors today.

### Matt Tilghman, Ph.D. — Chief Technology Officer
- **LinkedIn:** [matt-tilghman-071a5143](https://www.linkedin.com/in/matt-tilghman-071a5143/)
- **Background:** B.S. (Princeton University), Ph.D. in thermodynamics/heat transfer (Stanford University); prior to Blue Frontier worked at **Advantix Systems** (lead thermodynamicist/experimentalist, benchmarking and validating liquid-desiccant system performance) and then **Be Power Tech** (Principal Engineer, managing system architecture, controls, modeling, and testing of a liquid-desiccant air conditioner powered by generator waste heat — direct prior experience with waste-heat-driven liquid desiccant regeneration, the same mechanism relevant to a hypothetical datacenter application).
- **⚑ Overlap:** See Daniel Betts entry above — shared history with Betts and Graham at Be Power Tech/EnerFuel, and with Mojave's Phil Farese at Advantix Systems.

### Greg Tropsa — EVP of Business Development
- **LinkedIn:** [gregtropsa](https://www.linkedin.com/in/gregtropsa/)
- **Background:** B.S. (Clarkson College of Technology); founded Peak Efficiency (2013, Windsor, CO), aggregating energy-efficiency and peak-load-management technology into utility-scale demand resources; co-founded and served as President of **Ice Energy** (2003), commercializing behind-the-meter thermal energy storage under long-term utility contracts across 25 utilities, including a 53 MW distributed energy-storage contract; co-founded MegaEnergy (1998, stranded natural-gas asset monetization); earlier held sales/service leadership roles at Honeywell's Industrial Process Control Division, Industrial Dynamics, and Cutler Hammer.

### Matt Graham — VP of Engineering
- **LinkedIn:** [jouleinjected](https://www.linkedin.com/in/jouleinjected/)
- **Background:** B.S. Mechanical Engineering (University of Maryland, College Park); has designed liquid-desiccant air conditioners since 2013, starting at **Be Power Tech**; before that was Director of Product Development at **EnerFuel**, leading fuel-cell-stack cost reduction and a high-efficiency propane-fed fuel-cell telecommunications backup power program; focuses at Blue Frontier on material investigation, mechanical design, and fluid analysis of the system's heat/mass-exchange (HMX) devices and IP development.
- **⚑ Overlap:** See Daniel Betts entry above — shared history with Betts and Tilghman at Be Power Tech/EnerFuel.

### People — Last Reviewed: 2026-07-18

## Claim Verification

### Claim: "Blue Frontier's technology is applicable to datacenter waste-heat-driven cooling"
**Status:** Unverified / Not company-documented

**Supporting sources:** None found in company materials. The inference rests on the general mechanism (thermally-regenerated liquid desiccant, same class of technology as Mojave's AquaDry and Uravu Labs' Clausius platform, both of which explicitly target data centers) rather than any Blue Frontier statement.

**Refuting / questioning sources:** Blue Frontier's own site, press page, NREL/DOE partnership announcements (through September 2025), and its list of named deployments (Barry University, Indian Rocks, Waffle House, an office building, an IMAX theater, Valencia College, Jackson Memorial Hospital, and military bases) contain no mention of data centers, waste heat as a regeneration source, or any data-center customer.

**Summary:** Unverified. This is a reasonable technology-adjacency observation for cross-linking purposes (the same liquid-desiccant-plus-thermal-regeneration mechanism applies), not a documented company claim or deployment — treat any suggestion that Blue Frontier is "working on" datacenter waste-heat systems as unconfirmed until a primary company or NREL/DOE source states it directly.

### Claim: "ESEAC reduces peak AC power demand by up to 90% and electricity use for cooling by up to 45–90%"
**Status:** Partially verified

**Supporting sources:**
- [Cooler Buildings, Stronger Grid (NREL, Sept 2025), as reported by Facilities Dive](https://www.facilitiesdive.com/news/desiccant-based-storage-system-nearly-halves-cooling-bills-in-trials/759499/) — an NREL-run, year-long simulation (not company self-report) of a 20-ton ESEAC system in Miami found 93% peak-demand reduction, 38% cooling-electricity-use reduction, and 45% annual-cost reduction — independently corroborating the peak-demand and cost-savings figures, though at a lower cooling-electricity-reduction figure (38%) than the company's own top-line "up to 90%" claim
- [Blue Frontier homepage](https://bluefrontierac.com/) — company states COP ranging ~11 to >50 across climates, corresponding to 60–90%+ energy reductions, with the lower end for humid climates and the higher end for arid climates

**Refuting / questioning sources:** The NREL-simulated 38% cooling-electricity reduction is substantially lower than the company's headline "up to 90%" figure, though NREL's own framing describes the same underlying dataset as supporting "cutting peak air conditioning power demand by more than 90%" — the two figures describe different quantities (peak demand vs. total cooling energy use) and should not be conflated.

**Summary:** The 90%+ figure applies specifically to peak power demand, which is independently corroborated by NREL's own simulation; broader energy-use-reduction claims (60–90%) are climate-dependent per the company's own disclosure and were validated at the lower end (38%) in the one independent simulation reviewed. Treat headline percentages as needing the specific metric (peak demand vs. total energy vs. cost) and climate specified before comparing across sources.

## Sources

- [Blue Frontier homepage](https://bluefrontierac.com/) — technology explanation, COP figures, team bios and LinkedIn links, named deployments, awards. Fetched 2026-07-18.
- [2023 Climate Tech Companies to Watch: Blue Frontier (MIT Technology Review, Oct 4, 2023)](https://www.technologyreview.com/2023/10/04/1080128/2023-climate-tech-companies-blue-frontier-air-conditioning-energy-storage-climate-technology/) — founding year (2017), HQ (Boca Raton), NREL licensing, cumulative funding as of Oct 2023, technology explanation. Fetched 2026-07-18.
- [Bill Gates joins $20m investment in efficient AC concept (Cooling Post, Jul 29, 2022)](https://www.coolingpost.com/world-news/bill-gates-joins-20m-investment-in-efficient-ac-concept/) — Series A investor detail, 2018 NREL exclusive license date, Parkland FL HQ (2022), ORNL/IN2 program partners. Fetched 2026-07-18.
- [Desiccant-based storage system nearly halves cooling bills in trials (Facilities Dive, Sept 8, 2025)](https://www.facilitiesdive.com/news/desiccant-based-storage-system-nearly-halves-cooling-bills-in-trials/759499/) — NREL Miami simulation results, named deployments, Green Proving Ground program, CTO quote. Fetched 2026-07-18.
- [Blue Frontier's air-conditioning technology uses global warming as its solution (The Invading Sea, Apr 17, 2024)](https://www.theinvadingsea.com/2024/04/17/blue-frontier-air-conditioning-electricity-global-warming-boca-raton-startup-climate-technology/) — Boca Raton HQ (2024), Daniel Betts quotes, no data-center mention (used to establish absence of datacenter claim as of this date). Fetched 2026-07-18.
