---
title: Encoders
date: 2026-07-15
lastmod: 2026-07-15
draft: false
description: Rotary position encoders for robot joint and motor feedback — magnetic and optical encoder technology enabling precise position, velocity, and torque control in robotic arms, exoskeletons, and drone gimbals.
research_area: "robotics/encoders"
last_reviewed: 2026-07-15
stale_after_days: 180
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.

## Overview

Position encoders provide the real-time feedback a robot joint or motor needs to control torque, velocity, and position — without them, closed-loop servo control is impossible. Two encoding technologies dominate: optical (light-based, very high resolution, sensitive to contamination) and magnetic (non-contact, robust in harsh/dirty environments, slightly lower peak resolution). This subsection covers the specialist encoder manufacturers supplying robotic arms, humanoid/exoskeleton joints, and drone gimbals ([Gimbals & Camera Stabilization]({{< relref "../gimbals/_index.md" >}})) — distinct from the motor/actuator hardware itself ([Robotics Actuators]({{< relref "../actuators/_index.md" >}})) that the encoder is mounted to or integrated within.

## Key Themes

- Magnetic encoders have become the default choice for compact, weight-constrained robot joints (humanoid limbs, exoskeletons, surgical robots) because they are non-contact, tolerant of dirt/vibration, and can be built into very small, lightweight off-axis or through-hole form factors.
- RLS (Slovenia) and Renishaw (UK) operate as closely linked but formally distinct companies: Renishaw holds a 50% ownership stake in RLS and sells RLS-designed magnetic encoders through its own global distribution network, while RLS also sells independently, particularly across Central/Eastern Europe.
- Encoder selection for robotics involves trading off resolution, size, installation tolerance, and environmental robustness (temperature, vibration, EMC, sterilization compatibility for surgical use) rather than optimizing for any single metric.
- Documented robotics use cases span humanoid bipedal balance control (PAL Robotics), exoskeletons for mobility assistance (Marsi Bionics), and university self-balancing robot projects — illustrating the technology's reach from research/prototype to commercial deployment.

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [RLS (RLS Merilna tehnika d.o.o.)](https://www.rls.si) | Komenda, Slovenia | Private (50% owned by Renishaw plc) | Non-contact magnetic rotary and linear encoders, encoder ICs, and interpolators for industrial robotics, motor feedback, and joint position control. |

### Public Companies

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [LSE: RSW](https://www.londonstockexchange.com/stock/RSW/renishaw-plc/company-page) | [Renishaw plc](https://www.renishaw.com) | Precision metrology and encoder manufacturer; sells optical (ATOM™) and magnetic (AksIM™, Orbis™) encoders for robotics, and holds a 50% ownership stake in RLS. |

## Supply Chain

### Supply Chain Layers

| Layer | Key Inputs / Outputs | Companies Operating Here | Geographic Risk |
|-------|---------------------|--------------------------|-----------------|
| **1. Encoder sensing technology** | Magnetic sensor ICs (Hall-effect, TMR), optical readheads and scales | [RLS](https://www.rls.si), [Renishaw](https://www.renishaw.com) | Concentrated in Europe (Slovenia, UK) for these two named suppliers |
| **2. Encoder module/IC manufacturing** | Finished encoder modules, ICs, and interpolators | [RLS](https://www.rls.si) (design and manufacture), [Renishaw](https://www.renishaw.com) (design, manufacture, and global distribution including RLS products) | Slovenia and UK manufacturing; Renishaw also has a global sales/support office network |
| **3. Joint/actuator integration** | Encoder mounted to or integrated within a motor/joint assembly providing position feedback to the controller | See [Robotics Actuators]({{< relref "../actuators/_index.md" >}}) and [Gimbals & Camera Stabilization]({{< relref "../gimbals/_index.md" >}}) | N/A — integration layer |

### Key Supply Chain Notes

**Renishaw–RLS ownership and distribution relationship (⚑ shared supplier):** Renishaw holds a 50% ownership stake in RLS and sells RLS-designed magnetic encoders through its own worldwide sales network, while RLS independently sells and supports Renishaw products across several Central/Eastern European markets. Buyers sourcing "Renishaw" magnetic encoders and "RLS" magnetic encoders may, in some product lines, be sourcing the same underlying design and manufacturing base rather than two fully independent suppliers — worth flagging for any single-source risk analysis.

**European concentration:** Both named specialist encoder suppliers in this entry are European (Slovenia, UK); this entry does not yet cover Asian or US-based encoder manufacturers (e.g., AMS OSRAM's magnetic encoder ICs, or US Digital), which is a gap for future research rather than an indication that European suppliers dominate the entire market.

### Supply Chain — Last Reviewed: 2026-07-15
