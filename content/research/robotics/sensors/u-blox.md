---
title: "u-blox"
date: 2026-03-31
lastmod: 2026-03-31
draft: false
description: "Swiss GNSS module and cellular IoT module maker (formerly SIX: UBXN); taken private by Advent International for $1.3B in November 2025; F9 RTK GNSS and M9 modules are dominant in drone, AMR, and precision agriculture robotics positioning."
tags: ["robotics", "sensor", "gnss", "eu"]
categories: ["company"]
research_area: "robotics/sensors"
source_urls:
  - "https://www.adventinternational.com/news/advent-completes-acquisition-of-u-blox/"
  - "https://www.u-blox.com/en/positioning-chips-and-modules"
  - "https://content.u-blox.com/sites/default/files/ZED-F9P_ProductSummary_UBX-17005151.pdf"
last_reviewed: 2026-03-31
stale_after_days: 180
related: []
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

u-blox (formerly SIX Swiss Exchange: UBXN) is a Thalwil, Switzerland-based designer of GNSS positioning chips and modules, and cellular IoT communication modules. It was taken private by US private equity firm Advent International in November 2025 for CHF 1.05 billion ($1.3B). The company's F9 and M9 GNSS module families — particularly the ZED-F9P with centimeter-level RTK accuracy — are pervasive in drone navigation, autonomous mobile robots, precision agricultural equipment, and ground vehicle positioning. u-blox does not manufacture its own chips; it is a fabless design house that outsources production to semiconductor foundries and contract manufacturers. Its cellular module line (SARA, LARA series) positions it as a full connectivity supplier for robotics platforms.

## Key Facts

- **Founded:** 1997 (Thalwil, Switzerland)
- **HQ:** Thalwil, Switzerland
- **Type:** Private (acquired by Advent International November 2025 for ~$1.3B; previously SIX Swiss Exchange: UBXN)
- **Ownership:** Advent International (private equity, Boston, MA) since November 2025
- **Key products:** ZED-F9P (multi-band RTK GNSS, centimeter-level accuracy); NEO-M9N (standard GNSS module); SARA-R4/R5 (LTE-M/NB-IoT cellular modules); LARA-R6 (LTE advanced cellular)
- **Revenue:** Not disclosed post-privatization; u-blox announced significant project wins in robotic lawnmowers expected to generate $100M+ in revenue from 2024
- **Current leadership:** Co-CEOs Camila Japur (CFO) and Andreas Thiel (co-founder, head of business units) — as of January 2026 following Stephan Zizala's departure

## What It Is / How It Works

u-blox's GNSS modules integrate a GNSS receiver chip (processing satellite signals from GPS, GLONASS, Galileo, BeiDou), RF front end, and supporting circuitry into a compact module with a standard pin interface. The module approach allows robotics engineers to add positioning capability without designing the RF circuitry from scratch — u-blox handles the antenna matching, RF shielding, and firmware, and the module is dropped onto a PCB with minimal integration effort.

The F9 platform, the current flagship GNSS architecture, supports multi-band reception (L1+L5 or L1+L2 depending on variant). Multi-band capability is critical for RTK (Real-Time Kinematic) positioning: RTK uses carrier-phase measurements from a second receiver (a fixed base station or a network of reference stations) to compute corrections that reduce positioning error from meters to centimeters. The ZED-F9P, the most widely deployed F9 variant in robotics, achieves <1 cm horizontal accuracy in RTK mode with reliable correction data, with convergence time of approximately 60 seconds in PPP-RTK mode. This accuracy level enables precision row following in agricultural robots, lane-level positioning for AMRs operating outdoors, and reliable GPS-denied detection (when satellite signal is lost, the module flags it immediately rather than coasting on degraded data).

The M9 platform is the standard-grade tier: multi-constellation, single-band, sub-meter accuracy. It is the appropriate choice for applications where centimeter precision is unnecessary — logistics drones tracking coarse location, indoor-outdoor handoff systems, or consumer-grade autonomous systems. The M9N is the most common variant.

u-blox's cellular module line (SARA for LTE-M/NB-IoT, LARA for full LTE Cat 4+) is a growth area aimed at providing a combined GNSS + cellular solution for connected robots that need both positioning and cloud connectivity. In practice, many drone and AMR designs integrate a u-blox GNSS module alongside a separate cellular module from Quectel or Sierra Wireless — u-blox's ambition is to win both sockets on the same board.

The company is fabless — it designs chips and modules but contracts manufacturing to foundries. This is standard practice for analog/RF semiconductor companies but means u-blox is exposed to foundry allocation and lead-time constraints when demand spikes, as seen during the 2021–2022 semiconductor shortage.

The Advent International acquisition at a 53% premium to the prior 6-month volume-weighted average price reflects the strategic value of u-blox's market position — particularly its dominant design-in position in robotics GNSS. Advent took the company private to pursue accelerated growth without the quarterly reporting pressures of the public market.

## Notable Developments

- **2025-11:** Advent International completes acquisition of u-blox for ~$1.3B (CHF 1.05B); u-blox delisted from SIX Swiss Exchange; Stephan Zizala departs as CEO; Camila Japur and Andreas Thiel assume co-CEO roles. ([Advent International](https://www.adventinternational.com/news/advent-completes-acquisition-of-u-blox/))
- **2025-08:** Advent International announces takeover bid at 53% premium to 6-month VWAP; deal agreed by u-blox board. ([RCR Wireless](https://www.rcrwireless.com/20250818/internet-of-things/u-blox-sale-pe))
- **2024+:** Robotic lawnmower design wins expected to generate $100M+ in annual revenue starting 2024. ([Electronic Specifier](https://www.electronicspecifier.com/industries/robotics/u-blox-secures-significant-project-wins-in-the-robotic-lawnmower-market))
- **2023-01:** Stephan Zizala (former Infineon executive) becomes CEO, succeeding Thomas Seiler.
- **2021:** Acquisition of Sapcorda Services GmbH, a high-precision GNSS correction service provider, expanding into GNSS-as-a-service.
- **1997:** Company founded in Thalwil, Switzerland by ETH Zurich researchers.

## Key People

### Andreas Thiel — Co-CEO (since January 2026) and Co-Founder
- **LinkedIn:** Not found (no confirmed public profile)
- **Education:** Not publicly disclosed
- **Career (reverse-chronological):**
  - u-blox (1997–present): Co-founder; Head of Business Units; Co-CEO from January 2026
- **Notes:** Thiel is one of the original ETH Zurich founders of u-blox and has been a continuous presence through all ownership transitions.

### Camila Japur — Co-CEO (since January 2026) and CFO
- **LinkedIn:** Not found (no confirmed public profile)
- **Career (reverse-chronological):**
  - u-blox: CFO; Co-CEO from January 2026
- **Notes:** Appointed Co-CEO alongside Thiel following Zizala's departure upon the Advent acquisition close.

### Thomas Seiler — Former CEO (2002–2022)
- **LinkedIn:** [linkedin.com/in/thomas-seiler-95062911a](https://ch.linkedin.com/in/thomas-seiler-95062911a)
- **Education:** ETH Zurich (mechanical engineering); INSEAD (MBA)
- **Career (reverse-chronological):**
  - u-blox (2002–2022): CEO; Board Member and Strategy Committee Chair post-retirement
  - Kistler Holding AG (1999–2001): CEO
  - Melcher Holding AG (1987–1998): Executive Committee member; CEO 1991–1998
- **Notes:** Seiler led u-blox for over 20 years, building the company from a startup to a global GNSS module leader before its eventual privatization.

### People — Last Reviewed: 2026-03-31

## Supply Chain Position

u-blox operates at the **Component/Subsystem Supplier** layer: it sells GNSS and cellular modules to drone OEMs, AMR manufacturers, agricultural equipment makers, and robotics integrators. Being fabless, u-blox sources its chips from semiconductor foundries (not disclosed publicly) and assembles modules at contract manufacturers. **⚑ Shared supply chain exposure:** u-blox GNSS modules compete with STMicroelectronics Teseo, Quectel (GNSS module line), and Septentrio (high-precision RTK) for drone and AMR design wins; many platforms spec u-blox by name due to the dominant ecosystem of developer tooling and reference designs.

## Claim Verification

### Claim: ZED-F9P achieves centimeter-level RTK accuracy for robotics applications
**Status:** Verified

**Supporting sources:**
- [ZED-F9P Product Summary — u-blox](https://content.u-blox.com/sites/default/files/ZED-F9P_ProductSummary_UBX-17005151.pdf) — Datasheet specifies <1 cm horizontal RTK accuracy (CEP 50%)
- [Low-Cost GNSS and PPP-RTK Study — MDPI Sensors (2023)](https://www.mdpi.com/1424-8220/23/13/6074) — Independent academic evaluation confirms ZED-F9P achieves centimeter-level positioning in PPP-RTK mode with ~60s convergence; validated against geodetic-grade reference

**Refuting / questioning sources:**
- RTK accuracy is contingent on correction data availability, satellite geometry, multipath environment, and atmospheric conditions; in GPS-denied urban canyons or under tree canopy, accuracy degrades significantly; the centimeter-level claim assumes open sky and a functioning base station or NTRIP network within ~30km

**Summary:** The centimeter-level RTK claim is well-verified under appropriate conditions; real-world robotics deployments must account for correction data latency and environmental degradation.

## Sources

- [Advent Completes Acquisition of u-blox — Advent International (Nov 2025)](https://www.adventinternational.com/news/advent-completes-acquisition-of-u-blox/)
- [u-blox Sale to Advent International — RCR Wireless (Aug 2025)](https://www.rcrwireless.com/20250818/internet-of-things/u-blox-sale-pe)
- [Zizala Out as Advent Takes Over — Location Business News](https://locationbusinessnews.com/shake-up-at-u-blox-zizala-out-as-private-equity-firm-takes-over)
- [ZED-F9P Product Summary — u-blox](https://content.u-blox.com/sites/default/files/ZED-F9P_ProductSummary_UBX-17005151.pdf)
- [u-blox Robotic Lawnmower Wins — Electronic Specifier](https://www.electronicspecifier.com/industries/robotics/u-blox-secures-significant-project-wins-in-the-robotic-lawnmower-market)
- [ZED-F9P PPP-RTK Study — MDPI Sensors (2023)](https://www.mdpi.com/1424-8220/23/13/6074)
- [Thomas Seiler LinkedIn](https://ch.linkedin.com/in/thomas-seiler-95062911a)
