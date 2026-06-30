---
title: "Aaronia AARTOS"
date: 2026-06-05
lastmod: 2026-06-05
draft: false
description: "German RF spectrum monitoring-based drone detection system — passive RF from 20 MHz to 8 GHz; decodes DJI OcuSync, Mavlink, and 3G/4G/5G-connected drones; range up to 14 km."
research_area: "drone-detection/hardware"
source_urls:
  - "https://aaronia.com/en/solutions/drone-detection"
  - "https://drone-detection-system.com/aartos-dds/systems-versions/"
  - "https://downloads.aaronia.com/datasheets/solutions/drone_detection/Aaronia_AARTOS-DDS_Overview.pdf"
last_reviewed: 2026-06-05
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Aaronia AG (Germany) produces the AARTOS Drone Detection System — a passive RF monitoring platform that detects, decodes, and localizes drones by analyzing their electromagnetic emissions. AARTOS covers an unusually wide frequency range (20 MHz–8 GHz), decoding protocols including DJI OcuSync, Mavlink, and cellular-connected drones (3G/4G/5G). The flagship X9 variant claims up to 14 km range via scalable multi-node deployment. AARTOS is an RF-only system; it does not detect fiber-optic or pre-programmed RF-silent drones.

## Key Facts

- **Manufacturer:** Aaronia AG, Strickscheid, Germany
- **Type:** Company — RF sensor hardware + software
- **Frequency coverage:** 20 MHz–8 GHz
- **Protocol decoding:** DJI OcuSync, Mavlink, 3G/4G/5G drone uplinks; Remote ID
- **Coverage:** 360° full dome
- **Range by variant:**
  - X2 (portable/mobile): Up to 5 km
  - X9 (stationary): Up to 14 km (scalable via multi-node)
- **Status:** Active; commercial sales; export compliance standard German/EU

## Product Variants

**AARTOS X2:** Low-cost mobile drone detection. Portable for patrol or temporary deployment. Range up to 5 km. Single-node system for site security operations.

**AARTOS X9:** High-performance stationary system with 14 km range. Multi-node scaling available for extended area coverage. 360° full dome coverage with 3D direction finding (DF). Decodes manufacturer, model, and operator identity where protocol permits.

**AARTOS DDS (integrated systems):** Integrated counter-UAS variant combining AARTOS detection with optional EW countermeasures. Countermeasure options are jurisdiction-restricted.

## Capabilities

- **Drone manufacturer/model identification:** Protocol fingerprinting identifies specific DJI models, Mavlink-based platforms (ArduPilot), and other protocol-bearing drones
- **Operator location:** Where the control link is bidirectional and contains GPS, operator GPS coordinates can be extracted
- **Remote ID decoding:** ASTM F3411 / EUROCAE ED-269 ingestion
- **3G/4G/5G detection:** Drones using cellular uplinks (increasingly common for long-range or BVLOS operations) are detectable by their cellular signature

## Limitations

- **RF-only:** Zero capability against fiber-optic tethered or pre-programmed autonomous drones
- **Encrypted protocols:** Newer DJI O3 and some other protocols use encryption; decoding capability may be limited
- **No kinetic response:** Detection-only without countermeasure integration

## Sources

- [Aaronia AARTOS drone detection overview](https://aaronia.com/en/solutions/drone-detection)
- [AARTOS DDS systems and versions](https://drone-detection-system.com/aartos-dds/systems-versions/)
- [AARTOS DDS datasheet PDF](https://downloads.aaronia.com/datasheets/solutions/drone_detection/Aaronia_AARTOS-DDS_Overview.pdf)
