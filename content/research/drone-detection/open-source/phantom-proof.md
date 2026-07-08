---
title: "Phantom-Proof (Fantom Finder)"
date: 2026-07-07
lastmod: 2026-07-07
draft: false
description: "Open-source physical verification of FAA Remote ID broadcasts using passive radar — flags spoofed drone claims (PHANTOM) and contradictory type/signature claims (DECEPTION) rather than trusting the broadcast alone."
research_area: "drone-detection/open-source"
source_urls:
  - "https://github.com/eldaeonuap/phantom-proof"
  - "https://github.com/30hours/blah2"
  - "https://github.com/cyber-defence-campus/droneRemoteIDSpoofer"
last_reviewed: 2026-07-07
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Phantom-Proof (project name "Fantom Finder") is an open-source system that cross-checks FAA Remote ID broadcast claims against independent passive-radar tracks, flagging drones whose broadcast position has no corresponding radar contact as **PHANTOM**, and drones whose broadcast UA type contradicts their radar-observed micro-Doppler signature as **DECEPTION**. It directly addresses a limitation shared by every other tool in this section: Remote ID has no cryptographic signing, so a $5 ESP32 can spoof arbitrary Remote ID frames that any WiFi/BLE receiver will accept at face value. **Limitation:** requires a working passive-radar setup (illuminator of opportunity + coherent SDR receiver), which is more hardware and RF-siting effort than a pure Remote ID receiver.

## Key Facts

- **Author:** eldaeonuap (GitHub), built on the ELDAEON "Nemesis" hardware platform
- **Type:** Open-source software (verification/fusion layer over an existing passive-radar pipeline)
- **License:** MIT; built on `30hours/blah2` (BSD)
- **Status:** Early-stage; built at the 3rd Annual National Security Hackathon (Shack15, San Francisco, May 2–3, 2026); 2 GitHub stars, 1 fork as of review
- **Hardware demoed:** Raspberry Pi 5 + ADALM-Pluto+ SDR + RTL-SDR, ~$300 total, using a TV/DTV broadcast tower as the illuminator (no active emissions of its own)
- **Also covers:** An AIS (maritime) variant — same fusion logic applied to ship AIS spoof defense

## How It Works

A passive-radar receiver (two coherent channels via ADALM-Pluto+, reference + surveillance antennas) feeds `blah2`, an existing open-source passive-radar pipeline that performs clutter cancellation, cross-ambiguity-function processing, CFAR detection, and tracking to produce live target tracks. Separately, an ESP32/Linux Remote ID receiver (built on OpenDroneID) supplies decoded Remote ID claims as JSON. Phantom-Proof's `fusion.py` matches each Remote ID claim to the nearest radar track (within an ~80 m default radius): no matching track means the claim is flagged **PHANTOM**; a matching track whose rotor micro-Doppler signature contradicts the claimed aircraft type (e.g., claiming "Aeroplane" while the radar signature shows a quadcopter) is flagged **DECEPTION**; otherwise the claim is **CONFIRMED**. Verdicts stream to an operator dashboard with CoT (Cursor-on-Target) output for TAK/ATAK integration, and every verdict carries a human-readable rationale string.

For its own demo, the project includes a lightweight `spoofer.py` and an ESP32-S3 firmware sketch that emit fake Remote ID claims — the README credits [droneRemoteIDSpoofer]({{< relref "drone-remoteid-spoofer.md" >}}) (Swiss Cyber-Defence Campus) as the reference implementation for a more full-featured spoofer, useful for testing this and other Remote ID receivers against adversarial broadcasts.

## What Can Be Built With This

For sites already operating or building passive-radar capability (see this section's steering emphasis on micro-Doppler radar as the primary detection method):
1. Stand up `blah2` on a Pi 5 + Pluto+ SDR pair using a broadcast TV tower or strong FM/DTV signal as the illuminator
2. Run a Remote ID receiver (OpenDroneID-based) alongside it
3. Run Phantom-Proof's `fusion.py` to cross-verify Remote ID claims against radar truth
4. Feed verdicts into TAK/ATAK via the bundled CoT bridge for operator situational awareness

This is a verification layer, not a detection sensor in its own right — it assumes both a working passive-radar pipeline and a working Remote ID receiver are already in place. It's most relevant to this section's threat model of distinguishing real drones from spoofed broadcasts, a gap not addressed by pure Remote ID tools like [OpenDroneID]({{< relref "opendroneid.md" >}}) or [Mesh-Mapper]({{< relref "mesh-mapper.md" >}}).

## Critical Limitation

This is very early-stage, hackathon-built software (built over a single weekend in May 2026) with minimal community vetting to date. It depends entirely on having a functioning passive-radar installation — siting a usable illuminator of opportunity and achieving coherent dual-channel reception is nontrivial RF engineering, unlike a plug-and-play Remote ID receiver. The verdict logic's ~80 m match radius and type/signature contradiction rules are simple heuristics rather than a rigorously validated classifier. It also cannot detect drones that never emit Remote ID at all and aren't otherwise visible to the radar — a real fiber-optic-tethered or RF-silent drone below the radar's detection threshold produces no verdict either way.

## Sources

- [phantom-proof (Fantom Finder) — GitHub](https://github.com/eldaeonuap/phantom-proof)
- [blah2 passive-radar pipeline — GitHub](https://github.com/30hours/blah2)
