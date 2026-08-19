---
title: "Topology-Aware Multi-Camera Tracking (JYe9)"
date: 2026-08-15
lastmod: 2026-08-15
draft: false
description: "Open-source cross-camera vehicle tracking system using YOLO + ByteTrack per camera and a topology-aware spatiotemporal handover framework for consistent global IDs across overlapping UAV camera views — an adjacent, adaptable reference architecture rather than a drone-detection tool itself."
research_area: "drone-detection/open-source"
source_urls:
  - "https://github.com/JYe9/multi-camera-multi-vehicle-tracking-system"
last_reviewed: 2026-08-15
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

This project solves the **inverse** of this section's usual problem: it tracks ground vehicles across multiple UAV-mounted camera feeds, rather than tracking drones from fixed ground cameras. It's included here as an adjacent, adaptable reference architecture — the core technique (assigning one consistent identity to a moving target as it crosses between camera fields of view, using geometric/topological reasoning rather than pure visual re-identification) is the same cross-camera correlation problem that a fixed multi-camera drone-detection array has to solve. Each of three UAV video sources runs YOLO detection and ByteTrack per-camera tracking; a "topology-aware spatiotemporal handover" framework then assigns global IDs to vehicles as they move between camera overlap regions, described in an associated paper submitted to ICUAS 2026.

## Key Facts

- **Author:** JYe9 (GitHub)
- **Type:** Open-source software + associated paper — cross-camera vehicle tracking (UAV-sourced video, not drone detection itself)
- **License:** Academic and Non-Commercial Research License — **not** permissively licensed; commercial/production reuse would require separate arrangement
- **Status:** 33 stars, 0 forks as of this review
- **Detection/tracking:** Ultralytics YOLO (custom `3UAVs.pt` model) + ByteTrack via the Supervision library, per camera
- **Cross-camera matching:** Global ID correlation within defined camera-overlap regions
- **Associated paper:** "A Topology-Aware Spatiotemporal Handover Framework for Continuous Multi-UAV Tracking" — per the repository's own citation, submitted to ICUAS 2026 (arXiv:2605.15779 per the repo; this entry could not independently confirm the arXiv listing's content — the abstract page did not return readable text at time of review)

## How It Works

The system processes video from three UAV camera sources in parallel. Each stream runs an Ultralytics YOLO model fine-tuned for vehicle detection, feeding ByteTrack (via the Supervision library) for within-camera tracking. As a tracked vehicle moves from one camera's field of view into an overlapping neighbor's, the topology-aware handover framework — using known geometric relationships between camera coverage areas rather than relying solely on visual appearance matching — reassigns the same global ID rather than spawning a new track. Output includes per-camera annotated video, plus CSV metadata with per-vehicle speed (via pixel-to-meter calibration) and direction, frame index, global ID, camera ID, and status.

## Why This Is Here (Not a Drone-Detection Tool)

This is UAV-as-sensor, not UAV-as-target — the opposite configuration from the fixed-camera-array C-UAS use case this section otherwise documents. It's included because the specific sub-problem it solves — persistent identity across overlapping camera fields of view without continuous appearance-based re-identification — is directly relevant to any multi-camera drone-detection deployment, including [TRAMIS]({{< relref "../detection-methods/tramis.md" >}})'s own cross-camera track correlation (which uses timestamp synchronization plus heading-closeness rather than a topology/handover model) and the general [multi-sensor fusion]({{< relref "../detection-methods/multi-sensor-fusion.md" >}}) problem this section prioritizes. Treat it as a technique/architecture reference, not a candidate C-UAS product.

## Related / Further Reading (Not Independently Verified)

The following were flagged as adjacent references but could not be independently confirmed for this entry — treat as pointers for further research, not verified facts:

- **OpenVINO Multi-Camera Multi-Target Tracking demo** ([openvinotoolkit/open_model_zoo](https://github.com/openvinotoolkit/open_model_zoo/tree/master/demos/multi_camera_multi_target_tracking_demo/python)) — reported to combine detection with re-identification embeddings for cross-camera association (person/vehicle-oriented, described as a reusable architecture pattern). Direct fetch of this repository was blocked (robots.txt) for this entry; current status, license, and maintenance activity are unconfirmed.
- **Kinematics-based multi-camera aerial-target re-identification research** (e.g., work on "Multiple Aerial Targets Re-Identification by 2D- and 3D-Kinematics-Based Matching") — described as graph-matching approaches to cross-camera re-ID requiring little or no appearance-based training data, conceptually adjacent to the trajectory/kinematics-based (not appearance-based) approach used by [TRAMIS]({{< relref "../detection-methods/tramis.md" >}}). Specific paper(s) not identified/verified for this entry.

## Limitations

- **Non-commercial license:** The "Academic and Non-Commercial Research License" is a real constraint — this cannot be dropped into a commercial C-UAS product without separate licensing, unlike the MIT/permissively-licensed projects elsewhere in this section.
- **Not drone detection:** Targets are ground vehicles; sensors are airborne. Applying the technique to the drone-detection use case (fixed ground cameras, airborne targets) would require nontrivial adaptation, not a drop-in swap.
- **No published cross-camera accuracy metrics** (ID-switch rate, handover accuracy) in the repository as of this review — the associated paper (unconfirmed access) may contain these.

## Sources

- [multi-camera-multi-vehicle-tracking-system — GitHub](https://github.com/JYe9/multi-camera-multi-vehicle-tracking-system)
