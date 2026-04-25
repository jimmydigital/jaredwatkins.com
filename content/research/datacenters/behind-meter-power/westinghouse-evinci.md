---
title: "Westinghouse eVinci — Heat-Pipe Microreactor for Remote & Data Center BTM"
date: 2026-04-24
lastmod: 2026-04-24
draft: false
description: "Westinghouse Electric Company eVinci microreactor. 5 MWe / 15 MWt heat-pipe reactor; no coolant pumps; walk-away safe. TRISO fuel; 8+ year refueling interval; factory-assembled, rail/truck-transportable. NRC Principal Design Criteria approved March 2025; I&C platform approved Dec 2024. First customer: Saskatchewan Research Council (pilot 2029). Penn State university partnership. No commercial data center deployments announced. Parent: Westinghouse Electric Company (Brookfield Asset Management / Cameco JV)."
tags: ["nuclear", "microreactor", "heat-pipe", "behind-the-meter", "data-center", "westinghouse", "evinci"]
categories: ["company"]
research_area: "datacenters/behind-meter-power"
source_urls:
  - "https://westinghousenuclear.com/innovation/evinci-microreactor/"
  - "https://www.businesswire.com/news/home/20250331678087/en/Westinghouse-eVinci-Design-Reaches-Key-US-Licensing-Milestone"
  - "https://www.powermag.com/westinghouse-secures-first-customer-for-evinci-nuclear-microreactor/"
  - "https://www.ans.org/news/2025-03-05/article-6829/penn-state-and-westinghouse-make-evinci-microreactor-plan-official/"
  - "https://www.nrc.gov/reactors/new-reactors/advanced/who-were-working-with/pre-application-activities/evinci"
last_reviewed: 2026-04-24
stale_after_days: 90
---

## Summary

Westinghouse Electric Company's eVinci is a compact, heat-pipe-cooled microreactor producing up to **5 MWe / 15 MWt** from a single unit, with an 8+ year refueling interval. Unlike conventional reactors (which require coolant pumps, active circulation, and large pressure vessels), the eVinci uses **heat pipes** — passive two-phase devices that transfer heat from the reactor core to the power conversion system without any moving parts. The result is a reactor that is genuinely "walk-away safe" in the strongest sense: no active systems are needed to maintain core cooling, ever.

The eVinci is factory-assembled and designed to fit in a standard shipping container, making it transportable by rail or truck to remote sites. This positions it primarily for remote power applications (military bases, mining sites, Arctic communities) — and secondarily for data center co-located or near-site BTM deployment where grid access is unavailable or prohibitively expensive.

**Key 2025 milestones:** NRC approved the Principal Design Criteria (PDC) topical report (March 31, 2025) and the Instrumentation & Control System platform (December 2024). These are meaningful pre-licensing steps, but a Combined License Application (COLA) has not yet been submitted as of April 2026. Commercial deployment is likely **mid-2030s** for U.S. applications.

**No data center BTM customers with signed agreements have been announced as of April 2026.** The most developed customer relationship is the Saskatchewan Research Council (SRC) pilot (~2029) in Canada.

---

## Key Facts

- **Technology name:** eVinci™ Microreactor
- **Developer:** Westinghouse Electric Company (Nuclear division)
- **Parent company:** Westinghouse Electric Company LLC — owned via JV between:
  - **Brookfield Asset Management** (via Brookfield Renewable Partners subsidiary): majority ownership
  - **Cameco Corporation**: minority stake
  - Acquired from Toshiba in 2018 after Westinghouse Chapter 11 bankruptcy; Cameco/Brookfield partnership formed 2023
- **HQ:** Cranberry Township, Pennsylvania, USA
- **President & CEO (Westinghouse):** Patrick Fragman (since 2019)
- **eVinci Program lead:** Chris Colbert, VP of eVinci Technologies (as of recent organizational structure)

**Reactor specifications:**
- **Reactor type:** Heat-pipe-cooled microreactor
- **Output:** Up to 5 MWe (electric) / 15 MWt (thermal)
- **Fuel:** TRISO fuel pellets in graphite matrix (similar to Kairos, X-energy fuel; BWXT is U.S. supplier)
- **Coolant:** Heat pipes (no circulating fluid; passive two-phase heat transfer via sodium or lithium metal inside heat pipe)
- **Operating temperature:** ~600–700°C (high-temperature output enables cogeneration applications)
- **Refueling interval:** 8+ full-power years before refueling required; swap-and-replace design (new core module swapped in at factory; old core returned for reprocessing)
- **Footprint:** Factory-assembled; transportable in standard shipping containers; ~<2 acres total installation footprint
- **Walk-away safety:** Passive heat removal for indefinite period without operator action or AC power
- **First-of-a-kind differentiator:** No coolant pumps anywhere in the system; heat pipes have no moving parts; only the power conversion system (turbine or thermoelectric) has moving parts

---

## Technology Deep Dive: Heat Pipe Cooling

**How heat pipes work:** A heat pipe is a sealed metal tube partially filled with a working fluid (sodium or lithium at high temperature). One end (the evaporator) is in contact with the reactor core; the fluid vaporizes, absorbs heat, and travels to the other end (the condenser) where it releases heat to the power conversion system and condenses back to liquid. Gravity or capillary wicks return the liquid to the hot end. **No pumps. No valves. No moving parts.**

**Why this matters for safety:** Conventional reactor cooling requires pumps (active systems) that need power to run. If power fails, emergency core cooling systems must activate. Heat-pipe reactors have no such requirement — the heat pipes passively transfer heat as long as there is a temperature gradient. Even if all external power is lost, the reactor core will cool passively and indefinitely.

**Comparison to other microreactors:**
- **Oklo Aurora:** Sodium-cooled fast reactor; requires sodium circulation (passive natural convection, but sodium is active coolant); larger (75 MWe vs. 5 MWe)
- **Radiant Kaleidos:** High-temperature gas-cooled (helium coolant); passive safety but uses gas circulation
- **eVinci:** Purely passive heat pipes; smallest moving-parts count of any advanced reactor design

**Trade-off:** Heat pipes are proven at small scale but have not been demonstrated at reactor scale. The TRISO fuel design is shared with other advanced reactors, reducing fuel supply risk relative to HALEU (used by Oklo).

---

## Licensing Status (April 2026)

Westinghouse has pursued a phased NRC pre-licensing strategy:

**Completed milestones:**
1. **Instrumentation & Control (I&C) Platform approval** (December 2024): NRC issued Final Safety Evaluation Report for the eVinci Advanced Logic System (ALS) v2 — the first NRC-approved I&C system for any microreactor. This is a significant milestone because I&C licensing is often the longest-lead-time element.
2. **Principal Design Criteria (PDC) Topical Report approval** (March 31, 2025): NRC approved the foundational design safety criteria for the eVinci. This provides the basis for the eventual Combined License Application (COLA) and simplifies future site-specific license applications.
3. **Pre-application readiness activities:** Westinghouse has engaged the NRC in multiple pre-application meetings under 10 CFR 50 (or potentially 10 CFR 53, the new advanced reactor framework).

**Next steps for commercialization:**
- Submit Combined License Application (COLA) to NRC — not yet submitted as of April 2026; estimated 2027 at earliest
- COLA review timeline: Typically 3–5 years for first-of-a-kind designs, potentially faster for second-mover after Oklo and Kairos blaze the licensing trail
- First commercial deployment (U.S.): Mid-2030s realistic

**⚑ Licensing gap:** The PDC approval is a necessary but not sufficient step. Westinghouse has not yet submitted a COLA, which is the formal licensing action. Without a COLA submission, commercial deployment cannot occur. This puts eVinci behind Oklo (which has a new COLA Phase 1 planned for 2025) and Kairos (which has a test reactor at INL) in the licensing queue.

---

## Known Customers & Partnerships (April 2026)

**Saskatchewan Research Council (SRC) — First eVinci Customer:**
- SRC (Canada's second-largest R&D organization) announced intent to host an eVinci microreactor demonstration
- Target: Pilot deployment by ~2029 in Saskatchewan, Canada
- This is a research/demonstration application, not a commercial data center

**Penn State University — University Pilot:**
- Penn State submitted a Letter of Intent to the NRC (February 2025) to host and operate an eVinci microreactor on campus
- Formal partnership with Westinghouse announced March 2025
- Focus: Rapid prototyping, testing, and educational applications
- This is a research application, not commercial BTM power

**Data center customers:** None announced as of April 2026. Westinghouse markets eVinci to data center operators but no binding agreements have been disclosed.

---

## Data Center BTM Pitch

Westinghouse positions the eVinci for data center BTM based on:

1. **Long refueling intervals (8+ years):** Data center operators do not want to deal with fuel supply chains; eVinci requires no fuel deliveries for 8+ years, then a factory swap-out of the core module
2. **Factory-assembled, plug-and-play:** The eVinci is assembled at a factory, not built on-site — reducing construction labor and schedule risk
3. **Co-located deployment:** Small footprint (<2 acres) enables installation at or near a data center campus, avoiding transmission costs
4. **24/7 carbon-free:** Nuclear power is genuinely carbon-free at point of generation; unlike gas BTM, eVinci supports genuine "24/7 clean energy" claims
5. **Modular scaling:** Multiple eVinci units can be clustered (e.g., 5 units = 25 MW; 20 units = 100 MW); this enables phased capacity growth

**Limitation for hyperscalers:** At 5 MWe per unit, the eVinci serves small data centers or edge deployments. A 100 MW hyperscaler campus would require 20 eVinci units — feasible but a significant capital investment and NRC licensing challenge. For large hyperscale BTM, Oklo (75 MWe) or Kairos (50 MWe) offer more MW per licensing action.

---

## Westinghouse Corporate Context

Westinghouse Electric Company went through Chapter 11 bankruptcy in 2017 (under Toshiba ownership) following massive cost overruns on the Vogtle AP1000 construction projects in the U.S. The company emerged from bankruptcy in 2018, acquired by a consortium led by Brookfield Asset Management and Bechtel. In 2023, Cameco Corporation acquired a ~49% stake from Brookfield, forming the current Brookfield/Cameco JV structure.

The Brookfield/Cameco ownership is strategically important for the eVinci:
- **Cameco** is the world's largest uranium producer; owns uranium mines, conversion, and enrichment assets — reducing fuel supply risk for Westinghouse's reactor programs
- **Brookfield Renewable Partners** has existing relationships with hyperscalers and infrastructure investors — potentially valuable for commercializing eVinci at data center sites
- **Brookfield Asset Management** also invested $5B in Bloom Energy (separate nuclear vs. fuel cell bet), suggesting a portfolio approach to clean data center power

Patrick Fragman (CEO) has signaled that eVinci and advanced reactor development is a strategic priority for Westinghouse post-Vogtle, with the company rebuilding its reputation for nuclear innovation after the AP1000 cost overruns.

---

## Key People

### Patrick Fragman — President & CEO, Westinghouse Electric Company
- Belgian engineer; joined Westinghouse in 2019 after career at Tractebel Engineering (GDF Suez subsidiary), Belgian nuclear operator Engie Electrabel
- Overseeing company's transition from LWR maintenance/engineering to advanced reactor development
- Manages Brookfield Asset Management / Cameco JV ownership relationship

### Chris Colbert — VP, eVinci Technologies
- Internal program lead for eVinci commercialization
- Background in nuclear systems engineering at Westinghouse
- Key contact for regulatory interactions and customer development

### People — Last Reviewed: 2026-04-25

---

## Competitive Comparison: eVinci vs. Other Microreactors

| | Westinghouse eVinci | Radiant Kaleidos | Oklo Aurora (smallest config) |
|---|---|---|---|
| **Output** | 5 MWe / 15 MWt | 1.2 MWe / ~5 MWt | 75 MWe (no smaller commercial option) |
| **Cooling** | Heat pipes (passive, no pumps) | Helium gas (passive, no pumps) | Sodium metal (passive natural convection) |
| **Fuel** | TRISO | TRISO + HALEU | Metallic HALEU |
| **Refueling** | 8+ years | 3–5 years | Unknown commercial interval |
| **NRC status** | PDC approved; no COLA | Demo unit in construction at INL | Phase 1 COLA resubmission (2025) |
| **First customer** | Saskatchewan Research Council (2029) | Equinix (20-unit preorder) | Meta, Switch, Equinix (LOIs) |
| **Data center BTM** | No signed agreements | Active Equinix deployment pathway | Largest order book (~18 GW LOIs) |

---

## Watch List

- **COLA submission:** Expected 2026–2027; will trigger formal NRC review clock
- **SRC pilot deployment (2029):** First operational eVinci; critical proof point for commercialization
- **Penn State deployment:** University campus provides visibility and operational data
- **Data center customer announcement:** If Westinghouse secures a hyperscaler LOI or PPA for eVinci, it would signal move from R&D to commercial competition with Radiant and Oklo
- **TRISO fuel supply:** Shared BWXT dependency with Kairos, X-energy, USNC/NANO — monitor supply chain capacity

---

## Cross-Links

- BTM overview: {{< relref "_index.md" >}}
- Other microreactor BTM profiles: {{< relref "usnc-microreactor.md" >}}
- Oklo BTM profile: {{< relref "oklo-btm.md" >}}
- Energy section — nuclear overview: {{< relref "../../energy/nuclear/_index.md" >}}
