---
title: "Persistent Systems"
date: 2026-03-31
lastmod: 2026-03-31
draft: false
description: "New York City private MANET radio company; Wave Relay waveform and MPU5 radio deployed with US Army, SOCOM, Royal Marines, and Navy unmanned surface vessel programs; primary US competitor to Silvus Technologies StreamCaster."
tags: ["robotics", "communications", "defense", "us"]
categories: ["company"]
research_area: "robotics/communications"
source_urls:
  - "https://persistentsystems.com/mpu5/"
  - "https://persistentsystems.com/uk-royal-marines-field-over-1000-persistent-systems-mpu5-handheld-networking-radios-to-support-future-commando-force/"
  - "https://persistentsystems.com/persistent-systems-awarded-5-1-million-contract-to-supply-mpu5-radios-to-usaf/"
last_reviewed: 2026-03-31
stale_after_days: 180
related: []
---

## Summary

Persistent Systems LLC is a New York City-based private company that develops and manufactures Wave Relay MANET (Mobile Ad-hoc Network) tactical communications radios. Founded in 2007 by Johns Hopkins PhD graduates Herbert Rubens and David Holmer, Persistent Systems built its Wave Relay waveform out of graduate research into distributed wireless systems. The MPU5 — its current flagship radio — is described by the company as "the world's first Smart Radio," combining MANET networking with an integrated Linux computer. MPU5 and the Wave Relay waveform are deployed with US Army, SOCOM, US Air Force, US Navy (unmanned surface vessel programs), and the UK Royal Marines, making Persistent Systems the principal US competitor to Silvus Technologies (acquired by Motorola Solutions for $4.4B in 2025) in the defense MANET radio market.

## Key Facts

- **Founded:** 2007 (New York City, NY)
- **HQ:** New York, NY
- **Type:** Private; named to Inc. 5000 fastest-growing private companies
- **Key products:** MPU5 (3×3 MIMO MANET radio with integrated computer); PT5 (Personal Transport 5, next-gen handheld)
- **Key waveform:** Wave Relay (proprietary MANET waveform; multi-hop, multi-node MIMO)
- **Export control:** ITAR (defense communications)
- **Key customers:** US Army (4th Infantry Division, CS21 ITN programs); USAF Air Mobility Command; US Navy (unmanned surface vessels); UK Royal Marines (2,000+ MPU5 deployed); USSOCOM (SOF applications)

## What It Is / How It Works

Wave Relay is a proprietary MANET waveform that enables a self-forming, self-healing wireless mesh network. Nodes discover each other, establish routes automatically, and maintain connectivity as nodes move or drop out. Unlike infrastructure-based WiFi or cellular networks, Wave Relay nodes have no dependency on a base station, access point, or tower — any node can route packets to any other through multi-hop forwarding. This architecture is essential for military operations in contested or denied communications environments.

The MPU5 is the hardware platform running Wave Relay. It is a 3×3 MIMO radio (three transmit, three receive antennas, providing spatial multiplexing to increase throughput and diversity against multipath fading). The integrated computer runs a full Linux operating system, making the MPU5 programmable as a platform rather than just a radio — operators can load applications directly onto the device to process video feeds, run autonomy software, or integrate with ATAK (Android Team Awareness Kit) for situational awareness. The device transmits at up to 10W, supports FIPS-compliant and NIAP-approved encryption (two layers), and includes Wave Relay Interference Resilience & Defense (IRD) — a DoD-assessed library of electronic attack fingerprints and countermeasures for EW resilience.

The Wave Relay ecosystem extends beyond the MPU5 itself. Persistent Systems has published a Wave Relay ecosystem program that enables third parties to build products that operate natively on the MANET — drone controllers, ground vehicle modems, and robotic platforms can integrate as Wave Relay nodes without requiring a separate radio. This "ecosystem" approach is a deliberate platform strategy: once Wave Relay becomes the communications backbone for a program (such as the UK Royal Marines), switching costs rise and adjacent applications pull in additional hardware sales.

Persistent Systems' MANET architecture for unmanned systems is technically significant: for robotic systems and drone swarms operating in GPS-denied or RF-contested environments, a resilient mesh network that can route around failed or jammed nodes is a prerequisite for coordinated autonomous operation. The US Army Robotic Combat Vehicle (RCV) program uses Persistent Systems radios for the command-and-control link between manned companion vehicles and autonomous ground robots.

## Notable Developments

- **2025-11:** UK Royal Marines fully field 2,000+ MPU5 radios as part of Future Commando Force transformation. ([Persistent Systems](https://persistentsystems.com/uk-royal-marines-field-over-1000-persistent-systems-mpu5-handheld-networking-radios-to-support-future-commando-force/))
- **2025:** PT5 (Personal Transport 5) next-generation device previewed at SOF Week; pre-trialed by US Army.
- **2024-01:** USAF Air Mobility Command contract: $5.1M for 280+ MPU5 handheld radios and 10 integrated sector antennas. ([Persistent Systems](https://persistentsystems.com/persistent-systems-awarded-5-1-million-contract-to-supply-mpu5-radios-to-usaf/))
- **2024+:** US Navy contract for MANET communications supporting unmanned surface vessel (USV) operations.
- **2024:** US Army 4th Infantry Division equipped with Wave Relay devices for NGC2 (networked battle command and control).
- **2025 context:** Competitor Silvus Technologies acquired by Motorola Solutions for $4.4B (August 2025), intensifying the competitive dynamic.
- **2007:** Company founded by Dr. Herbert Rubens and Dr. David Holmer in New York City following Johns Hopkins PhDs; Wave Relay waveform originated in undergraduate distributed systems research.

## Key People

### Dr. Herbert Rubens — Co-Founder and CEO
- **LinkedIn:** [linkedin.com/in/herbert-r-b2b7173](https://www.linkedin.com/in/herbert-r-b2b7173/)
- **Education:** Johns Hopkins University (BS, MS, PhD Computer Science, PhD completed 2002–2006; minor in Business and Entrepreneurship)
- **Career (reverse-chronological):**
  - Persistent Systems (2007–present): Co-founder and CEO
  - Self-employed computer services business (teenage): Set up office systems for local businesses (pre-university)
- **Notes:** Rubens and co-founder David Holmer developed the Wave Relay concept as undergraduates at Johns Hopkins, motivated by poor cellular coverage in their apartment building. The origin story is unusually direct from academic frustration to defense technology product. Rubens holds expert status in mobile ad hoc wireless networking and distributed systems.

### Dr. David Holmer — Co-Founder
- **LinkedIn:** Not found (no confirmed public profile)
- **Education:** Johns Hopkins University (PhD Computer Science)
- **Career (reverse-chronological):**
  - Persistent Systems (2007–present): Co-founder
- **Notes:** Co-inventor of the original Wave Relay waveform alongside Rubens.

### People — Last Reviewed: 2026-03-31

## Supply Chain Position

Persistent Systems operates at the **Component/Subsystem Supplier** layer, selling radios and waveform solutions to defense prime contractors, unmanned systems integrators, and directly to military end-users. The MPU5 hardware is manufactured by contract; the Wave Relay waveform software is the core proprietary asset. The integrated Linux computer inside the MPU5 creates a software platform opportunity that Silvus (with its more traditional radio-only approach to the SC4200/4400) has historically not pursued to the same degree. **⚑ Competitive overlap:** Silvus Technologies (Motorola Solutions) is the direct competitor on virtually all the same DoD MANET programs; in some programs, both radios are evaluated head-to-head; in others, one has been selected as the standard.

## Claim Verification

### Claim: MPU5 is "the world's first Smart Radio" with integrated computer capabilities
**Status:** Partially verified

**Supporting sources:**
- [MPU5 Overview — Persistent Systems](https://persistentsystems.com/mpu5/) — Company describes integrated Linux OS computer inside the radio; ATAK support, programmable applications, video encoding confirmed in product documentation
- The concept of a compute-capable radio is technically distinct from conventional tactical radios (e.g., Harris AN/PRC-117) that perform only radio functions; the integrated computer enabling edge application execution is a genuine differentiator

**Refuting / questioning sources:**
- "World's first" is a marketing claim that is difficult to independently verify and is contested by other software-defined radio (SDR) developers; other SDR platforms (GNU Radio-based systems) also run software on embedded processors, though the MPU5's integrated operational design is more mature and purpose-built for field use

**Summary:** The integrated computer and application-layer programmability are genuine capabilities; whether MPU5 was literally the "first" such product is a marketing claim that cannot be independently verified.

## Sources

- [MPU5 Overview — Persistent Systems](https://persistentsystems.com/mpu5/)
- [MPU5 Technical Specifications — Persistent Systems](https://persistentsystems.com/mpu5-specs/)
- [UK Royal Marines Field 2,000+ MPU5 — Persistent Systems (Nov 2025)](https://persistentsystems.com/uk-royal-marines-field-over-1000-persistent-systems-mpu5-handheld-networking-radios-to-support-future-commando-force/)
- [USAF Air Mobility Command $5.1M Contract — Persistent Systems](https://persistentsystems.com/persistent-systems-awarded-5-1-million-contract-to-supply-mpu5-radios-to-usaf/)
- [Persistent Systems Company History](https://persistentsystems.com/persistent-systems-history/)
- [Herbert Rubens LinkedIn](https://www.linkedin.com/in/herbert-r-b2b7173/)
