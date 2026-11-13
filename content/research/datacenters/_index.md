---
title: Datacenter Research
date: 2026-03-24
lastmod: 2026-10-26
draft: false
description: Research on next-generation datacenter design, construction, cooling, automation, power, and distributed compute — covering the infrastructure race to power AI workloads.
research_area: "datacenters"
last_reviewed: 2026-10-26
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---

{{<steering>}}

## Datacenters — Steering Instructions

**Scope boundaries:**
- IN: Physical datacenter infrastructure — cooling, power, construction, physical automation, rack design, connectivity hardware; companies designing, building, or operating innovative datacenter facilities
- OUT: Cloud computing software, AI model development, chip design (separate sections); routine hyperscaler earnings or campus announcements without a novel infrastructure angle
- BORDERLINE: Rack-scale compute systems (NVIDIA NVL72, HPE Cray EX) — include only when the physical infrastructure or cooling integration is the notable element, not the compute itself

**Key metrics to document** for cooling technologies and products: PUE (target and measured annualized — not just design); WUE (liters per kWh IT load); rack density supported (kW/rack — air tops out ~15–20 kW, liquid starts at 20 kW); coolant temperature range (supply and return); ERE (Energy Reuse Effectiveness). For construction/design entries: time to power (months greenfield to live), cost per MW (verify whether figure includes land, power infrastructure, fit-out, and redundancy — not just shell-and-core), PUE target, and total MW at full buildout.

**Claim verification flags for datacenters:** Distinguish design PUE from measured annualized PUE. For "supports X kW/rack" claims, verify that figures account for real-world fluid distribution, manifold pressure drops, and redundancy — not just tank theoretical capacity. For autonomous operation claims, establish what fraction of tasks are genuinely automated vs. still requiring human intervention. For "100% renewable" power claims, determine whether the mechanism is RECs (does not change the physical grid mix) or 24/7 matched clean power. For cost per MW claims, see metrics note above.

**Additional entry types for datacenters** (beyond the global company/technology/person/breakthrough types):
- **Design pattern**: a documented approach being adopted by multiple operators (e.g., zoned hybrid cooling)
- **Facility entry**: a specific notable datacenter with documented novel infrastructure elements
- **Standard/specification**: an industry standard relevant to infrastructure (OCP, Open19, ASHRAE thermal guidelines)

{{</steering>}}

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


## Overview

Tracks the infrastructure frontier of AI-driven datacenter construction and operation. Focus areas: liquid cooling systems enabling 20–400+ kW/rack densities, robotics and autonomous operations reducing labor dependency, next-generation facility design cutting time-to-power and cost per MW, and alternative power sourcing for the energy intensity of modern AI workloads.

## Key Themes

- Rack density escalation driven by AI/HPC: GPU clusters require 20–100+ kW/rack, forcing a transition from air to liquid cooling at scale
- Liquid immersion cooling moving from HPC niche to mainstream AI datacenter consideration as rack densities exceed 30–40 kW
- Robotic automation of datacenter operations — server installation, maintenance, monitoring — reducing labor cost and enabling fully lights-out facilities
- $6.7T in cumulative global datacenter capex projected through 2030 (McKinsey), driving demand for faster, cheaper construction methods
- Power sourcing as the binding constraint: grid interconnection delays pushing operators toward behind-the-meter gas turbines, nuclear PPAs, and SMRs
- Blind-mate and tool-less connectivity hardware as the enabling component layer for robot-serviced facilities

## Companies

For full company tables by subsection, see [Cooling](./cooling/), [Design & Construction](./design-construction/), [Distributed & Decentralized Compute](./distributed-compute/), [Orbital Compute](./orbital-compute/), [Power Infrastructure](./power-infrastructure/), and [Robotics & Automation](./robotics-automation/).
