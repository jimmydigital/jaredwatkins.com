---
title: "Corintis"
date: 2026-04-03
lastmod: 2026-04-03
draft: false
description: "Swiss EPFL spinout developing microfluidic chip-scale cooling systems that route liquid through microscopic channels etched directly into silicon, claiming 3x better heat removal than advanced cold plates and enabling rack densities toward 1 MW/rack."
tags: ["cooling", "liquid-cooling", "datacenter", "chip-cooling", "emerging", "direct-to-chip", "high-density", "ultra-high-density", "us", "eu"]
categories: ["company"]
research_area: "datacenters/cooling"
source_urls:
  - "https://acequia.substack.com/p/the-hot-topic"
  - "https://www.globenewswire.com/news-release/2025/09/25/3156314/0/en/Corintis-raises-24M-to-target-the-next-AI-bottleneck-and-collaborates-with-Microsoft-for-chip-cooling-breakthrough.html"
  - "https://tech.eu/2025/09/25/corintis-lands-24m-and-microsoft-endorsement-for-chip-cooling-tech/"
  - "https://www.nextplatform.com/2025/09/26/microsoft-and-corintis-champion-microfluidics-cooling-pioneered-by-ibm/"
  - "https://epflalumni.ch/en/article/remco-van-erp-ceo-of-corintis-chip-cooling-will-be-key-to-the-future-of-ai/25/08/2025/531"
  - "https://finance.yahoo.com/news/chip-cooling-startup-corintis-raises-110309927.html"
  - "https://spectrum.ieee.org/microfluidics-cooling-ai-chips-corintis"
last_reviewed: 2026-04-03
stale_after_days: 90
---

## Summary

Corintis is a Lausanne, Switzerland–based startup spun out of EPFL's POWERlab that develops microfluidic cooling systems for high-power AI and HPC chips. Rather than resting a conventional cold plate atop a chip, Corintis etches microscopic channels — roughly 100 microns in diameter — directly into or just above the silicon die, routing coolant precisely to each thermal hotspot using AI-optimized flow topologies. The approach matters because conventional cold plates and air cooling are nearing physical limits at modern GPU power levels, and Corintis's chip-integrated path is positioned as a step toward the long-range datacenter target of 1 MW per rack.

## Key Facts

- **Founded:** 2022 (EPFL Innogrant awarded 2021; incorporated January 2022)
- **HQ:** Lausanne, Switzerland (EPFL campus)
- **Additional offices:** Munich, Germany; Bellevue, Washington, USA
- **Type:** Company — hardware and cooling design software
- **Status:** Active; Series A stage
- **Employees:** ~75 (as of late 2025)
- **Total funding raised:** $33.4 million
- **Post-money valuation:** ~$400 million (implied post-Series A, 2025)
- **Products:** Microfluidic cold plates (drop-in and embedded); Glacierware (AI-assisted cooling design software); Therminator Platform (silicon test chip for cooling validation)
- **Cumulative revenue:** Eight-figure USD cumulative since incorporation (company-disclosed)
- **Units manufactured:** 10,000+ cooling systems shipped
- **Recognition:** #1 Top 100 Swiss Startup 2025; #2 in 2024

## What It Is / How It Works

Corintis's core technology is the integration of microfluidic channels into the thermal management layer of a chip or directly into the chip substrate. Where a standard cold plate uses a rectilinear array of parallel channels machined from copper — distributing coolant uniformly regardless of where heat is actually generated — Corintis uses AI-driven simulation software (Glacierware) to map the power and temperature distribution of a specific chip design, then generates a custom channel topology that routes more coolant to high-flux hotspots and less to cooler regions. The resulting patterns are described as organic-looking — resembling circulatory systems, mycelial networks, or the Corinth Canal in Greece, from which the company takes its name. Channels are approximately 100 microns in diameter, within the range of human hair thickness, and are manufactured using copper microfabrication.

The company distinguishes two product generations. The current commercial offering is a drop-in replacement for existing cold plates: a microfluidic copper cold plate fitted to standard server hardware, connecting to the existing facility-side liquid cooling loop (CDU, facility chilled water). No changes are required to the chip itself. Future iterations will embed the microfluidic structure inside the chip die, co-designed with the electronics from the start — a fundamental shift in how chip and thermal management are conceived. This second-generation approach is already demonstrated in prototype with Microsoft (see Notable Developments).

The Therminator Platform is a dedicated silicon test chip with instrumented thermal sensors that allows Corintis and its customers to validate cooling designs in-silicon before committing to full production chip tape-outs. Glacierware, the design software, uses AI to iteratively optimize the tubule network topology, a problem with enormous solution space that makes manual design infeasible.

The technology builds on academic foundations established at IBM Zurich beginning around 2008 (embedded liquid cooling across 3D chip stacks) and extended through DARPA's ICECool program (2013). EPFL POWERlab's contribution, documented in a *Nature* paper co-authored by van Erp and Matioli's team, was to demonstrate the approach at the transistor level and on real power semiconductor devices. Corintis was founded specifically to commercialize that line of research.

## Notable Developments

- **2025-09:** Announced $24 million Series A led by BlueYard Capital, with participation from Founderful, Acequia Capital, Celsius Industries, and XTX Ventures. Total funding reached $33.4 million. Simultaneously announced Microsoft collaboration results (see below). Post-money valuation reported at ~$400 million. Intel CEO Lip-Bu Tan joined the board as a personal investor.

- **2025-09:** Microsoft announced it successfully tested a Corintis microfluidic in-chip cooling system running live Teams conferencing traffic on a CPU prototype. Microsoft reported the system removed heat "three times better" than standard cold plates. Reduced coolant intake temperature by 13% and cut pressure drop by 55% vs. parallel microchannel baseline. The test demonstrated overclocking headroom unavailable under standard thermal constraints. Microsoft subsequently placed orders for "large quantities" of customized cold plates.

- **2025:** Opened engineering offices in Munich, Germany and Bellevue, Washington, USA (headcount and date not publicly confirmed beyond 2025).

- **2025:** Named #1 Top 100 Swiss Startup 2025 (was #2 in 2024). Company had reached 75 employees and crossed eight-digit cumulative revenue.

- **2022 (early):** CHF 3.85 million seed funding round. Company had ~4 employees at this time.

- **2021:** Received EPFL Innogrant. Selected for Venture Leaders Mobile 2022 program (Venturelab).

- **2022 (January):** Incorporated as Corintis SA, Lausanne. Founders: Remco van Erp, Sam Harrison, Prof. Elison Matioli.

## Key People

### Dr. Remco van Erp — Co-founder & CEO
- **LinkedIn:** [https://www.linkedin.com/in/remcovanerp/](https://www.linkedin.com/in/remcovanerp/)
- Dutch national. Completed master's degree in the Netherlands (field not publicly specified).
- **2017–2022:** PhD at EPFL POWERlab (Prof. Elison Matioli's group) — microfluidics and semiconductor thermal management; co-authored *Nature* paper on transistor-integrated cooling.
- **2022–present:** Co-founder & CEO, Corintis SA.
- No documented overlap with other companies currently tracked in the Research section.

### Sam Harrison — Co-founder & COO
- **LinkedIn:** [https://www.linkedin.com/in/samuel-mark-harrison/](https://www.linkedin.com/in/samuel-mark-harrison/)
- Education: MSc Space Studies, International Space University (2016); Product Management Executive Programme, INSEAD.
- **2014–2017:** Various roles at UrtheCast (satellite imagery), Apple Retail, and co-founded a high-altitude launch service startup.
- **2017–2021:** Astrocast — Senior Product Manager, then Head of Product Management (satellite IoT connectivity embedded electronics and software).
- **At NASA:** Research Scholar (duration not publicly confirmed).
- **2022–present:** Co-founder & COO, Corintis SA.
- No documented overlap with other companies currently tracked in the Research section.

### Prof. Elison Matioli — Co-founder & Scientific Adviser
- **LinkedIn:** [https://www.linkedin.com/in/elison-matioli-74ab1586/](https://www.linkedin.com/in/elison-matioli-74ab1586/)
- **EPFL profile:** [https://www.epfl.ch/labs/powerlab/prof-elison-matioli/](https://www.epfl.ch/labs/powerlab/prof-elison-matioli/)
- Director of EPFL POWERlab (Power and Wide-bandgap Electronics Research Laboratory), Institute of Electrical Engineering.
- Remains active faculty at EPFL; role at Corintis is Scientific Adviser (not operational).
- No documented overlap with other companies currently tracked in the Research section.

### Lip-Bu Tan — Board Director (personal investor)
- **LinkedIn:** not searched (public figure; CEO of Intel as of March 2025)
- Chairman of Walden International (venture capital). Became Intel CEO March 2025. Invested in Corintis personally before his Intel appointment; joined board as director upon Series A announcement (September 2025).
- **⚑ Note:** As Intel CEO, Tan's board seat at a chip cooling startup creates a potential alignment with Intel's interest in solving thermal limits of future process nodes. This connection should be monitored for future Intel–Corintis partnership disclosures.

### Geoff Lyon — Board Member
- **LinkedIn:** not found via public search
- Founder and former CEO of CoolIT Systems (Calgary, Canada — direct-to-chip liquid cooling; also documented in the Research section).
- **⚑ Overlap:** Geoff Lyon is the founder of [CoolIT Systems](https://www.coolitsystems.com), which appears in the Datacenter Cooling companies table in `content/research/datacenters/cooling/_index.md`. His board membership at Corintis represents a direct link between these two documented cooling companies.

### People — Last Reviewed: 2026-04-03

## Key Organizations

**Investors:**
- BlueYard Capital (lead, Series A) — Berlin-based VC
- Founderful — Swiss early-stage VC
- Acequia Capital — the Acequia Substack author's associated fund (also the primary source article for this entry)
- Celsius Industries — climate tech VC
- XTX Ventures — quant-firm-affiliated VC (XTX Markets)

**Customers / Partners:**
- Microsoft — prototype testing partner; validated in-chip microfluidic cooling on Teams server workload; placed orders for customized cold plates (2025). Primary customer cited in Series A announcement.

**Research origin:**
- EPFL POWERlab — academic home of the founding research; Prof. Matioli remains active faculty

**Board-linked companies:**
- CoolIT Systems — Geoff Lyon (Corintis board) is founder and former CEO (see Key People overlap note)
- Intel — Lip-Bu Tan (Corintis board) is current CEO; no formal Intel–Corintis partnership announced

## Datacenter Metrics

| Metric | Value | Source | Notes |
|--------|-------|---------|-------|
| Cooling efficiency vs. cold plate | 3x better heat removal | Microsoft / GlobeNewswire press release | Measured on Teams-workload CPU prototype; not independently peer-reviewed |
| Energy efficiency vs. air cooling | Up to 50x more efficient | Corintis / EPFL Alumni article | Company claim; comparison basis (air vs. microfluidic at chip level) not fully specified |
| Heat removal improvement target | 10x vs. current methods | Corintis press materials | Long-range product goal; current product is nearer-term |
| Coolant intake temperature reduction | 13% vs. standard cold plate | Next Platform / Microsoft test | From Microsoft collaboration test data |
| Pressure drop reduction | 55% vs. parallel microchannel cold plate | Next Platform / Microsoft test | From Microsoft collaboration test data |
| GPU max temperature reduction | 65% under workload | Next Platform / Microsoft test | From Microsoft collaboration test data |
| Supported rack density | Not publicly specified per product | — | Corintis positions itself as enabling path to 1 MW/rack by 2030 (industry target); current deployment density not disclosed |
| Coolant approach | Direct-to-chip (microfluidic, chip-integrated) | — | Drop-in cold plate today; embedded in-chip in next generation |
| Coolant temperature range | Not publicly specified | — | Operates with standard facility liquid cooling loop |
| PUE impact | Not publicly stated | — | No design PUE or measured PUE claim found |

## Claim Verification

### Claim: "Up to 3x better at removing heat than the most advanced technology commonly used today" (cold plates)

**Status:** Partially verified

**Supporting sources:**
- [GlobeNewswire press release, September 2025](https://www.globenewswire.com/news-release/2025/09/25/3156314/0/en/Corintis-raises-24M-to-target-the-next-AI-bottleneck-and-collaborates-with-Microsoft-for-chip-cooling-breakthrough.html) — Microsoft is cited as the source of the 3x figure, based on its own testing of a Corintis prototype running Teams server traffic.
- [Next Platform, September 2025](https://www.nextplatform.com/2025/09/26/microsoft-and-corintis-champion-microfluidics-cooling-pioneered-by-ibm/) — Provides additional test metrics: 13% lower coolant intake temperature, 55% lower pressure drop, 65% GPU max temperature reduction vs. standard cold plate.

**Refuting / questioning sources:**
- No direct refuting sources found. However, the test was conducted by Microsoft (a customer and likely equity-aligned party) on a single CPU prototype running a specific workload (Teams conferencing). No third-party independent lab measurement or peer-reviewed replication has been identified. The "most advanced technology commonly used today" baseline is not precisely specified in public disclosures.

**Summary:** The 3x figure comes from a customer-conducted test, not an independent lab; the underlying metrics (temperature reduction, pressure drop) are directionally plausible given published microfluidic research, but the claim is not yet independently verified. Treat as plausible but unverified pending peer review or third-party benchmarking.

---

### Claim: "Up to 50x more energy-efficient than air cooling"

**Status:** Unverified

**Supporting sources:**
- [EPFL Alumni article, August 2025](https://epflalumni.ch/en/article/remco-van-erp-ceo-of-corintis-chip-cooling-will-be-key-to-the-future-of-ai/25/08/2025/531) — Quotes van Erp directly; basis of comparison not specified.

**Refuting / questioning sources:**
- No directly refuting source found. The comparison basis (air cooling of what workload, at what rack density, under what conditions) is not specified in any public source reviewed. A 50x figure for energy at chip scale is plausible in principle (liquid is far more thermally conductive than air) but the metric requires careful specification to be meaningful.

**Summary:** Unverified. No independent measurement found; comparison conditions unspecified. Treat as an illustrative marketing claim until sourced to a published test or paper.

---

### Claim: "10x improvement in chip cooling" (long-range product target)

**Status:** Unverified — stated as a design goal, not a demonstrated result

**Supporting sources:**
- [Venturelab profile](https://www.venturelab.swiss/Corintis-The-startup-that-solves-a-hot-problem) — Company-stated mission target.

**Refuting / questioning sources:**
- None found. This is a stated long-range target, not a current product specification. No timeline for achieving 10x is publicly defined.

**Summary:** Forward-looking company target; not a claim about current products. Not verifiable at this time.

## FAQ

**Why does microfluidic cooling outperform a standard cold plate?**

A standard cold plate is thermally blind — it runs parallel channels in straight lines across the entire chip surface, distributing coolant uniformly regardless of where heat is actually generated. Modern GPUs and CPUs are not thermally uniform: they have intense hotspots (compute cores, memory interfaces, voltage regulators) sitting beside relatively cool regions (unused logic, cache). When you cool everything uniformly, the hotspot temperature becomes the binding constraint even if average chip temperature is fine, and you waste pumping energy on areas that don't need it.

Corintis maps the actual power distribution of a specific chip design and generates a channel topology that concentrates flow at hotspots and backs off elsewhere. More flow where it's needed, less pressure drop overall (Microsoft measured a 55% reduction), and lower peak temperatures even at the same average coolant flow rate.

**What does channel diameter have to do with it?**

Heat transfer from a surface to a fluid improves as channels get smaller — smaller diameter means higher surface-area-to-volume ratio, which means better convective heat transfer per unit of pumping energy. Corintis's channels are approximately 100 microns in diameter (roughly the width of a human hair), narrow enough to dramatically improve the convective coefficient while remaining manufacturable at volume.

**Why is embedded-in-chip better than a cold plate sitting on top?**

A cold plate resting on a chip package is separated from the actual transistors by the die itself, a layer of thermal interface material, and the package lid — each layer adding thermal resistance. Corintis's next-generation approach embeds channels directly in the silicon, eliminating those intermediate layers and bringing coolant as close as physically possible to the heat source.

**Why is liquid so much more efficient than air at this?**

Water has roughly 3,500× the volumetric heat capacity of air and about 25× better thermal conductivity. You move vastly more heat with the same pumping energy, and you can deliver coolant directly to the source rather than hoping air can carry heat away from the chip surface, across a heatsink, and out of a rack. That's the physics behind the 50× energy efficiency claim versus air cooling.

**If the physics has been known since IBM demonstrated it in 2008, why wasn't this done earlier?**

Two barriers: manufacturing and organizational coordination. Etching precise microfluidic networks at or near silicon at production volumes is non-trivial. More importantly, chip thermal management and chip design have historically been done by entirely separate teams at separate companies — the chip designer tapes out the die, then someone else figures out how to cool it afterward. Corintis's Glacierware software is partly an attempt to bridge that gap, giving chip designers a tool to co-generate cooling topologies during the design phase rather than as an afterthought.

## Sources

- [Acequia Substack — "The Hot Topic"](https://acequia.substack.com/p/the-hot-topic) — Primary source; investor perspective on Corintis technology and datacenter cooling market context. (Acequia Capital is also a Corintis investor — disclose conflict of interest when citing.)
- [GlobeNewswire press release, 25 September 2025](https://www.globenewswire.com/news-release/2025/09/25/3156314/0/en/Corintis-raises-24M-to-target-the-next-AI-bottleneck-and-collaborates-with-Microsoft-for-chip-cooling-breakthrough.html) — Official Series A and Microsoft collaboration announcement; source for funding, investor list, Microsoft test results.
- [Tech.eu, 25 September 2025](https://tech.eu/2025/09/25/corintis-lands-24m-and-microsoft-endorsement-for-chip-cooling-tech/) — Series A coverage.
- [Next Platform, 26 September 2025](https://www.nextplatform.com/2025/09/26/microsoft-and-corintis-champion-microfluidics-cooling-pioneered-by-ibm/) — Deep technical coverage of microfluidic cooling history (IBM, DARPA ICECool, Georgia Tech) and Corintis's position; source for specific Microsoft test metrics.
- [EU-Startups, September 2025](https://www.eu-startups.com/2025/09/swiss-startup-corintis-raises-e20-million-to-target-ai-bottleneck-and-collaborates-with-microsoft-for-chip-cooling-breakthrough/) — European coverage of Series A.
- [EPFL Alumni — Remco van Erp interview, August 2025](https://epflalumni.ch/en/article/remco-van-erp-ceo-of-corintis-chip-cooling-will-be-key-to-the-future-of-ai/25/08/2025/531) — CEO background and company origin story.
- [Venturelab — founding profile](https://www.venturelab.swiss/Corintis-The-startup-that-solves-a-hot-problem) — Early company history, founding story, Corinth Canal naming origin.
- [Top 100 Swiss Startups 2025](https://www.top100startups.swiss/Engineering-startup-Corintis-wins-the-Top100-Swiss-Startup-Award-2025) — #1 ranking confirmation.
- [Reuters / Yahoo Finance — Lip-Bu Tan board appointment](https://finance.yahoo.com/news/chip-cooling-startup-corintis-raises-110309927.html) — Source for Tan investment and board role.
- [IEEE Spectrum — Microfluidics Cooling AI Chips](https://spectrum.ieee.org/microfluidics-cooling-ai-chips-corintis) — Technical coverage; "80% temperature reduction" headline claim (full article behind paywall; details not fully verified).
- [Silicon Canals — exit from stealth](https://siliconcanals.com/corintis-exits-stealth-mode-with-e20-4m/) — Reporting on Series A announcement.
- [GGBA (Greater Geneva Bern Area)](https://ggba.swiss/en/corintis-raises-usd-24-million-to-accelerate-chip-cooling-innovation/) — Swiss economic development coverage of Series A.
