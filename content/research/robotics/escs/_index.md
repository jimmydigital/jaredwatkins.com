---
title: Electronic Speed Controllers (ESCs)
date: 2026-07-15
lastmod: 2026-07-15
draft: false
description: The motor-driver layer between battery power and brushless motors in drones and robots — ESC hardware manufacturers and the open/closed-source firmware ecosystem that runs on them.
research_area: "robotics/escs"
last_reviewed: 2026-07-15
stale_after_days: 180
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


## Overview

Electronic speed controllers (ESCs) sit between the battery/power-distribution layer ([Robotics Power Systems]({{< relref "../power-systems/_index.md" >}}), [Robotics Connectors]({{< relref "../connectors/_index.md" >}})) and the brushless motors covered under [Robotics Actuators]({{< relref "../actuators/_index.md" >}}), converting DC battery power into the commutated AC waveform that drives a BLDC motor, at command rates set by the flight controller ([Flight Controllers & Autopilot Hardware]({{< relref "../flight-controllers/_index.md" >}})). Like drone motors, ESC hardware manufacturing is heavily concentrated in China (Hobbywing, T-Motor). The more distinctive supply chain risk in this layer is on the firmware side: a large share of the FPV/drone ESC market ran on a single closed-source firmware, BLHeli_32, until its Norwegian developer abruptly ceased operations in June 2024 — a live case study in single-vendor firmware dependency.

## Key Themes

- ESC hardware manufacturing concentrated in China (Hobbywing, T-Motor) for the commercial/commodity tier, with smaller specialist Western alternatives (APD/Advanced Power Drives, Australia) serving high-voltage/high-performance niches.
- T-Motor, covered in depth under [Aerial Drones]({{< relref "../aerial-drones/t-motor.md" >}}), is both a motor and ESC manufacturer — illustrating the vertical integration common among Chinese drone propulsion suppliers, and was added to the US BIS Entity List in May 2024 for alleged support to Russian UAV programs.
- Firmware single-vendor risk materialized directly: BLHeli AS (Norway), maker of the closed-source, licensing-fee-based BLHeli_32 firmware used across a large share of FPV/racing drone ESCs, abruptly ceased operations in June 2024, halting all updates and support with no warning to the manufacturers who had built products around it.
- AM32, an open-source, royalty-free firmware alternative, emerged from the FPV community (AlkaMotors) specifically to remove this single-vendor dependency and is now the primary forward path for new ESC hardware.
- FOC (field-oriented control) vs. traditional trapezoidal/BLHeli commutation is an active technical differentiator, with FOC offering better efficiency and lower motor noise at added firmware complexity.

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Advanced Power Drives (APD)](https://powerdrives.net) | Australia | Private | High-voltage, high-current ESCs (F Series, HV Pro) with proprietary firmware built from the ground up; power distribution boards rated to 180°C continuous operation; niche alternative to Chinese commodity ESCs for demanding heavy-lift/X-class builds. |

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [Hobbywing](https://www.hobbywing.com) | Hobbywing (private, Shenzhen, China) | Founded 2005; brushless ESC and motor manufacturer spanning RC models, drones, and personal mobility devices; a dominant supplier in the commercial/consumer drone propulsion market. |
| [T-Motor](https://uav-en.tmotor.com) 🇨🇳 | T-Motor / Jiangxi Xintuo Enterprise (private, China) | Combined motor + ESC + propeller manufacturer; see full entry at [T-Motor]({{< relref "../aerial-drones/t-motor.md" >}}) (US BIS Entity List, May 2024). |

## Supply Chain

### Supply Chain Layers

| Layer | Key Inputs / Outputs | Companies Operating Here | Geographic Risk |
|-------|---------------------|--------------------------|-----------------|
| **1. Power semiconductors** | MOSFETs/power transistors for motor phase switching | Infineon, STMicroelectronics, ON Semiconductor (broader power semiconductor market; not drone-specific) | Design US/EU/Japan; fabrication concentrated in Asian foundries |
| **2. ESC hardware manufacturing** | Complete ESC boards (single and 4-in-1 multirotor configurations) | [Hobbywing](https://www.hobbywing.com), [T-Motor]({{< relref "../aerial-drones/t-motor.md" >}}), [Advanced Power Drives](https://powerdrives.net) | Commodity tier concentrated in China; high-performance niche in Australia/EU |
| **3. ESC firmware** | Motor commutation control software (BLHeli_S, BLHeli_32 [discontinued], AM32, proprietary) | BLHeli AS (Norway, defunct since June 2024), AlkaMotors/AM32 open-source community, APD (proprietary) | Historically single-vendor concentrated (BLHeli AS); shifting toward open-source (AM32) after the 2024 shutdown |
| **4. Flight control integration** | ESC command signal (PWM/DSHOT/CAN) from flight controller | See [Flight Controllers & Autopilot Hardware]({{< relref "../flight-controllers/_index.md" >}}) | N/A — protocol/integration layer, not a manufacturing layer |

### Key Supply Chain Notes

**⚑ Firmware single-vendor collapse — BLHeli_32:** BLHeli originated as an open-source project (GPLv3) by Norwegian developer Steffen Skaug in the early 2010s, but its successor BLHeli_32 became closed-source and required ESC manufacturers to pay a licensing fee. In June 2024, BLHeli AS abruptly announced the cessation of its operations, halting all firmware updates and support with no transition plan for the manufacturers and consumers who had built products around it. This is a documented, dated example of the single-vendor firmware risk this knowledge base flags elsewhere (e.g., Quectel in [Communications]({{< relref "../communications/_index.md" >}})), except realized rather than hypothetical.

**AM32 as the open-source replacement:** AM32 (created by Peter Smith/AlkaMotors) is a royalty-free, open-source ESC firmware for ARM-based ESCs that emerged as the community's direct response to BLHeli_32's licensing costs and, later, its discontinuation. It supports Betaflight passthrough flashing and a growing list of ARM MCUs (STSPIN32F0, STM32F051, STM32G071, GD32E230, AT32F415/421), and new ESC hardware increasingly ships with AM32 pre-installed rather than BLHeli_32.

**Vertical integration in Chinese propulsion suppliers:** T-Motor manufactures motors, ESCs, and propellers under one roof — see [T-Motor]({{< relref "../aerial-drones/t-motor.md" >}}) for the full entry, including its May 2024 US Entity List addition — illustrating how the ESC layer is frequently bundled with the motor and propeller layers ([Propellers & Propulsion]({{< relref "../propellers/_index.md" >}})) rather than sourced independently.

### Supply Chain — Last Reviewed: 2026-07-15
