---
title: "Synapticon"
date: 2026-06-23
lastmod: 2026-06-23
draft: false
description: "Weinstadt, Germany EtherCAT servo drive and integrated actuator manufacturer; SOMANET product line integrates motor controller, safety, and communications into compact modules; vendor-supported ROS 2 driver (ros2_control); targeted at humanoid robots and high-performance manipulation."
research_area: "robotics/actuators"
source_urls:
  - "https://catalog.synapticon.com"
  - "https://github.com/synapticon/synapticon_ros2_control"
last_reviewed: 2026-06-23
stale_after_days: 180
related: []
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Synapticon, headquartered in Weinstadt, Baden-Württemberg, Germany, designs and manufactures the SOMANET line of EtherCAT servo drives and integrated actuator modules for demanding robotics applications. Unlike discrete motor controllers, SOMANET drives integrate motor power electronics, safety architecture, EtherCAT communications, and sensor interfaces into compact cylindrical or board-level modules optimized for robot joint integration. Synapticon's ROS 2 driver (synapticon_ros2_control) uses the ros2_control framework, providing high-bandwidth streaming control at EtherCAT bus rates (typically 1–4 kHz loop closure). The company appears on PickNik's ROS 2 hardware compatibility list in both the Motor Controllers and Motors/Actuators categories, with a community-supported driver.

## Key Facts

- **Founded:** ~2012 (as a spin-off from academic robotics research in Germany)
- **HQ:** Weinstadt, Baden-Württemberg, Germany
- **Type:** Private
- **Key products:** SOMANET Node series (EtherCAT servo drives, compact form factor); SOMANET integrated actuator modules (motor + drive + encoder in one unit)
- **Communications:** EtherCAT (IEC 61158); supports CiA 402 CANopen over EtherCAT (CoE) device profile
- **Safety:** IEC 61800-5-2 functional safety (STO, SS1, SS2, SLS); supports robot safety functions
- **ROS 2 driver:** Community-supported (GitHub: synapticon/synapticon_ros2_control)
- **PickNik compatibility:** Listed in Motor Controllers and Motors/Actuators categories; community-supported driver

## What It Is / How It Works

Synapticon's SOMANET product family bridges the gap between discrete servo drives (standalone motor controllers connected to external motors) and fully integrated actuator modules (everything in one unit). The SOMANET Node is a compact servo drive that mounts directly to or near a motor, handling power conversion, current control, position/velocity/torque loop closure, and EtherCAT bus communications — all at real-time rates up to 4 kHz. The compact cylindrical form factor is specifically designed to fit within robot joint envelopes without external control cabinets.

EtherCAT is the key differentiator versus bus-based systems like Dynamixel. EtherCAT achieves sub-microsecond cycle time jitter and supports hundreds of axes on a single bus at 1 kHz, enabling the high-bandwidth streaming required for force-compliant manipulation, visual servoing, and impedance control in advanced manipulation robots. The PickNik rating system classifies EtherCAT-based controllers as "Great" (>500 Hz) — the highest driver quality tier — because they enable the most sophisticated manipulation applications.

The ros2_control integration exposes Synapticon drives as standard ROS 2 hardware interfaces (joint_state_broadcaster, effort_controller, joint_trajectory_controller), making them compatible with MoveIt 2 and PickNik's MoveIt Pro without custom driver development.

## Notable Developments

- **2024–2025:** Growing adoption in humanoid robot development programs as developers seek compact, high-bandwidth joint controllers for torque-controlled manipulation.
- **Ongoing:** SOMANET product line expanded to support higher current ratings and more compact form factors for humanoid joint integration.
- **~2019:** synapticon_ros2_control driver first published; community-maintained with vendor engineering participation.

### People — Last Reviewed: 2026-06-23

## Supply Chain Position

Synapticon operates at the **Motor Controller** and **Integrated Actuator Module** layer (Layers 4–6 in the actuators supply chain). SOMANET drives are typically purchased by robot OEMs integrating third-party motors (Maxon, Kollmorgen, commodity BLDC) with Synapticon control electronics.

**⚑ Competing with Copley, Elmo, Galil:** Synapticon competes in the precision servo drive market with Copley Controls (US, PickNik Gold integration), Elmo Motion Control (Israel), and Galil Motion Control (US). Copley holds a Gold PickNik integration advantage; Synapticon differentiates on integrated form factor.

## Claim Verification

### Claim: Synapticon SOMANET supports >500 Hz EtherCAT control loops
**Status:** Partially verified

**Supporting sources:**
- EtherCAT protocol specification supports up to 1 kHz (1 ms) and faster cycle times in hardware; SOMANET product documentation references 4 kHz loop closure
- PickNik classifies EtherCAT-based controllers as "Great" driver quality, consistent with >500 Hz capability

**Refuting / questioning sources:**
- Actual achievable cycle rates in a ROS 2 application depend on host processor real-time configuration; the hardware supports kHz rates but ROS 2 application overhead may limit practical rates

**Summary:** EtherCAT hardware capability for >500 Hz is established; ROS 2 application performance depends on implementation.

## Sources

- [Synapticon Product Catalog](https://catalog.synapticon.com)
- [synapticon_ros2_control — GitHub](https://github.com/synapticon/synapticon_ros2_control)
- [PickNik ROS 2 Hardware Ecosystem (Motor Controllers)](https://picknik.ai/hardware-ecosystem/#motor-controllers)
