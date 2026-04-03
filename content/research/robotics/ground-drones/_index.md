---
title: Ground Drones & UGVs
date: 2026-03-24
lastmod: 2026-03-24
draft: false
description: Autonomous mobile robots, unmanned ground vehicles, and field robots — warehouse AMRs, outdoor platforms, and defense UGVs.
tags: ["robotics", "ugv", "amr"]
categories: ["overview"]
research_area: "robotics/ground-drones"
last_reviewed: 2026-03-24
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---

## Overview

The ground robot market splits into three commercially distinct segments that share some technology but operate in largely separate competitive environments: warehouse and logistics AMRs (autonomous mobile robots), outdoor and field robots (agricultural, delivery, security, construction), and defense UGVs. The AMR segment is the largest by deployed units and revenue, is growing rapidly, and is heavily contested between Western companies and Chinese manufacturers — particularly Geek+ — that compete primarily on price and deployment scale. The defense segment is smaller but carries higher margins and longer contract durations.

## Key Themes

- Chinese AMR manufacturers (Geek+, Hai Robotics, Quicktron) dominating global volume with aggressive pricing
- Teradyne as the dominant US public company with exposure across mobile robotics (MiR) and collaborative robot arms (Universal Robots)
- Boston Dynamics (Hyundai-owned) high profile but modest revenue — still early commercial traction
- Defense UGV programs (RCV, CRS-I, MTRS) as the funded leading edge of UGV technology
- Sidewalk delivery robots at early commercial scale (Starship, Serve Robotics) — regulatory environment as key gating factor
- Quadrupedal robots (Spot, Ghost Vision 60) finding real deployments in inspection and perimeter security

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Locus Robotics](https://locusrobotics.com) | Wilmington, MA, USA | Late Private (Series F) | Collaborative AMRs for fulfillment warehouses; works alongside human pickers; DHL, Quiet Logistics customers. |
| [Vecna Robotics](https://vecnarobotics.com) | Waltham, MA, USA | Growth | Autonomous tuggers, forklifts, and pallet movers; industrial facilities focus. |
| [Seegrid](https://seegrid.com) | Pittsburgh, PA, USA | Late Private | Vision-guided autonomous industrial vehicles (tuggers, pallet movers); no floor markers required. |
| [Ghost Robotics](https://www.ghostrobotics.io) | Philadelphia, PA, USA | Late Private | Q-UGV and Vision 60 quadruped platforms; USAF Tyndall AFB perimeter security deployment; adversarial environment design philosophy. |
| [Zipline](https://flyzipline.com) | South San Francisco, CA, USA | Late Private | Ground-adjacent delivery ecosystem; P2 Zip drone + logistics infrastructure. |
| [Starship Technologies](https://www.starship.xyz) | Tallinn, Estonia | Late Private | Sidewalk delivery robots; >7M deliveries as of 2024; 2,000+ fleet globally; university campus focus. |
| [Serve Robotics](https://www.serverobotics.com) | Redwood City, CA, USA | Public (NASDAQ: SERV) | Sidewalk delivery robots; LA operations via Uber Eats partnership; spun out from Uber 2021. |
| [Nuro](https://www.nuro.ai) | Mountain View, CA, USA | Late Private ($2B+ raised) | Road-going autonomous delivery vehicle; first NHTSA special permit for a vehicle without human controls. |
| [Monarch Tractor](https://www.monarchtractor.com) | Livermore, CA, USA | Series B | Electric autonomous tractor for specialty crops (vineyards, orchards); farmer-in-the-loop autonomy. |
| [Carbon Robotics](https://carbonrobotics.com) | Seattle, WA, USA | Series C | LaserWeeder — CO2 laser-based autonomous weed elimination; no herbicides; targets organic and conventional growers. |
| [Built Robotics](https://www.builtrobotics.com) | San Francisco, CA, USA | Series B | Autonomous guidance retrofit for heavy construction equipment (excavators, graders); GPS-guided earthmoving. |
| [Knightscope](https://www.knightscope.com) | Mountain View, CA, USA | Public (NASDAQ: KSCP) | Autonomous security robots (K1, K3, K5); RaaS model; cameras, ALPR, thermal sensors; >50 deployments. |
| [Milrem Robotics](https://milremrobotics.com) | Tallinn, Estonia | Private (EDGE Group majority) | THeMIS tracked UGV; widely deployed in NATO countries; Mission Master light combat variant. |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [TER](https://finance.yahoo.com/quote/TER) | [Teradyne](https://www.teradyne.com) | Semiconductor test equipment parent; owns MiR (AMR) and Universal Robots (cobots) — most significant public company with dedicated robotics revenue. |
| [SERV](https://finance.yahoo.com/quote/SERV) | [Serve Robotics](https://www.serverobotics.com) | Sidewalk delivery robot operator; NASDAQ-listed pure-play. |
| [KSCP](https://finance.yahoo.com/quote/KSCP) | [Knightscope](https://www.knightscope.com) | Autonomous security robot operator; RaaS model. |

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
        "title": "Ground Drones",
        "symbols": [
          {"s": "NASDAQ:TER", "d": "Teradyne"},
          {"s": "NASDAQ:SERV", "d": "Serve Robotics"},
          {"s": "NASDAQ:KSCP", "d": "Knightscope"}
        ],
        "originalTitle": "Ground Drones"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [Geek+](https://www.geekplus.com) 🇨🇳 | Geek+ (private, ~$2B valuation) | Largest AMR company globally by deployed units; goods-to-person, sorting, and heavy-load platforms; aggressive international expansion. |
| [HD](https://finance.yahoo.com/quote/HD) | [Boston Dynamics](https://www.bostondynamics.com) (Hyundai subsidiary) | Spot quadruped and Stretch logistics robot; acquired by Hyundai Motor Group 2021 for ~$1.1B; highest-profile robotics brand globally; commercial revenue still modest. |
| [DE](https://finance.yahoo.com/quote/DE) | [John Deere](https://www.deere.com) | Autonomous tractor (8R), See & Spray precision herbicide, autonomous tillage; acquired Blue River Technology 2017 ($305M); largest deployed base of autonomous agricultural machines. |
| [ZBRA](https://finance.yahoo.com/quote/ZBRA) | [Zebra Technologies](https://www.zebra.com) | Acquired Fetch Robotics 2021 ($290M); integrates AMRs with enterprise RFID and workflow management. |
| [TXT](https://finance.yahoo.com/quote/TXT) | [Textron Systems](https://www.textronsystems.com) | RIPSAW M5 unmanned tank; Common Robotic System – Individual (CRS-I); long-standing Army UGV programs. |
| [QQ.L](https://finance.yahoo.com/quote/QQ.L) | [QinetiQ](https://www.qinetiq.com) (parent) | Owns Endeavor Robotics (PackBot, Kobra); acquired from iRobot 2019 for $400M; primary US Army small robot supplier. |

## Supply Chain

### Supply Chain Layers

| Layer | Key Inputs / Outputs | Companies Operating Here | Geographic Risk |
|-------|---------------------|--------------------------|-----------------|
| **1. Raw Materials** | Neodymium (motors), lithium/cobalt/nickel (batteries), aluminum/steel (frames), silicon (compute/sensors) | Lynas Rare Earths (Australia), MP Materials (US), Albemarle (lithium), Glencore (cobalt) | NdFeB magnets: China ~90% processing; lithium: Australia/Chile/Argentina; cobalt: DRC ~75% |
| **2. Precision Components** | NdFeB magnets, precision bearings, encoder discs, carbon fiber structural panels | NSK (Japan, bearings), SKF (Sweden, bearings), Renishaw (UK, encoders), Hexcel (US, carbon fiber) | Bearing precision manufacturing: Japan and Sweden dominant |
| **3. Motors & Drive Systems** | BLDC hub motors, servo motors, gearboxes (harmonic drive, cycloidal), wheel drive assemblies | [Maxon Motor](https://www.maxongroup.com) (Swiss), [Faulhaber](https://www.faulhaber.com) (German), [Nabtesco](https://www.nabtesco.com) (Japan, cycloidal), [Harmonic Drive](https://www.harmonicdrive.net) (Japan/US), [Parker Hannifin](https://www.parker.com) (US, hydraulics), [Festo](https://www.festo.com) (German, pneumatics) | Precision servo gearboxes: Japan-dominated (Nabtesco, Harmonic Drive); motors: Switzerland and Germany for precision, China for volume |
| **4. Sensor & Compute Modules** | LiDAR, radar, cameras, depth sensors, compute boards | [Ouster](https://ouster.com) (US), [Luminar](https://luminartech.com) (US), [Hesai](https://www.hesaitech.com) 🇨🇳, [RoboSense](https://www.robosense.ai) 🇨🇳, [Stereolabs](https://www.stereolabs.com) (French), NVIDIA (Jetson), Intel (RealSense, withdrawing) | LiDAR: China (Hesai, RoboSense) taking volume share from US; radar: automotive-derived (Bosch, Continental) |
| **5. Communications Subsystems** | WiFi 6/6E modules, 4G/5G cellular modules, MANET radios, private LTE | [Quectel](https://www.quectel.com) 🇨🇳 (cellular modules), [Cradlepoint/Ericsson](https://cradlepoint.com) (private LTE), [Silvus](https://silvustechnologies.com) (defense MANET), [Persistent Systems](https://www.persistentsystems.com) (defense mesh) | IoT cellular modules: Quectel (Chinese) dominant globally by volume |
| **6. Power Subsystems** | 24–96V lithium-ion packs (NMC/LFP), BMS, opportunity charging hardware | [Flux Power](https://www.fluxpwr.com) (US, LFP), [Inventus Power](https://www.inventuspower.com) (US), [EaglePicher](https://www.eaglepicher.com) (US, defense), [Wiferion](https://wiferion.com) (German, wireless charging), [WiBotic](https://wibotic.com) (US, wireless charging) | LFP cells: CATL and BYD dominant; NMC cells: Samsung SDI, LGES |
| **7. Platform Integration** | Complete robot system, navigation software, fleet management | Boston Dynamics, Teradyne/MiR, Geek+ 🇨🇳, Ghost Robotics, Textron Systems, QinetiQ/Endeavor | Platform assembly geography varies; software/AI integration increasingly in US and Europe |

### Key Supply Chain Notes

**⚑ Shared supplier — Maxon Motor:** Maxon is a critical precision motor supplier to Boston Dynamics, multiple surgical robot makers, and defense UGV programs simultaneously. A Maxon supply disruption (single factory in Sachseln, Switzerland, plus Sexau, Germany) would affect multiple premium robotics programs at once.

**⚑ Shared supplier — Nabtesco cycloidal gearboxes:** Nabtesco holds a dominant position in cycloidal speed reducers (RV series) used in industrial robot joints. The same gearbox family specified into factory robot arms (FANUC, Yaskawa) is used in premium UGV joint designs. Production capacity constraints at Nabtesco are a recurring bottleneck during robot industry upcycles.

**Harmonic Drive vs. Nabtesco:** These two Japanese companies together supply the precision gearboxes that define the performance ceiling of robotic joint design. Harmonic Drive (strain wave) excels at high precision in compact form; Nabtesco cycloidal excels at high stiffness and shock resistance. Boston Dynamics' Spot uses both in different joints. Both are Japanese, privately or publicly held in Japan — limited US alternative supply.

**Chinese AMR pricing pressure:** Geek+, Hai Robotics, and Quicktron offer AMR platforms at 30–50% lower prices than Western competitors (MiR, Locus, Seegrid). This is a structural threat to US/European AMR companies that cannot easily compete on cost without moving manufacturing to China — which introduces the very data security concerns that differentiate them in sensitive facilities.

### Supply Chain — Last Reviewed: 2026-03-24
