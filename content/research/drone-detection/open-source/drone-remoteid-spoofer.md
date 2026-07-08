---
title: "droneRemoteIDSpoofer"
date: 2026-07-07
lastmod: 2026-07-07
draft: false
description: "Open-source WiFi/BLE Remote ID spoofer from the Swiss Cyber-Defence Campus that crafts and transmits fake ASTM F3411 drone broadcasts, demonstrating the protocol's lack of authentication."
research_area: "drone-detection/open-source"
source_urls:
  - "https://github.com/cyber-defence-campus/droneRemoteIDSpoofer"
  - "https://github.com/cyber-defence-campus/RemoteIDReceiver"
last_reviewed: 2026-07-07
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

droneRemoteIDSpoofer is an open-source Python tool from the Swiss Cyber-Defence Campus (built as a Zurich University of Applied Sciences thesis project) that crafts and transmits spoofed ASTM F3411 Remote ID packets over WiFi beacon frames and/or Bluetooth Low Energy advertisements. It demonstrates directly what [Phantom-Proof]({{< relref "phantom-proof.md" >}}) exists to defend against: Remote ID has no authentication or cryptographic integrity, so any receiver — OpenDroneID apps, DroneTag, DJI AeroScope, or custom monitoring systems — accepts a well-formed spoofed broadcast as genuine. **Limitation:** this is a research/testing tool, not a detection system — it generates fake drones, it does not find real ones.

## Key Facts

- **Authors:** Fabia Müller and Sebastian Brunner (Zurich University of Applied Sciences), Llorenç Romá (Cyber-Defence Campus)
- **Type:** Open-source software (proof-of-concept / security research tool)
- **License:** MIT
- **Status:** Active; 125 GitHub stars, 25 forks
- **Language:** Python (99.7%), using `scapy` for WiFi frame injection
- **Hardware:** Any 802.11 adapter supporting monitor mode (WiFi transport); any Bluetooth HCI adapter (BLE transport); Linux + root required for both

## How It Works

Each cycle, the spoofer builds four ASTM F3411 message payloads per fake drone — Basic ID, Location, System, and Operator ID — identical across transports, then hands them to WiFi and/or BLE backends. The WiFi backend wraps them in 802.11 beacon frames via `scapy`; the BLE backend wraps them in raw `ADV_NONCONN_IND` advertisements over the HCI socket. It supports spoofing a single drone, a "swarm" of several drones simultaneously (each with its own serial, MAC address, and flight behavior), and three flight modes: random walk, static position, or predefined waypoint paths. Scenarios are defined in JSON (ten-plus ready-made examples are included, from a simple single random drone to a 20-drone stress test to a simulated airport incursion), and a manual mode lets an operator fly a fake drone in real time with WASD keys.

## What Can Be Built With This

For testing or validating a Remote ID receiver or monitoring system:
1. Put a WiFi adapter in monitor mode and/or bring up a Bluetooth HCI adapter
2. Run `spoof_drones.py` with a built-in scenario, a custom JSON scenario, or CLI flags for a quick single/swarm spoof
3. Point any Remote ID receiver under test at it — e.g. [OpenDroneID]({{< relref "opendroneid.md" >}}), [Mesh-Mapper]({{< relref "mesh-mapper.md" >}}), or the authors' own companion [RemoteIDReceiver](https://github.com/cyber-defence-campus/RemoteIDReceiver) — to verify it correctly displays (or fails to distinguish) the fake traffic
4. Use the stress-test and airport-incursion scenarios to check receiver capacity and behavior under adversarial conditions

This is the natural counterpart to [Phantom-Proof]({{< relref "phantom-proof.md" >}}), whose passive-radar verification approach was built specifically to catch exactly this kind of spoofed broadcast — Phantom-Proof's own README credits this project as its spoofer reference.

## Related Hardware

The WiFi transport needs an 802.11 adapter capable of both monitor mode and raw frame injection — not every chipset supports this cleanly:

- **[RTL8812AU](https://github.com/aircrack-ng/rtl8812au)** — the default choice for this kind of work: dual-band (2.4/5 GHz), maintained by the aircrack-ng project, extensive community documentation. Requires DKMS and sometimes a rebuild after kernel updates.
- **[MT7612U](https://wireless.wiki.kernel.org/en/users/drivers/mt76)** (MediaTek, `mt76x2u` driver) — mainlined into the Linux kernel since 4.19, so no external driver compilation on most distros. Dual-band with clean `nl80211` support; increasingly preferred over the Realtek chip because it survives kernel updates without a rebuild.
- **[Nexmon](https://github.com/seemoo-lab/nexmon)** (SEEMOO Lab, TU Darmstadt) — a firmware-patching framework that unlocks monitor mode and injection on Raspberry Pi's own onboard Broadcom chips (BCM43430 on Pi 3, BCM43455 on Pi 4/Zero 2 W, and Pi 5's chip), removing the need for a USB adapter. Kali Linux's 2026 releases ship Nexmon-based support for Pi 3/4/5. This is a patched/unofficial firmware path rather than vendor-supported, and range/reliability trail a USB adapter with an external antenna.

On the microcontroller side, an ESP32 doesn't need monitor mode or an `nl80211` driver at all — its WiFi stack exposes raw 802.11 frame transmission directly via `esp_wifi_80211_tx()`. This is the injection mechanism used by ESP32-based Remote ID tools in this section (e.g. [Mesh-Mapper]({{< relref "mesh-mapper.md" >}})'s firmware) and is a lighter-weight alternative to a Linux host + injection-capable adapter if the goal is specifically to transmit Remote ID frames rather than run a general SDR/WiFi toolkit.

## Related Projects — Development Thread

This entry sits in the middle of a logical attack/defense progression documented in this section:

1. **[OpenDroneID]({{< relref "opendroneid.md" >}})** — the open standard and reference decode/encode library that everything downstream builds on.
2. **Detection tools** — [Mesh-Mapper]({{< relref "mesh-mapper.md" >}}), [DragonSync]({{< relref "dragonsync.md" >}}), and [iNTERCEPT]({{< relref "intercept.md" >}}) all receive and display Remote ID broadcasts, trusting them at face value.
3. **droneRemoteIDSpoofer (this entry)** — demonstrates that trust is misplaced: crafts fake broadcasts that every tool in step 2 will display as real drones.
4. **[Phantom-Proof]({{< relref "phantom-proof.md" >}})** — the answer to step 3: cross-verifies Remote ID claims against independent passive-radar tracks so spoofed broadcasts can be flagged rather than trusted. Its own README credits this project as the spoofer it was built to defend against.
5. **[RemoteIDReceiver](https://github.com/cyber-defence-campus/RemoteIDReceiver)** — the companion receiver from the same Cyber-Defence Campus team, built specifically to be tested against this spoofer (not yet a standalone entry in this section).

## Critical Limitation

This is explicitly a proof-of-concept research tool built for a university thesis, not hardened operational software — the authors disclaim responsibility for misuse and note it is intended for academic and security-research purposes only. It also only demonstrates the WiFi/BLE Remote ID attack surface; it says nothing about the security (or lack thereof) of DJI's proprietary DroneID protocol or other non-standard broadcast schemes.

## Sources

- [droneRemoteIDSpoofer — GitHub](https://github.com/cyber-defence-campus/droneRemoteIDSpoofer)
- [RemoteIDReceiver (companion receiver) — GitHub](https://github.com/cyber-defence-campus/RemoteIDReceiver)
