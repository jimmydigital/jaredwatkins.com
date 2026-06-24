---
title: "Stereolabs (ZED Cameras)"
date: 2026-06-23
lastmod: 2026-06-23
draft: false
description: "Paris/San Francisco stereo depth camera company; ZED 2, ZED X, and ZED Mini cameras provide active stereo vision with on-camera IMU; Gold MoveIt Pro integration; widely used in robotics, AMR, and drone applications with strong NVIDIA Jetson compatibility."
tags: ["robotics", "sensor", "depth-camera", "stereo-vision", "eu", "ros2"]
categories: ["company"]
research_area: "robotics/sensors"
source_urls:
  - "https://www.stereolabs.com/"
  - "https://github.com/stereolabs/zed-ros2-wrapper"
last_reviewed: 2026-06-23
stale_after_days: 180
related: []
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Stereolabs, headquartered in Paris with a US office in San Francisco, manufactures the ZED series of stereo depth cameras — widely used in robotics, AMR, drone, and augmented reality applications. ZED cameras use active stereo vision (infrared projector + two wide-baseline cameras) to generate dense depth maps and 6-DoF positional tracking in real time without external infrastructure. The company has a strong NVIDIA partnership, with ZED cameras natively supported in the Isaac ROS ecosystem and optimized for NVIDIA Jetson platforms. Stereolabs holds a Gold MoveIt Pro integration and maintains a vendor-supported ROS 2 driver.

## Key Facts

- **Founded:** 2015
- **HQ:** Paris, France (US office: San Francisco, CA)
- **Type:** Private (Series B as of last known funding)
- **Key products:** ZED 2 (wide-FoV stereo, 120° diagonal); ZED X (industrial/outdoor ruggedized); ZED Mini (compact, head-mounted AR); ZED 2i (IP66-rated industrial)
- **Technology:** Active stereo vision; on-board IMU; real-time 6-DoF positional tracking; neural depth via GPU; up to 15m depth range; 30–100 fps depending on resolution
- **ROS 2 driver:** Vendor-supported (github.com/stereolabs/zed-ros2-wrapper)
- **PickNik compatibility:** Gold MoveIt Pro integration
- **NVIDIA partnership:** ZED cameras are listed in the NVIDIA Isaac ROS NGC catalog; ZED SDK is CUDA-accelerated for Jetson AGX Orin

## What It Is / How It Works

Stereolabs ZED cameras operate on the principle of stereo vision: two cameras separated by a known baseline observe the same scene, and the horizontal displacement (disparity) of matching features between left and right images encodes depth. An on-camera infrared projector adds passive texture to featureless surfaces (walls, floors) that would otherwise confound stereo matching. The ZED SDK handles all disparity computation on the host GPU (or Jetson GPU), producing color point clouds, depth maps, and a fused 6-DoF pose estimate via visual-inertial odometry.

The on-board IMU integration is significant for robotics: combined with camera tracking, ZED cameras enable map-less visual-inertial odometry — a robot can track its own position and orientation without external SLAM infrastructure, using only the camera and IMU data fused in the ZED SDK. This is useful for AMRs and drones operating in environments where LiDAR-based SLAM is not deployed.

The ZED X introduced industrial-grade ruggedization (IP66, wider operating temperature) targeting factory floor and outdoor applications. The ZED 2i is an IP66-rated variant of the ZED 2 for similar environments.

The Gold MoveIt Pro integration means PickNik has validated ZED cameras in manipulation perception pipelines — typically used for workspace monitoring, human detection, and wide-area scene understanding rather than the high-accuracy close-range bin picking where Zivid excels. The use cases are complementary: Zivid for precise part location; ZED for broad workspace awareness and mobile base navigation support.

## Notable Developments

- **2023–2024:** ZED X released with industrial ruggedization; targets factory automation and outdoor robotics.
- **2023:** ZED SDK listed in NVIDIA Isaac ROS NGC catalog; Stereolabs and NVIDIA publish joint application notes for ZED + Jetson AGX Orin integration.
- **2022:** Series B funding; amount not publicly disclosed.
- **2015:** Company founded in Paris.

### People — Last Reviewed: 2026-06-23

## Supply Chain Position

Stereolabs operates at the **Complete Sensor System** layer (Level 4 in the sensors supply chain). ZED cameras use Sony CMOS image sensors and standard MEMS IMU components; the ZED SDK software is the primary differentiated value layer.

**⚑ Shared sensor platform with Intel RealSense:** As Intel RealSense exits the market, Stereolabs ZED cameras are a primary alternative. Several ROS 2 tutorials and applications that previously referenced RealSense have been updated to ZED.

**⚑ NVIDIA dependency:** The ZED SDK requires CUDA-capable GPU hardware for neural depth computation. On Jetson (NVIDIA), the integration is tight and optimized; on non-NVIDIA platforms (AMD GPU, ARM CPU without CUDA), the ZED SDK does not provide GPU acceleration, limiting performance.

## Claim Verification

### Claim: ZED cameras support 6-DoF positional tracking without external infrastructure
**Status:** Verified

**Supporting sources:**
- [Stereolabs ZED SDK documentation](https://www.stereolabs.com/docs/) — positional tracking is a documented SDK feature
- Multiple published academic papers and robotics tutorials confirm ZED visual-inertial odometry capability without external markers or SLAM maps

**Summary:** ZED SDK positional tracking without external infrastructure is a documented and widely demonstrated capability.

## Sources

- [Stereolabs Homepage](https://www.stereolabs.com/)
- [ZED ROS 2 Wrapper — GitHub](https://github.com/stereolabs/zed-ros2-wrapper)
- [PickNik ROS 2 Hardware Ecosystem (Depth Sensors)](https://picknik.ai/hardware-ecosystem/#depth-sensors)
