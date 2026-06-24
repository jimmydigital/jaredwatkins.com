---
title: "Zivid"
date: 2026-06-23
lastmod: 2026-06-23
draft: false
description: "Oslo, Norway 3D machine vision camera manufacturer; Zivid Two and Zivid 2+ structured-light cameras provide high-accuracy point clouds for bin picking and assembly robotics; Gold MoveIt Pro integration; vendor-supported ROS 2 driver."
tags: ["robotics", "sensor", "depth-camera", "3d-vision", "eu", "ros2"]
categories: ["company"]
research_area: "robotics/sensors"
source_urls:
  - "https://www.zivid.com/"
  - "https://github.com/zivid/zivid-ros"
last_reviewed: 2026-06-23
stale_after_days: 180
related: []
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Zivid, headquartered in Oslo, Norway, manufactures structured-light 3D machine vision cameras targeted at industrial robot manipulation applications — specifically bin picking, kitting, assembly verification, and quality inspection. The Zivid Two and Zivid 2+ cameras use multi-pattern fringe projection structured light to capture high-fidelity color point clouds with sub-millimeter accuracy, enabling robots to precisely locate and pick randomly oriented parts from bins. Zivid holds a Gold MoveIt Pro integration from PickNik, making it one of the highest-rated depth sensors in the ROS 2 manipulation ecosystem, and maintains a vendor-supported ROS 2 driver.

## Key Facts

- **Founded:** 2015
- **HQ:** Oslo, Norway
- **Type:** Private
- **Key products:** Zivid Two (high-resolution structured-light 3D camera); Zivid 2+ (updated generation with improved throughput and accuracy)
- **Technology:** Multi-pattern fringe projection structured light; captures color (RGB) + depth point clouds; sub-millimeter accuracy at typical industrial distances (0.3–1.2 m)
- **ROS 2 driver:** Vendor-supported (github.com/zivid/zivid-ros)
- **PickNik compatibility:** Gold MoveIt Pro integration; vendor-supported ROS 2 driver
- **Primary market:** Industrial robot manipulation (bin picking, kitting, assembly)

## What It Is / How It Works

Zivid cameras project structured light patterns (sequences of sinusoidal fringe patterns) onto the scene and capture the resulting deformation with a high-resolution RGB camera. By analyzing how the fringe patterns deform across the scene, the camera computes a dense, calibrated point cloud. The fringe projection approach achieves higher accuracy than time-of-flight cameras for structured industrial objects at close range, and higher throughput than photogrammetric scanning. Zivid's specific differentiation is the combination of high point cloud density, color texture capture, and industrial-grade environmental robustness (temperature stability, ambient light immunity).

For bin picking applications — where a robot arm must pick randomly oriented metal or plastic parts from a bin — Zivid cameras are used with object detection and pose estimation software to determine part position and orientation. The Gold MoveIt Pro integration means PickNik has validated that Zivid cameras integrate cleanly with MoveIt Pro's perception pipeline for grasp generation and planning.

The Zivid 2+ generation (released ~2023–2024) improves acquisition speed (important for high-throughput manufacturing lines) and introduces improved robustness for shiny metallic surfaces, which are notoriously difficult for structured light due to specular reflections.

## Notable Developments

- **~2023–2024:** Zivid 2+ released; improved throughput and metallic surface handling.
- **Ongoing:** Gold MoveIt Pro integration maintained with PickNik; Zivid appears in PickNik's bin picking and scan-pick-place application guides.
- **2015:** Company founded in Oslo.

### People — Last Reviewed: 2026-06-23

## Supply Chain Position

Zivid operates at the **Complete Sensor System** layer — producing complete 3D machine vision cameras sold to robot integrators and OEMs for manipulation applications.

**⚑ Competing with Intel RealSense (retreating), Photoneo, Mechmind:** Zivid competes with Photoneo (Slovakia), Mechmind (China), and the declining Intel RealSense line. Photoneo uses a different structured light modality (single-shot HDR); Mechmind is Chinese and faces US procurement scrutiny; Zivid's Norwegian origin has no current US export control concerns.

## Claim Verification

### Claim: Zivid cameras provide sub-millimeter accuracy
**Status:** Partially verified

**Supporting sources:**
- [Zivid product documentation](https://www.zivid.com/) — company-stated accuracy specifications
- Gold MoveIt Pro integration implies PickNik has validated performance in manipulation contexts

**Refuting / questioning sources:**
- Structured light accuracy degrades significantly with shiny, dark, or transparent surfaces; the Zivid 2+ addresses some of these, but no independent third-party accuracy benchmarks across surface types were confirmed in this session

**Summary:** Sub-millimeter accuracy claim is from manufacturer documentation; performance is surface-type and distance dependent.

## Sources

- [Zivid Homepage](https://www.zivid.com/)
- [Zivid ROS 2 Driver — GitHub](https://github.com/zivid/zivid-ros)
- [PickNik ROS 2 Hardware Ecosystem (Depth Sensors)](https://picknik.ai/hardware-ecosystem/#depth-sensors)
