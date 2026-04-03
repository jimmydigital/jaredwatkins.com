---
title: Robotics Power Systems
date: 2026-03-24
lastmod: 2026-03-24
draft: false
description: Batteries, fuel cells, hybrid power, and wireless charging for robots — manufacturers, chemistry trends, and supply chain overlap with EV and grid storage.
tags: ["robotics", "battery", "fuel-cell"]
categories: ["overview"]
research_area: "robotics/power-systems"
last_reviewed: 2026-03-24
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---

## Overview

Robot power systems are a derivative market: almost all robotics battery cells are sourced from the same manufacturers supplying EVs and grid storage (Samsung SDI, LG Energy Solution, CATL, BYD, Panasonic/Murata), with robotics-specific value added at the pack integration and BMS layer. The exception is LiPo cells for drones, where Grepow/Tattu has developed a focused OEM position. The more differentiated opportunities are in hydrogen fuel cells (Intelligent Energy, Doosan Mobility Innovation are genuine robotics specialists), wireless charging infrastructure (Wiferion, WiBotic), and the emerging opportunity in solid-state cells that could transform drone endurance if they reach commercial production. The supply chain overlaps substantially with the energy section — see `energy/batteries` for raw materials and cell-level detail.

## Key Themes

- Cell supply almost entirely shared with EV/grid storage: CATL, BYD, Samsung SDI, LGES, Panasonic/Murata
- Grepow/Tattu: the only significant drone-specific LiPo OEM manufacturer by volume
- LFP chemistry gaining ground in AMRs for cycle life and safety advantages despite lower energy density
- Hydrogen fuel cells: Intelligent Energy and Doosan DMI are the two most commercially advanced players for drone endurance extension
- Wireless opportunity charging (Wiferion, WiBotic) enabling continuous AMR operation without scheduled downtime
- Solid-state cells: if Toyota/QuantumScape timelines hold (2027–2028), drone endurance could double — worth tracking for robotics implications
- Raw material overlaps: identical lithium, cobalt, nickel, graphite supply chain as EV and grid storage

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Intelligent Energy](https://www.intelligent-energy.com) | Loughborough, UK | Late Private | Hydrogen PEM fuel cell modules for drones and ground robots; 650W and 2.4kW modules; most commercially active fuel cell supplier targeting drone endurance. |
| [Doosan Mobility Innovation](https://www.doosanmobility.com) | Seoul, South Korea | Private (Doosan Group subsidiary) | DS30 hydrogen fuel cell drone platform; 2+ hour endurance; one of the most commercially advanced hydrogen drone products globally. |
| [HES Energy Systems](https://hes.sg) | Singapore | Growth | Aeropak hydrogen fuel cell series for professional drones; commercial deployments in Asia and Europe. |
| [WiBotic](https://wibotic.com) | Seattle, WA, USA | Growth (acquired by Vertiv) | Wireless charging systems for aerial and ground robots; OC-110 drone charging dock; TR-110 ground robot charging; Boston Dynamics Spot integration. |
| [Wiferion](https://wiferion.com) | Freiburg, Germany | Growth (Würth Elektronik subsidiary) | etaLINK inductive floor-embedded charging pads for AMRs; 3.6 kW per pad; commercial deployments in European automotive and logistics facilities. |
| [Flux Power Holdings](https://www.fluxpwr.com) | Vista, CA, USA | Public (NASDAQ: FLUX) | LFP-based battery packs for industrial lift equipment and AMRs; US-made packs; growing AMR customer base. |
| [Skeleton Technologies](https://www.skeletontech.com) | Tallinn, Estonia | Series D | Curved graphene ultracapacitors (higher energy density than conventional EDLCs); rail, grid, defense, and robotics buffer storage. |
| [Grepow / Tattu](https://www.grepow.com) 🇨🇳 | Shenzhen, China | Private | Dominant OEM LiPo cell and pack manufacturer for drones; Tattu retail brand; custom-shaped cells for OEM drone makers. |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [FLUX](https://finance.yahoo.com/quote/FLUX) | [Flux Power Holdings](https://www.fluxpwr.com) | LFP battery packs for industrial lift equipment, AMRs; US-manufactured; pure-play robotics/industrial battery company. |
| [BLDP](https://finance.yahoo.com/quote/BLDP) | [Ballard Power Systems](https://www.ballard.com) | Canadian hydrogen PEM fuel cell maker; heavy transport focus (buses, trucks, trains); demonstration programs in UAS and UGV. |
| [PLUG](https://finance.yahoo.com/quote/PLUG) | [Plug Power](https://www.plugpower.com) | Hydrogen fuel cell systems for forklifts and logistics vehicles; building hydrogen infrastructure in warehouses — directly relevant to hydrogen AMR pathway. |
| [ULBI](https://finance.yahoo.com/quote/ULBI) | [Ultralife Corporation](https://www.ultralifecorp.com) | Military and commercial lithium battery systems; BA-5590 compatible and rechargeable packs; defense robot battery supplier. |

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
        "title": "Power Systems",
        "symbols": [
          {"s": "NASDAQ:FLUX", "d": "Flux Power"},
          {"s": "NASDAQ:BLDP", "d": "Ballard Power"},
          {"s": "NASDAQ:PLUG", "d": "Plug Power"},
          {"s": "NASDAQ:ULBI", "d": "Ultralife"}
        ],
        "originalTitle": "Power Systems"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [300750.SZ](https://finance.yahoo.com/quote/300750.SZ) | [CATL](https://www.catl.com/en/) 🇨🇳 | World's largest battery cell maker; LFP and NMC cells used in robotics packs; exploring humanoid robot battery supply; supply discussions with Tesla Optimus supply chain. |
| [006400.KS](https://finance.yahoo.com/quote/006400.KS) | [Samsung SDI](https://www.samsungsdi.com) | 18650 and 21700 NMC cylindrical cells widely used in AMR packs; also prismatic cells; solid-state development (PRiMX). |
| [373220.KS](https://finance.yahoo.com/quote/373220.KS) | [LG Energy Solution](https://www.lgesolution.com) | Pouch and cylindrical NMC cells; AMR battery pack integrators widely use LGES cells. |
| [6981.T](https://finance.yahoo.com/quote/6981.T) | [Murata Manufacturing](https://www.murata.com) | Acquired Sony battery business 2017; continues Sony VTC and Fortelion cylindrical cells; high-drain cells used in drones and robots. |
| [ETN](https://finance.yahoo.com/quote/ETN) | [Eaton](https://www.eaton.com) | Ultracapacitor distribution (Bussmann division) and power electronics for industrial and robotic applications. |

## Supply Chain

The robotics power system supply chain shares raw material inputs almost entirely with the EV and grid storage sectors documented in `content/research/energy/batteries`. The divergence occurs at the form factor, BMS specification, and application requirements. This section focuses on the robotics-specific differentiation; see `energy/batteries/_index.md` for the full raw materials and cell-level supply chain.

### Supply Chain Layers

| Layer | Key Inputs / Outputs | Companies Operating Here | Geographic Risk |
|-------|---------------------|--------------------------|-----------------|
| **1. Raw Materials** | Lithium, cobalt, nickel, manganese, graphite, phosphate (LFP), iron | Albemarle (ALB, lithium), SQM (lithium), Glencore (cobalt), Vale/BHP/Norilsk (nickel), Syrah/BTR (graphite) | See `energy/batteries` for detail; same supply chain as EV and grid |
| **2. Cells** | LiPo pouch cells (drones), 18650/21700 NMC cylindrical, LFP prismatic, primary lithium (long-life sensors) | [CATL](https://www.catl.com) 🇨🇳, [BYD](https://www.byd.com) 🇨🇳, Samsung SDI, LG Energy Solution, Panasonic/Murata, [Grepow](https://www.grepow.com) 🇨🇳 (LiPo OEM) | Cell production: South Korea (Samsung, LGES), Japan (Panasonic, Murata), China (CATL, BYD, Grepow) |
| **3. BMS Electronics** | Cell monitoring ICs, balancing circuits, thermal management, protection electronics | Texas Instruments (BMS ICs), Analog Devices (BMS ICs), Renesas | BMS IC design: US-dominant (TI, ADI); IC manufacturing: TSMC/Taiwan |
| **4. Battery Pack Assembly** | Configured packs with BMS, thermal management, connectors, enclosures | [Inventus Power](https://www.inventuspower.com) (US), [EaglePicher](https://www.eaglepicher.com) (US, defense), [Flux Power](https://www.fluxpwr.com) (US, industrial), [Bren-Tronics](https://www.bren-tronics.com) (US, defense), [Grepow/Tattu](https://www.grepow.com) 🇨🇳 (drone LiPo packs) | Pack assembly: US for defense/regulated; Chinese for commercial drones |
| **5. Fuel Cell Modules** | PEM hydrogen fuel cell stacks and integrated power modules | [Intelligent Energy](https://www.intelligent-energy.com) (UK), [Doosan DMI](https://www.doosanmobility.com) (Korea), [HES](https://hes.sg) (Singapore), Ballard (Canada) | Fuel cell development: UK, Korea, Canada, Singapore — no single geographic concentration |
| **6. Hydrogen Storage** | Compressed H₂ tanks (700 bar), carbon fiber overwrapped pressure vessels | [Luxfer Holdings](https://www.luxfergascontainers.com) (UK/US, LXFR), [Hexagon Purus](https://hexagonpurus.com) (Norway), Faber Industries (Italy) | Carbon fiber overwrapped pressure vessels: distributed production; CF fiber itself: Toray (Japan) dominant |
| **7. Wireless Charging Systems** | Inductive charging pads, receiver coils, power electronics | [Wiferion](https://wiferion.com) (Germany), [WiBotic](https://wibotic.com) (US) | Emerging segment; currently German and US suppliers only |
| **8. Integration** | Robot-mounted battery, fuel cell, or charging system | Robot OEMs (Boston Dynamics, MiR, etc.); specialty integrators | — |

### Key Supply Chain Notes

**Raw material overlap with EV and grid storage:** The lithium, cobalt, nickel, and graphite supply chains for robotics batteries are identical to those for EV batteries and grid-scale storage. Robotics does not have a separate raw material supply chain — it is a demand contributor to the same constrained resources. During EV ramp cycles, robotics battery pack makers face competition for cells from EV OEMs with larger purchasing power. This is a real procurement risk for robotics companies during periods of cell shortage (as seen in 2021–2022).

**⚑ Shared supplier — CATL:** CATL supplies cells to Tesla (automotive), BYD (captive), SAIC, BMW, and is in supply discussions for humanoid robot battery systems. It also produces the LFP cells increasingly specified into warehouse AMRs. CATL's dominant position means that any CATL supply disruption, Chinese government export restriction, or US-China trade action on battery cells would simultaneously affect EV, grid storage, and robotics battery supply.

**⚑ Shared supplier — Samsung SDI:** Samsung SDI supplies 18650 and 21700 cells to AMR pack integrators, EV OEMs (Stellantis, BMW, Rivian), and is integrating Solid Power's solid-state electrolyte into its next-generation cells. It is therefore a shared supplier between the robotics battery pack assembly layer and the advanced battery development layer documented in `energy/batteries`.

**Hydrogen infrastructure overlap with logistics:** Plug Power has deployed hydrogen fueling infrastructure in tens of thousands of forklifts at Amazon, Walmart, and Home Depot distribution centers. This infrastructure — hydrogen storage tanks, dispensers, electrolyzer systems — is directly applicable to hydrogen-powered AMR deployments. The warehouse hydrogen infrastructure being built for forklifts is the likely enabler for hydrogen AMRs in logistics environments. Track Plug Power's logistics facility deployments as a leading indicator of hydrogen AMR feasibility.

**Solid-state cells and drone endurance:** If Toyota and QuantumScape achieve commercial solid-state cell production in 2027–2028, the implications for drone endurance are significant. A 50% improvement in gravimetric energy density (from ~250 Wh/kg LiPo to ~375 Wh/kg solid-state at pack level) would extend a 30-minute commercial drone mission to approximately 45 minutes — or allow the same mission with a materially heavier payload. Track the automotive solid-state timelines in `energy/batteries` as the lead indicator for when this technology will reach the drone market. Drone applications are likely to receive solid-state cells 2–4 years after automotive qualification due to the OEM development cycle.

**Grepow/Tattu market position:** Grepow is the most commercially significant drone-specific battery manufacturer globally. Its LiPo packs and custom-shaped cells are specified into DJI competitors, agricultural drones, inspection drones, and numerous startup UAS platforms. Despite Chinese ownership, its technical position is genuinely strong — no equivalent Western LiPo OEM manufacturer exists at comparable scale. US-domestic LiPo pack manufacturing is a gap in the supply chain with national security implications for DoD UAS procurement.

### Supply Chain — Last Reviewed: 2026-03-24
