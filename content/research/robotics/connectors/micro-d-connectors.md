---
title: "Micro-D / Nano-D Connectors (MIL-DTL-83513)"
date: 2026-07-14
lastmod: 2026-07-14
draft: false
description: "Micro-miniature rectangular connector standard (MIL-DTL-83513) used throughout defense UAS, robotics, and space electronics, plus its higher-density Nano-D derivative."
research_area: "robotics/connectors"
source_urls:
  - "https://www.omnetics.com/products/micro-d/"
  - "https://www.omnetics.com/about/"
  - "https://www.molex.com/en-us/products/connectors/d-shaped-connectors/airborn-m-series-mil-dtl-83513-micro-d-connectors"
  - "https://www.ittcannon.com/mil-dtl-83513-series-micro-d-connectors"
  - "https://www.unmannedsystemstechnology.com/feature/nicomatics-lightweight-interconnect-solutions-for-uav-electronic-systems/"
last_reviewed: 2026-07-14
stale_after_days: 365
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Micro-D (per MIL-DTL-83513) is a rectangular, subminiature, high-reliability connector family standardized for military, aerospace, and space electronics, with a smaller Nano-D derivative (proprietary, not yet a full mil-spec). Both are foundational, low-level components in drone flight controllers, robot joint modules, and satellite/space avionics wherever board space and weight are tightly constrained.

## Key Facts

- Standard: MIL-DTL-83513 (Micro-D); Nano-D is a proprietary miniaturization below Micro-D, not separately mil-spec standardized
- Type: Connector standard / technology
- Status: Active, in continuous production since the standard's introduction; widely QPL (Qualified Products List) qualified
- Contact pitch: Micro-D at .050" (1.27 mm) centerlines; Nano-D at .025" (.64 mm) centerlines
- Contact system: Beryllium copper spring pin-to-socket contacts, nickel-and-gold plated for low contact resistance
- Pin counts: Micro-D typically 9 through 51+ positions; Nano-D higher density in a smaller footprint
- Key manufacturers: Omnetics, Positronic (Amphenol), ITT Cannon (Amphenol), AirBorn (Molex M Series), Nicomatic (DMM series, exceeds MIL-DTL-83513G performance)

## What It Is / How It Works

Micro-D connectors are two-row rectangular connectors using precision beryllium copper spring contacts arranged on a 1.27 mm grid, housed in a lightweight metal shell with jackscrew or latching hardware for secure mating under vibration. The beryllium copper contact material is chosen for its combination of high electrical/thermal conductivity, spring elasticity (so the contact retains mating force over thousands of cycles), and resistance to fatigue under shock and vibration — properties ordinary copper alloys lack. Contacts are typically plated with nickel (for corrosion resistance and as a diffusion barrier) followed by gold (for low, stable contact resistance).

MIL-DTL-83513 defines shell sizes, contact arrangements, and qualification testing (shock, vibration, temperature cycling, salt fog, and mating-cycle durability) that a connector must pass to be QPL-listed. Manufacturers producing to this standard include configuration variants: standard (jackscrew), latching (tool-free quick-latch), single-row (lower profile for space-constrained modules), low-profile (reduced flange height/weight), and specialty versions for high-temperature or deep-space (NASA low-outgassing) applications. Mounting styles range from free-hanging cable connectors to surface-mount, through-hole, and flex-circuit-mount board connectors.

Nano-D is a further miniaturization developed primarily by Omnetics, halving the pitch to .025" (.64 mm) to pack roughly four times the contact density into the same footprint as Micro-D, at the cost of lower per-contact current rating. It is not itself a MIL-DTL standard but is used alongside Micro-D in the same defense, aerospace, and space applications where the extra density is worth the tighter manufacturing tolerances.

Related and derivative product families extend the Micro-D/Nano-D concept: "Power Micro-D" variants add higher-current power contacts alongside signal pins in the same shell; Nicomatic's DMM connector line claims up to 40% weight reduction versus standard Micro-D while exceeding MIL-DTL-83513G performance and adding "mate-before-lock" mechanical protection.

## Notable Developments

- **2022–2025:** Nicomatic expands its DMM/CMM/EMM rugged micro connector lines and introduces the Matr'YX high-speed (up to 25 Gbps PAM-4) connector for defense/aerospace applications exceeding Micro-D-class density.
- **Ongoing:** Omnetics continues to expand Micro-D and Nano-D COTS catalog offerings (122 Micro-D and 155 Nano-D product variants listed on its site as of 2025), alongside power/signal hybrid and high-speed (USB 3.0-class) Micro-D variants.

## Claim Verification

### Claim: Nicomatic DMM connectors are "up to 40% lighter than standard Micro-D connectors while meeting or exceeding MIL standards"
**Status:** Partially verified

**Supporting sources:**
- [Nicomatic's Lightweight Interconnect Solutions for UAV Electronic Systems](https://www.unmannedsystemstechnology.com/feature/nicomatics-lightweight-interconnect-solutions-for-uav-electronic-systems/) — Nicomatic-authored feature article states the 40% weight-reduction figure and MIL-standard compliance claim.

**Refuting / questioning sources:**
- None found; this is a manufacturer-published figure carried by a trade publication (Unmanned Systems Technology) rather than independently tested. No independent third-party benchmark of DMM vs. standard Micro-D weight was located.

**Summary:** The 40% figure traces to a manufacturer feature article rather than an independent test; treat as a vendor claim pending independent verification.

## Sources

- [Micro-D - Omnetics Connector Corp.](https://www.omnetics.com/products/micro-d/) — product line detail, MIL-DTL-83513 QPL qualification, contact system description
- [About - Omnetics Connector Corp.](https://www.omnetics.com/about/) — Micro (1.27mm)/Nano (.64mm) pitch definitions, MIL-DTL-32139/83513 QPL approval
- [AirBorn M Series MIL-DTL-83513 Micro-D Connectors | Molex](https://www.molex.com/en-us/products/connectors/d-shaped-connectors/airborn-m-series-mil-dtl-83513-micro-d-connectors) — alternate manufacturer of MIL-DTL-83513 compliant connectors
- [MIL-DTL-83513 Series Micro-D Connectors | ITT Cannon](https://www.ittcannon.com/mil-dtl-83513-series-micro-d-connectors) — alternate manufacturer (Amphenol/ITT Cannon)
- [Nicomatic's Lightweight Interconnect Solutions for UAV Electronic Systems](https://www.unmannedsystemstechnology.com/feature/nicomatics-lightweight-interconnect-solutions-for-uav-electronic-systems/) — DMM/CMM/EMM connector family, weight and performance claims
