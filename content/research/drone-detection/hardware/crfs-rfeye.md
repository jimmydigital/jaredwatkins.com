---
title: "CRFS RFeye"
date: 2026-07-07
lastmod: 2026-07-07
draft: false
description: "UK spectrum-monitoring company whose RFeye passive RF sensor network hunts for signals of interest — telemetry, video links, payload data — rather than known drone signatures, geolocating any RF-emitting drone via AoA/TDoA/FDoA regardless of Remote ID compliance."
research_area: "drone-detection/hardware"
source_urls:
  - "https://www.crfs.com/solutions/drone-detection"
  - "https://www.crfs.com/rfeye-ecosystem"
  - "https://www.crfs.com/hardware/direction-finding"
last_reviewed: 2026-07-07
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

CRFS (UK) makes the RFeye family of networked, passive RF spectrum-monitoring sensors, marketed for drone detection among other spectrum-dominance use cases (military EW, border security, spectrum regulation). Rather than matching known drone protocol signatures, RFeye's "signal detectors" hunt for signals of interest — telemetry, video downlinks, payload data transfer — and geolocate the emitter in 3D the moment a match is found. This makes it agnostic to whether a drone is Remote ID compliant, COTS, modified, or military; it detects anything emitting RF in its covered bands. **Limitation:** like all RF-based systems, it has zero capability against drones with no active RF emission (fiber-optic tethered, fully autonomous pre-programmed, RF-silent).

## Key Facts

- **Manufacturer:** CRFS Ltd, United Kingdom
- **Type:** Company — RF sensor hardware + software (RFeye Suite)
- **Frequency coverage:** 100 MHz to above 10 GHz across the RFeye Node product line (specific range varies by node model, e.g. 100-8, 100-18, 100-40)
- **Geolocation techniques:** Angle of Arrival (AoA), Time Difference of Arrival (TDoA — 3 nodes for 2D, 4 for 3D), Frequency Difference of Arrival (FDoA), Power of Arrival (PoA)
- **Claimed range:** Up to 400 km for military drones under favorable conditions; shorter for COTS drones depending on power and environment
- **Integration:** TRL-9; integrated into L3Harris' Drone Guardian and Rafael's Drone Dome C-UAS systems
- **Status:** Active; deployed by NATO members and allied governments for spectrum dominance and drone detection

## How It Works

RFeye's core technology is "signal detectors" rather than drone-signature libraries: the system is configured to recognize categories of RF activity (telemetry, video link modulation characteristics, payload data transfer) instead of matching against a database of specific drone models. CRFS argues this is more robust against modified, homebuilt, or military drones that a library-based system (tuned to recognize specific COTS protocols) would miss. When a signal of interest is detected, the networked RFeye nodes immediately compute a 3D geolocation (latitude, longitude, altitude) using AoA, TDoA, FDoA, or PoA techniques depending on deployment geometry, streamed to a C2 platform via open APIs.

Because detection triggers on RF characteristics of the signal itself rather than decoding its content, RFeye can identify a drone's presence and location without needing the drone's cooperation — it doesn't rely on Remote ID broadcasts, though it can also monitor those bands if desired. The same underlying RFeye Node/Array hardware family also serves CRFS' broader spectrum-monitoring, EMSO, TSCM, and border-security product lines.

## Capabilities

- **Non-cooperative detection:** Works against COTS, modified, and military drones without needing a specific protocol signature match
- **3D geolocation:** Full lat/long/altitude fix via multi-technique geolocation (AoA/TDoA/FDoA/PoA)
- **Swarm detection:** Rapid geolocation cycles (down to once per second) support tracking multiple simultaneous drones
- **Open architecture:** Streaming geolocation data and APIs for integration into third-party C2 systems — already integrated into L3Harris and Rafael platforms
- **Dual-use spectrum monitoring:** The same sensor network can be used for general RF spectrum awareness beyond drone-specific detection

## Limitations

- **RF-only:** No capability against fiber-optic tethered or fully RF-silent autonomous drones
- **Geometry-dependent accuracy:** TDoA/FDoA geolocation accuracy depends on favorable sensor node placement and spacing; a single node can only provide a bearing (AoA), not a fix
- **No integrated countermeasures:** RFeye is a detection/geolocation sensor family — interdiction requires separate systems (as seen in its L3Harris/Rafael integrations)

## Sources

- [CRFS Drone Detection overview](https://www.crfs.com/solutions/drone-detection)
- [RFeye technology & ecosystem](https://www.crfs.com/rfeye-ecosystem)
- [RFeye Direction Finding hardware overview](https://www.crfs.com/hardware/direction-finding)
