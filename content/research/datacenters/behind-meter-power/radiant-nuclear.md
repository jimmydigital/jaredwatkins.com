---
title: "Radiant Nuclear: Kaleidos Microreactor for Data Centers"
date: 2026-04-25
lastmod: 2026-04-25
draft: false
description: "Radiant Nuclear's 1.2 MWe Kaleidos microreactor—high-temperature gas-cooled HTGR with HALEU/TRISO fuel. Equinix 20-unit preorder signals microreactor scaling for colocation data centers."
tags: ["microreactor", "htgr", "kaleidos", "equinix", "modular-nuclear", "data-center"]
categories: ["company"]
research_area: "datacenters/behind-meter-power"
source_urls:
  - "https://www.radiantnuclear.com/"
  - "https://www.equinix.com/"
last_reviewed: 2026-04-25
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


{{< steering >}}
**Scope:** Radiant Nuclear's Kaleidos microreactor platform—specifically the 1.2 MWe HTGR design, deployment strategy, and Equinix partnership. Focus on scalability, modular deployment, and microreactor market positioning.

**Key topics:**
- **Kaleidos design:** 1.2 MWe / ~5 MWth HTGR, HALEU TRISO fuel, helium coolant, factory-built modules
- **Deployment model:** Modular clustering (1.2, 2.4, 3.6, 4.8+ MW by stacking units) enables scaling from small colocation to large hyperscale campuses
- **Equinix preorder:** 20 units announced Aug 2025 (critical market validation signal)
- **Manufacturing strategy:** Factory construction + modular shipping; target 50 reactors/year by late 2020s
- **KDU demonstration:** Idaho National Lab (DOME facility) target 2026 startup
- **Competitive positioning:** vs. USNC KRONOS (larger, 15 MW), vs. Westinghouse eVinci (5 MW), vs. Oklo/Kairos (SMR baseload focus)
- **Capital structure:** Series C+ funding ($300M+ raised Dec 2025); Zeke Hausfather (CEO); Eric Ingersoll (NRC advisor on board)

**Track:**
- KDU startup and performance data (2026–2027)
- Equinix deployment site selection and timelines
- HALEU fuel supply agreements and bottleneck resolution
- Manufacturing ramp toward 50/year target
- Competitive differentiation vs. USNC/Westinghouse
- Technology validation (helium flow, TRISO thermal performance)
{{< /steering >}}

## Overview

**Radiant Nuclear** is developing the **Kaleidos microreactor**, a factory-built, modular high-temperature gas-cooled reactor (HTGR) designed for **distributed deployment at data center colocation facilities**. At 1.2 MWe per unit, Kaleidos is small enough to fit on a single truck, yet can be clustered to scale from 2.4 MW (two units) to 10+ MW (eight+ units) without significant site infrastructure.

| Attribute | Value |
|-----------|-------|
| **Technology** | High-temperature gas-cooled reactor (HTGR) |
| **Electrical Output** | 1.2 MWe per unit |
| **Thermal Output** | ~5 MWth per unit |
| **Fuel** | HALEU TRISO (pebble or prismatic blocks) |
| **Coolant** | Helium (passive, no pumps in emergency) |
| **Footprint** | <2 acres per unit |
| **Factory-Built** | Yes (modular containers, truck-transportable) |
| **Status** | KDU demonstration at INL; production target 2027–2028 |
| **Data Center Orders** | Equinix 20-unit preorder (Aug 2025) — 24 MW+ |
| **Capital Cost Target** | $40–60M per unit (if mass production achieved) |

---

## Technology: Kaleidos HTGR Design

### Core Reactor Physics

Kaleidos is a **pebble-bed or prismatic-block high-temperature gas-cooled reactor** (HTGR variant), operating at ~700–800°C helium outlet temperature:

**Design features:**
- **Helium coolant:** Inert, excellent heat transfer properties, no water corrosion concerns
- **TRISO fuel:** Tristructural Isotropic coated particles (uranium oxycarbide kernel surrounded by ceramic layers) — thermally and mechanically robust; can tolerate 1200°C+ peak temperatures
- **HALEU fuel:** Low-enriched uranium (typically 10–20% U-235), higher density than LEU but less restricted than weapons-grade HEU
- **Passive cooling:** No active pumps required in emergency; helium natural circulation cools the core to ambient via conduction through vessel walls
- **Walk-away-safe:** Core can withstand full loss of coolant and full loss of heat removal without melting — lowest decay heat, higher surface-to-volume ratio

### Factory Manufacturing Advantage

Unlike large LWRs (built on-site over 5+ years), Kaleidos units are **factory-constructed and shipped:**

1. **Modular construction:** Reactor vessel, steam generator, control systems all assembled in a factory (Radiant's planned Albuquerque-area facility or partner fab)
2. **Quality control:** 100% inspection and testing in controlled environment before shipment
3. **Transport:** Modules fit in standard truck containers or rail cars; no custom transport infrastructure required
4. **Site installation:** Plug-and-play setup; minimal on-site welding or heavy fabrication (weeks to months vs. years)
5. **Scaling:** Multiple units shipped to same site, assembled in parallel, commissioned independently or linked

**Timeline advantage:** Factory + transport + site assembly takes 12–18 months from order to power generation, vs. 36–48 months for on-site constructed SMRs.

### Modular Scaling Strategy

Radiant's key innovation is **scalability through clustering:**

| Configuration | Capacity | Footprint | Target Market |
|---|---|---|---|
| 1 unit | 1.2 MW | <2 acres | Small colocation, remote sites, research facilities |
| 2 units | 2.4 MW | <4 acres | Medium colocation facility |
| 4 units | 4.8 MW | <8 acres | Large colocation, hyperscale satellite campus |
| 6–8 units | 7.2–9.6 MW | <16 acres | Hyperscale primary data center site |

**Advantage:** Equinix (or any colocation player) doesn't have to commit to a single large reactor; can deploy 1–2 units initially, add capacity incrementally as site grows. This matches the **modular, incremental capex** of data center buildout.

---

## Market Opportunity: The Equinix Deal

### Equinix 20-Unit Preorder (August 2025)

**Announced:** August 2025
**Capacity:** 20 × 1.2 MWe = **24 MW+ deployed across multiple Equinix facilities**
**Timeline:** Phased deployment 2027–2030+
**Commercial terms:** Binding preorder with supply and deployment schedule milestones

**Significance:**

1. **Largest microreactor order to date:** 24 MW exceeds any single company's microreactor commitment
2. **Colocation validation:** Equinix operates 260+ data centers globally; 20-unit deployment spans multiple geographies and customers
3. **Production signal:** Equinix's order provides production volume certainty, enabling Radiant to scale manufacturing
4. **Competitive positioning:** Signals that colocation players (not just hyperscalers like Meta/Google) are betting on microreactors

**Strategic context:**
- Equinix generates revenue from customer power consumption; on-site nuclear BTM increases customer stickiness and SLA guarantees (99.99%+ uptime)
- 20-unit order diversifies Equinix's BTM portfolio (also evaluating Oklo SMRs, Bloom fuel cells, geothermal)
- Incremental deployment model matches Equinix's geographic expansion strategy

---

## Technology Validation: KDU Demonstration

### Kaleidos Demonstration Unit (KDU) at Idaho National Lab

**Location:** INL DOME facility (Dome Expansion Module — new experimental hall)
**Unit size:** 1.2 MWe / 5 MWth (full-scale commercial module)
**Target startup:** 2026 (as of this update; some slippage likely)
**Duration:** Minimum 18–24 months continuous operation

**Key milestones:**
- **Fuel loading:** Completion of HALEU TRISO fuel verification, loading into reactor
- **Criticality:** First chain reaction (confirms physics models)
- **Power ramp:** Step-wise increase from 10% to 100% power; validate thermal-hydraulics, control systems
- **Load-following tests:** Variable power output to simulate data center demand response
- **24/7 operation validation:** Minimum 1,000-day uninterrupted operation to demonstrate reliability

**Importance:** KDU is the **make-or-break milestone** for Radiant. Successful operation validates:
- TRISO fuel thermal performance under HTGR conditions
- Helium loop integrity and heat transfer
- Modular factory-built assembly and commissioning process
- Control system responsiveness and safety systems
- Data generation for NRC operating license applications

**Risk:** INL DOME facility has experienced delays due to infrastructure constraints. KDU startup could slip from target 2026 to 2027–2028.

---

## Regulatory & Licensing Path

### NRC Pre-Application Review

Radiant is in **pre-application phase** with NRC:
- **Design Certification Application (DCA):** Target filing 2026–2027 (non-specific to any plant)
- **Standard Design Certificate:** If approved, greatly accelerates individual project licensing
- **KDU DOME license:** Experimental reactor license; lower regulatory burden than commercial COLAs

### Equinix Site-Specific Licensing

For Equinix deployments, Radiant will pursue:
- **Site-specific Combined License Applications (COLAs):** One per facility or cluster of facilities
- **NRC review:** 18–24 months per COLA (standard path for established reactor designs; KDU validation + DCA may shorten this)
- **State/local siting:** Equinix facilities in various states; each may require state environmental review

**Advantage vs. larger SMRs:** Smaller reactor (1.2 MW) often faces less local opposition and simpler site reviews. Many Equinix colocation sites are industrial parks with existing infrastructure and permitting precedent.

---

## Manufacturing & Supply Chain

### Production Facility Plan

**Target:** 50 Kaleidos reactors/year by late 2020s
**Location:** Primary fab TBD (likely Albuquerque area or partnership with existing reactor OEM)
**Capex for fab:** Estimated $200–400M (factory, tooling, quality systems)
**Ramp timeline:** Pilot production 2027–2028 (10–15/year); scale to 50/year by 2029–2030

**Partners:**
- **Fuel supplier:** BWXT (TRISO) — shared bottleneck with Kairos, X-energy, USNC
- **Pressure vessel fabrication:** ASME-N stamped shops (heavy industrial suppliers)
- **Steam turbine/generator:** GE or Siemens (OEM surplus or custom small-scale units)
- **Instrumentation & control:** Conventional DCS suppliers (Siemens, Emerson, Foxboro)

### HALEU & TRISO Fuel Supply

**Risk:** TRISO fuel is a shared constraint across Kaleidos, Kairos Hermes, X-energy, and USNC KRONOS:
- **BWXT** is the sole U.S. TRISO supplier
- **Production capacity:** ~500–1,000 kg TRISO/year as of 2025; expanding to support SMR + microreactor pipeline
- **Radiant's need:** 20 units × 1.2 MW requires ~500 kg TRISO per year for supply + contingency
- **Competitive pressure:** If Kairos deploys 6–7 units (Google partnership) and X-energy scales, BWXT capacity may be exceeded by 2028–2030

**Mitigation:**
- Radiant is funding BWXT capacity expansion (co-investment)
- Exploring alternative TRISO sources (international suppliers, e.g., France, Japan)
- Possible fuel swap agreements with competitors (e.g., Radiant delays some units if Kairos needs priority fuel supply)

**Timeline concern:** TRISO supply may limit Equinix deployment to <10 units by 2030; full 20-unit order likely extends to 2032–2035.

---

## Competitive Landscape

### vs. USNC KRONOS MMR (15 MWe)

| Factor | Radiant Kaleidos | USNC KRONOS |
|--------|---|---|
| **Size** | 1.2 MWe (modular) | 15 MWe (larger unit) |
| **Technology** | Pebble-bed HTGR | Prismatic-block HTGR |
| **Fuel** | HALEU TRISO pebbles | HALEU TRISO prismatic |
| **Helium coolant** | Yes | Yes |
| **Factory-built** | Yes (small modules) | Partial (vessel only) |
| **Data center order** | 20 units (Equinix) | 0 units (pre-commercial) |
| **Demonstration** | KDU @ INL (2026+) | Pylon @ INL (2027+) |
| **Status** | Funded, Series C | Bankrupt (2024), acquired by NANO (2025) |

**Advantage:** Radiant's modularity and Equinix order provide credibility and production certainty. USNC bankruptcy and acquisition by NANO (mid-stage company) raised questions about KRONOS viability.

**Disadvantage:** Smaller unit (1.2 MW) means higher per-MW capital cost if not mass-produced. KRONOS's larger 15 MW size could offer better economics if successfully deployed.

### vs. Westinghouse eVinci (5 MW Heat-Pipe Microreactor)

| Factor | Radiant Kaleidos | Westinghouse eVinci |
|---|---|---|
| **Size** | 1.2 MWe | 5 MWe |
| **Technology** | Gas-cooled HTGR | Heat-pipe cooled (no working fluid pumping) |
| **Fuel** | HALEU TRISO pebbles | Metallic HALEU (TBD) |
| **Factory-built** | Yes (modules) | Yes (transportable containers) |
| **Data center orders** | 20 units (Equinix) | 0 units (pre-commercial) |
| **NRC status** | Pre-application | PDC (Principal Design Criteria) approved |
| **Partnership** | Equinix, INL DOME | Penn State (university pilot) |

**Advantage:** Kaleidos has proven data center market demand (Equinix) and factory-manufacturing experience. eVinci is larger unit, simpler cooling design, but unproven at commercial scale.

**Watch:** Westinghouse could rapidly scale eVinci if Penn State prototype succeeds and industry adopts it as standard. But as of April 2026, Kaleidos has stronger market validation.

### vs. Oklo Aurora & Kairos Hermes (SMRs, Baseload Focus)

| Factor | Radiant Kaleidos | Oklo Aurora | Kairos Hermes |
|---|---|---|---|
| **Size** | 1.2 MW (modular) | 75 MW | 50 MW |
| **Focus** | Colocation clustering | Hyperscale baseload | Hyperscale baseload + industrial heat |
| **Modularity** | Clusterable to multi-MW | Fixed unit size | Fixed unit size |
| **Data center contracts** | 24 MW (Equinix, binding) | 18 GW (90% LOIs, nonbinding) | 500 MW (Google binding) |
| **Market segment** | Colocation + edge | Hyperscaler internal | Hyperscaler internal |

**Radiant's niche:** Colocation players and mid-scale data center operators who want 1–5 MW increments, not 50–345 MW units. Equinix's 20-unit strategy is exactly this model.

---

## Capex & Economics

### Capital Cost Trajectory

**Unit 1 (KDU):** Estimated $60–100M (prototype, higher cost)
**Units 2–5 (pilot production):** ~$50–70M per unit
**Units 6–20 (scaling):** ~$40–60M per unit (target with 50/year production)
**Units 21+ (mature production):** ~$30–50M per unit (if 50+/year achieved)

**$/MW capital cost:**
- **Early units:** $42–83M/MW (high per-MW cost due to small unit size)
- **Mature production:** $25–50M/MW (if capital cost targets hit and volume ramps)

**Comparison:**
- SMRs (Oklo, Kairos): ~$2.5–4.0M/MW all-in
- Large gas turbines: ~$1.5–2.0M/MW
- Bloom fuel cells: ~$2–3M/MW

**Assessment:** Kaleidos per-MW capex is higher than SMRs or gas turbines at modest scales (1–5 MW). However, for colocation sites with existing infrastructure, **avoidance of large-scale site work, permitting delays, and regulatory queues** may justify the premium. Also, Equinix's revenue-per-MW-deployed is high; colocation economics differ from hyperscaler BTM.

### Levelized Cost of Power (LCOP)

**Assumptions:**
- Capex: $45M/unit × 1.2 MW = $37.5M/MW (mature production)
- Debt: 70% @ 5% interest
- Equity: 30% @ 12% return
- Capacity factor: 85% (data centers run ~24/7, slightly lower than grid baseload)
- O&M: $500–800K/unit/year (~$0.4–0.7M/MW/year)
- Fuel cost: Negligible (HALEU once-through fuel)
- Decommissioning reserve: ~$10M/unit amortized

**Estimated LCOP: $60–90/MWh (2026$)**

**Context:**
- Grid wholesale power (2025–2026): $30–60/MWh (varies by region)
- Bloom fuel cells (running on NG): $80–120/MWh levelized
- Solar + battery (100-hour storage): $100–150/MWh levelized
- Hyperscaler's grid interconnection + transmission: $40–80/MWh (including transmission charges)

**Interpretation:** Kaleidos's LCOP is **competitive with grid + transmission + reliability premium** in many data center markets, especially if colocation operators are willing to pay premium for 24/7 carbon-free + guaranteed availability.

---

## Risks & Challenges

### ⚠️ KDU Delay Risk

**Current target:** KDU startup 2026
**Realistic expectation:** Slippage to 2027–2028 is likely (INL DOME infrastructure constraints, NRC review bottlenecks)
**Impact:** Each 6-month delay pushes commercial production timeline back 12+ months (licensing relies on KDU data)

### ⚠️ TRISO Fuel Supply Bottleneck

Kaleidos uses HALEU TRISO, shared with:
- Kairos Hermes (50 MW Google contract)
- X-energy Xe-100 (5 GW Amazon contract, though distributed)
- USNC KRONOS (16 MW demo pipeline)

**BWXT capacity:** ~1,000 kg/year as of 2025; demand from all sources could exceed 1,500 kg/year by 2029 → **supply crunch**.

**Mitigation:** Radiant funding BWXT expansion, but capital and licensing timelines uncertain. Real risk: Equinix's full 20-unit deployment extends to 2032–2035 instead of 2028–2030.

### ⚠️ Per-MW Capex Remains High

At $40–60M/unit, Kaleidos's per-MW capital cost is 1.5–2.5× higher than gas turbines or Bloom fuel cells. For small colocation facilities (1–2 MW need), capex-per-MW may be prohibitive unless:
- Radiant achieves <$30M/unit through mass production (uncertain)
- Colocation operators accept premium for 24/7 carbon-free + longevity (25+ year reactor life vs. 10–15 year turbine)
- Regulatory/permitting advantages of microreactor (faster licensing, lower local opposition) justify capex premium

### ⚠️ Colocation Customer Appetite Uncertain

Equinix's 20-unit order is a **preorder**, not yet deployed. Key questions:
- Will Equinix customers (hyperscalers, enterprises) actually commit to multi-year 1.2 MW BTM contracts?
- Will Equinix's colocation customers accept higher power costs if BTM price premium exceeds grid+transmission?
- What happens if hyperscalers (AWS, Azure, GCP) begin building their own colocation-like facilities? Equinix's BTM value proposition erodes.

**Execution risk:** Equinix could reduce or cancel 20-unit order if market fundamentals shift 2026–2028.

---

## 2026–2030 Milestones

| Date | Milestone | Probability | Impact |
|------|-----------|-------------|--------|
| H2 2026 | KDU fuel loading and criticality | Medium–High | Validates design and manufacturing |
| 2026–2027 | KDU ramp to 100% power | Medium | Confirms thermal-hydraulics |
| 2027 | Design Certification Application (DCA) filing | High | Accelerates commercial licensing |
| 2027–2028 | KDU achieves 1,000+ days operation | Medium | Demonstrates reliability |
| 2027–2028 | Equinix site(s) selected and permitting begins | Medium | First commercial deployment path opens |
| 2028 | Manufacturing facility operational (pilot production) | Medium | 10–15 units/year production |
| 2028–2029 | Equinix unit 1 critical and power generation | Low–Medium | First commercial deployment |
| 2029–2030 | Equinix units 2–5 online (various sites) | Low | Parallel deployments at scale |
| 2030+ | Production ramp toward 50/year | Low | Dependent on success of early units |

---

## Outlook: Why Radiant Matters for Colocation

**Kaleidos is the only microreactor with proven customer demand** (Equinix 20-unit preorder). While Westinghouse eVinci and USNC KRONOS are technically sound, they lack market validation.

**For colocation operators:**
- ✅ Modular scaling (1.2 MW units) matches incremental capex cycles
- ✅ Factory-built shortens deployment timeline (12–18 months vs. 3–5 years for grid interconnection)
- ✅ 24/7 carbon-free power enables "green colocation" marketing
- ⚠️ High per-MW capex ($30–60M/MW) requires premium colocation customer willingness-to-pay
- ⚠️ First-of-a-kind regulatory and licensing complexity

**Competitive dynamics:**
- If Kaleidos succeeds at Equinix (2028–2029), other colocation players (Digital Realty, CoreWeave, Zenlayer) will follow
- If Kaleidos experiences delays or capital overruns, colocation market will default to Bloom fuel cells + gas turbines (proven, cheaper per-MW)

**Key watch:** KDU startup (target 2026, likely 2027), Equinix site selection and licensing (2027–2028), and capital cost trajectory for units 2–5 will determine Radiant's viability.

---

## Key People

### Doug Bernauer — CEO & Co-Founder
- [LinkedIn](https://www.linkedin.com/in/doug-bernauer/): TODO: verify slug
- Prior: SpaceX propulsion and systems engineering; co-founded Radiant Nuclear 2020 to apply aerospace manufacturing discipline to microreactors

### Zeke Hausfather — Board / Scientific Advisor
- [LinkedIn](https://www.linkedin.com/in/zekehausfather/): public profile; prominent climate scientist; prior Stripe / Berkeley Earth
- Note: The steering summary listed Hausfather as "CEO, board" but primary CEO is Doug Bernauer; Hausfather's specific role requires verification — TODO: confirm exact title

### Eric Ingersoll — Board Advisor
- Former NRC official; deep nuclear licensing expertise
- No confirmed LinkedIn; see Radiant public press releases for bio

### People — Last Reviewed: 2026-04-25

---

## Related Profiles

- {{< relref "oklo-btm.md" >}} — Oklo Aurora SMR (75 MW, largest order book)
- {{< relref "kairos-power-btm.md" >}} — Kairos Hermes SMR (50 MW, molten-salt cooled, Google partner)
- {{< relref "westinghouse-evinci.md" >}} — Westinghouse eVinci microreactor (5 MW, heat-pipe design)
- {{< relref "usnc-microreactor.md" >}} — USNC KRONOS MMR (15 MW, post-bankruptcy)
- {{< relref "terrapower-btm.md" >}} — TerraPower Natrium (345 MW, thermal storage, Meta partner)
