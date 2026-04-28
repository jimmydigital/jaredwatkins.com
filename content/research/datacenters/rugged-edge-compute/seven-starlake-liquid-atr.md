---
title: "7Starlake 7SL-3500 Liquid-Cooled VPX ATR"
date: 2026-04-25
lastmod: 2026-04-25
draft: false
description: "7Starlake's 7SL-3500 is a self-contained liquid-cooled 3U VPX ATR chassis compliant with VITA 48.4 LFT, supporting up to 500 W TDP in a closed-loop sealed design. Targeted at radar, EW, and UAS applications."
tags: ["rugged", "openvpx", "vita-48", "liquid-cooling", "atr", "sosa", "defense", "taiwan"]
categories: ["technology"]
research_area: "datacenters/rugged-edge-compute"
source_urls:
  - "https://7starlake.com/solutions/liquid-cooled-system/liquid-cooling-atr-system"
  - "https://7starlake.com/en/events/press-release/7starlake-unveils-next-gen-3u-vpx-self-contained-liquid-cooling-atr"
  - "https://militaryembedded.com/radar-ew/sensors/liquid-cooled-3u-vpx-atr-system-introduced-by-7starlake"
  - "https://7starlake.com/products/liquid-cooled/atr/7sl-3500-l2l"
last_reviewed: 2026-04-25
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

The 7Starlake 7SL-3500 is a 3U OpenVPX ATR chassis with an integrated, self-contained liquid cooling system compliant with the VITA 48.4 Liquid Flow-Through (LFT) standard. The key differentiator over earlier liquid-cooled ATR products is the closed-loop architecture: the coolant pump, heat exchanger, and reservoir are packaged within the chassis itself, eliminating dependence on external facility coolant or platform cooling infrastructure. The system supports up to 500 W total thermal design power in a platform that claims 10× greater thermal efficiency than air-cooled systems of comparable size.

## Key Facts

- **Manufacturer:** 7Starlake (Taiwan-based rugged compute company)
- **Product:** 7SL-3500 series — variants include 7SL-3500-L2L (liquid-to-liquid) and 7SL-3500-L2A (liquid-to-air)
- **Form factor:** 3U ATR chassis; 10.6" (H) × 7.6" (W) × 19.5" (D) including handles and connectors
- **Weight:** Approximately 38 lbs without payload boards
- **Cooling standard:** VITA 48.4 Liquid Flow-Through; self-contained closed-loop
- **Thermal capacity:** Up to 500 W TDP (closed-loop, self-contained)
- **Power input:** 18V–36V DC (MIL vehicle bus compatible)
- **Connectors:** IP65-rated; MIL-STD D38999 connectors
- **Standards:** OpenVPX, SOSA Technical Standard 3-slot backplane alignment; VITA 48.4 LFT
- **Applications:** Software-defined radar, sensor fusion, EW, threat detection, UAS, hypersonic glide vehicles, ground-based autonomous systems

## What It Is / How It Works

The 7SL-3500 addresses the gap between conduction-cooled systems (limited to ~150 W per chassis) and platform-coupled liquid-cooled systems (which require vehicle or aircraft plumbing infrastructure). By integrating the pump and heat exchanger within the ATR box itself, the 7SL-3500 enables high-density compute in any platform without special coolant plumbing.

**Closed-Loop Liquid-to-Air Variant (7SL-3500-L2A)**
Liquid circulates internally across the VPX module cold plates (via VITA 48.4 integral heatsinks), collects heat, and routes it to an internal liquid-to-air heat exchanger. The heat exchanger fans exhaust heat to the ambient environment. Net result: the chassis is an air-cooled box from the platform's perspective, but liquid-cooled internally. The liquid-to-air configuration is suitable for deployments with ambient cooling access (vehicle exterior air, aircraft ducted air).

**Platform-Coupled Liquid-to-Liquid Variant (7SL-3500-L2L)**
For platforms with access to a coolant loop (shipboard chilled water, vehicle engine cooling circuit), the 7SL-3500-L2L connects its internal cooling manifold to the platform supply. This enables sustained high-TDP operation beyond what an internal heat exchanger can handle, leveraging the platform's larger cooling capacity.

**VPX Slot Configuration**
The 7SL-3500 incorporates:
- 3-slot VPX backplane aligned with SOSA Technical Standard profiles
- Intel i7-1185GRE or Core Ultra 7-155H host processor
- IP65 sealed chassis for dust and splash protection
- MIL-STD D38999 connectors (military-grade circular connectors for shock/vibration resistance)

**Thermal Efficiency Claim**
7Starlake claims 10× greater thermal efficiency than "conventional air-cooled systems of similar size." This figure likely reflects the liquid-to-module heat transfer coefficient advantage over surface air convection, but the specific test conditions and reference system are not published.

## Notable Developments

- **2025:** 7Starlake unveiled the next-generation 7SL-3500 at a press event; Military Embedded Systems covered the liquid-cooled 3U VPX ATR introduction
- **2024:** 7SL-3500-L2L (liquid-to-liquid variant) entered product catalog with 500 W TDP spec
- **Prior:** 7Starlake's earlier THOR200-U8-D (half-rack NAS for submarine/aerospace) established the company's presence in US defense markets before the VPX ATR product line expansion

## Claim Verification

### Claim: "Up to 500 W TDP in self-contained closed-loop chassis"
**Status:** Partially verified

**Supporting sources:**
- [7Starlake Product Page](https://7starlake.com/solutions/liquid-cooled-system/liquid-cooling-atr-system) — company specification
- [Military Embedded Systems coverage](https://militaryembedded.com/radar-ew/sensors/liquid-cooled-3u-vpx-atr-system-introduced-by-7starlake) — third-party press coverage of the specification

**Refuting / questioning sources:**
- No independent lab test report confirming 500 W sustained operation at ambient temperature limits (-40°C or +60°C) has been located. The 500 W figure likely represents the cooling system capacity, not a validated sustained processor TDP at worst-case thermal conditions.

**Summary:** 500 W TDP is a plausible specification for VITA 48.4 LFT systems; the figure is cited by a third-party publication but not independently measured.

### Claim: "10× greater thermal efficiency than air-cooled systems of similar size"
**Status:** Unverified

**Supporting sources:**
- [7Starlake Press Release](https://7starlake.com/en/events/press-release/7starlake-unveils-next-gen-3u-vpx-self-contained-liquid-cooling-atr) — company claim

**Refuting / questioning sources:**
- Reference system and test conditions not specified. The 10× figure is company-issued with no methodology disclosed.

**Summary:** Plausible directionally (liquid cooling substantially outperforms air for high-power-density components) but the specific multiplier is unverified.

## Key People

- <!-- TODO: identify 7Starlake leadership; Taiwan-based company; LinkedIn profiles not confirmed -->

### People — Last Reviewed: 2026-04-25

## Sources

- [7SL-3500 Liquid Cooling ATR System (7Starlake)](https://7starlake.com/solutions/liquid-cooled-system/liquid-cooling-atr-system)
- [7SL-3500-L2L Product Page](https://7starlake.com/products/liquid-cooled/atr/7sl-3500-l2l)
- [Next-Gen 7SL-3500 Press Release (7Starlake)](https://7starlake.com/en/events/press-release/7starlake-unveils-next-gen-3u-vpx-self-contained-liquid-cooling-atr)
- [Military Embedded Systems: Liquid-cooled 3U VPX ATR from 7Starlake](https://militaryembedded.com/radar-ew/sensors/liquid-cooled-3u-vpx-atr-system-introduced-by-7starlake)
