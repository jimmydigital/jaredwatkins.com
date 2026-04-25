---
title: "QuantumScape"
date: 2026-04-24
lastmod: 2026-04-24
draft: false
description: "San Jose anode-free lithium-metal battery company; sulfide-based ceramic separator (Cobra process); QSE-5 B-samples shipping Q3 2025; Eagle Line pilot (Feb 2026) producing commercial-format cells; PowerCo non-exclusive license 40–80 GWh/year; Murata manufacturing partnership for ceramic separators; capital-light licensing model; FY2026 EBITDA guidance −$250M–$275M; $904.7M Q1 2026 liquidity."
tags: ["batteries", "solid-state", "lithium-metal", "anode-free", "us", "ev", "public"]
categories: ["company"]
research_area: "energy/batteries"
source_urls:
  - "https://www.quantumscape.com"
  - "https://www.quantumscape.com/blog/a-first-look-at-the-qse-5-b-sample/"
  - "https://www.quantumscape.com/resources/blog/coulombic-efficiency-demystified/"
  - "https://corporate.murata.com/en-us/newsroom/news/company/general/2025/1008"
  - "https://www.volkswagen-group.com/en/press-releases/powerco-and-quantumscape-announce-landmark-agreement-to-industrialize-solid-state-batteries-18494"
  - "https://www.fool.com/earnings/call-transcripts/2026/04/22/quantumscape-qs-q1-2026-earnings-transcript/"
  - "https://www.batterytechonline.com/design-manufacturing/quantumscape-updates-commercialization-strategy-for-solid-state-battery-technology"
last_reviewed: 2026-04-24
stale_after_days: 90
related:
  - "energy/batteries/lithium-metal.md"
  - "energy/batteries/solid-state-batteries.md"
---

## Summary

QuantumScape (NYSE: QS) is a San Jose, California lithium-metal battery developer pursuing an anode-free cell architecture using a proprietary ceramic separator (Cobra process) and sulfide-based solid electrolyte. The company is the highest-profile independent pure-play in the solid-state space, backed by Volkswagen since 2018 and publicly listed via SPAC in 2020. The QSE-5 cell (5 Ah, 844 Wh/L, 301 Wh/kg) began shipping B1-grade samples to automotive customers in Q3 2025. The Eagle Line pilot production facility was inaugurated in February 2026 and is ramping QSE-5 cell production. Volkswagen Group's PowerCo unit holds a non-exclusive license to produce up to 40 GWh/year (option to 80 GWh), marking QuantumScape's strategic pivot to a capital-light technology licensing model. As of Q1 2026, the company held $904.7M in liquidity and is guiding FY2026 EBITDA loss of −$250M–$275M.

## Technology Overview

### Why Lithium Metal Matters

Lithium metal as an anode material has a theoretical specific capacity of **3,860 mAh/g**, compared to graphite's **372 mAh/g** — roughly a 10-fold advantage per unit weight. Using lithium metal instead of graphite enables cell-level energy density improvements of 50–100% at the same pack weight, or the same range at dramatically lower weight and cost. For electric vehicles, this translates to either 50–80% longer driving range or significantly reduced pack weight and cost. This is why lithium metal is the focus of virtually every advanced battery chemistry: it is the single largest opportunity for energy density improvement in electrochemistry at the anode.

### The Dendrite Problem (50+ Years of Attempted Solutions)

Lithium metal is highly reactive. When lithium deposits during charging in conventional liquid electrolytes, it does not form a smooth, uniform layer. Instead, it plates unevenly, forming needle-like crystalline structures called dendrites that grow outward and often branch, resembling a pine tree. Over tens or hundreds of charge cycles, these dendrites grow long enough to penetrate the separator (the thin membrane between anode and cathode), make contact with the cathode, and cause an internal short circuit. The short circuit generates heat, which ignites the flammable liquid electrolyte, causing thermal runaway and potentially fire.

This is the reason commercial lithium-ion batteries use graphite anodes instead of lithium metal, despite the massive energy density penalty: graphite intercalates lithium safely into a stable crystal structure, preventing dendrite formation. However, the cost in energy density is enormous.

Every approach to lithium-metal battery commercialization is fundamentally a solution to the dendrite problem. The solutions differ in approach and tradeoff:

- **Solid ceramic electrolytes** (e.g., LLZO) physically block dendrite growth mechanically — they are hard enough that dendrites cannot penetrate them — but they are brittle, difficult to manufacture at scale, and suffer from high interface resistance.
- **Solid sulfide electrolytes** conduct lithium ions more efficiently than oxides, are softer and form better interfaces, but are more chemically reactive and require more careful manufacturing.
- **Hybrid and semi-solid approaches** use a liquid or gel component to reduce manufacturing complexity while relying on engineered separators or additives to suppress dendrites, gaining manufacturability at some cost to safety.
- **Protective coatings and engineered SEI** (solid electrolyte interphase) on the lithium surface attempt to regulate the deposition environment and slow dendrite growth, but do not eliminate it.

QuantumScape's approach combines elements of solid ceramic separators and solid sulfide electrolytes in a specific architecture designed to eliminate both dendrites and the manufacturing complexity of handling metallic lithium.

### QuantumScape's Solution: Anode-Free + Ceramic Separator

QuantumScape's QSE-5 cell uses a novel **anode-free** architecture: there is no pre-deposited lithium metal in the cell at manufacturing time. Instead, the cell is shipped with a cathode, a sulfide-based solid electrolyte, and a proprietary ceramic separator — but no lithium anode. During the first charge, lithium ions are extracted from the cathode (which must contain excess lithium), migrate through the solid electrolyte, and plate onto the anode side of the ceramic separator, forming a lithium metal anode in situ during first use.

**Advantages of anode-free design:**

1. **Manufacturing simplicity:** Lithium metal is hazardous to handle — it reacts with air and moisture. Eliminating lithium metal from the manufacturing process avoids the need for dry-room handling and reduces manufacturing complexity and cost.
2. **No dendrite growth during manufacturing:** The anode is formed only in the electrochemical environment of the cell, where the solid electrolyte and ceramic separator are present to suppress dendrites. There is no period during manufacturing where metallic lithium is exposed.
3. **Architectural leverage:** The ceramic separator physically suppresses dendrite growth by virtue of its material hardness and ionic conductivity, while the sulfide electrolyte provides efficient lithium-ion transport and a stable interface.

**Challenges and risks:**

1. **First-cycle irreversible loss:** The lithium extracted from the cathode during first charge cannot all be recovered. The lithium that plates on the anode gets "trapped" by interface reactions and is not available for subsequent cycles. This is called first-cycle coulombic efficiency loss, and QuantumScape reports coulombic efficiency better than 99.99% — meaning less than 0.01% of the lithium is lost per cycle after formation. However, the *first* cycle is the critical bottleneck: excess lithium must be built into the cathode material to account for this loss, and the amount of excess must be carefully managed.
2. **Cathode engineering:** The cathode must be engineered to tolerate repeated extraction and insertion of lithium, and to maintain structural integrity over 1,000+ cycles of significant volume change.
3. **Operating conditions:** The anode forms and operates under electrochemical stress. Temperature, charge rate, and depth of discharge all affect the anode's morphology and dendrite resistance.

QuantumScape's claim to superiority rests on the combination of (a) the ceramic separator's mechanical dendrite suppression, (b) the sulfide electrolyte's ionic conductivity and stability, and (c) the anode-free architecture's simplified manufacturing.

### Cobra Manufacturing Process

The Cobra process is QuantumScape's proprietary method for manufacturing the ceramic separator at scale. The term "Cobra" refers to the serpentine or coiled deposition path used in the process, though the specific chemistry and equipment are proprietary. Cobra produces a dense, thin ceramic film with precise ionic conductivity and mechanical properties.

Cobra was fully integrated into QuantumScape's baseline production in 2025. The Eagle Line pilot facility (opened Feb 2026) uses Cobra as its primary separator manufacturing method. The process is critical to QuantumScape's ability to reach gigawatt-hour scale manufacturing, as it determines the yield, consistency, and cost of the separator — the single most expensive and critical component of the cell.

### QSE-5 Cell Specifications

| Specification | Value | Context |
|---------------|-------|---------|
| **Capacity** | 5 Ah | Commercial format for automotive |
| **Gravimetric energy density** | 301 Wh/kg | Measured at C/5 discharge rate, 25°C, 100% SoC |
| **Volumetric energy density** | 844 Wh/L | Measured at C/5 discharge rate, 25°C, 100% SoC |
| **10–80% charge time** | 12.2 minutes | Claimed; conditions not disclosed in published materials |
| **Capacity retention at 1,000 cycles** | >95% | After 1,000 full charge-discharge cycles at room temperature |
| **Coulombic efficiency** | >99.99% | Per-cycle efficiency; better than 99.99% |
| **Operating pressure** | <3.4 atm | Sealed cell operating envelope |
| **Cell format** | FlexFrame (hybrid prismatic/pouch) | Designed for automotive pouch cells |

**Note on charge time:** The 12.2-minute 10–80% charge claim is high-profile but lacks published details on the current rate (C-rate), temperature, or ambient conditions. The claim appears to assume elevated temperature operation or a specific charging protocol not yet disclosed in public materials. Independent validation from automotive OEM testing (ongoing as of early 2026) will clarify the real-world conditions under which this performance is achieved.

### Ceramic Separator and Murata Partnership

The ceramic separator is the core IP. Murata Manufacturing — one of the world's largest precision ceramics companies, known for ceramic capacitors — announced a framework agreement (April 2025) and joint development agreement (October 2025) to scale Cobra separator production. Murata brings expertise in ceramic material formulation, sheet forming, sintering (high-temperature firing), and precision quality control from decades of ceramic components manufacturing. The companies are exploring business models for commercialization, with the goal of establishing a global supplier ecosystem capable of gigawatt-hour-scale production by the late 2020s.

In Q1 2026, QuantumScape reported continuing partnership development with both Murata and Corning to scale Cobra production and build a global value chain.

## Key Facts

- **Founded:** 2010 (incorporated in Delaware; operations in San Jose)
- **HQ:** San Jose, CA, USA
- **Type:** Public (NYSE: QS; SPAC IPO December 2020)
- **Key backers:** Volkswagen Group (strategic investor since 2018; ~9.9% equity stake as of Q1 2026; two board seats; ~$300M total capital committed as of 2026)
- **Technology:** Anode-free lithium-metal cell with sulfide-based solid electrolyte and proprietary ceramic separator ("Cobra" process)
- **QSE-5 cell specs:** 5 Ah capacity; 844 Wh/L volumetric density; 301 Wh/kg gravimetric density; 12.2-minute 10–80% charge (claimed); >95% capacity retention at 1,000 cycles; coulombic efficiency >99.99%
- **Cell status:** B1-grade samples shipping to automotive customers (Q3 2025); production ramping at Eagle Line
- **Eagle Line pilot:** Inaugurated February 2026; designed for higher-volume QSE-5 cell production; Q2 2026 ramping to support customer programs
- **Manufacturing partners:** Murata Manufacturing (ceramic separator scale-up, JDA Oct 2025); Corning (separator production scaling partnership, ongoing as of Q1 2026)
- **Business model:** Capital-light technology licensor model — licensing Cobra process and cell design IP to manufacturers and OEMs rather than building all manufacturing in-house
- **PowerCo (Volkswagen) license:** Non-exclusive license to produce up to 40 GWh/year cells using QuantumScape technology; option to expand to 80 GWh; announced March 2026; represents QuantumScape's primary automotive partnership
- **Secondary markets:** Defense/aerospace drones, AI data center power, robotics (announced 2026)
- **Financial position (Q1 2026):** $904.7M liquidity; GAAP net loss $100.8M (Q1); FY2026 adjusted EBITDA guidance −$250M to −$275M; 2026 cash investment guidance included in annual guidance
- **Mass production timeline:** First customer production ~2027–2028 (dependent on PowerCo and other OEM timelines)

## What It Is / How It Works

See the [Technology Overview](#technology-overview) section above for detailed explanation of lithium-metal anodes, the dendrite problem, anode-free architecture, Cobra process, and Murata partnership.

At a high level: QuantumScape makes lithium-metal cells with a proprietary ceramic separator that suppresses dendrite formation, enabling long cycle life and safety. The anode-free design (no pre-loaded lithium metal) simplifies manufacturing. The QSE-5 B1-grade samples (5 Ah, 301 Wh/kg) began shipping to automotive OEMs in Q3 2025 and are undergoing vehicle-level integration testing as of early 2026.

**Licensing Strategy:**

As of March 2026, QuantumScape has formally pivoted to a capital-light technology licensing model. Rather than trying to own all cell manufacturing at gigawatt scale, the company licenses its Cobra ceramic separator process and cell design IP to established battery manufacturers and OEMs. The PowerCo (Volkswagen) non-exclusive license announced in March 2026 — permitting up to 40 GWh/year production with an option to expand to 80 GWh — is the first major expression of this model.

CEO Siva Sivaram framed this approach as "demonstrate, distribute, develop":

1. **Demonstrate:** Prove the technology works at scale (Eagle Line pilot ramping Q2 2026).
2. **Distribute:** License to established manufacturers who already have production infrastructure and OEM relationships (PowerCo, Murata, others).
3. **Develop:** Continue advancing materials, process, and cell design IP while licensees handle manufacturing scale-up.

This approach mirrors ARM's semiconductor licensing model: QuantumScape captures licensing royalties and technology fees while avoiding the multi-billion-dollar capital requirements of owning gigawatt-scale fabs. The tradeoff is dependency on licensees' execution and manufacturing ramp success.

**Secondary Markets:**

In 2026, QuantumScape announced expansion into drone/defense aerospace (via IQT — CIA's strategic investment arm), AI data center power backup, and robotics. These markets value energy density and thermal stability more than EV cost, giving QuantumScape proof-of-concept revenue streams while automotive products mature.

## Notable Developments

- **2026-04:** Q1 2026 earnings: $904.7M liquidity; Q1 GAAP net loss $100.8M; FY2026 adjusted EBITDA guidance −$250M to −$275M reconfirmed; Eagle Line production ramping Q2 2026 to support customer programs.
- **2026-03:** CEO Siva Sivaram publishes one-year-into-CEO-role strategy update (March 2026); outlines capital-light "demonstrate, distribute, develop" licensing model; announces expansion into drones/defense (via IQT partnership), AI data center power, and robotics. ([Battery Tech Online](https://www.batterytechonline.com/design-manufacturing/quantumscape-updates-commercialization-strategy-for-solid-state-battery-technology))
- **2026-03:** PowerCo (Volkswagen Group's battery unit) announces non-exclusive licensing agreement: up to 40 GWh/year production capacity of cells using QuantumScape's ceramic separator technology; option to expand to 80 GWh. Two separate agreements with combined value ~$260M. PowerCo receives two board seats and has engineers stationed at QuantumScape.
- **2026-02:** Eagle Line pilot production facility inaugurated in San Jose; designed for higher-volume QSE-5 cell production; initial cells produced; startup operations underway.
- **2025-10:** Joint development agreement with Murata Manufacturing signed for manufacturing and scale-up of ceramic separators. ([Murata](https://corporate.murata.com/en-us/newsroom/news/company/general/2025/1008))
- **2025-10:** QuantumScape published "Coulombic Efficiency Demystified" technical note explaining >99.99% per-cycle efficiency and anode-free implications. ([QuantumScape](https://www.quantumscape.com/resources/blog/coulombic-efficiency-demystified/))
- **2025 (Q3):** B1-grade QSE-5 samples shipping to automotive launch customers for vehicle integration testing.
- **2025-04:** Framework agreement with Murata Manufacturing announced for ceramics separator collaboration. ([QuantumScape](https://www.quantumscape.com/quantumscape-and-murata-announce-framework-for-ceramics-collaboration/))
- **2025:** Cobra separator process fully integrated into baseline production; enables QSE-5 pilot production scaling.
- **2020 (Dec):** SPAC IPO on NYSE (QS) via merger with Kandi Technologies Corp; $680M raised.
- **2018:** Volkswagen Group strategic investment (initially $100M, expanded through 2026).

## Key People

### Jagdeep Singh — Co-Founder and Executive Chairman
- **LinkedIn:** [linkedin.com/in/jagdeep-singh-3b2a9222](https://www.linkedin.com/in/jagdeep-singh-3b2a9222/)
- **Role:** Co-founder; CEO from founding through early 2024; now Executive Chairman
- **Education:** University of Maryland (BS Computer Science) → Stanford University (MS) → UC Berkeley (MBA)
- **Career (reverse-chronological):**
  - QuantumScape (2010–present): Co-founder; CEO 2010–Feb 2024; Executive Chairman Feb 2024–present
  - Deep Valley Labs LLC (2024–present): Founder, VC firm focusing on innovative startups (concurrent with Chairman role)
  - Infinera (2001–2009): Co-founder and CEO
  - Lightera Networks: Co-founder (sold to Ciena)
  - Airsoft: Founder
  - Hewlett Packard: Early career

### Siva Sivaram — President and CEO (since February 2024)
- **LinkedIn:** [linkedin.com/in/siva-sivaram-1394ab5b](https://www.linkedin.com/in/siva-sivaram-1394ab5b/)
- **Role:** CEO since February 15, 2024; joined QuantumScape as President in September 2023; oversees commercialization strategy, manufacturing partnerships, and OEM relationships
- **Education:** National Institute of Technology, India (BS Mechanical Engineering) → Rensselaer Polytechnic Institute, Troy NY (MS Materials Science and PhD Materials Science)
- **Career (reverse-chronological):**
  - QuantumScape (Sep 2023–present): President (Sep–Feb 2024); CEO from Feb 2024; led pivot to capital-light licensing model (March 2026)
  - Western Digital Corp. (Nov 2017–Aug 2023): EVP Silicon Technology & Manufacturing (2017–2019, NAND flash memory); President, Technology & Strategy (2019–2023, oversaw manufacturing operations, R&D strategy)
  - SanDisk Corp. (acquired by Western Digital June 2016): EVP Memory Technology (2012–2016, flash NAND memory development)
  - Twin Creek Technologies (2008–2013): Founder and CEO (solar panel manufacturing equipment; divested to Applied Materials in 2018)
  - Matrix Semiconductor (2004–2008): VP Manufacturing (3D NAND and memory technology); acquired by Intel
  - Intel (early career, dates not publicly disclosed): Process engineer roles in semiconductor manufacturing
  - Earlier roles at multiple semiconductor/storage companies
- **Notes:** Sivaram's entire career has been in semiconductor/data storage manufacturing scale-up (NAND flash, 3D memory, silicon process). He is not originally from the battery sector. He was recruited to QuantumScape explicitly for his experience scaling manufacturing infrastructure in precision industries. The hire raised questions in 2023 about whether a memory technologist was the right background for battery manufacturing, but Sivaram's strategic pivot to capital-light licensing (Feb 2024–Mar 2026) and his emphasis on partnership-driven scale (Murata, Corning, PowerCo) suggest his semiconductor manufacturing architecture experience translated directly to batteries. **⚑ Context:** This unusual executive choice (memory technologist leading a battery company) signals that QuantumScape's board and founders viewed the critical challenge as *manufacturing execution and supply chain orchestration*, not battery chemistry — which was already proven by Tim Holme's team.

### Tim Holme — CTO and Co-Founder
- **LinkedIn:** No confirmed public profile found; Stanford Energy profile: [energy.stanford.edu/people/tim-holme](https://energy.stanford.edu/people/tim-holme)
- **Role:** CTO since founding; oversees advanced materials research, technical product development, machine learning, and IP
- **Education:** Stanford University (BS Physics; MS Mechanical Engineering; PhD Mechanical Engineering — Professor Fritz Prinz lab)
- **Career (reverse-chronological):**
  - QuantumScape (Jan 2011–present): CTO and co-founder
  - Stanford University (Jun 2008–Jan 2011): Research Associate in Professor Fritz Prinz's lab (materials science and electrochemistry of energy conversion and storage)
- **Notes:** QuantumScape was co-founded by Tim Holme, Jagdeep Singh, and Professor Fritz Prinz. Holme came directly from Prinz's Stanford lab where the ceramic separator research originated — he is the only co-founder whose entire career has been at QuantumScape.

**⚑ Overlap note:** Celina Mikolajczak (now CTO at [Lyten]({{< relref "lyten.md" >}})) served as VP of Manufacturing at QuantumScape in 2021 before departing to join Lyten in 2022. See Lyten Key People for details.

### People — Last Reviewed: 2026-03-24

## Supply Chain Position

QuantumScape operates at the **Cell Manufacturing** layer (Layer 4 in the batteries section value chain). The company produces QSE-5 cells in-house at its Eagle Line pilot facility in San Jose, but has pivoted to a distributed manufacturing model via PowerCo licensing.

**Upstream dependencies:**

- **Ceramic separator (Cobra process):** Proprietary IP owned by QuantumScape; manufactured in partnership with Murata Manufacturing (framework agreement April 2025, JDA Oct 2025). Murata supplies ceramic material expertise; QuantumScape owns the process. Scaling to multi-gigawatt capacity by late 2020s.
- **Sulfide solid electrolyte material:** QuantumScape synthesizes in-house; chemistry based on sulfide compounds requiring [lithium sulfide (Li₂S)]({{< relref "../resources/sulfur.md" >}}) as a precursor. **⚑ Critical upstream risk:** QuantumScape has not publicly disclosed its Li₂S supplier. The market has limited large-scale Li₂S capacity: Idemitsu Kosan (the only named large-scale producer at 1,000 MT/year by June 2027) is committed exclusively to Toyota. QuantumScape must either (a) secure alternate Li₂S supply, (b) develop captive Li₂S synthesis, or (c) share Idemitsu capacity with competing programs — none of which have been publicly confirmed.
- **Cathode materials:** Undisclosed; likely sourced from major precursor suppliers (POSCO Future M or others).
- **Lithium:** No specific supply agreement disclosed; sourced via material partners or downstream.

**Downstream:**

- **Primary OEM partner:** Volkswagen Group via PowerCo (40–80 GWh/year license, announced March 2026).
- **Secondary markets:** Defense/aerospace (via IQT partnership, 2026); AI data center (2026); other undisclosed automotive OEMs receiving B1 samples.
- **Manufacturing licensees:** PowerCo is the first; others may follow.

**⚑ Supply chain chokepoint:** All sulfide-based solid-state programs globally (QuantumScape, Solid Power, Idemitsu/Toyota) compete for Li₂S precursor. Idemitsu's exclusive commitment to Toyota creates a structural bottleneck for QuantumScape and Solid Power if both scale simultaneously post-2027.

## Claim Verification

### Claim 1: QSE-5 Energy Density — 844 Wh/L (volumetric), 301 Wh/kg (gravimetric)
**Status:** Verified (internal characterization; shipped to OEMs for validation)

**Supporting sources:**
- [QuantumScape QSE-5 B Sample technical note](https://www.quantumscape.com/blog/a-first-look-at-the-qse-5-b-sample/) — Detailed measurements at C/5 discharge, 25°C, 100% SoC; FlexFrame format specified.
- Measurements conducted at room temperature (25°C) and slow discharge rate (C/5, or 5-hour discharge), which tend to maximize apparent energy density compared to fast-charge or elevated-temperature conditions.

**Refuting / questioning sources:**
- None identified for the stated values at the stated conditions.

**Summary:** Energy density figures are company-reported and measured under standardized internal conditions (C/5, 25°C). The slow discharge rate (C/5) is more favorable than automotive driving conditions (typically 1–3C). Real-world energy density in vehicles will likely be 10–20% lower depending on discharge rate and temperature. No independent OEM validation results published yet (B1 testing ongoing as of April 2026).

---

### Claim 2: 12.2-Minute 10–80% Charge Time
**Status:** Claimed but conditions unclear; requires independent OEM validation

**Supporting sources:**
- QuantumScape has published this figure in corporate communications and presentations.

**Questions and missing context:**
- No published documentation of the charging current (C-rate), temperature during charge, or ambient conditions (cold start vs. warm battery).
- QuantumScape's published blog and technical materials emphasize coulombic efficiency and cycle life but do not detail the 12.2-min charge test protocol.
- The claim is plausible given the high ionic conductivity of the sulfide electrolyte and anode-free design, but it cannot be independently verified from public materials.

**Refuting / questioning sources:**
- None identified, but the absence of detailed test protocols raises questions about reproducibility and real-world conditions.

**Summary:** The 12.2-minute figure is aspirational and likely achievable under optimized conditions (elevated temperature, specific C-rate), but the exact conditions are not documented. Independent OEM validation (Mercedes, VW, others) will clarify the real-world charging performance over the next 12–24 months.

---

### Claim 3: >95% Capacity Retention at 1,000 Cycles
**Status:** Verified (internal characterization)

**Supporting sources:**
- QuantumScape Q1 2026 earnings and investor materials cite >95% retention at 1,000 cycles.
- Coulombic efficiency >99.99% per cycle (published in technical note) supports long-cycle behavior.

**Context:**
- This is achieved under controlled lab conditions (likely 25°C, moderate discharge rate).
- Real-world cycle life (accounting for temperature extremes, varied charge rates, and depth-of-discharge) will be validated by automotive OEMs during B2/C-sample phases (2026–2027).

**Summary:** Laboratory cycle life metrics are verified. Real-world automotive validation ongoing.

---

### Claim 4: Coulombic Efficiency >99.99%
**Status:** Verified (published technical note)

**Supporting sources:**
- [QuantumScape "Coulombic Efficiency Demystified" blog post](https://www.quantumscape.com/resources/blog/coulombic-efficiency-demystified/) — Detailed explanation of >99.99% per-cycle efficiency and implications for anode-free design.

**Context:**
- This figure excludes first-cycle irreversible loss (which is managed through cathode over-lithiation).
- Per-cycle efficiency >99.99% means <0.01% lithium loss per cycle, enabling long cycle life.

**Summary:** High coulombic efficiency is a key technical achievement. The figure is company-reported but is chemically plausible given anode-free architecture and solid electrolyte suppression of parasitic side reactions.

---

### Claim 5: Anode-Free Design Simplifies Manufacturing and Eliminates Dendrite Handling Risk
**Status:** Theoretically sound; manufacturing validation pending

**Supporting sources:**
- Academic literature on anode-free batteries and solid electrolytes supports the principle.
- QuantumScape's technical publications (Coulombic Efficiency Demystified, etc.) explain the rationale.

**Validation status:**
- Eagle Line is the first production test; yield rates, manufacturing repeatability, and cost per cell at scale have not been published.
- PowerCo's manufacturing ramp (2026–2028) will provide first real-world manufacturing validation.

**Summary:** The anode-free approach is technically sound and reduces lithium metal handling complexity, but full manufacturing validation is pending Eagle Line and PowerCo production ramp.

## Sources

**Company publications & technical:**
- [QuantumScape — Corporate website](https://www.quantumscape.com)
- [A First Look at the QSE-5 B Sample — QuantumScape (Oct 2025)](https://www.quantumscape.com/blog/a-first-look-at-the-qse-5-b-sample/)
- [Coulombic Efficiency Demystified — QuantumScape (2025)](https://www.quantumscape.com/resources/blog/coulombic-efficiency-demystified/)

**Partnerships & milestones:**
- [QuantumScape and Murata Announce Framework for Ceramics Collaboration — QuantumScape (Apr 2025)](https://www.quantumscape.com/quantumscape-and-murata-announce-framework-for-ceramics-collaboration/)
- [Murata and QuantumScape Joint Development Agreement — Murata (Oct 2025)](https://corporate.murata.com/en-us/newsroom/news/company/general/2025/1008)
- [PowerCo and QuantumScape Announce Landmark Agreement — Volkswagen Group (Mar 2026)](https://www.volkswagen-group.com/en/press-releases/powerco-and-quantumscape-announce-landmark-agreement-to-industrialize-solid-state-batteries-18494)

**Financial & strategy:**
- [QuantumScape Q1 2026 Earnings Transcript — The Motley Fool (Apr 2026)](https://www.fool.com/earnings/call-transcripts/2026/04/22/quantumscape-qs-q1-2026-earnings-transcript/)
- [QuantumScape Updates Commercialization Strategy — Battery Tech Online (Mar 2026)](https://www.batterytechonline.com/design-manufacturing/quantumscape-updates-commercialization-strategy-for-solid-state-battery-technology)
