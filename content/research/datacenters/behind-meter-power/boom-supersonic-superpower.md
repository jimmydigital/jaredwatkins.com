---
title: "Boom Supersonic (Superpower)"
date: 2026-04-21
lastmod: 2026-10-21
draft: false
description: "Boom Supersonic's Superpower: 42 MW aeroderivative natural gas turbine derived from the Overture airliner engine core, marketed for behind-the-meter data center power. Crusoe's 29-unit (1.21 GW) order from December 2025 was ended on 2026-09-25; Boom projects about 250 MW of 2027 deliveries to other sites (company projection)."
research_area: "datacenters/behind-meter-power"
source_urls:
  - "https://www.techrepublic.com/article/news-crusoe-boom-turbine-deal/"
  - "https://theaiinsider.tech/2026/09/29/crusoe-ends-1-25b-turbine-deal-with-boom-supersonic-for-ai-data-centers/"
  - "https://boomsupersonic.com/superpower"
  - "https://boomsupersonic.com/press-release/boom-supersonic-to-power-ai-data-centers-with-superpower-natural-gas-turbines-adds-300-million-in-new-funding"
  - "https://techcrunch.com/2025/12/09/boom-supersonic-raises-300m-to-build-natural-gas-turbines-for-crusoe-data-centers/"
  - "https://www.datacenterfrontier.com/energy/article/55358731/aeroderivative-turbines-move-to-the-center-of-ai-data-center-power-strategy"
last_reviewed: 2026-10-21
stale_after_days: 60
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Boom Supersonic, a Denver, Colorado aerospace company best known for developing the Overture supersonic airliner, has pivoted into data center power generation with Superpower — a 42 MW aeroderivative natural gas turbine designed for behind-the-meter (BTM) deployment. The company leverages the high-temperature, high-efficiency engine core developed for Overture to create a fast-start, compact power generation solution packaged in an ISO shipping container footprint. In December 2025, Crusoe Energy announced an order for 29 Superpower units (1.21 GW total) and Boom raised $300 million to ramp manufacturing; on 2026-09-25 Crusoe ended the agreement (see October 2026 Update below).

**Key appeal:** Waterless operation (critical for water-scarce data center regions), 42 MW per unit (larger than most aeroderivatives, smaller than heavy-frame turbines), five-minute fast-start capability, and a proven aerospace engine heritage in an untested turbine market for data centers.

**Risks:** First turbine deployment for Boom; engine core is heritage aerospace design (not originally designed for continuous baseload); supply chain ramp-up unproven; natural gas feedstock (not carbon-free).

---

## October 2026 Update: Crusoe Ends the Superpower Order

- **2026-09-25:** Crusoe announced it was ending its agreement with Boom for 29 Superpower turbines. The deal was reported at $1.25 billion; Boom's December 2025 launch described 29 units of 42 MW (1.21 GW) with deliveries expected from 2027. The reporting reviewed gives no detailed reason; Crusoe says it "remains flexible about power sourcing" across turbines, wind, solar, batteries and grid power. No replacement supplier for this order was named. ([TechRepublic](https://www.techrepublic.com/article/news-crusoe-boom-turbine-deal/))
- **Boom's stated outlook (company projections, via the same report):** about 250 MW of Superpower deliveries to other sites in 2027 and 1 GW in 2028. Boom has lost its launch customer; no other named customer was found in this review.
- **Crusoe's other power commitments:** 29 GE Vernova LM2500XPRESS aeroderivatives (nearly 1 GW combined) and a June 2026 agreement with Bergen Engines covering about 750 MW (a 438 MW contract plus a 310 MW letter of intent).
- **Order-book consequence:** Any section below describing the Crusoe order as contracted reflects the December 2025 announcement and is superseded by the cancellation.

---

## Key Facts

- **Founded:** 2014 (as Boom Supersonic for aircraft)
- **HQ:** Denver, Colorado
- **Type:** Private (Series B/C equivalent funding round; Dec 2025 $300M raise)
- **CEO/Founder:** Blake Scholl — aerospace engineer; prior startup experience (Spike Aerospace)
- **Core business pivot:** Primarily known for Overture supersonic aircraft development; launched Superpower turbine division ~2024–2025 to capitalize on data center power demand
- **Superpower turbine specs:**
  - **Power output:** 42 MW electrical per unit
  - **Form factor:** ISO shipping container (standard 20/40 ft equivalent)
  - **Fuel:** Natural gas (dual-fuel capability with diesel/other hydrocarbons)
  - **Start time:** Five-minute cold start (no grid power required)
  - **Cooling:** Waterless operation — air-cooled generator; no cooling water intake or discharge required
  - **Heat rate:** Estimated ~6,500–7,000 BTU/kWh (efficient for aeroderivative class)
  - **Emissions:** Not explicitly stated; assumed to have standard gas turbine NOx/particulate emissions (mitigation via SCR or similar likely required)
  - **Maintenance interval:** 20,000–25,000 operating hours typical for jet-derivative turbines

- **Manufacturing location:** TBD (as of April 2026); $300M funding likely supports new manufacturing facility or partnership with existing OEM
- **Supply chain:** Engine core is Boom's proprietary design (derived from Overture); balance-of-plant components sourced from suppliers (generator, controls, packaging)

---

## Superpower for Data Centers: The Pitch

### Why Aerospace-Derived?

The Symphony engine core, originally developed for Overture's sustained supersonic flight (Mach 1.7 cruise at 41,000 feet), operates at high combustor temperatures and pressures. These characteristics translate to:
- **Efficiency:** Higher thermal efficiency than conventional industrial turbines at equivalent MW size
- **Compact size:** Smaller core diameter enables higher power density (MW per unit volume)
- **Fast response:** Jet engines are designed for transient start/acceleration; this translates to rapid power ramp capability
- **High reliability:** Aerospace qualification standards (pressure cycling, temperature extremes, vibration) exceed industrial stationary turbine standards

### Waterless Operation: Key Differentiator

Most large gas turbines require evaporative cooling (cooling towers) or closed-loop cooling (heat exchangers + circulating water). Superpower uses direct air cooling of the generator, eliminating water intake and discharge:
- **Critical for water-scarce regions:** Texas, Arizona, California data centers face water scarcity and environmental restrictions on thermal discharge
- **Permitting advantage:** Air cooling avoids water discharge permits, which can delay projects 6–12 months in some jurisdictions
- **Operating cost:** Eliminates cooling water expense (significant for large plants in arid regions)

### Crusoe Energy Partnership & Order

In December 2025, Crusoe Energy announced an order for **29 Superpower units**, totaling **1.21 GW** of capacity. Crusoe is deploying these at its data center campuses in Texas (Abilene, and other sites planned).

**Crusoe's deployment model:**
- Crusoe develops and operates AI-focused data centers (not leasing colos, but owning infrastructure)
- Multi-unit Superpower deployments enable rapid power scaling: each unit can be installed in weeks; 29 units provide modular 1.21 GW backbone
- Integration with solar + battery storage at Crusoe Abilene facility (Lancium Clean Campus) enables hybrid BTM power model
- Fast time-to-power: 42 MW units online <6 months from order (vs. 2+ years for grid interconnection or large unified plants)

---

## Competition & Market Position

### Direct Competitors in Aeroderivative Turbine Space

**GE Vernova LM2500XPRESS** (35 MW, publicly available):
- Mature design (LM2500 is 30+ year lineage)
- Faster availability (shorter lead time, established supply chain)
- Proven in data center deployments (Crusoe also using 29 units; Project Stargate)
- Larger MW per unit (35 MW vs. Boom's 42 MW) allows wider range of site capacities

**Siemens Energy SGT-700/800** (40–62 MW, depending on configuration):
- Heavy-frame alternative; slower start but higher power output
- More established supply chain
- Higher per-unit capital cost due to larger footprint

**Boom's advantage:**
- **Waterless operation** — unique in large aeroderivative class (GE Vernova and Siemens still use water cooling on some configurations)
- **Fast start** — five minutes is industry-leading for 40+ MW class
- **Compact containerized design** — easier logistics to remote or existing datacenter sites

### Boom's Challenge

- **First turbine deployment:** Unlike GE Vernova or Siemens (both with 20+ year industrial turbine history), Boom's Superpower has zero operational hours as a stationary power plant. Crusoe is taking on first-customer technical risk.
- **Supply chain unproven:** Boom is establishing turbine manufacturing from scratch (aerospace production is different from industrial power). Scaling to deliver 29 units on schedule will test execution.
- **Capital intensity:** Manufacturing ramp requires significant capex; $300M funding may be tight if supply chain delays occur.

---

## Technology Details: Engine Core & Configuration

### Symphony Engine → Superpower Turbine

The Symphony engine is a high-bypass, geared turbofan developed for Overture:
- **Pressure ratio:** Estimated 50:1 (very high; typical industrial turbines are 15–30:1)
- **Combustor temperature:** Estimated 1,700+ K (optimized for supersonic cruise efficiency)
- **Compressor:** Multi-stage axial compressor; high-pressure stages similar to large commercial jet engines (CF6, GE90 lineage)

**Turbine adaptation:**
- Boom retrofits Symphony core into a stationary generator package (no gearbox or high-bypass fan of jet engine)
- Exhaust heat is recovered via heat recovery steam generator (HRSG) or rejected directly to atmosphere
- Fuel system adapted from jet fuel (kerosene, Jet A) to natural gas (requires fuel vaporization and control system redesign)

### Waterless Cooling

Direct air-cooled generator (permanent magnet or conventional):
- No cooling water loop; condenser-type radiator for generator jacket cooling
- Allows operation in dry climates without environmental discharge permits
- Trade-off: Air cooling is noisier and less efficient than water cooling (minor impact on overall plant efficiency)

---

## Crusoe Energy Deployment: Abilene & Beyond

### Lancium Clean Campus (Abilene, Texas)

**Site overview:**
- 4 million square feet; 1.2 GW total capacity (phases 1 & 2)
- Phase 1: 200 MW energized Q1 2025; two buildings
- Phase 2: 900 MW additional; six buildings; expected mid-2026

**Power mix:**
- **Gas generation:** Superpower turbines (Crusoe allocation, some capacity) + GE Vernova LM2500XPRESS (29 units, ~1 GW total)
- **Solar+storage:** Behind-the-meter solar arrays + battery storage (BESS)
- **Hybrid operation:** Gas turbines provide baseload/peaking; solar + BESS buffers midday renewable generation; grid backup if needed (though Crusoe targeting islanded operation)

**Timeline:**
- First Superpower unit expected operational by mid-2026
- Full 29-unit deployment stretched across 2026–2027

---

## Regulatory & Permitting Considerations

### Air Quality Permitting

Natural gas turbines emit NOx, particulate, and CO2. Texas (Abilene site) falls under TCEQ (Texas Commission on Environmental Quality) jurisdiction:
- **Texas advantage:** Deregulated market (ERCOT) has historically fast-tracked permitting for on-site power
- **SCR or LNB requirements:** Boom's turbines will likely require Selective Catalytic Reduction (SCR) or Lean-Burn controls to meet NOx limits
- **Permit timeline:** 6–12 months for typical Texas site

### Grid Interconnection (If Parallel with Grid)

If Superpower units are configured for "grid-parallel" backup (not pure BTM islanded):
- ERCOT interconnection review applies
- Boom/Crusoe must provide fault-current contribution studies, anti-islanding controls, etc.
- Timeline: 3–6 months typical for straightforward cases

---

## Financial & Investment Details

### $300 Million Funding Round (December 2025)

**Purpose:**
- Scaling manufacturing of Superpower turbines
- Establishing supply chain relationships
- Building manufacturing facility or contracting with Tier-1 OEM partner
- Working capital for delivering Crusoe's 29-unit order

**Valuation implication:**
- $300M funding suggests Boom's energy division is now valued at $1B+ (Series B/C equivalent)
- Separate valuation from Overture aircraft program (which has distinct investor base and timeline)

**Capital efficiency:**
- At $300M for 1.21 GW (Crusoe order), implied capital cost is ~$250M/GW for turbine supply (not including site work, integration, controls)
- This is competitive with GE Vernova, Siemens for aeroderivative turbines

---

## Key Risks & Uncertainties

1. **First commercial deployment:** No operational track record for Superpower turbines. Crusoe is taking technical risk; any early failures could delay entire order book.

2. **Supply chain execution:** Manufacturing scale-up from aerospace (low-volume, high-precision) to industrial power (higher-volume, tighter cost control) is a different skillset. Boom has aerospace expertise, not industrial OEM experience.

3. **Aerospace engine reliability ≠ industrial turbine reliability:** Jet engines are operated at peak efficiency for a few thousand hours (commercial flight is often 6–8 flight hours per day, then maintenance). Stationary power plants run 6,000–8,000 hours per year continuously. Boom must prove component durability (compressor blade erosion, combustor coking, etc.) under continuous operation.

4. **Natural gas feedstock:** 42 MW turbines burn 50–60 MMBTU/hr of natural gas (rough estimate). Crusoe's sites in Texas benefit from natural gas infrastructure, but future deployments may face fuel supply constraints or pricing exposure.

5. **Waterless cooling trade-off:** Air cooling is effective, but ambient temperature directly impacts generator efficiency and power output. High ambient (110°F+) can reduce output 5–10%. Boom claims "full output above 110°F," but independent verification is limited.

6. **Hydrogen-readiness:** Boom has not announced hydrogen fuel capability. Future 2030+ requirements for hydrogen-capable turbines may disadvantage Superpower in carbon-conscious markets.

---

## Competitive Outlook: 2026–2027

**Boom's window of opportunity:** 2026–2027, before established competitors (GE Vernova, Siemens, Wärtsilä) scale their data center turbine offerings. If Superpower executes flawlessly on Crusoe order, Boom could capture 10–20% of new aeroderivative data center turbine market through 2029.

**Risk scenario:** If Boom faces manufacturing delays or reliability issues on Crusoe units, the company could lose momentum to more established OEMs. Aerospace-to-industrial transition failures are common in energy equipment.

---

## Key People

- **Blake Scholl** (CEO, Founder) — Aerospace engineer; [LinkedIn](https://www.linkedin.com/in/blakescholl/): TODO: verify slug. Prior: product management at Amazon (pre-Boom); founded Boom Supersonic 2014; pivoted Superpower turbine division 2024–2025.
- **Manufacturing/turbine leadership** — TBD as of April 2026; Boom is actively hiring industrial OEM veterans to lead Superpower division. TODO: update when announced.

### People — Last Reviewed: 2026-04-25

---

## Summary: Boom Superpower as BTM Solution

Boom Superpower represents a novel entry into data center BTM turbine market, bringing aerospace efficiency and innovation to stationary power. The waterless operation differentiator is genuinely valuable for water-scarce data center regions. However, execution risk is high: Boom is entering industrial power generation with no track record, while facing mature competitors (GE Vernova, Siemens, Wärtsilä) with established supply chains and global service networks.

**Boom lost its launch customer in September 2026.** Whether Superpower reaches deployment now depends on securing other buyers and meeting delivery schedules; no replacement order had been identified in sources reviewed on 2026-10-21.

**Outlook:** Boom must secure replacement customers and demonstrate certification and delivery; its own projections are 250 MW in 2027 and 1 GW in 2028.
