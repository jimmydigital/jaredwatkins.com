---
title: ROS 2 Ecosystem
date: 2026-06-23
lastmod: 2026-06-23
draft: false
description: "Robot Operating System 2 (ROS 2) middleware, tooling, and the hardware and software ecosystem built around it — from Open Robotics foundations to commercial integrators and MoveIt Pro."
tags: ["robotics", "ros2", "middleware", "software"]
categories: ["overview"]
research_area: "robotics/ros2"
last_reviewed: 2026-06-23
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9
  disable: false
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


## Overview

ROS 2 (Robot Operating System 2) is the dominant open-source middleware platform for professional and research robotics, maintained by Open Robotics and the broader ROS community. It provides a standardized publish-subscribe communications framework, hardware abstraction, sensor drivers, and tool libraries that allow engineers to build complex robot systems without writing communications infrastructure from scratch. ROS 2 replaced the original ROS (now often called ROS 1) with improved real-time performance, security (DDS-based communications), multi-robot support, and Python 3/C++ 17 compatibility. Virtually all serious robotics research and most commercial robot development now targets ROS 2. The hardware ecosystem around ROS 2 — robots, sensors, actuators, and compute — is tracked comprehensively by PickNik Robotics at their [ROS 2 Compatible Hardware database](https://picknik.ai/hardware-ecosystem/).

## Key Themes

- ROS 2 is the de facto lingua franca of professional robotics — vendor-supported ROS 2 drivers are now table stakes for hardware market entry
- PickNik's MoveIt framework (MoveIt 2 / MoveIt Pro) is the dominant motion planning stack built on ROS 2; PickNik maintains the most complete ROS 2 hardware compatibility database
- Hardware driver quality varies enormously: "great" drivers support >500 Hz streaming enabling visual servoing and force compliance; "poor" single-point drivers limit sophisticated applications
- Commercial robot arm market is consolidating around vendor-supported ROS 2 drivers (Universal Robots, Kinova, FANUC, KUKA all offer vendor-maintained drivers)
- Depth sensor and LiDAR categories have near-universal ROS 2 support (95%+ of tracked sensors); motor controllers and actuator components lag (25–30% support)
- Chinese hardware dominates on price but faces increasing US government procurement restrictions; ROS 2 driver availability does not mitigate national security restrictions

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [PickNik Robotics](https://picknik.ai) | Boulder, CO, USA | Private | MoveIt Pro commercial motion planning platform; primary MoveIt 2 maintainer; ROS 2 driver development services; maintains the largest public ROS 2 hardware compatibility database. |
| [Clearpath Robotics](https://clearpathrobotics.com) | Kitchener, ON, Canada | Private (Rockwell Automation subsidiary) | Husky and Ridgeback mobile robot platforms with strong ROS 2 support; heavily used in academic and defense research. |
| [Hello Robot](https://hello-robot.com) | Seattle, WA, USA | Series A | Stretch mobile manipulation robot; vendor-supported ROS 2 driver; designed for human-scale environments. |
| [Intrinsic](https://intrinsic.ai) | Mountain View, CA, USA | Alphabet subsidiary | Industrial robotics software including ROS 2-based autonomy tools; Alphabet spin-out from X. |
| [Open Robotics](https://openrobotics.org) | Mountain View, CA, USA | Non-profit (merged into Open Source Robotics Alliance) | Original ROS maintainer; stewards the ROS 2 codebase and build infrastructure. |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [ROK](https://finance.yahoo.com/quote/ROK) | [Rockwell Automation](https://www.rockwellautomation.com) | Industrial automation; owns Clearpath Robotics (acquired 2023); significant ROS 2 ecosystem stake. |
| [NVDA](https://finance.yahoo.com/quote/NVDA) | [NVIDIA](https://developer.nvidia.com/isaac-ros) | Isaac ROS hardware-accelerated ROS 2 packages for Jetson; dominant compute platform for onboard robot AI inference. |

<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container" style="margin: 20px 0;">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
  {
    "colorTheme": "light",
    "dateRange": "12M",
    "showChart": true,
    "locale": "en",
    "showSymbolLogo": true,
    "showFloatingTooltip": true,
    "width": "100%",
    "height": "500",
    "tabs": [
      {
        "title": "ROS 2 Ecosystem",
        "symbols": [
          {"s": "NYSE:ROK", "d": "Rockwell Automation"},
          {"s": "NASDAQ:NVDA", "d": "NVIDIA"}
        ],
        "originalTitle": "ROS 2 Ecosystem"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [ABB](https://finance.yahoo.com/quote/ABB) | [ABB Robotics](https://new.abb.com/products/robotics) | Major industrial robot OEM; community-supported ROS 2 driver maintained in part by PickNik. |
| [FANUC](https://finance.yahoo.com/quote/FANUCF) | [FANUC](https://www.fanuc.com) | World's largest industrial robot maker; vendor-supported ROS 2 driver; Gold PickNik integration. |
| [6356.T](https://finance.yahoo.com/quote/6356.T) | [KUKA](https://www.kuka.com) | German industrial robot maker (Midea-owned); multiple vendor-supported ROS 2 drivers across LBR and KR series. |

## ROS 2 Hardware Compatibility Summary

The following table summarizes PickNik's tracked hardware categories and ROS 2 support rates (as of June 2026):

| Category | Brands Tracked | ROS 2 Support Rate |
|----------|----------------|-------------------|
| Robot Arms | 48 | 75% |
| Grippers & End Effectors | 4 | 100% |
| Depth Sensors | 22 | 95% |
| AGVs | 4 | 100% |
| AMRs | 7 | 100% |
| Linear Actuator / Gantry | 3 | 100% |
| Drone Controllers | 2 | 100% |
| Force Torque Sensors | 4 | 75% |
| Tool Changers | 2 | 0% |
| Human Robot Interfaces | 4 | 100% |
| Industrial Computers | 5 | 100% |
| Custom Joint Modules | 2 | N/A (component) |
| Encoders | 1 | N/A (component) |
| Gear Boxes | 3 | N/A (component) |
| Motor Controllers | 7 | 29% |
| Motors / Actuators | 8 | 25% |
| Open Source / DIY Arms | 2 | 100% |

Source: [PickNik ROS 2 Hardware Ecosystem](https://picknik.ai/hardware-ecosystem/)
