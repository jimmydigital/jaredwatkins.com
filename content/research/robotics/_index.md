---
title: Robotics Research
date: 2026-03-24
lastmod: 2026-07-15
draft: false
description: Research on commercial robotics platforms, components, and the companies and people building them.
research_area: "robotics"
last_reviewed: 2026-03-24
stale_after_days: 365
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---

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

## Subsections

- [Aerial Drones]({{< relref "aerial-drones/_index.md" >}}) — UAS platforms, defense/commercial, Blue UAS framework
- [Naval Drones / ASVs]({{< relref "naval-drones/_index.md" >}}) — Autonomous surface vessels for defense and maritime operations (Saronic, HavocAI, Anduril+HD Hyundai, MASC program)
- [Undersea Drones / AUVs]({{< relref "undersea-drones/_index.md" >}}) — Autonomous underwater vehicles and drone submarines (Anduril Ghost Shark/Dive-XL/Copperhead, L3Harris Iver4, Lockheed Lamprey)
- [Ground Drones / UGVs]({{< relref "ground-drones/_index.md" >}}) — Legged, wheeled, agricultural, delivery UGVs
- [AMR & Logistics]({{< relref "amr-and-logistics/_index.md" >}}) — Warehouse AMRs, picking robots, fleet management (6 River, Locus, Fetch, Geek+)
- [Industrial Robots & Cobots]({{< relref "industrial-robots/_index.md" >}}) — Robot arms and cobots; Universal Robots; FANUC/ABB/KUKA/Yaskawa context
- [Humanoid Robots]({{< relref "humanoid/_index.md" >}}) — US and non-US companies; autonomy claims; specialized robot debate
- [Software & Integration]({{< relref "software-and-integration/_index.md" >}}) — Middleware, fleet orchestration, WMS integration (SVT Robotics, Robust AI, Vecna)
- [Actuators]({{< relref "actuators/_index.md" >}}) — Harmonic drives, servo motors, gearboxes
- [Sensors]({{< relref "sensors/_index.md" >}}) — LiDAR, radar, GNSS, vision
- [Communications]({{< relref "communications/_index.md" >}}) — Mesh radio, cellular modules
- [Power Systems]({{< relref "power-systems/_index.md" >}}) — Batteries, fuel cells, wireless charging
- [Connectors]({{< relref "connectors/_index.md" >}}) — Micro-miniature power and data connectors: Micro-D/Nano-D, high-speed board-to-board, and drone battery quick-disconnects
- [ROS 2 Ecosystem]({{< relref "ros2/_index.md" >}}) — ROS 2 middleware, PickNik/MoveIt Pro, and the hardware compatibility ecosystem
- [EtherCAT]({{< relref "ethercat/_index.md" >}}) — Real-time Ethernet fieldbus for multi-axis motion control; protocol architecture, key companies, FSoE safety, open-source tooling, and limitations
- [Flight Controllers / Autopilot Hardware]({{< relref "flight-controllers/_index.md" >}}) — Pixhawk standard, PX4/ArduPilot, Blue UAS Framework, ModalAI, Auterion
- [Electronic Speed Controllers]({{< relref "escs/_index.md" >}}) — ESC hardware and firmware; BLHeli/BLHeli_32/AM32 lineage; Hobbywing, APD
- [Gimbals & Camera Stabilization]({{< relref "gimbals/_index.md" >}}) — Brushless gimbal stabilization; Gremsy, Freefly Systems, DJI
- [Propellers & Propulsion Mechanics]({{< relref "propellers/_index.md" >}}) — Composite and carbon fiber propeller design/materials; APC Propellers, Xoar International
- [Airframe Structural Materials]({{< relref "airframe-materials/_index.md" >}}) — Carbon fiber composite fabrication and additive manufacturing for drone/robot frames; DragonPlate, HP Additive Manufacturing
- [Encoders]({{< relref "encoders/_index.md" >}}) — Magnetic and optical rotary encoders for robot joint/motor feedback; RLS, Renishaw
- [Slip Rings]({{< relref "slip-rings/_index.md" >}}) — Rotary electrical interfaces for continuous gimbal/joint rotation; Fabricast, MOFLON
- [Antennas]({{< relref "antennas/_index.md" >}}) — Directional and auto-tracking antennas for long-range UAS command-and-control; Troll Systems, AeroVironment
