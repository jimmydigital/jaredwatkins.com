---
title: Robotics Connectors
date: 2026-07-14
lastmod: 2026-07-14
draft: false
description: Micro-miniature power and data connectors for drones and robots — Micro-D/Nano-D circular and rectangular interconnects, high-speed board-to-board systems, and battery quick-disconnects.
research_area: "robotics/connectors"
last_reviewed: 2026-07-14
stale_after_days: 180
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


## Overview

Micro-miniature connectors are the physical layer beneath every other robotics subsystem tracked in this knowledge base: they carry power to motors and batteries and data between flight controllers, sensors, and compute payloads, often in a package a few millimeters across. As drones and robots have shrunk and grown more sensor-dense, connector selection has become a first-order SWaP (size, weight, and power) constraint — every gram and cubic millimeter spent on a connector shell is a gram not spent on payload, flight time, or battery.

Two distinct connector worlds coexist in this space. The first is mil-spec/aerospace-grade precision connectors — Micro-D (MIL-DTL-83513), Nano-D, and proprietary rugged circular series like Fischer MiniMax, Nicomatic DMM/EMM, and ODU AMC — used in defense UAS, surgical robots, and high-reliability commercial platforms. Manufacturing for this tier is concentrated in the US and Western Europe (Minnesota, Missouri, France, Germany, Switzerland), largely because of ITAR/export-control requirements and the qualification testing (MIL-DTL-83513, MIL-STD-38999) that Chinese manufacturers have not broadly pursued. The second is the commodity battery quick-disconnect layer — XT60/XT90, AS150, and related bullet connectors — which is almost entirely designed and manufactured in China (Amass, of Changzhou, Jiangsu, being the dominant manufacturer) and supplies everything from hobbyist FPV drones to commercial platforms.

## Key Themes

- SWaP pressure is pushing connector density up and pitch down: Micro-D (1.27 mm / .050") and Nano-D (.64 mm / .025") pitches are standard; Fischer's MiniMax packs up to 24 signal/power contacts into a 12mm-diameter shell.
- Hybrid power+data connectors (combining high-current power pins with USB/Ethernet/CAN data pins in one shell) are becoming the default for UAV payload interfaces rather than separate power and data connectors.
- The mil-spec Micro-D/circular connector tier is one of the few robotics hardware layers *not* dominated by Chinese manufacturers — supply is concentrated in the US and EU due to ITAR and defense qualification requirements.
- By contrast, commodity drone battery connectors (XT/AS/Amass series) are almost entirely Chinese-designed and manufactured, supplying both hobbyist and commercial drone platforms.
- Consolidation: most of the historic independent US Micro-D/D-sub manufacturers are now divisions of larger conglomerates (Positronic → Amphenol 2021; Cinch → Bel Fuse 2010), leaving Omnetics as one of the few remaining independent US specialists.
- High-speed board-to-board connectors (Samtec Edge Rate, rated for 56 Gbps PAM4 mezzanine links) are increasingly the constraint on payload data throughput (LiDAR, high-res camera) rather than the radio link.
- Smart battery connectors that combine power delivery with BMS data communication (CAN/SMBus) are emerging to support autonomous battery-swap docking for BVLOS drone operations.

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Omnetics Connector Corp](https://www.omnetics.com) | Minneapolis, MN, USA | Private | Micro-D/Nano-D micro- and nano-miniature connectors with proprietary Flex-Pin beryllium copper contacts; QPL to MIL-DTL-83513/32139; one of the few remaining independent US Micro-D specialists. |
| [Fischer Connectors](https://fischerconnectors.com) (Conextivity Group) | Saint-Prex, Switzerland | Private (family-owned) | MiniMax/UltiMate hybrid circular connectors combining power and data in ultra-miniature shells (up to 24 contacts in ø12mm); widely used in UAV payload and LiDAR interfaces. |
| [Nicomatic](https://www.nicomatic.com) | Bons-en-Chablais, France | Private (family-owned) | DMM/CMM/EMM micro rugged connectors and FFC/CrimpFlex flat cables for UAV and defense electronics; up to 40% lighter than standard Micro-D; in-house manufacturing. |
| [Samtec](https://www.samtec.com) | New Albany, IN, USA | Private (family-owned) | High-speed micro rugged board-to-board connectors (Edge Rate ERF6/ERM6) for drone and robot mezzanine data links, up to 112 Gbps PAM4; also power and IP67/68 sealed micro interconnects. |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [APH](https://finance.yahoo.com/quote/APH) | [Amphenol](https://www.amphenol.com) | Owns Positronic (D-sub/Micro-D, acquired 2021) and a broad circular/rectangular connector portfolio for robotics and UAV; one of the largest interconnect makers in the world. |
| [BELFA / BELFB](https://finance.yahoo.com/quote/BELFA) | [Bel Fuse](https://www.belfuse.com) | Owns Cinch Connectivity Solutions (acquired from Safran 2010); Mil/Aero Circular MD801 lightweight ultraminiature connector series for UAVs and military avionics. |
| [APTV](https://finance.yahoo.com/quote/APTV) | [Aptiv](https://www.aptiv.com) | Owns Winchester Interconnect (acquired 2018); micro-miniature and RF/microwave connectors and cable assemblies for aerospace and industrial robotics. |
| [ETN](https://finance.yahoo.com/quote/ETN) | [Eaton](https://www.eaton.com) | Owns Souriau (harsh-environment circular connectors); MIL-DTL-38999-derived series used in UAV/UGV programs. |

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
        "title": "Connectors",
        "symbols": [
          {"s": "NYSE:APH", "d": "Amphenol"},
          {"s": "NASDAQ:BELFA", "d": "Bel Fuse"},
          {"s": "NYSE:APTV", "d": "Aptiv"},
          {"s": "NYSE:ETN", "d": "Eaton"}
        ],
        "originalTitle": "Connectors"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [TEL](https://finance.yahoo.com/quote/TEL) | [TE Connectivity](https://www.te.com) | Deutsch-brand micro and rectangular connectors for harsh-environment robotics; broad industrial/aerospace connector portfolio. |
| [Molex](https://www.molex.com) | Molex (private, Koch Industries subsidiary since 2018) | AirBorn M Series MIL-DTL-83513 Micro-D connectors and single-pair Industrial Ethernet connectors for humanoid robots. |
| [Glenair](https://www.glenair.com) | Glenair (private) | Mighty Mouse and Series 806 MIL-DTL-38999-derived micro circular connectors and PowerTrip power connectors for UAV/UGV. |
| [ODU](https://www.odu-usa.com) | ODU GmbH & Co. KG (private, Germany) | AMC blind-mate miniature high-speed connectors, down to 7mm shell diameter, IP68, for defense and medical robotics. |

## Supply Chain

### Supply Chain Layers

| Layer | Key Inputs / Outputs | Companies Operating Here | Geographic Risk |
|-------|---------------------|--------------------------|-----------------|
| **1. Raw Materials** | Beryllium copper alloy (contact springs, e.g. C17510/C17200), gold (plating), high-performance engineering plastics (LCP, PEEK, PPS) for insulators, aluminum/stainless steel for shells | [Materion](https://www.materion.com) (US, beryllium copper, formerly Brush Wellman), [Busby Metals/Wieland](https://busbymetals.com) (US/UK/France/China distribution), Solvay/Celanese (LCP resin) | Beryllium copper alloy production concentrated in the US (Materion); beryllium itself is a US-mined critical mineral with limited global sourcing |
| **2. Contacts & Plating** | Precision-stamped or machined pin/socket contacts, nickel-and-gold plating for low contact resistance | Omnetics (proprietary Flex-Pin), Positronic (machined contacts) | Precision machining/stamping capacity distributed across US and EU manufacturing sites |
| **3. Mil-Spec Micro/Nano-D & Circular Connectors** | Complete Micro-D (MIL-DTL-83513), Nano-D, and rugged circular connector assemblies | [Omnetics](https://www.omnetics.com), [Positronic/Amphenol](https://www.connectpositronic.com), [Cinch/Bel Fuse](https://www.cinch.com) (MD801), [Nicomatic](https://www.nicomatic.com), [ODU](https://www.odu-usa.com), [Fischer Connectors](https://fischerconnectors.com), [Glenair](https://www.glenair.com), [Souriau/Eaton](https://www.souriau.com) | Manufacturing concentrated in US (Minnesota, Missouri, Illinois) and Western Europe (France, Germany, Switzerland) due to ITAR and defense qualification requirements — a notable exception to the China-dominated pattern elsewhere in robotics hardware |
| **4. High-Speed / Board-to-Board** | Rugged micro board-to-board mezzanine connectors, e.g. 56 Gbps PAM4-rated Edge Rate ERF6/ERM6 | [Samtec](https://www.samtec.com), [TE Connectivity](https://www.te.com), [Molex](https://www.molex.com) | US-headquartered design; contract manufacturing distributed globally |
| **5. Battery / Power Quick-Disconnect** | XT/AS/EC-series bullet connectors, Molex balance-lead connectors, smart-battery power+data connectors (e.g. PDC1810F0002) | [Amass](https://www.china-amass.net) 🇨🇳, Power Data Connectors (PDC1810F0002 smart battery connector; official site not findable — see TODO) | Commodity battery connector layer (XT60/XT90/AS150) almost entirely designed and manufactured in China; Amass is the originating manufacturer and supplies DJI, Parrot, and Ninebot directly |
| **6. Cable Assembly & Integration** | Connector-to-cable termination, robot/drone OEM final integration | [Winchester Interconnect/Aptiv](https://www.winconn.com), [PEI-Genesis](https://www.peigenesis.com) (distributor/value-add assembler), robot and drone OEMs | Assembly distributed across US, Mexico, and Asia depending on program/ITAR requirements |

### Key Supply Chain Notes

**⚑ Shared supplier — beryllium copper contacts:** Omnetics, Positronic, and most other Micro-D/mil-spec connector makers rely on beryllium copper alloy (typically C17200 or C17510) for spring contacts, sourced predominantly from Materion (the former Brush Wellman), a US-concentrated supply chain for a critical mineral (beryllium) with few alternative global sources.

**Mil-spec connector tier is a US/EU-concentrated exception:** Unlike LiDAR, cellular modules, and batteries elsewhere in this robotics knowledge base — all Chinese-dominated — the Micro-D/Nano-D/mil-spec circular connector tier is manufactured almost entirely in the US and Western Europe. ITAR export controls and MIL-DTL-83513/MIL-STD-38999 qualification testing create a high barrier that Chinese manufacturers have not broadly entered, making this one of the few robotics hardware layers where Western supply is structurally secure.

**⚑ Shared supplier — Amass:** Amass (Changzhou, Jiangsu, China) manufactures the XT and AS connector families used across the broader hobbyist/FPV and commercial drone battery market; the company's own site lists "Intelligent robots" and "Model aircraft drone" as named solution areas. This is the drone-industry mirror image of the mil-spec layer above: a single Chinese manufacturer effectively sets the de facto standard for commercial and consumer drone battery interconnects. See [Drone Battery Power Connectors]({{< relref "drone-battery-power-connectors.md" >}}) for connector-family detail; specific named OEM customer claims are unverified.

**Consolidation of independent US Micro-D makers:** Positronic (founded 1966) was acquired by Amphenol in 2021; Cinch Connectors (maker of the MD801 series) was acquired by Bel Fuse from Safran in 2010. Omnetics remains one of the few Micro-D/Nano-D specialists still independently and privately held.

**Smart battery connectors for autonomous operations:** The PDC1810F0002 connector (Power Data Connectors) combines high-current power pins with CAN/SMBus data pins in a compact plug-and-play shell, designed for autonomous docking and battery-swap drone operations — a small but growing niche as BVLOS commercial drone operations scale. <!-- TODO: verify official Power Data Connectors (PDC) company website; not findable via search as of 2026-07-14 -->

### Supply Chain — Last Reviewed: 2026-07-14
