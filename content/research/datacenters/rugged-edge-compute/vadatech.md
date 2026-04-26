---
title: "VadaTech"
date: 2026-04-25
lastmod: 2026-04-25
draft: false
description: "Henderson, NV-based MicroTCA platform and AMC module specialist; largest dedicated MicroTCA vendor in North America serving defense, telecom, scientific, and industrial markets."
tags: ["microtca", "amc", "mch", "embedded-compute", "defense", "rugged", "us", "conduction-cooled"]
categories: ["company"]
research_area: "datacenters/rugged-edge-compute"
source_urls:
  - "https://www.vadatech.com/products/architecture/microtca/"
  - "https://www.vadatech.com/wp-content/uploads/2024/12/pdf_MicroTCA_Overview.pdf"
  - "https://www.vadatech.com/vt-news-april-2025/"
  - "https://militaryembedded.com/unmanned/rugged-computing/new-microtca-1-compliant-chassis-from-vadatech-for-rugged-applications"
  - "https://www.vadatech.com/vadatech-announces-a-conduction-cooled-microtca-chassis-with-full-redundancy-across-two-amc-slots/"
last_reviewed: 2026-04-25
stale_after_days: 180
---

## Summary

VadaTech (Henderson, Nevada) is the largest dedicated MicroTCA platform supplier in North America, offering the most complete range of MicroTCA Carrier Hubs (MCH), chassis, AMC compute/FPGA/networking modules, and power systems in the US market. Active across MTCA.0, MTCA.1, MTCA.3 (conduction-cooled), and MTCA.4 variants with particular emphasis on defense and scientific applications.

## Key Facts

- **Founded:** ~2006 (contemporaneous with initial MicroTCA ratification)
- **HQ:** Henderson, Nevada, USA
- **Type:** Private company
- **Product breadth:** MCH (6+ models), chassis (MTCA.0/1/3/4 variants), AMC compute/FPGA/signal processing/networking/storage modules, conduction-cooled chassis
- **MicroTCA variants:** MTCA.0, MTCA.1, MTCA.3 (conduction-cooled mil/aero), MTCA.4 (RTM-capable)
- **Key markets:** Defense/aerospace, scientific instruments, wireless/telecom, industrial automation, energy
- **Status:** Active; announced new products in April 2025

## What It Is / How It Works

VadaTech is a vertically integrated MicroTCA system house — they design and manufacture both the chassis/infrastructure (backplanes, power modules, cooling units, MCHs) and the payload AMC modules (CPUs, FPGAs, networking, storage). This distinguishes them from chassis specialists (nVent SCHROFF, Pixus) or MCH-only vendors (N.A.T. GmbH): VadaTech sells complete integrated systems from a single vendor.

### Key MCH Products

**UTC001 / UTC002 / UTC003:** Earlier-generation MCHs supporting MTCA.0/MTCA.4; UTC003 is the primary conduction-cooled MCH for MTCA.3 chassis, with a 400 MHz RISC CPU for shelf management and redundant boot.

**UTC040C (April 2024):** Conduction-cooled MCH; PCIe Gen 3 switch with 1024 Gbps aggregate bandwidth; designed for MTCA.3 mil/aero chassis. One of the most capable conduction-cooled MCHs announced as of mid-2024.

**UTC041:** MTCA.3 Conduction Cooled MCH; management software includes Carrier Manager and Shelf Manager; manages Power Modules, Cooling Units, and up to 12 AMCs.

**UTC042:** Rugged 3rd-generation MCH; 40 GbE / PCIe Gen 3 fabric; targeted at MTCA.1 ruggedized deployments.

**UTC004:** 40 GbE MCH with GPS, synchronous Ethernet (SyncE), and NTP — used in timing-critical telecom and 5G RAN applications.

### Chassis Portfolio

VadaTech offers chassis across all environmental tiers. For conduction-cooled deployments, the VT874 is a compact MTCA.3 chassis with three AMC slots designed for vehicle-mounted or airborne platforms. MTCA.0 and MTCA.4 standard air-cooled chassis are available in 1U through 9U heights supporting up to 12 AMC slots.

### AMC Module Types

VadaTech's AMC module catalog spans CPU modules (Intel Xeon D, Core-class), FPGA modules (Xilinx/AMD Kintex/Virtex, Altera/Intel Stratix), GPU modules, high-speed networking (10/40/100 GbE), storage (NVMe SSD), and specialized signal processing/data acquisition. This depth enables VadaTech to supply a complete MicroTCA solution without third-party modules — a significant integration advantage for programs requiring a single system supplier.

## Notable Developments

- **2025-04:** VT News April 2025 issue — new product announcements in Q1 2025; continued portfolio expansion across mil/aero and telecom segments.
- **2024-04:** Announced UTC040C conduction-cooled MCH with PCIe Gen 3 switch at 1024 Gbps aggregate bandwidth — targeting MTCA.3 mil/aero deployments.
- **2024-12:** Published updated MicroTCA ecosystem overview PDF, positioning VadaTech as reference system integrator for MTCA.0 Rev 3.0 ecosystem.
- **2023-2024:** Announced support for MTCA.0 Revision 3.0 compliant products (chassis, MCH, AMC) alongside NAT, AIES, and nVent SCHROFF following September 2023 PICMG ratification.
- **Prior:** Announced MTCA.1-compliant chassis for ruggedized applications (enhanced shock/vibration for outside-plant and light military use).
- **Prior:** Announced conduction-cooled MTCA.3 chassis with full redundancy across two AMC slots — enabling dual-redundant military compute nodes in very compact form factor.

## Key People

<!-- LinkedIn and detailed biographies not found in public sources for VadaTech executives; company maintains low public profile -->

### People — Last Reviewed: 2026-04-25

## Claim Verification

### Claim: UTC040C offers 1024 Gbps aggregate PCIe Gen 3 switch bandwidth

**Status:** Partially verified

**Supporting sources:**
- [VadaTech Product Releases](https://www.vadatech.com/product-releases/) — announcement confirms product designation and PCIe Gen 3 switch; 1024 Gbps stated in announcement
- [VadaTech April 2024 product release](https://www.vadatech.com/newsroom/) — confirmed April 2024 date

**Refuting / questioning sources:**
- No independent third-party benchmark or measurement has been identified in public sources

**Summary:** The 1024 Gbps aggregate figure is VadaTech's self-reported specification; consistent with PCIe Gen 3 ×16 lane counts across 12 AMC slots but not independently verified.

## Sources

- [VadaTech MicroTCA Products](https://www.vadatech.com/products/architecture/microtca/) — full product catalog
- [VadaTech MicroTCA Overview PDF](https://www.vadatech.com/wp-content/uploads/2024/12/pdf_MicroTCA_Overview.pdf) — December 2024 ecosystem guide
- [VadaTech VT News April 2025](https://www.vadatech.com/vt-news-april-2025/) — Q1 2025 product announcements
- [Military Embedded: MTCA.1 chassis from VadaTech](https://militaryembedded.com/unmanned/rugged-computing/new-microtca-1-compliant-chassis-from-vadatech-for-rugged-applications) — ruggedized chassis coverage
- [VadaTech: Conduction Cooled MicroTCA chassis announcement](https://www.vadatech.com/vadatech-announces-a-conduction-cooled-microtca-chassis-with-full-redundancy-across-two-amc-slots/) — MTCA.3 compact chassis
