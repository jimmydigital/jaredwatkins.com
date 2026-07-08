---
title: "DragonSync"
date: 2026-07-07
lastmod: 2026-07-07
draft: false
description: "Open-source gateway that converts WiFi/Bluetooth Remote ID and DJI DroneID detections into Cursor-on-Target (CoT) for TAK/ATAK, MQTT/Home Assistant, and Anduril Lattice — the software core of the WarDragon detection kit."
research_area: "drone-detection/open-source"
source_urls:
  - "https://github.com/alphafox02/DragonSync"
  - "https://github.com/alphafox02/droneid-go"
  - "https://github.com/alphafox02/antsdr_dji_droneid"
  - "https://www.rtl-sdr.com/wardragon-real-time-drone-remote-id-tracking-with-snifflee-tar1090-and-atak/"
last_reviewed: 2026-07-07
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

DragonSync (Community Edition) is an open-source Python gateway that turns Remote ID and DJI DroneID detections into Cursor-on-Target (CoT) messages for TAK/ATAK, and optionally publishes per-drone telemetry to MQTT/Home Assistant and Anduril Lattice. It is the software core of the "WarDragon" detection kit built by cemaxecuter (GitHub `alphafox02`) and is designed to run alongside that kit's pre-configured sniffers rather than as a standalone tool. **Limitation:** DragonSync itself does not decode RF — it consumes already-decoded detection streams from separate sniffer processes (droneid-go, antsdr_dji_droneid) over ZMQ.

## Key Facts

- **Maintained by:** alphafox02 / cemaxecuter (GitHub)
- **Type:** Open-source software (fusion/gateway layer, not a sensor)
- **License:** Apache 2.0
- **Status:** Active; 84 GitHub stars, 23 forks (as of mid-2026)
- **Language:** Python (98%)
- **Companion hardware:** Designed around the "WarDragon" kit (pre-integrated sniffers, GPS, ZMQ monitor); also usable standalone with manual sniffer setup

## How It Works

DragonSync ingests three ZMQ streams: decoded WiFi/Bluetooth Remote ID and DJI DroneID frames (via `droneid-go` and `antsdr_dji_droneid`), system/GPS status from `wardragon_monitor.py`, and optional FPV analog-video energy-scan alerts. It can also pull ADS-B/UAT aircraft data from a local `readsb` instance over HTTP. DragonSync merges these streams, rate-limits them, and fans out to multiple sinks simultaneously: CoT over multicast or a TAK server (with optional TLS) for ATAK/WinTAK display, MQTT with Home Assistant auto-discovery (per-drone device trackers, pilot/home markers, sensor entities), and Anduril Lattice for organizations using that platform. A read-only HTTP API also serves a companion WarDragon ATAK plugin.

Notable design details: CoT icons are chosen from the Remote ID UA Type field (fixed-wing vs. rotorcraft), drones that stop reporting are marked offline in Home Assistant while preserving location history, and an optional allow-list-only Kismet ingest path can add WiFi/Bluetooth device locations to the CoT feed without flooding ATAK with unrelated devices.

## What Can Be Built With This

For a TAK/ATAK-centric detection deployment:
1. Run WiFi/BLE Remote ID sniffers (droneid-go) and optionally a DJI DroneID SDR decoder (antsdr_dji_droneid) on the same host
2. Point DragonSync at their ZMQ outputs via `config.ini`
3. Feed CoT to ATAK via multicast (LAN/VPN) or a TAK server for wider distribution
4. Optionally bridge to Home Assistant for dashboarding or to Lattice for organizations already standardized on that C2 layer

This is primarily a fusion/integration layer — it assumes the detection hardware and sniffer software are already producing decoded output; see [OpenDroneID]({{< relref "opendroneid.md" >}}) and [DJI DroneID Decoder]({{< relref "dji-droneid-decoder.md" >}}) for the underlying decode stacks.

## Critical Limitation

DragonSync performs no RF capture or decoding itself — it is a data-fusion and CoT-conversion layer sitting downstream of separate sniffer processes. Deploying it requires the WarDragon kit or an equivalent manually-assembled sniffer stack (droneid-go, antsdr_dji_droneid, wardragon_monitor.py). Like all Remote ID–based tools, it cannot see non-compliant, RF-silent, or fiber-optic-tethered drones, and ADS-B/978 ingestion depends on a correctly configured local `readsb` instance.

## Sources

- [DragonSync — GitHub](https://github.com/alphafox02/DragonSync)
- [droneid-go — GitHub](https://github.com/alphafox02/droneid-go)
- [antsdr_dji_droneid — GitHub](https://github.com/alphafox02/antsdr_dji_droneid)
- [WarDragon: Real-Time Drone Remote ID Tracking — RTL-SDR.com](https://www.rtl-sdr.com/wardragon-real-time-drone-remote-id-tracking-with-snifflee-tar1090-and-atak/)
