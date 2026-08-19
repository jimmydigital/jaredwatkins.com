---
title: "UAV Detection and Tracking (RobCaamano)"
date: 2026-08-15
lastmod: 2026-08-15
draft: false
description: "Open-source single-camera UAV detection using a fine-tuned Faster R-CNN ResNet101 model (TensorFlow 2) with Kalman-filter trajectory tracking and visualization; 2D pixel-space only, no 3D geolocation."
research_area: "drone-detection/open-source"
source_urls:
  - "https://github.com/RobCaamano/Uav-Detection-And-Tracking"
last_reviewed: 2026-08-15
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

UAV Detection and Tracking is an open-source, single-camera pipeline that fine-tunes a Faster R-CNN ResNet101 object detector (from TensorFlow's model zoo) to identify drones in video, then applies a Kalman filter to trace and visualize each UAV's trajectory as an overlay line on the output video. It is a simpler, single-view, 2D pixel-space counterpart to this section's stereo/multi-camera 3D projects — useful as a lightweight starting point or baseline rather than a deployable multi-object 3D localization system.

## Key Facts

- **Author:** RobCaamano (GitHub)
- **Type:** Open-source software project — single-camera UAV detection + 2D trajectory tracking
- **Status:** Active — 36 stars, 5 forks, 1 open issue as of this review
- **Detection model:** Fine-tuned Faster R-CNN ResNet101 (`faster_rcnn_resnet101_v1_800x1333_coco17_gpu-8`, TensorFlow Object Detection API)
- **Tracking:** Kalman filter, single-camera, 2D pixel-space trajectory only (no stereo/3D geolocation)
- **License:** Not stated in the repository as of this review — confirm terms directly before reuse

## How It Works

The pipeline is a standard fine-tuning + inference + visualization chain built on the TensorFlow Object Detection API: video is split into frames (`vids_to_frames.py`), annotations are converted to TFRecord format (`XML_to_TFRecord.py`), and a Faster R-CNN ResNet101 model pretrained on COCO is fine-tuned for UAV detection (`model_main_tf2.py`). Inference (`UAV_FasterRCNN.py`) produces per-frame bounding boxes, and a Kalman filter module (`kalman_filter.py`) smooths detection centroids into a trajectory, which is drawn as a trace line over the output video. Training-loss curves (classification loss, localization loss, learning rate) are included in the repo, along with example detection images and demo tracking videos, but no formal accuracy metrics (mAP, precision/recall) are published.

## Limitations

- **No license specified:** Terms of reuse are unclear from the repository as reviewed — verify directly with the author before any derivative or commercial use.
- **2D, single-camera only:** No stereo pairing or 3D geolocation — trajectory is a pixel-space overlay, not a geographic or metric 3D position, unlike [Stereo Drone Tracker]({{< relref "stereo-drone-tracker.md" >}}) or [eye_sky]({{< relref "eye-sky.md" >}}) in this section.
- **No published accuracy metrics:** Training-loss curves are shown, but no detection accuracy (mAP), false-positive rate, or drone-vs-other-object discrimination performance is reported.
- **Older detection architecture:** Faster R-CNN ResNet101 is a heavier, slower two-stage detector relative to the single-stage YOLO-family models used in this section's newer projects (e.g., [Stereo Drone Tracker]({{< relref "stereo-drone-tracker.md" >}})'s YOLOv11s) — likely a real-time-performance tradeoff on comparable hardware, though not benchmarked in the repo.

## Sources

- [Uav-Detection-And-Tracking — GitHub](https://github.com/RobCaamano/Uav-Detection-And-Tracking)
