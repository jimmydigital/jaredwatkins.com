---
title: "Mojave Energy Systems"
date: 2026-07-18
lastmod: 2026-07-18
draft: false
description: "Sunnyvale, CA liquid-desiccant HVAC company (Xerox PARC spinout, 2022) whose ArctiDry/AquaDry product line names data centers as a target application — using building chilled water plus 110–180°F waste heat to cut chiller load and improve efficiency."
research_area: "datacenters/cooling"
source_urls:
  - "https://www.globenewswire.com/news-release/2026/05/12/3292920/0/en/Mojave-Energy-Systems-Launches-AquaDry.html"
  - "https://mojavehvac.com/"
  - "https://mojavehvac.com/leadership/"
  - "https://mojavehvac.com/about/"
  - "https://serdp-estcp.mil/projects/details/d3805f90-f29b-409a-b5c3-262be296cd18/improved-moisture-control-with-less-energy-mojave-liquid-desiccant-air-conditioning"
  - "https://www.facilitiesdive.com/news/air-conditioning-efficiency-electricity-costs-liquid-desiccant-mojave-energy-systems/736051/"
  - "https://pulse2.com/mojave-energy-systems-profile-phil-farese-interview/"
last_reviewed: 2026-07-18
stale_after_days: 90
related:
  - "datacenters/cooling/blue-frontier.md"
  - "datacenters/cooling/_index.md"
  - "datacenters/power-infrastructure/_index.md"
  - "datacenters/distributed-compute/model-for-disco-compute.md"
  - "atmospheric-water-generation/uravu-labs.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Mojave Energy Systems is a Sunnyvale, California liquid-desiccant HVAC company, spun out of Xerox PARC in October 2022, that sells the ArctiDry family of dehumidification/air-conditioning products. Its newest product, AquaDry (announced May 2026, also referred to internally as ArctiDry Hydro), is a hydronic liquid-desiccant air handler explicitly designed to regenerate from low-grade waste heat and lists data centers among its named target facility types — positioning Mojave as a direct, if not yet independently verified at data-center scale, supplier into the datacenter waste-heat-reuse theme tracked in this section (see [Datacenter Power Infrastructure]({{< relref "../power-infrastructure/_index.md" >}}) and the waste-heat analysis in [Model for DisCo Compute]({{< relref "../distributed-compute/model-for-disco-compute.md" >}})).

## Key Facts

- **Founded:** October 2022, as a spinout from Xerox's Palo Alto Research Center (PARC), where the core concentrated-saltwater liquid-desiccant technology originated from earlier grid energy-storage research that was later repointed at HVAC
- **Type:** Company (private)
- **Status:** Active — shipping ArctiDry DX since early 2024; AquaDry/ArctiDry Hydro announced May 12, 2026, shipping late 2026
- **HQ:** Sunnyvale, CA (corporate office and lab); manufacturing in Anderson, SC
- **Core technology:** Patented liquid-desiccant (lithium chloride) system that independently controls dew point and dry-bulb temperature; ArctiDry DX pairs a variable-speed DX system with liquid-desiccant dehumidification, while AquaDry/ArctiDry Hydro is fully hydronic, regenerating the desiccant with a building's own low-temperature hot water (110–180°F / 43–82°C) rather than a dedicated heat source
- **Key metric(s):** ArctiDry DX claims 30–60% (up to 11 lb/kWh ISMRE) energy savings versus conventional DOAS; AquaDry claims a 20% overall efficiency improvement, with each 6°F rise in chilled-water setpoint recovering ~12% chiller capacity and ~18% efficiency; DoD SERDP demonstration targets >9 lb/kWh integrated seasonal moisture removal efficiency and <24-month simple payback
- **Funding:** $9.5M Series A closed Q3 2024 (co-led by returning investors Fifth Wall and At One Ventures, with Myriad Venture Partners, Starshot Capital, and Alumni Ventures Group returning and Earth Venture Capital new), bringing cumulative funding to $25.6M per CEO Phil Farese; a 2023 seed round was co-led by Fifth Wall and At One Ventures with participation from Xerox Ventures (now Myriad Venture Partners) — a direct equity link back to the PARC parent
- **Other funding:** $2.6M DOE Office of Energy Efficiency and Renewable Energy award (September 2023, part of a $61M multi-project EERE tranche), funding a two-phase NREL manufacturing-scale-up and field-demonstration partnership

## What It Is / How It Works

Mojave's technology traces to Xerox PARC research into concentrated-saltwater energy storage; when the original grid-storage application didn't find a market, the PARC team redirected the same concentrated-brine chemistry toward liquid-desiccant air conditioning, where it could independently strip humidity from air (via the desiccant's hygroscopic pull) and separately manage sensible temperature — avoiding the overcool-and-reheat cycle conventional DX systems use to control humidity. The company spun out in October 2022 with Phil Farese joining as CEO alongside product lead Aaron Meles and engineering lead Rachel Ellman.

The flagship ArctiDry DX line pairs a variable-speed direct-expansion (DX) refrigerant loop for sensible cooling with the liquid-desiccant module for latent (humidity) control, plus an optional reversible heat-pump mode for winter operation — Mojave says it is the first company to integrate liquid desiccant with a reversible heat pump. AquaDry (announced May 12, 2026; also called ArctiDry Hydro on Mojave's own site) removes the dedicated DX/heat-pump loop entirely: it runs on a building's existing chilled water (28–55°F) and low-temperature hot water (110–180°F) connections, regenerating the desiccant from whatever low-grade heat is available — including, per Mojave's press materials, waste heat, boiler hot water, or solar thermal. Because the liquid desiccant removes moisture directly rather than relying on depressed chilled-water temperatures, a building can raise its chilled-water setpoint (Mojave cites ~12% capacity and ~18% efficiency gained per 6°F of setpoint increase) without sacrificing dew-point control, freeing chiller-plant capacity for other loads.

Mojave's own marketing explicitly names **data centers** as a target application — alongside healthcare, pharmaceutical manufacturing, laboratories, and industrial manufacturing — for any facility with an existing chilled-water plant: "Improve chiller efficiency, reduce power consumption per ton, and improve PU[E]. The result is more electrical capacity available for IT load, from the same infrastructure," per the company's Data Centers application page. This is the same low-grade-heat-driven liquid-desiccant mechanism used by [Uravu Labs]({{< relref "../../atmospheric-water-generation/uravu-labs.md" >}}) for its data-center water-positive cooling pitch, and the AquaDry regeneration band (110–180°F / 43–82°C) sits at or above the 45–55°C liquid-cooling return temperatures modeled for datacenter and distributed-compute waste heat streams in [Model for DisCo Compute]({{< relref "../distributed-compute/model-for-disco-compute.md" >}}), making Mojave's hardware one of the few named commercial products actually engineered around that temperature band rather than a laboratory concept.

Separately, Mojave is demonstrating ArctiDry (the DX line, not AquaDry) at Department of War facilities under a Strategic Environmental Research and Development Program (SERDP) project (EW26-9353, anticipated completion 2028), replacing up to three existing DOAS units to directly compare humidity control, energy use, and payback in humid/marine-zone military buildings — evidence of field traction outside the data-center pitch, even though no named data-center customer has been disclosed as of this review.

## Notable Developments

- **2026-05-12:** Launched AquaDry (internally ArctiDry Hydro), a hydronic liquid-desiccant air handler delivering 25°F supply dewpoints from conventional chilled-water temperatures without glycol; explicitly named data centers, healthcare, pharma, and industrial facilities with existing chilled-water plants as target markets and touted waste-heat-compatible regeneration (110–180°F).
- **2026 (date unspecified):** Awarded a SERDP demonstration project (EW26-9353) to install ArctiDry at Department of War buildings, targeting >9 lb/kWh integrated seasonal moisture removal efficiency and <24-month simple payback; anticipated completion 2028.
- **2025 (through year):** Expanded sales partner network to nearly 30 firms across the U.S. and into Latin America; became first company to pair liquid desiccant with a reversible heat pump (ArctiDry HP); ArctiDry DX passed 100,000 field hours.
- **2024-Q4:** Closed $9.5M Series A (Fifth Wall, At One Ventures co-lead; Myriad Venture Partners, Starshot Capital, Alumni Ventures Group returning; Earth Venture Capital new), bringing cumulative funding to $25.6M; began Phase 2 of a DOE/NREL field-demonstration program across 10 pilot sites.
- **2024-10:** Awarded 7th patent covering its liquid-desiccant regenerator design.
- **2024 (early):** ArctiDry DX debuted publicly at AHR Expo in Chicago; began shipping.
- **2023-09:** Awarded $2.6M DOE EERE grant (part of a $61M multi-project tranche) for manufacturing scale-up and NREL field demonstration.
- **2023:** Closed seed round co-led by Fifth Wall and At One Ventures with Xerox Ventures (now Myriad Venture Partners) participating; launched sales partner program; began manufacturing operations in Anderson, SC.
- **2022-10:** Spun out of Xerox PARC as Mojave Energy Systems, with Phil Farese joining as CEO.

## Key People

### Phil Farese — CEO
- **LinkedIn:** [philip-farese-49a81b1](https://www.linkedin.com/in/philip-farese-49a81b1/)
- **Background:** Ph.D. in Physics (UC Santa Barbara), postdoctoral research fellow and lecturer in physics at Princeton; began his corporate career at McKinsey & Company leading a U.S. energy-efficiency project; served as Senior Energy Analyst at the National Renewable Energy Laboratory (NREL), where he learned liquid-desiccant HVAC technology; became CTO of an unnamed Florida liquid-desiccant startup (Mojave's own leadership bio identifies this as Head of R&D/CTO at **Advantix Systems**); then Chief Strategy Officer at Enphase Energy; then Research Lead/Chief of Staff to the Head of Market Intelligence at Point72 Asset Management; joined Mojave as CEO in October 2022.
- **⚑ Shared background:** Farese's prior role as CTO of Advantix Systems overlaps directly with **Matt Tilghman**, CTO of [Blue Frontier]({{< relref "blue-frontier.md" >}}), who was lead thermodynamicist/experimentalist at Advantix Systems before moving to Be Power Tech and then Blue Frontier — Mojave's and Blue Frontier's leadership both trace through the same small liquid-desiccant-HVAC engineering lineage (Advantix Systems), even though the two companies are unaffiliated and now direct competitors.

### Rachel Ellman — VP of Engineering
- **LinkedIn:** [rachel-ellman](https://www.linkedin.com/in/rachel-ellman)
- **Background:** Ph.D. in Medical Engineering and Bioastronautics (Harvard/MIT), S.B. in Aeronautics and Astronautics (MIT); spent six years at SpaceX as a life-support systems engineer and flight controller on the Crew Dragon program, serving as spacecraft operator for propulsion/thermal/life-support during the first crewed re-entry and splashdown; worked at Xerox PARC's Cleantech team (Jan 2021–Oct 2022) immediately before Mojave spun out; joined Mojave as VP of Engineering in October 2022. Named to ACHR NEWS' 2024 "40 Under 40."

### Aaron Meles — VP of Product
- **LinkedIn:** [aaronmeles](https://www.linkedin.com/in/aaronmeles/)
- **Background:** B.S. Mechanical Engineering, summa cum laude (Rose-Hulman Institute of Technology); M.S.M.E. (University of North Florida), thesis on direct methanol fuel cells for military applications; prior engineering/product roles spanning gas-turbine combustion, distributed power-generation controls, fuel cells, and HVAC; came from the HVAC industry with prior liquid-desiccant experience and was one of the founding product team members who worked with PARC to develop Mojave's original prototype. Listed as Principal Investigator on Mojave's DoD SERDP demonstration project.

### Robert Fancher — VP of Manufacturing
- **LinkedIn:** [robert-fancher-a9a87724](https://www.linkedin.com/in/robert-fancher-a9a87724/)
- **Background:** M.Eng. and B.S. in Mechanical Engineering (University of South Carolina); prior senior leadership roles at Techtronic Industries (TTI) (Sr. Director of Automation, Manufacturing Engineering, and Operational Excellence) and Husqvarna Group (General Manager, PMO Operational Excellence, Design Engineering Manager); began his career at Wilson Heating and Cooling. Joined Mojave in March 2023; based in Anderson, SC, running Mojave's manufacturing operations.

### Greg Tatro — VP of Sales
- **LinkedIn:** Not found (not independently verified during this review)
- **Background:** B.S. Electrical Engineering (University of Illinois Urbana–Champaign), MBA (Mercer University); more than 20 years in HVAC sales, including 14 years at Trane and senior sales/service roles at Valent Air Management and Greenheck Group. Appointed VP of Sales January 2026.

### People — Last Reviewed: 2026-07-18

## Claim Verification

### Claim: "AquaDry is compatible with data center chilled-water plants and reduces chiller load/improves PUE for data center facilities"
**Status:** Unverified

**Supporting sources:**
- [Mojave Energy Systems Launches AquaDry (GlobeNewswire)](https://www.globenewswire.com/news-release/2026/05/12/3292920/0/en/Mojave-Energy-Systems-Launches-AquaDry.html) — company press release names data centers among target facility types for AquaDry, citing waste-heat compatibility (110–180°F regeneration) and the 12%/18% capacity/efficiency-per-6°F figures
- [Mojave HVAC Data Centers application page](https://mojavehvac.com/) — company's own site lists Data Centers as a named application, claiming improved chiller efficiency, reduced power per ton, and improved PUE

**Refuting / questioning sources:** None found. No named data-center customer, case study, or third-party engineering validation for a data-center deployment specifically was located during this review — all figures originate from Mojave's own product marketing, and AquaDry itself was only announced May 2026 with shipments not scheduled until late 2026.

**Summary:** Unverified company claim. Data centers are a credible, named target application backed by a coherent engineering mechanism (raising chilled-water setpoint by removing latent load from the chiller), and the temperature band matches datacenter liquid-cooling return-loop temperatures documented elsewhere in this section — but as of this review there is no disclosed data-center customer, pilot, or independent performance data, only product marketing for a unit that has not yet shipped.

### Claim: "ArctiDry reduces energy use by 30–60% (up to 11 lb/kWh ISMRE) versus conventional DOAS systems"
**Status:** Partially verified

**Supporting sources:**
- [Mojave works to scale its dehumidification-driven commercial AC technology (Facilities Dive, Dec 19, 2024)](https://www.facilitiesdive.com/news/air-conditioning-efficiency-electricity-costs-liquid-desiccant-mojave-energy-systems/736051/) — cites a DOE project description independently stating Mojave's ISMRE of "over 3.5 kilograms per kilowatt-hour" (≈7.7 lb/kWh) is "nearly twice the current state of the art," offering 40–60% DOAS energy-use reduction with ~16-month typical paybacks — a third-party (DOE) figure, not just company marketing
- [Improved Moisture Control with Less Energy (SERDP project page)](https://serdp-estcp.mil/projects/details/d3805f90-f29b-409a-b5c3-262be296cd18/improved-moisture-control-with-less-energy-mojave-liquid-desiccant-air-conditioning) — a DoD-funded demonstration targeting >9 lb/kWh, with success measured via pre/post-retrofit monitoring rather than company self-report

**Refuting / questioning sources:** None found questioning the mechanism; however, the higher-end "up to 11 lb/kWh" and "30–60%" figures are company-stated (via CEO interview) and have not yet been matched by the DoD field-demonstration results, which are still pending (project completion targeted 2028).

**Summary:** The efficiency mechanism and general magnitude (40–60% DOAS energy reduction) are corroborated by an independent DOE project description, which is stronger evidence than typical unverified startup marketing claims in this section — but the specific "11 lb/kWh" / "30–60%" range is company-sourced, and the DoD field data that would fully validate it is not yet available.

## Sources

- [Mojave Energy Systems Launches AquaDry (GlobeNewswire, May 12, 2026)](https://www.globenewswire.com/news-release/2026/05/12/3292920/0/en/Mojave-Energy-Systems-Launches-AquaDry.html) — AquaDry product launch, data-center application, waste-heat compatibility, CEO/VP Product quotes. Fetched 2026-07-18.
- [Mojave HVAC homepage](https://mojavehvac.com/) — product lines (ArctiDry DX, ArctiDry Hydro), Data Centers application page, company announcements. Fetched 2026-07-18.
- [Mojave Leadership page](https://mojavehvac.com/leadership/) — Phil Farese, Rachel Ellman, Aaron Meles, Robert Fancher, Greg Tatro bios. Fetched 2026-07-18.
- [Mojave About page](https://mojavehvac.com/about/) — investor list (Fifth Wall, At One Ventures, Myriad, Alumni Ventures, Earth Venture Capital, Starshot), company mission and metrics. Fetched 2026-07-18.
- [Improved Moisture Control with Less Energy: Mojave Liquid Desiccant Air Conditioning (SERDP-ESTCP, DoD)](https://serdp-estcp.mil/projects/details/d3805f90-f29b-409a-b5c3-262be296cd18/improved-moisture-control-with-less-energy-mojave-liquid-desiccant-air-conditioning) — DoD demonstration project EW26-9353, objectives, PI Aaron Meles. Fetched 2026-07-18.
- [Mojave works to scale its dehumidification-driven commercial AC technology (Facilities Dive, Dec 19, 2024)](https://www.facilitiesdive.com/news/air-conditioning-efficiency-electricity-costs-liquid-desiccant-mojave-energy-systems/736051/) — $9.5M Series A detail, DOE/NREL partnership, patent count, ISMRE figures. Fetched 2026-07-18.
- [Mojave Energy Systems: Interview With CEO Phil Farese (Pulse 2.0, May 7, 2025)](https://pulse2.com/mojave-energy-systems-profile-phil-farese-interview/) — Xerox PARC origin story, founding team (Farese/Meles/Ellman), funding history and cumulative total, TAM figures. Fetched 2026-07-18.
