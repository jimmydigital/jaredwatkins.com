---
title: "Bota Systems"
date: 2026-06-23
lastmod: 2026-06-23
draft: false
description: "Zürich, Switzerland force-torque sensor startup; ETH Zürich spinout; SensONE series provides 6-axis F/T sensing with on-board processing and multiple bus interfaces; vendor-supported ROS 2 driver; targeted at compliant manipulation and human-robot collaboration."
research_area: "robotics/sensors"
source_urls:
  - "https://www.botasys.com/force-torque-sensors/sensone"
  - "https://gitlab.com/botasys/bota_driver/"
last_reviewed: 2026-06-23
stale_after_days: 180
related: []
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Bota Systems, headquartered in Zürich, Switzerland, is an ETH Zürich spinout developing compact 6-axis force-torque sensors for robotics applications. The SensONE product family integrates strain gauge sensing, signal conditioning, and digital communication interfaces (EtherCAT, USB, SPI) into compact sensor housings designed to mount at robot wrist locations. The company maintains a vendor-supported ROS 2 driver (bota_driver, GitLab), and is listed on PickNik's ROS 2 hardware compatibility database in the Force Torque Sensors category.

## Key Facts

- **Founded:** ~2018 (ETH Zürich spinout)
- **HQ:** Zürich, Switzerland
- **Type:** Private (early/growth stage)
- **Key products:** SensONE 6-axis F/T sensor (multiple variants for different robot wrist mounting configurations); available with EtherCAT, USB, or SPI interface
- **Technology:** Strain gauge 6-axis force-torque measurement; on-board signal conditioning and digital output; selectable communication bus
- **ROS 2 driver:** Vendor-supported (gitlab.com/botasys/bota_driver)
- **PickNik compatibility:** Listed in Force Torque Sensors category; vendor-supported

## What It Is / How It Works

Force-torque sensors use strain gauges bonded to a precision-machined mechanical structure (typically cross-beam or Stewart platform geometry) to measure the six components of force and torque applied at the sensor's measurement point. The SensONE design integrates the analog strain gauge signal conditioning, analog-to-digital conversion, and digital protocol interface on a compact PCB inside the sensor housing, eliminating the need for external signal conditioning amplifiers that earlier-generation F/T sensors (like JR3) required.

The EtherCAT interface variant is particularly relevant for high-performance compliant manipulation: EtherCAT's deterministic, sub-millisecond cycle time allows force-torque data to be fed into robot control loops at rates >1 kHz, enabling high-bandwidth impedance control and contact detection. This is the architecture required for assembly tasks with tight tolerances (peg-in-hole, shaft insertion) and for safe physical human-robot contact.

## Notable Developments

- **Ongoing:** SensONE family expanded with variants supporting different robot flange mounting standards and communication interfaces.
- **~2020:** bota_driver ROS 2 driver published on GitLab; vendor-supported.
- **~2018:** Company founded as ETH Zürich spinout.

### People — Last Reviewed: 2026-06-23

## Supply Chain Position

Bota Systems operates at the **Complete Sensor System** layer in a high-value, low-volume niche. The primary competition is ATI Industrial Automation (Novanta subsidiary, US), which dominates the F/T sensor market but does not offer a public ROS 2 driver.

**⚑ Competing with ATI/Novanta:** ATI's Gamma and Delta series F/T sensors are the industry standard for surgical robotics and precision industrial assembly. ATI does not provide a public ROS 2 driver (PickNik lists them as "Not Available"), creating an opening for Bota Systems in ROS 2-based manipulation applications where customers prefer vendor-supported drivers.

## Claim Verification

### Claim: Bota SensONE supports EtherCAT interface
**Status:** Verified

**Supporting sources:**
- [Bota Systems product page](https://www.botasys.com/force-torque-sensors/sensone) — EtherCAT interface listed as product option

**Summary:** EtherCAT interface availability is directly stated in product documentation.

## Sources

- [SensONE Force-Torque Sensor — Bota Systems](https://www.botasys.com/force-torque-sensors/sensone)
- [bota_driver ROS 2 driver — GitLab](https://gitlab.com/botasys/bota_driver/)
- [PickNik ROS 2 Hardware Ecosystem (Force Torque Sensors)](https://picknik.ai/hardware-ecosystem/#force-torque-sensors)
