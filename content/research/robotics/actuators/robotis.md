---
title: "Robotis (Dynamixel)"
date: 2026-06-23
lastmod: 2026-06-23
draft: false
description: "Seoul, South Korea smart servo actuator manufacturer; Dynamixel series is the dominant integrated actuator module for research and educational robots; vendor-supported ROS 2 driver; widely used in humanoid, collaborative robot, and research platforms globally."
research_area: "robotics/actuators"
source_urls:
  - "https://www.robotis.us/"
  - "https://emanual.robotis.com/docs/en/platform/op2/ros_package/"
  - "https://github.com/ROBOTIS-GIT/dynamixel-workbench"
last_reviewed: 2026-06-23
stale_after_days: 180
related: []
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Robotis, headquartered in Seoul, South Korea, is the manufacturer of the Dynamixel smart servo actuator series — the most widely used integrated actuator module in robotics research, education, and development-stage commercial robots worldwide. Unlike commodity servo motors, Dynamixel actuators integrate the motor, gearbox, driver electronics, encoder, and communications bus (TTL/RS-485, later USB) into a single compact module with a standardized daisy-chain protocol. This integration dramatically simplifies robot joint design and has made Dynamixel the de facto standard for research platforms from small desktop robots to full humanoid systems. Robotis provides a vendor-supported ROS 2 driver (Dynamixel Workbench), maintaining compatibility with the ROS 2 ecosystem.

## Key Facts

- **Founded:** 1999
- **HQ:** Seoul, South Korea
- **Type:** Private
- **Key products:** Dynamixel XL, XC, XM, XH, XW, and MX series smart servo actuators; OpenCR embedded controller board; ROBOTIS OP3 (open-platform humanoid); TurtleBot3 (mobile research platform with Open Robotics)
- **Value chain position:** Component/Subsystem Supplier (integrated actuator modules to OEMs and researchers)
- **ROS 2 driver:** Vendor-supported; Dynamixel Workbench + DynamixelSDK
- **Notable OEM relationships:** TurtleBot3 is co-developed with Open Robotics (the ROS maintainer); OpenMANIPULATOR-X used in many ROS 2 tutorials; OP3 humanoid used in RoboCup Humanoid League

## What It Is / How It Works

Dynamixel actuators are "smart" servo motors: each unit packages a DC brushed or brushless motor, reduction gearbox, position/velocity/current encoder, PID motor driver, and a half-duplex TTL or RS-485 communications interface into a single enclosed module with standardized mounting patterns. The distinguishing feature is the daisy-chain bus architecture — dozens of actuators can be chained on a single cable with each unit addressed individually by ID. This eliminates the per-joint point-to-point wiring required by conventional servo systems and dramatically simplifies robot assembly.

The Dynamixel line spans a wide torque range. At the low end, the XL series (XL330, XL430) is designed for small desktop robots, grippers, and educational platforms. The XM and XH series cover mid-range collaborative and research robots. The XW series (XW540, XW430) provides waterproof sealing for outdoor and underwater applications. The highest-torque variant, the PH54 and PM54 Pro series, targets full humanoid and heavy manipulation applications.

The ROS 2 driver (dynamixel_workbench_ros2 / DynamixelSDK) uses the ros2_control framework to expose Dynamixel joints as standard ROS 2 hardware interfaces — position, velocity, and effort controllers are all supported. This tight ROS 2 integration is a primary reason Dynamixel appears in virtually every academic and research robotics lab: tutorials, courses, and textbooks throughout the ROS community assume Dynamixel hardware.

A key limitation of Dynamixel actuators is bandwidth. The TTL/RS-485 bus protocol limits control loop rates to roughly 50–200 Hz in practice for multi-joint systems — significantly below the >500 Hz streaming rates achievable with EtherCAT-based motor controllers like Synapticon or Copley. This makes Dynamixel suitable for research, education, slow manipulation, and compliant control, but not for high-speed precision manufacturing applications.

## Notable Developments

- **Ongoing:** Dynamixel XW series adds waterproofing (IP68/IP54) for field robot and underwater applications.
- **Ongoing:** TurtleBot4 (next-gen TurtleBot3 successor with iRobot Create 3 base) maintains Dynamixel ecosystem integration via ROS 2.
- **2019:** ROBOTIS OP3 humanoid released with 20 Dynamixel XM430-W350 actuators; used extensively in RoboCup Humanoid League.
- **2019:** TurtleBot3 (with Open Robotics) becomes the most popular ROS 2 educational robot platform worldwide.
- **1999:** Robotis founded in Seoul.

## Key People

Robotis executive leadership is not widely profiled in English-language sources. The company operates as a private Korean corporation and does not routinely publish leadership profiles in English.

### People — Last Reviewed: 2026-06-23

## Supply Chain Position

Robotis operates at the **Integrated Actuator Module** layer (Layer 6 in the actuators supply chain), one level above discrete motors and gearboxes. A Dynamixel unit replaces what would otherwise require four separate components: motor, gearbox, encoder, and driver electronics.

**⚑ Rare earth dependency:** Dynamixel motors use NdFeB permanent magnets for the BLDC and DC motor variants; rare earth supply chain dependency applies.

**⚑ Shared ecosystem with Open Robotics:** Robotis and Open Robotics (ROS maintainer) have a close co-development relationship via TurtleBot. Changes to ROS 2 are routinely tested against Dynamixel hardware, giving Dynamixel a privileged position in the ROS 2 reference ecosystem.

## Claim Verification

### Claim: Dynamixel is the most widely used integrated actuator in robotics research
**Status:** Partially verified

**Supporting sources:**
- Dynamixel appears in the ROS 2 official tutorials, Open Robotics TurtleBot3 reference design, and ROBOTIS OP3 humanoid reference design — the three most-referenced ROS 2 hardware platforms in academic robotics
- Search of academic robotics papers on Google Scholar confirms frequent citation of Dynamixel hardware

**Refuting / questioning sources:**
- No market share data for research actuator market is publicly available; "most widely used" is a qualitative claim

**Summary:** Dynamixel's ubiquity in ROS 2 tutorials, reference robots, and academic publications is well-established; quantitative market share data is unavailable.

## Sources

- [Robotis US website](https://www.robotis.us/)
- [Dynamixel e-Manual — ROS Package](https://emanual.robotis.com/docs/en/platform/op2/ros_package/)
- [Dynamixel Workbench GitHub](https://github.com/ROBOTIS-GIT/dynamixel-workbench)
- [TurtleBot3 with Dynamixel — ROBOTIS](https://www.robotis.us/turtlebot-3/)
