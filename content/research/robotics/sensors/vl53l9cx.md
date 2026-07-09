---
title: "STMicroelectronics VL53L9CX"
date: 2026-07-09
lastmod: 2026-07-09
draft: false
description: "STMicroelectronics' newest FlightSense direct Time-of-Flight (dToF) LiDAR module — up to 54x42 (~2.3k) zone multizone ranging, <5 cm to 8.8 m range, 100 Hz frame rate; currently in evaluation/engineering-sample stage."
research_area: "robotics/sensors"
source_urls:
  - "https://www.st.com/en/imaging-and-photonics-solutions/vl53l9cx.html"
  - "https://www.st.com/resource/en/datasheet/vl53l9cx.pdf"
last_reviewed: 2026-07-09
stale_after_days: 90
related:
  - "u-blox.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

The VL53L9CX is STMicroelectronics' newest direct Time-of-Flight (dToF) LiDAR module in its FlightSense product family, offering what ST describes as market-leading resolution of up to 2.3k zones (54x42) in a fully integrated, reflowable miniature package. As of this review the part is in the **Evaluation stage** — ST's own product page lists it as "Product is under characterization. Limited Engineering samples available," and the datasheet (DS14879, Rev 6, June 2026) is marked "Prerelease product(s)" on every page. It targets robotics (SLAM, obstacle avoidance, small-object identification), AR/VR, industrial content management, smart-home, and mobile-device applications.

## Key Facts

- **Developed by:** STMicroelectronics, part of the ST FlightSense product family (Imaging and Photonics Solutions / Time-of-Flight sensors line)
- **Type:** Component / subsystem — 3D dToF all-in-one LiDAR module
- **Status:** Evaluation — under characterization; limited engineering samples available as of 2026-07 (order code VL53L9CXV0VE/1, Optical LGA package, tape-and-reel, minimum order quantity 1,000)
- **Datasheet:** DS14879, Rev 6, June 2026 (Rev 5 first public release 2026-05-18; Rev 6 updated 2026-06-15 with revised I²C/XSHUT/INTR/SYNC_IN electrical characteristics)
- **Resolution:** Up to 54x42 zones (binning 2; ~2.3k zones), with binning options down to 4x4
- **Ranging:** <5 cm (precision mode) to 8.8 m (best case); 45 cm to 8.5 m in ambient mode
- **Frame rate:** Up to 100 Hz
- **Field of view:** 55° x 42° (71° diagonal), using metasurface optical elements (MOE) on both transmitter and receiver
- **Illumination:** Two 940 nm VCSEL flood emitters with integrated analog driver; Class 1 laser safe (IEC 60825-1:2014)
- **Size:** 12.8 x 6.1 x 4.6 mm
- **Interfaces:** I3C (12.5 MHz) and I²C (1 MHz) control; MIPI CSI-2 (1 Gbps) or I3C (12.5 Mbps) data output

## What It Is / How It Works

The VL53L9CX is a direct Time-of-Flight (dToF) sensor: it measures distance by timing the round-trip of pulsed laser light rather than inferring depth from stereo disparity or structured light. Two 940 nm VCSEL emitters flood-illuminate the scene through transmitter-side metasurface optical elements (MOE) that shape the beam into a rectangular 55°x42° field of view. The reflected light is focused by a receiver lens onto an array of single-photon avalanche diodes (SPADs) — up to 54x42 zones at full resolution, each zone formed from a 2x2 macro-SPAD binning group. An on-chip MCU runs histogram processing and dToF ranging hardware directly on the module, so the host receives already-processed range, amplitude, ambient, and dynamic-SPAD-selection (DSS) arrays rather than raw photon timing data.

Two ranging modes are available: a precision mode optimized for close, accurate measurement (down to <5 cm) and an ambient mode optimized for operation under IR ambient light (from 45 cm). A dynamic SPAD selection (DSS) algorithm keeps the signal rate within a target range to preserve accuracy as scene reflectance and distance vary. On-chip histogram processing and algorithmic compensation are used to reduce the impact of cover-glass crosstalk and veiling glare — a common failure mode for ToF sensors mounted behind a cover window.

Output is available over MIPI CSI-2 (up to 1 Gbps, the default and highest-bandwidth path) or via the I3C/I²C control interface directly, though the achievable frame rate drops with the slower control-interface path. ST's published profile examples illustrate the range of trade-offs the sensor supports: a "Gaming" profile runs full 54x42 resolution at 100 fps (420 mW); a "Room mapping" profile trades frame rate for range at 30 fps in ambient mode (200 mW, 8 m); an "Autofocus" profile runs reduced 24x20 resolution at 15 fps in an ultralow-power mode (80 mW); and a "Wake on approach" profile drops to 1 fps at 12x10 resolution for standby-level power draw (12.5 mW).

The module integrates the SPAD sensor, postprocessing SoC, VCSEL driver (BCD process), and PMIC into a single reflowable component — intended to minimize bill-of-materials and integration effort relative to discrete ToF designs. It supports dual power-supply operation (1.2 V / 3.3 V among other rail options) and is rated for -30°C to 70°C ambient operation (with a hardware temperature-protection cutoff between -35°C and 105°C junction temperature).

## Notable Developments

- **2026-06-15:** Datasheet DS14879 Rev 6 published, updating the I²C/XSHUT/INTR/SYNC_IN digital I/O electrical characteristics table.
- **2026-05-18:** Datasheet DS14879 Rev 5 — first public release.
- **2026 (current):** Product listed on st.com under "Evaluation" marketing status with limited engineering samples available; not yet in full production.

## Key People / Key Organizations

- **STMicroelectronics** — Franco-Italian semiconductor manufacturer (NYSE/Euronext Paris/Borsa Italiana: STM); developer of the VL53L9CX as part of its FlightSense ToF sensor line, which also includes the earlier, lower-resolution VL53L5CX multizone ToF sensor. No individual product engineers are named in the publicly available datasheet or product page.

### People — Last Reviewed: 2026-07-09

## Claim Verification

### Claim: "The fastest, truly integrated 3D lidar camera module on the market"
**Status:** Unverified (self-reported)

**Supporting sources:**
- [VL53L9CX datasheet, DS14879 Rev 6](https://www.st.com/resource/en/datasheet/vl53l9cx.pdf) — states this claim directly in the Description section, based on 100 Hz max frame rate at full 54x42 resolution

**Refuting / questioning sources:**
- None found. This is a first-party marketing claim; no independent benchmark comparing it against competing integrated ToF/LiDAR camera modules (e.g., other FlightSense predecessors, competing multizone ToF sensors) was found.

**Summary:** The frame-rate and resolution figures themselves are specified in ST's own datasheet, but the superlative "fastest on the market" claim has no independent, third-party verification identified.

### Claim: Ranging up to 8.8 m with sub-percent accuracy at long range
**Status:** Partially verified (first-party characterization only)

**Supporting sources:**
- [VL53L9CX datasheet, DS14879 Rev 6](https://www.st.com/resource/en/datasheet/vl53l9cx.pdf) — Section 8 (Ranging performances) reports 8.8 m maximum range achieved only indoors at 0 W/m² ambient illumination with a high-reflectance (62%) target; outdoor sunny conditions reduce max range to 6.0–7.6 m depending on profile and target reflectance. Accuracy is reported as <8 mm absolute error at short range and <0.5% relative error at long range under the same indoor/gray-target conditions, degrading somewhat outdoors (e.g., up to 1.8% relative error in ambient mode under outdoor sunny conditions on gray 62% targets).

**Refuting / questioning sources:**
- None found. All performance figures trace to ST's own datasheet characterization; no independent lab measurement was located.

**Summary:** The headline 8.8 m range and sub-1% accuracy figures are real but condition-dependent — they apply to best-case indoor/high-reflectance scenarios, not the full range of outdoor and low-reflectance conditions documented in the same datasheet. No third-party verification of these figures exists yet, consistent with the part's current evaluation/pre-production status.

## Supply Chain Position

The VL53L9CX sits at the **Complete Sensor System** layer of the robotics sensors supply chain (see [Robotics Sensors]({{< relref "_index.md" >}})) — a fully packaged, reflowable module rather than a discrete component requiring further system integration. STMicroelectronics is a large, vertically integrated semiconductor manufacturer (Incumbent tier in this section's company tables) that designs and fabricates its own SPAD arrays, VCSELs, and ToF processing silicon using its BSI (backside-illuminated) stacked CMOS process, giving it more manufacturing control than fabless competitors in the sensor module space.

**⚑ FlightSense product family:** The VL53L9CX extends ST's existing FlightSense line, which includes lower-resolution multizone ToF parts such as the VL53L5CX. As the part is still in evaluation/sampling status, it has not yet been confirmed in any specific robotics OEM design.

## Sources

- [VL53L9CX Product Page — STMicroelectronics](https://www.st.com/en/imaging-and-photonics-solutions/vl53l9cx.html) — Marketing status ("Evaluation"), part number, package, ordering details
- [VL53L9CX Datasheet, DS14879 Rev 6 — STMicroelectronics](https://www.st.com/resource/en/datasheet/vl53l9cx.pdf) — Full technical specifications, ranging performance, electrical characteristics, pinout
