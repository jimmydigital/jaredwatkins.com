---
title: Naval Drones / Autonomous Surface Vessels
date: 2026-06-29
lastmod: 2026-06-29
draft: false
description: Companies building autonomous surface vessels (ASVs) and unmanned maritime systems for defense and commercial applications.
tags: ["robotics", "naval-drone", "autonomous-surface-vessel", "maritime", "defense"]
categories: ["overview"]
research_area: "robotics/naval-drones"
last_reviewed: 2026-06-29
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9
  disable: false
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


## Overview

The autonomous surface vessel (ASV) sector is emerging as a major defense procurement category, driven by US Navy programs (MUSV, LUSV, Ghost Fleet Overlord) and the demonstrated effectiveness of naval drones in the Russia-Ukraine conflict. Unlike aerial drones, maritime autonomy development is concentrated in a small number of well-funded US defense startups — there is no DJI equivalent here. The competitive moat is system integration: hull engineering, propulsion, autonomy software, and payload integration combined at scale.

The US Navy's Distributed Maritime Operations (DMO) concept explicitly calls for a large unmanned surface fleet to extend the reach and lethality of manned ships without putting hulls and crews at equal risk. This doctrinal demand is the primary market driver.

## Key Themes

- US Navy MUSV (Medium Unmanned Surface Vehicle) and LUSV (Large Unmanned Surface Vehicle) programs as the primary government demand signal
- Ghost Fleet Overlord program validating ASV autonomy at operational scale
- Ukraine conflict demonstrating the asymmetric effectiveness of small, attritable maritime drones (Magura V5)
- Autonomy software and mission-level command and control as the primary competitive differentiator
- Shipbuilding capacity as a bottleneck — most players are investing in manufacturing infrastructure as much as R&D
- Payload modularity: ISO container-compatible payloads enabling multi-mission ASVs without dedicated hulls

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Saronic Technologies](https://www.saronic.com) | Austin, TX, USA | Late Private ($9.25B valuation, Series D 2026) | Autonomous surface vessels for US Navy; three-vessel product line (Corsair 24', Mirage 52', Marauder 180'); Echelon autonomy software; $392M Navy contract; selected for MUSV Marketplace. |
| [HavocAI](https://www.havocai.com) | Providence, RI, USA | Early Private (~$185M raised) | Software-first maritime autonomy; 30+ ASVs delivered to US DoD; Rampage swarm vessel; 200-foot ASV with Hanwha; first air-sea GPS-denied autonomy demo (December 2025). |
| [Anduril Industries](https://anduril.com) | Costa Mesa, CA, USA | Late Private (~$28–30B valuation) | Partnering with HD Hyundai for 200-foot ASV targeting MASC program; first vessel in fabrication (April 2026); Seattle shipyard (former Foss Shipyard) as US assembly hub. See also: [Anduril undersea systems]({{< relref "/research/robotics/undersea-drones/anduril-undersea.md" >}}). |

## Key Programs

| Program | Type | Lead Agency | Notes |
|---------|------|-------------|-------|
| **MASC (Modular Attack Surface Craft)** | Merged MUSV + LUSV | US Navy | Replaces separate MUSV/LUSV programs (merged 2025); Saronic, Anduril/HD Hyundai, and HavocAI/Hanwha all competing; modular payload emphasis |
| **MUSV Marketplace** | Medium USV (~185 ft) | US Navy (PEO USC) | Pre-MASC vehicle; Saronic selected and delivering Corsair ASVs under $392M OTA |
| **Ghost Fleet Overlord** | Autonomous teaming demo | DARPA / ONR | Validated long-range autonomous navigation at sea; completed Phase 2; Seahawk and Sea Hunter entering fleet operations early 2026 |
| **DARPA Pulling Guard** | ASW / undersea ISR | DARPA | Saronic selected; autonomous maritime ISR for anti-submarine warfare |

## Sources

- [Saronic Technologies — Vessels](https://www.saronic.com/vessels)
- [Saronic Newsroom](https://www.saronic.com/newsroom)
- [Defense One — Navy robot ships on 15-year path (Feb 2024)](https://www.defenseone.com/threats/2024/02/navy-15-year-path-operating-robot-ships-speed-and-scale-cno-says/394162/)
