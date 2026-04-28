---
title: "Silvus Technologies"
date: 2026-03-31
lastmod: 2026-03-31
draft: false
description: "Los Angeles MIMO MANET radio developer for defense and unmanned systems; StreamCaster radios are the dominant waveform on US Army Integrated Tactical Network programs; acquired by Motorola Solutions for $4.4B in August 2025."
tags: ["robotics", "communications", "defense", "us"]
categories: ["company"]
research_area: "robotics/communications"
source_urls:
  - "https://www.motorolasolutions.com/newsroom/press-releases/motorola-solutions-completes-acquisition-of-silvus-technologies.html"
  - "https://breakingdefense.com/2025/05/motorola-solutions-to-acquire-defense-radio-maker-silvus-technologies-for-4-4-billion/"
  - "https://silvustechnologies.com/products/streamcaster-radios/"
last_reviewed: 2026-03-31
stale_after_days: 180
related: []
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Silvus Technologies is a Los Angeles, California developer of software-defined MIMO MANET (Mobile Ad-hoc Network) tactical radios for defense, autonomous systems, and public safety. Founded in 2004 by UCLA EE Professor Babak Daneshrad, Silvus developed the StreamCaster radio family around a proprietary MN-MIMO waveform that enables multi-hop mesh networking without fixed infrastructure. StreamCaster radios are deployed across US Army, Marine Corps, and Special Operations programs including the Army Integrated Tactical Network (ITN), Integrated Visual Augmentation System (IVAS), and Robotic Combat Vehicle programs. Silvus was acquired by Motorola Solutions for $4.4 billion in August 2025 (with up to $600M in earnouts), making it Motorola Solutions' largest acquisition and its strategic entry into the defense unmanned systems communications market.

## Key Facts

- **Founded:** 2004 (Los Angeles, CA)
- **HQ:** Los Angeles, CA
- **Type:** Subsidiary of Motorola Solutions (NYSE: MSI) since August 2025; formerly private, backed by TJC (private equity)
- **Acquisition:** Motorola Solutions closed acquisition August 6, 2025; $4.4B up-front cash + up to $600M earnout based on 2027–2028 performance (total up to $5B)
- **Prior PE backer:** TJC (formerly The Jordan Company)
- **Key products:** StreamCaster 4200 Enhanced Plus (SC4200EP, 2×2 MIMO); StreamCaster 4400 Enhanced (SC4400E, 4×4 MIMO); StreamCaster 4400 XTREME (latest extended-range variant)
- **Key waveform:** MN-MIMO (proprietary multi-node MIMO MANET waveform)
- **Export control:** ITAR (defense radio; International Traffic in Arms Regulations); international military sales require US government approval

## What It Is / How It Works

MANET (Mobile Ad-hoc Network) radios create a mesh network without relying on a fixed base station or satellite link. Each radio acts simultaneously as a node and a router: it communicates with nearby radios, and packets hop through the mesh to reach any other node, even if they are not in direct line of sight. As nodes move, the routing topology updates automatically. This makes MANET ideal for military operations where infrastructure is unavailable or destroyed, and for UAS swarms where individual aircraft may drop in and out of the network.

Silvus' core innovation is MN-MIMO — the application of Multi-Node MIMO (Multiple Input Multiple Output) to MANET operation. Standard MIMO uses multiple antennas on a single transceiver to increase throughput and reliability on a single link. Silvus extended this concept to work across multiple independent nodes in a mesh: nodes cooperatively form virtual MIMO pairs, using spatial multiplexing to increase data rate and spatial diversity to improve robustness against jamming and multipath interference. This approach provides significantly better spectral efficiency and electronic warfare (EW) resilience than single-antenna MANET designs.

StreamCaster 4200 Enhanced Plus (2×2 MIMO): Operates across 300 MHz–6 GHz tunable; up to 100 Mbps throughput; 10W transmit power (20W effective with TX Eigen Beamforming); 7 ms average latency; suitable for small UAS, soldier-wearable, and dismounted applications due to compact size. StreamCaster 4400 Enhanced (4×4 MIMO): 20W transmit power (80W effective with TX Eigen Beamforming); dual-band operation; 100 Mbps throughput; designed for vehicle-mounted, fixed infrastructure, and airborne platforms where more antenna aperture is available. Both radios support simultaneous data, voice, and video streaming.

The US Army has integrated Silvus into multiple major programs. In Capability Set '21 (CS21) of the Army Integrated Tactical Network (ITN), Silvus was selected as the MANET node radio for the dismounted soldier and small vehicle tiers. The Army's Antenna Integrated Radio System (AIRS) contract for the Integrated Battle Command System (IBCS) netted Silvus a $35M directed procurement through Northrop Grumman. For IVAS (the Microsoft HoloLens-based augmented reality headset for soldiers), Silvus provides the radio backbone enabling data sharing between squads. Robotic Combat Vehicles (RCVs) use Silvus radios for remote control and telemetry links.

Motorola Solutions' acquisition rationale is straightforward: Silvus' customer base is overwhelmingly US government and allied military, Motorola Solutions already has a large government radio division (APX mission-critical radios for law enforcement), and the combination creates a single-vendor end-to-end communications supplier across the law enforcement to defense spectrum. The $4.4B price reflects a substantial multiple on Silvus' revenue, underscoring the strategic premium Motorola paid.

## Notable Developments

- **2025-08:** Motorola Solutions completes acquisition of Silvus Technologies for $4.4B; Silvus becomes a Motorola Solutions business unit. ([Motorola Solutions](https://www.motorolasolutions.com/newsroom/press-releases/motorola-solutions-completes-acquisition-of-silvus-technologies.html))
- **2025-05:** Motorola Solutions announces definitive agreement to acquire Silvus for $4.4B ($4.38B cash + ~$20M restricted stock); TJC announces sale with up to $5B total including earnouts. ([BusinessWire](https://www.businesswire.com/news/home/20250527272447/en/Motorola-Solutions-to-Acquire-Silvus-Technologies-a-Global-Leader-in-Mission-Critical-Mobile-Ad-hoc-Networks))
- **2023:** US Army IBCS Integrated Battle Command System — Silvus AIRS contract directed through Northrop Grumman, valued at ~$35M. ([PR Newswire](https://www.prnewswire.com/news-releases/us-army-selects-silvus-antenna-integrated-radio-system-for-integrated-battle-command-system-301876207.html))
- **2021:** US Army Capability Set '21 — Silvus adopted for Integrated Tactical Network as MANET radio. ([PR Newswire](https://www.prnewswire.com/news-releases/us-army-adopts-silvus-for-integrated-tactical-network-capability-set-21-301143968.html))
- **2020:** US Marine Corps selects Silvus StreamCaster 4400 for Joint Light Tactical Vehicle (JLTV) and Amphibious Combat Vehicle (ACV) networking; ~$5M contract. ([Shephard Media](https://www.shephardmedia.com/news/landwarfareintl/us-marine-corps-selects-silvus-radios-for-ground-vehicle-comms/))
- **2004:** Company founded by Babak Daneshrad, commercializing UCLA MIMO research.

## Key People

### Dr. Babak Daneshrad — Founder and CEO
- **LinkedIn:** [linkedin.com/in/babak-daneshrad-8911381](https://www.linkedin.com/in/babak-daneshrad-8911381/)
- **Education:** McGill University (MS Engineering, Communications, 1988); UCLA (PhD Electrical Engineering, 1993)
- **Career (reverse-chronological):**
  - Silvus Technologies (2004–present): Co-founder and CEO
  - UCLA (1996–2019): Professor, Electrical Engineering Department; Professor Emeritus from November 2019
  - Inovonics (co-founder; raised $14M VC to develop first multi-antenna WCDMA-3G ASIC)
  - AT&T Bell Labs: Broadband wireless communications research
- **Notes:** Named IEEE Communications Society Distinguished Industry Leader (2025). Daneshrad's direct pipeline from UCLA EE research to Silvus commercialization is the archetype of a defense tech spinout: foundational MIMO research performed in an academic lab, then productized specifically for military applications where cost sensitivity is lower than consumer markets.

### People — Last Reviewed: 2026-03-31

## Supply Chain Position

Silvus operates at the **Component/Subsystem Supplier** layer (selling radios to military prime contractors, autonomous systems integrators, and drone manufacturers) and increasingly as a **Software/AI layer** player (selling waveform technology and software integration to OEM partners). Its MN-MIMO waveform is the key proprietary element; hardware is assembled from commercial-off-the-shelf RF components but the software-defined waveform is what creates competitive differentiation and ITAR classification. **⚑ Competitive overlap:** Persistent Systems MPU5 (Wave Relay waveform) is the primary direct competitor in the US defense MANET market; both radios compete for the same Army and SOCOM programs.

## Claim Verification

### Claim: MN-MIMO provides "unmatched range, data throughput, EW resiliency, and scalability" for MANET
**Status:** Partially verified

**Supporting sources:**
- [US Army ITN CS21 adoption — PR Newswire](https://www.prnewswire.com/news-releases/us-army-adopts-silvus-for-integrated-tactical-network-capability-set-21-301143968.html) — Army selection implies successful competitive evaluation against alternatives
- [IBCS AIRS contract — PR Newswire](https://www.prnewswire.com/news-releases/us-army-selects-silvus-antenna-integrated-radio-system-for-integrated-battle-command-system-301876207.html) — Directed procurement suggests sole-source or best-value determination

**Refuting / questioning sources:**
- Persistent Systems claims comparable or superior specifications for its MPU5 with Wave Relay waveform; independent head-to-head public testing data comparing MANET radios under EW/jamming conditions is not publicly available for either product

**Summary:** The claim is commercially substantiated by major US Army program wins against a competitive field; the "unmatched" superlative cannot be independently verified due to classified test environments and competing vendor claims from Persistent Systems.

## Sources

- [Motorola Solutions Completes Acquisition of Silvus — Motorola Solutions (Aug 2025)](https://www.motorolasolutions.com/newsroom/press-releases/motorola-solutions-completes-acquisition-of-silvus-technologies.html)
- [Motorola to Acquire Silvus for $4.4B — Breaking Defense (May 2025)](https://breakingdefense.com/2025/05/motorola-solutions-to-acquire-defense-radio-maker-silvus-technologies-for-4-4-billion/)
- [TJC Sale Announcement — BusinessWire (May 2025)](https://www.businesswire.com/news/home/20250527013806/en/TJC-Announces-Sale-of-Silvus-Technologies-to-Motorola-Solutions-Inc.-for-up-to-$5.0-Billion)
- [StreamCaster Products — Silvus Technologies](https://silvustechnologies.com/products/streamcaster-radios/)
- [US Army ITN CS21 Adoption — PR Newswire](https://www.prnewswire.com/news-releases/us-army-adopts-silvus-for-integrated-tactical-network-capability-set-21-301143968.html)
- [US Army IBCS AIRS Contract — PR Newswire](https://www.prnewswire.com/news-releases/us-army-selects-silvus-antenna-integrated-radio-system-for-integrated-battle-command-system-301876207.html)
- [Babak Daneshrad LinkedIn](https://www.linkedin.com/in/babak-daneshrad-8911381/)
