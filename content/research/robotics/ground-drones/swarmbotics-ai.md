---
title: "Swarmbotics AI"
date: 2026-08-27
lastmod: 2026-08-27
draft: false
description: "Phoenix, AZ defense robotics startup building attritable ground robot swarms; FireAnt anti-armor UGV and HaulAnt hybrid-electric platform under the ANTS system; $4M pre-seed (2024); selected for US Army Transformation in Contact program with 1st Cavalry Division (Feb 2026)."
research_area: "robotics/ground-drones"
source_urls:
  - "https://www.swarmbotics.ai/"
  - "https://techcrunch.com/2024/08/19/swarmbiotics-founders-grew-obsessed-with-robot-swarms-and-now-plan-to-bring-them-to-the-battlefield/"
  - "https://interestingengineering.com/military/us-tank-hunting-robots"
  - "https://builtin.com/company/swarmbotics-ai/jobs"
  - "https://dtvc.substack.com/p/defense-tech-spotlight-swarmbotics"
  - "https://lmnt.vc/portfolio-swarmbotics-ai"
  - "https://www.trysignalbase.com/news/funding/swarmbotics-ai-secures-4-million-in-pre-seed-funding-to-revolutionize-industry-and-defense-robotics"
  - "https://thedefensepost.com/2026/02/09/swarmbotics-us-army/"
  - "https://armyrecognition.com/news/army-news/2025/u-s-army-tests-fireant-anti-tank-ground-robot-to-detect-track-and-neutralize-armored-vehicles"
  - "https://thedefensepost.com/2025/11/05/robots-wheels-tanks-swarms/"
  - "https://defence-blog.com/u-s-army-selects-swarmbotics-ai-for-autonomous-robot-swarms/"
  - "https://www.govintel.ai/companies/az/swarmbotics-ai-inc-1837152"
  - "https://www.calibredefence.co.uk/swarmbotics-ai-why-the-us-army-is-betting-on-robotic-mass/"
last_reviewed: 2026-08-27
stale_after_days: 90
related: []
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Swarmbotics AI is a Phoenix, Arizona defense robotics startup building low-cost, "attritable" ground robot swarms for the US military. Founded in 2023 by former Cruise/AWS executive Stephen Houghton and ex-CIA/JPL engineer Drew Watson, the company's ANTS system pairs a small anti-armor platform (FireAnt) and a larger hybrid-electric utility platform (HaulAnt) with a shared autonomy and swarm-control software stack (ANTSNet). In February 2026 the US Army selected Swarmbotics AI to develop swarming small unmanned ground vehicles (sUGVs) with the 1st Cavalry Division under its Transformation in Contact program, following the company's performance at the Army's xTechOverwatch competition.

## Key Facts

- **Founded:** 2023 (research and prototyping began summer 2023)
- **HQ:** Phoenix, AZ
- **Type:** Private
- **Value chain position:** Platform OEM (vertically integrated hardware + autonomy/swarm software)
- **Key backers:** Quiet Capital, Silent Ventures, LMNT Ventures, Soma Capital — approximately $4 million pre-seed, disclosed August 2024
- **Federal contracts:** $2.0 million in disclosed DoD prime contract value across 2 awards as of this review, including a Direct-to-Phase-II SBIR award under Topic A254-P030 (xTechOverwatch Open Topic)
- **Key products:** FireAnt (small anti-armor sUGV), HaulAnt (larger hybrid-electric utility UGV), ANTSNet (swarm autonomy software stack)
- **Employees:** 11 as of mid-2024, growing to approximately 20 as of this review
- **Defense/dual-use:** Active DoD SBIR and Army xTechOverwatch/Transformation in Contact engagement; no public indication of ITAR/EAR export status

## What It Is / How It Works

Swarmbotics AI builds ground robots designed to be cheap enough to lose. The company's stated philosophy — in CEO Stephen Houghton's words, achieving "mass" by fielding "swarms of heterogeneous small sUGVs" at "fractions of the cost of exquisite platforms" — targets a market segment distinct from expensive, exquisite unmanned systems: robots built from largely commercial off-the-shelf components (including hybrid-electric ATV bases) fitted with autonomy kits, designed to absorb losses in combat rather than avoid them entirely.

The product line sits under an umbrella the company calls ANTS (Attritable, Networked, Tactical Swarm). FireAnt is the smaller of the two platforms: a low-silhouette, tracked, hybrid-electric UGV weighing under 90 kg and just over a meter long, built to detect, track, and engage armored vehicles. It carries an infrared/electro-optical sensor package with laser rangefinding and a neural-processing unit for onboard vehicle-signature recognition, plus inertial navigation for GPS-degraded environments. Reported payload options include loitering munitions, explosively formed penetrator (EFP) devices, and a lightweight recoilless-rifle-class weapon comparable to the M72 LAW, aimed at side and rear armor rather than frontal armor. HaulAnt is the larger platform in the family, described as a hybrid-electric autonomous ATV-class vehicle intended for resupply, ISR, electronic warfare, and casualty-evacuation payloads.

Both platforms run on ANTSNet, the company's autonomy and swarm-coordination software, which the company describes as including a web-based control application, ATAK integration for tactical situational awareness, and "triple redundant comms." In field demonstrations, a single operator has directed groups of up to 6 to 8 units over a decentralized, peer-to-peer mesh network, with the robots coordinating spacing, fields of fire, and engagement prioritization with reduced direct human control. The platforms are also reported to integrate with ROS 2 and JAUS architectures for broader defense interoperability, and are built to IP67 ruggedization standards.

The company's most public validation to date came via the Army's xTechOverwatch competition, run by Army Futures Command's Transformation and Training Command. Swarmbotics was one of roughly 40 finalists selected from over 630 submissions; FireAnt was tested at the Innovation Proving Ground in Bryan, Texas in late October 2025, and the company publicly unveiled FireAnt shortly afterward, in November 2025. That led to selection, announced February 5, 2026, to work with the Army's 1st Cavalry Division under the Transformation in Contact (TiC) initiative through mid-2027, with a stated 2026 goal of establishing baseline concepts for deploying hundreds of robots during maneuver and breaching operations.

## Notable Developments

- **2026-02-05:** Selected by the US Army for its Transformation in Contact (TiC) program, partnered with the 1st Cavalry Division, following xTechOverwatch performance; work to run through mid-2027. ([The Defense Post](https://thedefensepost.com/2026/02/09/swarmbotics-us-army/); [Defence Blog](https://defence-blog.com/u-s-army-selects-swarmbotics-ai-for-autonomous-robot-swarms/))
- **2026-02 (as of review):** $2.0 million in disclosed DoD prime federal contract value across 2 awards, including a Direct-to-Phase-II SBIR award (Topic A254-P030, xTechOverwatch Open Topic); company registered in SAM.gov as Swarmbotics AI, Inc., Phoenix, AZ. ([GovIntel](https://www.govintel.ai/companies/az/swarmbotics-ai-inc-1837152))
- **2025-11-05:** Publicly unveiled the FireAnt anti-armor sUGV; company states a projected unit cost below $50,000. ([The Defense Post](https://thedefensepost.com/2025/11/05/robots-wheels-tanks-swarms/); [Army Recognition](https://armyrecognition.com/news/army-news/2025/u-s-army-tests-fireant-anti-tank-ground-robot-to-detect-track-and-neutralize-armored-vehicles))
- **2025-10-27 to 2025-10-29:** FireAnt tested at the Army's xTechOverwatch event, Innovation Proving Ground, Bryan, TX. ([Army Recognition](https://armyrecognition.com/news/army-news/2025/u-s-army-tests-fireant-anti-tank-ground-robot-to-detect-track-and-neutralize-armored-vehicles))
- **2025-04:** Army Transformation and Training Command launches xTechOverwatch competition; over 630 submissions, roughly 40 finalists selected. ([The Defense Post](https://thedefensepost.com/2026/02/09/swarmbotics-us-army/))
- **2024-08-19:** TechCrunch profile discloses approximately $4 million pre-seed round (Quiet Capital, Silent Ventures, LMNT Ventures, Soma Capital) and 11 employees. ([TechCrunch](https://techcrunch.com/2024/08/19/swarmbiotics-founders-grew-obsessed-with-robot-swarms-and-now-plan-to-bring-them-to-the-battlefield/))
- **2023 (end of year):** Pre-seed round closed. ([Defense Tech Spotlight](https://dtvc.substack.com/p/defense-tech-spotlight-swarmbotics))
- **2023 (summer):** Founded by Stephen Houghton and Drew Watson. ([TechCrunch](https://techcrunch.com/2024/08/19/swarmbiotics-founders-grew-obsessed-with-robot-swarms-and-now-plan-to-bring-them-to-the-battlefield/))

## Key People

### Stephen Houghton — Co-Founder and CEO
- **LinkedIn:** [linkedin.com/in/stephen-houghton-5644427](https://www.linkedin.com/in/stephen-houghton-5644427/)
- **Career (reverse-chronological):**
  - Swarmbotics AI (2023–present): Co-Founder and CEO
  - Embark Trucks: COO (autonomous trucking)
  - Cruise: VP of Global Markets; early employee who joined when the company was roughly 40 people and left as it grew to roughly 3,000
  - Amazon Web Services: Led autonomous vehicles and robotics division
  - US Marine Corps: Officer
- **Notes:** Public bio emphasizes scaling experience at Cruise during its highest-growth period plus enterprise robotics/AV exposure at AWS.

### Drew Watson — Co-Founder and CTO
- **LinkedIn:** [linkedin.com/in/drew-watson-444541122](https://www.linkedin.com/in/drew-watson-444541122/)
- **Career (reverse-chronological):**
  - Swarmbotics AI (2023–present): Co-Founder and CTO
  - Embark Trucks: Product operations
  - NASA Jet Propulsion Laboratory: Led software development for the Valkyrie humanoid robot program
  - Central Intelligence Agency: Prior role (specifics not publicly detailed)
- **Notes:** Watson and Houghton previously worked together at Embark Trucks (Houghton as COO, Watson in product operations) before co-founding Swarmbotics AI.

### People — Last Reviewed: 2026-08-27

## Supply Chain Position

Swarmbotics AI is a **Platform OEM** integrating both hardware and autonomy software. Its platforms are reported to be built on largely commercial off-the-shelf components, including hybrid-electric ATV chassis for HaulAnt, rather than a bespoke ground-up drivetrain. **⚑ Rare earth dependency:** as with other tracked/wheeled electric-drive UGVs in this section, any BLDC or servo drive motors used in FireAnt's or HaulAnt's propulsion are likely to depend on NdFeB permanent magnets; no source reviewed here discloses Swarmbotics' specific motor supplier.

## Claim Verification

### Claim: FireAnt has a projected unit cost below $50,000
**Status:** Unverified (company-stated design target)

**Supporting sources:**
- [Army Recognition](https://armyrecognition.com/news/army-news/2025/u-s-army-tests-fireant-anti-tank-ground-robot-to-detect-track-and-neutralize-armored-vehicles) — reports the sub-$50,000 figure as the company's projected unit cost

**Refuting / questioning sources:**
- No independent source reviewed confirms an actual production or per-unit contract cost; the figure is a pre-production company projection, not a delivered-unit price, and early-stage defense hardware programs routinely see unit costs rise between prototype and low-rate production.

**Summary:** The sub-$50,000 figure is a company-stated target tied to FireAnt's "attritable" design philosophy, not a verified delivered price; no production contract or per-unit pricing has been independently confirmed as of this review.

### Claim: Swarmbotics AI holds $2.0 million in disclosed DoD federal contract value across 2 prime awards
**Status:** Verified

**Supporting sources:**
- [GovIntel](https://www.govintel.ai/companies/az/swarmbotics-ai-inc-1837152) — federal contract database entry citing SAM.gov registration (UEI FX2TN3JT5RD1, active through 2027-04-27) and a $2.0 million total across 2 DoD prime contract awards, the most recent a Direct-to-Phase-II SBIR award under Topic A254-P030 (xTechOverwatch Open Topic)

**Refuting / questioning sources:**
- None found; this figure derives from a government-contract-data aggregator rather than company self-reporting, and is consistent with the publicly reported xTechOverwatch/Transformation in Contact selection.

**Summary:** The $2.0 million disclosed federal contract figure is corroborated by an independent federal-contracting database and is consistent with the publicly announced Army program selection; it likely understates Swarmbotics' eventual program value, since the February 2026 TiC selection is described as an initial engagement running through mid-2027 rather than a fixed-price delivery contract.

## Sources

- [Swarmbotics AI — official site](https://www.swarmbotics.ai/)
- [Swarmbotics founders grew 'obsessed with robot swarms' — TechCrunch (Aug 2024)](https://techcrunch.com/2024/08/19/swarmbiotics-founders-grew-obsessed-with-robot-swarms-and-now-plan-to-bring-them-to-the-battlefield/)
- [Swarmbotics unveils FireAnt robot to hunt heavy armor — Interesting Engineering](https://interestingengineering.com/military/us-tank-hunting-robots)
- [Swarmbotics AI — BuiltIn company page](https://builtin.com/company/swarmbotics-ai/jobs)
- [Defense Tech Spotlight: Swarmbotics — DTVC (May 2024)](https://dtvc.substack.com/p/defense-tech-spotlight-swarmbotics)
- [Swarmbotics AI — LMNT Ventures portfolio](https://lmnt.vc/portfolio-swarmbotics-ai)
- [Swarmbotics AI Secures $4 Million in Pre-Seed Funding — SignalBase](https://www.trysignalbase.com/news/funding/swarmbotics-ai-secures-4-million-in-pre-seed-funding-to-revolutionize-industry-and-defense-robotics)
- [Swarmbotics Wins US Army Contract for Swarming Ground Robots — The Defense Post (Feb 2026)](https://thedefensepost.com/2026/02/09/swarmbotics-us-army/)
- [U.S. Army tests FireAnt anti-tank ground robot — Army Recognition](https://armyrecognition.com/news/army-news/2025/u-s-army-tests-fireant-anti-tank-ground-robot-to-detect-track-and-neutralize-armored-vehicles)
- [Numbers Over Size: America's New Robots on Wheels Hunt Down Tanks in Swarms — The Defense Post (Nov 2025)](https://thedefensepost.com/2025/11/05/robots-wheels-tanks-swarms/)
- [U.S. Army Selects Swarmbotics AI for Autonomous Robot Swarms — Defence Blog](https://defence-blog.com/u-s-army-selects-swarmbotics-ai-for-autonomous-robot-swarms/)
- [Swarmbotics AI, Inc. (AZ) — federal contracts — GovIntel](https://www.govintel.ai/companies/az/swarmbotics-ai-inc-1837152)
- [Swarmbotics AI: Why the US Army is betting on robotic mass — Calibre Defence](https://www.calibredefence.co.uk/swarmbotics-ai-why-the-us-army-is-betting-on-robotic-mass/)
