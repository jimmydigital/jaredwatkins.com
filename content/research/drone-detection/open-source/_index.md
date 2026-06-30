---
title: "Open Source Drone Detection Projects"
date: 2026-06-05
lastmod: 2026-06-05
draft: false
description: "Open-source tools and libraries for drone detection and Remote ID decoding — usable today for building custom detection systems."
research_area: "drone-detection/open-source"
last_reviewed: 2026-06-05
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.7
  disable: false
---

# Open Source Drone Detection Projects

Active open-source projects for drone detection and Remote ID decoding. Filtered for projects that are functional and usable today.

## Projects

- [OpenDroneID]({{< relref "opendroneid.md" >}}) — ASTM F3411 encode/decode library; Android receiver; Linux transmitter
- [DJI DroneID Decoder]({{< relref "dji-droneid-decoder.md" >}}) — GNU Radio / SDR decoder for proprietary DJI DroneID (pre-Remote ID)
- [ArduPilot RemoteID]({{< relref "ardupilot-remoteid.md" >}}) — Open-source Remote ID transmitter for ArduPilot-based drones
- [Acoustic ML Pipeline]({{< relref "acoustic-ml-pipeline.md" >}}) — Raspberry Pi + MEMS mic array + CNN/Random Forest classifier; detects RF-dark drones acoustically

## Quick Reference: What Each Project Does

| Project | Language/Platform | Function | Status |
|---------|------------------|----------|--------|
| opendroneid-core-c | C | ASTM F3411 encode/decode library | Active |
| receiver-android | Android/Java | Decode BRI from Wi-Fi NAN + BT5 | Active |
| proto17/dji_droneid | GNU Radio / MATLAB | Decode proprietary DJI DroneID | Active (community) |
| ArduPilot/ArduRemoteID | C++ / ArduPilot | Transmit Remote ID from ArduPilot drones | Active |
| PiNcH | Python | Drone presence detection via network traffic analysis (ArduCopter) | Research |
| RPi acoustic ML pipeline | Python / scikit-learn / TFLite | MEMS mic array + MFCC + Random Forest/CNN for passive acoustic detection | DIY / Research |
