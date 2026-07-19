---
title: "Robotic Hands & Dexterous Manipulation"
date: 2026-07-18
lastmod: 2026-07-18
draft: false
description: "Multi-fingered end effectors and dexterous-hand actuation for humanoid and industrial manipulation — the component layer widely cited as the current bottleneck for useful humanoid work."
research_area: "robotics/hands"
last_reviewed: 2026-07-18
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.8
  disable: false
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.

## Overview

Dexterous hands are the end-effector layer that determines whether a humanoid or industrial robot can actually do useful manipulation work, as opposed to gross pick-and-place with simple grippers. Through 2023–2025 the segment was widely described as a scarcity market: capable multi-fingered hands existed mostly as research prototypes, expensive, fragile, and unable to reach production volume. By 2026, that has shifted — Chinese manufacturers in particular have crossed into genuine mass production, while several Western and Korean specialists are racing toward IPOs and Tier-1 industrial partnerships rather than staying lab-only. The bottleneck has moved from "can a hand exist at all" to reliability, repairability, and cost at scale: mean time between failures (MTBF) for multi-jointed fingers remains far below the levels needed for unattended industrial or consumer deployment, and no manufacturer has yet published a certified 10,000-hour MTBF figure.

This subsection tracks the component/subsystem suppliers building these hands — not the humanoid platform OEMs that integrate them (see [Humanoid Robots]({{< relref "../humanoid/_index.md" >}}) for platform-level entries). Per the parent [Robotics]({{< relref "../_index.md" >}}) section's editorial priority, the interesting entries here are the specialists solving the actuator-density, tactile-sensing, and durability problems — not the OEMs that will eventually bolt these hands onto a humanoid arm.

## Key Themes

- **From scarcity to mass production:** Chinese hand-component maker Inspire Robots delivered 10,000+ units in 2025 (up from roughly 2,000 the year before) and is targeting 50,000–100,000 units in 2026 — a genuine industrialization inflection, not just a prototype milestone.
- **The MTBF/repairability problem:** Multi-jointed fingers concentrate dozens of micro-actuators, sensors, and tendon-driven cables into a small, high-stress volume, creating disproportionate "failure density" relative to the rest of a humanoid robot. No manufacturer has published a certified 10,000-hour MTBF figure as of mid-2026; several (Tesollo) are explicitly designing for fast field-repairability (swappable fingers/joints) as a stopgap rather than solving durability outright.
- **Tactile sensing convergence with prosthetics:** US company PSYONIC's Ability Hand originated as an FDA-approved prosthetic device; its touch-sensing and compliant mechanics are now being repurposed for industrial/humanoid grasping (ABB Robotics partnership, 2026), and the company argues human-derived tactile/force data trains better manipulation models than teleoperation or video alone.
- **China's cost and scale advantage:** Chinese dexterous-hand makers claim 30–50% cost advantages over non-Chinese competitors and represent roughly half the reported global market by some industry counts, with 60+ companies active as of 2026.
- **Component-level capital is small relative to the platform layer:** Actuation/end-effector component suppliers have raised comparatively little venture capital next to full humanoid-platform OEMs, even though dexterity is widely cited as the binding constraint on humanoid usefulness — a mismatch worth tracking as the segment matures.

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Inspire Robots](https://en.inspire-robots.com) 🇨🇳 | Beijing, China | Growth (private) | Dexterous-hand and micro linear servo actuator manufacturer; China's first commercial mass-produced dexterous hand (2020); 10,000+ units delivered in 2025. |
| [Tesollo](https://en.tesollo.com) | Incheon, South Korea | Series B / pre-IPO | Multi-jointed robotic hand and gripper specialist (DG-2F, DG-3, DG-5F series); preparing an IPO; proprietary sub-1kg actuators for the DG-5F-S. |
| [PSYONIC](https://www.psyonic.io) | San Diego, CA, USA | Growth (private) | FDA-approved myoelectric prosthetic hand (Ability Hand) repurposed for industrial/humanoid dexterous manipulation via a 2026 partnership with ABB Robotics. |

### Incumbents & Adjacent Platforms

| Company | HQ | Relevance |
|---------|-----|-----------|
| [ABB Robotics](https://new.abb.com/products/robotics) | Zurich, Switzerland (sold to SoftBank, Oct 2025) | Major industrial robot arm/cobot maker; GoFa cobot is the test platform for PSYONIC's Ability Hand under their 2026 dexterous-manipulation partnership. |
| [NVIDIA](https://www.nvidia.com) | Santa Clara, CA, USA | Isaac Lab / GR00T foundation models used by multiple hand makers (PSYONIC, humanoid OEMs) to train vision-language-action manipulation policies with less data than teleoperation-only approaches. |

## Supply Chain

### Supply Chain Layers

| Layer | Key Inputs / Outputs | Companies Operating Here | Geographic Risk |
|-------|---------------------|--------------------------|-----------------|
| **1. Micro-actuation** | Miniaturized servo motors, linear actuators, and drivers small enough to fit inside individual finger joints | Inspire Robots (China, micro linear servo actuators), Tesollo (South Korea, proprietary sub-1kg actuators) | China dominant on cost/volume; South Korea and US on precision/reliability-focused designs |
| **2. Tactile & force sensing** | Pressure sensors, vibration feedback, fingertip contact sensing | PSYONIC (US, integrated touch sensors + vibration feedback in Ability Hand); see also [force-torque sensors]({{< relref "../sensors/force-torque/_index.md" >}}) | Concentrated in a small number of specialist US/EU firms; not yet a Chinese cost-volume category the way actuation is |
| **3. Integrated hand assemblies** | Complete multi-fingered end effectors (5–27 DoF), wrists, mounting interfaces | Inspire Robots, Tesollo, PSYONIC | China leads unit volume; South Korea and US compete on reliability/repairability and Tier-1 industrial validation |
| **4. AI/data layer** | Vision-language-action models, human-derived manipulation data (teleoperation, prosthetic users, video) | NVIDIA Isaac Lab/GR00T, PSYONIC (human prosthetic-user data), humanoid OEM in-house stacks | Global; NVIDIA's platform is a shared dependency across many hand and humanoid makers |
| **5. Integration into robot platforms** | Robot arms, cobots, and humanoid platforms that mount dexterous hands as end effectors | ABB Robotics, Apptronik, Figure AI, 1X, and other [Humanoid Robots]({{< relref "../humanoid/_index.md" >}}) entries | Globally distributed at the OEM layer |

### Key Supply Chain Notes

**⚑ Chinese cost/volume concentration:** Inspire Robots' jump from ~2,000 units (2024) to 10,000+ units (2025), with a stated 2026 target of 50,000–100,000, mirrors the broader pattern seen in Chinese humanoid platform manufacturing (Unitree, UBTECH) — rapid scale-up enabled by domestic supply chains and lower per-unit cost, generally 30–50% below non-Chinese competitors per industry estimates. This concentration risk compounds the existing NdFeB rare-earth magnet dependency documented in the [Actuators]({{< relref "../actuators/_index.md" >}}) supply chain, since dexterous-hand micro-actuators are BLDC/servo motors subject to the same magnet chokepoint.

**Repairability as a stopgap for the durability problem:** Rather than claiming a solved durability problem, Tesollo has explicitly designed its DG series hands for fast finger/joint replacement, treating high failure density as a given constraint of the current technology generation. This is a notably more candid engineering posture than platform-level humanoid OEMs typically take with battery or actuator claims elsewhere in this knowledge base.

**Prosthetics-to-robotics technology transfer:** PSYONIC's Ability Hand is a rare example of a medical device (FDA-approved, Medicare-covered, 300+ patients as of mid-2026) being repurposed for industrial robotics rather than the more common reverse flow (industrial actuator technology adapted for prosthetics). The company argues this gives it higher-fidelity human contact/force data than teleoperation-glove or video-based approaches used elsewhere in the sector.

### Supply Chain — Last Reviewed: 2026-07-18
