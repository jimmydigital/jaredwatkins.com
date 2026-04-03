---
title: "Quectel"
date: 2026-03-31
lastmod: 2026-03-31
draft: false
description: "Shanghai cellular IoT module maker (603236.SS); world's largest by shipment volume at ~47% global unit market share; EC/RG series modules are de facto standard in AMR and drone platforms globally; added to DoD Section 1260H Chinese Military Company list and subject to FCC national security scrutiny."
tags: ["robotics", "communications", "china"]
categories: ["company"]
research_area: "robotics/communications"
chinese-owned: true
source_urls:
  - "https://iotbusinessnews.com/2025/02/19/02010-2024-cellular-iot-module-market-update/"
  - "https://www.scmp.com/tech/tech-war/article/3233671/us-fcc-chair-says-chinas-iot-cellular-components-makers-quectel-fibocom-may-pose-national-security"
  - "https://iotdesignpro.com/news/fcc-now-urges-to-blacklist-chinese-iot-module-firms-quectel-and-fibocom-wireless-why"
last_reviewed: 2026-03-31
stale_after_days: 90
related: []
---

> **Note:** This company is Chinese-owned. Performance claims and publicly reported figures should be treated with additional skepticism until independently verified by non-affiliated third parties.

## Summary

Quectel Wireless Solutions (Shanghai STAR Market: 603236.SS) is the world's largest cellular IoT module maker by unit shipments, holding approximately 46.6% global market share on a shipment basis in 2024. Founded in 2010 by Patrick Qian, Quectel supplies LTE, 5G, NB-IoT, and GNSS modules that are widely integrated into AMR platforms, autonomous drones, industrial robots, and connected devices globally. Its dominant market position is achieved through aggressive pricing at low margins (~3%) and broad product coverage. The company's scale and Chinese ownership have generated significant US national security scrutiny: Quectel is listed on the DoD's Section 1260H Chinese Military Company list, the FCC has flagged its modules as a potential national security risk in critical infrastructure, and Quectel has denied any military affiliation while pledging to contest the designations.

## Key Facts

- **Founded:** 2010 (Shanghai, China)
- **HQ:** Shanghai, China
- **Type:** Public (Shanghai STAR Market: 603236.SS)
- **Ownership:** Chinese private company; Patrick Qian is founder and controlling shareholder
- **Key products:** EC series (LTE Cat 1/4/6/M1 modules); RG series (5G NR modules, including RG500Q); SC series (smart Android modules); GNSS standalone modules (LC29H series)
- **Revenue:** Part of the ~$5.6B global cellular IoT module market (2024); Quectel holds ~31% revenue market share (~$1.7B estimated)
- **Market share:** ~46.6% of global cellular IoT module unit shipments in 2024 (Statista/IoT Analytics); revenue leader among IoT module companies
- **US regulatory status:** Listed on DoD Section 1260H Chinese Military Company list; FCC flagged as potential national security risk (October 2025); Quectel denies military ties and has contested the designation

## What It Is / How It Works

A cellular IoT module is a self-contained circuit board that combines a cellular radio (modem) chip, RF transceiver, SIM interface, power management, and antenna connections into a standard form factor that a device maker can solder onto their circuit board. The module handles all the complexity of connecting to LTE, 5G, NB-IoT, or LTE-M networks — the host device simply sends AT commands over UART or USB to initiate connections and exchange data. For robotics applications, this means a drone or AMR manufacturer can add cloud connectivity and cellular positioning without designing RF circuitry from scratch.

Quectel's EC series (LTE) and RG series (5G) are its primary robotics-relevant product lines. The EC21, EC25, and related variants are the LTE modules embedded in most commercial drone ground control station modems, AMR fleet management systems, and warehouse robot connectivity modules. The RG500Q and RG520N are the 5G variants used in next-generation autonomous vehicle and AMR platforms requiring low-latency, high-bandwidth cloud connectivity. Many AMR platforms from Geek+, Locus Robotics, and similar companies use Quectel modules for their cellular uplink because no Western supplier approaches Quectel's price at equivalent integration levels.

Quectel's competitive strategy is volume over margin: the company accepts approximately 3% net profit margins to maximize market share. This is a deliberate choice to lock in design wins and create switching costs — once a robot OEM's firmware and supply chain is certified for a specific Quectel module, switching to a competing module requires significant re-engineering and re-certification effort. The ~46.6% unit market share in 2024 (up 5.2% year-over-year) indicates this strategy is succeeding.

The national security concerns center on PRC law requiring companies to cooperate with state intelligence agencies upon request. A cellular module with access to device location, network traffic metadata, and connectivity state — deployed in critical infrastructure, autonomous vehicles, or military-adjacent logistics robots — could theoretically be exploited for intelligence collection or remote disabling. Whether Quectel modules actually contain backdoors or have been used for such purposes is not established by public evidence. The US government's concern is structural: the legal and political environment in China means Quectel could be compelled to act as an intelligence asset regardless of its intentions. Quectel disputes this characterization.

Western alternative module suppliers include Sierra Wireless (Semtech), Telit Cinterion, Fibocom, and u-blox's cellular line. None match Quectel's breadth, volume, or pricing. This creates a genuine market problem: US robotics companies face a choice between security-compliant but more expensive modules that may lack certain form factors or certifications, or Quectel modules with better price-performance but national security exposure.

## Notable Developments

- **2025-10:** FCC publishes fact sheet specifically noting Chinese-produced cellular modules (including Quectel) as potential security threats in IoT infrastructure. ([FCC](https://docs.fcc.gov/public/attachments/DOC-415051A1.pdf))
- **2025:** DoD adds Quectel to Section 1260H Chinese Military Company list; Quectel denies affiliation and pledges to fight the designation. ([Light Reading](https://www.lightreading.com/security/baicells-quectel-pledge-to-fight-us-government-s-new-warning))
- **2024:** Full year 2024 — Quectel holds 46.6% global cellular IoT module shipment share (+5.2% YoY); cellular IoT module revenue leader globally; market grew to ~$5.6B total.
- **2024-Q1:** 19% YoY revenue growth in Q1 2024; managed to match full year 2023 revenue by Q3 2024.
- **2023:** House Select Committee on CCP writes to FCC warning about Quectel and Fibocom modules in IoT devices used by law enforcement and critical infrastructure operators. ([House Select Committee](https://chinaselectcommittee.house.gov/media/letters/letter-fcc-chair-chinese-internet-connectivity-modules))
- **2023:** FCC Chair Rosenworcel asks federal agencies to assess whether Quectel and Fibocom should be added to the Covered List. ([SCMP](https://www.scmp.com/tech/tech-war/article/3233671/us-fcc-chair-says-chinas-iot-cellular-components-makers-quectel-fibocom-may-pose-national-security))
- **2010:** Company founded by Patrick Qian in Shanghai; listed on Shanghai STAR Market.

## Key People

### Patrick Qian — Founder and CEO
- **LinkedIn:** Not found (no confirmed public LinkedIn profile for Patrick Qian)
- **Education:** Not publicly disclosed in detail
- **Career (reverse-chronological):**
  - Quectel (2010–present): Co-founder and CEO; Chairman of Board
  - Simcom (2002–2009): Vice General Manager of R&D (Chinese cellular module competitor)
  - ZTE (2000–2002): Project Manager
- **Notes:** Qian is described as one of the first engineers in China to dedicate his career to wireless module development. The Simcom → Quectel trajectory mirrors the broader Chinese electronics industry pattern of technical talent from state-adjacent companies spinning out to found competing ventures. His 7 years at Simcom before founding Quectel gave him deep knowledge of the module market and customer relationships.

### People — Last Reviewed: 2026-03-31

## Supply Chain Position

Quectel operates at the **Component/Subsystem Supplier** layer, selling modules to device OEMs, system integrators, and robotics manufacturers. Its modules incorporate cellular modem chips from Qualcomm (MDM9205/9607), MediaTek, and proprietary Quectel/Unisoc chips depending on the tier. Assembly is in China. The company offers over 500 module variants and 250 antennas, spanning every cellular technology from 2G through 5G and NB-IoT/LTE-M. **⚑ Shared supply chain exposure:** Many Quectel competitors (Fibocom, Sierra Wireless/Semtech) also use Qualcomm modem chips, creating shared supply chain exposure to Qualcomm chipset allocation constraints. The broader bifurcation risk — Western governments restricting Chinese cellular modules in critical applications — creates an opportunity for u-blox, Telit, and Sierra Wireless to capture volume currently going to Quectel.

## Claim Verification

### Claim: Quectel holds ~46.6% global cellular IoT module unit market share (2024)
**Status:** Verified (by independent market research)

**Supporting sources:**
- [IoT Business News — 2024 Cellular IoT Module Market Update (Feb 2025)](https://iotbusinessnews.com/2025/02/19/02010-2024-cellular-iot-module-market-update/) — Cites Quectel at 46.6% unit share in 2024, +5.2% YoY; independent analysis
- [Statista — Global Cellular IoT Module Shipments Share 2024](https://www.statista.com/statistics/787755/global-cellular-iot-module-shipments-share/) — Independent data confirming Quectel as dominant shipment leader

**Refuting / questioning sources:**
- Revenue market share (~31%) is substantially lower than unit share (~47%), suggesting Quectel's average selling price per module is below market average — consistent with the known 3% margin / volume strategy; the unit share figure is accurate but overstates Quectel's economic significance relative to its shipment dominance

**Summary:** The ~47% unit shipment market share is independently verified; the revenue share (~31%) is a more relevant economic metric and is also well-documented.

## Sources

- [2024 Cellular IoT Module Market Update — IoT Business News (Feb 2025)](https://iotbusinessnews.com/2025/02/19/02010-2024-cellular-iot-module-market-update/)
- [FCC Chair: Quectel and Fibocom May Pose National Security Risk — SCMP](https://www.scmp.com/tech/tech-war/article/3233671/us-fcc-chair-says-chinas-iot-cellular-components-makers-quectel-fibocom-may-pose-national-security)
- [FCC Fact Sheet on Cellular Modules (Oct 2025)](https://docs.fcc.gov/public/attachments/DOC-415051A1.pdf)
- [House Select Committee Letter to FCC on Chinese IoT Modules](https://chinaselectcommittee.house.gov/media/letters/letter-fcc-chair-chinese-internet-connectivity-modules)
- [FCC Urges Blacklist of Quectel and Fibocom — IoT Design Pro](https://iotdesignpro.com/news/fcc-now-urges-to-blacklist-chinese-iot-module-firms-quectel-and-fibocom-wireless-why)
- [Patrick Qian — Quectel](https://www.quectel.com/team/patrick-qian/)
- [Quectel Pledges to Fight US Government Warning — Light Reading](https://www.lightreading.com/security/baicells-quectel-pledge-to-fight-us-government-s-new-warning)
