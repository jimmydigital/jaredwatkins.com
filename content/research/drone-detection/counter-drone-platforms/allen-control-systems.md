---
title: "Allen Control Systems — Bullfrog Autonomous Weapon Station"
date: 2026-06-05
lastmod: 2026-06-05
draft: false
description: "Allen Control Systems (Austin, TX) builds the Bullfrog autonomous AI-guided weapon station — converts legacy machine guns into kinetic counter-drone systems. SOCOM contract awarded Sept 2025. $200M Series B at $2.2B valuation, June 2026."
research_area: "drone-detection/counter-drone-platforms"
source_urls:
  - "https://www.allencontrolsystems.com/products/bullfrog-m240"
  - "https://www.businesswire.com/news/home/20260526638233/en/Allen-Control-Systems-Raises-$200-Million-Series-B-at-$2.2-Billion-Post-Money-Valuation-to-Scale-Manufacturing-and-Accelerate-Deployment-of-Bullfrog"
  - "https://www.businesswire.com/news/home/20250925355643/en/Allen-Control-Systems-Awarded-Contract-With-Maritime-U.S.-Special-Operations-Forces-Unit"
  - "https://www.defenseone.com/business/2025/09/socom-get-robotic-anti-drone-tech-maritime-platforms/408418/"
  - "https://www.businesswire.com/news/home/20260223792790/en/Allen-Control-Systems-Triples-Austin-Operations-to-Meet-Demand-for-Bullfrog-Autonomous-Counter-Drone-Systems"
  - "https://www.businesswire.com/news/home/20251216968418/en/Allen-Control-Systems-Selected-by-U.S.-Army-Applications-Lab-for-Combat-Vehicle-Integration-Readiness Plan"
  - "https://fortune.com/2025/03/27/gun-turret-startup-allen-control-systems-series-a-venture-capital-defense-tech/"
last_reviewed: 2026-06-05
stale_after_days: 60
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Allen Control Systems (ACS) is an Austin, Texas defense startup building the **Bullfrog**, an AI-powered autonomous weapon station that attaches to standard legacy machine guns (M240, M2, M230, M134) and converts them into autonomous counter-drone systems. The platform uses computer vision, AI, and a sensor suite to detect, track, classify, and engage Groups 1–3 UAVs — requiring only a human command to fire. ACS is the highest-profile kinetic C-UAS startup in the US as of mid-2026, with active SOCOM and Army contracts and a $2.2B valuation following a $200M Series B closed June 2026.

## Key Facts

- **Headquarters:** Austin, Texas
- **Founded:** ~2022
- **Stage:** Series B — $200M raised June 2026 at $2.2B post-money valuation (led by Smash Capital; Craft Ventures, Rally Ventures, Inspired Capital)
- **Prior raise:** $30M Series A, March 2025 (Craft Ventures lead)
- **Contracts:** SOCOM maritime (Sept 2025, via ManTech); US Army AAL combat vehicle integration ($1.5M + up to $4.5M options, Dec 2025); South Korea and UAE customers
- **Facility:** 57,000+ sq ft Austin facility (tripled Feb 2026)
- **System:** Bullfrog autonomous weapon station — M240, M2, M230, M134 variants
- **Claimed cost-per-kill:** ~$10 in ammunition (vs. $400K–$1M per SAM intercept)
- **Fielding status:** Operational — SOCOM maritime deployment confirmed; Army combat vehicle integration testing ongoing

## What It Is

Bullfrog is a modular robotic weapon mount — not a new gun, but a robotic sleeve and sensor package that attaches to existing military-standard machine guns. The mount adds:

- Electro-optical (EO) and infrared (IR) cameras
- Laser rangefinder
- AI-driven computer vision trained on a large drone imagery dataset
- Autonomous target detection, classification, tracking, and fire control
- Human-on-the-loop design: the system autonomously acquires and tracks but fires only on operator command

The AI calculates target size, speed, distance, and predicted future position, then drives the mount to track and lead the target. The operator sees the track and authorizes engagement with a single command. No manual aiming required.

## Variants

| Variant | Gun | Primary Use |
|---------|-----|-------------|
| Bullfrog M240 | M240 7.62mm | Ground and maritime C-UAS |
| Bullfrog M2 | M2 .50 cal | Larger UAS, longer range |
| Bullfrog M230 | M230 30mm | Heavy UAS / hardened targets |
| Bullfrog M134 | M134 Minigun | High-rate suppression |

Also supports non-kinetic payloads (laser dazzler variant documented).

## Threat Coverage

Groups 1–3 UAVs per DoD classification:
- **Group 1:** Small UAS under 20 lbs (FPV drones, consumer quadcopters)
- **Group 2:** Medium UAS 21–55 lbs
- **Group 3:** Large UAS 55–1,320 lbs

Group 1 FPV drones are the primary operational threat in Ukraine-influenced scenarios. The Bullfrog engages targets from close range through several hundred meters depending on gun variant.

## Deployment Configurations

- **Fixed site:** Mounted on a post or structure for perimeter defense of a fixed installation
- **Vehicle-mounted:** Integration onto Humvee, JLTV, Stryker, Bradley, and other combat vehicles (Army AAL contract scope)
- **Maritime:** Mounted on SOF watercraft (SOCOM contract scope)

## Fielding Status (as of June 2026)

**Confirmed deployed:** ACS confirmed the system is "in the fight" following the SOCOM maritime contract award in September 2025. The company does not publicly disclose specific operational locations.

**In testing:** US Army Applications Lab selected ACS in December 2025 for a Combat Vehicle Integration Readiness Plan — integration across five Army combat vehicle platforms. Live testing with 1st Cavalry Division soldiers was scheduled for October 2026.

**International customers:** South Korea and UAE named as production customers following the February 2026 facility expansion.

**Demonstrated at:** DoD T-REX 2024 (Camp Atterbury, Indiana); Pentagon demonstration; White House demonstration.

## Why Kinetic Matters for Fiber-Optic Threats

Bullfrog is notable in the C-UAS space precisely because it is immune to the countermeasures that have rendered RF-based systems irrelevant against fiber-optic FPV drones. Since it detects via EO/IR and radar (not RF spectrum analysis) and defeats via physical projectile (not jamming), it works against:

- Fiber-optic FPV drones (no RF to jam or detect; physical destruction still works)
- Autonomous/pre-programmed drones (no operator signal; still trackable by radar/optical)
- RF-controlled drones (standard threat; straightforward engagement)

The claimed ~$10 cost-per-kill also addresses the fundamental economic asymmetry problem that has made SAM-based defense unsustainable at scale — the math works even against $200–$500 commercial FPV drones.

## Limitations and Open Questions

- **Urban/civilian context:** Gun-based kinetic C-UAS has significant collateral risk in populated areas — falling ammunition and drone debris are real concerns. Suitable for military/remote critical infrastructure, not urban settings.
- **Rate of fire vs. swarms:** A single Bullfrog mount can engage one target at a time. Against large coordinated swarms (dozens of simultaneous inbound FPV drones), multiple units or complementary countermeasures would be required.
- **Engagement range:** Effective range is limited by the gun caliber and the size of Group 1 FPV drones — these are small, fast targets. Precise effective range vs. FPV drones not publicly confirmed.
- **Legal/authorization (US civilian):** In the US civilian context, deploying any kinetic weapon against UAS (even for critical infrastructure protection) requires careful legal review. The Bullfrog is marketed to DoD/government; its deployment at private critical infrastructure would require legal analysis under federal aviation law.
- **Integration complexity:** Not a plug-and-play system — requires operator training, maintenance, and integration into a broader C2 architecture.

## Funding and Company Status

| Round | Date | Amount | Lead |
|-------|------|--------|------|
| Seed | ~2023 | Undisclosed | Inspired Capital, Rally Ventures |
| Series A | March 2025 | $30M | Craft Ventures |
| Series B | June 2026 | $200M | Smash Capital |

Post-Series B valuation: $2.2B. The company tripled its Austin facility to 57,000+ sq ft in February 2026, ahead of the Series B.

## Sources

- [ACS Product Page: Bullfrog M240](https://www.allencontrolsystems.com/products/bullfrog-m240)
- [Business Wire: ACS Raises $200M Series B at $2.2B Valuation (June 2026)](https://www.businesswire.com/news/home/20260526638233/en/Allen-Control-Systems-Raises-$200-Million-Series-B-at-$2.2-Billion-Post-Money-Valuation-to-Scale-Manufacturing-and-Accelerate-Deployment-of-Bullfrog)
- [Business Wire: SOCOM Maritime Contract Award (Sept 2025)](https://www.businesswire.com/news/home/20250925355643/en/Allen-Control-Systems-Awarded-Contract-With-Maritime-U.S.-Special-Operations-Forces-Unit)
- [Defense One: SOCOM to get robotic anti-drone turret for maritime platforms](https://www.defenseone.com/business/2025/09/socom-get-robotic-anti-drone-tech-maritime-platforms/408418/)
- [Business Wire: ACS Triples Austin Operations (Feb 2026)](https://www.businesswire.com/news/home/20260223792790/en/Allen-Control-Systems-Triples-Austin-Operations-to-Meet-Demand-for-Bullfrog-Autonomous-Counter-Drone-Systems)
- [Fortune: Gun turret startup ACS raises $30M Series A (March 2025)](https://fortune.com/2025/03/27/gun-turret-startup-allen-control-systems-series-a-venture-capital-defense-tech/)
