---
title: "D-Fend Solutions"
date: 2026-06-05
lastmod: 2026-07-07
draft: false
description: "Israeli C-UAS company specializing in cyber-takeover counter-drone technology — EnforceAir system takes control of unauthorized drones and lands them safely; reportedly acquired by Motorola Solutions for ~$1.5B."
research_area: "drone-detection/hardware"
source_urls:
  - "https://d-fendsolutions.com/"
  - "https://d-fendsolutions.com/by-sector/critical-facilities-and-infrastructure/"
  - "https://www.safewareinc.com/brands/d-fend-solutions/"
  - "https://www.calcalistech.com/ctechnews/article/y2wnwz0ak"
  - "https://d-fendsolutions.com/about-us/leadership/"
last_reviewed: 2026-07-07
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

D-Fend Solutions (Israel) produces EnforceAir, a cyber-driven counter-drone system that detects, tracks, and takes over unauthorized drones — landing them safely in a controlled location. Unlike jamming, which disrupts all RF in an area, EnforceAir's "cyber scalpel" approach is selective and non-disruptive to other communications. The mitigation capability requires government/federal authorization in the US; detection-only is permissible for critical infrastructure operators.

## Key Facts

- **HQ:** Israel (offices in US)
- **Type:** Company — Platform OEM
- **Key product:** EnforceAir
- **Mitigation method:** Cyber takeover (RF protocol manipulation) — not kinetic, not jamming
- **Status:** Active; DoD and government deployments; participated in Pentagon mountain tests (Falcon Peak, 2024)
- **US legal status for mitigation:** Federal agency authorization required (DoD, DHS, DOJ, FAA, Secret Service only)

## How EnforceAir Works

EnforceAir detects the drone's RF control link, identifies the protocol and manufacturer, then injects crafted RF commands that override the operator's control and take command of the drone. The system then navigates the drone to a safe landing zone.

Key claimed advantages over jamming:
- **Surgical:** Affects only the targeted drone; does not disrupt adjacent Wi-Fi, cellular, or other RF systems
- **Non-destructive:** Drone lands intact with payload (preserves evidence; avoids crashing a potentially armed drone into personnel or facilities)
- **Locates operator:** Protocol analysis reveals operator GPS position for law enforcement
- **Non-kinetic:** No physical projectile; no collateral damage risk

## Critical Limitation for Private Infrastructure

**Cyber takeover is illegal for private entities in the US.** The Computer Fraud and Abuse Act and the Communications Act both prohibit the interference with RF communications and unauthorized access to computer systems. Only specifically authorized federal agencies may legally deploy EnforceAir's mitigation capability. Private critical infrastructure operators can use D-Fend for **detection and tracking only** unless their facility is operated by or in direct partnership with authorized federal agencies.

## RF-Dark Threat Coverage

EnforceAir fundamentally requires an RF command link to take over. **It cannot mitigate fiber-optic tethered or pre-programmed autonomous drones.** Detection of these threats requires radar or optical/acoustic layers; mitigation requires kinetic methods.

## Notable Developments

- **2026:** Reported acquisition by Motorola Solutions for approximately $1.5 billion (per Calcalist reporting). This would place D-Fend alongside [CRFS]({{< relref "crfs-rfeye.md" >}}) — also reportedly acquired by Motorola Solutions around the same period — as part of a broader Motorola push into C-UAS RF/cyber technology; treat both acquisition reports as developing and verify against Motorola Solutions' own investor disclosures before relying on them
- **2025-2026:** Two key executives appointed to support accelerated global growth and expansion of the counter-drone business (per company press release)
- **2024-11:** Participated in Pentagon "Falcon Peak" mountain tests evaluating nets, jamming, and cyber-scalpel C-UAS approaches

## Key People

- **Zohar Halachmi** — Co-founder, Chairman and CEO; previously founded two mobile/enterprise application startups and held VP/C-level roles at Amdocs and ECI Telecom
- **Yaniv Benbenisti** — Co-founder, President and Chief Product Officer
- **Assaf Monsa** — Co-founder, CTO and Vice President
- D-Fend was founded in 2016 by the three individuals above

### People — Last Reviewed: 2026-07-07

## Sources

- [D-Fend Solutions corporate](https://d-fendsolutions.com/)
- [Critical infrastructure protection — D-Fend](https://d-fendsolutions.com/by-sector/critical-facilities-and-infrastructure/)
- [D-Fend / Safeware distribution](https://www.safewareinc.com/brands/d-fend-solutions/)
- [Pentagon Falcon Peak mountain tests — Breaking Defense 2024](https://breakingdefense.com/2024/11/nets-jamming-and-cyber-scalpels-pentagon-weighs-homeland-counter-drone-tech-in-mountain-tests/)
- [Motorola Solutions acquires D-Fend for $1.5 billion — Calcalist](https://www.calcalistech.com/ctechnews/article/y2wnwz0ak)
- [D-Fend Solutions Leadership](https://d-fendsolutions.com/about-us/leadership/)
