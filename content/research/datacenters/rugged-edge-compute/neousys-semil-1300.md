---
title: "Neousys SEMIL-1300 Series"
date: 2026-04-25
lastmod: 2026-04-25
draft: false
description: "Fanless 2U half-rack edge AI server with IP67 waterproofing, -40°C operation, PoE+ integration; Taiwan-based, Advantech subsidiary, semi-industrial edge compute."
tags: ["neousys", "fanless", "half-rack", "edge-ai", "ip67", "industrial", "taiwan"]
categories: ["technology"]
research_area: "datacenters/rugged-edge-compute"
source_urls:
  - "https://www.neousys-tech.com/en/product/product-lines/edge-ai-gpu-computing/semil-1300gc-ip67-nvidia-tesla-t4-quadro-p2200-gpu-fanless-computer/"
  - "https://coastipc.com/media/productattach/s/e/semil-1300gc_data_sheet_100924.pdf"
  - "https://www.assured-systems.com/neousys-semil-1300-intel-xeon-ecore-half-rack-rugged-fanless-computer/"
  - "https://www.stemmer-imaging.com/en/products/series/neousys-semil-1300/"
last_reviewed: 2026-04-25
stale_after_days: 180
---

## Summary

The SEMIL-1300 is a passively cooled, IP67-rated 2U half-rack fanless edge AI server designed for harsh-environment deployments. Built on a proven thermal design validated in transportation, industrial ITS, and field-portable scenarios, the SEMIL-1300 combines wide-temperature capability (-40°C to +70°C) with integrated PoE+ power distribution for sensor networks. Available with optional NVIDIA GPU acceleration (Tesla T4, Quadro P2200 variants).

## Key Facts

- **Developed by / Company:** Neousys Technology Inc. (Advantech subsidiary)
- **HQ:** New Taipei City, Taiwan
- **Type:** Rugged fanless edge AI server
- **Status:** Active, current production
- **Form Factor:** 2U 19" half-rack enclosure
- **Thermal Design:** Fully passive (fanless), -40°C to +70°C operation
- **Certifications:** IP67 (dust and waterproof), CE, FCC, EN 50155 (railway standard)

## What It Is / How It Works

The SEMIL-1300 is a passively cooled edge AI platform built around Intel Xeon E-series or 9th/8th-gen Core processors. Unlike traditional fans that fail in vibration-rich environments, the SEMIL-1300 relies on internal aluminum heat spreaders and conduction through the chassis to dissipate heat into the mounting rack or enclosure. This fanless design eliminates the most common failure point in mobile and field-deployed compute systems.

The architecture is optimized for distributed sensor-to-edge compute scenarios: four integrated Gigabit PoE+ ports deliver 25W each to networked cameras (IP/GigE vision systems), LiDAR sensors, or millimeter-wave radars. The PoE+ power delivery eliminates the need for a separate sensor power distribution layer, reducing system complexity and installation time. This is particularly valuable for vehicle-mounted systems and remote surveillance networks where power distribution space is constrained.

Memory is DDR4 with ECC support up to 64GB. Storage uses M.2 interfaces (B-key for 4G/5G modules, E-key for Wi-Fi), enabling flexible wireless integration. Wide-range DC input (8–48V) with integrated ignition power control handles both vehicle power buses and field-deployed battery systems.

The SEMIL-1300GC variant adds NVIDIA discrete GPU options (Tesla T4, Quadro P2200), targeting edge AI inference workloads (object detection, pose estimation, semantic segmentation) in video analytics, autonomous vehicle support, and predictive maintenance applications.

## Notable Developments

- **2024:** SEMIL-1700GC variant introduced with Quadro RTX 2000 Ada GPU option; expanded transportation market adoption
- **2023:** IP67 waterproof certification completed; deployed in railway and maritime surveillance systems
- **2022:** SEMIL-1300 launched; initial focus on ITS (Intelligent Transportation Systems) and vehicle-mounted AI analytics

## Market Position & Competitive Differentiation

The SEMIL-1300 occupies the upper tier of "semi-industrial" edge AI compute — above consumer ruggedized laptops, below military-grade MIL-STD-810H systems. The target customer is an integrator or system vendor building transportation, ITS, or defense-adjacent (base security, training) AI systems who needs proven passive thermal design, IP67-rated waterproofing, and PoE+ sensor integration but does not require full DoD qualification.

Neousys's competitive strength lies in **passive thermal engineering proven in shipping and field conditions**. The SEMIL series has accumulated field deployment hours in moving vehicle (train, bus, delivery vehicle), maritime surveillance, and outdoor stationary installations — thermal validation that many competitors claim but few have demonstrated through multi-year fleet deployments.

The PoE+ integration is a practical advantage for system integrators: a single 2U server can power up to four high-wattage GigE cameras, eliminating external power supplies and junction boxes. This reduces cabling, cuts installation time, and improves system reliability in constrained vehicle bays.

As an Advantech subsidiary, Neousys benefits from Advantech's global supply chain, channel, and industrial customer relationships. Disadvantage: not US-owned, limiting access to certain defense programs (DoD classified projects, ITAR-restricted integrations). However, the SEMIL-1300 is actively deployed in transportation and ITS applications serving government agencies (traffic management, transit authority) where Chinese ownership is less of a procurement barrier.

## Key Organizations & Partnerships

- **Advantech Group** (Taiwan, TWSE: 2345) — Parent company; industrial embedded computing diversification
- **Assisted Systems** (integrator/distributor) — SEMIL-1300 distribution in EMEA and Asia-Pacific
- **CoastiPC** (US distributor) — Reference documentation and technical support
- **STEMMER IMAGING** (vision systems integrator) — SEMIL-1300 in GigE vision and AI vision analytics platforms

## Deployment Context

The SEMIL-1300 is most heavily deployed in: (1) Vehicle-mounted AI analytics for transportation fleet monitoring and autonomous vehicle support; (2) ITS roadside and traffic control systems; (3) Maritime and railway surveillance (IP67 enables outdoor mounting); (4) Defense-adjacent applications (airbase perimeter surveillance, military training simulation networks) where non-classified, non-exported compute is acceptable.

## Sources

- [Neousys SEMIL-1300GC Product Page](https://www.neousys-tech.com/en/product/product-lines/edge-ai-gpu-computing/semil-1300gc-ip67-nvidia-tesla-t4-quadro-p2200-gpu-fanless-computer/) — Official specifications, GPU variant options
- [SEMIL-1300GC Datasheet](https://coastipc.com/media/productattach/s/e/semil-1300gc_data_sheet_100924.pdf) — Technical reference, thermal design, operating ranges
- [Assured Systems SEMIL-1300 Overview](https://www.assured-systems.com/neousys-semil-1300-intel-xeon-ecore-half-rack-rugged-fanless-computer/) — Integrator perspective, deployment notes
- [STEMMER IMAGING Product Page](https://www.stemmer-imaging.com/en/products/series/neousys-semil-1300/) — Integration with GigE vision systems
