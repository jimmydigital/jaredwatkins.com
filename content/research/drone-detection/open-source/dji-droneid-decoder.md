---
title: "DJI DroneID Decoder"
date: 2026-06-05
lastmod: 2026-06-05
draft: false
description: "Open-source GNU Radio / SDR decoder for DJI's proprietary DroneID protocol — decodes DJI drone telemetry transmitted on 2.4/5.8 GHz control links before and alongside FAA Remote ID."
tags: ["open-source", "dji", "drone-detection", "gnu-radio", "sdr", "rf-detection"]
categories: ["technology"]
research_area: "drone-detection/open-source"
source_urls:
  - "https://github.com/proto17/dji_droneid"
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC10490811/"
last_reviewed: 2026-06-05
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

DJI drones transmit a proprietary telemetry protocol called DroneID embedded in their OcuSync/O3 control link — separate from (and predating) the FAA Remote ID standard. The `proto17/dji_droneid` project reverse-engineered this protocol and provides a GNU Radio OOT module and MATLAB scripts to decode DroneID from received radio signals, exposing drone serial number, GPS position, altitude, velocity, and operator position. This enables passive detection and tracking of DJI drones using an SDR (software-defined radio) receiver without relying on FAA compliance.

## Key Facts

- **Repository:** `github.com/proto17/dji_droneid`
- **Tested against:** DJI Mini 2, and other OcuSync-based drones
- **Implementation:** GNU Radio out-of-tree (OOT) module + MATLAB processing scripts
- **Hardware required:** SDR receiver (RTL-SDR, HackRF, USRP, or similar) + antenna for 2.4/5.8 GHz
- **Detection range:** Dependent on SDR sensitivity and antenna; RF-based range applies (~1–3 km)
- **Status:** Community-maintained; active as of 2025 based on referenced research

## What It Does

DJI encodes a telemetry payload into OcuSync/Wi-Fi 2 frames on the downlink from drone to controller. This payload contains:
- Drone serial number
- GPS coordinates (latitude, longitude, altitude)
- Altitude above sea level and above home point
- Velocity vector
- Operator/home point GPS coordinates

The `proto17/dji_droneid` decoder captures the RF signal with an SDR, demodulates the OcuSync/Wi-Fi 2 frame, extracts and decodes the DroneID payload, and outputs structured telemetry. Detection distances up to 1.3 km (Mavic Air), 1.5 km (Mavic 3), and 3.7 km (Mavic 2 Pro) have been documented in literature.

## Practical Use for Critical Infrastructure

An RTL-SDR dongle (~$30) combined with a directional 2.4 GHz antenna and this software provides:
- Passive detection of DJI drones within RF range
- Operator GPS location (useful for law enforcement response)
- Drone model identification via serial number prefix
- No dependency on FAA Remote ID compliance

This is significantly more capable than Remote ID-only for detecting DJI drones, as it works even when a pilot deliberately disables Remote ID broadcast (which requires hardware modification on newer drones but is trivial on older ones).

## Limitations

- **DJI-only:** Does not decode other manufacturers' protocols (Skydio, Autel, Parrot, ArduPilot)
- **Encryption evolution:** DJI has changed OcuSync protocols across product generations; decoder may not cover all current models
- **RF-only:** Does not detect DJI drones operating autonomously without active RF link
- **Legal note:** Receiving and decoding RF is permissible (monitoring only); not jamming

## Sources

- [proto17/dji_droneid — GitHub](https://github.com/proto17/dji_droneid)
- [Drone Detection and Tracking Using RF Identification Signals — PMC 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10490811/) — academic study documenting detection ranges for Mavic series
