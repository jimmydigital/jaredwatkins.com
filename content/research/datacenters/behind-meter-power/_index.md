---
title: "Behind-the-Meter Power for Data Centers"
date: 2026-04-21
lastmod: 2026-04-24
draft: false
description: "Comprehensive research on behind-the-meter (BTM) power solutions for data centers: technology categories, companies, regulatory challenges, and 18+ GW of announced projects targeting grid-independent power for AI and hyperscale facilities."
tags: ["power", "behind-the-meter", "energy", "nuclear", "gas", "solar", "data-center", "smr", "microreactor", "fuel-cell"]
categories: ["overview"]
research_area: "datacenters/behind-meter-power"
last_reviewed: 2026-04-25
stale_after_days: 90
sitemap:
  changefreq: "weekly"
  priority: 0.8
  disable: false
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


{{< steering >}}
**Scope:** Companies selling, developing, or deploying on-site power generation specifically targeting data center customers. Includes natural gas turbines (aeroderivative and heavy-frame), reciprocating engines, micro-turbines, solar+battery storage, fuel cells, small modular reactors (SMRs), microreactors, geothermal, and hybrid systems. Covers both merchant power developers (sell power to DC operators) and OEM equipment vendors (sell generation hardware). Also covers vertically integrated operators that own both power and compute.

**Distinguish:**
- **BTM power providers** — own and operate the generation asset; sell power or capacity to a data center under a long-term PPA or tolling agreement (e.g., Oklo, Crusoe, Prometheus Hyperscale, VoltaGrid)
- **BTM equipment vendors** — sell hardware; customer builds and operates the plant (e.g., GE Vernova, Wärtsilä, Bloom Energy, Capstone)
- **Vertically integrated operators** — own both the generation and the compute (e.g., Crusoe, Lancium)

**Track:**
- Announced projects: power type, capacity (MW), timeline, data center customer name where known
- Signed contracts: distinguish binding PPAs/supply agreements from nonbinding LOIs/MOUs
- Key people: CEO/founder with prior roles, investor connections — flag ⚑ any leadership overlap across companies
- Regulatory status per technology type (NRC licensing, air quality permits, grid interconnection waivers)
- Cost estimates ($/MW capex, $/MWh levelized) where disclosed

**Flags:**
- ⚑ **Grid interconnection arbitrage** — some BTM arrangements face utility opposition or regulatory scrutiny for bypassing interconnection review, transmission cost allocation, and capacity reserve requirements
- ⚑ **"Carbon-free" claims** — nuclear and solar are carbon-free at point of generation; gas and fuel cells running on natural gas are not; verify any carbon claims carefully
- ⚑ **Order book credibility** — distinguish binding PPAs from nonbinding LOIs; many nuclear BTM order books are ~90% LOIs
- ⚑ **Supply chain constraints** — HALEU fuel (Oklo, X-energy), TRISO fuel (Kairos, X-energy, USNC), aeroderivative turbines (GE Vernova 24+ month lead times), all face binding supply limits

**Cross-links:**
- Energy section nuclear profiles: {{< relref "../../energy/nuclear/oklo.md" >}}, {{< relref "../../energy/nuclear/kairos-power.md" >}}, {{< relref "../../energy/nuclear/x-energy.md" >}}, {{< relref "../../energy/nuclear/terrapower.md" >}}, {{< relref "../../energy/nuclear/blue-energy.md" >}}, {{< relref "../../energy/nuclear/ge-hitachi-bwrx300.md" >}}
- Power infrastructure: {{< relref "../power-infrastructure/_index.md" >}}
{{< /steering >}}

## Executive Summary

Behind-the-meter (BTM) power solutions for data centers are reshaping energy infrastructure. As grid interconnection queues extend 5–10+ years and AI workload demand grows to 20–50+ GW by 2030, data center operators and developers are bypassing the grid entirely. **Approximately 46 data centers with 56 GW of combined planned capacity are building their own power generation, with 90% of BTM projects announced in 2025 alone.**

BTM power avoids regulatory delays, ensures availability independent of grid constraints, and enables deployment within months rather than years. Current deployments span **natural gas turbines (75% of identified generation), nuclear reactors (SMRs and microreactors targeting 2027–2035 online), fuel cells (Bloom Energy leading deployment), solar+storage (Amazon leading), and hydrogen-capable flexible engines.**

**Key regulatory challenge:** ⚑ Grid operators and utilities are increasingly opposing BTM power arrangements as regulatory arbitrage — operators are bypassing interconnection review, transmission pricing, and capacity reserve requirements. This friction will likely define the 2026–2028 period.

### April 2026 Significant Developments (Last Reviewed: 2026-04-24)

- **Kairos Power broke ground on Hermes 2 (April 17, 2026):** First Gen IV reactor ever to receive an NRC construction permit; first commercial-scale advanced nuclear reactor now under construction in the U.S. Located at Oak Ridge, TN; will supply 50 MW to TVA grid serving Google's data centers in Tennessee and Alabama. See {{< relref "kairos-power-btm.md" >}}.
- **Bloom Energy × Oracle 2.8 GW expansion (April 13, 2026):** Oracle expanded its fuel cell partnership after Bloom delivered a fully operational system in 55 days — 35 days ahead of schedule. Initial 1.2 GW contracted and deploying; up to 2.8 GW over 4 years. BE stock up 150% YTD. See {{< relref "bloom-energy-sofc.md" >}}.
- **Wärtsilä 790 MW Texas order (April 23, 2026):** Largest single Wärtsilä data center order to date; 42 × 50SG engines for Texas market entry. Cumulative data center sales now exceed 2.4 GW. See {{< relref "wartsila-btm.md" >}}.
- **GE Vernova Q1 2026 earnings beat:** $2.4B in data center electrification orders in Q1 alone (more than all 2025 combined). ~20% of 100 GW backlog tied to data centers. 2026 revenue guidance raised to $44.5–$45.5B. 20 GW annualized production target by Q3 2026. See {{< relref "ge-vernova-aeroderivative.md" >}}.
- **Oklo HSBC Buy rating + Nvidia partnership (April 2026):** HSBC initiated with Buy, $96 target; Oklo announced partnership with Nvidia and Los Alamos National Laboratory to accelerate nuclear-powered AI infrastructure.

---

## Why Behind-the-Meter Power for Data Centers?

### The Grid Bottleneck

- **Interconnection delays:** Queue times for grid connection now exceed 5–10 years in many regions; some projects are 15+ years out
- **Transmission constraints:** New transmission capacity is not being built at the pace of data center demand growth
- **Capacity reserve mandates:** Grid operators now require data centers to procure their own reserve capacity, increasing grid cost
- **Transmission pricing:** Charges for long-distance transmission can make grid power uneconomical relative to on-site generation

### Business Case for BTM

- **Time-to-power:** BTM natural gas turbines can be installed and online in weeks; compared to 5–10 years for grid interconnection
- **Certainty:** No dependence on utility schedules, regulatory approvals, or grid reliability
- **Cost:** At scale (500+ MW), on-site generation can be comparable to or cheaper than grid power plus transmission
- **Resilience:** Independent of grid outages; critical for customer SLAs requiring 99.99%+ uptime
- **Carbon narrative:** Wind, solar, nuclear, and fuel cell BTM solutions enable "24/7 carbon-free" marketing claims for hyperscalers

### Timeline Pressure

The "AI boom" timeline is compressing all decisions. OpenAI's Stargate initiative requires 10 GW by 2030; Amazon, Google, Microsoft, and Meta are all committing 5–10 GW each. Most grid projects can't deliver by 2030. **BTM is the only path to scale.**

---

## Technology Categories: BTM Power for Data Centers

### 1. Natural Gas Turbines & Engines (75% of identified generation)

**Why gas for data centers?**
- Fast start (5–30 minutes for aeroderivatives, hours for heavy-frame)
- Fuel supply reliable and distributed (pipeline or truck)
- Scalable modular architecture
- Can be retrofitted to hydrogen or sustainable fuels
- Low land footprint per MW

**Technology types:**

**Aeroderivative turbines (20–100 MW class):** Jet engine derivatives (GE Vernova LM2500XPRESS, Siemens SGT-700/800, Solar Turbines). Fast-start (minutes), high efficiency, suitable for peaking and fast-response applications.

**Heavy-frame turbines (100+ MW class):** Siemens, GE Vernova, Mitsubishi. Slower start, lower part-load efficiency, but higher power density. Dominated 2024; supply constrained in 2025–2026.

**Reciprocating engines (Wärtsilä 50/34SG, Caterpillar, Cummins, MAN):** 5–50 MW per unit, scalable in clusters. Excellent part-load efficiency, can run on multiple fuels (gas, biogas, hydrogen-blends). Wärtsilä booked ~800 MW in 2025 and has surpassed 2.4 GW in cumulative data center orders as of April 2026, including a 790 MW Texas order (April 23, 2026).

**Micro-turbines (Capstone, 30 kW – 10 MW):** Small deployments, CHP (combined heat and power) suitable for co-location facilities; not large-scale datacenter BTM typically.

**⚑ Regulatory friction:** State air quality boards (California, Texas, Pennsylvania) are increasingly resisting new gas capacity. Some projects face 18–36 month permitting delays. Texas and Louisiana permit faster due to deregulation.

**⚑ Carbon pressure:** Gas is not carbon-free; 24/7 carbon-free claims require pairing with wind/solar or power purchase agreements with nuclear/hydro.

---

### 2. Small Modular Reactors — SMRs (50–500 MW class)

**Core appeal:** Compact, walk-away-safe, flexible siting, 24/7 carbon-free baseload power. First commercial deployments 2027–2030.

**Leading designs & timeline:**

{{< relref "../../energy/nuclear/oklo.md" >}} **Oklo Aurora (75 MWe):**
- Sodium-cooled fast reactor; metallic HALEU fuel
- First deployment: Idaho National Laboratory, groundbreaking Sept 2025, target 2027–2028 criticality
- Order book: ~18 GW (mostly nonbinding LOIs) including Meta (~15 GW), Switch (12 GW), Equinix, Wyoming Hyperscale, Prometheus Hyperscale
- Key risk: HALEU fuel supply constrained; first-of-a-kind NRC licensing
- **BTM advantage:** Compact footprint (below-grade), minimal land use, can be co-located with or near data center

{{< relref "../../energy/nuclear/terrapower.md" >}} **TerraPower Natrium (345 MWe):**
- Sodium-cooled fast reactor; LEU metallic fuel (less enriched than HALEU)
- First deployment: Wyoming (Kemmerer site), expected on-line ~2030
- Agreements: Meta (8 units for 2.76 GW), Sabey Data Centers (MOU for wide-scale deployment)
- Key advantage: **Built-in molten-salt thermal storage** — can ramp from 345 MW to 500 MW+ for 5+ hours, enabling load-following
- **BTM advantage:** Storage feature makes it flexible for time-varying data center loads

{{< relref "../../energy/nuclear/blue-energy.md" >}} **Blue Energy (TBD size, est. 50+ MWe):**
- MIT spinout; development-stage SMR
- Crusoe Energy partnership: 1.5 GW facility at Port of Victoria, Texas (target power start 2031)
- Founded 2023; earlier stage than Oklo/TerraPower

**Kairos Power (50 MW molten-salt cooled):** ⚑ **MAJOR UPDATE: Hermes 2 groundbreaking April 17, 2026**
- Fluoride salt-cooled, high-temperature gas reactor (HTGR variant)
- Google partnership: 500 MW across 6–7 units by 2035, first unit (Hermes 2, Oak Ridge, TN) by 2030
- **Hermes 2 broke ground April 17, 2026** — first Gen IV reactor to receive NRC construction permit; first commercial-scale advanced reactor under construction in the U.S.; power to TVA grid for Google TN/AL data centers
- **Hermes 1 (test reactor)** at INL: reactor vessel installation complete; startup target 2027
- Key advantage: Molten salt coolant enables higher operating temperatures, potential for process heat (hydrogen production, desalination); binding Google PPA (not just LOI); factory-built modules from Albuquerque shipped to Oak Ridge

{{< relref "../../energy/nuclear/x-energy.md" >}} **X-energy Xe-100 (80 MWe, scalable to 320 MW as 4-pack):**
- High-temperature gas-cooled reactor (HTGR); TRISO fuel; modular architecture
- Amazon partnership: 5 GW by 2039 (plus Korea Hydro & Nuclear Power, Doosan Enerbility)
- TRISO-X fuel dependency on BWXT supply (shared bottleneck with Kairos, USNC)
- DOE funding; pre-application phase with NRC

**GE Hitachi BWRX-300 (300 MWe):**
- Water-cooled, natural circulation, passive safety
- {{< relref "../../energy/nuclear/ge-hitachi-bwrx300.md" >}}
- Google compatible statement (2025); construction starting Ontario, Canada (Darlington, May 2025, ~2029 completion)
- DOE grant to TVA ($400M, Dec 2025) to accelerate deployment
- Larger reactor (300 MW) — less suitable for co-located micro-deployment, but potential for large regional data center clusters

**⚑ Major risks:**
- **Licensing timeline:** First-of-a-kind designs (Oklo, Kairos, X-energy) faced/face NRC delays; Oklo's original COLA was rejected (2022). Re-licensing can add 2–4 years
- **HALEU and TRISO fuel supply:** HALEU enrichment capacity is the bottleneck. Oklo depends on INL inventory for first few units; commercial-scale HALEU supply (beyond ~1–2 GW) is unresolved. TRISO fuel: BWXT is the sole U.S. supplier; supply may constrain X-energy, Kairos, and USNC to <10 GW cumulative by 2030
- **Order book vs. binding commitments:** Oklo's ~18 GW order book is almost entirely nonbinding LOIs or framework agreements. If more than 2–3 units need to be deployed simultaneously, supply chain capacity (manufacturing, construction labor, NRC licensing) becomes severe constraint
- **First-of-a-kind cost:** Early units are typically 30–100% more expensive than mature designs; datacenter operators may defer projects if capital costs exceed grid-parity

**⚑ Regulatory friction:** Some states (California, New York) have statutory limits on reactor-size or siting requirements that SMR vendors must navigate separately.

---

### 3. Microreactors (< 10 MWe)

**Core appeal:** Smallest nuclear units; designed to be transportable, factory-built, and deployed in modular clusters. Refueling intervals 5–8+ years. First commercial deployments 2027–2030.

**Leading designs:**

**Westinghouse eVinci (5 MWe / 15 MWt):**
- Heat pipe reactor, no pumps, passive cooling, walk-away safe
- Factory-assembled, <2 acre footprint, transportable via standard rail/truck containers
- NRC Principal Design Criteria approved (2025)
- Penn State partnership (2025) for rapid prototyping
- Data center deployment pitch: "Multiple units can be deployed simultaneously or added as site grows"

**Radiant Kaleidos (1.2 MWe / ~5 MWt):**
- High-temperature gas-cooled (HTGR), HALEU TRISO fuel, helium coolant
- Equinix **preorder: 20 units** (announced Aug 2025) — major signal of data center demand
- Demonstration unit (KDU) at Idaho National Lab (DOME facility) targeted for 2026 startup
- Production target: 50 reactors/year by late 2020s
- **Modular strategy:** 1.2 MW per unit allows scaling to 2.4, 3.6, 4.8+ MW by clustering
- Capital cost target: ~$40–60M per unit (if mass production achieved)

**USNC MMR (→ NANO KRONOS MMR) (15 MWe / 45 MWt):**
- High-temperature gas-cooled, TRISO fuel, prismatic graphite blocks
- **Bankruptcy & acquisition:** USNC filed Chapter 11 (2024); NANO Nuclear acquired IP and assets (March 2025), rebranded as KRONOS MMR
- Pylon demonstration at INL DOME (target 2027)
- Data center fit: Larger than Kaleidos, but still deployable in clusters for campuses

**⚑ Microreactor specific risks:**
- **Unit economics:** At <10 MW, each unit has high per-MW capital cost (licensing, transport, first-of-a-kind). Equinix's 20-unit strategy is an exception; most deployments likely 1–3 units initially
- **HALEU supply:** Both Kaleidos and MMR use HALEU; supply is the bottleneck (see above)
- **Demonstration schedule slippage:** INL DOME facility is experiencing resource constraints; startup delays for KDU and Pylon are likely

---

### 4. Fuel Cells (Solid Oxide, Proton Exchange Membrane)

**Core appeal:** Distributed, modular, can run on natural gas or hydrogen, scalable from 100 kW to 50+ MW. Quiet operation (key for urban colos). Can provide combined heat and power (CHP).

**Technology:**

**Bloom Energy Server (SOFC, Solid Oxide Fuel Cell):**
- Current generation: Bloom Energy Server 5 (500 kW modules, scalable)
- Feedstock: Natural gas, biogas, hydrogen (today mostly natural gas)
- Efficiency: ~60% electrical + CHP capability
- **Data center deployments:** Apple, Google, Samsung, Equinix (100+ MW across 19 facilities), Oracle (2.8 GW MPA announced April 2026)
- **Major partnership:** Brookfield + Bloom Energy ($5B investment; 2025) for "AI factories" globally
- **AEP procurement:** Up to 1 GW of Bloom fuel cells from AEP (2024) — largest commercial fuel cell procurement to date
- Ramp: Bloom targeting 2 GW annual production capacity by end of 2026

**⚑ Fuel cell specific considerations:**
- **Natural gas feedstock:** Today's Bloom deployments mostly run on natural gas (not carbon-free). Green hydrogen path requires hydrogen infrastructure (limited availability, high cost as of 2026)
- **Capital cost:** ~$2–3M per MW (higher than gas turbines, lower than nuclear)
- **Regulatory:** Fuel cells face lower air quality restrictions than gas turbines in some jurisdictions
- **Maintenance:** Fuel cells are less mature than combustion engines; field reliability data still building

---

### 5. Solar + Battery Storage (Distributed BTM)

**Core appeal:** Renewable generation (zero emissions), increasingly cost-competitive. Battery storage can buffer multi-hour or full-day operations (depending on storage size). Slow deployment timeline (permitting + construction 2–3 years).

**Technology landscape:**

**Utility-scale solar + BESS clusters (100+ MW solar, 10–50+ MWh battery):**
- Amazon: 13.6 GW solar pipeline; projects pair solar + BESS (e.g., California project with battery storage)
- Google: Pine Island, Minnesota project — 1,400 MW wind + 200 MW solar + **300 MW iron-air battery storage (100-hour discharge)**, online 2028
- Microsoft: 475 MW renewable additions to existing 6.15 GW portfolio
- **Key insight:** 100-hour battery (Google) enables overnight and multi-day buffering; traditional 2–4 hour BESS insufficient for full "24/7 clean energy" claims

**⚑ Solar+storage BTM challenges:**
- **Diurnal/seasonal variability:** Even large battery banks cannot store 30+ days of winter generation; grid backup or other sources still required
- **Permitting timeline:** 2–3 years for land, environmental review, interconnection (if needed)
- **Land requirements:** Large solar arrays need significant acreage (not suitable for dense urban colos)
- **Cost competitiveness:** While solar and batteries have fallen dramatically, 100+ MWh battery systems still represent $100–300M capex

---

### 6. Hydrogen-Ready Turbines & Engines

**Emerging category:** Natural gas turbines and reciprocating engines are increasingly marketed as "hydrogen-capable" or "hydrogen-ready." Actual hydrogen deployments remain rare (2025) due to:
- Lack of pipeline infrastructure for industrial hydrogen (mostly merchant production centers)
- High cost of green hydrogen (~$3–5/kg as of 2026, vs. $1–2/kg for gray hydrogen)
- Turbine/engine redesign needed for full hydrogen (vs. natural gas)

**Players offering hydrogen paths:**
- Wärtsilä 50SG: "Hydrogen-ready" via fuel flexibility
- GE Vernova: Developing hydrogen turbine variants
- Siemens Energy: H-Class turbines and future hydrogen pathways
- Capstone micro-turbines: Can run hydrogen blends

**⚑ Hydrogen BTM for data centers (2026–2030 outlook):**
- Unlikely to be primary BTM path before 2030 due to infrastructure constraints
- Regional hydrogen hubs (Texas, Louisiana, Midwest) may enable pilot projects 2027–2029
- Long-term strategic optionality for data centers in hydrogen-producing regions (petrochemical centers, electrolysis hubs)

---

### 7. Geothermal (Enhanced Geothermal Systems — Emerging)

**Core appeal:** 24/7 carbon-free baseload power; no fuel supply chain; works at any hour and in any weather. Enhanced geothermal systems (EGS) use hydraulic fracturing and horizontal drilling to access geothermal heat in regions without traditional volcanic activity — dramatically expanding geographic viability.

**Market potential:** The Rhodium Group projected (March 2025) that enhanced geothermal systems could supply 55–64% of anticipated hyperscale data center capacity growth by 2030 — representing 15–17 GW of new BTM capacity. Western U.S. geothermal resources could theoretically meet 100% of regional new data center demand. A Bloomberg NEF analysis cited 4.9 GW of energy storage announcements co-located with on-site data center generation, many pairing geothermal baseload with BESS.

**Leading projects:**

**Fervo Energy Cape Station** (Southwest Utah):
- First commercial-scale enhanced geothermal project
- 100 MW Phase 1 under construction; target first power 2026
- 400 MW additional capacity by 2028 (500 MW total)
- Customers: Multiple data center operators (not yet fully disclosed)
- EGS technology uses horizontal well pairs; can be co-located or near-site (BTM-capable)

**Meta + Sage Geosystems:**
- Binding agreement for up to 150 MW of baseload geothermal power
- Technology: Pulsed geothermal (unique Sage approach using pressure management)
- Target: 2027 initial stage online
- Application: Meta data center operations (specific sites TBD)

**⚑ Geothermal BTM challenges:**
- **Geographic dependency:** Traditional geothermal is limited to tectonically active regions (West, Pacific Northwest). EGS expands this but adds drilling complexity and cost
- **Upfront capital:** EGS wells are expensive ($20–40M per well pair); high upfront capex even if fuel cost is zero
- **Lead time:** EGS projects require 2–4 years from site selection to first power (similar to gas, longer than fuel cells)
- **Unproven at scale:** No EGS project has sustained commercial operation at 100+ MW; Cape Station is the first demonstration at this scale

**Outlook:** Geothermal BTM is most credible for data centers in Texas, Nevada, Utah, Idaho, Oregon — states with geothermal resource access and favorable permitting. By 2030, EGS could represent 5–10% of BTM power deployed at data centers if costs and timelines hold.

**Sources:** [Rhodium Group EGS/data center analysis (March 2025)](https://rhg.com/research/geothermal-data-center-electricity-demand/), [Data Center Frontier: Fervo + geothermal BTM](https://www.datacenterfrontier.com/energy/article/55274889/why-geothermal-energy-could-be-a-behind-the-meter-game-changer-for-data-center-power-demand), [TechCrunch: Geothermal could power nearly all new data centers through 2030](https://techcrunch.com/2025/03/11/geothermal-could-power-nearly-all-new-data-centers-through-2030/)

---

## Project Status Tracker: Known BTM Power Projects for Data Centers

**Note:** Distinction between "operating," "under construction," and "announced" is fluid. Many projects have signed PPAs but haven't started construction. **Binding agreements (PPAs/supply contracts) are listed as "Contracted"; nonbinding LOIs/MOUs as "LOI only".**

| Project Name / Location | Data Center Customer | Power Provider / Developer | Technology | Capacity (MW) | Status | Target Online | Notes |
|---|---|---|---|---|---|---|---|
| **Crusoe Abilene (Lancium Clean Campus)** — Texas | Crusoe (internal) | Lancium + GE Vernova (29 LM2500XPRESS turbines) + solar+battery BTM | Gas turbines + Solar + BESS | 200 MW initial; 1,200 MW phase 2 | Under Construction | H1 2025 (phase 1); mid-2026 (phase 2) | Phase 1 complete; phase 2 adding 900 MW BTM gas + BESS |
| **Crusoe Port of Victoria BTM** — Texas | Crusoe (internal) | Blue Energy (SMR) | Nuclear (SMR, TBD size) | ~1,500 MW total facility | LOI/Early | 2031 | Blue Energy partnership; first SMR for datacenter |
| **OpenAI Stargate (Project Stargate)** — Multiple U.S. sites (5 sites announced by end 2025) | OpenAI (internal, plus cloud customers) | GE Vernova + various | Gas turbines (aeroderivative) | 7 GW (goal 10 GW by end 2025) | Contracted / Under Construction | Staged 2026–2028 | 29 LM2500XPRESS turbines delivering ~1 GW; additional sites TBD |
| **Equinix Multi-Site BTM Deployment** — Global (19 data centers announced) | Equinix customers | Oklo (500 MW), Radiant (20 x Kaleidos units), Bloom Energy, others | Mixed: SMR, microreactor, fuel cell, solar | 500 MW+ (Oklo alone); 20+ MW (Radiant Kaleidos) | Contracted / LOI | 2027–2030+ | Diversified energy strategy; largest colocation player; Radiant preorder signal |
| **Google Kairos Power — Hermes 2** — Oak Ridge, Tennessee | Google (internal cloud) | Kairos Power | Molten-salt SMR | 50 MW initial | **Under Construction** (groundbreaking April 17, 2026) | 2030 | **First Gen IV reactor with NRC construction permit; first commercial-scale advanced reactor now under construction in U.S.**; power to TVA grid for Google TN/AL data centers |
| **Google Pine Island** — Minnesota | Google (internal cloud) | Xcel Energy / utility + on-site integration | Wind (1,400 MW) + Solar (200 MW) + Battery (300 MW iron-air) | 1,800 MW total renewable + 300 MWh storage | Under Construction | 2028 | Not pure BTM (utility partnership); 100-hour battery enables load-shifting |
| **Microsoft Three Mile Island Restart** — Pennsylvania | Microsoft (internal cloud) | Constellation Energy (utility, but power purchased for Microsoft exclusive use) | Nuclear (1,100 MW existing reactor) | 835 MW available to Microsoft | Under Construction | 2028 | 20-year, $16B PPA; largest corporate nuclear deal to date |
| **Meta Constellation Energy Clinton** — Illinois | Meta (internal) | Constellation Energy | Nuclear (existing facility) | 1.1 GW | Contracted | 2025+ (existing) | 20-year PPA; operational 2024+ |
| **Meta TerraPower Natrium** — Wyoming (Kemmerer site + others) | Meta (internal) | TerraPower | Sodium-cooled SMR (Natrium) | 2.76 GW (8 units @ 345 MW each) | Contracted | 2030–2035 | Major SMR ordering commitment; demonstrates datacenter demand |
| **Meta Oklo Aurora** — Multiple TBD | Meta (internal) | Oklo | Sodium-cooled fast microreactor | ~15 GW (LOI, nonbinding) | LOI | 2027–2032 | Largest order book in nuclear datacenter space; mostly framework agreements |
| **Amazon X-energy Xe-100** — Multiple U.S. sites | Amazon (internal AWS) | X-energy (+ KHNP, Doosan Enerbility) | High-temp gas-cooled SMR (HTGR) | 5 GW by 2039 (phased) | Contracted | 2032–2039 | Partnership announced Aug 2025; manufacturing partnership with Korean utilities |
| **Oklo Idaho National Laboratory Aurora Unit 1** — Idaho | DOE / Test deployment (potential future datacenter integration) | Oklo | Sodium-cooled fast microreactor | 75 MW | Under Construction | Late 2027 / early 2028 | Groundbreaking Sept 2025; first commercial Oklo deployment; Kiewit contractor |
| **Equinix Oklo** — TBD sites | Equinix | Oklo | Aurora | 500 MW | Contracted | 2027–2030+ | Subset of Oklo order book; Equinix diversified energy play |
| **NuScale Standard Power** — Ohio + Pennsylvania | Standard Power (colocation) | NuScale | VOYGR SMR modules | ~2 GW (24 modules) | Contracted | 2030s | Post-UAMPS refocus on data center segment |
| **Kairos Power + Google** — Six sites planned U.S. | Google | Kairos Power | Molten-salt SMR | 500 MW (6–7 units) | Contracted | 2030–2035 | Growth from initial 50 MW Hermes 2 deal |
| **Siemens Energy + Eaton Data Center Power Plant** — Multiple | Multiple datacenter operators | Siemens Energy | Gas turbines (SGT-800 series, 45–62 MW each) | 500 MW standard modular plant | Contracted / Early | 2026–2028 | Integrated power + cooling solution; hydrogen-capable turbines |
| **Bloom Energy + Brookfield** — Global AI factories | Brookfield + datacenter customers | Bloom Energy | Fuel cell (SOFC) | TBD; $5B investment implies 500+ MW+ | Early / Design | 2026–2028 | Strategic partnership for "AI factory" model |
| **CoreWeave Volo, Illinois** — Illinois | CoreWeave | Bloom Energy | Fuel cell (SOFC) | ~100 MW (multiple Bloom units) | Under Construction | Q3 2025 (target) | CoreWeave partnership; 500 MW Bloom order implied |
| **Oracle + VoltaGrid/Energy Transfer** — Multiple U.S. | Oracle | VoltaGrid + Energy Transfer | Gas turbines / reciprocating engines | 2.3 GW | Contracted | 2026–2028 | Off-grid fossil gas power for Oracle cloud |
| **Joule Data Center** — Utah | Joule (developer) | On-site generation + grid interconnect | Gas-fired generation + potential nuclear future | 1.3 GW | Contracted / Under Construction | 2026–2028 | Fully islanded from grid (unique model) |
| **Prometheus Hyperscale + Engie** — Evanston, Wyoming | Prometheus Hyperscale | Engie (gas generation) + Oklo (future nuclear) | Gas-fired initially; nuclear BTM planned | 1.2 GW initial (gas); nuclear phased | Contracted (gas); LOI (Oklo) | 2026+ (gas); 2030s (nuclear) | Two-phase power transition model; Wyoming Oklo LOI for nuclear phase |
| **Wärtsilä Ohio Data Center** — Ohio | Unnamed operator | Wärtsilä | Reciprocating engines (18V50SG) | 282 MW | Contracted | 2025+ | 15-unit deployment; low water consumption feature |
| **Wärtsilä 507 MW Project** — U.S. (location TBD) | Unnamed operator | Wärtsilä | Reciprocating engines (50SG) | 507 MW | Contracted | 2026–2027 | 27-unit deployment |
| **Wärtsilä 429 MW Project** — U.S. | Unnamed operator | Wärtsilä | Reciprocating engines (50SG) | 429 MW | Contracted | 2027 | 24-unit deployment; January 2026 announcement |
| **Wärtsilä 790 MW Texas Project** — Texas | Unnamed operator | Wärtsilä | Reciprocating engines (50SG) | 790 MW | Contracted | 2027–2028 | 42-unit deployment; April 23, 2026 announcement; largest single Wärtsilä data center order |
| **Boom Supersonic (Superpower) Turbines** — Multiple Crusoe sites | Crusoe (internal) | Boom Supersonic | Aeroderivative gas turbine (42 MW each) | 1.21 GW (29 units) | Contracted | 2026–2027 | Symphony engine derivative; waterless operation; major Crusoe order |
| **Advanced Energy & Intelligence Campus** — Texas | Multiple (Permian Basin operators) | TBD mix | Mixed (gas + future nuclear/SMR) | 18 million sq ft campuses; 5 GW+ | Early | 2026+ (first 1 GW) | 5,800-acre multi-operator campus |
| **Sabey Data Centers + TerraPower** — Multiple sites | Sabey Data Centers | TerraPower | Natrium SMR | TBD | MOU / Early | 2030s | Sabey is smaller colocation provider; wide-scale deployment target |
| **Equinix Radiant Kaleidos** — Global sites TBD | Equinix | Radiant Nuclear | Microreactor (1.2 MW each) | 24 MW+ (20-unit preorder) | Preorder / Contracted | 2028–2030 | Major scaling signal for microreactors; modular deployment strategy |
| **CoreWeave + Liquid Cooling Leaders** — Multiple U.S. | CoreWeave | Bloom Energy | Fuel cells | 850 MW active (as of Q4 2025) | Operating / Ramping | 2025–2026 | One of largest operational BTM fuel cell deployments; 250MW added Q4 2025 |
| **Westinghouse eVinci + Penn State** — Pennsylvania | Penn State (pilot) | Westinghouse | Microreactor (5 MW) | 5 MW | Research / Pilot | 2026–2027 | University deployment; rapid prototyping focus |
| **Radiant Kaleidos Demonstration** — Idaho National Lab (DOME) | DOE / Test | Radiant Nuclear | Microreactor (1.2 MW) | 1.2 MW | Research / Under Construction | 2026 | First demonstration unit for Equinix/market validation |
| **Prometheus Hyperscale + Conduit Power** — Kaufman County, Texas (west of Dallas) | Prometheus Hyperscale | Conduit Power (Jenbacher J620 gas engines + ENGIE BESS) | Gas engines + battery storage (hybrid BTM) | Up to 300 MW per site (2 sites) | Contracted | 2026 (first sites) | Liquid-cooled AI-ready campus; 500 acres; hybrid bridge+backup power; ENGIE battery co-location |
| **Fervo Cape Station** — Southwest Utah | Multiple (data center customers TBD) | Fervo Energy | Enhanced geothermal (EGS) | 500 MW (100 MW phase 1 online 2026; 400 MW by 2028) | Under Construction | 2026 (phase 1) | First commercial-scale EGS; BTM-capable; geothermal baseload, 24/7 carbon-free |
| **Meta + Sage Geosystems** — U.S. (location TBD) | Meta | Sage Geosystems | Advanced geothermal | Up to 150 MW | Contracted | 2027 (initial stage) | Baseload clean power for Meta data center operations |
| **International Electric Power** — Pennsylvania | Unnamed data center operator | International Electric Power | Gas plant + battery storage | 944 MW | Contracted | 2026–2027 | Avoiding PJM interconnection; BTM gas plant + BESS |

**Note on project status:**
- **Operating:** Facility online and generating power for data centers
- **Under Construction:** Physical construction underway; expected completion within 12–24 months
- **Contracted:** Binding power purchase agreement (PPA) or supply contract signed; pre-construction or early construction
- **LOI only:** Letter of Intent or nonbinding framework agreement; no binding commitment or hard timeline

---

## Company Landscape

### Startups & Development Partners (Power Generation Focus)

| Company | HQ | Stage | Technology | Target | Recent News |
|---------|-----|-------|-----------|--------|-------------|
| [Oklo]({{< relref "oklo-btm.md" >}}) | Santa Clara, CA | Public (NYSE: OKLO) | SMR, sodium-cooled fast reactor | Data centers | Aurora unit 1 groundbreaking Sept 2025; 18 GW order book |
| [Kairos Power]({{< relref "kairos-power-btm.md" >}}) | Albuquerque, NM | Private (Series C+) | Molten-salt SMR | Data centers, industrial | **Hermes 2 groundbreaking April 17, 2026** — first Gen IV NRC construction permit; first commercial-scale advanced reactor under construction; Google 500 MW deal |
| [X-energy]({{< relref "x-energy.md" >}}) | Greensboro, NC | Private (Series D, $700M raised) | High-temp gas-cooled SMR | Data centers, hydrogen | Amazon 5 GW partnership (2025) |
| [Blue Energy]({{< relref "blue-energy.md" >}}) | Cambridge, MA | Private (funded by MIT, The Engine) | SMR (size TBD) | Data centers | Crusoe partnership for Port of Victoria project |
| [TerraPower]({{< relref "terrapower-btm.md" >}}) | Seattle, WA | Private (Bill Gates backed) | Sodium-cooled fast SMR (Natrium) | Data centers, industrial heat | Meta 8-unit deal (2.76 GW); Sabey MOU |
| [Radiant Nuclear]({{< relref "radiant-nuclear.md" >}}) | Los Altos, CA | Private (Series C+, $300M+ raised) | HTGR microreactor (Kaleidos) | Data centers, remote power | Equinix 20-unit preorder; INL DOME demonstration |
| [Westinghouse (eVinci)]({{< relref "westinghouse-evinci.md" >}}) | Pittsburgh, PA | Subsidiary (Brookfield Asset Management / Cameco JV) | Heat-pipe microreactor | Data centers, remote, military | NRC PDC approval; Penn State partnership |
| [Boom Supersonic (Superpower)]({{< relref "boom-supersonic-superpower.md" >}}) | Denver, CO | Private (recent funding rounds, aerospace heritage) | Aeroderivative gas turbine (42 MW) | Data centers | Crusoe 29-unit order (1.21 GW); $300M funding announced |
| [Bloom Energy]({{< relref "bloom-energy-sofc.md" >}}) | San Jose, CA | Public (NASDAQ: BE) | Fuel cell (SOFC) | Data centers, commercial, industrial | Oracle 2.8 GW MSA (April 2026; 1.2 GW deployed + expanding); 55-day delivery record; BE stock +150% YTD; Brookfield $5B partnership |
| [NANO Nuclear / USNC (KRONOS MMR)]({{< relref "usnc-microreactor.md" >}}) | Seattle, WA | Private (acquired USNC IP, 2025) | HTGR microreactor (KRONOS MMR) | Data centers, industrial | USNC bankruptcy; NANO acquisition (March 2025); INL DOME demo |

### Public Companies (Power Generation & Equipment)

| Ticker | Company | HQ | Focus | Data Center Role | Status |
|--------|---------|-----|-------|-----------------|--------|
| [OKLO](https://finance.yahoo.com/quote/OKLO) | [Oklo]({{< relref "oklo-btm.md" >}}) | Santa Clara, CA | SMR (Aurora) | End-user power + OEM | Public May 2024; growing order book |
| [BE](https://finance.yahoo.com/quote/BE) | [Bloom Energy]({{< relref "bloom-energy-sofc.md" >}}) | San Jose, CA | Fuel cells (SOFC) | Distributed BTM power (500 kW–50 MW modules) | Oracle 2.8 GW MSA (April 2026); BE stock +150% YTD; 2 GW annual prod target |
| [SMR](https://finance.yahoo.com/quote/SMR) | [NuScale Power]({{< relref "nuscale-power.md" >}}) | Portland, OR | SMR (VOYGR, 77 MWe modules) | Grid-connected SMR plants for DC PPAs | Only NRC SDA-approved SMR; post-UAMPS pivot to data center market; class action lawsuits; stock down 70%+ |
| [WRTBV](https://finance.yahoo.com/quote/WRTBV.HE) | [Wärtsilä]({{< relref "wartsila-btm.md" >}}) | Helsinki, Finland | Gas engines, turbines | Reciprocating engines (5–50 MW class) | Cumulative 2.4+ GW booked for U.S. data centers; 790 MW Texas order April 2026 |
| [CAT](https://finance.yahoo.com/quote/CAT) | [Caterpillar]({{< relref "caterpillar-solar-turbines.md" >}}) | Peoria, IL | Gas turbines (Solar Turbines subsidiary) | Mid-sized turbines (1–39 MW) | Vertiv partnership (Nov 2025) |
| [CGEH](https://finance.yahoo.com/quote/CGEH) | [Capstone Green Energy]({{< relref "capstone-green-energy.md" >}}) | Van Nuys, CA | Micro-turbines (65 kW – 1 MW) | Small-scale CHP for colocation DCs; new 800 VDC AI product | ~$103M TTM revenue; ITC phaseout headwind; expanding to AI edge |
| [SIEGY](https://finance.yahoo.com/quote/SIEGY) | [Siemens Energy]({{< relref "siemens-energy-btm.md" >}}) | Munich, Germany | Gas turbines (SGT series), power plants | Modular 500 MW plants (Eaton partnership) | Nearly doubled turbine sales (194 units 2025 vs 100 in 2024) |

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
        "title": "BTM Power",
        "symbols": [
          {"s": "NYSE:OKLO", "d": "Oklo"},
          {"s": "NASDAQ:BE", "d": "Bloom Energy"},
          {"s": "NYSE:SMR", "d": "NuScale Power"},
          {"s": "NYSE:CAT", "d": "Caterpillar"},
          {"s": "NASDAQ:CGEH", "d": "Capstone Green Energy"},
          {"s": "XETR:ENR", "d": "Siemens Energy"}
        ],
        "originalTitle": "BTM Power"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents & Tier-1 OEMs

| Company | HQ | Power Generation Products | Data Center BTM Role | Notes |
|---------|-----|-------------------------|----------------------|-------|
| [GE Vernova]({{< relref "ge-vernova-aeroderivative.md" >}}) | Boston, MA | Aeroderivative turbines (LM2500XPRESS, LM6000), gas turbines | 29 LM2500XPRESS for Crusoe (1 GW+); 29 for Stargate; $2.4B in Q1 2026 data center electrification orders | Dominant aeroderivative supplier; Q1 2026 record orders; 2026 rev guidance raised to $44.5–$45.5B |
| [Mitsubishi Power](https://www.mhi.com/en/products/power/thermal-power-generation.html) | Tokyo, Japan | Heavy-frame & aeroderivative turbines | Limited datacenter BTM orders (2025); supply constrained | Competing with Siemens for large plant orders |
| [Solar Turbines (CAT subsidiary)]({{< relref "caterpillar-solar-turbines.md" >}}) | San Diego, CA | Industrial gas turbines (1–39 MW class) | CHP & mid-sized BTM applications | Vertiv partnership signals move toward integrated datacenter solutions |
| [GE Hitachi (BWRX-300)]({{< relref "ge-hitachi-bwrx300.md" >}}) | Wilmington, NC | Water-cooled SMR | Google-compatible; not yet deployed for datacenters | Larger reactor (300 MW); more suitable for regional clusters |
| [Eaton](https://www.eaton.com/) | Dublin, Ireland | Power distribution, electrical equipment | Integration partner with Siemens Energy (2025) | End-to-end power plant + cooling solutions |

---

## Regulatory & Competitive Friction Points

### ⚑ Grid Operator Opposition to BTM Arbitrage

**The issue:** BTM power bypasses traditional grid interconnection review, transmission planning, and capacity reserve requirements. Grid operators view this as "regulatory arbitrage" — operators are sidestepping:
- Interconnection queue review (which enforces load-serving obligation and grid stability studies)
- Transmission cost allocation (BTM avoids paying for transmission maintenance)
- Capacity reserve mandates (utilities traditionally procure reserve capacity; BTM operators self-procure)

**2025–2026 developments:**
- **Texas:** Deregulated market (ERCOT) has been most permissive of BTM; no major opposition yet
- **California:** Grid operator (CAISO) and state regulators are increasingly requiring BTM projects to meet grid stability standards; some projects face delays
- **PJM (Northeast):** Interconnection queue for grid-parallel backup has become more restrictive; utilities pushing for "must serve the grid" clauses on backup generators

**Outcome:** Expect litigation 2026–2028 over whether BTM projects should be subject to interconnection review. Some regions may impose new BTM permitting requirements.

---

### ⚑ Air Quality Permitting — Gas Turbine / Engine Projects

**The issue:** Natural gas turbines and reciprocating engines emit NOx, particulate, and CO2. State environmental agencies (California Air Resources Board, Texas Commission on Environmental Quality, others) have tightened standards for new combustion facilities.

**2025 experience:**
- **Texas (Abilene Crusoe project):** Initial air quality permitting faced 18+ month delay; resolved through low-emission turbine selection (SCR-equipped GE Vernova units)
- **California:** New data center BTM gas projects face heightened scrutiny; some face 24+ month permit review
- **Pennsylvania:** Faster permitting than CA/NY for natural gas (legacy coal/gas infrastructure precedent)

**Outcome:** Air permitting will add 12–24 months to gas BTM projects in CA, NY, New England. Texas and Louisiana remain faster. Hydrogen-capable turbines may receive preferential permitting path (zero-emission ready).

---

### ⚑ Nuclear Siting & Local Opposition

**SMR/microreactor specific:**
- **NRC pre-application review:** First-of-a-kind designs (Oklo Aurora, Kairos, X-energy, Radiant) are in pre-application phase; formal Combined License Applications (COLA) remain 12–24 months away for most
- **Local/state opposition:** Communities sometimes object to nuclear facilities (even small, safe-by-design reactors). Oklo's first deployment (INL) faced no significant local opposition (federal site). Future datacenter-sited SMRs may face community review periods
- **Fuel supply:** HALEU enrichment capacity and TRISO fuel supply are the real bottleneck, not licensing

**Outcome:** First SMR datacenter deployments (2027–2028) will likely occur at federal sites (INL, INEEL-adjacent) or data-center-owned facilities in permissive states (Wyoming, Texas). Coastal or densely-populated siting will face delays.

---

### ⚑ Carbon Claims & Fuel Source Transparency

**The issue:** Hyperscalers market "24/7 carbon-free" energy. But:
- **Natural gas BTM:** 75% of identified BTM generation is natural gas — not carbon-free. Marketing claims of "clean energy" are false unless paired with renewable PPAs or offsets
- **Fuel cell BTM:** Today running mostly on natural gas (not carbon-free). Green hydrogen path unproven at scale
- **Nuclear BTM:** Genuinely 24/7 carbon-free, but data centers must clearly mark nuclear power separately from gas generation in sustainability disclosures
- **Solar+storage BTM:** Zero-emission at point of generation, but batteries and grid backup still needed for overnight/winter

**2025 developments:** California and EU regulators are increasingly requiring energy source transparency in sustainability claims. Expect SEC enforcement action against hyperscalers mis-claiming "clean energy" from gas-BTM projects. This will drive renewed interest in nuclear and fuel-cell BTM.

---

### ⚑ Supply Chain Constraints (2026–2030)

**Gas turbines:** Aeroderivative turbine supply is constrained. GE Vernova, Siemens, Mitsubishi all report 24+ month lead times for new orders (as of Q4 2025). This is the binding constraint for gas BTM projects in 2026–2027. Heavy-frame turbines face even longer queues.

**HALEU fuel:** Enrichment capacity is the bottleneck for Oklo, X-energy, and Kairos deployments. Oklo secured INL inventory for first unit, but commercial-scale HALEU supply (beyond ~2–4 GW cumulative) is unresolved. This will likely cap first-wave SMR deployments to 2–4 units per developer by 2030.

**TRISO fuel:** BWXT is the sole U.S. TRISO supplier. Capacity is adequate for current pipeline (~5 GW by 2030), but supply may tighten for second-wave deployments (2031+).

**NRC licensing bandwidth:** NRC staff is stretched thin. First-of-a-kind reviews are taking 18–36+ months longer than standard LWR reviews. This is a soft constraint (can be resolved by adding staff), but it is affecting schedules.

---

## Cross-Links to Energy Section

For detailed profiles on nuclear SMR and microreactor developers, see the Energy section:
- {{< relref "../../energy/nuclear/oklo.md" >}}
- {{< relref "../../energy/nuclear/kairos-power.md" >}}
- {{< relref "../../energy/nuclear/x-energy.md" >}}
- {{< relref "../../energy/nuclear/terrapower.md" >}}
- {{< relref "../../energy/nuclear/blue-energy.md" >}}
- {{< relref "../../energy/nuclear/ge-hitachi-bwrx300.md" >}}

---

## Key People: Executives & Technologists

### Oklo
- **Jacob DeWitte** (CEO, co-founder) — MIT nuclear engineering background; prior energy startup experience
- **Caroline Cochran** (COO, co-founder) — Business/operations focus; prior cleantech scaling experience
- **Sam Altman** (Chairman) — OpenAI CEO; SPAC investor/promoter; driving hyperscaler awareness

### Kairos Power
- **Chris Levesque** (CEO) — Prior TerraPower SVP; deep advanced reactor experience; recruiting talent from Oklo competitors

### X-energy
- **Clay Siegall** (CEO, co-founder) — PhD nuclear engineering (Georgia Tech); prior Lightbridge startup; technical credibility

### Radiant Nuclear
- **Zeke Hausfather** (CEO, board) — Climate/energy policy background; raised $300M+ Series C (Dec 2025)
- **Eric Ingersoll** (Board, consultant) — Former NRC official; key licensing advisor

### Bloom Energy
- **KR Sridhar** (CEO, founder) — MIT researcher; prior fuel cell technology pioneer; serial entrepreneur

### Boom Supersonic
- **Blake Scholl** (CEO, founder) — Aerospace engineer; founded Boom for supersonic aircraft; pivoting Superpower to datacenters (Series B+ funding)

### Westinghouse (eVinci)
- **Patrick Fragman** (President & CEO, Westinghouse Electric) — Brookfield Asset Management oversight; transitioning to advanced reactor focus

### GE Vernova
- **Scott Strazik** (CEO, GE Vernova Gas Power) — Gas turbine executive; driving data center turbine sales ramp

### Siemens Energy
- **Christian Bruch** (CEO, Siemens Energy) — Raised mid-term financial targets on datacenter turbine demand (2025)

### Wärtsilä
- **Jaakko Eskola** (CEO) — Engine maker; cumulative 2.4+ GW in U.S. data center orders as of April 2026

---

## 2026–2027 Watch List: Critical Inflection Points

1. **✅ Kairos Hermes 2 groundbreaking (April 17, 2026):** COMPLETED — first Gen IV reactor under NRC construction permit; construction of first commercial-scale advanced reactor in U.S. now underway. Watch for: operating license application submission (expected mid-2026), first concrete pour, equipment module deliveries from Albuquerque.

2. **First Oklo Aurora criticality (target late 2027):** Will demonstrate sodium-cooled fast reactor commercial viability; signals to Meta, Switch, Equinix that order-book projects will move forward

3. **Kairos Hermes 2 operating license (2026–2028):** Operating license application expected mid-2026; NRC review 18–24 months; successful issuance clears path to power generation ~2030

4. **Fuel supply resolution for HALEU (2026–2027):** Will determine whether Oklo, X-energy, and Kairos can scale beyond 2–4 units each. If HALEU remains constrained, SMR datacenter deployments will plateau at ~5–10 GW by 2030

4. **Grid operator push-back lawsuits:** Expect first litigation 2026–2027 over BTM regulatory arbitrage. Outcome will determine whether BTM remains open or becomes more tightly regulated state-by-state

5. **Gas turbine supply easing (2027+):** If GE Vernova, Siemens, and Mitsubishi bring new capacity online, lead times will drop from 24+ months to 12–18 months. This could accelerate gas-BTM projects 2027–2028

6. **Hyperscaler carbon disclosure & enforcement:** SEC or state regulators may force restatement of "carbon-free" claims on gas-BTM projects. This will create demand for nuclear/fuel-cell BTM and solar+storage (true zero-emission)

---

## Summary: Why BTM Data Center Power Matters

Behind-the-meter power is reshaping the energy infrastructure of the 2030s. Grid constraints, AI workload intensity, and time-to-market pressure have made BTM the only viable path to powering 10–20 GW of new data center capacity by 2030. **Expect BTM to absorb 30–50% of new U.S. data center power by 2030.**

Winner-takes-most dynamics are emerging: Oklo and Kairos (if HALEU supply resolves) will likely dominate SMR datacenter segment; Bloom Energy and Wärtsilä will dominate distributed fuel-cell and gas-engine sectors; Crusoe and Boom Supersonic will drive aeroderivative turbine deployments. Incumbent utilities will face pressure to innovate on distributed power, CHP, and hybrid BTM models.

Regulatory friction (grid operator opposition, air permitting delays, HALEU supply constraints) will compress deployment timelines and increase capital requirements. **First-mover advantage is critical: projects deployed 2026–2028 will set operational precedent and inform supply chain scaling for 2030+.**
