---
title: "OpenDroneID"
date: 2026-06-05
lastmod: 2026-06-05
draft: false
description: "Open-source implementation of the ASTM F3411 / FAA Remote ID standard — core C library, Android receiver, and Linux transmitter for decoding and displaying Remote ID broadcasts from compliant drones."
research_area: "drone-detection/open-source"
source_urls:
  - "https://github.com/opendroneid/opendroneid-core-c"
  - "https://github.com/opendroneid/specs"
  - "https://mavlink.io/en/services/opendroneid.html"
  - "https://github.com/ArduPilot/ArduRemoteID"
last_reviewed: 2026-06-05
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

OpenDroneID is the open-source reference implementation of the ASTM F3411 Remote ID standard — the protocol underpinning the FAA's mandatory Broadcast Remote ID requirement for US drones. The project provides a C encode/decode library, an Android receiver app, a Linux transmitter, and the formal specification. It is the correct starting point for any custom Remote ID monitoring infrastructure. **Limitation:** Decodes only FAA-compliant drones broadcasting on standard protocols. Does not detect DJI proprietary DroneID, non-compliant drones, or RF-dark threats.

## Key Facts

- **Maintained by:** OpenDroneID GitHub organization (community; multiple contributors including Wingcopter, AeroDefense, others)
- **Standard implemented:** ASTM F3411-22a (equivalent to EUROCAE ED-269)
- **Broadcast media:** Wi-Fi NAN (802.11), Bluetooth 5 Long Range (BT5 LR), Bluetooth 4 Legacy
- **License:** Apache 2.0 (core-c library)
- **Status:** Active; regularly updated

## Repositories

**opendroneid-core-c** (`github.com/opendroneid/opendroneid-core-c`)
The core C library for encoding and decoding ASTM F3411 messages. Produces and parses all message types: Basic ID, Location/Vector, Authentication, Self-ID, System, Operator ID. Includes MAVLink bindings. Dependency for building any custom Remote ID receiver or sender in C/C++ or systems with C FFI.

**receiver-android** (`github.com/opendroneid/receiver-android`)
Android app that decodes Broadcast Remote ID from Wi-Fi NAN and Bluetooth 5 LR. Displays drone ID, position, altitude, velocity, and operator location on a map. Practical for field use (phone or tablet carried by security personnel). Requires Android hardware with Wi-Fi NAN support (most Android phones from ~2018+).

**transmitter-linux** (`github.com/opendroneid/transmitter-linux`)
Linux reference transmitter using Wi-Fi and Bluetooth interfaces. Used for testing receiver implementations.

**specs** (`github.com/opendroneid/specs`)
Formal Open Drone ID specification document.

## What Can Be Built With This

For a fixed-site critical infrastructure Remote ID monitoring installation:
1. Use a Raspberry Pi 4 or similar Linux SBC with a Wi-Fi adapter supporting NAN and a BT5 adapter
2. Run a custom receiver based on opendroneid-core-c
3. Feed decoded telemetry to a local dashboard or alert system
4. Range: ~300 m–1.5 km for BT5 LR; ~100–500 m for Wi-Fi NAN depending on environment

This is a low-cost (< $200 hardware), permissible (detection-only), and immediately deployable solution for identifying compliant US drone operators.

## Critical Limitation

OpenDroneID only decodes drones broadcasting the ASTM F3411 standard. It will not detect:
- DJI drones using proprietary DroneID (separate protocol — see DJI DroneID Decoder entry)
- Non-compliant or unregistered drones
- Any drone not actively transmitting (fiber-optic, pre-programmed, or RF-silent)

Remote ID enforcement is improving but compliance is not universal. Do not rely on Remote ID as the sole detection layer.

## Sources

- [opendroneid-core-c — GitHub](https://github.com/opendroneid/opendroneid-core-c)
- [OpenDroneID specification — GitHub](https://github.com/opendroneid/specs)
- [MAVLink OpenDroneID service documentation](https://mavlink.io/en/services/opendroneid.html)
- [ArduPilot ArduRemoteID](https://github.com/ArduPilot/ArduRemoteID) — open-source Remote ID transmitter built on OpenDroneID
