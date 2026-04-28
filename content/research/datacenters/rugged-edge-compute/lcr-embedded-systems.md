---
title: "LCR Embedded Systems"
date: 2026-04-25
lastmod: 2026-04-25
draft: false
description: "US defense ATR chassis and integrated systems supplier with 35+ years supplying mission-critical VPX enclosures, backplanes, and chassis managers to US defense programs. VITA 46.11-compliant chassis manager with open-source field upgrade capability."
tags: ["rugged", "openvpx", "atr", "defense", "chassis", "thermal-management", "us", "sosa"]
categories: ["company"]
research_area: "datacenters/rugged-edge-compute"
source_urls:
  - "https://www.lcrembeddedsystems.com/"
  - "https://www.lcrembeddedsystems.com/resources/thermal-management-challenges/"
  - "https://www.lcrembeddedsystems.com/new-vpx-chassis-manager/"
  - "https://www.eejournal.com/industry_news/new-vpx-chassis-manager-from-lcr-embedded-systems-allows-open-source-in-field-code-upgrades-manufactured-in-the-usa/"
last_reviewed: 2026-04-25
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

LCR Embedded Systems is a US defense ATR chassis and integrated systems supplier with over 35 years of proven program history. The company designs and builds rugged VPX chassis, backplanes, and integrated systems in conduction-cooled, air-cooled, and liquid-cooled configurations. LCR serves as a critical supply chain enabler: defense primes who buy Mercury Systems or Curtiss-Wright VPX compute modules still need a chassis integrator to package them into mission-ready ATR enclosures. In October 2025, LCR announced a VITA 46.11-compliant chassis manager with open-source code enabling rapid in-field firmware upgrades — a differentiator in programs requiring field maintainability.

## Key Facts

- **Headquarters:** USA (specific location: not publicly confirmed; operations are US-based)
- **Type:** Private
- **Status:** Active, 35+ years in defense supply chain
- **Key product:** Rugged VPX ATR chassis (3U conduction, air, and LFT variants); VITA 46.11 Chassis Manager
- **Certifications:** US-manufactured; designed for MIL-STD-810 and MIL-STD-461 environments
- **Target markets:** US Army, Navy, Air Force programs; defense primes requiring chassis integration for VPX compute modules

## What It Is / How It Works

LCR occupies the chassis integrator role in the rugged compute supply chain. Defense programs typically procure compute capability as a stack: compute modules (Mercury/Curtiss-Wright VPX cards) + chassis + backplane + power supply + chassis manager + integration services. LCR provides the chassis, backplane, and increasingly the chassis manager — the controller that manages slot power, temperature monitoring, health monitoring, and remote management.

**ATR Chassis Portfolio**

LCR offers ATR chassis solutions supporting:
- **3U VPX conduction-cooled:** Standard for most deployed defense systems; cold plate contact via wedge locks; supports 100–150 W per slot
- **Air-cooled VPX:** Internal fans or AFT (air flow-through); 100–200 W per slot range
- **Liquid-cooled VPX:** LFT configurations for high-TDP 3U modules pushing beyond 200 W per slot

LCR notes that 3U VPX modules for advanced RF/EW/SIGINT applications can reach approximately 200 W TDP at full rate due to escalating FPGA clock rates and inference workloads.

**VITA 46.11 Chassis Manager (October 2025)**

The October 2025 chassis manager release is notable for two reasons:
1. **Open-source firmware:** LCR publishes the chassis manager firmware as open source, enabling customers to inspect, modify, and push updates in the field without returning hardware to LCR. This is uncommon in the proprietary defense electronics sector, where chassis manager software is typically locked.
2. **US manufactured:** Emphasizes Buy American compliance; relevant for programs with domestic manufacturing requirements.

Specifications:
- VITA 46.11 conformant
- Monitors up to 32 temperature sensors
- Monitors up to 16 I/O points
- Controls up to 12 fans
- Field firmware upgrade via open-source code path

**Thermal Management Advisory**

LCR has published detailed technical guidance on thermal challenges in SOSA-aligned 3U VPX systems — acknowledging that rising FPGA power densities are pushing conduction cooling toward its limits and that LFT is increasingly required for leading-edge signal processing payloads.

## Notable Developments

- **2025-10:** Released VITA 46.11 compliant chassis manager with open-source code; US manufactured
- **Ongoing:** Thermal management guidance focused on SOSA-aligned 3U programs; acknowledgment that 200 W per slot is at the practical ceiling for conduction cooling
- **35+ year history:** Established supply chain presence across Navy, Army, and Air Force programs for chassis and backplane supply

## Key People

- <!-- TODO: verify current leadership and LinkedIn profiles from lcrembeddedsystems.com -->

### People — Last Reviewed: 2026-04-25

## Sources

- [LCR Embedded Systems Corporate Website](https://www.lcrembeddedsystems.com/)
- [Thermal Management Challenges in SOSA Systems (LCR)](https://www.lcrembeddedsystems.com/resources/thermal-management-challenges/)
- [VITA 46.11 Chassis Manager Press Release (EEJournal)](https://www.eejournal.com/industry_news/new-vpx-chassis-manager-from-lcr-embedded-systems-allows-open-source-in-field-code-upgrades-manufactured-in-the-usa/)
- [LCR Products Page](https://www.lcrembeddedsystems.com/products/)
