---
title: "Anduril Industries — Autonomous Systems & Drones"
date: 2026-04-05
lastmod: 2026-04-05
draft: false
description: "Anduril autonomous systems angle: Fury YFQ-44A CCA in production at Arsenal-1 (March 2026); Roadrunner reusable turbojet interceptor; Altius-600/700 loitering munitions; Anvil/Pulsar/Sentry CUAS stack; Ghost Shark XL-AUV maritime; Barracuda cruise missile. All platforms are Lattice OS nodes."
tags: ["robotics", "aerial-drone", "autonomous-systems", "defense", "us", "private", "counter-uas", "loitering-munition", "cca", "maritime"]
categories: ["company"]
research_area: "robotics/aerial-drones"
source_urls:
  - "https://www.anduril.com/fury"
  - "https://www.anduril.com/roadrunner"
  - "https://www.anduril.com/anvil"
  - "https://www.anduril.com/counter-uas"
  - "https://breakingdefense.com/2026/03/as-fury-production-starts-anduril-pledging-a-different-production-approach-at-arsenal-1/"
  - "https://theaviationist.com/2026/03/24/yfq-44a-fury-cca-is-now-in-production/"
last_reviewed: 2026-04-05
stale_after_days: 60
related:
  - "datacenters/rugged-edge-compute/anduril.md"
---

> **Company overview, key people, funding, Lattice OS, Menace-T/X edge compute, and the $20B Army contract are covered in the canonical file:** [Anduril Industries]({{< relref "/research/datacenters/rugged-edge-compute/anduril.md" >}}). This file covers the autonomous systems and drone product portfolio specifically.

## Autonomous Systems Portfolio

Anduril builds a coordinated portfolio of autonomous platforms across aerial, counter-UAS, and maritime domains — not a single product category. Every platform feeds into and is cued by Lattice OS, making the portfolio an integrated kill chain rather than a collection of standalone products.

| Platform | Type | Domain | Status |
|----------|------|--------|--------|
| **Fury (YFQ-44A)** | Collaborative Combat Aircraft (CCA) | Aerial | In production — Arsenal-1, March 2026 |
| **Roadrunner** | Reusable turbojet interceptor | Aerial / CUAS | Low-rate production; operationally deployed |
| **Barracuda** | Cruise missile | Aerial / Strike | Arsenal-1 production by end-2026 |
| **Altius-600/700** | Tube-launched loitering munition | Aerial | Fielded (acquired via Area-I, 2021) |
| **Anvil** | Kinetic counter-drone interceptor | Counter-UAS | Fielded; Lattice-cueable |
| **Pulsar** | Directed RF/EW counter-drone | Counter-UAS | Fielded |
| **Sentry Tower** | Autonomous surveillance tower | Surveillance | Fielded; US border and military installations |
| **Wisp / Spyglass / Spark** | Distributed sensor nodes | Counter-UAS | Fielded as Lattice sensor network |
| **Ghost Shark XL-AUV** | Extra-large autonomous underwater vehicle | Maritime | In development (ADF partnership) |
| **Dive-LD** | Large displacement AUV | Maritime | Operational |

## Platform Details

### Fury YFQ-44A — Collaborative Combat Aircraft

Anduril's bid for the US Air Force CCA program — an autonomous wingman designed to fly alongside manned F-35s and F-22s, absorbing attrition risk and extending sensor/weapons reach. Production began at Arsenal-1 in March 2026, ~4 months ahead of the original July 2026 schedule.

- **Wingspan:** ~17 ft (5.2 m); subsonic; stealthy configuration
- **Production line:** 22 workstations at Arsenal-1; capacity ~150 aircraft/year per shift at full rate
- **Autonomy:** Lattice-integrated; human-supervised autonomous wingman; operates in GPS-denied/comms-degraded environments
- **Competition:** Competing against Shield AI's CCA platform for USAF selection; both are in parallel developmental production

### Roadrunner — Reusable Interceptor

A 6-foot twin-turbojet delta-wing autonomous aircraft that operates as both a reusable interceptor and an expendable kinetic effector (Roadrunner-M variant). Unique economics: only expends itself on a successful intercept; returns to base if mission is aborted.

- **Speed:** High subsonic (approaching Mach 0.9); VTOL capable
- **Roles:** Counter-cruise missile, counter-drone, counter-aircraft; Roadrunner-M carries kinetic warhead
- **Production:** Low-rate production for US government order of "hundreds of units" (announced December 2023)
- **International:** Demonstrated in Australia (September 2024); ADF CUAS interest

### Altius — Tube-Launched Loitering Munitions

Acquired via Area-I (2021). Multi-role loitering munitions deployable from ground, aircraft (MQ-9 Reaper), ships, and submarines.

- **Altius-600:** ~280-mile range; up to 4 hours endurance; 13.8 lbs; modular payload (kinetic, EW, comms relay, ISR)
- **Altius-700:** Larger, higher-payload; details classified
- **Swarm-capable:** Lattice-coordinated multi-unit operations in GPS-denied environments

### Anvil and the CUAS Stack

The full Anduril counter-UAS system is a sensor-to-effector stack unified under Lattice, not a single product:

- **Sentry Tower / Spyglass:** Radar and EO/IR detection; AI threat classification; Lattice nodes
- **Wisp / Spark:** Distributed small sensor nodes for wide-area coverage
- **Anvil:** Kinetic interceptor that physically rams small UAS; ~200 mph; autonomous terminal guidance
- **Pulsar:** Directed RF/EW for non-kinetic neutralization
- **Roadrunner-M:** Kinetic intercept for higher-value threats (cruise missiles, aircraft)

This full stack is the primary deliverable for the $20B Army Lattice enterprise contract.

### Ghost Shark and Maritime Platforms

**Ghost Shark XL-AUV** is a long-range extra-large autonomous underwater vehicle co-developed with the Australian Defence Force for ISR and undersea warfare in the Indo-Pacific. In development as of 2026; relevant to AUKUS undersea warfare requirements. **Dive-LD** is an operational large-displacement AUV already in service.

## Arsenal-1 Manufacturing

The $1B Arsenal-1 facility in Pickaway County, Ohio (~20 miles south of Columbus) is central to Anduril's transition from software-first startup to production-scale manufacturer.

- **March 2026:** Fury production begins (~4 months early); 22 production workstations
- **End-2026:** Roadrunner, Barracuda, and one classified platform added
- **Capacity:** ~150 Fury/year per shift; designed to scale to tens of thousands of autonomous systems annually
- **SRM supply:** McHenry, Mississippi facility (operational August 2025) provides propulsion for Roadrunner and Altius — first new US solid rocket motor production in 50 years

## Notable Developments

- **2026-03:** Fury YFQ-44A production begins at Arsenal-1; ~4 months ahead of schedule
- **2026-03:** $20B Army Lattice enterprise contract — CUAS stack is a core deliverable (see canonical file)
- **2025-08:** McHenry SRM facility opens; propulsion supply chain vertically integrated
- **2024-09:** Roadrunner demonstrated in Australia; first international CUAS deployment
- **2024:** Ghost Shark XL-AUV program announced with ADF
- **2023-12:** Roadrunner publicly revealed; low-rate production authorized
- **2021:** Area-I acquisition — brought Altius family into portfolio

## Competitive Position

| Competitor | Overlap | Key Difference |
|-----------|---------|----------------|
| [Shield AI]({{< relref "/research/robotics/aerial-drones/shield-ai.md" >}}) | CCA (YFQ-44A vs. Shield AI platform); autonomy software | Shield AI leads with Hivemind software + V-BAT hardware; both competing for USAF CCA |
| [AeroVironment]({{< relref "/research/robotics/aerial-drones/aeroviroment.md" >}}) | Loitering munitions (Altius vs. Switchblade) | AeroVironment fielded at scale; Altius more capable but earlier stage |
| [Skydio]({{< relref "/research/robotics/aerial-drones/skydio.md" >}}) | Autonomous small UAS | Skydio is commercial-rooted moving into defense; Anduril is defense-native |

## Sources

- [Anduril — Fury](https://www.anduril.com/fury)
- [Anduril — Roadrunner](https://www.anduril.com/roadrunner)
- [Anduril — Anvil](https://www.anduril.com/anvil)
- [Anduril — Counter-UAS](https://www.anduril.com/counter-uas)
- [Breaking Defense — Fury production at Arsenal-1 (March 2026)](https://breakingdefense.com/2026/03/as-fury-production-starts-anduril-pledging-a-different-production-approach-at-arsenal-1/)
- [The Aviationist — YFQ-44A in production (March 24, 2026)](https://theaviationist.com/2026/03/24/yfq-44a-fury-cca-is-now-in-production/)
- [Breaking Defense — Roadrunner in Australia (September 2024)](https://breakingdefense.com/2024/09/anduril-brings-roadrunner-drone-and-solid-rocket-motor-to-australia-for-first-time/)
