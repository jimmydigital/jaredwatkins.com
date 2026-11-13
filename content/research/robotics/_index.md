---
title: Robotics Research
date: 2026-03-24
lastmod: 2026-08-27
draft: false
description: Research on commercial robotics platforms, components, and the companies and people building them.
research_area: "robotics"
last_reviewed: 2026-08-27
stale_after_days: 365
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---

{{<steering>}}

## Robotics — Steering Instructions

**Editorial priority:** The component and subsystem layer — motors, gearboxes, LiDAR sensors, radio subsystems, battery packs — not the platform OEMs. Platform OEM entries (DJI, Boston Dynamics, etc.) provide market context, but the more interesting entries are the materials company solving motor efficiency, the startup building a better harmonic drive, or the researcher commercializing a new LiDAR architecture.

**Value chain position** — every company entry must be described by its position:
- **Platform OEM** — sells a complete, ready-to-use robot to end customers (DJI, Boston Dynamics, Knightscope, AeroVironment)
- **Component/subsystem supplier** — sells components or subsystems to OEMs or integrators (T-Motor, Maxon, Ouster, u-blox, Silvus, Intelligent Energy)
- **Software/AI layer** — sells autonomy software that runs on hardware platforms (Shield AI Hivemind, Skydio AI stack)
- **Integrator** — assembles third-party components into custom platforms for specific verticals

When a company operates at multiple layers (e.g., DJI makes its own motors AND sells complete drones), note both roles and describe the vertical integration explicitly — it is a significant competitive moat worth documenting.

**Claim verification for robotics — categories requiring scrutiny in every entry:** Endurance claims (confirm test conditions: payload, speed, altitude, temperature — quoted figures almost always assume ideal/unloaded conditions); autonomy claims ("fully autonomous," "zero operator required" — establish human-in-the-loop reality and what regulatory approvals are required and obtained, including FAA Part 107 waivers, BVLOS approvals); unit deployment figures (distinguish units sold vs. units in active service vs. cumulative lifetime deliveries); defense contract claims (verify against USASpending.gov or SAM.gov where possible — press releases routinely overstate contract scope).

**Defense and dual-use notation** for entries with significant defense business: note active DoD contracts and programs (public); note ITAR or EAR implications for export; if a UAS platform appears on the Blue UAS framework (DoD-approved drone procurement list), note explicitly — it is a material commercial differentiator in the US government market. For defense UGV programs, reference the relevant Army program office (DEVCOM GVSC, PEO Soldier) when documenting contracts.

**DJI specifically:** DJI is on the US DoD Chinese military company list and the FCC Covered List (as of 2022–present). The American Security Drone Act (signed 2023) prohibits US federal agencies from procuring DJI and other covered drones. Every DJI entry must prominently note these designations and their practical implications — the regulatory overhang is a material risk that must be documented.

**Rare earth dependency** is a pervasive, often underdiscussed supply chain risk throughout the robotics hardware stack. NdFeB permanent magnet BLDC and servo motors depend on neodymium and dysprosium; China controls ~85% of global rare earth mining and ~90% of processing. This affects every motor and actuator regardless of where the final robot was assembled. Note it in any motor or actuator entry.

**People network clusters in robotics** — flag connections to these origin clusters explicitly (in addition to the global people tracking format):
- Carnegie Mellon Robotics Institute (Red Whittaker field robotics lab; AMR company founders)
- MIT CSAIL and AeroAstro (drone and autonomy startups; Russ Tedrake manipulation group)
- Stanford SAIL/ME (manipulation, legged robots; DJI co-founder Frank Wang, Stanford dropout)
- iRobot alumni diaspora (wide spread after Amazon acquisition 2022)
- DJI engineering alumni (several competing drone company founders)
- DARPA PMs who funded foundational robotics programs and later joined portfolio companies — document these explicitly; the DARPA PM → company advisor/board pipeline is common and worth tracking
- Ex-Uber ATG / Waymo / Cruise / Aurora engineers moving into AMR and delivery robot startups

**Subsection review cadence:**
- Aerial drones, Ground drones, Sensors/LiDAR, Power systems: 90 days (fast-moving, regulatory changes)
- Actuators, Communications: 180 days

**What NOT to include (robotics-specific):** Hobbyist or purely recreational products with no commercial or professional market relevance; "announced" products with no hardware prototype publicly demonstrated (document announcement date, mark Key Facts status as "Announced / Undemonstrated"); AV companies not primarily in the robotics market (Waymo, Cruise, Mobileye — separate AV section); humanoid robots (track in dedicated `humanoid/` subsection when the area warrants it — do not fold into ground-drones); traditional fixed-factory industrial robot arms (FANUC, Kuka, ABB, Yaskawa) — incumbents table only; simulation software platforms (Isaac Sim, Gazebo) — context but not primary entries.

{{</steering>}}

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


## Overview

Tracks commercial robotics platforms, component suppliers, and the people and capital moving through the industry. Organized by platform type (aerial drones, ground drones/UGVs, AMR/logistics, industrial robots, humanoids) and category (actuators, sensors, communications, power systems, software/integration). Editorial focus is on the component and subsystem layer — the suppliers that determine the performance, cost, and geopolitical risk profile of deployed robot systems.

## Key Themes

- Chinese dominance at critical hardware chokepoints (DJI in aerial, Geek+ in AMR, Hesai/RoboSense in LiDAR, Quectel in cellular modules, CATL/Grepow in batteries)
- Rare earth dependency throughout the motor and actuator stack — a systemic but underreported risk
- LiDAR commoditization driven by Chinese manufacturers vs. US/Israeli players
- US federal procurement bans (Blue UAS framework) creating a bifurcated commercial and government market
- Defense UGV programs accelerating commercial robotics technology transfer in both directions
- Hydrogen fuel cells emerging as a credible alternative to batteries for extended endurance applications
- Humanoid robot sector experiencing a valuation bubble: Chinese manufacturers dominate unit volume (~90% of 2025 shipments), US companies dominate private valuations; autonomy claims broadly unverified
- Naval/maritime autonomy emerging as a major defense procurement category; US Navy MUSV/LUSV programs driving large ASV startup valuations (Saronic at $9.25B); no Chinese/foreign-dominated supply chain problem here
- Micro-miniature connectors split sharply by tier: mil-spec Micro-D/circular connectors (Omnetics, Positronic, Nicomatic, Fischer, ODU) are manufactured almost entirely in the US/EU due to ITAR and qualification requirements, while commodity drone battery quick-disconnects (XT/AS series) are dominated by Chinese manufacturer Amass
- Flight controller hardware sits on an open-hardware standard (Pixhawk) and open-source firmware (PX4/ArduPilot), but the US Blue UAS Framework is a deliberate government intervention to keep the *manufacturing* layer domestic even where the design and firmware are open
- ESC firmware is a documented single-vendor collapse case study: BLHeli AS ceased operations in June 2024, leaving the open-source AM32 project as the primary successor for a firmware layer nearly the entire hobbyist/prosumer drone industry depended on
- Camera gimbal stabilization splits into vertically integrated platform OEMs (DJI, Freefly Systems) and independent component suppliers selling to third-party integrators (Gremsy) — the same OEM-vs-component-supplier split recurring across propulsion, connectors, and now gimbals
- Two of the most established propeller specialists (APC, Xoar) are US-manufactured, a notable exception to the Chinese concentration in the adjacent motor/ESC layers of the propulsion stack
- Additive manufacturing (3D printing) has crossed from prototyping into genuine production-volume drone airframe manufacturing, lowering the capital/tooling barrier to entry for new platform startups
- Renishaw holds a 50% ownership stake in magnetic encoder specialist RLS — a reminder that nominally separate component brands in a supply chain can share deeper ownership ties than they first appear to
- Slip rings and tracking antennas are comparatively under-concentrated risk areas so far: no single-vendor chokepoint on the scale of BLHeli AS or Amass has been identified in either subsection to date
- Dexterous hands have shifted from a hardware-scarcity problem to a reliability/repairability problem: Chinese manufacturer Inspire Robots went from ~2,000 to 10,000+ units delivered year-over-year, but no manufacturer has published a certified 10,000-hour MTBF for multi-jointed fingers as of mid-2026
- Established industrial component manufacturers (Bosch, Schaeffler, Samsung, HL Mando) are increasingly taking direct equity stakes in humanoid-adjacent hardware specialists (Neura Robotics, Tesollo) rather than only supplying components at arm's length — a notable shift in how incumbents are positioning for the humanoid buildout
- A wave of small European "sovereign UAS" entrants is marketing edge-AI, GPS-denied autonomy as the answer to the electronic-warfare environment demonstrated in Ukraine — but the architecture is now near-universal in the segment and most of these firms publish no specifications, no team, and no independent validation ([Sentinel Robotics]({{< relref "aerial-drones/sentinel-robotics.md" >}}) is recorded as a stub on exactly these grounds). Treat "sovereign + edge-AI" positioning as a market frame, not evidence of capability.
- Home/consumer humanoid robots moved from announcement to open pre-order in this period (1X NEO, Oct 2025) and Western industrial players (Neura Robotics' 4NE1 Mini) are explicitly targeting household tasks alongside commercial/industrial use, not just US and Chinese consumer entrants

## Subsections

- [Aerial Drones]({{< relref "aerial-drones/_index.md" >}}) — UAS platforms, defense/commercial, Blue UAS framework
- [Naval Drones / ASVs]({{< relref "naval-drones/_index.md" >}}) — Autonomous surface vessels for defense and maritime operations (Saronic, HavocAI, Anduril+HD Hyundai, MASC program)
- [Undersea Drones / AUVs]({{< relref "undersea-drones/_index.md" >}}) — Autonomous underwater vehicles and drone submarines (Anduril Ghost Shark/Dive-XL/Copperhead, L3Harris Iver4, Lockheed Lamprey)
- [Ground Drones / UGVs]({{< relref "ground-drones/_index.md" >}}) — Legged, wheeled, agricultural, delivery UGVs
- [AMR & Logistics]({{< relref "amr-and-logistics/_index.md" >}}) — Warehouse AMRs, picking robots, fleet management (6 River, Locus, Fetch, Geek+)
- [Industrial Robots & Cobots]({{< relref "industrial-robots/_index.md" >}}) — Robot arms and cobots; Universal Robots; FANUC/ABB/KUKA/Yaskawa context
- [Humanoid Robots]({{< relref "humanoid/_index.md" >}}) — US and non-US companies; autonomy claims; specialized robot debate
- [Robotic Hands & Dexterous Manipulation]({{< relref "hands/_index.md" >}}) — Multi-fingered end effectors for humanoid/industrial manipulation; Inspire Robots, Tesollo, PSYONIC
- [Software & Integration]({{< relref "software-and-integration/_index.md" >}}) — Middleware, fleet orchestration, WMS integration (SVT Robotics, Robust AI, Vecna)
- [Actuators]({{< relref "actuators/_index.md" >}}) — Harmonic drives, servo motors, gearboxes
- [Sensors]({{< relref "sensors/_index.md" >}}) — LiDAR, radar, GNSS, vision
- [Communications]({{< relref "communications/_index.md" >}}) — Mesh radio, cellular modules
- [Power Systems]({{< relref "power-systems/_index.md" >}}) — Batteries, fuel cells, wireless charging
- [Connectors]({{< relref "connectors/_index.md" >}}) — Micro-miniature power and data connectors: Micro-D/Nano-D, high-speed board-to-board, and drone battery quick-disconnects
- [Space Robotics]({{< relref "space-robotics/_index.md" >}}) — Planetary drills, rock abrasion tools, and mechanisms for extreme off-Earth environments (Honeybee Robotics); autonomous orbital defense spacecraft (True Anomaly)
- [ROS 2 Ecosystem]({{< relref "ros2/_index.md" >}}) — ROS 2 middleware, PickNik/MoveIt Pro, and the hardware compatibility ecosystem
- [EtherCAT]({{< relref "ethercat/_index.md" >}}) — Real-time Ethernet fieldbus for multi-axis motion control; protocol architecture, key companies, FSoE safety, open-source tooling, and limitations
- [Flight Controllers / Autopilot Hardware]({{< relref "flight-controllers/_index.md" >}}) — Pixhawk standard, PX4/ArduPilot, Blue UAS Framework, ModalAI, Auterion
- [Electronic Speed Controllers]({{< relref "escs/_index.md" >}}) — ESC hardware and firmware; BLHeli/BLHeli_32/AM32 lineage; Hobbywing, APD
- [Gimbals & Camera Stabilization]({{< relref "gimbals/_index.md" >}}) — Brushless gimbal stabilization; Gremsy, Freefly Systems, DJI
- [Propellers & Propulsion Mechanics]({{< relref "propellers/_index.md" >}}) — Composite and carbon fiber propeller design/materials; APC Propellers, Xoar International
- [Airframe Structural Materials]({{< relref "airframe-materials/_index.md" >}}) — Carbon fiber composite fabrication and additive manufacturing for drone/robot frames; DragonPlate, HP Additive Manufacturing
- [Bearings]({{< relref "bearings/_index.md" >}}) — US thin-section, precision and thrust bearing makers: SKF Kaydon, Schatz, NHBB, Auburn
- [Magnets]({{< relref "magnets/_index.md" >}}) — US permanent magnet producers and developers: Noveon, Vulcan Elements, USA Rare Earth, Niron
- [Motor Materials]({{< relref "motor-materials/_index.md" >}}) — US motor laminations and winding wire: Thomson Lamination, Laser Technologies, Tempel, Rea, MWS, Essex
- [Encoders]({{< relref "encoders/_index.md" >}}) — Magnetic and optical rotary encoders for robot joint/motor feedback; RLS, Renishaw
- [Slip Rings]({{< relref "slip-rings/_index.md" >}}) — Rotary electrical interfaces for continuous gimbal/joint rotation; Fabricast, MOFLON
- [Antennas]({{< relref "antennas/_index.md" >}}) — Directional and auto-tracking antennas for long-range UAS command-and-control; Troll Systems, AeroVironment
