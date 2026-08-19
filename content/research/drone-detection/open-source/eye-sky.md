---
title: "eye_sky"
date: 2026-08-15
lastmod: 2026-08-15
draft: false
description: "Open-source Python multi-object, multi-camera drone tracker (OpenCV-based) with binocular 3D triangulation and optical-flow camera stabilization; a Python port/extension of the MATLAB SPOTIT3D system, backed by two peer-reviewed papers on continuous cross-camera drone tracking."
research_area: "drone-detection/open-source"
source_urls:
  - "https://github.com/Yi-Jiahe/eye_sky"
last_reviewed: 2026-08-15
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

eye_sky is an open-source Python system for camera-based multi-object tracking across multiple camera feeds, with a binocular camera package supporting 3D triangulation. It originated as a Python port and extension of SPOTIT3D, a MATLAB system developed by Dr. Sutthiphong Srigrarom, adding filtering, visualization, and additional triangulation capability. Two peer-reviewed papers grew out of this line of work: one on continuous drone tracking through camera-to-camera "frame-stitching" as an object crosses between fields of view, and one on binocular camera systems for multi-drone detection specifically.

## Key Facts

- **Author:** Yi-Jiahe (GitHub); builds on SPOTIT3D by Dr. Sutthiphong Srigrarom (originally MATLAB)
- **Type:** Open-source software — multi-camera, multi-object tracking with 3D triangulation
- **Status:** Small/active — 3 stars, 0 forks as of this review
- **Core stack:** OpenCV, NumPy, FilterPy, SciPy, Matplotlib
- **Associated publications:** Yi, Chew & Srigrarom (2021) on continuous drone tracking via frame-stitching across camera transitions; Yi & Srigrarom (2020) on binocular camera systems for multi-drone detection

## How It Works

The system combines background subtraction and real-time detection with an object-tracking pipeline that handles video I/O and image transformations for multiple simultaneous camera feeds. An optical-flow-based camera stabilization module compensates for camera motion/jitter before tracking. The "Binocular Camera" package pairs two camera views to perform 3D triangulation, directly analogous in goal (if not implementation) to this section's [Stereo Drone Tracker]({{< relref "stereo-drone-tracker.md" >}}). The project structure includes separate modules for real-time multi-camera tracking, binocular 3D triangulation, multi-view indoor tracking, comparisons of different object trackers, and integration scripts for DJI Tello drones (likely used as a convenient, controllable test target).

## Relevance to This Section

Dr. Sutthiphong Srigrarom's broader body of work on trajectory-based drone-vs-bird classification (motion-characteristic-based discrimination rather than appearance-based) is directly in the same research lineage documented in this section's [TRAMIS]({{< relref "../detection-methods/tramis.md" >}}) entry, which cites a related Srigrarom paper ("Drone versus bird flights: Classification by trajectories characterization") among its references. eye_sky and TRAMIS independently arrive at a similar architectural thesis — multi-camera, trajectory/track-based processing rather than per-frame image classification — for the same underlying problem.

## Limitations

- **Small project, thin documentation on current state:** No confirmed license, last-commit date, or contributor count found in available material — verify directly on GitHub before relying on or building against it.
- **No consolidated performance metrics** in the main repository; benchmark/accuracy figures would need to be sourced from the associated Yi/Chew/Srigrarom papers rather than the code repo itself.
- **Research-grade code:** Like most projects in this section's open-source list, this is more likely to need adaptation (calibration, synchronization, outdoor robustness) than to be production-deployable as-is.

## Sources

- [eye_sky — GitHub](https://github.com/Yi-Jiahe/eye_sky)
