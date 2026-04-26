---
title: "VITA 48 REDI Thermal Cooling Standards for VPX"
date: 2026-04-25
lastmod: 2026-04-25
draft: false
description: "VITA 48 REDI (Ruggedized Enhanced Design Implementation) defines the family of mechanical and thermal interface standards for OpenVPX modules. Overview of the major variants: conduction cooling, air flow-through (AFT), and liquid flow-through (LFT/VITA 48.4)."
tags: ["vita-48", "openvpx", "thermal-management", "liquid-cooling", "conduction-cooling", "defense", "rugged"]
categories: ["technology"]
research_area: "datacenters/rugged-edge-compute"
source_urls:
  - "https://militaryembedded.com/radar-ew/thermal-management/liquid-flow-through-vita-484-cooling-technology-in-rugged-openvpx-atr-platform"
  - "https://militaryembedded.com/radar-ew/thermal-management/cool-world-a-tour-of-thermal-management-approaches-for-rugged-computer-systems"
  - "https://www.elma.com/en/news-events/news-releases/rugged-atr-platform-for-vita-48-4-lft-cooling"
  - "https://defense-solutions.curtisswright.com/media-center/articles/vita-48.8-aft-cooling-standard-lowers-swap-c-on-deployed-vpx-systems"
  - "https://www.electronicdesign.com/technologies/industrial/boards/article/55233125/advanced-cooling-technologies-overcome-thermal-management-challenges-in-rugged-system-design-to-optimize-swap-c"
last_reviewed: 2026-04-25
stale_after_days: 365
---

## Summary

VITA 48, known as REDI (Ruggedized Enhanced Design Implementation), is the family of ANSI-ratified standards that defines mechanical and thermal interface requirements for OpenVPX plug-in modules. The VITA 48.x sub-standards address different cooling methods — conduction, air flow-through, and liquid flow-through — establishing interoperability between modules from different vendors within the same chassis. As GPU and FPGA power densities push beyond what conduction cooling can handle, VITA 48.4 (liquid flow-through) is becoming a critical enabler for next-generation defense AI processing.

## Key Facts

- **Standards Body:** VITA (VMEbus International Trade Association), part of ANSI
- **Applies to:** 3U and 6U OpenVPX (VITA 65) plug-in modules
- **Primary variants:** VITA 48.1 (conduction), VITA 48.8 (air flow-through), VITA 48.4 (liquid flow-through)
- **Driver:** Power per slot has risen from ~50 W (legacy VME) to 200–500 W+ (modern GPU/FPGA cards), exceeding air-cooling limits
- **DoD relevance:** SOSA-aligned programs specify VITA 48.x cooling compliance alongside VITA 65 slot profiles

## What It Is / How It Works

### Background: The Thermal Escalation Problem

For decades, conduction cooling dominated rugged embedded computing. Modules transfer heat laterally through wedge-lock retainers into the chassis cold wall, which then conducts to the chassis rails and ultimately to the host platform (vehicle bulkhead, aircraft skin). This approach has no moving parts, achieves excellent MTBF, and integrates well with military platform cooling systems.

However, power densities have escalated sharply. Where 50-watt cards were once standard, 120–200 W cards are now common. High-performance AI accelerators and modern FPGAs push beyond that. Conduction cooling typically tops out at approximately 50–100 W per 3U slot and 80–150 W per 6U slot depending on chassis design. Beyond these limits, thermal resistance becomes unacceptable and processors throttle or shut down.

### VITA 48 Cooling Variants

**VITA 48.1 — Conduction Cooling**
The baseline approach. The module's PCB heat spreads through a conduction frame (wedge lock) into the chassis sidewall and rails. No fluid or airflow required inside the module. Thermal performance depends on contact pressure, interface materials (graphite inserts, heat pipes embedded in cold plate), and chassis thermal capacity. Thermal limit: approximately 100–150 W per 6U slot with optimized cold plates. Operating range: -40°C to +85°C.

Advanced conduction cold plates improve on baseline aluminum:
- Graphite inserts (3 mm APG) reduce thermal resistance by ~30% vs. aluminum baseline
- Heat pipe cold plates (24× 3 mm heat pipes) reduce thermal resistance by up to 90% vs. baseline aluminum cold plates

**VITA 48.8 — Air Flow-Through (AFT)**
An ANSI-ratified standard for air-cooled VPX modules. Unlike legacy convection cooling (external fans blowing across board edges), AFT routes airflow directly through sealed channels within the module. A heat-exchanger frame creates a thermally isolated internal flow path. Performance: up to 200 W per slot. Advantage over LFT: no liquid lines or connectors, simpler logistics. Used where ambient air is available and thermal loads fall in the 100–200 W range. Curtiss-Wright's FFT (Fluid Flow-Through) cooling is a proprietary variant of this approach.

**VITA 48.4 — Liquid Flow-Through (LFT)**
The high-power standard. Coolant circulates through an integral heatsink machined into the module body. Quick-disconnect coupling assemblies (per VITA 48.4 mechanical spec) allow fluidic connection to the chassis manifold without tooling or alignment issues. Individual card coolant flow rates are adjustable with selectable orifices. The connector layout remains common with VITA 46 (electrical backplane), so VITA 48.4 modules can coexist with conduction-cooled modules in a mixed chassis.

**Performance:** 200–500 W per 6U slot typical; theoretical ceiling approaching 1,000 W per slot depending on flow rate and coolant type.

**Coolant types supported:**
- Polyalphaolefin (PAO) oil — dielectric, food-safe, standard military/aerospace fluid; 5× more thermally efficient than air
- Inhibited glycol/water solutions (PGW, EGW) — water-glycol mix, corrosion inhibited
- Kerosene — available in some fielded platform cooling loops
- De-ionized water — high thermal performance but corrosion risk if not properly managed
- Salt water — viable in naval platforms with access to seawater cooling

**Chassis compatibility:** Elma Electronic offers VITA 48.4-compatible ATR chassis with electron-beam welded fluid channels in the sidewalls. 7Starlake's 7SL-3500-L2L is a self-contained VITA 48.4 LFT system for 3U VPX applications. Annapolis Micro Systems' WC34D0 is a liquid-cooled 3U OpenVPX chassis supporting LFT modules.

### Thermal Performance Comparison

| Method | Max W/Slot (6U) | Moving Parts | Coolant Required | Platform Integration |
|--------|----------------|--------------|-----------------|---------------------|
| Conduction (VITA 48.1) | ~150 W | None | None | Chassis cold wall |
| Air Flow-Through (VITA 48.8) | ~200 W | Fans in chassis | Ambient air | Air supply path |
| Liquid Flow-Through (VITA 48.4) | 200–500 W+ | None (in module) | Liquid loop | Platform coolant system |

### Chassis Architectures Using LFT

**Self-Contained (Closed-Loop) Systems**
Vendors like 7Starlake integrate the pump, heat exchanger, and coolant reservoir within the ATR chassis itself. The chassis is a sealed liquid-to-air system — liquid circulates internally, and the heat exchanger exhausts to ambient air via chassis-mounted fans. Advantage: no facility or platform cooling infrastructure needed. Limitation: ultimate thermal ceiling is still air-cooled on the outside.

**Platform-Coupled (Liquid-to-Liquid) Systems**
For vehicle, aircraft, or shipborne installations, the chassis LFT loop connects to the platform's existing coolant supply (aircraft environmental control system, vehicle engine cooling loop, shipboard chilled water). Advantage: significantly higher sustained power (platform cooling capacity can be hundreds of kW). Limitation: requires plumbing integration during platform installation.

## Notable Developments

- **2025-11 (AUSA):** nVent SCHROFF demonstrated a VITA 48.4 LFT module rated at 300 W per 6U slot at AUSA Annual Meeting 2025, highlighting liquid cooling as an emerging necessity for AI GPU-equipped VPX systems.
- **2025:** Elma Electronic released a rugged ATR chassis compatible with VITA 48.4 LFT 6U VPX modules, supporting MIL-STD-810G/F, MIL-STD-901D, and MIL-STD-461F.
- **2025:** 7Starlake released the 7SL-3500-L2L self-contained liquid-cooled 3U VPX ATR, supporting 500 W TDP in a closed-loop chassis.
- **2024–2025:** Annapolis Micro Systems' WC34D0 liquid-cooled 3U OpenVPX chassis with 100 GbE fabric and VITA 91 high-density connectors.
- **Ongoing:** VITA 48.8 AFT standard gaining adoption as a mid-tier alternative — simpler than LFT, more powerful than conduction.

## Key Ecosystem Players

| Company | Role | VITA 48.x Relevance |
|---------|------|---------------------|
| [Elma Electronic](https://www.elma.com) | Chassis/ATR manufacturer | VITA 48.4 LFT ATR chassis; ½ ATR to 1 ATR formats |
| [Annapolis Micro Systems](https://www.annapmicro.com) | FPGA boards + chassis | WC34D0 liquid-cooled 3U chassis; LFT module supplier |
| [7Starlake](https://7starlake.com) | Integrated VPX systems | 7SL-3500-L2L self-contained LFT system |
| [nVent SCHROFF](https://www.nvent.com/en-us/schroff) | Chassis and thermal enclosures | VITA 48.4 LFT module (300W/6U slot, AUSA 2025) |
| [LCR Embedded Systems](https://www.lcrembeddedsystems.com) | ATR chassis integrator | Conduction + LFT chassis; VITA 46.11 chassis manager |
| [Curtiss-Wright](https://defense-solutions.curtisswright.com) | VPX compute modules | VITA 48.8 AFT (FFT proprietary); VITA 48.1 conduction; Blackwell SOSA-aligned modules |
| [Mercury Systems](https://www.mrcy.com) | VPX compute modules | Conduction and AFT cooled modules; SOSA transition |

## Sources

- [VITA 48.4 Liquid Flow-Through in Rugged OpenVPX ATR Platform (Military Embedded Systems)](https://militaryembedded.com/radar-ew/thermal-management/liquid-flow-through-vita-484-cooling-technology-in-rugged-openvpx-atr-platform)
- [Tour of Thermal-Management Approaches for Rugged Computer Systems (Military Embedded Systems)](https://militaryembedded.com/radar-ew/thermal-management/cool-world-a-tour-of-thermal-management-approaches-for-rugged-computer-systems) — Conduction vs. AFT vs. LFT comparison; PAO oil 5× efficiency claim; 1,000 W LFT ceiling
- [Rugged ATR Platform for VITA 48.4 LFT Cooling (Elma Electronic)](https://www.elma.com/en/news-events/news-releases/rugged-atr-platform-for-vita-48-4-lft-cooling) — Elma chassis specs, electron-beam welded fluid channels, coolant types
- [VITA 48.8 AFT Standard (Curtiss-Wright)](https://defense-solutions.curtisswright.com/media-center/articles/vita-48.8-aft-cooling-standard-lowers-swap-c-on-deployed-vpx-systems) — AFT standard overview and SWaP-C advantages
- [Thermal Challenges in Rugged System Design (Electronic Design)](https://www.electronicdesign.com/technologies/industrial/boards/article/55233125/advanced-cooling-technologies-overcome-thermal-management-challenges-in-rugged-system-design-to-optimize-swap-c)
