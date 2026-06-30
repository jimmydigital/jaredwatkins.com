---
title: "Skydio C-UAS and Autonomous Patrol"
date: 2026-06-05
lastmod: 2026-06-05
draft: false
description: "Skydio's counter-UAS and autonomous patrol capabilities for critical infrastructure and military base protection — drone-in-a-box perimeter defense, AI anomaly detection, and the X10/X10D platform."
research_area: "drone-detection/hardware"
source_urls:
  - "https://www.skydio.com/solutions/national-security/base-security"
  - "https://www.skydio.com/solutions/site-security"
  - "https://www.skydio.com/x10d/technical-specs"
  - "https://www.skydio.com/blog/u-s-army-usd52-million-order-skydio-x10d"
  - "https://www.skydio.com/blog/skydio-raises-230-million-series-e-funding-round"
  - "https://dronelife.com/2025/05/05/skydio-delivers-first-x10d-systems-for-u-s-armys-srr-program-as-u-s-manufacturers-race-to-scale-production/"
  - "https://www.airforce-technology.com/news/skydio-dock-us-airforce-drone/"
  - "https://www.tectonicdefense.com/skydio-raises-110m-at-4-4b-valuation/"
last_reviewed: 2026-06-05
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Skydio is a US drone manufacturer that has pivoted heavily to defense and critical infrastructure security, now the largest US-manufactured drone platform by DoD procurement. Its core C-UAS and site-security capability is AI-driven autonomous patrol: a dock-deployed drone that autonomously detects, identifies, and tracks intruders — including drones — without requiring a trained pilot. This makes Skydio relevant to critical infrastructure operators both as an autonomous patrol asset and as a UAS intruder response platform.

## Key Facts

- **HQ:** Redwood City, California, USA
- **Founded:** 2014
- **Type:** Company — drone hardware, autonomy software
- **Status:** Active (private, post-Series F)
- **Latest funding:** $110M Series F at $4.4B valuation (2025)
- **Prior funding:** $230M Series E (2023) + $170M extension (Nov 2024) at $2.5B valuation
- **Key platform:** Skydio X10 / X10D
- **Value chain position:** Platform OEM + Software/AI layer
- **Blue UAS:** Skydio X10D is on the DoD Blue UAS approved procurement list — material differentiator for US government customers

## What It Is / How It Works

Skydio's defense-relevant capability rests on two distinct but related pillars:

**1. Autonomous flight and obstacle avoidance.** Skydio drones use onboard computer vision (six 360° navigation cameras) rather than GPS as the primary navigation reference. This provides GPS-denied flight capability and autonomous obstacle avoidance — important in contested environments and around infrastructure with complex geometry. Drones can execute programmed patrol routes and return-to-dock autonomously.

**2. AI detection and anomaly classification.** Onboard AI processes camera feeds in real time to detect people, vehicles, and anomalies without offloading to cloud or requiring remote piloting. When deployed in a Skydio Dock, the system autonomously launches to investigate sensor alerts or programmed patrol intervals.

**Skydio Dock (drone-in-a-box):** A weatherproof autonomous charging and launch station. When triggered by a perimeter sensor alert, access control event, or schedule, the dock automatically opens, launches the drone, navigates to the alert location, and streams live video to security personnel — all without requiring a pilot on-site. Dock-to-airborne time is under 20 seconds.

**C-UAS role:** Skydio's C-UAS capability is primarily detection and documentation of intruder drones rather than interdiction. When an unauthorized drone enters a protected site, a responding Skydio drone can track it autonomously, maintain visual contact, record evidence, and provide live coordinates to security personnel or law enforcement. The X10D's EW-resilient design means it continues operating in RF-contested environments where a less hardened drone might lose control link.

## Products

### Skydio X10

Commercial/law enforcement version of the platform. Features:
- Multiple camera payloads: 50.3 MP wide-angle, 48 MP telephoto, 64 MP narrow-field
- AI anomaly detection (people, vehicles, intrusions)
- Dock-compatible for autonomous deployment
- Used in civilian critical infrastructure security, utility inspection, and law enforcement DFR (Drone as First Responder)

**Maximum radio range:** Up to 12 km (Connect SL link)

### Skydio X10D

Defense/government version. Differences from X10:
- ITAR-controlled; sold to US government and approved allies
- Teledyne FLIR Boson+ thermal sensor integration (640×512, ≤30mK sensitivity)
- Electronic warfare (EW) resilience — operates in GPS-denied and RF-contested environments
- GPS-denied navigation via onboard visual SLAM
- Hardened controller: 6.6" AMOLED display, 1,750 nit outdoor brightness, 9,600 mAh battery (5 hours)
- Deployment time: under 40 seconds
- Top speed: 45 mph

### Skydio F10 (announced/upcoming)

Extended-range base security drone for long-perimeter response. Larger operational radius than X10, capable of responding to incidents miles from the launch dock. Designed for large military base and border perimeter applications.

## Notable Developments

- **2025:** $110M Series F announced; valuation reaches $4.4B
- **2025-07:** $9.4M contract with Royal Norwegian Ministry of Defence for X10D systems
- **2025-05:** Delivers first X10D units under US Army Short Range Reconnaissance (SRR) Tranche 2 program
- **2025-02:** $18.7M contract with Spain's Ministry of Defence
- **2024-11:** $170M extension to Series E; valuation $2.5B
- **2024:** USAFCENT places $9M+ order for Skydio Dock + X10 systems to secure US airbases in Middle East — one of the largest autonomous drone security deployments by the US Air Force internationally
- **2024:** US Army places $52M+ order for 2,500+ X10D — largest single-vendor tactical sUAS order in Army history
- **2023:** $230M Series E raised; company described as largest US drone manufacturer

## Relevance to Critical Infrastructure Protection

For non-federal critical infrastructure operators (power utilities, water facilities, data centers), the Skydio X10 + Dock combination provides:

- **24/7 autonomous patrol** without requiring continuous operator staffing — the drone launches automatically on schedule or on alarm trigger
- **Drone response to drone threat** — when a hostile drone is detected by a radar or RF sensor layer, a Skydio dock can launch to track it autonomously, providing visual evidence that fixed cameras cannot
- **On-demand inspection** — the same platform serves routine infrastructure inspection and security patrol, improving ROI

**Limitation:** Skydio's system detects intruding drones visually and tracks them but does not jam, spoof, or take control. It is a tracker/documenter, not an interceptor. Physical interdiction requires either DoD/DHS authorization or a separate kinetic system.

**Blue UAS distinction:** The X10D's presence on the DoD Blue UAS list means US federal agencies and many state/local law enforcement entities can procure it directly without additional vendor vetting. This accelerates adoption at federally regulated critical infrastructure.

## Claim Verification

### Claim: Sub-20-second Skydio Dock deployment time
**Status:** Partially verified

**Supporting sources:**
- [Skydio base security page](https://www.skydio.com/solutions/national-security/base-security) — company states "deploys in under 20 seconds"

**Refuting / questioning sources:**
- No independent third-party timing verification found. Time-to-launch figures from company demos may not reflect cold-start, low-temperature, or high-wind conditions.

**Summary:** Company-stated figure; likely representative of nominal conditions. Cold weather or mechanical hesitation may extend deployment time.

### Claim: GPS-denied autonomous navigation in contested RF environments
**Status:** Partially verified

**Supporting sources:**
- [X10D specs page](https://www.skydio.com/x10d/technical-specs) — documented visual SLAM navigation using six onboard cameras
- Army SRR program selection implies performance in relevant test environments

**Refuting / questioning sources:**
- Visual SLAM degrades in low-light, featureless terrain, or heavy smoke/fog environments. No public independent evaluation of GPS-denied performance under adversarial EW conditions.

**Summary:** Technology approach (visual SLAM with six cameras) is sound; operational performance under realistic EW conditions not independently verified in public literature.

## Key People

- **Adam Bry** — Co-founder and CEO. [LinkedIn](https://www.linkedin.com/in/adam-bry-3891271/) — previously MIT AeroAstro, Google[X]
- **Abraham Bachrach** — Co-founder and CTO. [LinkedIn](https://www.linkedin.com/in/abachrach/) — previously MIT, Google[x]
- **Matt Donahoe** — Chief Revenue Officer. LinkedIn: not confirmed
- **⚑ MIT AeroAstro cluster:** Both founders have MIT AeroAstro background, aligning with the MIT CSAIL/AeroAstro robotics people cluster noted in the robotics steering doc.

### People — Last Reviewed: 2026-06-05

## Sources

- [Skydio base security](https://www.skydio.com/solutions/national-security/base-security) — autonomous patrol and C-UAS use case
- [Skydio site security](https://www.skydio.com/solutions/site-security) — civilian infrastructure deployment
- [X10D technical specs](https://www.skydio.com/x10d/technical-specs) — full hardware specifications
- [Army $52M order announcement](https://www.skydio.com/blog/u-s-army-usd52-million-order-skydio-x10d) — largest Army sUAS procurement
- [Series E announcement](https://www.skydio.com/blog/skydio-raises-230-million-series-e-funding-round) — funding and company scale
- [X10D first deliveries (DroneLife)](https://dronelife.com/2025/05/05/skydio-delivers-first-x10d-systems-for-u-s-armys-srr-program-as-u-s-manufacturers-race-to-scale-production/) — SRR Tranche 2 delivery
- [USAFCENT contract](https://www.airforce-technology.com/news/skydio-dock-us-airforce-drone/) — Middle East airbase security
- [Series F at $4.4B](https://www.tectonicdefense.com/skydio-raises-110m-at-4-4b-valuation/) — latest funding round
