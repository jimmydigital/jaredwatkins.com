---
title: "Dedrone (Axon)"
date: 2026-06-05
lastmod: 2026-06-05
draft: false
description: "Multi-sensor drone detection platform combining RF sensing, radar, video, acoustic, and Remote ID ingestion — acquired by Axon Enterprise in October 2024; DedroneTracker.AI software fusion engine."
research_area: "drone-detection/hardware"
source_urls:
  - "https://www.dedrone.com/"
  - "https://www.dedrone.com/products/drone-detection-software"
  - "https://www.dedrone.com/press/dedrone-defense-launches-dedronetactical-to-meet-rising-demand-for-agile-expeditionary-multi-sensor-counter-suas-solutions"
  - "https://internet-satelitarny.eu/2025/09/22/inside-the-anti%E2%80%91drone-shield-stopping-uavs-cold-how-dedrones-ai-rf-sensors-smart-jammers-secure-skies-from-stadiums-to-battlefields/"
last_reviewed: 2026-06-05
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Dedrone (now a division of Axon Enterprise) is one of the largest civilian C-UAS detection platform vendors. Its hardware-agnostic software platform, DedroneTracker.AI, fuses inputs from proprietary RF sensors, radar, cameras, acoustic devices, and Remote ID receivers to deliver detection, tracking, classification, and mitigation across large facilities. Axon acquired Dedrone in October 2024, expanding into the enterprise and law enforcement markets.

## Key Facts

- **Parent:** Axon Enterprise (NASDAQ: AXON), acquired October 2024
- **Founded:** 2014, Germany
- **HQ:** Washington, D.C. (post-acquisition)
- **Type:** Company — Platform OEM + Software
- **Key product:** DedroneTracker.AI (fusion software) + RF-360 sensor hardware
- **Drone protocol library:** dedroneDNA — 200+ drone types
- **Status:** Active; growing post-acquisition

## What It Is / How It Works

Dedrone's architecture separates sensors from the intelligence layer:

**RF-360 Sensor (flagship RF hardware):**
- Detection range: ~2 km typical / up to 5 km in ideal line-of-sight conditions
- Direction finding: 2.5° azimuth accuracy via angle-of-arrival (AoA)
- Coverage: 360° omnidirectional
- Ruggedization: IP65; MIL-STD-810H; MIL-STD-1275 power
- Power: 24 W typical; integrated LTE/GPS for remote reporting
- Detects: RF control links, video downlinks, proprietary protocols (DJI OcuSync, Mavlink); ingests Remote ID

**DedroneTracker.AI (software fusion engine):**
- Fuses RF, radar, video, and acoustic inputs into unified threat picture
- AI/ML classification against dedroneDNA library (200+ drone types)
- Operator location triangulation where RF link present
- Alert and integration APIs for SOC/SIEM connection

**DedroneTactical (2025 launch):**
A man-portable, expeditionary multi-sensor C-UAS package targeting mobile security operations. Launched mid-2025 in response to growing demand for rapid-deployment C-UAS.

## Notable Developments

- **2025:** Dedrone Defense launches DedroneTactical — expeditionary portable multi-sensor C-UAS solution
- **2025:** Intelligence report documents evolving drone tactics in the field; swarm detection identified as emerging requirement
- **2024-10:** Axon Enterprise closes acquisition of Dedrone; integrates into public safety / law enforcement product suite
- **2024-05:** Axon agrees to acquire Dedrone (announced)

## Key People

<!-- TODO: Research and add Dedrone/Axon leadership. Post-acquisition org chart not yet researched. -->

### People — Last Reviewed: 2026-06-05

## Claim Verification

### Claim: 200+ drone type library (dedroneDNA)
**Status:** Unverified independently — company-stated figure. The protocol library claim is plausible given the age and market position of the platform.
**Supporting sources:** [Dedrone product page](https://www.dedrone.com) — company-stated
**Refuting/questioning sources:** None found. Independent lab validation not publicly available.
**Summary:** Plausible; unverified by independent third parties.

### Claim: RF-360 range up to 5 km
**Status:** Partially verified — 2 km typical, 5 km stated as ideal-conditions maximum.
**Supporting sources:** [Dedrone technical writeup](https://internet-satelitarny.eu/2025/09/22/inside-the-anti%E2%80%91drone-shield-stopping-uavs-cold-how-dedrones-ai-rf-sensors-smart-jammers-secure-skies-from-stadiums-to-battlefields/) cites these figures
**Summary:** 2 km is the realistic planning figure; 5 km is best-case and should not be used for site planning.

## Sources

- [Dedrone product portfolio](https://www.dedrone.com/)
- [DedroneTracker.AI](https://www.dedrone.com/products/drone-detection-software)
- [DedroneTactical launch press release](https://www.dedrone.com/press/dedrone-defense-launches-dedronetactical-to-meet-rising-demand-for-agile-expeditionary-multi-sensor-counter-suas-solutions)
- [Dedrone 2025 Intelligence Report](https://www.dedrone.com/blog/intelligence-report-2025)
