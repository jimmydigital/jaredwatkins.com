---
title: "Sentrycs"
date: 2026-06-05
lastmod: 2026-06-05
draft: false
description: "Israeli C-UAS company specializing in Cyber-over-RF (protocol manipulation) counter-drone technology — detects, identifies, and mitigates unauthorized drones without jamming. Acquired by Ondas Holdings (NASDAQ:ONDS) for ~$200M in November 2025."
tags: ["c-uas", "counter-drone", "rf-detection", "cyber-over-rf", "israel", "critical-infrastructure", "commercial-legal"]
categories: ["company"]
research_area: "drone-detection/hardware"
source_urls:
  - "https://sentrycs.com/"
  - "https://ir.ondas.com/press-releases/detail/256/ondas-completes-acquisition-of-sentrycs-a-global-leader-in"
  - "https://sentrycs.com/news/sentrycs-unveils-horizon-a-revolutionary-self-learning-counter-drone-engine/"
  - "https://sentrycs.com/news/sentrycs-unveils-version-6-0-of-its-counter-drone-software-delivering-unmatched-coverage-and-efficiency/"
  - "https://dronelife.com/2026/02/17/sentrycs-scout-expands-counter-drone-capabilities-for-law-enforcement/"
  - "https://dronexl.co/2026/05/18/sentrycs-scout-rf-counter-drone/"
  - "https://sentrycs.com/news/sentrycs-wins-the-2025-army-technology-innovation-award-for-groundbreaking-counter-uas-technology/"
  - "https://ir.ondas.com/press-releases/detail/281/ondas-sentrycs-secures-german-state-police-contract-to"
last_reviewed: 2026-06-05
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Sentrycs is an Israeli counter-drone technology company whose core differentiator is Cyber-over-RF (CoRF): protocol-layer analysis and manipulation of the radio communications between a drone and its operator. This approach identifies drones down to serial number, locates operators, and — where legally authorized — takes control of the drone without broadband jamming. Sentrycs was acquired by Ondas Holdings (NASDAQ:ONDS) for approximately $200 million in November 2025.

## Key Facts

- **Founded:** 2017 (as Convexum Ltd; rebranded Sentrycs)
- **HQ:** Israel (with international subsidiaries)
- **Type:** Company — C-UAS hardware and software
- **Status:** Active (subsidiary of Ondas Holdings as of Nov 2025)
- **Parent:** [Ondas Holdings](https://ondas.com) (NASDAQ: ONDS)
- **Acquisition price:** ~$200M (cash + stock)
- **Customers:** 25+ countries; tier-1 defense and security agencies
- **2025 Army Technology Innovation Award:** Winner for counter-UAS technology
- **Key technology:** Cyber-over-RF (CoRF) protocol manipulation — not a jammer

## What It Is / How It Works

Sentrycs operates at the protocol layer of drone-to-controller communications rather than the physical RF layer. Conventional RF detectors identify the presence of radio signals; Sentrycs decodes the communication protocol at the bit level and extracts structured data: drone serial number, model, operator position, flight mode, and active frequencies. This yields richer situational awareness than signal-power-based approaches and dramatically reduces false positives from non-drone RF sources.

The mitigation capability — taking control of the drone — works via the same protocol channel. Because Sentrycs injects commands in the drone's own protocol rather than blanket-jamming the spectrum, it avoids the legal and collateral issues associated with jamming. It also allows soft landing of an intercepted drone rather than a crash. In most jurisdictions (including the US), this "cyber takeover" mitigation is only lawfully usable by federal agencies; commercial operators at critical infrastructure may use Sentrycs for detection and identification only.

**Horizon engine (launched early 2025):** Sentrycs' AI-powered extension to CoRF that handles drone types not in the protocol library. Horizon analyzes the RF environment for signal patterns characteristic of drone-controller datalinks (burst timing, frequency behavior, modulation type) and builds a real-time model of unknown protocols. This makes it the first non-library-dependent CoRF system — meaningful given the proliferation of custom/DIY drones and rapid firmware evolution by adversarial operators.

## Products

### Core System (Fixed/Mobile)

The primary Sentrycs platform is a rack-mounted sensor and software system deployable at fixed sites or on vehicles. It integrates omnidirectional antenna arrays, CoRF processing hardware, and the Sentrycs software suite. Version 6.0 (June 2025) extended mitigation range to a 10-kilometer diameter.

**Capabilities:**
- Passive detection, tracking, and identification of RF-transmitting drones
- Drone serial number extraction and model identification
- Operator location estimation via signal analysis
- Mitigation (cyber takeover or forced landing) for authorized deployments
- Integration with third-party sensor fusion platforms via API

**Limitations:** Blind to RF-dark threats (fiber-optic FPV, pre-programmed autonomous, GPS-waypoint-only drones with no active control link). These require radar or acoustic layers.

### Sentrycs Scout (launched early 2026)

A compact, battery-powered portable version of the CoRF system for tactical and mobile deployments. Designed for:
- Law enforcement operations (event security, VIP protection)
- Convoy security
- Border enforcement
- Infrastructure patrol

Scout delivers detect/track/identify/mitigate in a man-portable form factor without requiring fixed infrastructure.

### Horizon Engine

AI-based protocol analysis extension available as a software module on both the core system and Scout. Handles analog, digital, and video transmission types including DIY and custom drone protocols not in the signature library.

## Notable Developments

- **2026-05:** Sentrycs Scout commercially available; marketed to law enforcement and infrastructure patrol
- **2026-02:** Sentrycs delivers C-UAS system to German State Police department
- **2025-11:** Ondas Holdings completes acquisition of Sentrycs for ~$200M
- **2025-06:** Software version 6.0 released; mitigation range extended to 10 km diameter
- **2025-01:** Horizon self-learning counter-drone engine unveiled; first non-library-based CoRF system
- **2025:** Won 2025 Army Technology Innovation Award for counter-UAS technology
- **Pre-2025:** Systems deployed with tier-1 defense and security agencies in 25+ countries; integrated into Rafael Drone Dome system

## Integration with Rafael Drone Dome

Sentrycs' CoRF technology is integrated into [Rafael Advanced Defense Systems](https://www.rafael.co.il)' Drone Dome layered C-UAS system. Drone Dome combines radar, EO/IR, laser effectors, and RF jamming; Sentrycs adds protocol-layer cyber takeover as an alternative to jamming for environments where spectrum management is critical.

## Integration with Ondas Iron Drone Raider

Following acquisition, Ondas is integrating Sentrycs' CoRF capability with its Iron Drone Raider autonomous interceptor drone. The architecture combines Sentrycs' electronic identification and control channel with Iron Drone's physical interception capability — targeting and cyber takeover before physical engagement.

## Claim Verification

### Claim: 10 km mitigation range (v6.0)
**Status:** Unverified (company-stated)

**Supporting sources:**
- [Sentrycs v6.0 announcement](https://sentrycs.com/news/sentrycs-unveils-version-6-0-of-its-counter-drone-software-delivering-unmatched-coverage-and-efficiency/) — company press release stating 10 km diameter coverage

**Refuting / questioning sources:**
- No independent third-party validation found. RF mitigation range is highly environment-dependent (urban vs. open terrain, RF noise floor, drone transmit power).

**Summary:** Range claim is company-stated; no independent measurement available. Treat as maximum under ideal conditions.

### Claim: Protocol-layer identification to serial number without jamming
**Status:** Partially verified

**Supporting sources:**
- [Cyber Over RF blog](https://sentrycs.com/the-counter-drone-blog/cyber-over-rf-the-future-of-counter-drone-technology-is-already-here/) — technical description of protocol analysis approach
- Rafael integration confirms the technology works at scale in operational deployments

**Refuting / questioning sources:**
- Effectiveness depends on drone manufacturer supporting known protocols. DIY, modified, or firmware-updated drones may fall outside the library — Horizon addresses this but remains proprietary and unaudited.

**Summary:** Technology approach is credible and operationally deployed; serial-number-level identification works for supported commercial drone protocols; coverage of adversarial custom drones depends on Horizon AI performance.

## Key People

- **Tal Cohen** — Founder and CTO, Sentrycs Ltd. LinkedIn: not found (searching returns multiple profiles; not confirmed)
- **Eric Brock** — Chairman and CEO, Ondas Holdings (parent company). [LinkedIn](https://www.linkedin.com/in/ericbrock/)
- **Oshri Lugassy** — Co-CEO, Ondas Autonomous Systems

### People — Last Reviewed: 2026-06-05

## Sources

- [Sentrycs official site](https://sentrycs.com/) — product descriptions and technology overview
- [Ondas acquisition completion press release](https://ir.ondas.com/press-releases/detail/256/ondas-completes-acquisition-of-sentrycs-a-global-leader-in) — acquisition terms and background
- [Horizon announcement](https://sentrycs.com/news/sentrycs-unveils-horizon-a-revolutionary-self-learning-counter-drone-engine/) — AI engine launch details
- [Version 6.0 announcement](https://sentrycs.com/news/sentrycs-unveils-version-6-0-of-its-counter-drone-software-delivering-unmatched-coverage-and-efficiency/) — range extension claim
- [Scout launch (DroneLife)](https://dronelife.com/2026/02/17/sentrycs-scout-expands-counter-drone-capabilities-for-law-enforcement/) — portable system for law enforcement
- [Scout specs (DroneXL)](https://dronexl.co/2026/05/18/sentrycs-scout-rf-counter-drone/) — Scout commercial launch details
- [2025 Army Innovation Award](https://sentrycs.com/news/sentrycs-wins-the-2025-army-technology-innovation-award-for-groundbreaking-counter-uas-technology/) — award citation
- [German State Police contract](https://ir.ondas.com/press-releases/detail/281/ondas-sentrycs-secures-german-state-police-contract-to) — European customer deployment
- [Haaretz: $200M acquisition](https://www.haaretz.com/israel-news/tech-news/2025-11-04/ty-article/.premium/u-s-defense-tech-firm-ondas-buys-israeli-drone-interception-company-sentrycs-for-200m/0000019a-4f2f-d5d0-a59f-6f6f3b7e0000) — acquisition valuation
