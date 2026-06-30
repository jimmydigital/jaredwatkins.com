---
title: Robotics Research
date: 2026-03-24
lastmod: 2026-06-29
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
- [ROS 2 Ecosystem]({{< relref "ros2/_index.md" >}}) — ROS 2 middleware, PickNik/MoveIt Pro, and the hardware compatibility ecosystem
- [EtherCAT]({{< relref "ethercat/_index.md" >}}) — Real-time Ethernet fieldbus for multi-axis motion control; protocol architecture, key companies, FSoE safety, open-source tooling, and limitations
