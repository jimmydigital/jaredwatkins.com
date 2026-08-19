---
title: "Stereo Drone Tracker"
date: 2026-08-15
lastmod: 2026-08-15
draft: false
description: "Open-source real-time stereo-camera (2× Sony IMX477) drone detection, 3D triangulation, and Kalman/Hungarian multi-target tracking with occlusion re-identification on a Jetson Orin Nano; framed as a ~$550 alternative to $95K+ commercial systems."
research_area: "drone-detection/open-source"
source_urls:
  - "https://github.com/Capstone-16/Stereo-Drone-Tracker"
last_reviewed: 2026-08-15
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Stereo Drone Tracker is an open-source, real-time stereo-vision drone detection and 3D localization pipeline: two Sony IMX477 CSI cameras in a fixed-baseline stereo rig feed a YOLOv11s detector (exported to TensorRT) running on an NVIDIA Jetson Orin Nano. Detections are paired across the two camera views using epipolar geometry, triangulated into 3D positions, and tracked over time with a Hungarian-algorithm assignment step plus a Kalman filter — including a "zombie re-identification" mechanism that extrapolates a track through brief occlusions so an object's ID survives short dropouts. The authors (a university capstone team) frame it explicitly as a low-cost, passive, RF-silent alternative to commercial drone tracking systems they price above $95,000, with a claimed hardware bill of materials around $550.

## Key Facts

- **Author/org:** Capstone-16 (GitHub); contributors Khaled Ghanem, Eralp Erol, Halit Özkaya, Mustafa Ecevit
- **Type:** Open-source software project — real-time stereo drone detection, 3D localization, and tracking
- **License:** MIT
- **Status:** Active but early-stage — 0 stars, 1 fork, 6 commits on `main` as of this review; small/young project
- **Hardware target:** NVIDIA Jetson Orin Nano (8GB) + 2× Sony IMX477 CSI cameras
- **Detection model:** YOLOv11s, TensorRT-accelerated

## How It Works

The pipeline runs a fine-tuned YOLOv11s model (TensorRT engine) on each camera's video feed via a GStreamer capture pipeline for synchronization. Detected bounding boxes from the two cameras are matched to each other using epipolar-geometry constraints, then triangulated (via OpenCV/NumPy/SciPy geometry) into a 3D position relative to the stereo rig. A Hungarian-algorithm assignment step matches new detections to existing tracks frame-to-frame, and a Kalman filter smooths position/velocity estimates and predicts forward through gaps. The "zombie re-identification" feature specifically addresses occlusion: rather than dropping an ID the moment detection fails, the system extrapolates the predicted trajectory and re-associates the same ID once detection resumes, reported to recover within 2 frames.

Deployment requires a one-time stereo calibration step (20–30 checkerboard image pairs, validated to RMS reprojection error under 1.0 px and a focal-length ratio within [0.5, 2.0]) before running the main tracking script. Output is a timestamped CSV log of per-frame 3D position, velocity, and detection confidence.

## Performance (Author-Reported)

- Pipeline speed: 27 FPS
- YOLO inference latency: 30 ms (batch=2)
- End-to-end latency: 60 ms (capture to display)
- 3D position error at 20 m range: ±5%
- Detection confidence: ~80%
- ID recovery after occlusion: ≤2 frames

## Claim Verification

### Claim: 27 FPS pipeline, 60 ms end-to-end latency, ±5% 3D position error at 20 m, ~$550 total hardware cost vs. $95K+ commercial systems
**Status:** Unverified.
**Supporting sources:** Project's own repository documentation only.
**Refuting/questioning sources:** None found; no independent benchmark, field test, or third-party review located.
**Summary:** These are self-reported figures from what appears to be a university capstone project (very low adoption signal — 0 stars, 6 commits at time of review). Plausible as a bench-test result at short range, but unreplicated; the $550-vs-$95K framing is a marketing-style comparison against unnamed commercial systems and should not be read as an apples-to-apples cost comparison without knowing what capability tier those systems represent.

## Limitations

- **Early-stage project:** Very low community adoption signal (0 stars, 1 fork, 6 commits) as of this review — limited independent code review or field validation exposure.
- **Calibration-dependent:** 3D accuracy depends on stereo calibration quality; recalibration likely needed per physical deployment/rig.
- **Fixed short baseline:** A two-camera stereo rig's 3D accuracy degrades with range; the reported ±5% figure is specifically at 20 m, and there's no data on longer-range performance (contrast with this section's [multi-view triangulation]({{< relref "../detection-methods/tramis.md" >}}) approaches that use wider, more flexible camera spacing).
- **No drone-vs-bird classification:** This is a detection + 3D tracking pipeline for whatever the YOLO model is trained to recognize — it does not include the kind of trajectory-based species/type discrimination documented elsewhere in this section (e.g., [TRAMIS]({{< relref "../detection-methods/tramis.md" >}})).

## Sources

- [Stereo-Drone-Tracker — GitHub](https://github.com/Capstone-16/Stereo-Drone-Tracker)
