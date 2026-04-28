---
title: "u-blox"
date: 2026-03-31
lastmod: 2026-03-31
draft: false
description: "Thalwil, Switzerland GNSS chip and cellular module maker; formerly SIX: UBXN; acquired by Advent International for $1.3B (Nov 2025); 2024 revenue $262.9M (down 54% from $576.9M in 2023 due to inventory correction); ZED-F9P high-precision RTK GNSS module used in agricultural robots, AMRs, and drones; Stephan Zizala CEO."
tags: ["robotics", "sensors", "gnss", "components", "eu"]
categories: ["company"]
research_area: "robotics/sensors-lidar"
source_urls:
  - "https://en.wikipedia.org/wiki/U-blox"
  - "https://www.u-blox.com/"
  - "https://stockanalysis.com/quote/swx/UBXN/"
  - "https://www.u-blox.com/en/u-blox-announces-ceo-transition-effective-1-january-2023"
last_reviewed: 2026-03-31
stale_after_days: 90
related: []
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

u-blox (formerly SIX Swiss Exchange: UBXN), headquartered in Thalwil, Switzerland, designs semiconductor chips and wireless modules for GNSS positioning, cellular (LTE/5G) connectivity, and short-range radio (Bluetooth, Wi-Fi) in automotive, industrial, and robotics applications. Founded in 1997, the company established itself as the dominant supplier of compact, low-power GNSS positioning modules used in consumer devices, automotive systems, and increasingly in robotics — from agricultural autonomous tractors and precision-guided drones to indoor AMRs requiring GNSS waypoint integration. In November 2025, private equity firm Advent International completed the acquisition of u-blox for approximately $1.3 billion via a public tender offer on the Swiss Stock Exchange, delisting the company. 2024 revenue was $262.9 million, a 54% decline from $576.9 million in 2023, reflecting an industry-wide electronics inventory correction that particularly impacted wireless module suppliers.

## Key Facts

- **Founded:** 1997
- **HQ:** Thalwil, Switzerland
- **Type:** Private (acquired by Advent International, November 2025; formerly SIX: UBXN)
- **CEO:** Stephan Zizala (since January 1, 2023; succeeded Thomas Seiler, who served ~20 years)
- **Key products:** ZED-F9P (high-precision multi-band GNSS, cm-level RTK positioning); u-blox M9 / M10 (standard GNSS); SARA-R4/R5 (LTE-M/NB-IoT cellular); LARA-R6 (LTE Cat 1); NINA (Bluetooth/Wi-Fi combo); NEO-M8 series (legacy standard)
- **Revenue:** FY2024 $262.9M (−54.4% vs. FY2023 $576.9M); trailing twelve months to June 2025 ~$337M (partial recovery)
- **Acquisition:** Advent International $1.3B public tender offer, completed November 26, 2025

## What It Is / How It Works

u-blox's core product is the GNSS receiver chip and module: a small PCB-mountable device that receives GPS, GLONASS, Galileo, and BeiDou satellite signals and outputs a position fix (latitude, longitude, altitude) with associated accuracy. The standard consumer/industrial module (NEO-M8 series, M9, M10) provides 2–5 meter accuracy — adequate for general navigation. The ZED-F9P supports Real-Time Kinematic (RTK) positioning using correction data from a base station or correction service network, achieving 1–2 centimeter horizontal accuracy — the precision level required for agricultural autonomous steering (where a tractor must stay within 2 cm of a predefined row), drone precision landing, and ground robot localization when paired with pre-mapped environments.

The ZED-F9P has become the standard GNSS module in the professional autonomous outdoor robotics market: it appears in Monarch Tractor's MK-V, agricultural AutoSteer systems from John Deere (in non-Star Fire equipped applications), and the autopilot systems of professional UAS platforms. Its dual-frequency (L1/L2 GPS plus multi-constellation) capability and multi-band RTK algorithms make it the price/performance benchmark for cm-accuracy GNSS in robotic applications.

In cellular modules, u-blox supplies the LTE-M and NB-IoT modules used in asset tracking, industrial IoT, and cellular-connected drone command-and-control links. The SARA-R4 series became the standard for Cat-M1 cellular connectivity in low-power IoT devices.

The 2023–2024 revenue decline reflects a dramatic inventory correction across the electronics supply chain: post-COVID demand pulled forward massive orders that left distributors and OEM customers with 12–18 months of buffer stock entering 2023. Module suppliers including u-blox, Quectel, and Sierra Wireless all saw order cancellations and demand reductions as customers worked through inventory — not a demand destruction event but a timing dislocation. The $337M trailing twelve-month figure to mid-2025 indicates the correction is partially unwinding.

## Notable Developments

- **2025-11-26:** Advent International completes $1.3B acquisition of u-blox via public tender offer; company delisted from SIX Swiss Exchange. ([u-blox press release](https://www.u-blox.com/))
- **2025:** Revenue recovery begins; trailing twelve months to June 2025 approximately $337M vs. FY2024 $262.9M.
- **2024:** FY2024 revenue $262.9M, down 54.4% from FY2023 $576.9M — inventory correction impact. ([StockAnalysis](https://stockanalysis.com/quote/swx/UBXN/))
- **2023-01:** CEO transition: Stephan Zizala succeeds Thomas Seiler as CEO effective January 1, 2023. ([u-blox](https://www.u-blox.com/en/u-blox-announces-ceo-transition-effective-1-january-2023))
- **1997:** Founded in Thalwil, Switzerland; went public on SIX Swiss Exchange.

## Key People

### Stephan Zizala — CEO
- **LinkedIn:** Not confirmed in public search
- **Education:** Not publicly disclosed
- **Career (reverse-chronological):**
  - u-blox (2023–present): CEO
  - u-blox (prior): Senior executive roles before CEO appointment
- **Notes:** Stepped up from within the company to replace long-serving founder CEO Thomas Seiler.

### People — Last Reviewed: 2026-03-31

## Supply Chain Position

u-blox operates as a **Component-Subsystem Supplier** at the GNSS module and cellular module layer. The company is a fabless semiconductor designer for its chips (GNSS receiver ASICs manufactured at Asian foundries), and an integrated module assembler where it packages the chip with RF front-end, antenna connector, and baseband processing. The finished module is a drop-in PCB component that robotics engineers can use without deep RF design expertise — a key value-add for the large robotics engineering market that is software-strong but RF-capability-light.

**⚑ BeiDou/Chinese positioning dependency note:** u-blox modules support BeiDou (Chinese GPS system) alongside GPS, Galileo, and GLONASS. This multi-constellation support is a feature for global coverage, but BeiDou signal availability creates an integration pathway for Chinese satellite infrastructure into non-Chinese systems. U-blox modules that receive BeiDou in GNSS-denied environments where only BeiDou is available could create an operational dependency on Chinese satellite infrastructure.

**⚑ Competition from Quectel:** Quectel (Shanghai, Chinese-owned) produces competing GNSS and cellular modules at substantially lower prices. The u-blox vs. Quectel choice is a common design decision in robotics and IoT — u-blox for quality/reliability/support, Quectel for cost optimization.

## Claim Verification

### Claim: u-blox ZED-F9P is the standard high-precision GNSS module in professional autonomous robotics
**Status:** Partially verified

**Supporting sources:**
- ZED-F9P is extensively referenced in agricultural robot, drone autopilot, and professional UGV technical documentation as the positioning module of choice
- The module appears in published design references for ArduPilot, PX4, and other open-source autopilot systems
- Multiple agricultural robot OEMs (including published specs from companies using u-blox for RTK positioning) confirm the module's market position

**Refuting / questioning sources:**
- "Standard" is a qualitative claim; NovAtel (Hexagon), Trimble, and Septentrio all supply high-precision GNSS modules in overlapping applications, particularly in higher-value agriculture and survey applications where OEMs prefer full-system suppliers
- Quectel's LG69T AG and similar modules are entering the RTK market at lower price points, potentially eroding ZED-F9P's market share in cost-sensitive segments

**Summary:** The ZED-F9P is the dominant reference-design GNSS module in the professional robotics RTK positioning market based on its prevalence in published technical documentation; full market share data is not independently available.

## Sources

- [u-blox Wikipedia](https://en.wikipedia.org/wiki/U-blox)
- [u-blox CEO Transition — u-blox (Jan 2023)](https://www.u-blox.com/en/u-blox-announces-ceo-transition-effective-1-january-2023)
- [u-blox SWX:UBXN Revenue — StockAnalysis](https://stockanalysis.com/quote/swx/UBXN/)
- [u-blox website — u-blox.com](https://www.u-blox.com/)
