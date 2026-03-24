---
title: Battery Technology Research
date: 2026-03-23
lastmod: 2026-03-23
draft: false
description: Research on emerging battery technologies including solid-state, flow batteries, and high-density storage.
tags: ["batteries", "energy"]
categories: ["overview"]
research_area: "energy/batteries"
last_reviewed: 2026-03-23
stale_after_days: 365
---

## Overview

Tracks advances in battery chemistry and storage technology, with a focus on solid-state batteries, flow batteries, and the companies and researchers pushing energy density and cycle life forward.

## Key Themes

- Solid-state electrolytes (oxide, sulfide, polymer)
- High-energy-density cathode and anode materials
- Leading manufacturers and research institutions
- Safety, scalability, and cost-to-production challenges

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Factorial Energy](https://factorialenergy.com) | Cambridge, MA, USA | Pre-IPO | Semi-solid FEST® electrolyte platform; 375 Wh/kg validated with Stellantis; JDAs with Mercedes-Benz, Hyundai, Kia; expanding to drones/robotics. |
| [Donut Lab](https://donutlab.com) | Estonia (Finnish roots) | Private | Solid-state battery startup with production-ready cells in Verge Motorcycles; 400 Wh/kg and 100k-cycle claims unverified. |
| [Nordic Nano](https://nordicnano.fi) | Finland | Private | Manufacturing partner producing Donut Lab's amorphous titanium dioxide nanostructure-based cells. |
| [ProLogium Technology](https://prologium.com) | Taiwan | Pre-IPO | Oxide-based solid-state pioneer (est. 2006); Superfluidized All-Inorganic architecture unveiled CES 2026; Dunkirk gigafactory groundbreaking 2026. |
| [Adden Energy](https://addenenergy.com) | Cambridge, MA, USA | Series A | Harvard SEAS spinout; thin-film solid-state cells; 10,000-cycle and 10-min charge in lab; $20M raised; pilot line under construction. |
| [Lyten](https://lyten.com) | San Jose, CA, USA | Series B+ | 3D Graphene-enabled lithium-sulfur batteries; ~2× Li-ion energy density; no nickel/cobalt/graphite; $625M+ raised; acquired Northvolt BESS facility. |
| [Verge Motorcycles](https://vergemotorcycles.com) | Finland | Private | Electric motorcycle OEM; launch platform for Donut Lab solid-state cells; TS Pro shipping 2026. |
| [Idemitsu Kosan](https://www.idemitsu.com/en/) (Battery Materials) | Japan | Public subsidiary | 30-year sulfide electrolyte R&D; exclusive Toyota supplier; ¥21.3B Li₂S plant + solid electrolyte pilot plant under construction. |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [QS](https://finance.yahoo.com/quote/QS) | [QuantumScape](https://www.quantumscape.com) | Solid-state lithium-metal battery developer; sulfide-based separator; shipping B-samples to auto customers in 2025–2026. |
| [SLDP](https://finance.yahoo.com/quote/SLDP) | [Solid Power](https://www.solidpowerbattery.com) | All-solid-state lithium battery developer on roll-to-roll production line; cells in BMW i7 validation. |

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [TM](https://finance.yahoo.com/quote/TM) | [Toyota](https://global.toyota/en/) | Largest solid-state patent holder; signals commercial timeline (2027–2028 target); key customer for Idemitsu sulfide electrolyte. |
| [006400.KS](https://finance.yahoo.com/quote/006400.KS) | [Samsung SDI](https://www.samsungsdi.com) | Major cell manufacturer targeting 500 Wh/kg solid-state; market validation signal for Korea cell supply chain. |
| [PCRFY](https://finance.yahoo.com/quote/PCRFY) | [Panasonic](https://www.panasonic.com/global/home.html) | Lithium-ion incumbent (Tesla supplier) with solid-state R&D; no firm timeline; indicator of when the technology reaches mainstream tier-1 supply. |
| [300750.SZ](https://finance.yahoo.com/quote/300750.SZ) | [CATL](https://www.catl.com/en/) 🇨🇳 | World's largest EV battery maker; solid-state target ~2027; treat claims with additional skepticism. |

> **Note on CATL:** Chinese-owned. Performance claims and production timelines should be treated with additional skepticism until independently verified by non-affiliated third parties.

## Supply Chain

The supply chains for solid-state and lithium-sulfur batteries diverge significantly from conventional lithium-ion at the electrolyte and cathode layers. This section maps the chain from raw materials to OEM integration for the technologies documented here.

### Supply Chain Layers

| Layer | Key Inputs / Outputs | Companies Operating Here | Geographic Concentration Risk |
|-------|---------------------|--------------------------|-------------------------------|
| **1. Raw Materials** | Lithium (spodumene / brine), Sulfur, Cobalt, Nickel, Manganese | [SQM](https://www.sqm.com), [Albemarle](https://www.albemarle.com), [Ganfeng Lithium](https://www.ganfenglithium.com), [Pilbara Minerals](https://www.pilbaraminerals.com.au), [Tianqi Lithium](https://www.tianqilithium.com.au), [Glencore](https://www.glencore.com) | Lithium mining: Australia (~50% of hard rock), Chile/Argentina/Bolivia (brine); Lithium refining: China (~65%+); Cobalt: DRC ~75% of global production; Nickel: Indonesia ~40% |
| **2. Precursor Chemicals** | Lithium sulfide (Li₂S), NMC precursor (pCAM), lithium carbonate / lithium hydroxide | [Idemitsu Kosan]({{< relref "idemitsu-solid-state.md" >}}) (Li₂S), [Umicore](https://www.umicore.com) (pCAM, NMC precursor), [Sumitomo Metal Mining](https://www.smm.co.jp/E/) (cathode precursor for Toyota) | Li₂S production for sulfide electrolytes: Idemitsu is the only named large-scale supplier as of 2026; pCAM processing dominated by China, South Korea |
| **3. Electrolyte / Active Materials** | Sulfide solid electrolyte, oxide ceramic electrolyte, Li-S cathode (sulfur + graphene scaffold), NMC / NCA / LFP cathode powder | [Idemitsu Kosan]({{< relref "idemitsu-solid-state.md" >}}) (sulfide SE for Toyota), [Solid Power]({{< relref "solid-power.md" >}}) (sulfide SE for BMW/Samsung SDI), [Lyten]({{< relref "lyten.md" >}}) (3D Graphene Li-S cathode), [POSCO Future M]({{< relref "../resources/posco-future-m.md" >}}) (NMC cathode + anode) | Sulfide SE supply is a critical bottleneck; currently only Idemitsu at meaningful scale; ceramic oxide SE: ProLogium proprietary; |
| **4. Cell Manufacturing** | Assembled solid-state or Li-S pouch / prismatic cells | [Factorial Energy]({{< relref "factorial-energy.md" >}}) (FEST® semi-solid), [QuantumScape]({{< relref "quantumscape.md" >}}) (QSE-5 ceramic separator cell), [Adden Energy]({{< relref "adden-energy.md" >}}) (thin-film solid-state), [ProLogium]({{< relref "prologium.md" >}}) (oxide ASSB), Samsung SDI (integrating Solid Power electrolyte), [Lyten]({{< relref "lyten.md" >}}) (Li-S cells) | Cell manufacturing for ASSB is currently concentrated in Japan (Toyota/Idemitsu ecosystem), US (Factorial, QuantumScape, Adden), Taiwan (ProLogium), and scaling to Europe (Lyten/Gdańsk, ProLogium/Dunkirk) |
| **5. Pack Assembly** | Cell-to-pack integration; thermal management; BMS | [Verge Motorcycles]({{< relref "verge-motorcycles.md" >}}) / [Donut Lab]({{< relref "donut-lab.md" >}}) (motorcycle pack, air-cooled), FEV Group (ProLogium module engineering), Factorial OEM partners (Stellantis, Karma) | Incumbent tier-1 pack assemblers (Panasonic, Samsung SDI, CATL) still dominate conventional Li-ion; ASSB pack integration is OEM-specific |
| **6. OEM Integration** | Finished EV, motorcycle, drone, satellite systems | Stellantis, Mercedes-Benz, Hyundai, Kia (Factorial customers); Volkswagen (QuantumScape launch partner); BMW (Solid Power validation); Toyota (Idemitsu/ASSB program); IQT defense/drone (Factorial) | OEM integration timelines: 2027–2028 for Toyota, 2027+ for VW/BMW/Stellantis |

### Key Supply Chain Notes

**Lithium:** All documented companies require lithium. Top mining regions are Australia (hard rock spodumene, led by Pilbara Minerals) and the Lithium Triangle (Chile/Argentina/Bolivia brine, led by SQM and Albemarle). China controls the dominant share of lithium chemical refining (conversion to lithium hydroxide and lithium carbonate), creating a chokepoint even for Western-mined material. No documented battery company in this knowledge base has publicly disclosed a specific lithium supply agreement at the raw materials level.

**Sulfur:** Sulfur is a byproduct of petroleum and natural gas refining — one of the most abundant and cheapest industrial chemicals globally. This is a strategic advantage for lithium-sulfur (Lyten) and sulfide solid electrolyte programs (Solid Power, QuantumScape, Idemitsu). **⚑ Shared supplier advantage:** Idemitsu's unique position as both an oil company (producing sulfur as a refining byproduct) and a solid electrolyte manufacturer gives it a vertically integrated sulfur-to-Li₂S supply chain that no other documented electrolyte maker replicates. Lyten's sulfur sourcing for its cathode is similarly commodity-grade and broadly available.

**Cobalt:** Most documented companies eliminate cobalt entirely. Lyten (Li-S chemistry) and solid-state programs using Li metal anodes with non-NMC cathodes avoid cobalt by design. This is a strategically significant differentiation from conventional Li-ion, given DRC cobalt supply instability and DRC's 2025 export quota system. Cobalt price rose ~140% from its 2024 trough to ~$24/lb in December 2025. Major cobalt producers: CMOC (~31% global share), Glencore.

**Nickel:** Similarly, most solid-state programs use lithium metal anodes and do not require nickel-heavy NMC cathodes. Lyten eliminates nickel entirely. Factorial uses POSCO Future M for cathode/anode materials; POSCO Future M produces Ultra Hi-Ni single crystal cathodes, but Factorial's FEST® platform can accommodate different cathode chemistries. Indonesia controls ~40% of global nickel supply; Chinese operators control 70-75% of Indonesian processing capacity.

**Lithium Sulfide (Li₂S) — Critical Precursor:** Lithium sulfide is the key precursor for sulfide solid electrolytes used by Solid Power, QuantumScape, and Toyota/Idemitsu. Idemitsu is the only company in this knowledge base building dedicated large-scale Li₂S manufacturing capacity (1,000 MT/year by June 2027, serving ~50,000–60,000 EVs). This makes Idemitsu a potential upstream bottleneck for the broader sulfide solid electrolyte supply chain. **⚑ Shared supplier risk:** If QuantumScape, Solid Power, and Toyota's programs all scale simultaneously, Li₂S supply could become a chokepoint. Idemitsu's capacity is currently committed exclusively to Toyota.

**Ceramic Separators:** QuantumScape's ceramic separator (Cobra process) is a proprietary film — the company has partnered with [Murata Manufacturing](https://www.murata.com) for scale-up. Murata's ceramics precision manufacturing expertise (it is the world's leading ceramic capacitor maker) is being applied to separator production. This is the only documented third-party ceramic separator manufacturing partnership in the knowledge base.

**Cathode and Anode Materials:** [POSCO Future M]({{< relref "../resources/posco-future-m.md" >}}) (South Korea) is the documented cathode and anode material supplier for Factorial Energy (MOU signed December 2025) and a key supplier to GM, LG Energy Solution, Samsung SDI, and SK On. **⚑ Shared supplier:** POSCO Future M supplies materials to both Factorial Energy and Samsung SDI — and Samsung SDI is the cell manufacturer for Solid Power, creating a potential indirect supply chain connection between Factorial and Solid Power through POSCO Future M.

**Graphite (Conventional Anode):** Not directly relevant to solid-state or Li-S companies here (which use Li metal anodes or Li-S chemistry), but notable context: conventional graphite anodes are ~65%+ China-sourced. The documented companies' shift to lithium metal or sulfur cathodes largely sidesteps this risk.

### Supply Chain — Last Reviewed: 2026-03-23
