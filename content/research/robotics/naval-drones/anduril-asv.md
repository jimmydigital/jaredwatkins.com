---
title: "Anduril Industries — Autonomous Surface Vessels"
date: 2026-06-29
lastmod: 2026-06-29
draft: false
description: "Anduril's ASV program: partnering with HD Hyundai to build a new class of autonomous surface vessels targeting the US Navy MASC program. First vessel in fabrication in South Korea (April 2026); US assembly hub at former Foss Shipyard in Seattle. Separate from Anduril's undersea portfolio (Ghost Shark, Dive-LD, Copperhead)."
tags: ["robotics", "naval-drone", "autonomous-surface-vessel", "maritime", "defense", "us", "private"]
categories: ["company"]
research_area: "robotics/naval-drones"
source_urls:
  - "https://www.anduril.com/news/anduril-to-build-autonomous-warships"
  - "https://www.defensenews.com/industry/techwatch/2026/04/20/anduril-hd-hyundai-expands-partnership-with-first-autonomous-surface-vessel-in-production/"
last_reviewed: 2026-06-29
stale_after_days: 60
related:
  - "robotics/aerial-drones/anduril.md"
  - "datacenters/rugged-edge-compute/anduril.md"
  - "robotics/naval-drones/anduril-undersea.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


> **See also:** [Anduril — Autonomous Aerial Systems]({{< relref "/research/robotics/aerial-drones/anduril.md" >}}) and [Anduril — Undersea Systems]({{< relref "anduril-undersea.md" >}}). Company overview, Lattice OS, and the $20B Army contract are covered in the [canonical Anduril file]({{< relref "/research/datacenters/rugged-edge-compute/anduril.md" >}}).

## ASV Program Overview

Anduril's surface vessel program is a partnership with HD Hyundai Heavy Industries — the world's largest shipbuilder by volume — to design and produce a new class of modular autonomous surface vessels. The primary target is the US Navy's MASC (Modular Attack Surface Craft) program, which merged the earlier MUSV and LUSV programs in 2025.

The strategic logic: Anduril provides the autonomy software stack (Lattice OS), mission systems integration, and speed-to-market; HD Hyundai provides industrial-scale shipbuilding capability and hull engineering expertise. This mirrors the Saronic/Gulf Craft acquisition approach but uses a joint venture model rather than direct acquisition.

## Vessel Specifications

Specific dimensions and payload figures have not been publicly released. The vessel is designed around:

- **Software-defined architecture:** Propulsion, navigation, and payload control integrated into Lattice OS; missions reconfigurable in real time without hardware changes
- **Modular payload bays:** Multiple mission configurations — ISR, strike, EW — from the same hull
- **No vendor lock:** Open hardware and software stacks to accommodate Navy-specified payloads

## Development Timeline

| Date | Milestone |
|------|-----------|
| Late 2024 | Partnership announced between Anduril and HD Hyundai |
| April 2026 | First vessel in fabrication at HD Hyundai shipyard in South Korea |
| October 2026 | Prototype expected to be in the water (per April 2026 reporting) |
| Late 2026 | Anduril takes ownership of vessel for US coastal testing |
| TBD | Transition to US manufacturing at former Foss Shipyard, Seattle |

## US Manufacturing Hub

Anduril has invested tens of millions of dollars in the historic former Foss Shipyard in Seattle, Washington, to serve as its initial US hub for low-rate vessel assembly, integration, and testing. All future ASVs — including any MASC production units — will be US-built.

## Lattice Integration

The ASV is an explicit Lattice OS node — making it part of the same command-and-control mesh as Anduril's Fury CCA, Roadrunner interceptor, Ghost Shark AUV, and Altius loitering munitions. The cross-domain integration is the differentiating claim: one Lattice interface cuing surface, aerial, and undersea autonomous assets simultaneously.

## Competitive Position

| Competitor | Overlap | Key Difference |
|-----------|---------|----------------|
| [Saronic]({{< relref "saronic.md" >}}) | MASC/MUSV; 200-foot ASV class | Saronic selected for Navy MUSV Marketplace and has $392M contract; Anduril vessel still in prototype fabrication as of mid-2026 |
| [HavocAI + Hanwha]({{< relref "havocai.md" >}}) | Same 200-foot ASV class; same Hanwha relationship | HavocAI has earlier delivery track record; Anduril has deeper software and multi-domain integration |

## Sources

- [Anduril — Autonomous Warships announcement](https://www.anduril.com/news/anduril-to-build-autonomous-warships)
- [Defense News — First ASV in production (April 2026)](https://www.defensenews.com/industry/techwatch/2026/04/20/anduril-hd-hyundai-expands-partnership-with-first-autonomous-surface-vessel-in-production/)
- [Army Recognition — Anduril/HD Hyundai MASC](https://www.armyrecognition.com/news/navy-news/2025/anduril-unites-with-hd-hyundai-to-pioneer-next-gen-modular-warship-autonomy-for-u-s-naval-vision)
