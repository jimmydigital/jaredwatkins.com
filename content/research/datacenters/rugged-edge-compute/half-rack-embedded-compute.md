---
title: "Half-Rack Embedded Compute Form Factor"
date: 2026-04-25
lastmod: 2026-04-25
draft: false
description: "10-inch half-width rackmount compute systems for space-constrained deployments. Overview of form factor, SWaP advantages, platform tiers, and competing ecosystem (MicroTCA, VPX, commercial)."
tags: ["half-rack", "form-factor", "swp", "embedded-compute", "edge-infrastructure", "microtca"]
categories: ["technology"]
research_area: "datacenters/rugged-edge-compute"
source_urls:
  - "https://www.picmg.org/openstandards/microtca/"
  - "https://www.nvent.com/en-us/schroff/products/microtca"
  - "https://pixustechnologies.com/products/enclosure-system-solutions/microtca-systems-2/microtca-systems/"
  - "https://www.powergridm.com/"
  - "https://www.electronicdesign.com/technologies/industrial/boards/article/55233125/advanced-cooling-technologies-overcome-thermal-management-challenges-in-rugged-system-design-to-optimize-swap-c"
last_reviewed: 2026-04-25
stale_after_days: 180
---

## Summary

Half-rack (10-inch width) embed compute systems are purpose-built for applications where physical footprint is the primary constraint: vehicle bays, aircraft compartments, naval platforms, and edge datacenters with fixed rack-unit budgets. The form factor trades off absolute compute density against space efficiency, enabling 2–4 servers to fit in the space of a single full-width (19-inch) system. Three distinct ecosystems serve this market: commercial industrial-grade systems (Neousys, ASUS, ADLINK), military-grade MicroTCA modular platforms (nVent SCHROFF, Pixus, Recab), and purpose-built vertical solutions (Galleon NAS, 7Starlake NAS, Anduril/Klas Voyager).

## Key Facts

- **Form Factor:** 10-inch width (half of standard 19-inch rackmount); typical heights 1U–3U
- **Thermal Design:** Fanless (passive) or ultra-low-airflow; power budgets 50–600W depending on variant
- **Standards:** No unified standard (unlike VPX/OpenVPX); loosely follows industrial rackmount conventions (EIA RS-310)
- **Primary Use Cases:** Vehicle/aircraft/naval compartment deployment, space-constrained edge POPs, modular multi-node clusters
- **Ecosystem Fragmentation:** High — no cross-vendor form-factor compatibility (unlike MicroTCA/VPX backplanes)

## What It Is / How It Works

### Why Half-Rack?

Standard full-width (19-inch) servers occupy ~152mm width. A 10-inch half-rack is ~254mm width—exactly half the footprint. This enables critical deployments where space is finite and non-negotiable:

- **Vehicle bay mount:** A Bradley Fighting Vehicle, Black Hawk helicopter, or patrol boat has a fixed equipment rack (6U–9U height), usually one meter wide. Two half-rack servers fit where one full-width server would. This doubles operational flexibility: a vehicle can carry dual-redundant compute, or a compute + networking unit.
- **Ship compartment:** Naval surface combatants (destroyers, frigates) pack electronics into compact combat information centers. Half-rack width reduces floor space, enabling more sensor processing pipelines in the same compartment.
- **Aircraft avionics bay:** Narrow fuselage sections (business jets, transport aircraft) require thin, tall server forms. Half-rack width maximizes compute density in constrained vertical spaces.
- **Edge datacenter:** A modular edge POP (Point of Presence) designed for rapid deployment uses ruggedized shipping containers or prefab structures. Half-rack systems stack two-per-width, increasing node count per footprint, reducing site size and power-distribution weight.

### Platform Tiers

**Tier 1: Commercial Semi-Industrial (Neousys SEMIL, ASUS RUC-1000D, ADLINK AXE, Premio JCO)**
- 2U–3U height; fanless or low-airflow cooling; DDR4/DDR5 DRAM
- Processors: Intel Core Ultra, Xeon E, or Xeon D
- Temperature range: -20°C to +60°C (some extended to -40°C/+70°C)
- Network: GigE or dual GigE; occasional 10 GbE option
- Storage: M.2 NVMe or 2.5" SSD
- Target: ITS, transportation, base security, non-classified defense-adjacent
- Price: $5K–$20K per unit

**Tier 2: Military-Grade Modular (MicroTCA systems from nVent SCHROFF, Pixus, Recab)**
- 1U–3U height; modular backplane architecture; Advanced Mezzanine Cards (AMCs)
- Processors: Module-dependent (FPGA, custom AI accelerators, ARM/x86 compute)
- Temperature range: -40°C to +85°C typical
- Network: Custom per-module (GigE to 100 GbE backplane)
- Certifications: VITA 62 (modular power), MIL-STD-810, MIL-STD-461 (EMI)
- Target: DoD tactical edge, signals processing, classified AI inference
- Price: $50K–$150K+ (high complexity, low volume)

**Tier 3: Vertical Domain Solutions (Galleon XSR NAS, 7Starlake THOR200 NAS, Anduril Menace Compute)**
- 2.5U–3U height; purpose-built for specific mission (NAS, tactical C4, autonomous vehicle compute)
- Processors: Xeon E/D (NAS), or custom integration (Menace)
- Storage: 40TB–80TB (NAS tier) or modular GPU expansion (tactical tier)
- Certifications: MIL-STD-810/901D, FIPS-140-2 (NAS); MIL-STD-461, MilSpec power (tactical)
- Target: Naval platforms, aerospace, special operations, autonomous systems
- Price: $25K–$100K+ (domain-specific, moderate volume)

## Competitive Landscape

### vs. MicroTCA (VITA 62)

MicroTCA modular standards enable hot-swap compute modules, true multi-vendor interoperability, and field customization. However, MicroTCA systems are **significantly more expensive** (~$100K+ for a 3-slot µTCA chassis with compute), and their modular overhead (standardized backplane, inter-module connectors, MCH controller) means lower density than purpose-built systems. MicroTCA is preferred in classified DoD programs where modularity and long-term supportability outweigh cost; commercial/non-classified programs prefer purpose-built half-rack systems.

### vs. Full-Width (19-Inch) Rackmount

Full-width servers (2U, 4U standard) achieve better thermal dissipation (larger chassis, more airflow), more expansion slots, and lower cost-per-compute (economy of scale). Half-rack trades off compute density and cost to gain spatial footprint reduction — only justified when space is the binding constraint. For fixed datacenters with unlimited floor space, full-width is always more cost-effective.

### vs. Blade/Sled Systems (e.g., NVIDIA HGX)

Modular blade systems (Supermicro SuperBlade, OAM GPU sleds) pack even higher density by eliminating per-node redundancy (shared power, cooling, fabric). Half-rack systems maintain per-node power supplies and thermal isolation, incurring a density penalty. Blades are preferred for homogeneous, high-scale deployments (hyperscaler datacenters); half-rack systems are preferred for heterogeneous, small-cluster, or tactical deployments where modularity and spares commonality matter.

## Key Technical Trade-Offs

**Thermal Design:**
- Fanless half-rack systems achieve -40°C operation (Neousys, Galleon, 7Starlake) by relying on conduction cooling and passive heat sinks, but limited to 50–150W thermal dissipation.
- GPUs requiring 300W+ thermal budget demand active cooling (fans) or liquid cooling, reducing fanless feasibility.
- Result: Half-rack fanless systems support edge inference (NVIDIA Jetson Orin, modest RTX), not heavy compute (H100, H200).

**Power Density:**
- Full-width 2U: up to 5–10 kW per unit (shared PSU, shared cooling infrastructure).
- Half-rack 2U: up to 2–3 kW per unit (smaller PSU, more thermal challenges).
- Result: Two half-rack units ≠ one full-width unit in raw power capacity. Offset by spatial savings.

**Modularity:**
- Half-rack commercial systems (Neousys, ASUS) are largely fixed-configuration ("buy the spec you need").
- MicroTCA allows in-field module swaps and future upgrades.
- Result: Commercial systems are cheaper and simpler; MicroTCA is flexible but expensive.

## Ecosystem Players

### System Builders

| Company | Form Factor | Ecosystem | Market Tier |
|---------|------------|-----------|------------|
| Neousys | 2U half-rack, fanless | Industrial/commercial | Tier 1 (semi-industrial) |
| ASUS RUC-1000D | Half-rack, fanless | Commercial | Tier 1 (semi-industrial) |
| ADLINK AXE | 2U–3U half-rack | Industrial/defense-adjacent | Tier 1–2 |
| Premio | 2U–3U half-rack | Commercial edge | Tier 1 |
| Galleon XSR | 3U half-rack | Military NAS | Tier 3 (vertical) |
| 7Starlake THOR200 | 2.5U half-rack | Military aerospace/submarine | Tier 3 (vertical) |
| nVent SCHROFF | 1U–3U µTCA half-rack | Military modular | Tier 2 (MicroTCA) |
| Pixus Technologies | µTCA chassis | Military modular backplane | Tier 2 (MicroTCA enabler) |

### Processor Supply

- **Intel Xeon E / Core / Core Ultra:** Dominant in Tier 1 systems
- **Intel Xeon D:** Preferred for Tier 3 (extreme-environment) due to low thermal envelope
- **NVIDIA Jetson Orin:** Man-portable variant (8–16W); Tier 1 systems
- **NVIDIA RTX Discrete:** Tier 1–2 systems; 150–300W typical
- **Custom FPGA / AI Accelerators:** Tier 2 (MicroTCA modules)

## Power Delivery and DC Distribution

Power budget is a hard constraint in half-rack form factors. The smaller chassis volume limits PSU size, thermal dissipation, and cabling.

**Typical power envelopes by tier:**

| Tier | Power Budget | Notes |
|------|-------------|-------|
| Tier 1 (commercial fanless, Neousys/Premio) | 50–150 W | Intel Core or Xeon E; Jetson Orin class GPU |
| Tier 1 (semi-industrial GPU, ASUS RUC-1000G) | 300–600 W | Discrete NVIDIA RTX 40-series; requires fan cooling |
| Tier 2 (MicroTCA, nVent SCHROFF) | 50–500 W | Module-dependent; VITA 62 power supply standard |
| Tier 3 (vertical, Galleon XSR, 7Starlake THOR200) | 100–300 W | Xeon D with NVMe storage; fanless possible |

**Vehicle bus power standards:**

Half-rack systems deployed in ground vehicles must accept 24–28V DC power from the vehicle bus (MIL-STD-1275 for military ground vehicles). Aircraft platforms typically supply 28V DC (MILSPEC aircraft) or 115V AC (transport aircraft with conversion). Shipboard platforms may supply 115/220V AC (MIL-STD-1399). Power supply selection is a first-order integration challenge for deployed systems, and some half-rack vendors (PowergridM, Behlman) supply purpose-built 1U half-rack UPS/conditioners designed to sit in the same bay as the compute unit.

**48V DC distribution:**

Higher-performance half-rack systems increasingly use 48V internal distribution to reduce cable losses at high current. The VITA 62 power supply standard supports 48V outputs. PowergridM's stackable UPS line includes 48V-capable configurations for tactical power conditioning; output voltages are configurable from 2V to 48V. 48V internal buses allow thinner cables and lower I²R losses, important in chassis where cable routing is tightly constrained.

**Power redundancy:**

Most Tier 1 commercial half-rack systems do not offer redundant PSUs — the chassis is too small. Redundancy is achieved at the system level (two units, failover). MicroTCA Tier 2 systems support redundant power modules (two VITA 62 PSUs per shelf) per the standard.

## Ruggedness and Environmental Ratings

**MIL-STD-810H compliance:** The current revision of the DoD environmental test standard. Vendors claiming "MIL-STD-810" should be qualified: which revision (H is current), and which test methods?

Key MIL-STD-810H methods relevant to half-rack edge compute:
- **Method 501/502:** High/low temperature storage and operation. Relevant range for vehicle deployment: operating at -32°C to +63°C (Category C3).
- **Method 514:** Vibration. Different profiles for ground transport, wheeled vehicle, tracked vehicle, and aircraft. Tracked vehicle spectra are far more severe than wheeled.
- **Method 516:** Shock. Drop testing (1m operational shock) and bench handling. Naval shock (Method 522 / MIL-STD-901D) is a separate, far more demanding standard.
- **Method 507:** Humidity (damp heat, 40°C / 85% RH sustained)
- **Method 510:** Sand and dust ingestion — test for IP-rated sealed enclosures

**IP ratings (IEC 60529):**

| Rating | Protection | Application |
|--------|-----------|-------------|
| IP54 | Dust-limited / splash-resistant | Light outdoor use; Neousys SEMIL standard configuration |
| IP65 | Dust-tight / water jet resistant | Vehicle exterior, maritime deck exposure |
| IP67 | Dust-tight / 30-minute immersion (1m) | Amphibious, exposed deployment; Neousys SEMIL-1300 and Galleon |
| IP69K | Steam jet cleaning | Extreme wash-down industrial |

**Operating temperature ranges:**

| Configuration | Range | Notes |
|--------------|-------|-------|
| Standard commercial server | 0°C to +40°C | Controlled datacenter |
| Semi-industrial (Neousys, Premio, ADLINK) | -20°C to +60°C | Typical fanless AI edge server |
| Extended rugged (Neousys SEMIL-1300, Galleon XSR) | -40°C to +70°C | Vehicle bay, exposed rack |
| MIL-grade (Crystal Group, VPX Tier 2) | -40°C to +71°C or +85°C | Full MIL-STD-810H qualification |

**Cost premium of ruggedization:**

Ruggedization adds material cost (aluminum alloy vs. steel chassis, conformal coating on PCBs, MIL-spec connectors), qualification cost (running MIL-STD-810 test campaigns costs $50K–$250K per product), and production overhead (lower volume, US sourcing requirements for DoD programs). As a rough multiplier: a commercial Tier 1 half-rack unit priced at $5K–$20K may have a ruggedized/qualified equivalent at $25K–$100K for the same processing capability. Full VPX Tier 2 systems with MIL-STD-810H/901D qualification can run $100K–$300K.

## Sources

- [PICMG MicroTCA Standard](https://www.picmg.org/openstandards/microtca/) — Modular compute ecosystem overview
- [nVent SCHROFF MicroTCA Products](https://www.nvent.com/en-us/schroff/products/microtca) — Military-grade modular half-rack systems
- [Pixus Technologies Modular Systems](https://pixustechnologies.com/products/enclosure-system-solutions/microtca-systems-2/microtca-systems/) — MicroTCA chassis and integration
- [PowergridM Military UPS](https://www.powergridm.com/) — Half-rack military UPS and power conditioners
- [Ruggedized System Design Thermal Management (Electronic Design)](https://www.electronicdesign.com/technologies/industrial/boards/article/55233125/advanced-cooling-technologies-overcome-thermal-management-challenges-in-rugged-system-design-to-optimize-swap-c) — SWaP-C thermal trade-offs in rugged design
