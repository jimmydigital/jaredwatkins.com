---
title: Robotics Communications
date: 2026-03-24
lastmod: 2026-03-24
draft: false
description: Wireless communications subsystems for drones and ground robots — radio modules, cellular modems, mesh networking, and spectrum management.
tags: ["robotics", "communications"]
categories: ["overview"]
research_area: "robotics/communications"
last_reviewed: 2026-03-24
stale_after_days: 180
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


## Overview

Communications is a layer where robotics splits sharply along use-case lines. Consumer and commercial drones use proprietary protocols or commodity ISM-band radios. Industrial AMRs rely on enterprise WiFi. Outdoor field robots are increasingly cellular-connected. Defense platforms demand encrypted, low-probability-of-intercept/detect (LPI/LPD) MANET radios that are tightly controlled and US-export restricted. The cellular IoT module layer is particularly notable: Quectel, a Chinese company, has captured an estimated 30–35% of the global cellular module market, creating a systemic dependency that is now drawing scrutiny from Western governments and enterprises concerned about data security in connected robots.

## Key Themes

- Quectel (Chinese) dominance in cellular IoT modules — a supply chain security concern for enterprise and defense robot operators
- 5G BVLOS: cellular connectivity as the regulatory unlock for beyond-visual-line-of-sight drone operations
- Private LTE / CBRS deployments in warehouses enabling deterministic connectivity for dense AMR fleets
- Defense-grade MANET radios (Silvus, Persistent Systems, TrellisWare) as a small but strategically important US-controlled segment
- DJI's proprietary OcuSync/O3 protocols: performance benchmark that open-standard alternatives haven't matched
- Spectrum regulation (FCC, ITU) as a key variable — frequency allocations differ by country and constrain operational design

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Silvus Technologies](https://silvustechnologies.com) | Los Angeles, CA, USA | Private | StreamCaster MIMO mesh radios; software-defined, FHSS waveform; widely deployed in DoD UAS and UGV programs; no direct commercial equivalent. |
| [Persistent Systems](https://www.persistentsystems.com) | New York, NY, USA | Private | MPU5 Wave Relay MANET radio; enables multi-hop mesh networking across ground/air mixed teams; deployed on numerous Army and Marine programs. |
| [Celona](https://www.celona.io) | Campbell, CA, USA | Series C | Enterprise private 5G / CBRS solutions for industrial facilities; relevant for warehouse AMR connectivity infrastructure. |
| [RFDesign](https://rfdesign.com.au) | Brisbane, Australia | Growth | RFD900 telemetry radio series for drones; 900 MHz, long-range, used extensively in defense and research UAS. |
| [Doodle Labs](https://doodlelabs.com) | Singapore / USA | Growth | Mesh Rider radio family; 900 MHz and dual-band mesh networking for robots and UAS; used in defense and public safety. |
| [TrellisWare Technologies](https://www.trellisware.com) | San Diego, CA, USA | Private (Kratos subsidiary) | TSM waveform for Army tactical communications; contested RF environment performance. |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [SMTC](https://finance.yahoo.com/quote/SMTC) | [Semtech](https://www.semtech.com) | Acquired Sierra Wireless (2023); LoRa IoT radio technology + Sierra's LTE/5G cellular module business; broad IoT and robotics connectivity exposure. |
| [VSAT](https://finance.yahoo.com/quote/VSAT) | [Viasat](https://www.viasat.com) | Satellite communications; SATCOM datalinks for long-range UAS and maritime robots; DoD SATCOM contracts. |
| [LHX](https://finance.yahoo.com/quote/LHX) | [L3Harris](https://www.l3harris.com) | Defense electronics prime; encrypted tactical radios, datalinks, and SATCOM for defense UAS and UGV programs. |
| [KTOS](https://finance.yahoo.com/quote/KTOS) | [Kratos Defense](https://www.kratosdefense.com) | Owns TrellisWare; also makes tactical drones (UTAP-22 Mako, XQ-58 Valkyrie); defense comms and unmanned systems. |

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
        "title": "Communications",
        "symbols": [
          {"s": "NASDAQ:SMTC", "d": "Semtech"},
          {"s": "NASDAQ:VSAT", "d": "Viasat"},
          {"s": "NYSE:LHX", "d": "L3Harris"},
          {"s": "NASDAQ:KTOS", "d": "Kratos Defense"}
        ],
        "originalTitle": "Communications"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [Quectel](https://www.quectel.com) 🇨🇳 | Quectel Wireless Solutions (private, Chinese) | World's largest cellular IoT module supplier by volume (~30–35% global market); LTE Cat-1 through 5G NR modules embedded in AMRs, delivery robots, and commercial drones globally. |
| [UBXN.SW](https://finance.yahoo.com/quote/UBXN.SW) | [u-blox](https://www.u-blox.com) | Expanded from GNSS into cellular modules (SARA, LARA, LEXI series); Swiss-owned alternative to Quectel. |
| [TLIT.L](https://finance.yahoo.com/quote/TLIT.L) | [Telit Cinterion](https://www.telit.com) | UK-listed cellular module maker (merged with Thales/Cinterion); LTE and 5G modules for industrial IoT and robotics. |
| [ERIC](https://finance.yahoo.com/quote/ERIC) | [Ericsson / Cradlepoint](https://cradlepoint.com) | Cradlepoint (Ericsson subsidiary since 2020); enterprise private LTE and 5G routers for industrial AMR deployments. |
| [QCOM](https://finance.yahoo.com/quote/QCOM) | [Qualcomm](https://www.qualcomm.com) | Snapdragon Flight platform integrates LTE/5G with drone compute; cellular modems in connected robots; RB5 robotics platform. |

## Supply Chain

### Supply Chain Layers

| Layer | Key Inputs / Outputs | Companies Operating Here | Geographic Risk |
|-------|---------------------|--------------------------|-----------------|
| **1. Raw Materials** | Silicon (RF chips), gallium arsenide/gallium nitride (power amplifiers), PCB substrates, antenna materials | TSMC (Taiwan, RF SoC foundry), WIN Semiconductors (Taiwan, GaAs PA), Murata (Japan, ceramic RF components) | GaAs/GaN PA foundry: Taiwan-concentrated; ceramic RF components: Japan-dominated |
| **2. RF Semiconductors** | Transceiver ICs, power amplifiers, front-end modules, baseband processors | Qualcomm (US, cellular baseband), Skyworks (US, RF front-end), Qorvo (US, GaN PA), MediaTek (Taiwan, cellular), Nordic Semiconductor (Norway, Bluetooth/BLE) | RF front-end: Skyworks and Qorvo (US) dominant; cellular baseband: Qualcomm and MediaTek |
| **3. Radio / Modem Modules** | Complete cellular modems, WiFi modules, LoRa modules, satellite modem modules | [Quectel](https://www.quectel.com) 🇨🇳, [Telit Cinterion](https://www.telit.com), [u-blox](https://www.u-blox.com), [Sierra Wireless/Semtech](https://www.sierrawireless.com), [Fibocom](https://www.fibocom.com) 🇨🇳 | Cellular module assembly: Chinese manufacturers (Quectel, Fibocom) dominate by volume |
| **4. Integrated Radio Systems** | Complete mesh radio units, encrypted MANET radios, custom waveform radios | [Silvus Technologies](https://silvustechnologies.com), [Persistent Systems](https://www.persistentsystems.com), [TrellisWare/Kratos](https://www.trellisware.com), [Doodle Labs](https://doodlelabs.com) | Defense MANET radios: US-controlled and ITAR-restricted; commercial mesh: globally distributed |
| **5. Network Infrastructure** | Private LTE base stations, CBRS spectrum access system, enterprise WiFi APs | [Cradlepoint/Ericsson](https://cradlepoint.com), [Celona](https://www.celona.io), [Cisco](https://www.cisco.com), [Extreme Networks](https://www.extremenetworks.com) | Network infrastructure: US and European vendors; manufacturing in Asia |
| **6. Integration into Robot Platforms** | Radio module embedded in robot controller board; antenna integration | Robot OEMs, PCB contract manufacturers | PCB assembly: China, Taiwan, Southeast Asia dominant |

### Key Supply Chain Notes

**⚑ Shared supplier — Quectel:** Quectel's cellular modules appear in Starship delivery robots, numerous AMR platforms, agricultural robots, and commercial drones. The same Chinese-manufactured module that enables a US logistics company's warehouse robot fleet is also the connectivity layer being evaluated for security risks by CISA. Companies with regulatory compliance requirements (defense-adjacent, critical infrastructure, healthcare) should audit their robot connectivity stack for Quectel and Fibocom modules. Alternatives: u-blox (Swiss), Telit Cinterion (UK/Italian), Sierra Wireless/Semtech (Canadian-headquartered).

**⚑ Shared supplier — Qualcomm Snapdragon Flight / RB5:** Qualcomm's drone-specific (Snapdragon Flight) and robotics-specific (RB5 platform) compute and connectivity modules appear in Skydio, professional drone builds, and AMR platforms. Qualcomm is US-owned and ITAR-compliant, but its chips are manufactured at TSMC (Taiwan), adding a secondary geographic concentration.

**DJI proprietary protocols:** DJI's OcuSync and O3 image transmission systems operate in 2.4/5.8 GHz with FHSS and MIMO for long-range, low-latency HD video. The performance of these systems — particularly O3's 15 km range and sub-120ms latency — has not been matched by any open-standard equivalent. This is a genuine technical moat, not just a marketing claim, and is one reason DJI maintains market share even in enterprise segments where data security concerns are known.

**5G BVLOS opportunity:** The combination of 5G cellular connectivity (enabling command and control at range) and evolving FAA BVLOS rulemaking is the key unlock for commercial drone delivery at scale. Companies like AT&T, Verizon, and T-Mobile are positioning 5G aviation services for drone operators; Qualcomm's Snapdragon X65 modem with drone-specific features is the likely connectivity layer. Watch FAA BVLOS ARC (Aviation Rulemaking Committee) outputs and the progress of Part 108 BVLOS rules as the key regulatory variable.

### Supply Chain — Last Reviewed: 2026-03-24
