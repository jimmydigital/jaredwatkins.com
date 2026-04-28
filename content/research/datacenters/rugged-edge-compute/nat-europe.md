---
title: "N.A.T. GmbH (NAT Europe)"
date: 2026-04-25
lastmod: 2026-04-25
draft: false
description: "Hennef, Germany-based MicroTCA Carrier Hub (MCH) specialist with the NAT-MCH product line; primary MCH supplier for European physics accelerator and 5G RAN timing applications."
tags: ["microtca", "mch", "picmg", "embedded-compute", "telecom", "scientific", "defense", "europe", "timing"]
categories: ["company"]
research_area: "datacenters/rugged-edge-compute"
source_urls:
  - "https://nateurope.com/product/nat-mch/"
  - "https://nateurope.com/products/"
  - "https://nateurope.com/microtca-0-revision-3-released/"
  - "https://nateurope.com/ieee-quantum-week-2024/"
  - "https://www.picmg.org/spec-product/nat-microtca-carrier-hub-mch-gen3/"
last_reviewed: 2026-04-25
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

N.A.T. GmbH (trading as NAT Europe) is a Hennef, Germany-based specialist in MicroTCA Carrier Hub (MCH) design. The NAT-MCH product line is the reference MCH for European particle accelerator control systems (CERN, DESY, PSI) and has expanded to 5G RAN timing, defense, and quantum computing control infrastructure. Their 4th-generation NAT-MCH-G4 family (announced 2023–2024) introduces PCIe Gen 4/5 fat pipe, 100 GbE optical uplinks, and enhanced GPS/PTP/SyncE clocking — the most capable AMC-form MCH announced as of mid-2024.

## Key Facts

- **HQ:** Hennef, Germany
- **Type:** Private company
- **Core product:** NAT-MCH — MicroTCA Carrier Hub in single-width or double-width, mid- or full-size AMC form factor
- **Supported standards:** MTCA.0, MTCA.4; NAT-MCH-G4 supports MTCA.0 Rev 3.0
- **Key markets:** High-energy physics (accelerator LLRF control), 5G RAN timing and fronthaul, defense/aerospace, medical, industrial
- **Chassis slot support:** Up to 12 AMC modules (13 in non-redundant configuration); up to 2 Cooling Units, up to 4 Power Modules
- **Status:** Active; NAT-MCH-G4 announced 2023–2024; IEEE Quantum Week 2024 participation

## What It Is / How It Works

The NAT-MCH is the central switching and management resource in a MicroTCA system. Physically, it occupies one or two AMC slots in the MCH positions of the chassis (rather than the payload AMC positions). It provides:

1. **Fabric switching:** Base fabric (Ethernet) and fat pipe (PCIe or 100 GbE) switching between all AMC slots via the backplane. The NAT-MCH-G4 supports 10 GbE base fabric, 40 GbE fat pipe, and PCIe Gen 4/5 fat pipe options.
2. **Clocking and timing:** GPS receiver input, IEEE 1588 PTP (Precision Time Protocol), and SyncE (Synchronous Ethernet). This built-in timing distribution is critical for 5G RAN synchronization (where each baseband unit needs sub-microsecond accuracy) and accelerator RF control systems (where timing jitter directly impacts beam quality).
3. **System management:** IPMI-compliant shelf management; power and cooling unit monitoring; AMC module inventory and health; e-keying to prevent incompatible modules from powering up.

### Modular Architecture

NAT-MCH is built on a base module with optional daughter cards — enabling customers to configure timing, uplink, and fabric options without replacing the whole MCH. Uplink options span copper (GigE/10 GbE) and fiber (100 GbE optical) for base fabric, and PCIe x16 optical for fat pipe — enabling rack-scale and cross-chassis connectivity at speeds not previously achievable in MicroTCA.

### Physics Accelerator Heritage

N.A.T.'s MCH is the standard choice for the XTCA for Physics community — a working group of accelerator labs (DESY Hamburg, CERN Geneva, SLAC Menlo Park, BNL Brookhaven, PSI Villigen) that co-developed MTCA.4 with PICMG specifically for LLRF control. Physics labs need: many analog I/O channels (RTM rear modules), deterministic low-latency processing, precision timing (sub-nanosecond synchronization between rack-distributed nodes), and carrier-grade reliability. NAT-MCH is present at major free-electron laser (FLASH, European XFEL), synchrotron (PETRA IV), and linear accelerator (E-XFEL) facilities.

### NAT-MCH-G4 Key Features

- 10 GbE base fabric (up from 1/10 GbE mix in prior generation)
- 40 GbE or PCIe Gen 4/5 fat pipe per slot
- 100 GbE optical uplinks (copper and fiber)
- Enhanced GPS/PTP/SyncE timing with improved accuracy
- Fully compliant with MTCA.0 Revision 3.0 (September 2023)

## Notable Developments

- **2023-2024:** NAT-MCH-G4 family announced with MTCA.0 Rev 3.0 compliance — significant upgrade in clocking, switching, and uplink capability over G3 generation.
- **2024-09:** N.A.T. GmbH participated in IEEE International Conference on Quantum Computing and Engineering (QCE 2024) — presenting MicroTCA for quantum control system infrastructure; an emerging use case alongside accelerator LLRF systems.
- **2023-09:** PICMG ratified MTCA.0 Rev 3.0; N.A.T. published compatibility notes for NAT-MCH-G4, confirming it supports 100 GbE and PCIe Gen 5 fabric as specified in the new revision.
- **Ongoing:** NAT-MCH deployed in PETRA IV upgrade at DESY (Hamburg) — one of the world's most advanced synchrotron radiation sources; MicroTCA.4 used for entire machine control hierarchy.

## Key People

<!-- N.A.T. GmbH executives and LinkedIn profiles not confirmed in public sources at time of writing -->
<!-- TODO: Research NAT Europe leadership team at nateurope.com/about -->

### People — Last Reviewed: 2026-04-25

## Sources

- [NAT-MCH Product Page](https://nateurope.com/product/nat-mch/) — official product overview
- [NAT Europe Products](https://nateurope.com/products/) — full product catalog including chassis
- [NAT Europe: MTCA.0 Rev 3 Released](https://nateurope.com/microtca-0-revision-3-released/) — G4 compatibility notes
- [NAT Europe: IEEE Quantum Week 2024](https://nateurope.com/ieee-quantum-week-2024/) — quantum control infrastructure application
- [PICMG: NAT-MCH Gen3 Product Listing](https://www.picmg.org/spec-product/nat-microtca-carrier-hub-mch-gen3/) — PICMG-certified listing
