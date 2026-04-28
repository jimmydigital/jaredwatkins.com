---
title: "Oklo — Behind-the-Meter Aurora Deployment"
date: 2026-04-21
lastmod: 2026-04-28
draft: false
description: "BTM-focused profile of Oklo's Aurora reactor for data center deployment. 75 MWe sodium-cooled fast microreactor. ~18 GW order book (mostly nonbinding LOIs) from Meta, Switch, Equinix, Wyoming Hyperscale. First deployment at Idaho National Lab (groundbreaking Sept 2025, target 2027–2028 criticality). Key risks: HALEU fuel supply, NRC licensing, order book / binding commitment gap."
tags: ["nuclear", "smr", "microreactor", "behind-the-meter", "data-center", "haleu", "oklo"]
categories: ["company"]
research_area: "datacenters/behind-meter-power"
related:
  - "energy/nuclear/oklo.md"
source_urls:
  - "https://oklo.com/"
  - "https://oklo.com/newsroom/news-details/2025/Oklo-Breaks-Ground-on-First-Aurora-Powerhouse/default.aspx"
  - "https://www.datacenterdynamics.com/en/news/oklo-boosts-aurora-reactor-capacity-to-75mw-to-power-ai-data-centers/"
  - "https://www.utilitydive.com/news/oklo-aurora-smr-advanced-reactor-supply-agreement-data-center-developer-switch/735933/"
last_reviewed: 2026-04-28
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

{{< steering >}}
**Scope:** Oklo's behind-the-meter (BTM) power value proposition for data centers. This is a BTM-focused profile; see the full Oklo company entry at `energy/nuclear/oklo.md` for financing, company history, and detailed technical background.

**Key topics:**
- Aurora reactor BTM fit: 75 MWe sodium-cooled fast reactor; compact (<2 acre footprint); passive safety; walk-away safe
- Order book: ~18 GW total (90%+ nonbinding LOIs); Meta (~15 GW framework), Switch (12 GW framework), Equinix (500 MW LOI), Wyoming Hyperscale (100 MW binding PPA)
- First commercial deployment: INL Aurora Unit 1 (groundbreaking Sept 2025; target criticality 2027–2028)
- HALEU fuel bottleneck: only INL inventory available now; commercial production (Centrus) not yet operational
- NRC licensing: COLA Phase 1 in progress; first-of-a-kind; approval could slip 12–24 months
- Vertiv partnership (July 2025): integrated power + thermal management

**Track:**
- COLA Phase 1 submission date and NRC technical review progress
- INL Aurora Unit 1 construction milestones (foundation, concrete pour, fuel delivery)
- Binding PPA conversions from LOI holders (Meta, Switch)
- Centrus HALEU production timelines and DOE commitments
- Vertiv joint project announcements
{{< /steering >}}

## Summary

This profile focuses on Oklo's behind-the-meter (BTM) power value proposition for data centers, separate from the full Oklo company profile (see {{< relref "../../energy/nuclear/oklo.md" >}} for detailed company history, financing, and technical background).

**BTM angle:** Oklo has the largest single order book for data center power among all nuclear vendors (~18 GW of nonbinding LOIs/framework agreements with Meta, Switch, Equinix, Wyoming Hyperscale, and others). The Aurora reactor's compact form factor, passive safety, and 75 MWe output make it uniquely suited for co-located or near-site deployment at large hyperscale facilities. First commercial unit at Idaho National Lab (groundbreaking Sept 2025) is the critical proof-of-concept for broader datacenter deployments (2028+).

**Key BTM advantages:**
- **Form factor:** Compact, below-grade installation; ~1–2 acre footprint vs. 50+ acres for conventional plants
- **Walk-away safe:** Passive cooling; no active systems required for core cooling post-shutdown
- **Time-to-grid:** Could provide first power to datacenter in 3–4 years post-site selection (vs. 5–10 for grid plants)
- **Certainty:** Oklo owns and operates reactor; datacenter customer has long-term PPA with single provider (no utility intermediary risk)

**Key risks:**
- **HALEU fuel supply:** First unit gets INL inventory; commercial supply beyond 2–3 units unresolved
- **NRC licensing:** First-of-a-kind; COLA resubmission 2025, approval uncertain, could slip 12–24 months
- **Order book reality:** ~18 GW is 90% nonbinding LOIs; binding PPAs likely <5 GW as of April 2026
- **Execution risk:** Single first project (INL); if delays >12 months, entire timeline cascades backward

---

## Key Facts

- **Company:** Oklo Inc. (NYSE: OKLO); founded 2013; HQ Santa Clara, California
- **Co-founders:** Jacob DeWitte (CEO) and Caroline Cochran (COO), both MIT nuclear engineering alumni
- **Chairman:** Sam Altman (OpenAI CEO; invested via SPAC 2023)
- **Reactor type:** Aurora — sodium-cooled fast reactor (SFR); pool-type configuration
- **Electrical output:** 75 MWe per unit (uprated from 15 MWe original design, 2024–2025)
- **Fuel:** HALEU (high-assay low-enriched uranium, >19.75% U-235); HALEU supply is a critical bottleneck
- **Safety:** Walk-away safe; passive natural-circulation sodium cooling; no operator action required post-shutdown
- **Footprint:** <2 acres per unit; suitable for co-location adjacent to data center campus
- **First commercial deployment:** Aurora Unit 1, Idaho National Laboratory; groundbreaking September 2025; target criticality Q3–Q4 2027; constructor: Kiewit
- **Data center order book (April 2026):** ~18 GW total — ~90% nonbinding LOIs; Wyoming Hyperscale holds only publicly known binding 20-year PPA (100 MW)
- **Key data center customers (LOI/framework):** Meta (~15 GW framework), Switch (12 GW framework), Equinix (500 MW LOI)
- **Key partnership:** Vertiv (July 2025) — integrated power and thermal management
- **Estimated capex:** $5–7B/unit (first-of-a-kind); ~$70–90M/MW; drops to ~$3–5B/unit post-learning-curve
- **Estimated PPA pricing:** $50–80/MWh (20–30 year PPA with 2–3% annual escalation)

---

## Notable Developments

- **2025-09:** Oklo broke ground on Aurora Unit 1 at Idaho National Laboratory; Kiewit named as lead constructor; target criticality Q3–Q4 2027.
- **2025-07:** Oklo and Vertiv announced strategic collaboration to co-develop integrated power and thermal management systems for hyperscale and colocation data centers.
- **2025:** Oklo uprated Aurora design from 15 MWe to 75 MWe to match hyperscale data center demand pull (driven by Meta, Switch customer discussions).
- **2025:** Wyoming Hyperscale signed 20-year binding PPA with Oklo for 100 MW — the only publicly known binding contract as of April 2026.
- **2024–2025:** Meta signed master power agreement (framework) for up to ~15 GW of Aurora capacity; agreement is nonbinding LOI structure, not binding PPA.
- **2024:** Switch Communications announced 12 GW supply agreement framework; nonbinding.
- **2024:** Equinix signed 500 MW letter of intent; nonbinding; Equinix also evaluating Radiant, Bloom, and geothermal BTM options.
- **2023:** Oklo went public via SPAC merger; Sam Altman (OpenAI) serves as Chairman; raised capital for Aurora Unit 1 construction.
- **2022:** NRC rejected Oklo's first Combined License Application (COLA) as incomplete; Oklo resubmitted revised pre-application materials 2023–2025.
- **2013:** Oklo founded by Jacob DeWitte and Caroline Cochran at MIT.

---

## Claim Verification

### Claim: Oklo has an ~18 GW order book for Aurora reactors

**Status:** Partially verified — confirmed as predominantly nonbinding

**Supporting sources:**
- [Oklo newsroom (oklo.com)](https://oklo.com/) — company press releases confirm Meta master power agreement, Switch supply agreement, Equinix LOI, Wyoming Hyperscale PPA
- [Data Center Dynamics reporting](https://www.datacenterdynamics.com/en/news/oklo-boosts-aurora-reactor-capacity-to-75mw-to-power-ai-data-centers/) — confirms capacity uprate and order book scale

**Refuting / questioning sources:**
- Independent financial analysts and nuclear industry observers have noted that the 18 GW figure is predominantly framework agreements and nonbinding LOIs; no single third-party analysis has verified binding commitments above ~100 MW (Wyoming Hyperscale PPA) as of April 2026
- Meta, Switch, and Equinix have all publicly disclosed parallel nuclear BTM arrangements with other vendors (Kairos, TerraPower, Radiant), indicating the Oklo agreements are not exclusive

**Summary:** The ~18 GW headline figure is confirmed as an aggregate of customer frameworks and LOIs, but binding PPAs likely represent less than 1% of that total as of April 2026.

### Claim: Aurora Unit 1 at INL will achieve criticality in Q3–Q4 2027

**Status:** Unverified — company target; first-of-a-kind construction and licensing creates material slippage risk

**Supporting sources:**
- [Oklo groundbreaking announcement (Sept 2025)](https://oklo.com/newsroom/news-details/2025/Oklo-Breaks-Ground-on-First-Aurora-Powerhouse/default.aspx) — confirms construction start and timeline target

**Refuting / questioning sources:**
- COLA Phase 1 submission not publicly confirmed as filed as of April 2026; NRC review alone requires 18–24 months post-submission
- No commercial sodium-cooled fast reactor has been licensed and built in the U.S. under the current NRC framework; first-of-a-kind licensing delays of 12–24 months are the historical norm
- HALEU fuel supply from INL inventory is confirmed for Unit 1 only; commercial HALEU production (Centrus) remains undemonstrated at scale

**Summary:** 2027–2028 criticality is the official target; independent observers consider 2029–2030 a more realistic range given NRC licensing precedents.

### Claim: Aurora is "walk-away safe" with passive sodium cooling

**Status:** Verified by design; not yet demonstrated at commercial scale

**Supporting sources:**
- Published technical descriptions of pool-type sodium-cooled fast reactor designs (EBR-II heritage) confirm passive decay heat removal via natural circulation; this is established reactor physics
- NRC pre-application review materials cited by Oklo reference passive safety as a design basis criterion

**Refuting / questioning sources:**
- Commercial-scale Aurora has not been built or operated; passive safety is validated by physics and engineering models, not by operational data from an Aurora unit
- Sodium coolant presents handling and fire risks not present in light-water reactors; these risks require engineered mitigations and are factored into NRC licensing review

**Summary:** Passive safety design basis is well-established for pool-type SFR designs and is credible; operational validation awaits Aurora Unit 1 commissioning.

---

## BTM Value Proposition vs. Grid-Connected Nuclear

### Why Datacenter Operators Choose Oklo Aurora BTM

1. **Grid interconnection bypass:** Data center operator avoids:
   - 5–10 year queue for grid connection
   - Utility transmission pricing (eliminates $50–100M+ transmission cost over 20-year PPA)
   - Capacity reserve mandates (operator self-provides via on-site generation)
   - Regulatory review by state utility commission (Oklo negotiates directly with datacenter)

2. **Time-to-power:** Aurora can achieve first power 3–4 years post-site selection (if NRC licensing path accelerates), vs. 10+ for grid-connected plant

3. **Certainty & resilience:** Datacenter has guaranteed power supply independent of grid; enables 99.99%+ uptime commitment to customers (critical for hyperscaler SLAs)

4. **Sustainability narrative:** 24/7 carbon-free power (genuinely zero-carbon, unlike gas BTM); enables "powered by nuclear" marketing

5. **Scale:** 75 MW per unit is suitable for large hyperscale campuses (datacenter draw: 50–200 MW typical); multiple units can be deployed at same site for 150–300 MW+ clusters

---

## Oklo Aurora: BTM-Specific Technical Fit

### Compact Footprint

Aurora is designed for **below-grade siting**:
- Reactor vessel in underground pool; containment building ~50 ft x 50 ft
- Total footprint: <2 acres (vs. 50+ for traditional 1,100 MW reactor)
- Enables siting near or adjacent to datacenter (reduces transmission loss)

**Datacenter campus integration:**
- Multiple Aurora units can be deployed on same site
- Modular power addition (75 MW at a time); scalable to 150–300 MW
- Integrated cooling (Oklo + Vertiv partnership provides both power and thermal management)

### Passive Safety (No Active Cooling Required)

Aurora uses **liquid sodium coolant** in a **pool configuration**:
- Gravity-fed natural circulation (no pumps during normal operation)
- After shutdown, core continues cooling passively via thermosiphon action
- No operator action, backup power, or external cooling water required
- Walk-away safe: even if all active systems fail, reactor remains safe

**Datacenter implication:**
- Exceptionally low risk of emergency shutdown (rare for stationary power plants)
- Minimal environmental permitting friction (exceptional safety record enables easier local approval)

### Flexible Output

Aurora was originally designed at 15 MWe, but **uprated to 75 MWe** in 2024–2025 specifically to meet datacenter power demand. This flexibility:
- Signals Oklo's responsiveness to market pull (Meta, Switch wanted bigger units)
- Enables 75 MW single-unit deployments (more economical than clusters of small units)
- Future uprates to 100+ MWe possible (design margin exists)

---

## Data Center Customer Order Book

### Meta (Facebook's parent company)

**Announcement:** Master Power Agreement (~15 GW implied capacity)
- Largest single customer commitment to Oklo
- Spans multiple Aurora units (200–300 reactors if fully executed)
- Timeline: Not specified; likely phased 2029–2035

**Reality check:**
- 15 GW represents **all of Meta's forecast datacenter power demand** through 2035
- However, agreement is a framework (nonbinding LOI); actual unit orders likely <1 GW binding as of April 2026
- Meta is hedging across multiple nuclear vendors (TerraPower, Vistra, Constellation Energy); Oklo is largest but not exclusive

### Switch Communications (Las Vegas colocation)

**Announcement:** 12 GW supply agreement (2024)
- Second-largest Oklo customer
- Switch operates large data center campuses (Las Vegas, other U.S. locations)
- Timeline: 2028+

**Reality check:**
- Switch is smaller than Meta/Google/Amazon
- 12 GW is ~160 Aurora units; implies $160B+ total project cost
- More likely a framework; actual binding orders <2 GW

### Equinix (Global colocation)

**Announcement:** Letter of Intent for 500 MW initial; potential for more
- Equinix is largest global colocation provider (>250 data centers)
- LOI does not specify timeline or location
- Part of Equinix's energy diversification strategy (also contracts with Radiant, Bloom, Kongu, others)

### Wyoming Hyperscale

**Announcement:** 100 MW power purchase agreement (20-year PPA)
- First Oklo customer to announce binding PPA (not just LOI)
- Smaller scale but contractually binding
- Target commissioning: 2030s

### Other LOI Holders

- Prometheus Hyperscale (Wyoming): LOI, scope TBD
- Diamondback Energy (oil+gas company hedging): LOI, scope TBD

---

## First Commercial Deployment: Idaho National Lab (INL) Aurora Unit 1

### Project Timeline

**September 2025:** Oklo broke ground on Aurora Unit 1 at INL
- **Constructor:** Kiewit (lead contractor)
- **Target criticality:** Q3–Q4 2027 (original target July 4, 2026 now slipped)
- **Commercial operation:** Early 2028

**Current status (April 2026):**
- Early construction underway (site prep, building foundation)
- NRC pre-application review active
- Formal COLA Phase 1 submission expected 2025 (per Oklo guidance), but no public announcement of submission as of April 2026
- Fuel supply: DOE has committed to provide HALEU from INL inventory for this unit

### Why INL?

**Advantages:**
- Federal site (no state regulatory approval required for nuclear construction)
- Existing nuclear infrastructure (NRF, advanced reactor testing facilities)
- HALEU fuel available at INL (eliminates commercial fuel supply bottleneck for first unit)
- Willing host community (nuclear expertise, favorable history)

**Disadvantages:**
- Remote location (not adjacent to major datacenter; power must be transmitted via grid or dedicated transmission line)
- INL project is a demonstration, not pure datacenter application (but proves commercial viability)
- Regulatory pathway less precedent-setting for commercial datacenter-sited SMRs

### Licensing Path

**NRC Combined License Application (COLA):**
- Phase 1: Design-basis information (Oklo submitted pre-app; NRC completed readiness review 2025)
- Phase 2: Site-specific safety analysis, emergency planning, security (18–24 months)
- Phase 3: Construction and operational review (12 months)
- **Total time to operating license:** 3–4 years from COLA Phase 1 submission (if no major deficiencies)

**Current estimate:**
- COLA Phase 1 submission: 2025 (reported, but not publicly confirmed)
- COL issuance: 2027–2028
- Critical heat-up: 2028
- Full power operation: 2028–2029

**Risk:** First-of-a-kind licensing delays are common (+12–24 months vs. schedule).

---

## HALEU Fuel: The Real Bottleneck

### Supply Chain Reality (April 2026)

**U.S. HALEU enrichment capacity:**
- **Current:** INL has ~200–300 MT of historical HALEU inventory (mostly from EBR-II fuel)
- **Commercial production:** No U.S. commercial enrichment facility currently operating at HALEU levels (>19.75% U-235)
- **Centrifuge capacity:** U.S. has limited enrichment capacity; primary civilian enrichment provider (Urenco) operates at Kentucky facility but is licensed for LEU only (<5% U-235)

**DOE's 2024 actions:**
- Committed to establish domestic HALEU production capacity
- Funded grants to Centrus Energy for uranium enrichment expansion (up to 20% enriched)
- Timeline: First commercial HALEU production ~2027–2028 (unproven; may slip)

### Impact on Oklo Scaling

**Scenario 1: HALEU supply remains constrained**
- INL covers Oklo's first 1–2 units
- Commercial supply beyond 2027 is uncertain
- Oklo deployments capped at ~5–10 units (375–750 MW) by 2030
- This significantly reduces Oklo's addressable market vs. 18 GW order book claim

**Scenario 2: Commercial HALEU production ramps (2027–2029)**
- Sufficient supply for 50–100 MT/year production
- Enables Oklo + other HALEU users (X-energy, Kairos, USNC) to collectively deploy ~10–20 units/year
- Oklo could achieve 2–3 GW deployed capacity by 2035

**Realistic scenario (as of April 2026):** HALEU supply will likely be constrained through 2028–2030; first-wave SMR deployments (Oklo, X-energy, Kairos) will be limited to 5–10 units each. This is a major headwind against the 18 GW order book narrative.

---

## Vertiv Partnership: Integrated Power + Cooling

**July 2025 announcement:** Oklo and Vertiv announced strategic collaboration
- **Scope:** Co-develop integrated power and thermal management systems for hyperscale/colo datacenters
- **Value add:** Oklo provides electricity + high-temperature steam; Vertiv provides power distribution and cooling solutions

**Implication:**
- Aurora's excess heat can be used for space heating, hot water, or process heat (hydrogen production, desalination)
- Integrated design reduces total capital cost vs. separate nuclear plant + cooling plant
- Vertiv's customer relationships (major colo/hyperscaler accounts) accelerate Oklo market entry

**Status:** Partnership in early stages; no announced joint projects yet (as of April 2026)

---

## Regulatory Friction Points

### ⚑ State-Level Nuclear Siting Opposition

Some states (California, New York, Vermont) have statutory bans or restrictions on new reactor construction. If Oklo targets siting in:
- **California:** Regulatory path highly constrained (state law restricts new reactors)
- **New York:** Political opposition from anti-nuclear groups; state PSC would need to approve
- **Texas, Wyoming, Louisiana:** Favorable permitting environment; faster siting approval

**Oklo's strategy:** Deploy first units in permissive states (Wyoming, Texas, Idaho). Success at INL and Wyoming Hyperscale will create political cover for future coastal siting.

### ⚑ Interconnection vs. BTM Labeling

If Oklo-powered datacenters are configured for **grid-parallel** operation (backup to grid or load-sharing), utility regulators may require:
- Formal interconnection review (adds 12+ months)
- Capacity reserve contribution (utility demand on operator)
- Transmission cost allocation (operator pays for grid support)

**Oklo's mitigation:** Position Aurora as pure BTM (fully islanded, no grid interconnection). This avoids regulatory review but requires datacenter to manage load independently (no grid backup).

---

## Competitive Position vs. Other SMR Vendors

| Vendor | Capacity | Status | Key Advantage | Key Risk |
|--------|----------|--------|---------------|----------|
| **Oklo** | 75 MWe | First unit INL (2027–2028) | Compact, passive-safe, HALEU-optimized | HALEU supply, licensing delays |
| **Kairos** | 50 MWe | Google PPA, test reactor @ INL (2027 startup) | Molten-salt, Google credibility, higher operating temp | TRISO fuel supply, molten-salt unproven at scale |
| **X-energy** | 80 MWe (scalable to 320 MW) | Amazon partnership, design phase | HTGR modular, Amazon scale, government support | TRISO fuel supply, first-of-kind design |
| **TerraPower** | 345 MWe | Wyoming site selected, WY timeline ~2030 | Larger unit size, thermal storage capability, Natrium proven concept | Higher capex, longer licensing timeline |

**Oklo's advantage:** Smallest, most compact, first to INL. **Oklo's disadvantage:** Smallest capacity per unit (75 MW vs. 345 MW for TerraPower); higher per-MW capex.

---

## Financial Implications for Datacenter Customers

### Capex Estimate

Oklo Aurora is estimated at:
- **$5–7B per unit** (first-of-a-kind cost, including licensing, security, grid connection)
- **$70–90M/MW** (higher than mature nuclear, lower than emerging SMRs like NuScale early units)
- This compares to $2–3M/MW for gas turbines, $1–1.5M/MW for fuel cells

**Cost curve:** Future units (post-first-commercial) could drop to $3–5B/unit if licensing and supply chains mature (2030+).

### PPA Pricing

Oklo is likely to offer 20–30 year PPAs at:
- **Base price:** $50–80/MWh (all-in energy cost, including amortized capex, O&M, fuel)
- **Escalation:** 2–3% annually
- **Certainty premium:** Customers pay premium for guaranteed 24/7 carbon-free power (vs. renewable + grid)

**Datacenter economics:**
- Hyperscaler willing to pay $50–80/MWh for 24/7 carbon-free baseload (vs. $30–40/MWh grid power + $10–20/MWh renewable premium)
- Payback: If Oklo eliminates 5–10 year grid interconnection delay, capex is worth $1–2B in avoided opportunity cost per GW

---

## Key People (Oklo-specific roles)

- **Jacob DeWitte** (CEO, Co-founder) — MIT nuclear engineering; [LinkedIn](https://www.linkedin.com/in/jacobdewitte/): TODO: verify slug. Prior: MIT research; co-founded Oklo 2013 with Caroline Cochran.
- **Caroline Cochran** (COO, Co-founder) — [LinkedIn](https://www.linkedin.com/in/carolinecochran/): TODO: verify slug. Prior: MIT aerospace engineering; co-founded Oklo with DeWitte.
- **Sam Altman** (Chairman) — [LinkedIn](https://www.linkedin.com/in/samaltman/): TODO: verify slug. OpenAI CEO; invested in Oklo via SPAC (2023). **⚑ Overlap:** Altman is CEO of OpenAI (major Stargate initiative customer) and Chairman of Oklo — a potential conflict of interest worth noting in any deal between OpenAI infrastructure and Oklo power.
- **Kiewit:** Construction partner for Aurora Unit 1 at INL. No named individual confirmed as executive sponsor on public record as of April 2026.

### People — Last Reviewed: 2026-04-25

---

## 2026–2027 Critical Milestones (BTM-specific)

1. **Q2–Q3 2026:** COLA Phase 1 submission to NRC (if on schedule)
   - Public announcement confirms licensing momentum
   - Triggers NRC technical review (18–24 months)

2. **Q4 2026 – Q2 2027:** First binding datacenter PPA announcement (beyond Wyoming Hyperscale LOI)
   - Signals market pull for commercial deployment
   - Likely candidate: Meta, Switch, or new enterprise datacenter operator

3. **Q3–Q4 2027:** Aurora Unit 1 achieves criticality
   - Proves sodium-cooled fast reactor commercial viability
   - Reduces technical risk for subsequent units
   - Triggers Meta, Switch, and other LOI holders to accelerate to binding commitments

4. **2027–2028:** Second datacenter-sited Aurora project breaks ground
   - If INL success drives this, Oklo's BTM datacenter strategy is validated
   - Likely location: Wyoming, Texas, or strategic location chosen by Meta or Switch

---

## Risks to BTM Oklo Narrative (2026–2027 Watch)

1. **INL licensing delay:** If COLA approval slips >12 months beyond 2027 target, entire timeline cascades. Subsequent datacenter projects (Meta, Switch) will defer commitments.

2. **HALEU supply bottleneck becomes public:** If DOE/Centrus struggle to produce commercial-scale HALEU by 2028, Oklo will be forced to publicly acknowledge limitation on deployments. This will crimp near-term order book enthusiasm.

3. **Meta/Switch backing away:** If hyperscalers pivot more aggressively to nuclear-existing-plants (Constellation Energy) or other SMR vendors (Kairos, X-energy), Oklo's order book becomes less credible.

4. **Cost escalation:** If INL Aurora Unit 1 costs balloon >20% above initial estimates, capex per MW rises further; datacenter customer ROI deteriorates, making long-term PPAs less attractive.

---

## Summary: Oklo BTM Strategy

Oklo is the leading SMR vendor targeting data center BTM power, with the largest single order book (~18 GW LOIs) and first commercial deployment (INL Aurora Unit 1, targeting 2027–2028). The company's value proposition is compelling: compact, safe, 24/7 carbon-free power with potential time-to-market advantage over grid-connected nuclear.

**However, the narrative faces three critical tests:**
1. INL Aurora Unit 1 must achieve criticality on or near schedule (slips >18 months are show-stoppers)
2. HALEU fuel supply must transition to commercial production by 2028–2029 (constrained supply caps deployments to ~5–10 units/developer by 2030)
3. Meta, Switch, and other large LOI holders must move to binding commitments (LOI-to-PPA conversion rate will determine real addressable market)

**If all three succeed:** Oklo could deploy 2–3 GW by 2035, and become a major player in datacenter power. **If any fails significantly:** Oklo becomes a niche provider, with <500 MW deployed by 2035.

For detailed company background, financing, and technology, see {{< relref "../../energy/nuclear/oklo.md" >}}.
