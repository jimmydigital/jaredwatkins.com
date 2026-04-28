---
title: "Teledyne FLIR"
date: 2026-03-31
lastmod: 2026-03-31
draft: false
description: "Teledyne Technologies' thermal imaging division; world's largest volume manufacturer of ITAR-free infrared sensors and modules; Boson and Lepton modules are the dominant OEM thermal payloads for drones, UGVs, and defense platforms."
tags: ["robotics", "sensor", "us", "defense", "commercial"]
categories: ["company"]
research_area: "robotics/sensors"
source_urls:
  - "https://oem.flir.com/products/lepton/"
  - "https://defense.flir.com/about/news/teledyne-flir-defense-unveils-cerberus-xl-c-uas-mobile-counter-drone-system-at-ausa-2024/"
  - "https://dronelife.com/2026/02/24/teledyne-flir-lepton-xds-dual-thermal-visible-camera/"
  - "https://dronelife.com/2025/03/11/teledyne-flir-introduces-radiometric-thermal-camera-modules-for-defense-and-industrial-applications/"
last_reviewed: 2026-03-31
stale_after_days: 180
related: []
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Teledyne FLIR is the thermal imaging division of Teledyne Technologies (NYSE: TDY), headquartered in Wilsonville, Oregon. FLIR Systems was acquired by Teledyne in 2021 for approximately $8 billion. It is the world's largest volume manufacturer of commercial and defense thermal infrared (IR) imaging sensors and modules, with products ranging from the Lepton (penny-sized OEM module for consumer and commercial drones) to the Boson+ (military-grade uncooled LWIR for UAS, UGV, and defense platforms) to the Neutrino series (cooled, high-performance ISR sensors). Teledyne FLIR maintains a strategic position in the robotics supply chain because thermal imaging is the dominant sensor modality for night operations, target detection, fire monitoring, and machine vision in degraded visual environments, and FLIR holds near-monopoly market share in ITAR-free uncooled OEM thermal modules.

## Key Facts

- **Founded:** FLIR Systems founded 1978; acquired by Teledyne Technologies 2021 for ~$8B
- **HQ:** Wilsonville, OR (Teledyne Technologies HQ: Thousand Oaks, CA)
- **Type:** Subsidiary of [Teledyne Technologies (NYSE: TDY)](https://finance.yahoo.com/quote/TDY)
- **Teledyne CEO:** Robert Mehrabian (Chairman, President, and CEO; returned to role October 2021 upon Al Pichelli's retirement)
- **Key products:** Lepton (OEM micro-thermal, 160×120 or 160×120 radiometric, ITAR-free); Boson / Boson+ (640×512 or 320×256 uncooled LWIR, ITAR-free); Hadron 640R/R+ (dual thermal+visible fusion module); Neutrino Ground ISR (cooled MWIR, EAR-controlled); SIRAS UAS (complete drone platform)
- **Teledyne TDY total revenue:** $5.67B FY2024; Digital Imaging segment (includes FLIR) approximated at ~$3B pro-forma at acquisition; current segment breakdown not separately disclosed

## What It Is / How It Works

Thermal infrared cameras detect emitted heat radiation rather than reflected visible light, making them independent of lighting conditions. Uncooled LWIR (Long-Wave Infrared, 8–14 μm wavelength) sensors use a microbolometer detector array — a grid of tiny resistive elements that change resistance when heated by incoming infrared radiation. The readout electronics measure these resistance changes to form a temperature map of the scene. Microbolometers operate at or near room temperature (hence "uncooled"), making them compact, low-power, and suitable for integration into drones and robots where size and power matter. Teledyne FLIR is the largest producer of microbolometer-based imaging modules.

The Lepton module family is the smallest production thermal sensor in the lineup — approximately 8.5mm × 11.7mm, drawing under 150 mW, and priced accessible to commercial drone OEMs and IoT applications. The Lepton 3.5 offers 160×120 pixels with radiometric capability (pixel-level temperature measurement, not just relative heat mapping), making it useful for temperature monitoring in industrial and safety applications. The Lepton XDS (launched February 2026) adds a 5MP visible camera to the thermal sensor in a single module, implementing FLIR's MSX technology that embeds visible-camera edge data onto the thermal image for improved scene interpretation.

The Boson and Boson+ are the higher-performance uncooled tier: 640×512 or 320×256 pixel thermal resolution, with Boson+ delivering noise-equivalent temperature difference (NETD) of 20 mK or better. Boson sensors are the dominant thermal payload for commercial and defense UAS platforms globally. They are classified under EAR (Export Administration Regulations) 6A003.b.4.a — not ITAR — which provides substantially greater flexibility for integration with international customers and foreign drone manufacturers.

The ITAR-free status of Boson and Lepton is a strategic commercial advantage. Many competing high-performance thermal modules from defense primes fall under ITAR, which restricts re-export and limits their use in international commercial robotics programs. Teledyne FLIR's OEM segment has explicitly marketed the ITAR-free classification of its commercial modules to enable broader international adoption.

For defense applications, FLIR's Neutrino series uses cooled MWIR (Mid-Wave Infrared) detectors (indium antimonide or similar cooled focal plane arrays), providing significantly better sensitivity and longer detection range than uncooled microbolometers at the cost of a cryogenic cooler, larger form factor, and higher power. These systems are used in ISR (intelligence, surveillance, reconnaissance) payloads, ground vehicle sighting systems, and manned/unmanned aircraft. The Neutrino Ground ISR module targets UGV and counter-UAS applications.

Teledyne FLIR has vertically integrated into complete drone platforms (SIRAS) and counter-drone systems (Cerberus XL C-UAS), moving beyond component supply into system integration. The Cerberus XL is a mobile counter-drone platform that combines FLIR thermal sensors, radar, and RF direction-finding to detect up to 500 targets simultaneously — a defense system competing with dedicated C-UAS integrators.

## Notable Developments

- **2026-02:** Lepton XDS dual thermal+visible OEM module launched; combines radiometric Lepton 3.5 with 5MP visible camera and MSX technology. ([Drone Life](https://dronelife.com/2026/02/24/teledyne-flir-lepton-xds-dual-thermal-visible-camera/))
- **2025-11:** FLIR Boson thermal camera powers SYPAQ CorvoX drone for Australian Army. ([Drone Life](https://dronelife.com/2025/11/03/teledyne-flir-boson-thermal-camera-powers-sypaqs-corvox-for-australian-army/))
- **2025-05:** Dragoon Defense selects Teledyne FLIR autonomy software for next-generation defense drones. ([Drone Life](https://dronelife.com/2025/05/20/dragoon-taps-teledyne-flir-for-next-gen-defense-drones/))
- **2025-03:** Radiometric versions of Boson+ and Hadron 640R+ released, enabling pixel-level temperature measurement (20 mK NETD) for UGV, UAS, and AI applications. ([Drone Life](https://dronelife.com/2025/03/11/teledyne-flir-introduces-radiometric-thermal-camera-modules-for-defense-and-industrial-applications/))
- **2024-10:** Cerberus XL C-UAS mobile counter-drone system unveiled at AUSA 2024 (Association of the United States Army). ([FLIR Defense](https://defense.flir.com/about/news/teledyne-flir-defense-unveils-cerberus-xl-c-uas-mobile-counter-drone-system-at-ausa-2024/))
- **2021:** Teledyne Technologies acquires FLIR Systems for approximately $8B (cash and stock); Robert Mehrabian resumes CEO role at Teledyne post-acquisition.

## Key People

### Robert Mehrabian — Chairman, President, and CEO of Teledyne Technologies
- **LinkedIn:** Not found
- **Education:** Not publicly disclosed in standard biographical sources; PhD-level engineering background (founded Teledyne Technologies in 1999)
- **Career (reverse-chronological):**
  - Teledyne Technologies (1999–present): Founder, Chairman, President, CEO; briefly stepped back as CEO 2019–2021 during Al Pichelli's tenure
- **Notes:** Mehrabian founded Teledyne Technologies in 1999 as a spinoff from the original Teledyne Inc. conglomerate. He has built Teledyne through serial acquisitions of high-technology defense and industrial instrumentation companies. The FLIR acquisition at ~$8B was the largest in Teledyne's history.

### People — Last Reviewed: 2026-03-31

## Supply Chain Position

Teledyne FLIR operates at multiple layers: **Component/Subsystem Supplier** (Lepton, Boson OEM modules sold to drone and robot OEMs) and **Platform OEM** (SIRAS drone, Cerberus C-UAS system). The microbolometer detector arrays at the core of uncooled thermal sensors require specialized wafer-level vacuum packaging — a manufacturing capability held by a small number of companies globally, of which Teledyne FLIR (through its SCD and DRS subsidiaries) is the dominant Western producer. **⚑ Shared supply chain dependency:** Many drone and UGV platforms that use FLIR thermal modules also use Bosch IMU, u-blox GNSS, and Herelink/Cube flight controllers — standard robotics component stacks that concentrate risk in a small number of component families.

## Claim Verification

### Claim: Teledyne FLIR is "the world's largest volume manufacturer of ITAR-free infrared sensors and modules"
**Status:** Partially verified

**Supporting sources:**
- [Teledyne FLIR OEM — StockTitan (company statement)](https://www.stocktitan.net/news/TDY/teledyne-flir-oem-advances-state-of-the-art-in-infrared-w9l6xyjc65ub.html) — Direct company claim in press release
- Market context: FLIR's Lepton module, widely available through distributors like GroupGets and DigiKey, is the de facto standard OEM thermal module for commercial drones; no Western competitor approaches its volume or distribution reach at the Lepton price point

**Refuting / questioning sources:**
- Chinese thermal sensor manufacturers (including InfiRay/IRay Technology, HIKMICRO) produce high-volume uncooled thermal modules at lower prices, though they are subject to US export restrictions and are not ITAR-free in the sense of being exportable to US government programs; the "largest" claim is contested in the global market when Chinese manufacturers are included

**Summary:** The claim is credible for ITAR-free modules sold through standard commercial channels; Chinese manufacturers likely exceed FLIR's unit volume globally, but are subject to their own export restrictions for US government customers.

## Sources

- [Lepton LWIR Micro Thermal Camera Module — Teledyne FLIR OEM](https://oem.flir.com/products/lepton/)
- [Lepton XDS Launch — Drone Life (Feb 2026)](https://dronelife.com/2026/02/24/teledyne-flir-lepton-xds-dual-thermal-visible-camera/)
- [Radiometric Boson+ and Hadron 640R+ — Drone Life (Mar 2025)](https://dronelife.com/2025/03/11/teledyne-flir-introduces-radiometric-thermal-camera-modules-for-defense-and-industrial-applications/)
- [Cerberus XL C-UAS at AUSA 2024 — FLIR Defense](https://defense.flir.com/about/news/teledyne-flir-defense-unveils-cerberus-xl-c-uas-mobile-counter-drone-system-at-ausa-2024/)
- [SYPAQ CorvoX uses FLIR Boson — Drone Life (Nov 2025)](https://dronelife.com/2025/11/03/teledyne-flir-boson-thermal-camera-powers-sypaqs-corvox-for-australian-army/)
- [Teledyne FLIR ITAR-Free IR Statement — StockTitan](https://www.stocktitan.net/news/TDY/teledyne-flir-oem-advances-state-of-the-art-in-infrared-w9l6xyjc65ub.html)
- [Teledyne Technologies FY2024 Annual Report](https://www.teledyne.com/en-us/investors/Documents/2024%20Teledyne%20Annual%20Report.pdf)
