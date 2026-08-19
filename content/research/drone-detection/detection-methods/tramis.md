---
title: "TRAMIS (TRack-based Airspace Monitoring IoT System)"
date: 2026-08-15
lastmod: 2026-08-15
draft: false
description: "Texas A&M academic research system: multi-camera, track-based (not image/ML-based) real-time airspace monitoring for drone/bird/aircraft detection, classification, and 3D geolocation on commodity hardware; field-tested in Alaska UAS flight campaigns."
research_area: "drone-detection/detection-methods"
source_urls:
  - "http://www.conf-icnc.org/2026/papers/p1010-ajeigbe.pdf"
  - "https://ieeexplore.ieee.org/document/11416861"
last_reviewed: 2026-08-15
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

TRAMIS (TRack-based Airspace Monitoring Internet-of-Things System) is an academic research system from Texas A&M University's Department of Electrical & Computer Engineering for real-time, multi-camera monitoring of small aerial objects (UAS, birds, light crewed aircraft). Its distinguishing idea is that it is entirely **track-based rather than image-based**: instead of running deep-learning object detection/classification on every video frame, it extracts lightweight object trajectories from distributed camera feeds and runs detection, drone-vs-bird classification, and 3D geolocation on those trajectories. This sidesteps the need for large labeled training datasets and heavy per-frame compute, and — per the authors' preliminary testing — outperforms a standard YOLOv11 baseline on small, distant objects. TRAMIS is not a commercial product; it has been field-tested during multi-UAS flight campaigns in Alaska, at NASA's Langley Research Center, and in Texas, with results published at ICNC 2026 (paper p1010-ajeigbe).

## Key Facts

- **Developer:** Oluwafemi Ajeigbe and Chenyan Zhu (co-first authors) and Sandip Roy, Dept. of Electrical & Computer Engineering, Texas A&M University
- **Type:** Academic research system (not a commercial product; not published as open-source at time of writing)
- **Detection method:** Passive, purely optical multi-camera video; track/trajectory-based processing (visible-spectrum results reported; infrared and depth cameras integrated but not covered in this paper's reported results)
- **Status:** Field-tested (not commercialized); preliminary performance evaluation published; further field evaluation and a companion paper are in preparation
- **Venue:** 2026 International Conference on Computing, Networking and Communications (ICNC)

## How It Works

TRAMIS uses distributed "sensing pods" — each with multiple video cameras (commonly a Raspberry Pi Camera Module 3 / Sony IMX708 sensor, 1920×1080 @ 25 fps) connected to a Raspberry Pi 4B edge device — that stream video over a local wireless mesh network (consumer ASUS routers) to a central control node. The edge devices deliberately do minimal work: they just capture, locally record, and relay video (dual-path via `ffmpeg` and a TCP dispatcher) rather than running any detection themselves, because low-cost/low-power boards like the Raspberry Pi can't sustain the full processing pipeline without overheating or requiring expensive GPU hardware at every pod.

All the actual computation happens at the control node (tested on an Apple M1 MacBook Pro, Dell laptops, and an NVIDIA Jetson Orin Nano for a GPU-accelerated variant under development): Gaussian-mixture background subtraction (OpenCV MOG2) and morphological filtering extract foreground motion, which customized multi-track extraction algorithms turn into per-camera object trajectories using distance/direction-based association (physics-informed — exploiting the fact that aerial objects move under inertial constraints, so search windows can be small and cheap rather than exhaustive). A "quality gate" then filters spurious tracks (vegetation, cloud edges, camera jitter) using five metrics — sample count, duration, completeness, density, and a linearity score — before any downstream algorithm runs on them.

The advanced monitoring functions are all track-based rather than frame-based: **classification** (bird vs. fixed-wing UAS vs. rotorcraft vs. crewed aircraft) uses correlation coefficients over short track windows to measure how close a trajectory is to a straight line — aircraft show correlation >0.95, birds typically 0.6–0.85 — reaching reliable discrimination within about 7 seconds of track initiation; **3D geolocation** uses multi-view triangulation between paired camera tracks (computing the closest point of approach between rays from two cameras to the object), with one-shot calibration from a known reference point rather than dense 3D scene reconstruction. Because these algorithms operate on lightweight track data instead of images, the authors report they require "very limited computational effort even for 10's or 100's of tracks" and no additional inter-node communication.

## Notable Developments

- **2026 (ICNC 2026 publication):** Results published as "An Object-Track-Driven Distributed System for Real-Time Airspace Monitoring," introducing TRAMIS; paper number p1010-ajeigbe.
- **Two 3-day field campaigns, Nenana Airport, Alaska:** Multiple UAS flown in close proximity (plus birds and crewed aircraft) in structured crossing-traffic patterns with intentional near-conflicts (25–250 ft separation); up to 5 pods and 11 cameras deployed, pod separations 20–90 m.
- **Full-day BVLOS field test, NASA Langley Research Center (Virginia):** Multi-UAS beyond-visual-line-of-sight flights alongside large numbers of birds.
- **Multiple shorter field tests, College Station, Texas.**
- **In preparation:** A field-surveillance dataset of 10,000+ labeled tracks of fixed-wing/rotor-based UAS, birds, and crewed light aircraft (Zhu, Ajeigbe, Roy); an extended field-evaluation paper submitted to the AIAA AVIATION Forum 2026; a companion algorithms paper accepted for presentation at AIAA SciTech 2026 (session IS-34, scheduled Jan 16, 2026); a related FAA UAS Integration Office-funded project report ("Distributed multi-hazard monitoring system for high-density BVLOS operation," Texas A&M Engineering Experiment Station).

## Field Performance (Preliminary)

Reported metrics, drawn from roughly one hour of field data from the second Alaska flight campaign (~220 object tracks of interest) plus separate networking/compute measurements:

| Metric | Reported Value |
|---|---|
| Per-stream video transmission rate | 2.55 Mbps |
| Wireless mesh range tested | Up to 300 m between pods |
| Communication delay | < 0.5 s |
| Frame processing time | 0.08 sec/frame |
| Control-node CPU usage | ~80% average (4 concurrent streams) |
| Classification accuracy (drone vs. bird/other) | 95–98% |
| Object first-detection time | < 0.25 s for 100% of UASs/birds tracked |
| Track fidelity | Tracks maintained for 94% of time points |
| 3D localization error | 8.1–39 m at 300–800 m range |
| Spurious-track filtering | ~1M raw tracks → ~8,000 tracks of interest (~99% reduction) over a 3-day campaign |

As an informal baseline comparison, the authors report that a standard deep-learning detector (YOLOv11) showed "minimal detection capability" for objects under 20 pixels at distances beyond 200 m, while TRAMIS's track-based approach successfully tracked objects with diameters of only 1–4 pixels — illustrating the core argument for track-based over frame-based processing at this scale.

## Claim Verification

### Claim: 95–98% classification accuracy, <0.25s detection time, 8.1–39m 3D localization error
**Status:** Unverified by independent third parties.
**Supporting sources:** The paper itself (Table III), based on the authors' own field-test data — approximately one hour of footage and ~220 tracks from a single Alaska flight campaign.
**Refuting/questioning sources:** None found. Notably, the authors themselves characterize the evaluation as preliminary and based on "relatively limited data," and state that more extensive statistical analysis from longer-duration field campaigns is forthcoming in a separate submission.
**Summary:** These are self-reported results from a conference paper, not yet independently replicated or validated at scale. Treat as promising early-stage evidence of a working system rather than settled, generalizable performance figures.

## Limitations

- **Preliminary evaluation:** Headline accuracy/latency/localization figures are drawn from a single ~1-hour data window (~220 tracks); the authors explicitly caveat this as limited.
- **Bandwidth-heavy, centralized architecture:** Edge pods do no on-board detection — all raw video is streamed to a central control node over the local wireless mesh, which trades edge cost/power savings for high control-node bandwidth and compute demand, and ties effective range to the wireless mesh (tested to 300 m between pods) rather than enabling wide-area distributed deployment.
- **Concurrent-stream ceiling:** Reported field tests processed 4 concurrent video streams at the control node; scaling to substantially more simultaneous pods/cameras is not yet demonstrated.
- **Visible-spectrum results only:** Infrared and depth cameras (TOPDON thermal, OAK-D Long Range) have been integrated and tested, but this paper's reported results are visible-spectrum only.
- **Residual false-track sources:** Vegetation motion, cloud-edge movement near the frame boundary, and brief track fragmentation during rapid maneuvers or occlusion remain open refinement areas per the authors, despite the quality-gate filtering.
- **Not commercialized:** This is a university research system, not a company or product with a funding history or path to market; the closest funding link documented is an FAA UAS Integration Office-sponsored related project report.

## Key People

- **Sandip Roy** — Senior author; Texas A&M University, Dept. of Electrical & Computer Engineering.
- **Oluwafemi Ajeigbe** — Co-first author; Texas A&M University, Dept. of Electrical & Computer Engineering.
- **Chenyan Zhu** — Co-first author; Texas A&M University, Dept. of Electrical & Computer Engineering.

## Sources

- Oluwafemi Ajeigbe, Chenyan Zhu, and Sandip Roy, ["An Object-Track-Driven Distributed System for Real-Time Airspace Monitoring"](http://www.conf-icnc.org/2026/papers/p1010-ajeigbe.pdf) (PDF), ICNC 2026, paper p1010-ajeigbe.
- [IEEE Xplore record](https://ieeexplore.ieee.org/document/11416861)
