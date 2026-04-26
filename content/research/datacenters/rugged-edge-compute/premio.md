---
title: "Premio"
date: 2026-04-25
lastmod: 2026-04-25
draft: false
description: "San Jose, CA rugged industrial computing manufacturer; JCO Series (JCO-6000-ORN, JCO-3000-ORN) NVIDIA Jetson Orin NX/AGX fanless AI edge systems; RCO Series rackmount rugged servers with EDGEBoost I/O expansion technology; MIL-STD-810H and E-Mark certified platforms for defense, transportation, and industrial AI."
tags: ["rugged", "edge-compute", "ai-inference", "industrial", "us", "private", "fanless", "jetson", "gpu-edge"]
categories: ["company"]
research_area: "datacenters/rugged-edge-compute"
source_urls:
  - "https://premioinc.com/"
  - "https://premioinc.com/collections/rugged-edge-ai-computers"
last_reviewed: 2026-04-25
stale_after_days: 180
---

## Summary

Premio is a San Jose, California-based designer and manufacturer of rugged industrial computing platforms for edge AI, IoT, and industrial automation applications. The company occupies the semi-industrial and light-mil-spec tier of rugged compute: fanless enclosures, wide-temperature operation, and MIL-STD-810H vibration/shock qualification for transportation, defense-adjacent, and industrial markets. Premio's JCO Series (NVIDIA Jetson Orin NX/AGX Orin based) and RCO Series (Intel/AMD x86 with discrete GPU, featuring its proprietary EDGEBoost I/O expansion architecture) represent the two main tiers of its edge AI portfolio.

## Key Facts

- **Founded:** 1994
- **HQ:** San Jose, CA
- **Ownership:** Private, US-based
- **Value chain position:** Rugged system integrator and OEM platform supplier
- **Platform tier:** Fanless appliance and short-depth rackmount tiers
- **Key certifications:** MIL-STD-810H (vibration, shock, temperature), E-Mark (vehicle/transportation), CE, FCC, UL
- **Primary markets:** Defense-adjacent (soldier modernization, tactical comms support), transportation/autonomous vehicles, utilities/energy infrastructure, industrial AI, ITS

## Key Products

### JCO Series — NVIDIA Jetson Orin Fanless AI Systems

The JCO Series is Premio's family of fanless rugged AI computers built on NVIDIA Jetson Orin modules. Jetson Orin (NX and AGX variants) is NVIDIA's embedded AI platform: a system-on-module combining an ARM CPU cluster, NVIDIA Ampere GPU cores, and dedicated deep learning accelerators (DLA) on a single compact module. Premio's JCO Series provides the ruggedized carrier board, chassis, I/O, power conditioning, and thermal management that transforms a bare Jetson module into a deployable edge AI appliance.

**JCO-6000-ORN** — Higher-performance variant; targets NVIDIA Jetson AGX Orin (up to 275 TOPS) or Jetson Orin NX (up to 100 TOPS); supports higher I/O density including multi-camera inputs (MIPI CSI), GbE/10GbE, USB 3.2, M.2 storage, and optional cellular or Wi-Fi. Target applications: autonomous vehicle compute node, multi-camera AI analytics, smart infrastructure AI.

**JCO-3000-ORN** — Compact variant; targets NVIDIA Jetson Orin NX (16GB or 8GB module options; 100 TOPS or 70 TOPS); designed for more constrained SWaP deployments; fewer expansion slots but similar environmental qualification. Target applications: drone compute, handheld/portable AI inference support, smaller vehicle integrations, sensor-local processing.

Key specifications across JCO Series:
- **AI performance:** 70–275 TOPS depending on Jetson Orin module selection
- **Form factor:** Compact fanless desktop/wallmount; din-rail variants available
- **Cooling:** Passive fanless via chassis heatsink
- **Operating temperature:** -40°C to +70°C (extended temperature models)
- **Power input:** 9–36VDC wide-range (vehicle bus compatible)
- **Standards:** MIL-STD-810H, E-Mark (transportation)
- **I/O:** Multi-camera (MIPI CSI), GbE/10GbE, USB, CAN bus, RS-232/422/485, M.2 NVMe, HDMI/DisplayPort

### RCO Series — Rugged Rackmount Servers with EDGEBoost

The RCO Series is Premio's rackmount rugged server line for applications requiring x86 processor performance with discrete GPU expansion — step above the Jetson tier in compute density. RCO platforms integrate Intel Core or Xeon processors with PCIe expansion for NVIDIA GPUs and leverage Premio's proprietary **EDGEBoost** I/O architecture.

**EDGEBoost** is Premio's modular I/O expansion technology: a PCIe-connected expansion slot on RCO Series servers that accepts swappable EDGEBoost I/O modules. A single RCO server can be configured with different EDGEBoost modules depending on the deployment — a video capture module for AI video analytics, a FPGA module for protocol bridging, a GPU module for additional inference capacity, or a networking module for specialized connectivity. This field-swappable I/O architecture allows a single base RCO platform to serve multiple application profiles without custom enclosure design.

Key specifications for RCO Series:
- **Form factor:** 1U–3U short-depth rackmount; designed for transit, vehicle rack, and wall-mount installations
- **Processors:** Intel Core i7/i9 (H-series mobile, for low-power configurations) or Intel Xeon E/W
- **GPU expansion:** PCIe x16 slot for NVIDIA discrete GPU; EDGEBoost GPU add-in option
- **EDGEBoost slots:** 1–2 swappable I/O expansion bays (video capture, FPGA, networking, GPU)
- **Operating temperature:** 0°C to +50°C (standard); -40°C to +70°C on extended-temp models
- **Standards:** MIL-STD-810H (vibration, shock, drop, humidity, temperature)
- **Power:** AC/DC auto-ranging; 12V/24V/48V DC input options for vehicle/railway

## What It Is / How It Works

Premio's core design philosophy is configurable ruggedization: rather than designing bespoke systems for each customer, it builds a platform architecture (JCO for Jetson-class AI, RCO for x86-class) and provides configurability through module swaps, I/O options, and module upgrades. EDGEBoost is the clearest expression of this — it turns a fixed-I/O rackmount server into a field-configurable platform.

The **JCO-ORN** platforms sit at the intersection of two trends: NVIDIA's Jetson Orin push into edge AI (Orin is explicitly positioned against industrial and transportation applications) and the growth of vision-based AI for smart infrastructure, autonomous vehicles, and military situational awareness. Premio provides the ruggedized hardware platform that customers deploy in the field — the software AI stack (camera inference models, object detection, tracking algorithms) is customer-provided or partner-provided.

The **RCO with EDGEBoost** targets customers who need more compute than Jetson provides (multi-camera 4K+ analytics, LLM inference at the edge, video transcoding + AI simultaneously) but can't justify full MIL-spec rackmount servers. EDGEBoost's field-swappability matters for fleet operators: a city operating 500 smart intersection AI nodes wants to swap a failed I/O module without returning the unit to a depot, and EDGEBoost modules are designed to be field-replaceable.

**Defense-adjacent positioning:** Premio does not sell primarily to defense primes or directly to DoD. Its defense-adjacent customers are integrators building soldier support systems, base security AI, unmanned vehicle ground support stations, and intelligence analysis workstations at forward operating bases — applications that need more ruggedization than a commercial laptop but less than a VPX-tier Mercury Systems subsystem.

## Market Context

Premio competes with Neousys, ADLINK, Cincoze, and Vecow in the semi-industrial edge AI appliance market. The competitive differentiation in this segment is GPU TDP headroom in fanless form factors, certification breadth, and platform longevity (industrial customers want 7–10 year product lifecycle, not consumer product 1–2 year cycles).

Premio's US headquarters and manufacturing partnerships position it well for NDAA Section 889 compliance — a requirement for US government and defense-adjacent procurements that excludes hardware from certain Chinese suppliers. This is an increasingly important differentiator versus Taiwanese and Chinese competitors in government-adjacent deals.

## Notable Developments

- **Ongoing:** JCO Series expanding to support Jetson Orin NX Super and next-generation Jetson modules as NVIDIA refreshes embedded AI platform
- **Ongoing:** EDGEBoost ecosystem growing with additional I/O module SKUs for 5G/LTE cellular, high-density PoE+ camera aggregation, and PCIe GPU offload
- **Trend:** Transition from Jetson Xavier (previous generation) to Jetson Orin across JCO Series — Orin delivers 2–8× performance improvement at similar or lower power versus Xavier, driving platform refresh cycle

## Sources

- [Premio — Official Website](https://premioinc.com/)
- [Premio — Rugged Edge AI Computers](https://premioinc.com/collections/rugged-edge-ai-computers)
- [NVIDIA Jetson Orin](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/) — module platform underlying JCO Series
