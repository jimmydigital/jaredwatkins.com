---
title: "Drone Tracking Datasets (CenekAlbl)"
date: 2026-08-15
lastmod: 2026-08-15
draft: false
description: "Open, RTK-ground-truthed multi-view drone tracking dataset collection (5 sequences, 4–7 consumer cameras each) for developing and benchmarking multi-camera 3D drone trajectory estimation; paired with an unsynchronized-camera 3D reconstruction pipeline (mvus)."
research_area: "drone-detection/open-source"
source_urls:
  - "https://github.com/CenekAlbl/drone-tracking-datasets"
  - "https://github.com/CenekAlbl/mvus"
  - "https://arxiv.org/abs/2003.04784"
last_reviewed: 2026-08-15
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Drone Tracking Datasets is an open collection of five multi-view drone-flight recordings — captured with 4 to 7 consumer-grade cameras per sequence — paired with high-accuracy 3D ground-truth trajectories from a real-time RTK positioning system (Fixposition). Unlike the individual open-source trackers elsewhere in this section, this is a **benchmarking resource**, not a detection/tracking tool itself: it exists to let researchers develop and validate multi-camera 3D trajectory-estimation methods against known-accurate ground truth, including the harder case of cameras that are unsynchronized and have unknown relative poses. The authors' companion repository, `mvus`, implements a pipeline that reconstructs 3D object trajectories and camera poses from exactly this kind of unsynchronized, uncalibrated multi-camera setup.

## Key Facts

- **Author:** CenekAlbl (GitHub)
- **Type:** Open dataset (+ companion reconstruction pipeline `mvus`)
- **Status:** Well-adopted relative to other entries in this section — 213 stars, 55 forks on the dataset repo; 89 stars, 18 forks, 200 commits on `mvus`
- **Ground truth source:** Real-time RTK positioning (Fixposition)
- **Associated paper:** ["3D trajectory reconstruction from unsynchronized, uncalibrated camera networks"](https://arxiv.org/abs/2003.04784) (arXiv:2003.04784) — describes reconstructing an airborne object's 3D trajectory from cameras that may be unsynchronized, exhibit rolling-shutter distortion, and have unknown viewpoints

## Dataset Contents

| Dataset | Cameras | Duration | Notes |
|---|---|---|---|
| 1 | 4 | ~2 min | Easy — short, slow flight |
| 2 | 4 | ~2.5 min | Easy — longer, faster flight |
| 3 | 6 | ~9 min | Medium difficulty, various velocities |
| 4 | 7 | ~7 min | High difficulty — fast motion, challenging conditions |
| 5 | 6 | ~10 min | Winter dataset — 3 drones simultaneously, snow-covered terrain |

Ground truth and supporting data vary by set: all five include 3D trajectories and per-camera calibration; datasets 3–5 add temporal synchronization data; datasets 3 and 5 include camera GPS locations; datasets 1–4 include 2D pixel-space labels; dataset 5 (the multi-drone winter set) additionally includes 3D orientation.

## Why This Matters for This Section

This section's steering priorities call out multi-sensor fusion and multi-camera systems that discriminate drones reliably, but nearly every vendor and open-source project here reports its own accuracy figures on its own test data — there is no shared, independently-collected ground truth to check claims against. This dataset is the one resource in this section built specifically to fill that gap: RTK ground truth is materially more trustworthy than GPS-log or manual-inspection "truth" data (the comparison method used in, e.g., [TRAMIS]({{< relref "../detection-methods/tramis.md" >}})'s own preliminary evaluation), and the multi-camera, multi-drone winter set (dataset 5) stresses exactly the close-proximity, adverse-condition scenario this section's editorial focus prioritizes.

## Limitations

- **Dataset, not a tool:** Using this requires separate detection/tracking/reconstruction code — either the authors' own `mvus` pipeline or a different one adapted to consume the provided calibration/sync data.
- **Small sample:** Five sequences total, several only 2–2.5 minutes long — useful for method validation, not a large-scale training corpus.
- **Consumer camera baseline:** Captured with consumer-grade cameras rather than the industrial/purpose-built sensors used in this section's commercial hardware entries — a reasonable proxy for DIY/open-source builds, less so for evaluating high-end fixed-site systems.
- **License:** A license file is present in the repository, but its specific terms were not confirmed for this entry — check directly before reuse.

## Sources

- [drone-tracking-datasets — GitHub](https://github.com/CenekAlbl/drone-tracking-datasets)
- [mvus — 3D trajectory reconstruction pipeline — GitHub](https://github.com/CenekAlbl/mvus)
- [3D trajectory reconstruction from unsynchronized, uncalibrated camera networks — arXiv:2003.04784](https://arxiv.org/abs/2003.04784)
