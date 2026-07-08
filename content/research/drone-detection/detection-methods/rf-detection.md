---
title: "FAA Remote ID Monitoring"
date: 2026-06-05
lastmod: 2026-07-07
draft: false
description: "Reception and decoding of FAA/ASTM F3411 Remote ID broadcasts — the fastest path to identifying compliant US drones, but entirely dependent on the drone's voluntary cooperation. See RF Direction Finding for detection that doesn't require it."
research_area: "drone-detection/detection-methods"
source_urls:
  - "https://www.faa.gov/uas/getting_started/remote_id"
  - "https://advexure.com/blogs/news/top-5-remote-id-detection-systems"
  - "https://aerodefense.tech/airwarden-remote-id-receiver/"
  - "https://www.dronetag.com/products/bs"
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC10490811/"
last_reviewed: 2026-07-07
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

FAA Remote ID (ASTM F3411 / 14 CFR Part 89) requires US-registered drones manufactured after 2022 to broadcast identification telemetry — drone ID, position, altitude, velocity, and operator location — over WiFi NAN and Bluetooth 5 Long Range every second. Receiving and decoding these broadcasts is the fastest and cheapest path to identifying a compliant drone and its operator. **Critical distinction:** this is a fundamentally cooperative detection method — it works only because the drone chooses to broadcast. It provides zero coverage against non-compliant, modified, or RF-silent drones. For detection that doesn't depend on the drone's cooperation, see [RF Direction Finding]({{< relref "rf-direction-finding.md" >}}), which locates drones by their control-link and video-link emissions instead.

## Key Facts

- **Governing standard:** ASTM F3411-22a (equivalent to EUROCAE ED-269); 14 CFR Part 89 (US)
- **FAA Remote ID enforcement:** Active as of 2023; as of 2025 local law enforcement can use Remote ID apps to identify non-compliant operators
- **Broadcast protocols:** Wi-Fi NAN (802.11) and Bluetooth 5 Long Range
- **Detection range:** ~300 m–3.7 km depending on drone model, protocol, and environment
- **International adoption:** The US, UK, and EU all converge on this same ASTM F3411 broadcast standard — see [International Remote ID Requirements]({{< relref "../international-remote-id-requirements.md" >}}); China layers on an additional mandatory network-mode requirement not covered by broadcast-only receivers
- **Critical limitation:** Entirely dependent on the drone choosing to broadcast — no capability against non-compliant, spoofed, or RF-silent drones

## What It Is / How It Works

**FAA Remote ID** mandates that compliant drones broadcast identification messages including drone ID, takeoff location, current position, altitude, velocity, and operator location every second, using two mechanisms:

- **Broadcast Remote ID (BRI):** Direct RF broadcast from the drone (Wi-Fi NAN, Bluetooth 5 LR) — receivable with off-the-shelf hardware within ~300 m–3.7 km depending on protocol and environment
- **Network Remote ID:** Drone sends data to a USS (UAS Service Supplier) via cellular uplink — requires network access by the drone

Receivers built to the ASTM standard — [Dronetag BS and RIDER](https://www.dronetag.com/products/bs), AeroDefense AirWarden, and open-source stacks like [OpenDroneID]({{< relref "../open-source/opendroneid.md" >}}) — decode BRI and display operator identity, position, and flight path. This is the mechanism behind most of the open-source Remote ID tooling covered elsewhere in this section, including [Mesh-Mapper]({{< relref "../open-source/mesh-mapper.md" >}}) and [DragonSync]({{< relref "../open-source/dragonsync.md" >}}).

**Research-grade RF identification** work (Svanström et al., 2023) demonstrates decoding Remote ID telemetry from DJI drones at up to 3.7 km and reconstructing 2D position and altitude in real time from the encoded GPS data.

## Hardware Available Today

| Product | Vendor | Type | Range | Notes |
|---------|--------|------|-------|-------|
| AirWarden | AeroDefense | Remote ID receiver | ~300 m–1 km | Small form factor; low maintenance; FAA BRI compatible |
| Dronetag BS | Dronetag | Remote ID base station | ~3–5 km | Fixed outdoor receiver; feeds UTM/app |
| Dronetag RIDER | Dronetag | Portable Remote ID | ~3 mi radius | IP54; 6–10 hr battery; patrol use |
| AARTOS X9 | Aaronia AG | Passive RF + Remote ID | Up to 14 km | Also does non-cooperative RF triangulation — see [RF Direction Finding]({{< relref "rf-direction-finding.md" >}}) |

Several of the non-cooperative RF systems in [RF Direction Finding]({{< relref "rf-direction-finding.md" >}}) — notably Aaronia AARTOS and Tron Future T.Sensor — also decode Remote ID as an additional capability layered on top of their primary control-link detection.

## Why Cooperative Detection Is Not Enough

Remote ID's core weakness for critical infrastructure protection is that it only works if the drone operator complies:

- **Non-compliant or unregistered drones** simply don't broadcast — there is no enforcement mechanism at the receiver end
- **Spoofing:** Remote ID has no cryptographic authentication. Any transmitter can broadcast fabricated Remote ID claims that a receiver will display as genuine — see [droneRemoteIDSpoofer]({{< relref "../open-source/drone-remoteid-spoofer.md" >}}) for an open-source tool demonstrating this, and [Phantom-Proof]({{< relref "../open-source/phantom-proof.md" >}}) for a passive-radar approach to verifying broadcast claims against independent physical tracks
- **Fiber-optic tethered and pre-programmed autonomous drones** may or may not transmit Remote ID depending on compliance, but by definition have no RF *control* link — see [RF Direction Finding]({{< relref "rf-direction-finding.md" >}}) for why this defeats RF-based detection generally

Because of these gaps, Remote ID reception should be treated as one input among several — not a standalone detection layer — for any critical infrastructure deployment. See [Multi-Sensor Fusion]({{< relref "multi-sensor-fusion.md" >}}).

## Regulatory / Legal Context

Receiving and decoding Remote ID broadcasts is unambiguously legal for any entity — it is a public broadcast signal designed to be received. This is distinct from RF jamming or signal takeover, which remain restricted to authorized federal agencies under US law; see [Regulatory Framework]({{< relref "../regulatory-framework.md" >}}).

## Sources

- [FAA Remote ID overview](https://www.faa.gov/uas/getting_started/remote_id)
- [Top 5 Remote ID Detection Systems — Advexure 2025](https://advexure.com/blogs/news/top-5-remote-id-detection-systems)
- [AeroDefense AirWarden Remote ID Receiver](https://aerodefense.tech/airwarden-remote-id-receiver/)
- [Dronetag BS product](https://www.dronetag.com/products/bs)
- [Drone Detection and Tracking Using RF Identification Signals — PMC 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10490811/) — Remote ID decoding at 3.7 km
