---
title: "Mesh-Mapper"
date: 2026-07-07
lastmod: 2026-07-07
draft: false
description: "Open-source ESP32-based Remote ID detector with dual-core WiFi/Bluetooth scanning, real-time web mapping, Meshtastic mesh alerting, and FAA registration lookup."
research_area: "drone-detection/open-source"
source_urls:
  - "https://www.hackster.io/colonelpanic/mesh-mapper-drone-remote-id-mapping-and-mesh-alerts-8e7c61"
  - "https://github.com/colonelpanichacks/drone-mesh-mapper"
  - "https://github.com/colonelpanichacks/mesh-detect"
  - "https://www.tindie.com/products/colonel_panic/mesh-detect-2/"
  - "https://www.cnx-software.com/2026/03/27/esp32-p4-pi-viewe-raspberry-pi-esp32-p4-esp32-c6-board/"
  - "https://viewedisplay.com/product/esp32-p4-pi-dev-board-wifi6/"
  - "https://linuxgizmos.com/waveshare-pairs-risc-v-esp32-p4-and-esp32-c6-for-wi-fi-6-bluetooth-5-le-and-poe-support/"
  - "https://www.cnx-software.com/2024/04/30/m5stack-coremp135-a-linux-powered-industrial-controller-based-on-stm32mp135-cortex-a7-mpu/"
last_reviewed: 2026-07-07
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Mesh-Mapper is an open-source, ESP32-based Remote ID detection system built by maker "Colonel Panic." A dual-core Xiao ESP32 S3 captures Broadcast Remote ID over WiFi and Bluetooth simultaneously, streams it to a Python Flask web app for real-time map visualization, and optionally relays compact alerts over a Meshtastic LoRa mesh network for distributed, off-grid coverage. **Limitation:** decodes only FAA-compliant Remote ID broadcasts — no capability against non-compliant, RF-silent, or fiber-optic-tethered drones.

## Key Facts

- **Author:** Colonel Panic (Hackster.io / GitHub `colonelpanichacks`), building on Remote ID decoding work by Cemaxecuter
- **Type:** Open-source hardware + software project
- **Status:** Active; published May 31, 2025
- **Hardware:** Xiao ESP32 S3 (dual-core); custom "MeshDetect" boards sold pre-assembled on Tindie; optional Heltec LoRa V3 for Meshtastic
- **Software:** Python Flask/Flask-SocketIO web app (`mesh-mapper.py` / `mapper.py`); PlatformIO firmware (`remoteid_mesh_dualcore` environment)
- **License/availability:** Firmware and mapper software open on GitHub; PCBs available commercially via Tindie

## How It Works

Core 0 of the ESP32 S3 monitors WiFi in promiscuous mode, capturing Remote ID data from beacon frames and WiFi NAN transmissions. Core 1 concurrently scans Bluetooth LE (BT 4.0 and 5.0) for Remote ID advertisements. Both cores stream detections as JSON over USB serial (115200 baud) to a Flask web application, which renders live drone and pilot positions on a map, logs to CSV and KML, and performs FAA registration lookups on detected aircraft with local caching and rate limiting. The system supports up to three ESP32 devices simultaneously.

Detections can also be forwarded over UART to a Meshtastic LoRa device, letting multiple field nodes share sightings across a mesh network for extended, off-grid coverage — useful for property- or neighborhood-scale distributed monitoring without relying on continuous network connectivity.

## Reported Performance

- Effective detection range: ~5 km in urban environments, 10–15 km in open terrain with improved antennas (author-reported, not independently verified)
- Multi-node deployments described as eliminating coverage gaps via overlapping range

## Critical Limitation

Like other Remote ID–based tools (see [OpenDroneID]({{< relref "opendroneid.md" >}})), Mesh-Mapper only detects drones actively broadcasting FAA-compliant Remote ID over WiFi or Bluetooth. It will not detect non-compliant or unregistered drones, RF-silent/pre-programmed craft, or fiber-optic-tethered drones. The author also notes the bundled Flask server is not production-hardened — a reverse proxy and authentication are recommended for sensitive deployments.

## Related Hardware

Mesh-Mapper's architecture splits the job in two: an ESP32 does WiFi/BT Remote ID capture, and a separate Linux host (Pi, PC) runs the Flask mapping/logging app. A few boards attempt to fuse both roles onto one PCB:

- **[ESP32-P4-Pi (VIEWE)](https://viewedisplay.com/product/esp32-p4-pi-dev-board-wifi6/)** ([writeup](https://www.cnx-software.com/2026/03/27/esp32-p4-pi-viewe-raspberry-pi-esp32-p4-esp32-c6-board/)) — Raspberry Pi form factor (85×56mm, 40-pin GPIO) pairing a 400MHz ESP32-P4 dual-core RISC-V (compute/UI/edge-AI) with an onboard ESP32-C6 (Wi-Fi 6, Bluetooth 5). Runs ESP-IDF/RTOS rather than Linux, but is the closest single-board fit for running both the capture and web-serving roles without a discrete second host.
- **[Waveshare ESP32-P4-WIFI6-POE-ETH](https://linuxgizmos.com/waveshare-pairs-risc-v-esp32-p4-and-esp32-c6-for-wi-fi-6-bluetooth-5-le-and-poe-support/)** — same dual-chip P4 (compute) + C6 (Wi-Fi 6/BLE) pairing, plus PoE, aimed at embedded/display use cases.
- **[M5Stack CoreMP135](https://www.cnx-software.com/2024/04/30/m5stack-coremp135-a-linux-powered-industrial-controller-based-on-stm32mp135-cortex-a7-mpu/)** — genuine embedded Linux host (STM32MP135, Cortex-A7) with Ethernet, USB, and CAN FD. No onboard ESP32 — would still need a discrete ESP32 module (e.g., the Xiao ESP32S3 this project already uses) wired over UART/USB for RF capture.

No mainstream board yet combines a full Linux SoC and an ESP32 as a single fused chip; current options trade either full Linux (P4-Pi boards run RTOS) or onboard wireless capture (CoreMP135 has neither WiFi promiscuous mode nor BLE scanning built in).

## Sources

- [Mesh-Mapper — Hackster.io project writeup](https://www.hackster.io/colonelpanic/mesh-mapper-drone-remote-id-mapping-and-mesh-alerts-8e7c61)
- [drone-mesh-mapper — GitHub](https://github.com/colonelpanichacks/drone-mesh-mapper)
- [mesh-detect firmware — GitHub](https://github.com/colonelpanichacks/mesh-detect)
- [MeshDetect boards — Tindie](https://www.tindie.com/products/colonel_panic/mesh-detect-2/)
