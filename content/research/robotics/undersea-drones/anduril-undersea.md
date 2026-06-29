---
title: "Anduril Industries — Undersea Systems"
date: 2026-06-29
lastmod: 2026-06-29
draft: false
description: "Anduril's undersea portfolio: Ghost Shark XLUUV (ADF; factory open; first delivery Nov 2025); Dive-XL selected by US Navy for XLUUV program (March 2026); Copperhead-100M/500M autonomous undersea munitions (sea trials ongoing, April 2026). All integrated into Lattice OS."
tags: ["robotics", "undersea-drone", "auv", "uuv", "xluuv", "maritime", "defense", "us", "private", "autonomous-munition"]
categories: ["company"]
research_area: "robotics/undersea-drones"
source_urls:
  - "https://breakingdefense.com/2025/11/first-ghost-shark-extra-large-auv-delivered-to-australian-navy/"
  - "https://www.navalnews.com/naval-news/2026/03/diu-and-u-s-navy-select-anduril-for-xl-auv-program/"
  - "https://www.anduril.com/news/anduril-unveils-copperhead-a-new-era-of-autonomous-undersea-dominance"
  - "https://theaviationist.com/2026/04/27/anduril-shows-copperhead-500m-autonomous-underwater-munitions-testing/"
  - "https://www.anduril.com/dive-ld"
last_reviewed: 2026-06-29
stale_after_days: 60
related:
  - "robotics/aerial-drones/anduril.md"
  - "robotics/naval-drones/anduril-asv.md"
  - "datacenters/rugged-edge-compute/anduril.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


> **See also:** [Anduril — Autonomous Aerial Systems]({{< relref "/research/robotics/aerial-drones/anduril.md" >}}) and [Anduril — Autonomous Surface Vessels]({{< relref "/research/robotics/naval-drones/anduril-asv.md" >}}). Company overview and Lattice OS are in the [canonical Anduril file]({{< relref "/research/datacenters/rugged-edge-compute/anduril.md" >}}).

## Undersea Portfolio Summary

Anduril's undersea portfolio is the most ambitious in the defense startup sector, spanning three distinct capability layers: a long-range XLUUV (Ghost Shark / Dive-XL), a medium displacement AUV (Dive-LD), and an autonomous undersea munition family (Copperhead). Every platform is a Lattice OS node — the strategic intent is an undersea equivalent of the aerial autonomous swarm.

| Platform | Type | Status |
|----------|------|--------|
| **Ghost Shark XLUUV** | Extra-large AUV for ADF | Production; first delivery November 2025 |
| **Dive-XL** | XLUUV for US Navy | Selected by DIU/Navy, March 2026 |
| **Dive-LD** | Large displacement AUV | Operational |
| **Copperhead-100M** | Autonomous undersea munition (LWT class) | Sea trials ongoing (April 2026) |
| **Copperhead-500M** | Autonomous undersea munition (HWT class) | Speed record testing, April 2026 |

## Ghost Shark XLUUV

Ghost Shark is an extra-large autonomous underwater vehicle developed for the Australian Defence Force under an AUKUS-adjacent program. It is the flagship demonstration that a defense startup can develop a large AUV in three years for ~$100M (Anduril contributed ~$50M; ADF contributed the other half).

- **Contract:** 1.7 billion AUD (~$1.1B USD) with ADF, announced September 2025
- **Factory:** Dedicated robotic XLUUV manufacturing facility in Australia; $60M Anduril investment; first vehicle off the line in 2025; first delivery November 2025
- **Manufacturing:** Uses Large Format Additive Manufacturing (LFAM) for hull sections — key to rapid production scaling
- **Architecture:** Modular swappable sections with sealed pressure zones for propulsion, navigation, and payloads within a largely flooded hull volume
- **Software:** Lattice OS for autonomous navigation, mission decision-making, and multi-asset teaming

## Dive-XL — US Navy XLUUV

In March 2026, the Defense Innovation Unit (DIU) and US Navy selected Anduril's Dive-XL for the XLUUV program — the US equivalent of the Ghost Shark mission. The Dive-XL is designed for 1,000+ nautical mile autonomous undersea missions, enabling operations deep in contested Pacific maritime zones without a nearby mothership.

- **Selected:** March 2026 via DIU OTA contract
- **Range:** 1,000+ nautical miles
- **Mission:** Long-range ISR, undersea warfare, seabed mapping, forward sensor seeding
- **Payload:** Can carry "dozens" of Copperhead-100M or "multiple" Copperhead-500M — making it an autonomous undersea mothership for distributed undersea effects
- **Competition:** Boeing Orca (original XLUUV awardee) has faced significant production delays, creating the opening for Anduril

## Dive-LD

The Dive-LD is the foundational large-displacement AUV on which Ghost Shark was based. Operational with US and allied customers.

- **Length:** 5.8 meters
- **Depth rating:** 6,000 meters
- **Endurance:** 10+ days
- **Payloads:** Modular; ISR, mine countermeasures, undersea survey
- **Power:** Electrically powered

## Copperhead — Autonomous Undersea Munitions

Copperhead is a family of reusable autonomous underwater munitions that challenge the economics of legacy torpedo programs. Unlike a torpedo, Copperhead is designed to be recovered and reused when it doesn't expend itself on a target.

### Copperhead-100M
- **Diameter:** ~12.75 inches (comparable to Mk 54 lightweight torpedo diameter)
- **Class:** Lightweight torpedo equivalent
- **Speed:** 30+ knots
- **Characteristics:** Recoverable/reusable; autonomous terminal guidance

### Copperhead-500M
- **Diameter:** ~21 inches (comparable to Mk 48 heavyweight torpedo diameter)  
- **Class:** Heavyweight torpedo equivalent
- **Speed:** Broke internal speed records during April 2026 sea trials; high-agility maneuvers demonstrated in high seas
- **Characteristics:** Recoverable/reusable; significantly cheaper than Mk 48 to manufacture

### Operational Concept

The Copperhead + Dive-XL combination creates an autonomous undersea mothership concept: a Dive-XL infiltrates a contested area autonomously, loiters, seeds seabed sensors, relays data back via Lattice, and then launches distributed Copperhead effectors instead of expending one legacy torpedo per target. Multiple Copperhead-100Ms per Dive-XL means many engagements per sortie.

## Notable Developments

- **2026-04:** Copperhead-500M sea trials; speed records broken; high seas high-agility testing
- **2026-03:** Dive-XL selected by DIU/US Navy for XLUUV program
- **2025-11:** First Ghost Shark XLUUV delivered to Australian Navy
- **2025-09:** Ghost Shark enters Program of Record; 1.7B AUD ADF contract announced
- **2025-04:** Copperhead unveiled publicly
- **2025:** Ghost Shark factory opens; LFAM production begins
- **~2022–2023:** Ghost Shark R&D (~$100M total; ADF + Anduril co-funded)

## Sources

- [Breaking Defense — Ghost Shark first delivery (November 2025)](https://breakingdefense.com/2025/11/first-ghost-shark-extra-large-auv-delivered-to-australian-navy/)
- [Naval News — DIU/Navy select Anduril Dive-XL (March 2026)](https://www.navalnews.com/naval-news/2026/03/diu-and-u-s-navy-select-anduril-for-xl-auv-program/)
- [Anduril — Ghost Shark Program of Record](https://www.anduril.com/news/ghost-shark-enters-program-of-record-from-prototype-to-fleet-in-three-years)
- [Anduril — Copperhead unveiled](https://www.anduril.com/news/anduril-unveils-copperhead-a-new-era-of-autonomous-undersea-dominance)
- [The Aviationist — Copperhead-500M sea trials (April 2026)](https://theaviationist.com/2026/04/27/anduril-shows-copperhead-500m-autonomous-underwater-munitions-testing/)
- [Army Recognition — Dive-XL 1,000 nm missions](https://www.armyrecognition.com/news/navy-news/2026/u-s-navy-selects-anduril-dive-xl-autonomous-submarine-for-1-000-nautical-mile-undersea-missions)
- [Anduril — Dive-LD](https://www.anduril.com/dive-ld)
