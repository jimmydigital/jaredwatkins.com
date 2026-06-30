---
title: "Williams Companies (Power Innovation)"
date: 2026-06-04
lastmod: 2026-06-04
draft: false
description: "Williams Companies' Power Innovation program: natural gas pipeline operator turned BTM power provider, deploying modular gas turbine plants directly serving AI data centers."
research_area: "datacenters/behind-meter-power"
source_urls:
  - "https://www.williams.com/power-innovation/"
  - "https://www.williams.com/2026/03/17/powering-data-centers-behind-the-meter-power-explained/"
  - "https://www.datacenterdynamics.com/en/news/ohio-regulators-approve-construction-of-200mw-gas-power-plant-to-serve-meta-data-center-in-new-albany-ohio/"
  - "https://www.powermag.com/new-200-mw-gas-fired-plant-in-ohio-will-power-meta-data-center/"
  - "https://www.power-eng.com/gas/williams-pushes-deeper-into-power-generation-as-data-center-power-demand-accelerates/"
  - "https://www.distilled.earth/p/metas-data-center-strategy-and-the"
  - "https://www.power-eng.com/onsite-power/onsite-gas-turbines-reciprocating-engines-to-power-meta-data-center/"
  - "https://www.cat.com/en_US/products/new/power-systems/electric-power/gas-generator-sets/130060.html"
  - "https://www.solarturbines.com/en_US/products/power-generation-packages/titan-130.html"
last_reviewed: 2026-06-04
stale_after_days: 90
related:
  - "datacenters/design-construction/meta-rapid-deployment-structures.md"
  - "datacenters/behind-meter-power/ge-vernova-aeroderivative.md"
  - "datacenters/behind-meter-power/siemens-energy-btm.md"
  - "datacenters/behind-meter-power/caterpillar-solar-turbines.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Williams Companies is a Tulsa, Oklahoma-based natural gas pipeline and processing operator (NYSE: WMB) that launched a Power Innovation program to build dedicated behind-the-meter gas turbine power plants for AI data centers. Williams leverages its existing pipeline infrastructure to deliver gas supply and build generation capacity directly adjacent to hyperscale campuses. Its first project — "Socrates" in New Albany, Ohio — is a 400 MW off-grid plant serving Meta, scheduled to enter service late 2026.

## Key Facts

- **Founded:** 1908 (Tulsa, OK); NYSE: WMB
- **Type:** Publicly traded pipeline operator / BTM power developer
- **Status:** Active — Power Innovation program underway; Socrates (Ohio) under construction as of 2026
- **Capital commitment:** $5.1 billion committed to Power Innovation buildout
- **Target capacity:** 6+ GW of BTM power across Texas, Tennessee, and Ohio by 2027
- **First project:** Socrates — two × 200 MW gas plants at New Albany, Ohio for Meta (10-year agreement)
- **Turbine OEMs used:** Solar Turbines (Titan 250, PGM 130), Siemens Energy (SGT-400), Caterpillar (3520 engines)

## What It Is / How It Works

Williams Companies built its business on natural gas transmission — its Transco pipeline is the largest-volume natural gas pipeline in the US. The Power Innovation program extends that vertical by having Williams build, own, and operate gas-fired generation assets that sit physically adjacent to data center campuses and supply power directly, bypassing the electric grid entirely.

The model is distinct from an equipment sale: Williams takes a developer role, financing and constructing the generation asset, then selling power to the data center operator under a long-term power purchase agreement (PPA) or tolling arrangement. The data center customer avoids the capital cost and regulatory complexity of building its own power plant; Williams earns a long-term contracted revenue stream leveraging its gas supply and pipeline expertise.

Williams' existing pipeline infrastructure is a core competitive advantage. Where a standalone power developer would need to negotiate gas supply contracts and build interconnections, Williams already controls the gas delivery. The Socrates project in Ohio, for example, is fed by two dedicated 24-inch pipelines from Williams' existing Transco system.

The generation equipment mix in early projects reflects what is fast to deploy and source: Solar Turbines Titan 250 and PGM 130 aeroderivative units, Siemens Energy SGT-400 turbines, and Caterpillar 3520 reciprocating engines. These are packaged, modular units that can be deployed in weeks and scaled in parallel — consistent with data center operators' demand for fast time-to-power. Williams explicitly selected this combination for high reliability: the turbines provide high-output baseload generation while the quick-start reciprocating engines provide fast ramping and redundancy during turbine maintenance windows.

The Socrates project's two 200 MW plants are designed to operate entirely off-grid: "will operate 'behind-the-meter' to serve the electric load of an adjacent data center and will not be physically connected to the electric power grid," per Ohio regulatory filings. This structure avoids grid interconnection review, MISO capacity reserve obligations, and transmission pricing — but also means the data center depends entirely on Williams' on-site generation for power, with no grid backup.

## Generation Equipment Supply Chain

The Socrates South project (200 MW, Ohio) is the only Williams BTM plant with public equipment specifications, drawn from Ohio Power Siting Board (OPSB) filings. It provides a detailed picture of Williams' generation stack and OEM supply chain.

### Socrates South Equipment Mix (one 200 MW plant)

| Equipment | OEM | Type | Count | Unit Output (est.) | Role |
|-----------|-----|------|-------|--------------------|------|
| Titan 250 | Solar Turbines (CAT subsidiary) | Industrial gas turbine | 3 | ~22 MW each | Primary baseload |
| PGM 130 | Solar Turbines (CAT subsidiary) | Industrial gas turbine | 9 | ~15 MW each | Primary baseload |
| SGT-400 | Siemens Energy | Industrial gas turbine | 3 | ~13 MW each | Supplemental baseload |
| G3520 | Caterpillar | Reciprocating engine (natural gas) | 15 | ~2–3 MW each | Fast-response / redundancy |
| SMT 130 | Solar Turbines | Mobile combustion turbine (generator set) | 1 (space reserved) | ~15 MW | Contingency / outage backup |
| C15 diesel | Caterpillar | Diesel generator | 8 | 500 kW each | Emergency / black start |

**Estimated nameplate breakdown (Socrates South, 200 MW total):**
- Solar Turbines Titan 250 (×3): ~66 MW
- Solar Turbines PGM 130 (×9): ~135 MW
- Siemens Energy SGT-400 (×3): ~39 MW
- Caterpillar G3520 (×15): ~35–45 MW
- Total primary generation: ~275–285 MW (nameplate), derated to 200 MW net output accounting for auxiliary loads, ambient derating, and maintenance reserve

The full Socrates project comprises two 200 MW plants (Socrates North and Socrates South) for 400 MW total. The equipment mix for Socrates North has not been separately disclosed but is assumed similar.

### Equipment Technology Notes

**Solar Turbines Titan 250** — The Titan 250 is Solar Turbines' largest industrial gas turbine, a single-shaft recuperated design producing approximately 22 MW at ISO conditions. It is optimized for oil and gas compression and power generation duty, with high availability ratings from decades of field deployment. As a Caterpillar subsidiary product, Solar Turbines brings mature supply chain and global service network. The "250" designation refers to the engine's compressor class, not output in MW.

**Solar Turbines PGM 130** — The PGM 130 (Power Generation Module based on the Titan 130 engine) is a packaged turbine generator set producing approximately 15 MW. The Titan 130 is a proven workhorse in the 15 MW class with strong part-load efficiency from its recuperated design. Nine units gives Williams fine-grained output control — units can be staged on/off to follow the data center's actual load, reducing fuel burn during lower-demand periods.

**Siemens Energy SGT-400** — The SGT-400 is a 13 MW class industrial gas turbine in Siemens Energy's smaller SGT series (distinct from the larger SGT-700/800 series targeting 60+ MW). It is a two-shaft design with fast-start capability and good part-load efficiency, commonly used in oil and gas and distributed power applications. At three units, it contributes roughly 40 MW of supplemental generation and adds OEM diversity to the plant — reducing single-supplier risk.

**Caterpillar G3520 reciprocating engine** — The G3520 is a large-bore, 20-cylinder, V-configuration natural gas engine producing 2–3 MW per unit (specific rating varies by model variant: G3520C ≈ 2.0 MW, G3520E ≈ 2.5 MW, newer variants up to 3.1 MW). Fifteen units contribute approximately 35–45 MW of total capacity. The critical operational role of reciprocating engines in this plant is **fast start**: while gas turbines require 10–30 minutes to reach full load from cold, reciprocating engines can reach rated output in under 2 minutes. This allows the plant to cover sudden load spikes or a turbine trip without interrupting the data center. Reciprocating engines also excel at part-load efficiency (best efficiency band 75–85% of rated load), making them economical for load-following as data center demand varies through the day.

**Caterpillar C15 diesel generators (×8, 500 kW each)** — These are conventional emergency diesel generators, not primary generation. Their role is black start capability: if the plant loses all prime movers simultaneously, the C15 diesels restart the facility from zero. They also cover station auxiliary loads during startup sequences. Total emergency capacity: 4 MW.

**SMT 130 mobile turbine (reserved space)** — Williams reserved footprint on the site for a Solar Turbines SMT 130 mobile generator set, a trailer-mounted unit producing approximately 15 MW. This can be trucked to site and connected during planned outages or forced outages on a primary turbine, maintaining output availability without requiring a permanently installed spare.

### Supply Chain Logic: Why This Mix?

Williams' equipment selection reflects several deliberate tradeoffs:

**Reliability through OEM diversity.** Using three OEMs (Solar Turbines, Siemens Energy, Caterpillar) means a supply disruption, product recall, or maintenance campaign at one OEM does not take down the entire plant. If Siemens issues a turbine inspection bulletin grounding the SGT-400 units, the Solar Turbines and CAT engines continue running.

**Turbines for efficiency, engines for agility.** Gas turbines are more fuel-efficient at sustained high loads (lower heat rate per MWh), making them the right choice for the baseload fraction of a 24/7 data center's power demand. Reciprocating engines are less efficient per MWh but start faster and follow load better — making them the right tool for ramping, redundancy, and covering turbine downtime.

**Modular unit count for granular control.** Having 9 PGM 130 turbines rather than a single 135 MW heavy-frame unit means the plant can shed or add ~15 MW increments as the data center's real-time load fluctuates. This avoids the efficiency penalty of running a large turbine at deep part-load.

**Pipeline gas as sole fuel.** All primary generation runs on pipeline natural gas delivered via two dedicated 24-inch diameter pipelines from Williams' own Transco system. No dual-fuel backup (diesel, propane) is specified for primary generation — the gas supply reliability is treated as sufficient given Williams' control of the pipeline infrastructure.

**Supply chain flags:**
- ⚑ **Solar Turbines lead times:** As a Caterpillar subsidiary, Solar Turbines has historically had shorter lead times than GE Vernova (which faces 24+ month backlogs in the aeroderivative market). However, rapidly growing demand from data center BTM projects industry-wide is beginning to tighten Solar Turbines capacity; lead times may extend through 2027.
- ⚑ **Siemens SGT-400 availability:** The SGT-400 sits in a less-congested market segment than the large aeroderivatives; Siemens has available capacity in this class as of 2026.
- ⚑ **CAT G3520 supply:** Caterpillar's large-bore gas engine manufacturing is primarily at its Lafayette, Indiana facility. The G3520 series is a mature product with a deep installed base; supply constraints are less acute than for gas turbines, though 15-unit orders of this size are unusual for a single project and may require lead times of 9–18 months.

## Notable Developments

- **2026-Q3 (projected):** Socrates power plants (New Albany, Ohio) scheduled to enter service — 400 MW total, serving Meta's Prometheus campus and adjacent rapid deployment structures
- **2026-Q1:** Williams reported expanding Power Innovation pipeline; 6+ GW target across Texas, Tennessee, Ohio by 2027; $5.1B committed capital; Q1 2026 earnings showed strong data center pipeline growth
- **2026-Mar:** Williams published explainer on BTM power model for data centers, signaling intent to market the model broadly — [Williams.com](https://www.williams.com/2026/03/17/powering-data-centers-behind-the-meter-power-explained/)
- **~2025-Q3:** Broke ground on Socrates (Ohio) project following Ohio Public Utilities Commission approval; two-plant design using modular gas units
- **2025:** Ohio regulators approved construction of 200 MW gas plant (first Socrates unit) to serve Meta New Albany campus — [Data Center Dynamics](https://www.datacenterdynamics.com/en/news/ohio-regulators-approve-construction-of-200mw-gas-power-plant-to-serve-meta-data-center-in-new-albany-ohio/)
- **2024–2025:** Williams announced Power Innovation program at CERAWeek 2024; initial design centered on modular gas units (Solar Turbines, Siemens, Caterpillar) for fast deployment in power-constrained markets

## Key People

Research on Williams Power Innovation leadership is ongoing. Williams Companies CEO is Alan Armstrong (long tenure; known for pipeline growth strategy). Power Innovation division leadership not yet identified in public sources.

<!-- TODO: identify Power Innovation division head and key deal team; check Williams investor presentations and press releases -->

### People — Last Reviewed: 2026-06-04

## Claim Verification

### Claim: Socrates plants will operate entirely off-grid, physically disconnected from the electric power grid

**Status:** Verified

**Supporting sources:**
- [Ohio Public Utilities Commission filing via Data Center Dynamics](https://www.datacenterdynamics.com/en/news/ohio-regulators-approve-construction-of-200mw-gas-power-plant-to-serve-meta-data-center-in-new-albany-ohio/) — quotes regulatory filing directly: facility "will not be physically connected to the electric power grid"
- [Power Magazine](https://www.powermag.com/new-200-mw-gas-fired-plant-in-ohio-will-power-meta-data-center/) — independently confirms off-grid operating structure

**Refuting / questioning sources:**
- None found. The off-grid claim is confirmed by state regulatory filings, not company marketing.

**Summary:** Confirmed by Ohio regulatory filings. The off-grid operating status is a defined fact in the project's regulatory record.

### Claim: $5.1 billion committed to Power Innovation; 6+ GW target by 2027

**Status:** Partially verified

**Supporting sources:**
- [Power Engineering](https://www.power-eng.com/gas/williams-pushes-deeper-into-power-generation-as-data-center-power-demand-accelerates/) — reports Williams investment figure and GW target
- [Rextag](https://rextag.com/blogs/blog/natural-gas-fuels-the-ai-boom-williams-builds-the-backbone-for-data-centers) — corroborates 6 GW / multi-state expansion

**Refuting / questioning sources:**
- The 6 GW figure includes projects in development pipeline, not just committed construction. Distinction between signed PPAs and LOIs not clearly broken out in public reporting.

**Summary:** Capital commitment and GW target figures appear in multiple trade sources and are consistent with Q1 2026 earnings disclosures; however, project-by-project breakdown of binding contracts vs. pipeline is not publicly confirmed.

## Sources

- [Williams Companies Power Innovation](https://www.williams.com/power-innovation/)
- [Williams: Powering data centers — behind-the-meter power, explained](https://www.williams.com/2026/03/17/powering-data-centers-behind-the-meter-power-explained/)
- [Data Center Dynamics: Ohio regulators approve 200MW gas plant for Meta data center](https://www.datacenterdynamics.com/en/news/ohio-regulators-approve-construction-of-200mw-gas-power-plant-to-serve-meta-data-center-in-new-albany-ohio/)
- [Power Magazine: New 200-MW Gas-Fired Plant in Ohio Will Power Meta Data Center](https://www.powermag.com/new-200-mw-gas-fired-plant-in-ohio-will-power-meta-data-center/)
- [Power Engineering: Williams pushes deeper into power generation as data center demand accelerates](https://www.power-eng.com/gas/williams-pushes-deeper-into-power-generation-as-data-center-power-demand-accelerates/)
- [Distilled.earth: Meta's Data Center Strategy and the Mad Max Phase of the AI Boom](https://www.distilled.earth/p/metas-data-center-strategy-and-the)
- [S&P Global: Williams to use modular gas units in early data center power projects (CERAWeek)](https://www.spglobal.com/energy/en/news-research/latest-news/natural-gas/032426-ceraweek-williams-to-use-modular-gas-units-in-early-data-center-power-projects)
- [Power Engineering: Onsite gas turbines, reciprocating engines to power Meta data center](https://www.power-eng.com/onsite-power/onsite-gas-turbines-reciprocating-engines-to-power-meta-data-center/) — OPSB filing details; exact equipment counts and OEM names for Socrates South
- [Cat G3520 product page](https://www.cat.com/en_US/products/new/power-systems/electric-power/gas-generator-sets/130060.html) — G3520 specifications
- [Solar Turbines Titan 130 product page](https://www.solarturbines.com/en_US/products/power-generation-packages/titan-130.html) — PGM 130 / Titan 130 specifications
