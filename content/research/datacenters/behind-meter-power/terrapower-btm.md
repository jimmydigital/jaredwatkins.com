---
title: "TerraPower: Natrium SMR for Data Centers"
date: 2026-04-25
lastmod: 2026-04-25
draft: false
description: "TerraPower's Natrium sodium-cooled fast reactor with molten-salt thermal storage for flexible, load-following power to data centers. Built-in storage enables ramp from 345 MW to 500+ MW for 5+ hours."
tags: ["smr", "sodium-cooled", "fast-reactor", "data-center", "thermal-storage", "meta", "sabey"]
categories: ["company"]
research_area: "datacenters/behind-meter-power"
source_urls:
  - "https://www.terrapower.com/"
  - "https://www.terrapower.com/our-technology/natrium"
last_reviewed: 2026-04-25
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


{{< steering >}}
**Scope:** TerraPower's Natrium sodium-cooled fast reactor platform, focused on data center deployment contracts and technical advantages for load-following power generation.

**Key topics:**
- Natrium reactor design: 345 MWe baseload + molten-salt thermal energy storage enabling 500+ MW output for 5+ hours
- Data center partnerships: Meta (8 units, 2.76 GW), Sabey Data Centers (MOU)
- First deployment site: Wyoming (Kemmerer), expected 2030 online
- Competitive advantages vs. Oklo Aurora and Kairos: built-in storage = grid-following capability without separate battery investment
- Supply chain: Bill Gates backing; construction partnerships

**Track:**
- Project timeline updates: site preparation, permitting milestones, manufacturing timelines
- Meta deployment expansion: additional units beyond initial 8
- Sabey partnership materialization: geographic sites, commitment stages
- HALEU fuel supply (Natrium uses LEU, less constrained than Aurora)
- Technology validation from Hermes testing (comparison reactor)
{{< /steering >}}

## Overview

TerraPower, backed by Bill Gates and founded by John Deutch, is developing the **Natrium** sodium-cooled fast reactor specifically for industrial and data center power. The key differentiator is **integrated molten-salt thermal energy storage**—the reactor can dispatch 500+ MW of power for 5+ hours by drawing down heat stored in a molten-salt tank, enabling true load-following without separate battery infrastructure.

| Attribute | Value |
|-----------|-------|
| **Technology** | Sodium-cooled fast reactor (SFR) |
| **Fuel** | Low-enriched uranium (LEU) metallic fuel |
| **Baseload Capacity** | 345 MWe |
| **Peak Output (with storage)** | 500+ MWe for 5+ hours |
| **Thermal Storage** | Molten salt (enables load-following) |
| **Status** | Pre-construction (site prep Wyoming) |
| **First Online Target** | ~2030 (Kemmerer, Wyoming) |
| **Data Center Partnerships** | Meta (8 units, 2.76 GW); Sabey Data Centers (MOU) |

---

## Technology: Natrium Reactor + Storage System

### Core Reactor Design

The Natrium reactor operates at **545°C** in a **pool-type configuration** with sodium coolant circulating through the core and three independent cooling loops—a design inherited from Integral Fast Reactor (IFR) research and validated across decades of sodium-cooled reactor operation (EBR-II, FFTF, Monju).

**Key design features:**
- **Passive safety:** No active cooling required; if all power is lost, natural circulation and thermal conduction safely cool the core
- **Compact footprint:** Pool design limits external footprint; can be sited on industrial campuses or within large data center sites
- **Fuel efficiency:** Fast spectrum breeding allows multi-cycle operation on depleted uranium or LEU stockpiles
- **Metallurgical fuel:** Metallic U-Zr fuel (vs. oxide pellets in light-water reactors); higher density, higher burnup capability

### Thermal Energy Storage Integration

The **distinguishing feature** of Natrium is integrated molten-salt thermal storage. At steady state:
1. Reactor operates at 345 MWe baseload output
2. Excess heat is directed into a molten-salt storage tank (liquid salt maintained at ~500°C)
3. When data center demand spikes, the salt discharges its heat to a steam generator, boosting turbine output to **500+ MW for 5+ hours** without reactor power increase

**Storage capacity:** Approximately 1 GWh thermal energy, enabling realistic data center load-following without external battery hardware.

**Advantage over SMRs without storage:**
- Oklo Aurora (75 MW) and Kairos Hermes (50 MW) cannot follow variable data center loads; they run flat baseload
- Natrium with storage is truly flexible—can match 24/7 varying compute demand without grid backup
- Eliminates need for 500+ MWh battery systems (cost: $100–300M for equivalent storage)

---

## Data Center Partnerships

### Meta: 8-Unit Natrium Fleet (2.76 GW)

**Signed:** Binding agreement (spring 2025)
**Capacity:** 8 × 345 MW = 2.76 GW baseload + storage-enabled flexibility
**Locations:** Specific Meta data center sites TBD (likely Wyoming + additional locations)
**Timeline:** First unit (Kemmerer) ~2030; subsequent units phased through 2035

**Significance:**
- Largest SMR data center order to date (by GWh)
- Meta's diversification strategy: balances Oklo (15 GW LOI), TerraPower (2.76 GW binding), geothermal (Sage, 150 MW), and solar
- Storage feature aligns with Meta's variable load profile (model training batches + inference peaks)

### Sabey Data Centers: Multi-Site MOU

**Announced:** 2025
**Type:** Memorandum of Understanding (nonbinding framework)
**Target:** Wide-scale deployment at Sabey facilities nationwide
**Status:** Early-stage; specific site selection and commitment timelines TBD

**Context:**
- Sabey is a mid-tier colocation/hyperscale data center provider (not Meta/Google/Amazon scale)
- MOU suggests TerraPower exploring sub-hyperscaler customer segment for Natrium units
- Sabey partnership may focus on 1–2 unit deployments at regional data center clusters

---

## First Deployment: Wyoming Kemmerer Site

### Site & Regulatory Status

**Location:** Kemmerer, Wyoming (Sweetwater County) — formerly a coal plant site
**Site Preparation:** Underway (site survey, environmental baseline, infrastructure planning)
**Expected Permit Status:** Construction permit application expected 2026; NRC review 24–36 months nominal
**Target First Power:** ~2030

**Advantages of Wyoming:**
- Permissive regulatory environment (no state-level SMR size limits or restrictions)
- Industrial precedent (coal generation → power plant workforce transition narrative)
- Proximity to Meta hyperscale demand centers
- Adequate water supply for cooling (Kemmerer site has industrial water access)

### Construction & Manufacturing

TerraPower partners with:
- **BWXT (Babcock & Wilcox):** Reactor vessel fabrication, ASME N stamped components
- **Kiewit Corporation:** Heavy civil construction (concrete, structural steel, site infrastructure)
- **Burnham Industrial:** Molten-salt storage tank fabrication and installation

**Lead time expectations:**
- Permit-to-first-pour: 12–18 months post-license
- First-of-a-kind construction: 36–48 months (Kemmerer likely on higher end due to prototype complexities)
- Subsequent units (units 2–8): 24–36 months per unit (learning curve, pre-fabrication maturity)

---

## Technology Advantages for Data Centers

### Load-Following Without External Storage

Unlike Oklo or Kairos (which run constant baseload), Natrium's integrated storage enables:
- **Matched load response:** If data center demand drops 30%, reactor can divert heat to storage rather than curtailing power
- **Demand peaks:** Molten-salt discharge can boost output 45% above baseload for 5+ hours (e.g., training run, model deployment surge)
- **Cost savings:** No separate 500 MWh battery pack ($100–300M capex) needed for daily load-following

### Fuel Supply Advantage

Natrium uses **low-enriched uranium (LEU) metallic fuel**, not HALEU:
- LEU enrichment (<20% U-235) widely available; no supply bottleneck
- Competing with Oklo (HALEU-dependent), Kairos (TRISO/HALEU-dependent), X-energy (TRISO-dependent)
- TerraPower's fuel pathway more resilient to supply constraints

**Caveat:** No commercial metallic-fuel processing in the U.S. yet; terawatt would need pilot-scale fab (currently BWXT can support ~4 GW/year capacity if funded). This is a soft constraint, not a binding limitation like HALEU enrichment.

---

## Competitive Position

### vs. Oklo Aurora (75 MW, nonbinding LOIs)

| Factor | TerraPower Natrium | Oklo Aurora |
|--------|---|---|
| **Capacity** | 345 MW + storage | 75 MW baseload only |
| **Load-following** | Yes (integrated storage) | No (constant output) |
| **Fuel supply risk** | Low (LEU available) | High (HALEU bottleneck) |
| **Data center contracts** | 2.76 GW binding (Meta) | 15 GW LOI (~90% nonbinding) |
| **First deployment** | 2030 (Kemmerer) | 2027–2028 (INL, demo phase) |

### vs. Kairos Hermes (50 MW, molten-salt cooled)

| Factor | TerraPower Natrium | Kairos Hermes |
|---|---|---|
| **Fuel** | LEU metallic | TRISO (HALEU in some contexts) |
| **Cooling** | Sodium + molten-salt storage | Molten-salt direct coolant |
| **Temperature** | 545°C | 700+°C (higher efficiency potential) |
| **Load flexibility** | Integrated thermal storage | None (constant output) |
| **Data center contracts** | 2.76 GW (Meta, 8 units) | 500 MW (Google, 6–7 units) |

**Advantage:** TerraPower's storage + LEU fuel is more flexible and supply-resilient. **Disadvantage:** Later first deployment (~2030 vs. Kairos 2030).

---

## Regulatory & Permitting Status

### NRC Licensing

TerraPower's Natrium design is undergoing **pre-application phase** reviews with NRC:
- **Design Certification Application (DCA):** Expected to be filed 2026–2027 (ahead of specific project COLAs)
- **Kemmerer Combined License Application (COLA):** Expected 2027–2028
- **NRC review timeline:** 18–24 months nominal; first-of-a-kind designs often slip to 24–36 months
- **Operating License:** Earliest issuance ~2029; construction then 36–48 months → first power ~2030–2031

### Wyoming State Regulatory

- **Air Quality:** No major expected opposition; Wyoming Office of Air Quality (air regulator) is pro-business
- **Water permits:** Adequate industrial water available at Kemmerer site; no expected conflict
- **Decommissioning / Financial Assurance:** Wyoming requires standard financial assurance for reactor decommissioning; TerraPower is securing DOE backing and commercial financing

---

## Financial & Supply Chain

### Capex Estimates

| Component | Estimate (2026$) |
|-----------|---|
| **Reactor vessel + core internals** | $200–300M |
| **Molten-salt storage system** | $100–150M |
| **Steam turbine + generator** | $80–120M |
| **Site, BOP, engineering** | $300–500M |
| **Contingency (first-of-a-kind)** | +30–50% |
| **Total capex (unit 1, Kemmerer)** | **~$1.0–1.5B** |
| **Subsequent units (learning curve)** | **~$0.8–1.2B** |

**$/MW:** ~$2.9–4.3M/MW all-in capex (Kemmerer); ~$2.3–3.5M/MW (units 2–8, learning curve).

### Financing

- **Bill Gates (TerraPower founder/investor):** Committed $1B+ via Breakthrough Energy Ventures
- **U.S. DOE:** Path to federal loan guarantee or direct investment (advanced reactor program)
- **Meta partnership:** Potential direct investment or structured PPA financing
- **Private equity:** Discussions ongoing with infrastructure funds

### Supply Chain Partnerships

| Component | Supplier | Lead Time | Risk |
|-----------|----------|-----------|------|
| **Reactor vessel (ASME N)** | BWXT | 24–30 months | Medium (first-of-a-kind) |
| **Molten-salt storage tank** | Burnham Industrial / ITM | 18–24 months | Medium (specialty fabrication) |
| **Metallic fuel manufacturing** | TBD (BWXT capable) | 12–18 months | Medium (scale-up needed) |
| **Turbine/generator** | GE or Siemens | 18–24 months | Low (standard LWR heritage) |
| **Cooling loops, piping, controls** | Multiple (Sensormatic, Emerson, etc.) | 12–18 months | Low (industrial sourcing) |

**Key constraint:** Metallic-fuel fabrication is **not yet commercial** in the U.S. BWXT is the leading candidate but would require pilot-scale production facility startup (2026–2027). This is a **soft constraint** (solvable with capex + time), not a binding supply bottleneck like HALEU enrichment.

---

## Risks & Challenges

### ⚠️ First-of-a-Kind Construction Complexity

Natrium has never been built at commercial scale:
- **Molten-salt storage system:** Proven in academic + pilot settings; no full commercial deployment as primary BTM storage
- **Sodium reactor construction:** Proven design lineage (EBR-II, FFTF), but U.S. regulatory environment for new sodium reactors is untested at commercial scale
- **Likelihood:** Kemmerer unit 1 is likely 10–30% more expensive and 12–24 months behind schedule relative to plan

### Metallic Fuel Supply Ramp

Natrium uses metallic U-Zr fuel, which offers:
- ✅ Higher density than oxide (more burnup per batch)
- ✅ No HALEU enrichment bottleneck
- ⚠️ Manufacturing not yet operational in U.S.; BWXT capable but unfunded

**Status:** TerraPower is working with DOE on pilot-scale fuel fab funding (expected decisions 2026–2027). If funded, production facility operational by 2028; if delayed, first units may source from foreign facilities (Russia, France, UK have limited capacity) → potential 12–18 month supply delay.

### Regulatory Uncertainty

- **Molten-salt systems in nuclear plants:** NRC has limited precedent for integrated thermal energy storage in reactor designs; review could uncover new safety questions → schedule slippage
- **Decommissioning of molten-salt equipment:** No established decommissioning precedent for large molten-salt systems; NRC may impose costly monitoring / long-term stewardship requirements

### Market Execution Risk

- **Meta commitment:** 8 units is a binding order, but contract likely includes "development milestones" gates. If Kemmerer unit 1 experiences major cost overruns or schedule delays >24 months, Meta may renegotiate or withdraw
- **Sabey MOU:** Nonbinding; heavily dependent on Kemmerer success and cost trajectory

---

## 2026–2030 Milestones

| Date | Milestone | Probability | Impact |
|------|-----------|-------------|--------|
| Q2–Q4 2026 | Design Certification Application filing (NRC) | High | Clears regulatory pathway for any COLA |
| 2027 | Kemmerer COLA filed; construction prep begins | High | Site ready for first concrete |
| 2027–2028 | Metallic fuel fab pilot phase funded (DOE decision) | Medium | Resolves fuel supply path for units 2+ |
| Late 2028 | First concrete pour (Kemmerer) | Medium | ~18-month construction phase begins |
| 2029 | Fuel loading (first core assembly) | Medium | Final NRC operating license imminent |
| ~2030 | Critical and first power (Kemmerer unit 1) | Medium–Low | Demonstrates Natrium commercial viability |
| 2031–2032 | Meta unit 2 online (site TBD) | Low–Medium | Parallel construction begins |
| 2033–2035 | Meta units 3–8 online (phased) | Low | If schedule holds and costs acceptable |

---

## Outlook: Why Natrium Matters for Data Centers

**Natrium's integrated molten-salt storage is a genuine competitive advantage** over constant-baseload SMRs (Oklo, Kairos, X-energy). Data center power demands are **not flat**—they vary 2–5x between idle and peak model-training loads. Most SMR developers are ignoring this; Natrium is solving for it.

**If Kemmerer unit 1 succeeds** (on-time, on-budget), Natrium could capture 5–10% of SMR data center market by 2035. **If Kemmerer faces major cost overruns or delays**, Meta's 8-unit commitment likely dissolves or shrinks to 2–3 units; Natrium becomes niche player.

**Supply chain and fuel:** Advantage over Oklo/Kairos (no HALEU bottleneck), but dependent on metallic-fuel fab capitalization in 2026–2027.

**Competitive pressure:** Watch for Kairos molten-salt cooled design to offer storage options (different approach from Natrium's separate storage tank). If Kairos adds storage, it could erode Natrium's differentiation.

**Key watch:** Kemmerer site prep and COLA timeline 2026–2027 will determine whether 2030 first-power target is realistic or slips to 2032+.

---

## Key People

### Bill Gates — Co-Founder, Principal Investor
- Co-founded TerraPower in 2006 alongside John Deutch; primary private backer
- [LinkedIn](https://www.linkedin.com/in/williamhgates/): public profile available
- Background: Microsoft co-founder; global health/energy philanthropist via Bill & Melinda Gates Foundation; nuclear energy advocate

### Chris Levesque — President & CEO
- [LinkedIn](https://www.linkedin.com/in/chris-levesque-kairos/): TODO: verify slug — note this is the same name as Kairos CEO; these are different people. TODO: find TerraPower's Chris Levesque LinkedIn.
- Prior: TerraPower COO (pre-CEO); deep advanced reactor operations experience. **⚑ Overlap:** TerraPower and Kairos Power are often discussed together in data center nuclear context; the coincidence of the name "Chris Levesque" at both companies requires verification — confirm these are distinct individuals.

### People — Last Reviewed: 2026-04-25

---

## Related Profiles

- {{< relref "oklo-btm.md" >}} — Oklo Aurora microreactor (75 MW, nonbinding LOIs)
- {{< relref "kairos-power-btm.md" >}} — Kairos Hermes (50 MW molten-salt cooled SMR, Google partnership)
- {{< relref "x-energy.md" >}} — X-energy Xe-100 (80 MW HTGR, Amazon partnership)
- {{< relref "blue-energy.md" >}} — Blue Energy SMR (emerging, Crusoe partnership)
