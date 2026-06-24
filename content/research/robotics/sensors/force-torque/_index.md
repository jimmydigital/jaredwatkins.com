---
title: Force-Torque Sensors
date: 2026-06-23
lastmod: 2026-06-23
draft: false
description: "6-axis force-torque sensors for robot wrist applications — enabling compliant manipulation, assembly force control, and human-robot collaboration."
tags: ["robotics", "sensor", "force-torque", "manipulation"]
categories: ["overview"]
research_area: "robotics/sensors"
last_reviewed: 2026-06-23
stale_after_days: 180
sitemap:
  changefreq: "monthly"
  priority: 0.8
  disable: false
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


## Overview

Force-torque (F/T) sensors mounted at the robot wrist between arm and end effector measure the six-component wrench (three forces, three torques) applied at the tool center point. This feedback enables robots to perform compliant manipulation tasks — assembly with tight tolerances, grinding and deburring, polishing, safe physical human-robot contact — that are impossible with position control alone. The force-torque sensor market is a high-value, defensible niche with limited competition: ATI Industrial Automation (US), Robotiq (Canada), and Bota Systems (Switzerland) are the dominant players with ROS 2 support, while JR3 (US) is community-supported.

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Bota Systems](https://www.botasys.com) | Zürich, Switzerland | Growth (ETH Zürich spinout) | SensONE family of compact F/T sensors with on-board signal processing and EtherCAT/USB/SPI interfaces; vendor-supported ROS 2 driver. |
| [Robotiq](https://robotiq.com) | Lévis, Québec, Canada | Private (acquired by OnRobot 2023) | FT 300S force-torque sensor; integrated with Robotiq gripper ecosystem and Universal Robots e-Series; Gold MoveIt Pro integration via PickNik. |

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [ATI Industrial Automation](https://www.ati-ia.com) | Apex, NC, USA (Novanta subsidiary) | World's largest F/T sensor manufacturer; Gamma, Delta, Theta series; used in surgical robots, industrial assembly, and precision manufacturing; no public ROS 2 driver. |
| [JR3](https://www.jr3.com) | Woodland, CA, USA | Long-established F/T sensor maker; community-supported ROS 2 driver (rosjr3). |
