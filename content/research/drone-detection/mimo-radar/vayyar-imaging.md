---
title: "Vayyar Imaging"
date: 2026-07-17
lastmod: 2026-07-17
draft: false
description: "Israeli radar-on-chip maker; its XRR single-chip MIMO RFIC (48 transceivers, on-chip processing) delivers 4D imaging radar for automotive safety and is also marketed into public-safety/security screening — a dual-use MIMO chip platform with no confirmed drone-detection product, included here as adjacent enabling technology."
research_area: "drone-detection/mimo-radar"
source_urls:
  - "https://blog.vayyar.com/xrr-0-300-m-single-chip"
  - "https://vayyar.com/blog/automotive/vayyar-releases-worlds-first-mimo-single-chip-xrr-rfic"
  - "https://vayyar.com/public-safety/"
  - "https://vayyar.com/blog/vayyar/radar-applications-the-potential-of-4d-imaging/"
last_reviewed: 2026-07-17
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Vayyar Imaging (Israel) makes single-chip MIMO radar-on-chip (RFIC) products, most notably **XRR**, described as the world's first single-chip MIMO RFIC with 48 transceivers and on-chip processing. Vayyar's primary go-to-market is automotive 4D imaging radar (passenger cars, trucks, motorcycles) for safety applications, but the company also markets its 4D imaging-radar chips into public-safety and security-screening use cases, including perimeter and presence-detection scenarios for homes and smart buildings. No source reviewed here describes a Vayyar product specifically marketed for drone or counter-UAS detection — it is included in this subtopic as an example of the underlying MIMO radar-on-chip technology that could plausibly be adapted to a low-cost drone-detection sensor, similar in spirit to how [Uhnder]({{< relref "uhnder.md" >}}) is included as enabling technology rather than a fielded C-UAS product.

## Key Facts

- **HQ:** Israel (Yehud, with additional offices internationally)
- **Type:** Company — radar-on-chip (RFIC) semiconductor + reference design maker
- **Flagship chip:** XRR — single-chip MIMO RFIC with a 48-antenna MIMO array (transceivers) and on-chip signal processing
- **Architecture:** Traditional radar solutions typically use 2–3 transmit and 3–4 receive antennas; Vayyar's 4D imaging radar uses a much larger MIMO array (48 antennas in XRR) for higher-resolution mapping of surroundings
- **Primary market:** Automotive (passenger cars, trucks, motorcycles) — safety and driver-assistance applications
- **Secondary markets:** Public-safety and security screening (concealed-object detection); smart-home presence detection, perimeter monitoring, and health monitoring from a single sensor
- **Status:** Active; XRR positioned as a multi-range chip covering short- to long-range automotive use cases from one part

## How It Works

Vayyar's radar-on-chip integrates a large MIMO antenna array (transmit and receive elements each carrying distinguishable signals) plus signal processing directly on a single RFIC, rather than requiring a separate processing module — the "on-chip processing" claim in XRR's marketing. The larger antenna count (48 transceivers, versus the handful used in conventional automotive radar) synthesizes a bigger virtual aperture and correspondingly finer angular resolution, enabling "4D imaging" (range, azimuth, elevation, and velocity) sufficient to distinguish closely-spaced objects — Vayyar calls this High Contrast Resolution (HCR). The same underlying chip architecture is reused across Vayyar's automotive and public-safety/security product lines, with different reference designs and software layered on top for each application, rather than fundamentally different radar hardware per market.

## Notable Developments

- **XRR launch:** Vayyar announces the XRR chip as the world's first single-chip MIMO RFIC with 48 transceivers and on-chip processing, targeted at automotive multi-range imaging use cases
- No confirmed 2026-specific security or defense contract was found in this review; Vayyar's public-safety materials describe capability (concealed-object detection, perimeter/presence sensing) rather than named drone-detection deployments

## Limitations

- **No confirmed drone/C-UAS product:** This entry documents adjacent, enabling MIMO radar-on-chip technology, not a fielded or marketed counter-drone system — treat any drone-detection application as speculative/architectural rather than a current Vayyar offering
- **Automotive-first company:** Most of Vayyar's public technical detail, case studies, and third-party coverage concern automotive ADAS rather than security or defense use cases
- **Chip-level claims sourced from company blog/marketing:** Antenna counts and "world's first" framing come from Vayyar's own announcements; independent benchmarking against competing automotive-radar chipmakers was not found in this review

## Sources

- [Vayyar releases world's first MIMO single-chip "XRR" RFIC with 48 transceivers and on-chip processing — Vayyar Blog](https://blog.vayyar.com/xrr-0-300-m-single-chip)
- [Vayyar Releases World's 1st Single-chip "XRR" MIMO RFIC](https://vayyar.com/blog/automotive/vayyar-releases-worlds-first-mimo-single-chip-xrr-rfic)
- [Security Screening With Advanced 4D Imaging Radar — Vayyar](https://vayyar.com/public-safety/)
- [Radar Applications: The Potential of 4D Imaging — Vayyar](https://vayyar.com/blog/vayyar/radar-applications-the-potential-of-4d-imaging/)
