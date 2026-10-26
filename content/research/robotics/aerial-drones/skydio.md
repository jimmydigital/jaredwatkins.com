---
title: "Skydio"
date: 2026-03-24
lastmod: 2026-10-23
draft: false
description: "San Mateo-based autonomous drone maker; X10/X10D tactical sUAS with onboard NVIDIA Jetson Orin compute; full lineup on the DoD Blue UAS Cleared List (July 2026); $110M Series F at $4.4B (April 2026); $52M+ Army X10D order (2,500+ units, March 2026); $3.5B five-year US manufacturing pledge."
research_area: "robotics/aerial-drones"
source_urls:
  - "https://www.skydio.com/x10"
  - "https://www.skydio.com/x10/technical-specs"
  - "https://www.skydio.com/resources/podcasts/skydio-raises-usd110m-series-f-at-usd4-4b-valuation-ceo-adam-bry"
  - "https://dronexl.co/2026/04/23/skydio-110m-series-f-44-billion-valuation/"
  - "https://www.tectonicdefense.com/skydio-raises-110m-at-4-4b-valuation/"
  - "https://www.skydio.com/blog/skydio-commits-usd3-5-billion-to-expand-u-s-manufacturing-and-secure-american-drone-leadership"
  - "https://dronexl.co/2026/07/23/skydio-full-lineup-blue-uas-cleared-list/"
  - "https://dronexl.co/2026/09/24/skydio-f10-lightrunner-ascend-2026-lobbying/"
  - "https://www.asdnews.com/news/defense/2026/03/22/us-army-places-52m-order-skydio-x10d-largest-singlevendor-tactical-suas-order-army-history"
  - "https://dronexl.co/2026/03/22/skydio-x10d-army-52-million-order/"
  - "https://www.asdnews.com/news/defense/2025/10/14/us-army-awards-79m-contract-skydio-short-range-reconnaissance-tranche-2"
  - "https://www.skydio.com/blog/USAF-Awards-Skydio-Initial-Contracts-to-Bring-Advanced-Autonomy-to-Mission-Critical-specialties"
  - "https://www.skydio.com/blog/skydio-drones-selected-NATO-nspa-for-nano-uas-framework-agreement"
  - "https://www.skydio.com/blog/skydio-raises-230-million-series-e-funding-round"
  - "https://techcrunch.com/2024/11/15/drone-manufacturer-skydio-raises-170-million-extension-round/"
  - "https://www.skydio.com/blog/u-s-department-of-defense-adds-skydio-x10d-drone-to-blue-uas-cleared-list"
  - "https://www.skydio.com/blog/skydio-nightsense-is-now-blue-uas-approved"
  - "https://www.diu.mil/latest/blue-uas-refresh-list-and-framework-platforms-and-capabilities-selected"
  - "https://spectrum.ieee.org/skydios-dock-in-a-box-enables-longterm-autonomy-for-drone-applications"
  - "https://investor.axon.com/2024-06-20-Axon-and-Skydio-partner-to-deliver-scalable-drone-offering-for-public-safety,-including-Drone-as-First-Responder-solution"
  - "https://en.wikipedia.org/wiki/Skydio"
  - "https://www.linkedin.com/in/abachrach/"
last_reviewed: 2026-10-23
stale_after_days: 90
related:
  - "robotics/aerial-drones/_index.md"
  - "robotics/aerial-drones/dji.md"
  - "robotics/aerial-drones/anduril.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Skydio is a San Mateo, California maker of small unmanned aircraft systems (sUAS) built around onboard computer-vision autonomy, selling to defense, public safety, utility and enterprise customers. It was founded in 2014 by Adam Bry, Abraham Bachrach and Matt Donahoe and is the leading US-built alternative to DJI in tactical and public-safety drones. The core platform is the X10 (commercial) and X10D (defense) quadcopter, with an NVIDIA Jetson Orin compute module, a FLIR Boson+ thermal camera and a 360° navigation camera array. As of July 2026 Skydio says every current platform (X10, X10D, X10 Dock, R10) is on the DoD Blue UAS Cleared List. In 2026 it raised a $110M Series F at a $4.4B valuation (April), received a US Army X10D order of more than $52M (March) and announced a $3.5B five-year US manufacturing commitment (April).

## Key Facts

- **Founded:** 2014
- **HQ:** San Mateo, CA, USA
- **Type:** Private (venture-backed)
- **Status:** Active production and deployment
- **Latest round:** $110M Series F at $4.4B post-money, announced 2026-04-23; lead investor not named in the sources reviewed. Previous valuation $2.5B (November 2024 Series E extension)
- **Earlier backers:** Andreessen Horowitz (led 2021 round), Linse Capital (led 2023 Series E), NVIDIA, DoCoMo, Next47, IVP, UP.Partners, Axon, KDDI (strategic, 2024)
- **Platforms:** X10 (commercial), X10D (defense), R10 (indoor), X10 Dock; F10 "Lightrunner" fixed-wing shown September 2026 (no price or ship date published)
- **Airframe:** X10 weighs about 4.65–4.75 lb (2.11–2.16 kg) depending on configuration; folding arms; IP55 aircraft rating
- **Compute and sensors:** NVIDIA Jetson Orin plus Qualcomm Snapdragon 865; six navigation cameras; 50.3MP wide, 64MP narrow and 48MP telephoto cameras; FLIR Boson+ 640×512 thermal
- **Endurance:** up to 40 minutes flight, up to 35 minutes hover (specifications measured under ideal lab conditions per Skydio)
- **Autonomy:** computer-vision obstacle avoidance; under FAA Part 107 a remote pilot still retains control authority; BVLOS operations depend on FAA waivers
- **Compliance:** NDAA-compliant; Blue UAS Cleared List (X10D since 2024; X10, Dock and R10 added 2026-07-23 per Skydio, as reported by DroneXL)
- **Company-reported scale (April 2026):** 60,000+ drones shipped; 3,800+ customers; 1,200+ public-safety agencies; roughly 900 employees per DroneXL (Skydio's April blog cites 2,000+ planned new jobs)
- **Government programs:** US Army Short Range Reconnaissance (SRR) Program of Record (selected 2022 and 2025); US Air Force TACP and EOD contracts (2025); NATO NSPA nano UAS framework (2025)

## What It Is / How It Works

The X10 is a tactical sUAS for autonomous visual reconnaissance, inspection and public-safety work. Folding arms let it be carried in a backpack and launched quickly, and the battery is swappable in the field.

**Sensor suite.** Redundant perception combines six navigation cameras with a 50.3MP 1-inch wide camera (93° field of view), a 64MP narrow camera (50°), a 48MP telephoto camera (13°) and a FLIR Boson+ uncooled thermal imager (640×512, 41° field of view). Skydio's NightSense mode uses these sensors for obstacle avoidance in low light.

**Autonomy engine.** Skydio's proprietary software builds a real-time 3D map of surroundings from camera data, running on the onboard NVIDIA Jetson Orin. It supports obstacle avoidance in cluttered or GPS-degraded environments, subject tracking and waypoint missions with replanning around obstacles. It does not remove the pilot-in-command requirement under FAA Part 107; it reduces manual flight workload.

**Connectivity and docking.** The X10D adds encrypted data links and NDAA-compliant components. Optional 5G/LTE modems extend control beyond radio line of sight where FAA waivers allow. The Dock charges the aircraft and launches it remotely; paired with Remote Ops it supports unattended drone-as-first-responder and inspection missions under FAA BVLOS waivers.

**Fixed-wing line.** At Ascend 2026 (2026-09-23) Skydio showed the F10 Lightrunner, a fixed-wing aircraft launched from a robotic MegaDock. Skydio's stated figures are 100 mph, a 30-mile radius and up to 120 minutes of flight (per DroneXL coverage of the event); no price or ship date has been published.

## Notable Developments

- **2026-09:** Ascend 2026 (Summerlin, NV, 2026-09-23): F10 Lightrunner fixed-wing and MegaDock (up to five F10s) shown, plus power-line detection and "Thermal Boost" software updates. ([DroneXL](https://dronexl.co/2026/09/24/skydio-f10-lightrunner-ascend-2026-lobbying/))
- **2026-07:** Skydio announces X10, X10 Dock and R10 are on the Blue UAS Cleared List, completing clearance for its current lineup; it claims the first Blue UAS-cleared drone-as-first-responder system. ([DroneXL](https://dronexl.co/2026/07/23/skydio-full-lineup-blue-uas-cleared-list/))
- **2026-04:** Skydio commits $3.5B over five years to US manufacturing, R&D and supply chain, including a new factory about five times its current space, more than $1B to domestic suppliers and 2,000+ new Skydio jobs. The site is not named. ([Skydio blog](https://www.skydio.com/blog/skydio-commits-usd3-5-billion-to-expand-u-s-manufacturing-and-secure-american-drone-leadership))
- **2026-04-23:** $110M Series F at $4.4B post-money; CEO Adam Bry said the notable fact of the round was "how little we are raising." ([Skydio](https://www.skydio.com/resources/podcasts/skydio-raises-usd110m-series-f-at-usd4-4b-valuation-ceo-adam-bry), [DroneXL](https://dronexl.co/2026/04/23/skydio-110m-series-f-44-billion-valuation/))
- **2026-03-22:** US Army places a $52M+ order for 2,500+ X10D under the SRR Program of Record via Atlantic Diving Supply; moved from bid to award in under 72 hours. ([ASD News](https://www.asdnews.com/news/defense/2026/03/22/us-army-places-52m-order-skydio-x10d-largest-singlevendor-tactical-suas-order-army-history))
- **2025-11:** US Air Force awards initial contracts for Tactical Air Control Party and Explosive Ordnance Disposal units. ([Skydio blog](https://www.skydio.com/blog/USAF-Awards-Skydio-Initial-Contracts-to-Bring-Advanced-Autonomy-to-Mission-Critical-specialties))
- **2025-10:** US Army awards a $7.9M SRR Tranche 2 contract. ([ASD News](https://www.asdnews.com/news/defense/2025/10/14/us-army-awards-79m-contract-skydio-short-range-reconnaissance-tranche-2))
- **2025-08:** NATO Support and Procurement Agency selects Skydio for a nano UAS framework agreement. ([Skydio blog](https://www.skydio.com/blog/skydio-drones-selected-NATO-nspa-for-nano-uas-framework-agreement))
- **2025-03:** China's Ministry of Commerce adds Skydio and 14 other US entities to its export control list. ([Wikipedia](https://en.wikipedia.org/wiki/Skydio))
- **2024-11:** $170M extension to the Series E, with KDDI and Axon participating, at a $2.5B valuation. ([TechCrunch](https://techcrunch.com/2024/11/15/drone-manufacturer-skydio-raises-170-million-extension-round/))
- **2024-06:** Axon and Skydio partner on a drone-as-first-responder offering for public safety. ([Axon](https://investor.axon.com/2024-06-20-Axon-and-Skydio-partner-to-deliver-scalable-drone-offering-for-public-safety,-including-Drone-as-First-Responder-solution))
- **2023-02:** $230M Series E led by Linse Capital. ([Skydio blog](https://www.skydio.com/blog/skydio-raises-230-million-series-e-funding-round))
- **2023-09:** X10 announced. ([Wikipedia](https://en.wikipedia.org/wiki/Skydio))
- **2018:** R1 launched, the first consumer drone with autonomous subject tracking and obstacle avoidance.

## Key People

### Adam Bry — Co-Founder and CEO
- **LinkedIn:** [linkedin.com/in/adambry](https://www.linkedin.com/in/adambry/)
- **Role:** Co-founder (2014); CEO
- **Education:** Franklin W. Olin College of Engineering (BS Mechanical Engineering); MIT (MS)
- **Career (reverse-chronological):**
  - Skydio (2014–present): Co-founder and CEO
  - MIT CSAIL: research on autonomous flight
- **Notes:** His MIT autonomous-flight research is the technical origin of Skydio's autonomy approach.

### Abraham (Abe) Bachrach — Co-Founder and CTO
- **LinkedIn:** [linkedin.com/in/abachrach](https://www.linkedin.com/in/abachrach/)
- **Role:** Co-founder (2014); CTO
- **Education:** UC Berkeley (BS EECS); MIT (PhD, robotics, advised by Nicholas Roy)
- **Career (reverse-chronological):**
  - Skydio (2014–present): Co-founder and CTO
  - MIT Robotics Laboratory: PhD research on planning and estimation
- **Notes:** Leads the perception and planning stack.

### Matt Donahoe — Co-Founder
- **Role:** Co-founder (2014); current title not confirmed from a fetched source
- **LinkedIn:** not found

**⚑ Shared background:** Bry, Bachrach and Donahoe all studied at MIT before founding Skydio (per Wikipedia).

### People — Last Reviewed: 2026-10-23

## Supply Chain Position

Skydio sits at the **Platform Integration** layer, building complete X10/X10D systems in California and, per the April 2026 commitment, planning a larger US factory plus a supplier co-location program called SkyForge.

**Proprietary:** autonomy software, navigation camera array design and firmware.

**Third-party components (confirmed on Skydio's spec page):**
- **Compute:** NVIDIA Jetson Orin and Qualcomm Snapdragon 865
- **Thermal imaging:** Teledyne FLIR Boson+ 640×512
- **Batteries, motors, structure:** suppliers not publicly disclosed

**Rare earth dependency:** Brushless motors typically use NdFeB magnets, and China dominates rare earth processing, so US assembly does not remove upstream exposure. Skydio's April 2026 statement says more than $1B will go to domestic suppliers, which targets this risk.

**China sanctions:** China's October 2024 sanctions and March 2025 export control listing bar Chinese entities from doing business with Skydio, which constrains component sourcing.

**⚑ Shared supplier:** Teledyne FLIR Boson modules and NVIDIA Jetson modules are also used by other drone makers documented in this section (see the [Aerial Drones]({{< relref "_index.md" >}}) supply chain table).

## Claim Verification

### Claim: "Autonomous" operation

**Status:** Partially verified

**Supporting sources:**
- [IEEE Spectrum](https://spectrum.ieee.org/skydios-dock-in-a-box-enables-longterm-autonomy-for-drone-applications) — describes Dock-based unattended operation
- [Skydio X10 page](https://www.skydio.com/x10) — documents autonomous obstacle avoidance, tracking and missions

**Refuting / questioning sources:**
- [FAA commercial operators](https://www.faa.gov/uas/commercial_operators) — Part 107 requires a remote pilot in command with authority over the aircraft; beyond-visual-line-of-sight flight needs specific waivers

**Summary:** Obstacle avoidance and mission automation are documented; "fully autonomous" overstates what regulation allows, since a pilot remains responsible.

### Claim: X10 specifications (40-minute flight, ~4.7 lb, IP55)

**Status:** Partially verified

**Supporting sources:**
- [Skydio X10 technical specs](https://www.skydio.com/x10/technical-specs) — up to 40 minutes flight, 35 minutes hover, 4.65–4.75 lb, IP55 aircraft rating

**Refuting / questioning sources:**
- The same page states figures were measured under ideal lab conditions, so field endurance will be lower. No independent benchmark was found.

**Summary:** Figures are company-reported lab values.

### Claim: Army order — $52M+, 2,500+ X10D units, March 2026

**Status:** Verified

**Supporting sources:**
- [ASD News](https://www.asdnews.com/news/defense/2026/03/22/us-army-places-52m-order-skydio-x10d-largest-singlevendor-tactical-suas-order-army-history) — over $52M, over 2,500 X10D, bid to award in under 72 hours
- [DroneXL](https://dronexl.co/2026/03/22/skydio-x10d-army-52-million-order/) — corroborating coverage

**Refuting / questioning sources:**
- DroneXL's April coverage of the Series F describes the order as "nearly 3,000" drones; ASD News's "over 2,500" is used here. The "largest single-vendor tactical sUAS order in Army history" wording comes from the ASD News headline and was not confirmed against an Army source.

**Summary:** Order value and minimum unit count are consistent across sources; the "largest" superlative is secondary-source only.

### Claim: Blue UAS clearance for the full lineup

**Status:** Partially verified

**Supporting sources:**
- [DroneXL, 2026-07-23](https://dronexl.co/2026/07/23/skydio-full-lineup-blue-uas-cleared-list/) — reports Skydio's announcement that X10, Dock and R10 were added; X10D was already listed
- [Skydio blog](https://www.skydio.com/blog/u-s-department-of-defense-adds-skydio-x10d-drone-to-blue-uas-cleared-list) — X10D clearance

**Refuting / questioning sources:**
- None found, but the July 2026 additions were not checked against the current list at [DIU](https://www.diu.mil/latest/blue-uas-refresh-list-and-framework-platforms-and-capabilities-selected).

**Summary:** X10D clearance is documented by Skydio; the 2026 additions rest on Skydio's announcement as reported by a trade outlet.

### Claim: $4.4B valuation and funding totals

**Status:** Partially verified

**Supporting sources:**
- [Skydio](https://www.skydio.com/resources/podcasts/skydio-raises-usd110m-series-f-at-usd4-4b-valuation-ceo-adam-bry), [DroneXL](https://dronexl.co/2026/04/23/skydio-110m-series-f-44-billion-valuation/), [Tectonic Defense](https://www.tectonicdefense.com/skydio-raises-110m-at-4-4b-valuation/) — $110M at $4.4B

**Refuting / questioning sources:**
- Cumulative funding differs by source (about $672M in DroneXL, about $951M in Tectonic Defense); no company-stated total was found, so none is given here.

**Summary:** Round size and valuation agree; cumulative funding is unresolved.

## Competitive Position vs. DJI

DJI was added to the FCC Covered List on 2025-12-22, which blocks new US equipment authorizations (see [DJI]({{< relref "dji.md" >}})). Skydio's position is the compliant alternative: US-built, NDAA-compliant, Blue UAS-listed, and focused on public safety, defense and utilities rather than consumer or prosumer sales.

| Factor | Skydio X10/X10D | DJI enterprise (typical) |
|--------|-----------------|---------------------------|
| **Manufacturing** | California; NDAA-compliant | China; FCC Covered List; not on Blue UAS |
| **Federal procurement** | Blue UAS Cleared List; Army SRR | Restricted under US federal procurement law |
| **Thermal** | FLIR Boson+ 640×512 | Model-dependent |
| **Market focus** | Defense, public safety, utilities | Global commercial and consumer |

Critics tie Skydio's federal lobbying to the policy shift against DJI; CEO Adam Bry has denied lobbying for the Countering CCP Drones Act ([DroneXL](https://dronexl.co/2026/09/24/skydio-f10-lightrunner-ascend-2026-lobbying/)).

## Sources

- [Skydio X10](https://www.skydio.com/x10)
- [Skydio X10 technical specifications](https://www.skydio.com/x10/technical-specs)
- [Skydio Series F announcement](https://www.skydio.com/resources/podcasts/skydio-raises-usd110m-series-f-at-usd4-4b-valuation-ceo-adam-bry)
- [DroneXL — Series F](https://dronexl.co/2026/04/23/skydio-110m-series-f-44-billion-valuation/)
- [Tectonic Defense — Series F](https://www.tectonicdefense.com/skydio-raises-110m-at-4-4b-valuation/)
- [Skydio — $3.5B US manufacturing commitment](https://www.skydio.com/blog/skydio-commits-usd3-5-billion-to-expand-u-s-manufacturing-and-secure-american-drone-leadership)
- [DroneXL — Blue UAS full lineup](https://dronexl.co/2026/07/23/skydio-full-lineup-blue-uas-cleared-list/)
- [DroneXL — Ascend 2026](https://dronexl.co/2026/09/24/skydio-f10-lightrunner-ascend-2026-lobbying/)
- [ASD News — Army $52M order](https://www.asdnews.com/news/defense/2026/03/22/us-army-places-52m-order-skydio-x10d-largest-singlevendor-tactical-suas-order-army-history)
- [DroneXL — Army order](https://dronexl.co/2026/03/22/skydio-x10d-army-52-million-order/)
- [ASD News — SRR Tranche 2](https://www.asdnews.com/news/defense/2025/10/14/us-army-awards-79m-contract-skydio-short-range-reconnaissance-tranche-2)
- [Skydio — USAF contracts](https://www.skydio.com/blog/USAF-Awards-Skydio-Initial-Contracts-to-Bring-Advanced-Autonomy-to-Mission-Critical-specialties)
- [Skydio — NATO NSPA](https://www.skydio.com/blog/skydio-drones-selected-NATO-nspa-for-nano-uas-framework-agreement)
- [Skydio — Series E](https://www.skydio.com/blog/skydio-raises-230-million-series-e-funding-round)
- [TechCrunch — Series E extension](https://techcrunch.com/2024/11/15/drone-manufacturer-skydio-raises-170-million-extension-round/)
- [Skydio — X10D Blue UAS](https://www.skydio.com/blog/u-s-department-of-defense-adds-skydio-x10d-drone-to-blue-uas-cleared-list)
- [Skydio — NightSense Blue UAS](https://www.skydio.com/blog/skydio-nightsense-is-now-blue-uas-approved)
- [DIU — Blue UAS list](https://www.diu.mil/latest/blue-uas-refresh-list-and-framework-platforms-and-capabilities-selected)
- [IEEE Spectrum — Skydio Dock](https://spectrum.ieee.org/skydios-dock-in-a-box-enables-longterm-autonomy-for-drone-applications)
- [Axon — partnership](https://investor.axon.com/2024-06-20-Axon-and-Skydio-partner-to-deliver-scalable-drone-offering-for-public-safety,-including-Drone-as-First-Responder-solution)
- [FAA — commercial operators](https://www.faa.gov/uas/commercial_operators)
- [Wikipedia — Skydio](https://en.wikipedia.org/wiki/Skydio)
