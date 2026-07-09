---
title: "AERIS-10 (PLFM_RADAR)"
date: 2026-07-09
lastmod: 2026-07-09
draft: false
description: "Open-source, low-cost 10.5 GHz phased array Pulse Linear Frequency Modulated (PLFM) radar — full hardware (schematics, PCB layouts) and FPGA/firmware/software stack, in two range variants (3 km and 20 km); accepted by Crowd Supply for a Q3 2026 crowdfunding launch."
research_area: "drone-detection/open-source"
source_urls:
  - "https://github.com/NawfalMotii79/PLFM_RADAR"
  - "https://nawfalmotii79.github.io/PLFM_RADAR/docs/"
  - "https://hackaday.io/project/205190-open-source-plfm-radar-up-to-20km-range"
  - "https://hackaday.io/project/205190/log/246728-project-log-002-aeris-10-accepted-by-crowd-supply-the-journey-to-production-begins"
  - "https://www.crowdsupply.com/"
last_reviewed: 2026-07-09
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

AERIS-10 (repository name `PLFM_RADAR`) is an open-source, low-cost 10.5 GHz phased array radar using Pulse Linear Frequency Modulation (PLFM/chirp) — a genuinely different detection layer from every other open-source project in this section, which are almost all Remote ID receivers or RF control-link sniffers. Radar detects a physical target by reflected energy rather than any RF emission the drone chooses (or fails) to transmit, which is exactly the capability gap this section's steering doc flags for [fiber-optic tethered and RF-silent autonomous drones]({{< relref "../detection-methods/rf-direction-finding.md" >}}). The project ships complete hardware design files (schematics, PCB layouts, BOM, Gerbers) under CERN-OHL-P and complete firmware/software (FPGA VHDL/Verilog, STM32 firmware, Python GUI) under MIT. **Limitation:** the project is explicitly labeled "Alpha" status, is a from-scratch hardware build (PCB assembly, RF component sourcing, FPGA toolchain) rather than a plug-and-play sensor, and has no drone-specific classification (bird-vs-drone discrimination, protocol ID) built in — it outputs raw radar tracks, not a labeled threat picture.

## Key Facts

- **Author:** Nawfal Motii (GitHub `NawfalMotii79`)
- **Type:** Open-source hardware + software project (radar, not RF/Remote ID)
- **Status:** Active; Alpha; 7.6k GitHub stars, 1.6k forks, 149 watchers, 3 releases (latest v1.1.0-agc, April 2026), 240+ commits
- **Frequency:** 10.5 GHz (X-band)
- **Variants:** AERIS-10N "Nexus" (3 km range, 8×16 patch antenna array) and AERIS-10X "Extended" (20 km range, 32×16 dielectric-filled slotted waveguide array with 16× 10W GaN power amplifier boards)
- **Beam steering:** ±45° electronic steering in both elevation and azimuth via 4-channel phase shifters (ADAR1000); 360° mechanical scan via stepper motor
- **Processing:** Onboard FPGA (Xilinx XC7A50T) handles pulse compression, Doppler FFT, MTI (moving target indication), and CFAR (constant false alarm rate) detection
- **License:** Hardware under CERN Open Hardware Licence v2 – Permissive (CERN-OHL-P); firmware/software under MIT — split specifically because MIT lacked liability protections appropriate for high-power RF hardware
- **Commercialization:** Accepted by [Crowd Supply](https://www.crowdsupply.com/) (backed by Mouser Electronics) as of March 2026; targeting a Q3 2026 crowdfunding campaign launch with first deliveries in late 2026 — this would be the first path to a pre-assembled, purchasable unit rather than a from-scratch build

## How It Works

AERIS-10 is built around a DAC-generated PLFM (chirp) waveform, up-converted and radiated through a phased array whose element phases are set by four ADAR1000 4-channel phase shifters, giving electronic beam steering without moving parts (a mechanical stepper motor handles full 360° coverage). Returns are down-converted, digitized, and processed entirely onboard an FPGA: I/Q baseband down-conversion, decimation/filtering, pulse compression, Doppler FFT, MTI, and CFAR detection all run in the FPGA fabric before results reach an STM32 microcontroller (which also handles power sequencing, GPS/IMU-corrected positioning, and peripheral control) and finally a Python GUI with map integration for real-time target plotting.

The two-variant design is a direct range/power/cost tradeoff: AERIS-10N uses a compact 8×16 patch array at roughly 1W×16 output for a 3 km range, aimed at makers and researchers; AERIS-10X swaps in a 32×16 slotted waveguide array and 16 GaN power amplifier boards (10W each) to reach 20 km, a scale more relevant to fixed-site perimeter defense.

## What Can Be Built With This

For a critical infrastructure site that wants radar-layer detection — the primary detection modality this section's steering doc already recommends over RF — without a commercial radar vendor's price tag:

1. Order and assemble the PCBs from `/4_Schematics and Boards Layout/4_7_Production Files` (Gerbers, BOM, CPL co-located)
2. Build or acquire the target antenna array (patch array for AERIS-10N's 3 km class, or the slotted waveguide array plus GaN amplifier boards for AERIS-10X's 20 km class)
3. Flash the STM32 firmware and FPGA bitstream (Vivado toolchain required for FPGA modifications)
4. Run the Python GUI for live target plotting with map integration and GPS/IMU-corrected positioning

Because it outputs raw MTI/CFAR-detected tracks rather than a classified drone-vs-bird picture, this is best understood as a detection-layer building block to feed into a larger fusion pipeline — comparable in role to how [Echodyne]({{< relref "echodyne.md" >}}) radar is consumed as a component inside other vendors' C-UAS platforms — rather than a complete end-user C-UAS product on its own.

## Crowd Supply Launch

As of a March 17, 2026 project log on the creator's [Hackaday.io project page](https://hackaday.io/project/205190-open-source-plfm-radar-up-to-20km-range), AERIS-10 has been formally accepted by [Crowd Supply](https://www.crowdsupply.com/), an open-source-hardware crowdfunding platform backed by Mouser Electronics. Per the creator's announcement, this brings professional campaign management, fulfillment (picking/packing/shipping/support handled by Crowd Supply), free worldwide shipping for backers, and the possibility of post-campaign distribution through Mouser globally. The campaign is targeting a **Q3 2026 launch** with **first deliveries in late 2026**; a pre-launch signup page, campaign video, beta testing with selected partners, and FCC/CE regulatory certification were all in progress as of the announcement. This is a meaningful shift for accessibility: everything documented above (PCB assembly, RF component sourcing, FPGA toolchain) describes building AERIS-10 from the open-source design files, but a Crowd Supply campaign would offer a path to a pre-assembled or kitted unit for the first time.

The project's creator, Nawfal Motii, describes starting the project independently ("a guy in a workshop in Morocco with a soldering iron") before it grew into a six-person Hackaday.io project team and attracted outside interest — including an invitation to write for *Circuit Cellar* magazine and community proposals for cloud-connected radar networks and RF/ML-based automatic drone/bird classification, which would directly address the classifier gap noted below.

**Sourcing note:** The GitHub README lists the onboard FPGA as a Xilinx XC7A50T; the Hackaday.io project description instead lists an XC7A100T. This entry has not resolved which is current — treat the FPGA part number as unconfirmed pending a direct check of the latest schematics, and don't rely on either figure for a build without cross-checking the repository's current schematic files.

## Critical Limitation

The project is explicitly labeled Alpha, and building it requires real RF/PCB assembly work, an FPGA toolchain (Vivado), and sourcing specialized components (microwave mixers, phase shifters, GaN amplifiers) — a materially higher bar than flashing an ESP32 for a Remote ID receiver like [Mesh-Mapper]({{< relref "mesh-mapper.md" >}}). It has no built-in drone/bird classification or protocol identification: unlike this section's commercial micro-Doppler systems (see [Robin Radar IRIS]({{< relref "../hardware/robin-radar-iris.md" >}}) and [Fortem Technologies]({{< relref "../hardware/fortem-technologies.md" >}}), both of which market AI-based bird/drone discrimination as a core feature), AERIS-10 delivers CFAR-detected tracks that still require a downstream classifier to reliably distinguish a drone from a bird or other clutter. As with any radar, it also requires legal/regulatory awareness around intentional RF emission (unlike the purely passive/receive-only tools elsewhere in this section) — operators should confirm compliance with local spectrum authorization requirements before transmitting at 10.5 GHz.

## Sources

- [PLFM_RADAR (AERIS-10) — GitHub](https://github.com/NawfalMotii79/PLFM_RADAR)
- [AERIS-10 documentation — GitHub Pages](https://nawfalmotii79.github.io/PLFM_RADAR/docs/)
- [Open Source PLFM RADAR project — Hackaday.io](https://hackaday.io/project/205190-open-source-plfm-radar-up-to-20km-range)
- [Project Log #002: AERIS-10 Accepted by Crowd Supply — Hackaday.io](https://hackaday.io/project/205190/log/246728-project-log-002-aeris-10-accepted-by-crowd-supply-the-journey-to-production-begins)
- [Crowd Supply](https://www.crowdsupply.com/)
