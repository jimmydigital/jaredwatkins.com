---
title: "ArduPilot ArduRemoteID"
date: 2026-06-05
lastmod: 2026-06-05
draft: false
description: "Open-source Remote ID transmitter module for ArduPilot-based drones — implements OpenDroneID/ASTM F3411 broadcast on Wi-Fi and Bluetooth from any ArduPilot vehicle."
research_area: "drone-detection/open-source"
source_urls:
  - "https://github.com/ArduPilot/ArduRemoteID"
  - "https://mavlink.io/en/services/opendroneid.html"
last_reviewed: 2026-06-05
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

ArduRemoteID is the official ArduPilot implementation of the Remote ID transmitter. It runs on a companion microcontroller attached to any ArduPilot flight controller (Pixhawk and derivatives) and broadcasts ASTM F3411 Broadcast Remote ID over Wi-Fi NAN and Bluetooth 5 LR. Relevant to the critical infrastructure detection use case as context: custom or hobbyist ArduPilot drones are a significant threat vector (used in DIY FPV attack drones), and ArduRemoteID is what makes those drones detectable via the OpenDroneID receiver stack if the operator installs it.

## Key Facts

- **Repository:** `github.com/ArduPilot/ArduRemoteID`
- **Purpose:** Transmitter (on-drone side); relevant to detection in that it enables OpenDroneID receivers to detect ArduPilot drones
- **Protocol:** ASTM F3411 / OpenDroneID; MAVLink interface to flight controller
- **Hardware:** ESP32-based module; runs on widely available development boards

## Relevance to Threat Modeling

ArduPilot is the most widely used open-source autopilot in the world, used in:
- DIY multi-rotors and fixed-wing aircraft
- Commercial agricultural drones
- Academic research platforms
- Modified consumer drones

An ArduPilot drone **without** ArduRemoteID installed will not broadcast Remote ID and will be invisible to Remote ID receivers. This is the default state for most DIY/custom builds. The threat actor building a custom surveillance or attack drone based on ArduPilot will not install Remote ID — making RF and radar detection modalities the only effective approaches.

## Sources

- [ArduPilot/ArduRemoteID — GitHub](https://github.com/ArduPilot/ArduRemoteID)
- [MAVLink OpenDroneID service](https://mavlink.io/en/services/opendroneid.html)
