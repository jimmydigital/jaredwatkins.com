---
title: "Blue Energy"
date: 2026-03-25
lastmod: 2026-03-25
draft: false
description: "Edinburgh-based SMR developer; MIT NSE spinout; co-founded 2023 by Jake Jurewicz and Matt Slotkin; $45M Series A (Oct 2024, Engine Ventures / At One Ventures); shipyard-constructed modular LWR; NRC topical report approved for construction resequencing; 1.5 GW plant at Port of Victoria TX announced for Crusoe AI datacenter campus; gas bridge 2028 → nuclear 2031."
tags: ["nuclear", "smr", "energy", "us", "behind-the-meter", "shipyard-construction", "startup"]
categories: ["company"]
research_area: "energy/nuclear"
source_urls:
  - "https://blueenergy.co/"
  - "https://blueenergy.co/blue-energy-and-crusoe-partner-to-develop-advanced-nuclear-powered-ai-data-center-project-in-port-of-victoria-texas/"
  - "https://blueenergy.co/blue-energy-achieves-key-u-s-nrc-licensing-milestone-paving-the-way-for-power-in-48-months-or-less-with-natural-gas-bridge/"
  - "https://www.datacenterdynamics.com/en/news/crusoe-taps-blue-energy-to-supply-nuclear-power-for-up-to-15gw-data-center-in-port-of-victoria-texas/"
last_reviewed: 2026-03-25
stale_after_days: 90
related:
  - "energy/nuclear/_index.md"
  - "datacenters/design-construction/crusoe.md"
  - "datacenters/power-infrastructure/_index.md"
---

## Summary

Blue Energy is an Edinburgh, Scotland-based small modular reactor (SMR) developer founded in 2023 by Jake Jurewicz (CEO) and Matt Slotkin, emerging from MIT's Nuclear Science & Engineering Department. The company designs modular light water reactor (LWR) plants built in existing shipyards and fab yards — applying the manufacturing logic of offshore oil & gas platform construction to nuclear power. Blue Energy claims this approach cuts construction time by ~80% (3 years vs. 10+ traditionally) and cost to ~$5,000/kW (vs. $13,000+/kW for recent stick-built nuclear). The company raised $45M in Series A funding in October 2024 from Engine Ventures and At One Ventures. Its most significant milestone is a partnership with Crusoe announced in late 2024 to develop a 1.5 GW nuclear-powered AI datacenter campus at the Port of Victoria, Texas — with a gas-to-nuclear conversion model: natural gas supplies power from 2028 while nuclear licensing completes, transitioning to nuclear generation by 2031. The U.S. NRC has approved Blue Energy's licensing topical report for its construction resequencing approach, enabling non-nuclear infrastructure to be built before nuclear construction permits are granted. Construction begins Q2 2026; NRC construction permit application filed 2027.

**⚑ Direct datacenter overlap:** Blue Energy is the power supplier for Crusoe's Port of Victoria AI datacenter campus. See [Crusoe]({{< relref "../../datacenters/design-construction/crusoe.md" >}}) and [Datacenter Power Infrastructure]({{< relref "../../datacenters/power-infrastructure/_index.md" >}}).

## Key Facts

- **Founded:** 2023
- **HQ:** Edinburgh, Scotland (US operations: San Antonio, TX)
- **Type:** Private
- **Co-Founders:** Jake Jurewicz (CEO), Matt Slotkin
- **Origins:** MIT Nuclear Science & Engineering Department
- **Total raised:** $45M (Series A, October 2024)
- **Series A investors:** Engine Ventures (lead), At One Ventures (co-lead); Angular Ventures, Tamarack Global, Propeller Ventures, Starlight Ventures, Nucleation Capital
- **Reactor type:** Light Water Reactor (LWR) — mature, proven technology; not a novel Gen IV design
- **Construction method:** Shipyard / fab yard modular prefabrication; transported to operating site
- **Cost target:** ~$5,000/kW (vs. ~$13,000/kW for recent stick-built US nuclear)
- **Build time claim:** 48 months or less (with gas bridge); nuclear power online ~36 months after gas bridge
- **NRC milestone:** Topical report BE-BOPTR-02-NP approved — authorizes construction resequencing approach (non-nuclear non-safety infrastructure can be built before nuclear construction permit)
- **Key project:** Port of Victoria, TX — 1.5 GW for Crusoe AI datacenter campus
  - Gas bridge: power delivery targeting 2028
  - Nuclear generation: targeting 2031
  - Construction start: Q2 2026
  - NRC construction permit application: 2027
- **Business model:** Finance, build, own, and operate; customers purchase power via long-term PPAs (no upfront capital for the customer)

## What It Is / How It Works

Blue Energy's core insight is that nuclear plant cost and schedule overruns are predominantly a construction problem, not a reactor design problem. The company estimates that 93% of nuclear plant costs are in the balance-of-plant (civil works, cooling systems, turbine halls, electrical infrastructure, security systems) — not the reactor itself. Traditional nuclear builds all of this on-site with craft labor over many years. Blue Energy's approach:

**Shipyard construction:** Fab yards and shipyards are purpose-built for large, complex modular assembly under controlled conditions. Offshore oil platforms, LNG vessels, and naval ships are built this way — Blue Energy applies the same manufacturing logic to nuclear plant modules. The key advantages are: parallel manufacturing of multiple modules simultaneously, factory quality control vs. field construction variability, and reuse of the same tooling and workforce across multiple units.

**Mature LWR technology:** Unlike Kairos (fluoride salt), X-energy (pebble-bed HTGR), or TerraPower (sodium fast), Blue Energy's reactor is a light water reactor — the same fundamental design as the 440+ LWRs currently operating globally. This is a deliberate choice: LWR technology has the longest NRC licensing precedent, the deepest supply chain, the most experienced construction and operating workforce, and the broadest international deployment base. The novelty is in the construction method, not the physics.

**"Passive safety advancements" and walk-away safe design:** The reactor building is submerged in a pool, providing defense-in-depth cooling without active pumping — the pool acts as a passive heat sink. "Walk-away safe" means that in a loss-of-coolant accident, the design can maintain core cooling for 72+ hours without operator action or external power. This is an evolutionary improvement on existing LWR passive safety designs (similar to Westinghouse AP1000 principles).

**Gas-to-nuclear conversion model:** Blue Energy's NRC topical report approval specifically authorizes a construction resequencing approach. Non-nuclear, non-safety-significant infrastructure (civil works, turbine halls, power electronics, cooling towers, switchgear) can be built, financed, and put into service with natural gas generation while the nuclear components proceed through the NRC licensing and fabrication process. This is strategically important for two reasons:
1. **Time to revenue:** Gas generation in 2028 generates cash flow and proves the facility before nuclear commissioning in 2031
2. **Project financing:** The non-nuclear portion of the plant (which Blue Energy estimates represents a large fraction of total capex) can attract conventional infrastructure financing that cannot be secured for nuclear-specific construction — broadening the capital base

**Port of Victoria, Texas project:** The site is at the Port of Victoria, south of the city of Victoria in Calhoun County. The Victoria County Navigation District has formally partnered with Blue Energy on the project. The 1.5 GW capacity makes this one of the largest announced SMR projects by output. The Crusoe AI datacenter campus at this site would be powered behind-the-meter — avoiding ERCOT grid interconnection delays that affect competing datacenter power strategies.

## Notable Developments

- **2025 (early):** NRC approves Blue Energy's licensing topical report (BE-BOPTR-02-NP) — formally authorizes the construction resequencing approach; clarifies which project elements require prior NRC approval and which do not. ([Blue Energy](https://blueenergy.co/blue-energy-achieves-key-u-s-nrc-licensing-milestone-paving-the-way-for-power-in-48-months-or-less-with-natural-gas-bridge/))
- **2024 (late):** Blue Energy and Crusoe announce partnership to develop 1.5 GW nuclear-powered AI datacenter campus at Port of Victoria, TX; gas bridge 2028, nuclear 2031. ([Blue Energy](https://blueenergy.co/blue-energy-and-crusoe-partner-to-develop-advanced-nuclear-powered-ai-data-center-project-in-port-of-victoria-texas/)) ([Data Center Dynamics](https://www.datacenterdynamics.com/en/news/crusoe-taps-blue-energy-to-supply-nuclear-power-for-up-to-15gw-data-center-in-port-of-victoria-texas/))
- **2024-10:** Series A — $45M; Engine Ventures and At One Ventures lead. ([VC News Daily](https://www.vcnewsdaily.com/blue-energy/venture-capital-funding/xtcsftnkgn))
- **2023:** Founded by Jake Jurewicz and Matt Slotkin; emerged from MIT Nuclear Science & Engineering.
- **2026 Q2 (planned):** Construction begins at Port of Victoria site on non-nuclear infrastructure.
- **2027 (planned):** NRC construction permit application filed.
- **2028 (targeted):** Gas bridge power delivery to Crusoe campus.
- **2031 (targeted):** Nuclear generation begins at Port of Victoria.

## Key People

### Jake Jurewicz — Co-Founder and CEO
- **LinkedIn:** Search "Jake Jurewicz Blue Energy nuclear"
- **Role:** Co-founder and CEO
- **Background:** MIT Nuclear Science & Engineering Department; one of the two original founders; leads company strategy and external relationships including the Crusoe partnership and NRC engagement
- **Notes:** Nuclear engineer by training; the MIT NSE origin gives Blue Energy technical credibility in LWR design and NRC engagement that purely finance-led nuclear startups lack

### Matt Slotkin — Co-Founder
- **LinkedIn:** Search "Matt Slotkin Blue Energy"
- **Role:** Co-founder
- **Background:** MIT NSE peer of Jurewicz; co-developed the shipyard construction model; specific current title not confirmed in public sources

### Antonios Zoulis — Nuclear Licensing Advisor
- **LinkedIn:** Search "Antonios Zoulis Blue Energy"
- **Role:** Senior licensing and regulatory advisor
- **Background:** 30+ years of commercial and nuclear regulatory experience; supports NRC licensing activities; critical for navigating topical report approval and construction permit process
- **Notes:** This kind of senior licensing expertise is a genuine differentiator for early-stage nuclear startups — NRC engagement requires deep institutional knowledge

### People — Last Reviewed: 2026-03-25

## Supply Chain Position

Blue Energy sits at the **Nuclear Power Plant Developer/Owner-Operator** layer — designing the plant, contracting fabrication, securing NRC licensing, and owning/operating the facility under long-term PPAs.

| Layer | Detail |
|-------|--------|
| **Fuel (upstream)** | Low-enriched uranium (LEU) — LWR fuel; multiple NRC-licensed US fabricators (Global Nuclear Fuel, Framatome, Westinghouse); less constrained than HALEU required by Gen IV designs |
| **Reactor pressure vessel** | Heavy forgings required; Japan Steel Works and Doosan are primary global sources; 3–5 year lead times |
| **Turbine-generators** | GE Vernova, Siemens Energy, Mitsubishi Power — standard steam turbine supply chain; not nuclear-specific |
| **Modular fabrication** | Shipyards/fab yards (specific contractor not disclosed) — the key manufacturing partnership Blue Energy has not yet named publicly |
| **NRC licensing** | In-progress; topical report approved; construction permit application planned 2027 |
| **EPC contractor** | Not yet publicly named |
| **Power customer (downstream)** | Crusoe (Port of Victoria, TX); PPA structure, no upfront capital for customer |

**⚑ Fabrication partner not disclosed:** The shipyard manufacturing model is Blue Energy's primary cost and schedule claim, but the specific shipyard or fab yard partner has not been named publicly. The credibility of the 3-year build time depends entirely on which fabricator is engaged, their capacity, and their experience with nuclear-grade quality assurance. This is the most important unverified element in Blue Energy's story.

**⚑ LWR fuel supply is relatively benign:** Unlike HALEU-dependent designs (X-energy, Oklo), Blue Energy's LWR design uses standard low-enriched uranium. The US LEU supply chain is well-established with multiple qualified fabricators. This is a genuine risk reduction vs. Gen IV competitors.

## Claim Verification

### Claim: 3-year build time vs. 10+ years traditionally
**Status:** Unverified; NRC topical report approval is a necessary but not sufficient precondition; no shipyard nuclear build has been completed at this scale

**Mechanism claimed:** Shipyard/modular fabrication eliminates sequential on-site construction; parallel fabrication of modules; factory QA vs. field QA. This is the same logic that reduced offshore wind platform construction times.

**Supporting:**
- NRC approval of construction resequencing topical report confirms the regulatory pathway is viable — a real milestone
- The offshore oil & gas analogy is genuinely applicable: platform jacket fabrication at shipyards has achieved remarkable scale and speed
- LWR technology eliminates the licensing novelty risk that has delayed Gen IV designs for decades

**Refuting / questioning:**
- Nuclear quality assurance (10CFR50 Appendix B) is more stringent than oil & gas quality systems; the assumption that a shipyard can simply switch to nuclear-grade QA is unproven at scale
- No modular shipyard-constructed commercial nuclear power plant exists anywhere in the world; the claim is a design-stage projection, not an operational result
- NuScale, Rolls-Royce SMR, and others have made similar cost/schedule claims at design stage; NuScale's CFPP project was cancelled due to cost overruns before it broke ground
- The specific shipyard partner has not been named; without a named, qualified fabricator, the 3-year timeline is aspirational
- The 2031 nuclear generation target was announced in late 2024; a 7-year timeline to nuclear generation is less aggressive than the "3 years" headline suggests

**Summary:** The construction resequencing approach is novel and NRC-approved — a legitimate regulatory achievement. The 3-year claim is the design-stage target for the nuclear portion once the gas bridge is operating; the full gas-to-nuclear timeline is ~7 years from now. The claim should be tracked against (1) fabricator announcement, (2) NRC construction permit application in 2027, and (3) actual construction start of nuclear components.

### Claim: $5,000/kW cost vs. $13,000/kW traditional
**Status:** Design-stage target; unverified; no reference plant exists

**Supporting:**
- The $13,000/kW figure is accurate for recent stick-built US nuclear (Vogtle Units 3 & 4 came in at ~$14,000–$17,000/kW)
- The $5,000/kW target is consistent with what Korean and Chinese shipyard-built reactors have achieved historically (APR-1400 in UAE at ~$5,400/kW); this is the most credible evidence that the target is achievable
- Modular manufacturing does systematically reduce costs in analogous industries

**Refuting / questioning:**
- Korean/UAE nuclear builds involved established utilities with decades of nuclear experience and lower labor costs; a startup applying the same model faces a steeper learning curve
- The NRC's more stringent quality requirements than Korean or UAE regulatory frameworks add cost that may not appear in international comparisons

**Summary:** The $5,000/kW target is credible as a design goal with historical precedent in international nuclear builds. Whether a US startup can achieve it in a US regulatory environment is unproven. Track against first construction permit costs and independent project finance underwriting assumptions when available.

## Sources

- [Blue Energy — blueenergy.co](https://blueenergy.co/)
- [Blue Energy and Crusoe Partner for Port of Victoria TX — Blue Energy](https://blueenergy.co/blue-energy-and-crusoe-partner-to-develop-advanced-nuclear-powered-ai-data-center-project-in-port-of-victoria-texas/)
- [Blue Energy Achieves NRC Licensing Milestone — Blue Energy](https://blueenergy.co/blue-energy-achieves-key-u-s-nrc-licensing-milestone-paving-the-way-for-power-in-48-months-or-less-with-natural-gas-bridge/)
- [Crusoe Taps Blue Energy for Port of Victoria Nuclear — Data Center Dynamics](https://www.datacenterdynamics.com/en/news/crusoe-taps-blue-energy-to-supply-nuclear-power-for-up-to-15gw-data-center-in-port-of-victoria-texas/)
- [Blue Energy and Crusoe Plan Texas Nuclear-Powered Data Centre — World Nuclear News](https://world-nuclear-news.org/articles/blue-energy-and-crusoe-unveil-texas-nuclear-powered-data-centre-plan)
- [Blue Energy Series A ($45M) — VC News Daily](https://www.vcnewsdaily.com/blue-energy/venture-capital-funding/xtcsftnkgn)
- [Blue Energy — Accelerating SMR Deployments — Nucleation Capital](https://nucleationcapital.com/blue-energy-accelerating-deployment-smrs)
- [Blue Energy NRC Pre-Application Activities — U.S. NRC](https://www.nrc.gov/reactors/new-reactors/advanced/who-were-working-with/pre-application-activities/blue-energy)
- [Victoria County Navigation District Partners with Blue Energy — Port of Victoria](https://www.portofvictoria.com/news-and-media/p/item/65061/victoria-navigation-district-partners-with-blue-energy-to-advance-small-modular-nuclear-power-project)
