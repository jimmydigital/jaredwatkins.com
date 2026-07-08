---
title: "iNTERCEPT"
date: 2026-07-07
lastmod: 2026-07-07
draft: false
description: "Open-source, web-based signal-intelligence platform unifying SDR tools (ADS-B, AIS, pagers, weather satellites, and more); includes a multi-vector drone-detection module combining Remote ID, sub-GHz RF, and 2.4/5.8 GHz scanning."
research_area: "drone-detection/open-source"
source_urls:
  - "https://github.com/smittix/intercept"
  - "https://smittix.github.io/intercept/"
last_reviewed: 2026-07-07
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

iNTERCEPT is an open-source, self-hosted signal-intelligence platform that unifies a broad set of SDR-based tools behind a single web interface — ADS-B/AIS tracking, pager and satellite decoding, APRS, counter-surveillance (TSCM), and more. Its relevance to drone detection is one module among many: a "Drone Intelligence" feature performing multi-vector UAV detection via ASTM F3411 Remote ID (WiFi/BLE), RTL-SDR scanning at 433/868 MHz, and HackRF scanning at 2.4/5.8 GHz, with a live contact map and risk scoring. **Limitation:** drone detection is a secondary feature of a general SIGINT platform, not a purpose-built counter-UAS tool — evaluate it primarily if you already want the broader SDR toolkit.

## Key Facts

- **Author:** smittix (GitHub)
- **Type:** Open-source software (Flask/Python web application)
- **License:** Apache 2.0
- **Status:** Very active; 1.9k GitHub stars, 247 forks, releases through v2.27.0 (May 2026)
- **Stack:** Python (46%), HTML/JS/CSS front end, Docker support (amd64 + arm64), optional PostgreSQL for ADS-B history
- **Hardware:** RTL-SDR (required baseline, ~$25–35), monitor-mode WiFi adapter, Bluetooth adapter (often built-in), optional HackRF and GPS

## How It Works

iNTERCEPT bundles and web-ifies a long list of established open-source SDR tools rather than reimplementing signal processing itself: `rtl_fm`/`multimon-ng` for pager decoding, `rtl_433` for 433 MHz IoT/sensor traffic, `dump1090` for ADS-B, `acarsdec`/`dumpvdl2` for aircraft datalink, `direwolf` for APRS, `aircrack-ng` for WiFi monitor-mode scanning, and SatDump for weather satellite imagery, among others. The Drone Intelligence module adds ASTM F3411 Remote ID decoding over WiFi/BLE alongside RTL-SDR-based sub-GHz RF scanning (433/868 MHz, common analog FPV/control bands in some regions) and HackRF-based 2.4/5.8 GHz scanning, correlating detections on a live map with a risk-scoring layer. A guided setup wizard installs tool profiles (Core SIGINT, Maritime & Radio, RF Security, etc.) and the platform can run standalone or in Docker, including distributed "remote agent" sensor nodes.

## What Can Be Built With This

For a general-purpose field SIGINT/monitoring station that includes drone awareness as one of several capabilities:
1. Deploy on a Raspberry Pi 5 (or x86 host) via the setup wizard or Docker, selecting the "RF Security" and relevant profiles
2. Attach an RTL-SDR, monitor-mode WiFi adapter, and optionally a HackRF for 2.4/5.8 GHz coverage
3. Enable the Drone Intelligence module alongside ADS-B/AIS tracking for a unified airspace/maritime/RF picture
4. Use the distributed remote-agent feature to extend coverage across multiple sites

This is a better fit for users who want one platform covering many SIGINT domains (aircraft, vessels, pagers, weather, drones) than for a dedicated single-purpose drone sensor — compare to [Mesh-Mapper]({{< relref "mesh-mapper.md" >}}) or [OpenDroneID]({{< relref "opendroneid.md" >}}) for narrower, lighter-weight deployments.

## Critical Limitation

Drone detection in iNTERCEPT depends on the same constraints as any Remote-ID-based tool for the WiFi/BLE vector, plus whatever RF signatures its 433/868 MHz and 2.4/5.8 GHz scanning modes are tuned to recognize — it does not claim to detect RF-silent, fiber-optic-tethered, or non-compliant drones outside those signatures. As a broad multi-domain SIGINT platform (built partly with AI-assisted coding per the project's own disclosure), the drone module has had less dedicated scrutiny than single-purpose tools; the README explicitly states the software is for educational and authorized use only.

## Sources

- [iNTERCEPT — GitHub](https://github.com/smittix/intercept)
- [iNTERCEPT project site](https://smittix.github.io/intercept/)
