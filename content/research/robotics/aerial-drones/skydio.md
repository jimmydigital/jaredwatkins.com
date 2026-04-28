---
title: "Skydio"
date: 2026-03-24
lastmod: 2026-03-24
draft: false
description: "San Jose-based autonomous drone manufacturer; X10/X10D tactical small UAS platforms with onboard NVIDIA Jetson Orin compute; Blue UAS certified; $52M+ US Army procurement (2,500+ units, March 2026); $715M+ total funding, $2.5B valuation (Nov 2024); founded 2014; US-manufactured, NDAA-compliant."
tags: ["robotics", "aerial-drone", "us", "defense", "commercial"]
categories: ["company"]
research_area: "robotics/aerial-drones"
source_urls:
  - "https://www.skydio.com/x10"
  - "https://www.skydio.com/x10/technical-specs"
  - "https://www.asdnews.com/news/defense/2026/03/22/us-army-places-52m-order-skydio-x10d-largest-singlevendor-tactical-suas-order-army-history"
  - "https://www.skydio.com/blog/skydio-raises-230-million-series-e-funding-round"
  - "https://www.linkedin.com/in/adambry/"
  - "https://www.linkedin.com/in/abachrach/"
  - "https://www.skydio.com/blog/u-s-department-of-defense-adds-skydio-x10d-drone-to-blue-uas-cleared-list"
  - "https://dronelife.com/2025/05/21/faa-waiver-enables-fully-remote-drone-inspections-with-docked-systems/"
  - "https://www.skydio.com/blog/USAF-Awards-Skydio-Initial-Contracts-to-Bring-Advanced-Autonomy-to-Mission-Critical-specialties"
last_reviewed: 2026-03-24
stale_after_days: 90
related:
  - "robotics/aerial-drones/_index.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Skydio is a San Jose, California manufacturer of small unmanned aircraft systems (sUAS) focused on autonomous flight technology for defense, public safety, and enterprise applications. Founded in 2014 by Adam Bry, Abraham Bachrach, and Matt Donahoe, Skydio has positioned itself as the primary US-based alternative to DJI in the tactical small UAS market. The company's flagship platform is the X10 (commercial) and X10D (defense-specific) — 4.7 lb tactical drones with six 32MP navigation cameras, NVIDIA Jetson Orin compute, FLIR thermal imaging, and proprietary autonomy software for obstacle avoidance and autonomous mission execution. The X10D is certified on the Department of Defense Blue UAS Cleared List. In March 2026, the US Army placed a record $52+ million single-vendor procurement order for 2,500+ X10D systems — the largest tactical sUAS purchase in Army history. Skydio has raised $715 million across seven funding rounds (as of November 2024) at a $2.5 billion valuation. Key investors include Andreessen Horowitz, DoCoMo, NVIDIA, Axon, and KDDI.

## Key Facts

- **Founded:** 2014
- **HQ:** San Jose, CA, USA
- **Type:** Private (venture-backed)
- **Status:** Active production and deployment
- **Key backers:** Andreessen Horowitz (early investor), Next47, IVP, DoCoMo, NVIDIA, UP.Partners, Hercules Capital, Axon, KDDI (strategic investor, 2024)
- **Platform:** X10 (commercial) / X10D (defense); 4.7 lbs; folding design
- **Autonomy:** Computer-vision based obstacle avoidance; proprietary Autonomy Engine; does **not** eliminate remote pilot requirement under FAA Part 107 (pilot must retain control authority); advanced FAA BVLOS waivers obtained for specific use cases (energy, law enforcement, logistics)
- **Compute:** Onboard NVIDIA Jetson Orin GPU; six 32MP navigation cameras (360° visibility); 50MP wide-angle camera (1" module, 93° FOV); 64MP narrow-angle camera (50° FOV); FLIR Boson+ 640x512 thermal; 4K/60fps video
- **Flight endurance:** 40 minutes (X10 commercial load); up to 35 minutes (X2D tactical variant)
- **Regulatory compliance:** NDAA-compliant; US-manufactured; Blue UAS certified (X10D); Remote ID compatible; IP55 weather rating; -4° to 113°F operating range
- **Government programs:** US Army Short Range Reconnaissance (SRR) Program of Record (2022, 2025); US Air Force Tactical Air Control Party (TACP) and Explosive Ordnance Disposal (EOD) contracts (2025); NATO NSPA nano UAS framework agreement (2025)
- **Total funding:** $715M (seven rounds); latest Series E extension: $170M (November 2024)
- **Current valuation:** $2.5B (November 2024)
- **Mass production:** X10D ramping for large-scale military deployment (2026 onwards)

## What It Is / How It Works

The Skydio X10 is a tactical small unmanned aircraft system designed as a portable, rapidly-deployable platform for autonomous visual reconnaissance, surveillance, and inspection. The platform consists of three key elements:

**Hardware Platform:**
The X10 is a quadcopter with a 4.7 lb airframe and folding arms, enabling deployment from a backpack in under 40 seconds. The battery is hot-swappable for extended mission cycles. The platform incorporates IP55 weather sealing (resistant to dust and water jets) and operates across a broad temperature range, making it suitable for field deployment in harsh environments.

**Sensor Suite:**
The X10 integrates redundant perception: six 32MP navigation cameras (optimized for motion planning), a 50MP wide-angle RGB camera (1" sensor for image quality), a 64MP telephoto narrow-angle camera, and a FLIR Boson+ thermal imager (640x512, radiometric). This multi-modal sensor design enables obstacle avoidance, target detection, and situation awareness in zero-light and smoky/obscured conditions (NightSense mode).

**Autonomy Engine:**
Skydio's proprietary Autonomy Engine is a computer-vision-based system developed over 10+ years (since the R1 launch in 2018). It uses deep learning and stereo vision to build a real-time 3D occupancy map of the environment, enabling:
- **Autonomous obstacle avoidance:** Flight in GPS-denied, cluttered environments (urban, indoor, forest)
- **Subject tracking:** Ability to follow a moving target while maintaining safety margins
- **Autonomous mission execution:** Pre-programmed waypoint navigation with dynamic replanning around obstacles
- **NightSense mode:** Visual and infrared perception without external illumination (using either visible-light or IR sensors)

The Autonomy Engine is proprietary software running on the onboard NVIDIA Jetson Orin. It is **not** a replacement for the remote pilot — regulatory compliance under FAA Part 107 requires that the remote pilot in command retain the ability to direct the aircraft at all times. However, Skydio's technology enables mission automation that reduces pilot workload and enables operations under specific FAA waivers for BVLOS (beyond visual line of sight) scenarios.

**Connectivity & Security:**
The X10D variant includes AES-256 encryption, full NDAA compliance, and secure data architecture. Optional 5G/LTE modems enable remote operation beyond RF line-of-sight (under approved FAA waivers). The X10 supports modular payloads including RTK surveying, spotlight, and speaker modules.

**Dock & Remote Operations:**
Skydio offers a "Dock" accessory for autonomous charging and mission continuity. The Dock + Remote Ops combination enables 24/7 autonomous surveillance and rapid-response launch without human presence on-site (under approved FAA BVLOS waivers, e.g., for energy utilities and law enforcement).

## Notable Developments

- **2026-03 (22 March):** US Army awards Skydio $52+ million contract for 2,500+ X10D systems — largest single-vendor tactical sUAS procurement in Army history. Order moved from bid to award in less than 72 hours, reflecting operational urgency. ([ASD News](https://www.asdnews.com/news/defense/2026/03/22/us-army-places-52m-order-skydio-x10d-largest-singlevendor-tactical-suas-order-army-history))
- **2025-11 (13 November):** US Air Force awards Skydio initial multi-million dollar contracts for Tactical Air Control Party (TACP) and Explosive Ordnance Disposal (EOD) unit deployment. ([Skydio blog](https://www.skydio.com/blog/USAF-Awards-Skydio-Initial-Contracts-to-Bring-Advanced-Autonomy-to-Mission-Critical-specialties))
- **2025-10 (14 October):** US Army awards Skydio $7.9M contract for Short Range Reconnaissance Tranche 2. Skydio is sole manufacturer to win both SRR Tranche 1 (2022) and Tranche 2 awards. ([ASD News](https://www.asdnews.com/news/defense/2025/10/14/us-army-awards-79m-contract-skydio-short-range-reconnaissance-tranche-2))
- **2025-08:** NATO Support and Procurement Agency (NSPA) selects Skydio for nano UAS framework agreement to supply small ISR drones across NATO member nations (in partnership with COBBS BELUX BV). ([Skydio blog](https://www.skydio.com/blog/skydio-drones-selected-NATO-nspa-for-nano-uas-framework-agreement))
- **2025-05:** FAA grants waivers enabling fully remote BVLOS operations using Skydio Dock + Remote Ops for Dominion Energy and New York Power Authority; FAA extends nation-wide Tactical BVLOS waiver to all public safety agencies based on Chula Vista Police Department deployment. ([Drone Life](https://dronelife.com/2025/05/21/faa-waiver-enables-fully-remote-drone-inspections-with-docked-systems/))
- **2025-06:** Skydio X10 Gen 2 announced with hardware upgrades focusing on cellular/LTE performance (narrowband LTE, 5G readiness). ([Skydio support docs](https://support.skydio.com/hc/en-us/articles/39423158528795-Skydio-X10-Gen-2))
- **2024-11 (15 November):** Series E extension round of $170M closes; investors include strategic partners KDDI (Japanese telecom, plans 1,000-unit deployment across Japan) and Axon (police technology, Drone as First Responder partnership). Brings total funding to $715M+ at $2.5B valuation. ([TechCrunch](https://techcrunch.com/2024/11/15/drone-manufacturer-skydio-raises-170-million-extension-round/))
- **2024-08:** Optelos and Skydio announce technology partnership for autonomous asset inspection workflows. ([Optelos](https://optelos.com/skydiopartnership/))
- **2024-06:** Axon and Skydio partner to deliver end-to-end offering for public safety, including Drone as First Responder (DFR) solution. ([Axon investor relations](https://investor.axon.com/2024-06-20-Axon-and-Skydio-partner-to-deliver-scalable-drone-offering-for-public-safety,-including-Drone-as-First-Responder-solution))
- **2024-11:** Series E round ($230M) closed in early 2023, led by Linse Capital; co-investors Andreessen Horowitz, Next47, IVP, DoCoMo, NVIDIA, UP.Partners.
- **2018:** Skydio launches R1 — first commercial autonomous drone with obstacle avoidance and subject tracking (no pilot input required for basic missions).

## Key People

### Adam Bry — Co-Founder and CEO
- **LinkedIn:** [linkedin.com/in/adambry](https://www.linkedin.com/in/adambry/)
- **Role:** Co-founder (2014); CEO
- **Education:**
  - Franklin W. Olin College of Engineering: BS Mechanical Engineering (2008)
  - Massachusetts Institute of Technology (MIT): MS Computer Science, Aerospace, Aeronautical and Astronautical Engineering (2012, AI/robotics focus)
- **Career (reverse-chronological):**
  - Skydio (2014–present): Co-founder and CEO
  - MIT Computer Science and Artificial Intelligence Laboratory (CSAIL) (2010–2014): Led award-winning autonomous flight research; pioneered computer-vision-based drone autonomy
  - DARPA Urban Challenge (2007): Member of winning autonomous ground vehicle team
  - Hewlett Packard: Early-career role
- **Notes:** Bry's MIT CSAIL work on autonomous flight forms the technical foundation for Skydio's Autonomy Engine. He is a licensed R/C pilot and transferred hands-on flight experience into software architecture for autonomy.

### Abraham (Abe) Bachrach — Co-Founder and CTO
- **LinkedIn:** [linkedin.com/in/abachrach](https://www.linkedin.com/in/abachrach/)
- **Role:** Co-founder (2014); CTO
- **Education:**
  - University of California, Berkeley: BS Electrical Engineering and Computer Sciences (EECS)
  - Massachusetts Institute of Technology (MIT): PhD under Professor Nicholas Roy, focus on "Trajectory Bundle Estimation for Perception-Driven Planning" (robotics, estimation theory)
- **Career (reverse-chronological):**
  - Skydio (2014–present): Co-founder and CTO; led development of Autonomy Engine and computer-vision perception stack
  - MIT Robotics Laboratory (2008–2014): PhD research under Prof. Nicholas Roy on trajectory estimation and motion planning
- **Notes:** Bachrach's PhD focus on sensor-based planning and estimation directly informed Skydio's vision-based autonomy approach. He is the primary architect of the obstacle avoidance and trajectory planning algorithms. Bachrach came from MIT's renowned Robotics Lab, one of the primary origin clusters for US drone company founders.

### Matt Donahoe — Co-Founder
- **Role:** Co-founder (2014); Chief Operating Officer (operations, manufacturing, scaling)
- **LinkedIn:** LinkedIn profile not publicly confirmed at time of research
- **Notes:** Donahoe led Skydio's manufacturing scale-up and production operations, particularly critical for the NDAA-compliant, US-manufactured supply chain.

### People — Last Reviewed: 2026-03-24

## Supply Chain Position

Skydio operates at the **Platform Integration** layer, manufacturing complete X10/X10D sUAS systems in the United States (San Jose, California). The platform is vertically integrated in key subsystems:

**Proprietary Elements:**
- Autonomy Engine (computer-vision stack, obstacle avoidance, motion planning) — fully proprietary
- Custom multi-lens navigation camera array (six 32MP lenses, designed for stereo perception)
- Firmware and embedded software stack

**Third-Party Components (Verified):**
- **Compute:** NVIDIA Jetson Orin (GPU for real-time perception and planning)
- **Thermal imaging:** Teledyne FLIR Boson+ 640x512 radiometric imager (module supply)
- **RF/Connectivity:** Cellular modems (optional 5G/LTE); standard ISM-band RF for command/control
- **Battery/Power:** Not publicly disclosed; Skydio has indicated supply chain constraints from international sanctions (restricting battery distribution internationally per search results)
- **Structural materials:** Carbon fiber, aluminum (standard aerospace suppliers)
- **Optical elements:** Custom lens fabrication for navigation and main cameras

**Rare Earth Dependency:** Like all BLDC motor-driven platforms, the X10's propulsion system depends on neodymium-iron-boron (NdFeB) permanent magnet motors. China controls ~85% of global rare earth mining and 90%+ of rare earth processing/separation, creating a systemic geopolitical risk — though Skydio's US manufacturing and NDAA compliance are designed to mitigate supply chain vulnerability compared to DJI.

**Regulatory Advantage:** NDAA compliance and Blue UAS certification create exclusive access to US federal procurement, a significant competitive moat. However, this also creates dependency on US regulatory continuity and military budget appropriations.

**⚑ Shared supplier risk:** Skydio's thermal imaging (FLIR Boson), compute (NVIDIA Jetson), and optical subsystems are also used by competing US drone platforms (Autel, Teal). The NVIDIA Jetson supply chain became a bottleneck during the post-2022 AI compute shortage, though this has eased.

## Claim Verification

### Claim: "Fully Autonomous" Operations

**Company claim:** Skydio markets the X10 as capable of "fully autonomous" flight, obstacle avoidance, subject tracking, and mission execution without continuous pilot input.

**Status:** Partially verified with important regulatory caveats.

**Supporting sources:**
- [Skydio Autonomy blog](https://www.skydio.com/blog/part-107-autonomy-skydio-drone) — Confirms autonomous mission modes (waypoint navigation, subject tracking, obstacle avoidance)
- [Imatest evaluation](https://www.originofbots.com/robot/skydio-x10-by-skydio-details-specifications-rating) — Independent test confirms obstacle avoidance in GPS-denied cluttered environments (urban, indoor)
- [IEEE Spectrum — Dock autonomy](https://spectrum.ieee.org/skydios-dock-in-a-box-enables-longterm-autonomy-for-drone-applications) — Confirms Dock + Remote Ops enables 24/7 autonomous surveillance under FAA waivers

**Refuting / questioning sources:**
- [Skydio regulatory services blog](https://www.skydio.com/blog/part-107-autonomy-skydio-drone) — **Explicitly clarifies:** FAA Part 107 requires remote pilot to retain ability to direct aircraft at all times; "autonomous" refers to mission automation, not elimination of human control
- [FAA Remote ID and Part 107 regulations](https://www.faa.gov/uas/commercial_operators) — Remote pilot certificate required; pilot must maintain authority to redirect for safety/compliance

**Summary:**
- **Obstacle avoidance:** Verified independent of human input; computer-vision-based detection and dynamic replanning confirmed
- **Subject tracking:** Verified in field conditions
- **Autonomous missions:** Verified (waypoint nav, patrol patterns) but **NOT** true autonomy-without-operator — pilot must remain available to assume control
- **BVLOS operations:** Only enabled under FAA-granted waivers (not standard Part 107 authority); limited to specific operators (energy utilities, law enforcement, select public safety) and require pilot monitoring of data feed
- **Operational reality:** The X10 is best characterized as "highly automated with autonomous mission modes" rather than "fully autonomous." The remote pilot in command (PIC) is always required under US law; what Skydio's tech eliminates is **continuous manual flight control**, not **human presence in the loop**. This distinction is material for customers evaluating deployment in remote or dangerous areas.

### Claim: X10D Specifications — 40-minute flight time, 4.7 lbs, 360° vision, NightSense zero-light nav

**Status:** Verified (company-reported; independent field testing in progress).

**Supporting sources:**
- [Skydio X10 technical specs](https://www.skydio.com/x10/technical-specs) — Flight time 40 minutes (commercial payload); weight 4.7 lbs; camera/thermal specs confirmed
- [Skydio blog — X10 Gen 2 improvements](https://support.skydio.com/hc/en-us/articles/39423158528795-Skydio-X10-Gen-2) — Hardware upgrades focus on cellular connectivity, confirms baseline X10 endurance spec
- [Loyaltydrones review (2025)](https://loyaltydrones.com/skydio-x10-ultimate-guide-2025-breaking-news-latest-updates-complete-analysis/) — Field testing confirms 40-minute endurance under standard operating conditions
- [Imatest visual quality evaluation](https://www.originofbots.com/robot/skydio-x10-by-skydio-details-specifications-rating) — Confirms image quality across visible and thermal bands

**Refuting / questioning sources:**
- None identified; however, endurance figures assume moderate wind, hover-heavy profiles, and commercial payload; surveillance missions with constant altitude hold may see shorter effective endurance

**Summary:** Specifications are company-reported and appear consistent with field deployments by Army and law enforcement (2025–2026). No independent peer-reviewed publication yet; B1-equivalent testing by federal agencies is ongoing as of early 2026.

### Claim: US Army "Largest Single-Vendor Tactical sUAS Purchase in Army History" ($52M, 2,500+ units, March 2026)

**Status:** Verified.

**Supporting sources:**
- [ASD News, 22 March 2026](https://www.asdnews.com/news/defense/2026/03/22/us-army-places-52m-order-skydio-x10d-largest-singlevendor-tactical-suas-order-army-history) — Official announcement of $52M+ award
- [Soldier Systems Daily, 22 March 2026](https://soldiersystems.net/2026/03/22/us-army-places-52m-order-for-skydio-x10d-the-largest-single-vendor-tactical-suas-order-in-army-history/) — Corroborates "largest single-vendor" designation and 72-hour bid-to-award timeline
- [Drone XL coverage](https://dronexl.co/2026/03/22/skydio-x10d-army-52-million-order/) — Confirms 2,500+ unit count

**Refuting / questioning sources:**
- None; this is a recent government procurement and the largest Army sUAS award on record

**Summary:** The March 2026 Army award is a landmark procurement, representing rapid military adoption and confidence in the X10D platform. The 72-hour acceleration (unusual for federal procurement) suggests either urgent operational need or successful demonstration/evaluation in prior tranches.

### Claim: Blue UAS Certification and Security Compliance

**Status:** Verified.

**Supporting sources:**
- [DIU Blue UAS Cleared List](https://www.diu.mil/latest/blue-uas-refresh-list-and-framework-platforms-and-capabilities-selected) — X10D listed as approved platform
- [Skydio blog — X10D Blue UAS approved](https://www.skydio.com/blog/u-s-department-of-defense-adds-skydio-x10d-drone-to-blue-uas-cleared-list) — Confirms NDAA compliance, AES-256 encryption, cybersecurity review passed
- [Skydio blog — NightSense approved](https://www.skydio.com/blog/skydio-nightsense-is-now-blue-uas-approved) — Extended certification for thermal/NightSense operations

**Refuting / questioning sources:**
- None; Blue UAS is a DoD-controlled list with rigorous cybersecurity review — inclusion is a genuine credential

**Summary:** X10D is certified on the DoD's definitive approved-vendor list. Certification requires passing rigorous source-code review, supply-chain audits, and secure data architecture validation. This is a significant differentiator from non-certified platforms (including most DJI models, which are excluded due to Chinese ownership).

## Competitive Position vs. DJI

Skydio's strategy explicitly positions against DJI's market dominance. Key differentiation:

| Factor | Skydio X10D | DJI Matrice / Mavic (typical) |
|--------|-------------|------|
| **US Manufacturing** | San Jose, CA; NDAA-compliant; source-code access for government | Chinese; subject to FCC Covered List; US federal procurement prohibited |
| **Autonomy** | Computer-vision obstacle avoidance; 10+ years R&D; BVLOS waivers obtained | Assisted flight modes; no native obstacle avoidance in most models |
| **Endurance** | 40 min (X10); modular payloads | 30–35 min typical; less modular |
| **Thermal/Low-Light** | FLIR Boson+ 640x512; NightSense zero-light nav | Optional thermal; limited night capability |
| **Blue UAS** | Certified (X10D) | Not eligible (Chinese manufacturer) |
| **Price** | ~$15K–20K per unit (government pricing); $20K–25K commercial | $1K–5K (consumer/prosumer); $15K+ (enterprise Matrice) |
| **Supply Chain** | Constrained by US manufacturing and rare-earth availability; restricted international battery distribution | Global scale; lower cost; subject to US export controls and potential bans |

**Strategic implication:** Skydio concedes the consumer/prosumer drone market to DJI (where cost is paramount). Skydio's moat is in defense, government, and regulated enterprise where NDAA compliance, US manufacturing, and security clearance are non-negotiable. The $52M Army contract signals that this bet is validated — the federal procurement market is large enough to support a capital-intensive US-centric manufacturer.

## Sources

- [Skydio X10 Product Page](https://www.skydio.com/x10)
- [Skydio X10 Technical Specifications](https://www.skydio.com/x10/technical-specs)
- [US Army Awards Skydio $52M Contract for 2,500+ X10D (ASD News, March 2026)](https://www.asdnews.com/news/defense/2026/03/22/us-army-places-52m-order-skydio-x10d-largest-singlevendor-tactical-suas-order-army-history)
- [US Army Awards Skydio $7.9M for Short Range Reconnaissance Tranche 2 (ASD News, October 2025)](https://www.asdnews.com/news/defense/2025/10/14/us-army-awards-79m-contract-skydio-short-range-reconnaissance-tranche-2)
- [Skydio Raises $230M Series E Funding (Skydio Blog)](https://www.skydio.com/blog/skydio-raises-230-million-series-e-funding-round)
- [Skydio Raises $170M Extension (TechCrunch, November 2024)](https://techcrunch.com/2024/11/15/drone-manufacturer-skydio-raises-170-million-extension-round/)
- [Adam Bry LinkedIn Profile](https://www.linkedin.com/in/adambry/)
- [Abraham Bachrach LinkedIn Profile](https://www.linkedin.com/in/abachrach/)
- [Skydio X10D Certified on Blue UAS Cleared List (Skydio Blog)](https://www.skydio.com/blog/u-s-department-of-defense-adds-skydio-x10d-drone-to-blue-uas-cleared-list)
- [FAA BVLOS Waivers and Remote Operations (Drone Life, May 2025)](https://dronelife.com/2025/05/21/faa-waiver-enables-fully-remote-drone-inspections-with-docked-systems/)
- [US Air Force Awards Skydio Multi-Million Dollar Contracts (Skydio Blog, November 2025)](https://www.skydio.com/blog/USAF-Awards-Skydio-Initial-Contracts-to-Bring-Advanced-Autonomy-to-Mission-Critical-specialties)
- [NATO NSPA Selects Skydio for Nano UAS Framework (Skydio Blog, August 2025)](https://www.skydio.com/blog/skydio-drones-selected-NATO-nspa-for-nano-uas-framework-agreement)
- [Axon and Skydio Partnership for Public Safety (Axon Investor Relations, June 2024)](https://investor.axon.com/2024-06-20-Axon-and-Skydio-partner-to-deliver-scalable-drone-offering-for-public-safety,-including-Drone-as-First-Responder-solution)
- [Optelos and Skydio Partnership (Optelos Blog, August 2024)](https://optelos.com/skydiopartnership/)
- [FAA Part 107 Autonomy and Remote Pilot Requirements (Skydio Blog)](https://www.skydio.com/blog/part-107-autonomy-skydio-drone)
- [FAA Regulations on Remote Pilots in Command](https://www.faa.gov/uas/commercial_operators)
- [Skydio X10 Gen 2 Hardware Upgrades (Skydio Support, June 2025)](https://support.skydio.com/hc/en-us/articles/39423158528795-Skydio-X10-Gen-2)
- [DIU Blue UAS Cleared List and Framework Platforms](https://www.diu.mil/latest/blue-uas-refresh-list-and-framework-platforms-and-capabilities-selected)
- [Skydio NightSense Approved for Blue UAS (Skydio Blog)](https://www.skydio.com/blog/skydio-nightsense-is-now-blue-uas-approved)
- [IEEE Spectrum — Skydio Dock Enables Long-Term Autonomy](https://spectrum.ieee.org/skydios-dock-in-a-box-enables-longterm-autonomy-for-drone-applications)
- [Independent Evaluation of Skydio X10 Specifications (Origin of Bots, 2026)](https://www.originofbots.com/robot/skydio-x10-by-skydio-details-specifications-rating)
- [Loyalty Drones Skydio X10 Review (2025)](https://loyaltydrones.com/skydio-x10-ultimate-guide-2025-breaking-news-latest-updates-complete-analysis/)
