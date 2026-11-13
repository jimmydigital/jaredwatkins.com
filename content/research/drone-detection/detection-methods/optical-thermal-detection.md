---
title: "Optical / Thermal Detection"
date: 2026-06-05
lastmod: 2026-11-12
draft: false
description: "Electro-optical and infrared (EO/IR) camera systems for drone detection — the only modality effective against fiber-optic tethered drones in a passive sensor role; requires AI classification to discriminate drones from birds."
research_area: "drone-detection/detection-methods"
source_urls:
  - "https://marduk.ee/news/the-growing-threat-of-fiber-optic-uavs-and-how-to-see-them-coming"
  - "https://marduk.ee/news/estonian-defence-forces-and-marduk-technologies-demonstrate-cutting-edge-counter-drone-capability-at-siil-2025"
  - "https://drone-warfare.com/counter-uas/multi-sensor-fusion/"
last_reviewed: 2026-11-12
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Electro-optical (EO) and infrared (IR/thermal) camera systems detect drones visually against the sky or by heat signature from motors. EO/IR is the **only passive sensor modality effective against fiber-optic tethered drones** — which emit no RF, produce minimal acoustic signature at distance, but are still physically visible. Machine learning object detection (YOLO-class models) enables automated classification, but drone-vs-bird discrimination at range requires high-resolution sensors and well-tuned models. The Marduk Technologies Piraya system, shown at the Siil 2025 exercise, is a notable example of passive optical C-UAS.

## Key Facts

- **Type:** Passive sensor (EO cameras require visible light; IR is passive; no emissions)
- **Effective range:** 200 m–2+ km depending on sensor resolution, aperture, and drone size
- **Bird discrimination:** Moderate to good with trained AI; challenging for small drones vs. small birds at range
- **Works against:** All drone types including fiber-optic and RF-dark; also detects birds (which then need to be filtered)
- **Key advantage:** Only modality that detects fiber-optic tethered drones at tactically useful range
- **Key limitation:** Requires adequate visibility (degraded by fog, heavy rain, darkness without IR); computational cost of real-time AI inference across multiple camera fields

## What It Is / How It Works

**Visible (EO) detection:** High-resolution PTZ cameras or fixed wide-angle cameras cover a sector of sky. AI object detection models (YOLO, SSD, or custom architectures) run inference on frames to detect small moving objects. The primary challenge is distinguishing small drones from birds at range — both appear as small, dark, moving objects against sky. Detection range for a DJI Phantom-class drone is approximately 200–800 m with commercial megapixel cameras; purpose-built systems with larger apertures extend to 1–2 km.

**Infrared (IR/thermal) detection:** Drone motors and ESCs generate heat (typically 40–80°C during operation). MWIR and LWIR cameras detect this thermal signature against the cooler sky background. Detection range is commonly reasoned about with the Johnson criteria (the number of pixels on target needed to detect, recognize or identify), so small drones need long focal lengths or high-resolution sensors. IR detection is less affected by lighting conditions (effective day and night) but thermal contrast varies with ambient temperature and drops near thermal crossover, when the target and background are at similar temperatures, which is more likely in hot weather. IR is particularly effective for detecting hovering drones where the motor has been running.

**AI classification for drone-vs-bird:**
- Visual object detectors (YOLO-class) train on annotated drone datasets. Public datasets include "Drone vs. Bird" detection challenge datasets (used in academic competitions).
- Motion analysis — trajectory prediction and flight path smoothness — helps filter out birds, which exhibit more erratic movement than drones on programmed paths.
- Multi-frame tracking improves accuracy over single-frame detection.

## Fiber-Optic Drone Specific Application

Fiber-optic tethered drones are emerging as a critical threat. These drones:
- Carry no RF transceiver
- Are unjammable and undetectable by RF sensors
- Are being deployed in conflict zones (Ukraine/Russia) for both surveillance and kamikaze missions
- Are becoming commercially available

**Why optical is the solution:** While fiber-optic drones hide from all RF-based sensors, they cannot hide from optical observation — they are physically present in the sky and produce heat from motors. Marduk Technologies' approach uses passive high-resolution optical and thermal cameras with AI tracking, specifically targeting this threat class.

Fiber-optic control links also remove the RF emissions that other sensors rely on, so optical and radar tracks are the main passive options; see [Multi-Sensor Fusion]({{< relref "multi-sensor-fusion.md" >}}).

## Key Commercial Implementation: Marduk Piraya

Marduk Technologies (Tallinn, Estonia) has developed the Piraya passive optical C-UAS system. Vendor-reported results from the Siil 2025 exercise (20 May 2025):
- Integrated on CV90 infantry fighting vehicle
- Six quadcopters detected, tracked, and neutralized
- One engagement at 2 km range
- Fully passive — emits no signals; operates in electronically contested environments
- Estonian Ministry of Defense funding support

These results come from the vendor's own announcement and have not been independently verified; Marduk also markets a related Shark system, whose ranges are likewise vendor claims.

## Drone-vs-Bird in Visual Systems

Visual drone-vs-bird discrimination remains an active research area:
- **Shape analysis:** Multi-rotor drones have symmetric, compact shapes; birds have elongated bodies with outstretched wings — detectable at sufficient resolution
- **Flight behavior:** Drones maintain steadier flight paths; birds bank and flap irregularly
- **Motor glint:** Exposed ESCs and motors can produce visual/IR glints distinguishing them from birds

## Notable Developments

- **2026-01:** Industry analysis (Drone Warfare) discusses the Johnson criteria and thermal crossover as limits on EO/IR drone detection.
- **2025-05:** Marduk Technologies and the Estonian Defence Forces demonstrated Piraya at Siil 2025 (20 May).
- **2025:** Marduk publishes guidance on detecting fiber-optic UAVs with passive optical sensors.

## Key Organizations

- **Marduk Technologies** (Tallinn, Estonia) — Piraya and Shark passive optical C-UAS systems
- **Estonian Defence Forces / Ministry of Defense** — Siil 2025 exercise and funding partner

## Sources

- [Marduk — Fiber Optic UAV Threat and Optical Detection](https://marduk.ee/news/the-growing-threat-of-fiber-optic-uavs-and-how-to-see-them-coming)
- [Marduk Piraya — Siil 2025 live-fire test results](https://marduk.ee/news/estonian-defence-forces-and-marduk-technologies-demonstrate-cutting-edge-counter-drone-capability-at-siil-2025)
- [Counter-UAS 101: Multi-Sensor Fusion — Drone Warfare](https://drone-warfare.com/counter-uas/multi-sensor-fusion/) — Johnson criteria and thermal crossover discussion
