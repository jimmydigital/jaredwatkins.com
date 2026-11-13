---
title: "ArduPilot ArduRemoteID"
date: 2026-06-05
lastmod: 2026-11-12
draft: false
description: "Open-source Remote ID transmitter module for ArduPilot-based drones — implements OpenDroneID/ASTM F3411 broadcast on Wi-Fi and Bluetooth from any ArduPilot vehicle."
research_area: "drone-detection/open-source"
source_urls:
  - "https://github.com/ArduPilot/ArduRemoteID"
  - "https://mavlink.io/en/services/opendroneid.html"
  - "https://discuss.ardupilot.org/t/ardupilot-opendroneid-support/89407"
  - "https://github.com/ArduPilot/ArduRemoteID/releases"
last_reviewed: 2026-11-12
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

ArduRemoteID is the official ArduPilot implementation of the Remote ID transmitter. It runs on a companion microcontroller attached to any ArduPilot flight controller (Pixhawk and derivatives) and broadcasts ASTM F3411 Broadcast Remote ID over Wi-Fi NAN and Bluetooth 5 LR. Relevant to the critical infrastructure detection use case as context: custom or hobbyist ArduPilot drones are a significant threat vector (used in DIY FPV attack drones), and ArduRemoteID is what makes those drones detectable via the OpenDroneID receiver stack if the operator installs it.

## Key Facts

- **Repository:** `github.com/ArduPilot/ArduRemoteID`
- **Purpose:** Transmitter (on-drone side); relevant to detection in that it enables OpenDroneID receivers to detect ArduPilot drones
- **Protocol:** ASTM F3411 / OpenDroneID; MAVLink interface to flight controller
- **Hardware:** ESP32-S3 and ESP32-C3 based boards, including commercial boards from Holybro, CUAV, BlueMark and mRo; also runs on development boards
- **Interfaces:** MAVLink and DroneCAN connections to the flight controller
- **Security:** Firmware supports a lock level (LOCK_LEVEL) and signed secure updates
- **Latest release seen:** v1.14 (16 October 2023)

## What It Is / How It Works

ArduPilot firmware gained OpenDroneID support in the 4.2.3 beta releases (announced 10 August 2022 on the ArduPilot Discourse). The flight controller sends Remote ID data (basic ID, location, operator ID, system and self-ID messages) over MAVLink to a companion board running ArduRemoteID, or over DroneCAN. The board encodes the messages per ASTM F3411 and broadcasts them over Bluetooth 5 long range and Wi-Fi (NAN, with WLAN beacon support added in a later release).

Operators set identifiers through parameters. A lock level setting, together with signed firmware updates, is intended to stop owners tampering with the transmitter configuration on compliant builds. A detection receiver sees an ArduRemoteID drone the same way it sees any other F3411 broadcaster; see [FAA Remote ID Monitoring]({{< relref "../detection-methods/rf-detection.md" >}}).

## Relevance to Threat Modeling

ArduPilot is the most widely used open-source autopilot in the world, used in:
- DIY multi-rotors and fixed-wing aircraft
- Commercial agricultural drones
- Academic research platforms
- Modified consumer drones

An ArduPilot drone **without** ArduRemoteID installed will not broadcast Remote ID and will be invisible to Remote ID receivers. This is the default state for most DIY/custom builds. The threat actor building a custom surveillance or attack drone based on ArduPilot will not install Remote ID — making RF and radar detection modalities the only effective approaches.

## Notable Developments

- **2023-10:** ArduRemoteID v1.14 — lock level handling fix, DroneCAN acceptance filters, serial console output of received Remote ID messages.
- **2022-08:** ArduRemoteID 1.1 (12 August) adds Bluetooth 5 long range on ESP32-S3; release 1.4 (17 August) adds ESP32-C3 support.
- **2022-08:** OpenDroneID support announced for ArduPilot 4.2.3 beta (10 August).
- **Between releases 1.10 and 1.13:** added BlueMark public key support, WLAN beacon and dual-ID transmission, and boards from Holybro, CUAV, mRo and BlueMark (release years not confirmed).

## Key Organizations

- **ArduPilot project** — maintains the flight stack and ArduRemoteID
- **MAVLink** — defines the OpenDroneID message service used between flight controller and transmitter
- **Holybro, CUAV, BlueMark, mRo** — hardware vendors with ArduRemoteID-supported boards
- **ASTM International** — publishes the F3411 standard being implemented

## Sources

- [ArduPilot/ArduRemoteID — GitHub](https://github.com/ArduPilot/ArduRemoteID)
- [MAVLink OpenDroneID service](https://mavlink.io/en/services/opendroneid.html)
- [ArduPilot OpenDroneID support (ArduPilot Discourse)](https://discuss.ardupilot.org/t/ardupilot-opendroneid-support/89407) — August 2022 announcement
- [ArduRemoteID releases (GitHub)](https://github.com/ArduPilot/ArduRemoteID/releases) — release history
