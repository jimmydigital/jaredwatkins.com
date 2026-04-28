---
title: "Annapolis Micro Systems"
date: 2026-04-25
lastmod: 2026-04-25
draft: false
description: "Annapolis, MD company specializing in FPGA-based rugged OpenVPX boards and chassis for high-performance signal processing in defense applications. Developer of the WILD100 EcoSystem for SOSA-aligned rugged compute."
tags: ["rugged", "fpga", "openvpx", "sosa", "defense", "liquid-cooling", "signal-processing", "us"]
categories: ["company"]
research_area: "datacenters/rugged-edge-compute"
source_urls:
  - "https://www.annapmicro.com/"
  - "https://www.annapmicro.com/annapolis-microsystems/cooling/"
  - "https://www.annapmicro.com/products/wc34d0/"
  - "https://militaryembedded.com/radar-ew/signal-processing/product-of-the-week-annapolis-microsystems-3u-vpx-switches-and-chassis"
last_reviewed: 2026-04-25
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Annapolis Micro Systems is an Annapolis, Maryland company specializing in FPGA-based rugged OpenVPX boards and chassis for defense signal processing and high-performance data acquisition. The company's WILD100 EcoSystem provides a complete, SOSA-aligned portfolio of rugged 3U and 6U OpenVPX boards, backplanes, and chassis — including a liquid-cooled (VITA 48.4 LFT) 3U chassis. Annapolis is positioned as a specialist component/subsystem supplier to defense primes and government labs requiring FPGA-accelerated DSP at the signal processing front end.

## Key Facts

- **Founded:** 1992
- **Headquarters:** Annapolis, Maryland, USA
- **Type:** Private
- **Status:** Active
- **Key product line:** WILD100 EcoSystem — SOSA-aligned OpenVPX boards, chassis, and chassis managers
- **Core technology:** FPGA-based signal processing (Xilinx/AMD UltraScale+, Versal); multi-cooling-mode chassis
- **Target markets:** Defense SIGINT, EW, radar, sonar; high-performance data acquisition; scientific instrumentation

## What It Is / How It Works

Annapolis occupies the component/subsystem tier of the rugged compute stack — it designs and builds the FPGA compute cards and chassis that defense primes and system integrators slot into their platforms. Unlike Mercury Systems or One Stop Systems (which integrate boards into complete, qualified systems), Annapolis sells primarily to engineers who will integrate WILD100 boards into their own chassis or use Annapolis chassis as the integration base.

**WILD100 EcoSystem**

WILD100 is the product family branding for Annapolis's SOSA-aligned 3U OpenVPX portfolio. Key components:

- **FPGA payload boards:** AMD/Xilinx UltraScale+ and Versal-based 3U VPX cards; supports all VITA 48.x cooling modes (conduction, AFT, LFT)
- **Chassis:** Multiple chassis variants including conduction-cooled ATR, air-cooled 19" rackmount, and the WC34D0 liquid-cooled variant
- **Chassis Manager:** VITA 46.11-compliant; Xilinx UltraScale+ ZU11EG MPSoC; VITA 91 high-density connector support
- **100 GbE fabric:** Full non-blocking switched backplane; all slots on same switch fabric via VITA 91 connectors

**WC34D0 Liquid-Cooled 3U Chassis**

The WILD100 WC34D0 is the most distinctive product in the lineup for dense AI and DSP:
- **Type:** Rugged COTS 3U OpenVPX chassis with VITA 48.4 Liquid Flow-Through cooling
- **Slots:** 8 payload (conduction-cooled LFT modules), 2 HD switches, 1 radial clock, 2 VITA 62 PSUs — 13 total
- **Fabric:** 100 GbE switched; VITA 91 high-density connectors enabling non-blocking backplane
- **PCIe:** 8× or 4× Gen4 PCIe per slot; 8× LVDS or dual 100 GbE per slot
- **Cooling interface:** VITA 48.4 quick-disconnect couplings; compatible with PAO, glycol/water, or other coolants
- **Chassis Manager:** Xilinx UltraScale+ ZU11EG MPSoC-based; VITA 46.11 compliant

**Cooling Approach**

Annapolis supports multiple VITA 48.x modes across its product range:
- Conduction cooling: standard for many ATR applications; cold plate integration via chassis sidewalls
- Air Flow-Through (AFT/VITA 48.8): where airflow is available and 100–200 W per slot is sufficient
- Liquid Flow-Through (VITA 48.4): the WC34D0 chassis; for 200 W+ per-slot requirements

The company publishes detailed guidance distinguishing these three cooling modes and their application contexts.

## Notable Developments

- **2024–2025:** WC34D0 liquid-cooled 3U chassis available with full SOSA alignment and VITA 91 high-density connectors — represents the company's highest-density compute chassis
- **2023:** 3U VPX ATR and 19" rackmount chassis added to WILD100 family
- **Ongoing:** SOSA Technical Standard alignment across full portfolio; 100 GbE fabric integration as primary differentiator vs. competitors using older 1/10 GbE fabrics

## Key People

- <!-- TODO: verify current CEO and engineering leadership; LinkedIn profiles not confirmed -->

### People — Last Reviewed: 2026-04-25

## Sources

- [Annapolis Micro Systems Corporate Website](https://www.annapmicro.com/)
- [WILD100 Cooling Approaches](https://www.annapmicro.com/annapolis-microsystems/cooling/) — Conduction, AFT, LFT overview
- [WC34D0 Liquid-Cooled 3U OpenVPX Chassis](https://www.annapmicro.com/products/wc34d0/) — Chassis specs
- [Military Embedded Systems Product of the Week Coverage](https://militaryembedded.com/radar-ew/signal-processing/product-of-the-week-annapolis-microsystems-3u-vpx-switches-and-chassis)
