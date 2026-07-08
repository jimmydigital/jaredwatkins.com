---
title: "International Remote ID Requirements"
date: 2026-07-07
lastmod: 2026-07-07
draft: false
description: "Comparison of drone Remote ID / remote identification mandates across the UK, EU, China, and Japan — timelines, technical scope, and how each regime differs from the US FAA Remote ID rule."
research_area: "drone-detection"
source_urls:
  - "https://www.caa.co.uk/drones/moving-on-to-more-advanced-flying/remote-id-rid/"
  - "https://www.heliguy.com/blogs/posts/remote-id-what-it-means-for-uk-drone-pilots/"
  - "https://www.airhub.app/resources/news/remote-id-easa-vs-uk-2026"
  - "https://www.elsight.com/blog/primer-on-easa-remote-id-regulations/"
  - "https://lowaltitudeeconomy.aero/evtol-news-and-electric-aircraft-news/cargo-drones/china-drone-identification-standards-2026"
  - "https://www.sixthtone.com/news/1017964/china-mandates-registration%2C-real-time-tracking-for-civilian-drones"
  - "https://www.flyeye.io/japan-drone-laws/"
last_reviewed: 2026-07-07
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Remote ID-style broadcast identification for drones is rapidly becoming a global norm, not a US-specific requirement. The UK, EU, China, and Japan have each adopted their own mandates — largely aligned in concept (drones broadcast identity, position, and operator information) but differing meaningfully in technical scope, timeline, and enforcement mechanism. This matters for this section's tooling: most open-source Remote ID software here (see [OpenDroneID]({{< relref "open-source/opendroneid.md" >}})) targets ASTM F3411, the standard shared by the US, UK, and EU — but is not sufficient on its own for China's dual broadcast-plus-network mandate. **Limitation:** regulatory detail below is a snapshot as of mid-2026; several regimes (UK, China) are still in active phase-in.

## Key Facts

- **Shared technical baseline (US/UK/EU):** ASTM F3411 broadcast Remote ID over WiFi NAN/BLE — see [OpenDroneID]({{< relref "open-source/opendroneid.md" >}}) for the reference implementation
- **Outlier:** China requires simultaneous broadcast-mode *and* network-mode (internet-routed) identification — a materially different and more centralized architecture
- **EU alone** layers a second system, "Network Remote ID," required only inside designated U-space airspace zones (EU Regulation 2021/664)
- **Fastest-moving deadlines:** UK (2026–2028 phase-in), China (May 2026 standards, June 2027 retrofit deadline)

## Country-by-Country Comparison

### United Kingdom

The UK Civil Aviation Authority (CAA) is phasing in **Direct Remote ID** as both a product and an operational requirement, treated as legally distinct from "Electronic Conspicuity" (ADS-B-style manned/unmanned traffic-awareness systems), even though both involve a drone emitting identifying signals.

- From **January 1, 2026:** Direct Remote ID becomes a product requirement for any newly placed-on-market UK class-marked UAS (classes UK1, UK2, UK3, UK5, UK6)
- From **January 1, 2028:** Remote ID becomes an operational requirement for essentially all drone and model aircraft flights, absent a CAA exemption
- The UK's approach broadly mirrors the US/EU ASTM F3411 broadcast model rather than China's network-mandatory approach

### European Union (EASA)

The EU is furthest along of the four. **Direct Remote ID has been mandatory since January 1, 2024** for drones in classes C1, C2, and C3 operating in the Open category, with narrow exemptions for sub-250g C0 drones, C4 model aircraft, and some tethered C3 operations meeting specific technical conditions.

The EU additionally operates **Network Remote ID** under the U-space framework (Implementing Regulation (EU) 2021/664) — a digital UTM (Unmanned Traffic Management) system. Network Remote ID routes drone identification over the internet to centralized service providers rather than only broadcasting locally, enabling longer-range tracking and integration with air traffic management. It is mandatory only inside designated U-space airspace, which individual EU member states activate as needed — it is not a blanket requirement like Direct Remote ID.

### China

China's approach is the most centralized and technically distinct. Two mandatory national standards — **GB 46761-2025** (real-name registration and activation) and **GB 46750-2025** (real-time operational identification) — take effect **May 1, 2026**.

Unlike the US/UK/EU broadcast-only model, Chinese civil drones must carry **both** broadcast-mode identification (local, ADS-B-like, received by proximate ground equipment without a network connection) **and** network-mode identification (routed via cellular, wired, or satellite communications to the CAAC's centralized monitoring infrastructure) simultaneously. New production drones must comply from May 1, 2026; drones already sold and in use have until approximately **June 2027** (13 months after the standard takes effect) to complete back-registration and activation. China's revised Civil Aviation Law, effective July 1, 2026, elevates this framework to statutory law.

### Japan

Japan's requirement is narrower in scope: registered drones must carry a visible registration ID and, where equipped, broadcast Remote ID information via radio while flying. Japan has not (as of this review) adopted a network-mode requirement comparable to the EU's U-space system or China's dual-mode mandate.

## Implications for This Section's Tooling

- Open-source WiFi/BLE Remote ID tools built against ASTM F3411 ([OpenDroneID]({{< relref "open-source/opendroneid.md" >}}), [Mesh-Mapper]({{< relref "open-source/mesh-mapper.md" >}}), [DragonSync]({{< relref "open-source/dragonsync.md" >}})) should be broadly portable across US, UK, and EU airspace without modification, since all three jurisdictions converge on the same broadcast standard.
- None of the broadcast-only tools in this section would fully satisfy China's network-mode requirement, which depends on a centralized CAAC backend rather than local broadcast reception.
- The protocol-level vulnerability documented in [droneRemoteIDSpoofer]({{< relref "open-source/drone-remoteid-spoofer.md" >}}) and defended against by [Phantom-Proof]({{< relref "open-source/phantom-proof.md" >}}) — unauthenticated broadcast, spoofable by any transmitter — applies equally to the UK and EU's ASTM F3411 deployments, since it is the same underlying standard.
- Unlike the [US federal detect-vs-interdict framework]({{< relref "regulatory-framework.md" >}}), none of the international sources reviewed here address interdiction authority — they cover identification/broadcast mandates only, not who may jam, take over, or destroy a drone.

## Notable Developments

- **2026-07:** Sixth Tone and Low Altitude Economy report on China's GB 46761-2025 / GB 46750-2025 standards taking effect May 1, 2026, with June 2027 retrofit deadline for existing drones
- **2026-01:** UK CAA begins phase-in of Direct Remote ID as a product requirement for new class-marked UAS
- **2024-01:** EU EASA Direct Remote ID becomes mandatory for C1/C2/C3 Open category drones

## Sources

- [Remote ID (RID) — UK Civil Aviation Authority](https://www.caa.co.uk/drones/moving-on-to-more-advanced-flying/remote-id-rid/)
- [Remote ID 2026: What it means for UK drone pilots — Heliguy](https://www.heliguy.com/blogs/posts/remote-id-what-it-means-for-uk-drone-pilots/)
- [Remote ID Regulations Explained: EASA vs UK Rules from 2026 — AirHub](https://www.airhub.app/resources/news/remote-id-easa-vs-uk-2026)
- [EASA Remote ID Requirements: Compliance for Drone Operators — Elsight](https://www.elsight.com/blog/primer-on-easa-remote-id-regulations/)
- [Every Drone in China Goes Dark on May 1 Unless Its Owner Registers — Low Altitude Economy](https://lowaltitudeeconomy.aero/evtol-news-and-electric-aircraft-news/cargo-drones/china-drone-identification-standards-2026)
- [China Mandates Registration, Real-Time Tracking for Civilian Drones — Sixth Tone](https://www.sixthtone.com/news/1017964/china-mandates-registration%2C-real-time-tracking-for-civilian-drones)
- [Japan Drone Laws (2026): Rules, Limits & Penalties — Fly Eye](https://www.flyeye.io/japan-drone-laws/)
