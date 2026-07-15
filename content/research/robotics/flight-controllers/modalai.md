---
title: "ModalAI"
date: 2026-07-15
lastmod: 2026-07-15
draft: false
description: "San Diego-based, US-assembled maker of Blue UAS Framework-compliant flight controllers and AI companion computers (VOXL/VOXL 2) for drones and robots."
research_area: "robotics/flight-controllers"
source_urls:
  - "https://www.modalai.com/blogs/press-releases/modalai%E2%93%A1-launches-voxl%E2%93%A1-2-the-smallest-smartest-blue-uas-framework-autopilot-at-16g"
last_reviewed: 2026-07-15
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

ModalAI is a San Diego-based manufacturer of Blue UAS Framework-compliant autopilot and companion computer hardware for drones and ground robots. Its VOXL and VOXL 2 product lines integrate a PX4 real-time flight controller with a high-performance AI compute core on a single small, lightweight board, explicitly positioned as a US-manufactured alternative to foreign (primarily Chinese) flight controller hardware.

## Key Facts

- Founded: 2018, by former Qualcomm Technologies employees
- Type: Component/subsystem supplier — flight controller and companion computer manufacturer
- Status: Active, privately held
- Key metric(s): VOXL 2 weighs 16 grams; integrates an 8-core CPU (Qualcomm QRB5165) delivering up to 15+ TOPS of AI compute, seven image sensors, TDK IMUs/barometer, and 5G connectivity; described by the company as "the smallest, smartest Blue UAS Framework autopilot" at launch
- Value chain position: Component/subsystem supplier (flight controller and companion computer hardware for drone/robot OEMs and integrators, not a complete platform vendor)

## What It Is / How It Works

ModalAI's core product line, VOXL, combines two functions that were historically separate boards: a real-time PX4 flight controller (handling low-level stabilization and control-loop timing) and a high-performance application processor for onboard AI, computer vision, and autonomy (SLAM, obstacle avoidance, GPS-denied navigation). VOXL 2, built on the Qualcomm Flight RB5 5G platform (QRB5165 SoC), adds 5G connectivity intended to support BVLOS operations and links to Auterion's AuterionOS as an optional software layer, since PX4 runs natively on the QRB5165.

The company's flight controllers and companion computers are certified or cleared under the Blue UAS Framework, a US Department of Defense Defense Innovation Unit (DIU) initiative that vets commercial drone components for government procurement; ModalAI states VOXL was "the first Blue UAS Framework autopilot," and frames its US-assembly and component sourcing explicitly as a response to supply chain and security concerns around foreign-manufactured flight control hardware — the same category of concern documented for DJI drones and Quectel cellular modules elsewhere in this robotics knowledge base. Beyond VOXL, ModalAI also sells FPV drone components, ESCs, radios, and development drones (e.g., Starling 2 Max), and documents case studies with drone OEMs including Inspired Flight, Cleo Robotics, Corvus Drones, and XTEND using its flight controller and companion computer hardware.

## Notable Developments

- **2022-04-25:** ModalAI launches VOXL 2, built on the Qualcomm Flight RB5 5G platform, adding 5G connectivity and up to 15+ TOPS of onboard AI compute at 16 grams.
- **2018:** ModalAI founded in San Diego by former Qualcomm Technologies employees.

## Key People / Key Organizations

- **Chad Sweet** — CEO and co-founder, ModalAI. LinkedIn: not found.

### People — Last Reviewed: 2026-07-15

## Sources

- [ModalAI Launches VOXL 2, the Smallest, Smartest Blue UAS Framework Autopilot at 16g](https://www.modalai.com/blogs/press-releases/modalai%E2%93%A1-launches-voxl%E2%93%A1-2-the-smallest-smartest-blue-uas-framework-autopilot-at-16g) — VOXL 2 specifications, Blue UAS Framework positioning, company founding details, Auterion OS collaboration
