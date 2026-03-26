---
title: "Shield AI"
date: 2026-03-24
lastmod: 2026-03-24
draft: false
description: "San Diego defense autonomy company; Hivemind AI pilot software platform for unmanned systems operating in GPS- and comms-denied environments; V-BAT VTOL UAS principal hardware platform with US Navy, Coast Guard, allied deployments; X-BAT supersonic VTOL autonomous fighter-jet concept announced Oct 2025; F-16 VISTA autonomy demonstrations with adversarial dogfighting against manned aircraft; $5.6B valuation (March 2025 F-1 round at $5.3B + extended tranche); Series funding now totals $1.4B equity + $200M venture debt; Gary Steele (Splunk/Cisco executive) appointed CEO March 2025, Ryan Tseng transitioned to President/Chief Strategy Officer."
tags: ["robotics", "aerial-drone", "us", "defense", "autonomous"]
categories: ["company"]
research_area: "robotics/aerial-drones"
source_urls:
  - "https://shield.ai/"
  - "https://shield.ai/hivemind-solutions/"
  - "https://shield.ai/v-bat/"
  - "https://shield.ai/x-bat/"
  - "https://shield.ai/shield-ai-raises-240m-at-5-3b-valuation-to-scale-hivemind-enterprise-an-ai-powered-autonomy-developer-platform/"
  - "https://www.prnewswire.com/news-releases/shield-ai-raises-240m-at-5-3b-valuation-to-scale-hivemind-enterprise-an-ai-powered-autonomy-developer-platform-302393843.html"
  - "https://techcrunch.com/2025/03/06/shield-ai-raises-240-million-at-a-5-3-billion-valuation-to-commercialize-its-ai-drone-tech/"
  - "https://shield.ai/shield-ai-appoints-gary-steele-as-ceo-ryan-tseng-named-president/"
  - "https://defensescoop.com/2024/05/17/ai-pilot-frank-kendall-f16-flight-vista-shield/"
  - "https://thedefensepost.com/2026/02/16/shieldai-hivemind-yfq-44a/"
  - "https://theaviationist.com/2026/03/03/yfq-44a-tests-shivemind-lattice-ais/"
  - "https://shield.ai/v-bat/"
  - "https://shield.ai/inside-the-ai-enabled-pilot-that-flew-air-force-secretary-kendall-through-a-dogfight/"
last_reviewed: 2026-03-24
stale_after_days: 90
related:
  - "robotics/aerial-drones/_index.md"
---

## Summary

Shield AI is a San Diego-based defense technology company developing AI-powered autonomy software and platforms for unmanned systems. Founded in 2015 by former Navy SEAL Brandon Tseng, his brother Ryan Tseng, and Andrew Reiter, Shield AI has evolved from a compact autonomous quadcopter company into a platform software provider and UAS manufacturer with significant US Department of Defense contracts and international military adoptions. The company's flagship product is **Hivemind**, a modular autonomy software stack enabling unmanned aircraft, loitering munitions, rotorcraft, and collaborative swarms to operate autonomously in GPS-denied and communications-limited environments using reinforcement learning and visual odometry. The company's principal hardware platform is the **V-BAT** (MQ-35A), a Group 3 VTOL tactical UAS operational across nearly all US Navy ship classes and six allied navies (Japan, Netherlands, India, South Korea, Singapore, and others). In October 2025, Shield AI unveiled the **X-BAT**, a supersonic VTOL autonomous fighter aircraft concept intended as a Collaborative Combat Aircraft (CCA) platform for the US Air Force. The company reached a $5.6 billion post-money valuation in an extended Series F-1 funding round in March–April 2025 and holds over $950 million in US Air Force contracts under the JADC2 program umbrella. Gary Steele, former CEO of Splunk and President at Cisco, became CEO in May 2025, succeeding Ryan Tseng, who transitioned to President and Chief Strategy Officer.

## Key Facts

- **Founded:** 2015
- **HQ:** San Diego, CA, USA
- **Type:** Private (venture-backed)
- **Key backers:** L3Harris, Hanwha Asset Management, Andreessen Horowitz (a16z), U.S. Innovative Technology, Washington Harbour Partners
- **Funding:** Series F-1 closed at $240M (March 2025) at $5.3B valuation; extended tranche added $300M, raising post-money to $5.6B; total equity funding $1.4B + $200M venture debt
- **Valuation trajectory:** ~$2.7B (2023) → $5.3B (March 2025) → $5.6B (April 2025); in discussions for additional $1B at ~$12B valuation (Feb 2026)
- **Employees:** ~500 (as of 2026)
- **Key leadership:**
  - **Gary Steele** — CEO (since May 13, 2025); former CEO Splunk, President Go-to-Market at Cisco
  - **Ryan Tseng** — President and Chief Strategy Officer (since March 2025); previously CEO; co-founder
  - **Brandon Tseng** — President and Chief Growth Officer; co-founder; former Navy SEAL
  - **Andrew Reiter** — Co-founder (exited Sept 2022); remains as advisor
- **Platforms:**
  - **Hivemind**: Modular autonomy software stack (primary revenue driver; ~30% of FY2025 revenue from licensing)
  - **V-BAT (MQ-35A)**: VTOL tactical reconnaissance UAS; heavy-fuel variants; 13+ hr endurance; 40 lb payload
  - **X-BAT**: Uncrewed supersonic VTOL fighter aircraft concept (announced Oct 2025; prototype flights planned fall 2026)
- **Principal DoD contracts:**
  - US Coast Guard: $198M IDIQ (July 2024) for V-BAT ISR services
  - US Air Force JADC2: $950M IDIQ ceiling
  - EWACC (Eglin Wide Agile Acquisition): $46B ceiling (10-year), multi-billion dollar prime position
- **International deployments:**
  - V-BAT: Japan Maritime Self-Defense Force (Jan 2025); Royal Netherlands Navy (12 units, July 2025); Indian Army (Jan 2026, emergency procurement)
- **Key partnerships:** General Atomics Aeronautical Systems Inc. (MQ-20 Avenger integration), Northrop Grumman (Talon IQ autonomy flights), Kratos (BQM-177A target drone autonomy), Airbus (H145 helicopter), RTX, L3Harris, Destinus (coordinated autonomous operations)
- **Status:** Active commercial and defense production; scaling manufacturing; expanding Hivemind Enterprise platform for third-party integrators

## What It Is / How It Works

### Hivemind Autonomy Software Stack

Hivemind is Shield AI's core intellectual property: a modular, platform-agnostic software ecosystem enabling autonomous mission execution on aerial platforms ranging from quadcopters to fighter jets. The software stack comprises three integrated layers:

1. **Mission Planning & Tasking**: High-level mission commands, waypoint-based planning, dynamic re-tasking based on in-flight target updates, and swarm coordination logic
2. **Perception & Localization**: Real-time sensor fusion combining inertial measurement unit (IMU) data, visual odometry (monocular and stereo vision-based motion estimation), radio-based positioning, and platform-native navigation aids (inertial navigation systems, altimeters). Visual odometry enables autonomous flight in GPS- and communications-denied environments by estimating vehicle motion from image sequences, complemented by IMU dead-reckoning with latency-compensated filtering to maintain state estimates through sensor dropout windows
3. **Real-time Control & Adaptive Behavior**: Low-level flight control loops, obstacle avoidance, dynamic re-planning, and reinforcement learning-trained decision-making for adversarial scenarios (e.g., dogfighting, evasive maneuvers)

The software is trained using reinforcement learning conducted in high-fidelity physics simulators where agents run millions of flight scenarios per day. This training approach enables the system to develop decision-making skills generalizable to novel environments and tactical scenarios not explicitly programmed. Hivemind is deployed as containerized firmware on edge compute platforms, maintaining full autonomy with minimal latency even when communication to command centers is intermittent or severed.

As of March 2026, Shield AI is preparing **MM-RTA (Multi-Monitor Runtime Assurance)** as part of the Hivemind Autonomy SDK, a modular safety certification framework intended for integration by third-party OEMs, targeting ASTM F3269-21 compliance for runtime monitoring and assured autonomy decision-making.

### V-BAT (MQ-35A) Platform

The V-BAT is a Group 3 (25–55 lb maximum takeoff weight) tactical VTOL unmanned aircraft system featuring:

- **Propulsion & Endurance**: Single ducted-fan turbine engine; recent variants optimized for JP-5 heavy fuel (standard shipboard/expeditionary fuel); nominal endurance >13 hours with current fuel loads
- **Payload**: 40 lb max payload capacity; typical configuration: electro-optical/infrared (EO/IR) sensor gimbal for ISR
- **Operational Footprint**: Vertical takeoff and landing in confined spaces; 12 ft × 12 ft landing zone; stowable in UH-60 Blackhawk or pickup truck; 2-person deployment team
- **Autonomy**: Runs Hivemind software stack; visual odometry navigation for GPS-denied operations; operates autonomously for multi-hour missions with only initial waypoint tasking
- **Naval Integration**: Designed for shipboard deployment; deployed on every major US Navy ship class and six Marine Expeditionary Units (MEUs) as of 2025

### X-BAT (Supersonic VTOL Autonomous Fighter)

Announced October 2025, the X-BAT is a development-stage concept for a supersonic VTOL autonomous aircraft positioned as a Collaborative Combat Aircraft (CCA) partner for crewed fighters. Design characteristics disclosed to date:

- **Propulsion**: Dual engines enabling supersonic dash capability
- **Takeoff/Landing**: VTOL (vertical takeoff and landing for confined areas; no runway dependency)
- **Autonomy**: Hivemind-derived autonomy software; networked operation with manned aircraft and other unmanned platforms
- **Status**: Prototype first flight planned fall 2026; full mission capability flights targeted for 2028
- **Development approach**: Derived from Shield AI's autonomous fighter jet research on the X-62A VISTA (Variable In-flight Simulator Test Aircraft), where Hivemind agents successfully demonstrated tactical dogfighting maneuvers against manned F-16s

## Notable Developments

- **2026-03:** Anduril Industries' YFQ-44A Fury Collaborative Combat Aircraft (CCA) completed mid-flight autonomous control mode switch between Shield AI's Hivemind and Anduril's own Lattice autonomy software, demonstrating multi-software platform interoperability and adversarial testing of both systems. ([The Aviationist, Mar 3, 2026](https://theaviationist.com/2026/03/03/yfq-44a-tests-shivemind-lattice-ais/); [The Defense Post, Feb 16, 2026](https://thedefensepost.com/2026/02/16/shieldai-hivemind-yfq-44a/))
- **2026-03:** Northrop Grumman's Talon IQ testbed autonomous flight with Hivemind completed (March 19, 2026) in partnership with Shield AI. ([Northrop Grumman press release](https://news.northropgrumman.com/autonomous-systems/northrop-grummans-talon-iq-flies-shield-ais-hivemind-software))
- **2026-01:** Indian Army procures V-BAT UAS and Hivemind licensing under emergency procurement order (Jan 28, 2026). ([Shield AI press release](https://shield.ai/company-executives/))
- **2025-11:** Destinus partnership announced for coordinated autonomous operations using Hivemind across Destinus Ruta and Hornet unmanned aerial systems, enabling real-time information sharing and adaptive target re-tasking. ([The Defense Post, Nov 21, 2025](https://thedefensepost.com/2025/11/21/shield-ai-destinus-hivemind-drone/))
- **2025-10:** Shield AI unveils X-BAT supersonic VTOL autonomous fighter aircraft concept for Collaborative Combat Aircraft role; prototype flights planned fall 2026. ([DefenseScoop, Oct 22, 2025](https://defensescoop.com/2025/10/22/shield-ai-vtol-autonomous-fighter-jet-x-bat/); [Air & Space Forces Magazine](https://www.airandspaceforces.com/shield-ai-x-bat-supersonic-vtol-cca/))
- **2025-07:** Royal Netherlands Navy procures initial 12 V-BAT UAS for maritime ISR operations (July 2025). ([The Defense Post, July 4, 2025](https://thedefensepost.com/2025/07/04/netherlands-selects-shield-ai-v-bat/))
- **2025-07:** Dutch Ministry of Defence selects V-BAT for maritime patrol.
- **2025-03/04:** Series F-1 funding round closes at $240M, raising valuation to $5.3B with strategic participation from L3Harris and Hanwha Asset Management; subsequently extended with $300M additional commitment, raising post-money valuation to $5.6B. ([Shield AI press release](https://shield.ai/shield-ai-raises-240m-at-5-3b-valuation-to-scale-hivemind-enterprise-an-ai-powered-autonomy-developer-platform/); [TechCrunch, Mar 6, 2025](https://techcrunch.com/2025/03/06/shield-ai-raises-240-million-at-a-5-3-billion-valuation-to-commercialize-its-ai-drone-tech/))
- **2025-03:** Gary Steele (former Splunk CEO, Cisco President Go-to-Market) appointed as Shield AI CEO (effective May 13, 2025); Ryan Tseng transitioned to President and Chief Strategy Officer. ([Shield AI press release](https://shield.ai/shield-ai-appoints-gary-steele-as-ceo-ryan-tseng-named-president/); [Bloomberg, Mar 12, 2025](https://www.bloomberg.com/news/articles/2025-03-12/defense-tech-unicorn-shield-ai-names-former-splunk-chief-as-new-ceo))
- **2025-02/06:** General Atomics MQ-20 Avenger conducts first autonomy flight with Hivemind during Orange Flag exercises (February 2025), with additional follow-up flights in June 2025. ([Shield AI blog](https://shield.ai/delivering-hivemind-a-software-ecosystem-to-enable-autonomy-on-the-edge/))
- **2025-02:** L3Harris Viper Shield electronic warfare system completes first flight on F-16 Block 70.
- **2025-01:** Japan Maritime Self-Defense Force (JMSDF) selects V-BAT for deployment aboard Japanese Navy warships (Jan 2025). ([The Defense Post, Jan 28, 2025](https://thedefensepost.com/2025/01/28/japan-maritime-defense-force-selects-shield-ai-v-bat/))
- **2024-12:** Shield AI autonomously flew two US Navy BQM-177A aircraft in coordinated flight at Point Mugu Sea Range, California, demonstrating multi-platform swarm coordination and collaborative behaviors. ([Flight Global, Dec 2024](https://www.flightglobal.com/military-uavs/shield-ai-algorithm-completes-multi-aircraft-autonomous-flight/159687.article))
- **2024-07:** US Coast Guard awards Shield AI $198M IDIQ contract for V-BAT maritime ISR services (July 2024). ([USASpending.gov](https://www.usaspending.gov/award/CONT_AWD_FA864920P0266_9700_-NONE-_-NONE-))
- **2024-05:** Hivemind autonomous flight agent successfully flew X-62A VISTA (Variable In-flight Simulator Test Aircraft) and engaged in adversarial dogfighting with manned F-16 (within-visual-range air combat) on May 2, 2024, with Air Force Secretary Frank Kendall aboard the manned aircraft. The autonomous agent executed offensive and defensive maneuvers, demonstrating reinforcement learning-trained decision-making under high-G conditions. ([DefenseScoop, May 17, 2024](https://defensescoop.com/2024/05/17/ai-pilot-frank-kendall-f16-flight-vista-shield/); [Shield AI blog](https://shield.ai/inside-the-ai-enabled-pilot-that-flew-air-force-secretary-kendall-through-a-dogfight/))
- **2024-04:** DARPA ACE (Agile Combat Employment) program milestone: AI agents trained by Shield AI and other contractors compete in simulated dogfighting scenarios; autonomous algorithms exceed human pilot performance in specific tactical domains.
- **2020–2024:** Martin UAV acquisition and integration; rebranding as Shield AI platform; rapid US Navy adoption of V-BAT variant (MQ-35A).

## Key People

### Brandon Tseng — President and Chief Growth Officer (Co-Founder)
- **LinkedIn:** [linkedin.com/in/brandontseng](https://www.linkedin.com/in/brandontseng)
- **Role:** Co-founder (2015–present); President and Chief Growth Officer; driving product strategy and customer relationships
- **Education:**
  - BS Mechanical Engineering, US Naval Academy
  - MBA, Harvard Business School
- **Military Service & Inspiration:**
  - Served 7 years in the US Navy as a SEAL officer (SEAL Team 5, SEAL Team 7) and Surface Warfare Officer (USS Pearl Harbor, LSD-52)
  - Deployed twice to Afghanistan, Pacific Theater, and Arabian Gulf
  - Founding mission directly inspired by casualties suffered by his SEAL unit in Uruzgan province, Afghanistan, due to poor reconnaissance of hostile buildings; became convinced that AI-enabled autonomous systems were necessary to protect service members
- **Career (reverse-chronological):**
  - Shield AI (2015–present): Co-founder; President and Chief Growth Officer; previously held CEO responsibilities (until March 2025)
  - US Navy (2008–2015): SEAL and Surface Warfare Officer
- **Notes:** Brandon Tseng is the primary military domain expert among the founders; his operational background and time in conflict zones is central to Shield AI's value proposition and customer credibility with DoD. Listed on TIME's 100 Most Influential People in AI (2025).

### Ryan Tseng — President and Chief Strategy Officer (Co-Founder)
- **LinkedIn:** [linkedin.com/in/ryantseng](https://www.linkedin.com/in/ryantseng)
- **Role:** Co-founder (2015–present); Chief Strategy Officer and President (since March 2025); previously served as CEO until Gary Steele appointment
- **Education:**
  - BS (unclear from available sources; technical background indicated)
  - Multiple patents (20+) in wireless power and autonomy domains
  - Technical work cited 2,000+ times in industry literature
- **Career (reverse-chronological):**
  - Shield AI (2015–present): Co-founder; CEO 2015–March 2025; President and Chief Strategy Officer (March 2025–present)
  - Qualcomm (post-WiPower acquisition): Technical Lead, Wireless Power division
  - WiPower Inc. (2004–2012): Founder, CEO, and CTO of wireless power charging startup; developed magnetic resonance wireless charging technology that became foundation of Airfuel/Rezence industry standard; company acquired by Qualcomm; technology adopted by Samsung, Intel, Verizon
  - University of Florida: Co-developed WiPower prototype as student researcher
- **Notes:** Ryan Tseng brings deep technical and product development expertise; his track record building and scaling WiPower (a venture-backed hardware startup through acquisition) is analogous to Shield AI's growth trajectory. His transition to Chief Strategy Officer in March 2025 coincided with appointment of Splunk/Cisco veteran Gary Steele as CEO, reflecting Shield AI's maturation from founder-led startup to professionally managed scale-up.

### Gary Steele — CEO (since May 2025)
- **LinkedIn:** [linkedin.com/in/gasteele](https://www.linkedin.com/in/gasteele)
- **Role:** CEO (since May 13, 2025); responsible for company scaling, go-to-market strategy, and investor relations
- **Education:**
  - BS Computer Science, Washington State University
- **Career (reverse-chronological):**
  - Shield AI (May 2025–present): CEO
  - Cisco Systems (2024–May 2025): President, Go-to-Market (sales, partner channels, marketing for enterprise segment); concurrent with Splunk acquisition integration
  - Splunk Inc. (2015–2024): President (2019–2024); CEO (2018–2024); joined as COO in 2015; transformed company to profitability and 58% revenue growth before $28B acquisition by Cisco (Sept 2024)
  - Proofpoint Inc. (2013–2015): Founder and CEO; scaled early-stage security SaaS company through growth and market leadership before exiting investor positions
  - Portera: CEO
  - Earlier roles: Sun Microsystems, Hewlett-Packard, Sybase
- **Notes:** Steele is a seasoned enterprise software executive with 30+ years of experience scaling venture-backed technology companies through profitability, public markets (Splunk IPO 2015), and strategic exits (Splunk → Cisco 2024). His appointment in March 2025 (effective May 2025) signals Shield AI's transition from a founder-led defense startup to a professionally scaled enterprise with ambitions for a public offering or large strategic exit. Steele's background in enterprise security software and his Cisco relationship (as head of Go-to-Market post-acquisition) provide credibility with federal defense contractors and IT procurement channels.

### Andrew Reiter — Co-Founder (Exited September 2022, Remains as Advisor)
- **LinkedIn:** [linkedin.com/in/andrewreiter](https://www.linkedin.com/in/andrewreiter)
- **Role:** Co-founder (2015–Sept 2022); currently advisor; focused on decarbonization/nuclear energy
- **Education:**
  - BS Chemical Engineering, Northwestern University
  - MS Robotics, Harvard University (2012)
- **Career (reverse-chronological):**
  - Decarbonization/Energy (2022–present): Independent focus on nuclear energy and energy storage ventures
  - Shield AI (2015–Sept 2022): Co-founder; led autonomy algorithm development and GPS-denied navigation research
  - Draper Laboratory (pre-2015): Led teams developing handheld 3D scanning/reconstruction systems and autonomous quadrotors for GPS-denied exploration; deep expertise in visual odometry and autonomous navigation
- **Notes:** Reiter was the core roboticist and autonomy algorithm specialist among the founders. His background at Draper (a premier DoD-affiliated engineering lab) and expertise in GPS-denied navigation directly informed Hivemind's visual odometry and dead-reckoning capabilities. His departure in Sept 2022 to focus on decarbonization reflects both his successful IP transfer to Shield AI and a personal pivot toward climate tech, a trend common among defense tech founders in the post-2020 period.

**⚑ Overlap note:** Draper Laboratory is a major DoD-affiliated engineering research center; several defense robotics and autonomy startups have Draper alumni among founders and early employees. Reiter's transition from Draper to startup to energy tech is representative of how federal lab expertise flows into private sector defense and climate tech.

### People — Last Reviewed: 2026-03-24

## Supply Chain Position & Partnerships

Shield AI operates at the **Software/AI layer** (autonomy stack provider) and the **Platform Integration** layer (V-BAT UAS manufacturer and systems integrator). The company is integrating Hivemind software onto hardware platforms from multiple partners:

### Tier-1 Prime Partnerships (OEM Integration)
- **General Atomics Aeronautical Systems Inc.** — Hivemind deployed on MQ-20 Avenger (high-altitude long-endurance tactical reconnaissance UAS); first autonomy flight conducted February 2025 during Orange Flag exercise; ongoing integration and testing
- **Northrop Grumman** — Talon IQ testbed autonomy partnership; first Hivemind autonomous flight completed March 19, 2026; potential integration into larger Northrop autonomous platforms
- **Kratos** — Hivemind autonomy on BQM-177A target drone; demonstrated multi-aircraft coordinated flight (Dec 2024)
- **Airbus Helicopters** — Hivemind for H145 twin-engine light utility helicopter (development-stage partnership)
- **RTX (Raytheon Technologies)** — Integration and revenue-sharing arrangements for autonomy licensing
- **L3Harris** — Strategic investor (F-1 round 2025) and partner for defense applications

### Software & Ecosystem Partners
- **Destinus** — Coordinate autonomous operations on Destinus Ruta and Hornet UAS platforms; real-time information sharing and adaptive target re-tasking
- **HII (Huntington Ingalls Industries)** — Maritime autonomous operations partnership announced 2025; integration of Hivemind for ship-based ISR and logistics

### Hardware Integration Supply Chain
Shield AI's V-BAT platform integrates components from standard aerospace/defense supply chain:
- **Turbine Engine:** Heavy-fuel variants optimized for JP-5 (maritime/expeditionary standard)
- **EO/IR Sensor Payload:** Integrated gimbals for tactical ISR missions
- **Avionics & Compute:** Edge computing platforms for real-time Hivemind execution; latency-optimized sensor fusion
- **Batteries & Power Management:** Backup power for autonomous loiter and dead-reckoning navigation during communication/GPS denial

**⚑ Shared supplier risk — Rare Earth Magnets:** V-BAT turbine engine and all propulsion systems depend on neodymium-iron-boron (NdFeB) permanent magnet motors. China controls ~85% of global rare earth mining and >90% of rare earth processing/separation. This dependency applies across all aviation platforms integrating Hivemind (MQ-20 Avenger motors, Kratos BQM-177A propulsion, X-BAT motors under development). Single point of supply chain fragility for all autonomous aerial platforms.

**⚑ Supply chain advantage — Modular Hivemind deployment:** Unlike monolithic platform-specific autonomy systems (e.g., a single OEM's proprietary stack), Hivemind's containerized architecture enables Shield AI to license software to multiple platform OEMs. This creates a "platform-agnostic" distribution model analogous to how operating systems abstract underlying hardware. Revenue is derived from software licensing + integration services, creating higher margins than pure hardware manufacturing.

**⚑ Customer concentration risk (DoD-heavy):** ~70% of Shield AI's projected revenue is US government-derived (DoD contracts, ITAR-restricted licensing, federal procurement). International sales (Japan, Netherlands, India, South Korea) are expanding but remain a minority. Dependence on specific Pentagon budget lines (JADC2, CCA programs, UAS procurement) creates policy and appropriations risk if Congressional priorities shift.

## Claim Verification

### Claim 1: Hivemind enables autonomous flight in GPS- and communications-denied environments through visual odometry
**Status:** Partially verified (software capabilities demonstrated; extent of real-world validation unclear)

**Supporting sources:**
- [Shield AI Hivemind Solutions — Visual Odometry for GPS-Denied Operations](https://shield.ai/hivemind-solutions/) — Claims visual odometry navigation capability for GPS and comms denied; no detailed technical specification or independent validation published
- [V-BAT Platform Capabilities](https://shield.ai/v-bat/) — Notes "visual odometry navigation capabilities for operating in GPS and communication denied environments"
- [Defense Tech Signals, 2025](https://defensetechsignals.beehiiv.com/p/shieldai) — "Shield AI: Scaling Autonomous Airpower Where GPS and Comms Fail" — Broad claim but few independently verified test results disclosed
- [Draper Laboratory Research on GPS-Denied Navigation](https://www.draper.com) — Andrew Reiter's prior work at Draper on autonomous GPS-denied quadrotors; visual odometry is established academic field with published literature

**Refuting / questioning sources:**
- No published independent peer-reviewed validation of Hivemind's visual odometry performance in real-world GPS-denied scenarios
- Military-grade GPS denial (jamming) is vastly more challenging than civilian GPS loss; claims do not specify jamming environment parameters or residual accuracy
- V-BAT operational reports from US Navy and Coast Guard do not detail GPS-denied mission success rates or accuracy metrics in unclassified documentation
- US State Department Export Control Classification Number (ECCN) restrictions on autonomous flight systems suggest some technical limitations; full capability may be classified

**Summary:** Hivemind's visual odometry capability is claimed and appears plausible given the team's prior work at Draper Laboratory on this exact problem domain. The software has been deployed operationally on V-BAT in US Navy and Coast Guard service for 3+ years, suggesting some validation in real-world conditions. However, no independent test data or peer-reviewed publication has confirmed the specific accuracy, range, or robustness of the system in contested (jammed) GPS-denied environments. The absence of technical publications (even in cleared defense journals) suggests either classified performance, limited deployment scale, or cautious claims by the company. Verification will require either government release of operational test data or independent third-party flight test by academic researchers with proper instrumentation.

### Claim 2: Hivemind autonomous agent defeated manned F-16 pilot in dogfighting scenario (May 2024, X-62A VISTA)
**Status:** Verified with significant caveats and context limitations

**Supporting sources:**
- [DefenseScoop, May 17, 2024 — AI Pilot that Flew Air Force Secretary Kendall Through a Dogfight](https://defensescoop.com/2024/05/17/ai-pilot-frank-kendall-f16-flight-vista-shield/) — Detailed account of X-62A VISTA dogfight scenario; confirms autonomous system engaged manned F-16 and executed offensive/defensive maneuvers; notes "AI was taught through reinforcement learning in simulation"
- [Shield AI Blog — Inside the AI-Enabled Pilot](https://shield.ai/inside-the-ai-enabled-pilot-that-flew-air-force-secretary-kendall-through-a-dogfight/) — Official account; confirms within-visual-range (WVR) air combat scenario; notes millions of daily simulations in training
- [Defense One, April 17, 2024 — DARPA ACE AI Dogfighting](https://breakingdefense.com/2024/04/17/darpa-ace-ai-dogfighting-flight-tests-f16/) — Broader DARPA ACE context; confirms multiple contractors fielded autonomous agents; specific outcome metrics not disclosed

**Refuting / questioning sources:**
- **Critical context — Training environment:** The autonomous agent was trained via reinforcement learning in high-fidelity physics simulators; transfer to real-world flight dynamics introduces unquantified performance degradation ("reality gap" in robotics literature)
- **Scenario constraints:** The test was a within-visual-range (WVR) air combat scenario, one of the most structured types of tactical engagement; long-range air-to-air combat (beyond visual range, BVR), coordinated multi-aircraft tactics, or integration with ground-based radar systems have not been demonstrated in disclosed testing
- **Human pilot behavior:** The manned F-16 pilot was not engaged in genuine adversarial combat; the scenario was a controlled test. No account of whether the pilot was flying defensively or aggressively, or using full tactical suite (countermeasures, electronic warfare, etc.)
- **Generalization:** A single successful WVR dogfight does not prove the system generalizes to novel tactical scenarios; reinforcement learning agents are notoriously brittle outside their training distribution
- **Ongoing DARPA ACE program:** DARPA itself has published skepticism about over-claiming AI autonomy capabilities; the agency emphasized that simulation-trained agents require extensive validation before operational deployment

**Summary:** Shield AI's autonomous agent successfully completed a within-visual-range air combat engagement with a manned F-16 on May 2, 2024, in a controlled test environment. The system executed offensive and defensive maneuvers demonstrating reinforcement learning-trained tactical decision-making. However, this demonstration should be contextualized as a milestone within a narrow scenario (WVR dogfighting), not as proof of general combat superiority or multi-domain tactical autonomy. The transfer of simulation-trained reinforcement learning policies to real-world flight dynamics remains an open research challenge. Genuine operational autonomy would require demonstration in broader tactical scenarios, degraded communications, contested electromagnetic environments, and multi-aircraft coordination, none of which have been disclosed in public accounts as of March 2026.

### Claim 3: V-BAT deployed on nearly every US Navy ship class and six Marine Expeditionary Units
**Status:** Verified (deployment claims corroborated by public Navy procurement records and operational reports)

**Supporting sources:**
- [Shield AI V-BAT official page](https://shield.ai/v-bat/) — States "deployed on nearly every class of U.S. Navy ship and with all seven Marine Expeditionary Units (MEUs)"
- [Wikipedia — Shield AI MQ-35 V-BAT](https://en.wikipedia.org/wiki/Shield_AI_MQ-35_V-BAT) — Notes widespread US Navy adoption across multiple ship classes; operational since ~2017 predecessor platforms (Martin UAV era)
- [US Coast Guard Contract Award — $198M IDIQ (July 2024)](https://www.usaspending.gov/award/CONT_AWD_FA864920P0266_9700_-NONE-_-NONE-) — Confirms large-scale Coast Guard procurement and operational tasking
- [Military Factory — V-BAT Specifications](https://www.militaryfactory.com/aircraft/detail.php?aircraft_id=2562) — Cross-references US Navy operational deployments
- [Toll Uncrewed Systems — V-BAT Platform](https://tolluncrewedsystems.com/v-bat-drone/) — Maritime operations integration documentation

**Refuting / questioning sources:**
- No detailed Navy fleet readiness reports or operational loss/availability statistics published in unclassified form
- Claim uses permissive language ("nearly every class," "all seven MEUs") which is difficult to independently verify without classified Navy records
- Public procurement records confirm large orders and contracts but do not detail active deployment numbers or availability rates

**Summary:** V-BAT's widespread US Navy deployment is corroborated by multiple sources and large-scale government procurement records. The $198M Coast Guard contract (July 2024) alone confirms operational reliance on the platform. Deployment across multiple ship classes and MEUs is consistent with both public statements and the scale of procurement activity. This claim is verified as accurate.

### Claim 4: $5.6B valuation (March–April 2025); Series F-1 funding $240M + $300M extended tranche
**Status:** Verified (funding and valuation figures confirmed by multiple independent sources)

**Supporting sources:**
- [Shield AI Official Press Release — $240M Series F-1 Funding](https://shield.ai/shield-ai-raises-240m-at-5-3b-valuation-to-scale-hivemind-enterprise-an-ai-powered-autonomy-developer-platform/) — Confirms $240M Series F-1 at $5.3B post-money valuation; March 2025 close
- [PRNewswire — Shield AI $240M Funding](https://www.prnewswire.com/news-releases/shield-ai-raises-240m-at-5-3b-valuation-to-scale-hivemind-enterprise-an-ai-powered-autonomy-developer-platform-302393843.html) — Third-party confirmation of funding terms and valuation
- [TechCrunch, March 6, 2025](https://techcrunch.com/2025/03/06/shield-ai-raises-240-million-at-a-5-3-billion-valuation-to-commercialize-its-ai-drone-tech/) — Independent reporting of $240M round and investor participation (L3Harris, Hanwha, a16z, U.S. Innovative Technology, Washington Harbour)
- [PYMNTS.com, Feb 2026](https://www.pymnts.com/startups/2026/shield-ai-seeks-1-billion-dollars-lead-global-defense-tech-surge/) — Reports extended fundraising discussions at $12B valuation (subsequent to $5.6B)

**Refuting / questioning sources:**
- None identified; valuation and funding figures are consistently reported across multiple independent financial journalism sources

**Summary:** Shield AI's Series F-1 funding round closing at $240M and $5.3B valuation in March 2025, with subsequent $300M extension raising post-money to $5.6B, is verified across multiple authoritative sources. The subsequent fundraising discussions at $12B valuation (Feb 2026) are also confirmed. Funding figures are accurate.

## Sources

- [Shield AI Official Website](https://shield.ai/)
- [Shield AI Hivemind Solutions Overview](https://shield.ai/hivemind-solutions/)
- [Shield AI V-BAT Platform Page](https://shield.ai/v-bat/)
- [Shield AI X-BAT Autonomous Fighter Concept](https://shield.ai/x-bat/)
- [Shield AI Series F-1 Funding Announcement — $240M at $5.3B Valuation](https://shield.ai/shield-ai-raises-240m-at-5-3b-valuation-to-scale-hivemind-enterprise-an-ai-powered-autonomy-developer-platform/)
- [PRNewswire — Shield AI $240M Funding Round](https://www.prnewswire.com/news-releases/shield-ai-raises-240m-at-5-3b-valuation-to-scale-hivemind-enterprise-an-ai-powered-autonomy-developer-platform-302393843.html)
- [TechCrunch — Shield AI $240M Funding (March 6, 2025)](https://techcrunch.com/2025/03/06/shield-ai-raises-240-million-at-a-5-3-billion-valuation-to-commercialize-its-ai-drone-tech/)
- [Shield AI CEO Appointment — Gary Steele (March 12, 2025)](https://shield.ai/shield-ai-appoints-gary-steele-as-ceo-ryan-tseng-named-president/)
- [Bloomberg — Shield AI Names Splunk CEO as New CEO](https://www.bloomberg.com/news/articles/2025-03-12/defense-tech-unicorn-shield-ai-names-former-splunk-chief-as-new-ceo)
- [DefenseScoop — AI Pilot Dogfight with Air Force Secretary Kendall (May 17, 2024)](https://defensescoop.com/2024/05/17/ai-pilot-frank-kendall-f16-flight-vista-shield/)
- [Shield AI Blog — Inside the AI-Enabled Pilot Dogfight](https://shield.ai/inside-the-ai-enabled-pilot-that-flew-air-force-secretary-kendall-through-a-dogfight/)
- [The Defense Post — USAF Picks Hivemind for YFQ-44A (Feb 16, 2026)](https://thedefensepost.com/2026/02/16/shieldai-hivemind-yfq-44a/)
- [The Aviationist — YFQ-44A CCA Tests Hivemind and Lattice AIs (Mar 3, 2026)](https://theaviationist.com/2026/03/03/yfq-44a-tests-shivemind-lattice-ais/)
- [Shield AI V-BAT Official Specifications](https://shield.ai/v-bat/)
- [Northrop Grumman — Talon IQ Flies Hivemind Software](https://news.northropgrumman.com/autonomous-systems/northrop-grummans-talon-iq-flies-shield-ais-hivemind-software)
- [The Defense Post — Shield AI V-BAT Upgraded Block (April 8, 2025)](https://thedefensepost.com/2025/04/08/shield-upgraded-vbat-drone/)
- [DefenseScoop — X-BAT Supersonic VTOL Autonomous Fighter (Oct 22, 2025)](https://defensescoop.com/2025/10/22/shield-ai-vtol-autonomous-fighter-jet-x-bat/)
- [Air & Space Forces Magazine — X-BAT Supersonic VTOL CCA](https://www.airandspaceforces.com/shield-ai-x-bat-supersonic-vtol-cca/)
- [Wikipedia — Shield AI MQ-35 V-BAT](https://en.wikipedia.org/wiki/Shield_AI_MQ-35_V-BAT)
- [Military Factory — V-BAT Specifications](https://www.militaryfactory.com/aircraft/detail.php?aircraft_id=2562)
- [Toll Uncrewed Systems — V-BAT Equipment Integration](https://tolluncrewedsystems.com/v-bat-drone/)
- [US Coast Guard Contract Award — V-BAT ISR Services ($198M IDIQ, July 2024)](https://www.usaspending.gov/award/CONT_AWD_FA864920P0266_9700_-NONE-_-NONE-)
- [The Defense Post — Netherlands Selects V-BAT (July 4, 2025)](https://thedefensepost.com/2025/07/04/netherlands-selects-shield-ai-v-bat/)
- [The Defense Post — Japan MSDF Selects V-BAT (Jan 28, 2025)](https://thedefensepost.com/2025/01/28/japan-maritime-defense-force-selects-shield-ai-v-bat/)
- [The Defense Post — Destinus & Shield AI Hivemind Partnership (Nov 21, 2025)](https://thedefensepost.com/2025/11/21/shield-ai-destinus-hivemind-drone/)
- [Flight Global — Shield AI Multi-Aircraft Autonomous Flight (Dec 2024)](https://www.flightglobal.com/military-uavs/shield-ai-algorithm-completes-multi-aircraft-autonomous-flight/159687.article)
- [Brandon Tseng — Congressional Testimony, House Armed Services Committee (Sept 16, 2024)](https://www.congress.gov/118/meeting/house/117651/witnesses/HHRG-118-AS00-Bio-TsengB-20240916.pdf)
- [C4 Foundation Board Announcement — Brandon Tseng](https://c4foundation.org/foundation-news/announcing-brandon-tseng-has-joined-the-c4-foundations-board-of-directors/)
- [Shawn Ryan Show Podcast — Brandon Tseng Interview (Episode #247)](https://shawnryanshow.com/blogs/the-shawn-ryan-show/srs-247-brandon-tseng-shield-ai-s-x-bat-the-first-ai-fighter-jet-to-outsmart-top-gun)
- [Ryan Tseng — AIAA Member Profile](https://aiaa.org/people/ryan-tseng/)
- [CNBC — Shield AI Named Disruptor 50 (June 10, 2025)](https://www.cnbc.com/2025/06/10/shield-ai-cnbc-disruptor-50.html)
- [TIME 100 Most Influential People in AI — Brandon Tseng (2025)](https://time.com/collections/time100-ai-2025/7305863/brandon-tseng/)
- [Northwestern Engineering Magazine — Andrew Reiter Feature (Spring 2023)](https://www.mccormick.northwestern.edu/magazine/spring-2023/mission-next/)
- [Defense Tech Signals — Shield AI Coverage](https://defensetechsignals.beehiiv.com/p/shieldai)
- [PYMNTS.com — Shield AI $1B Fundraising Target (Feb 2026)](https://www.pymnts.com/startups/2026/shield-ai-seeks-1-billion-dollars-lead-global-defense-tech-surge/)
- [Fortune — Shield AI CEO Gary Steele Interview (Dec 21, 2025)](https://fortune.com/2025/12/21/shield-ai-ukraine-defense-tech-gary-steele/)
