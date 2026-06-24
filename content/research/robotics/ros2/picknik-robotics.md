---
title: "PickNik Robotics"
date: 2026-06-23
lastmod: 2026-06-23
draft: false
description: "Boulder, CO robotics software company; primary commercial maintainer of MoveIt 2 and MoveIt Pro; publishes the largest public ROS 2 hardware compatibility database; provides ROS 2 driver development services and application development for manipulation robotics."
tags: ["robotics", "ros2", "software", "manipulation", "us"]
categories: ["company"]
research_area: "robotics/ros2"
source_urls:
  - "https://picknik.ai/"
  - "https://picknik.ai/hardware-ecosystem/"
  - "https://picknik.ai/history"
  - "https://picknik.ai/pro"
last_reviewed: 2026-06-23
stale_after_days: 90
related: []
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

PickNik Robotics, headquartered in Boulder, Colorado, is a robotics software company founded in 2015. It is the primary commercial maintainer of MoveIt — the dominant open-source motion planning framework for ROS 2 robot manipulation — and sells MoveIt Pro, a commercial platform layering behavior tree-based autonomy, AI-driven perception, simulation, and teleoperation tooling on top of the open-source stack. PickNik maintains what is widely considered the most comprehensive public database of ROS 2-compatible hardware. The company provides ROS 2 driver development services to hardware vendors and application development services for manipulation robotics deployments across industrial, space, medical, and warehouse verticals.

## Key Facts

- **Founded:** 2015
- **HQ:** Boulder, Colorado, USA
- **Type:** Private
- **Core products:** MoveIt Pro (commercial manipulation platform); MoveIt Pro Core (C++/Python real-time manipulation libraries with minimum dependencies); ROS 2 hardware compatibility database
- **Key services:** ROS 2 driver development; application development; digital twin prototyping; training courses; solution studies
- **Key verticals:** Space robotics; complex manufacturing; warehouse & fulfillment; commercial cleaning
- **Open source contributions:** Primary maintainer of MoveIt 2 (ROS 2 motion planning); significant contributor to ros2_control, ros_industrial, and related ROS 2 packages
- **Hardware compatibility database:** Tracks 100+ hardware brands across 17 categories with ROS 2 driver quality scores

## What It Is / How It Works

PickNik's core product, MoveIt Pro, is a commercial software platform for building and deploying advanced robot manipulation applications. It layers several capabilities on top of ROS 2 and MoveIt 2:

**Runtime Autonomy:** ML-based perception and grasping models; real-time motion planners and controllers with collision and force awareness; end-to-end ML toolchain for training generalizable AI models; mobile base navigation for AMRs and humanoids.

**User Interfaces:** A behavior tree builder for constructing reactive robot logic; debugging toolchains with runtime blackboard inspection; a robot visualizer; and a four-mode teleoperation suite for human-in-the-loop operation.

**Simulation:** AI training simulation environment for synthetic data generation; offline developer simulation for application development without physical hardware.

MoveIt Pro Core is a separately licensed, minimum-dependency C++ and Python library set intended for customers who want the real-time planning and control capabilities without the full Pro platform. This tiered product architecture allows PickNik to address both embedded/constrained deployments and full autonomy applications.

PickNik's ROS 2 hardware ecosystem database is a publicly accessible resource that rates hardware on two axes: MoveIt Pro compatibility (Gold Integration = PickNik-tested; Basic Integration = third-party-tested) and ROS 2 Driver Quality Score (Great = >500 Hz streaming; Average = <25 Hz trajectory; Poor = <25 Hz single-point). As of June 2026, the database tracks 17 hardware categories covering robot arms, grippers, depth sensors, AGVs, AMRs, force-torque sensors, motor controllers, actuators, and more.

The company's position as the primary MoveIt maintainer creates a significant competitive moat: hardware vendors whose robots have Gold MoveIt Pro integration gain access to PickNik's customer base, creating incentives for vendors to work with PickNik for driver development. This network effect between hardware vendors and software customers reinforces PickNik's position at the center of the ROS 2 manipulation ecosystem.

## Notable Developments

- **2026 (ongoing):** ROS 2 hardware compatibility database expanded to 17 categories, 100+ hardware brands; used as the de facto industry reference for ROS 2 hardware selection.
- **2025:** MoveIt Pro Core launched as a separate product; enables minimum-dependency real-time manipulation library deployment distinct from full MoveIt Pro platform.
- **2024–2025:** Expanded space robotics vertical; Motiv Space Systems (xLink space manipulator) listed as Gold MoveIt Pro integration partner.
- **2023 onward:** Growing focus on humanoid robot application development as manipulator + mobile base systems multiply.
- **2015:** Founded in Boulder, CO. Initially focused on consulting and open-source MoveIt contributions before developing commercial product layer.

## Key People

### Dave Coleman — Co-Founder and CEO
- **LinkedIn:** Not confirmed — LinkedIn profile not publicly accessible
- **Notes:** Dave Coleman is the primary author and original creator of MoveIt 2 and has been the driving force behind the commercialization of MoveIt into the PickNik product suite. Widely cited in the ROS 2 community. Co-founded PickNik after contributing to MoveIt while at NIST and during his graduate studies.
- **Education:** University of Colorado Boulder (PhD, Mechanical Engineering, robotics focus)

### People — Last Reviewed: 2026-06-23

## Supply Chain Position

PickNik operates at the **Software/AI Layer** of the robotics value chain — it does not manufacture hardware but provides the motion planning and autonomy software layer that hardware integrates into. Its position as primary MoveIt 2 maintainer gives it unique leverage: changes to the open-source framework are influenced by PickNik's priorities and customer requirements, creating a combination of commercial and community influence that is unusual in robotics software.

**Value chain role:** Software platform provider between ROS 2 hardware drivers (maintained by vendors or community) and end-user applications (warehouse, manufacturing, space).

## Claim Verification

### Claim: PickNik is the primary commercial maintainer of MoveIt
**Status:** Verified (by inspection of MoveIt GitHub commit history and maintainers list)

**Supporting sources:**
- [MoveIt GitHub repository](https://github.com/moveit/moveit2) — PickNik engineers are the most active committers and listed maintainers
- [PickNik history page](https://picknik.ai/history) — Company self-describes as "the company behind MoveIt"
- [ROS 2 community references](https://picknik.ai/moveit) — MoveIt brand is strongly associated with PickNik in public documentation

**Summary:** PickNik's role as primary MoveIt 2 maintainer is well-established and verifiable from open-source commit history and community documentation.

## Sources

- [PickNik Robotics Homepage](https://picknik.ai/)
- [ROS 2 Compatible Hardware Database — PickNik](https://picknik.ai/hardware-ecosystem/)
- [PickNik History](https://picknik.ai/history)
- [MoveIt Pro Product Page](https://picknik.ai/pro)
- [MoveIt Pro Core Product Page](https://picknik.ai/moveit-pro-core)
- [PickNik Services](https://picknik.ai/services)
