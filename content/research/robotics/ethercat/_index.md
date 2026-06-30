---
title: EtherCAT
date: 2026-06-26
lastmod: 2026-06-26
draft: false
description: "EtherCAT (Ethernet for Control Automation Technology) — the dominant real-time Ethernet fieldbus for robotics and industrial automation. Covers protocol architecture, key companies, use cases, open-source tooling, functional safety, and limitations."
research_area: "robotics/ethercat"
last_reviewed: 2026-06-26
stale_after_days: 180
source_urls:
  - https://www.ethercat.org/en/technology.html
  - https://en.wikipedia.org/wiki/EtherCAT
  - https://www.acontis.com/en/what-is-ethercat-communication-protocol.html
  - https://www.ethercat.org/en/safety.html
sitemap:
  changefreq: "monthly"
  priority: 0.85
  disable: false
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.

## Overview

EtherCAT (Ethernet for Control Automation Technology) is a real-time Ethernet fieldbus protocol originally developed by [Beckhoff Automation](https://www.beckhoff.com) and published as an open standard in 2003. It is now governed by the **EtherCAT Technology Group (ETG)**, a vendor-neutral industry consortium that as of late 2024 counts over 8,000 member companies across 75 countries — making it one of the largest industrial fieldbus consortia in the world.

EtherCAT is the dominant communication protocol for high-performance motion control in robotics, CNC machine tools, semiconductor fabrication equipment, and factory automation. Its key differentiator is a "processing-on-the-fly" architecture that achieves cycle times as low as 62.5 µs and synchronization jitter under 1 µs — performance no standard Ethernet switch-based network can match. Virtually every serious multi-axis robot controller, industrial servo drive, and high-throughput machine built after ~2010 either uses EtherCAT or evaluates it as the default option.

## How EtherCAT Works

Standard Ethernet sends a frame to one device at a time; each switch or node receives the full frame, buffers it, processes it, and re-transmits. This introduces latency and jitter that are incompatible with real-time control.

EtherCAT inverts this model. The EtherCAT master sends one large Ethernet frame that travels through all slave devices in a logical ring. Each slave reads its addressed input data and inserts its output data **while the frame passes through** — no buffering, no store-and-forward delay. The frame returns to the master with all process data updated in a single network cycle.

Key protocol properties:

- **Cycle times:** 62.5 µs to 1 ms typical in motion control; 30 µs possible for high-end I/O configurations
- **Distributed clocks:** Hardware-based clock synchronization across all slaves; jitter under 1 µs
- **Topology:** Line, ring, tree, and star topologies all supported; up to 65,535 devices per segment; no Ethernet switches (switches degrade performance and must be avoided in real-time segments)
- **Physical layer:** Standard 100BASE-TX Ethernet cabling (Cat 5e or better); also supports fiber for long runs or electrical isolation
- **Addressing:** Each slave has a fixed station address programmed at startup; the master enumerates all slaves during network initialization
- **Protocols over EtherCAT:** CAN Application Protocol over EtherCAT (CoE) for drive profiles and object dictionaries; File Access over EtherCAT (FoE) for firmware updates; Ethernet over EtherCAT (EoE) for tunneling IP traffic; Servo Drive Profile over EtherCAT (SoE)

## Market Position

Among industrial Ethernet protocols, EtherCAT holds approximately 17% of new node installations globally (2025 HMS Networks data), behind PROFINET (27%) and EtherNet/IP (23%). However, in high-performance motion control — multi-axis robotics, precision machinery, semiconductor tooling — EtherCAT dominates. PROFINET and EtherNet/IP trade cycle time and determinism for broader IT integration and PLC ecosystem compatibility; EtherCAT optimizes purely for real-time performance.

| Protocol | Market Share | Cycle Time | Jitter | Primary Ecosystem |
|----------|-------------|-----------|--------|------------------|
| PROFINET | 27% | 250 µs–1 ms (IRT) | ~1 µs (IRT) | Siemens / European PLCs |
| EtherNet/IP | 23% | 1–10 ms typical | ~1 ms | Rockwell / North American PLCs |
| EtherCAT | 17% | 62.5 µs–1 ms | <1 µs | Motion control, robotics |

## Key Companies

### The Standard Body

| Organization | Role |
|---|---|
| [EtherCAT Technology Group (ETG)](https://www.ethercat.org) | Manages the open standard; 8,000+ member companies; publishes specifications, conformance test tools, and interoperability guidance. Membership is required to receive the vendor-assigned device ID and access the full specification set. |

### Master Controller Vendors

EtherCAT masters are software-implemented on any standard Ethernet MAC. The master software handles frame construction, distributed clock synchronization, state machine management, and process data mapping.

| Company | Product / Role |
|---|---|
| [Beckhoff Automation](https://www.beckhoff.com) | Originator of EtherCAT; TwinCAT runtime is the reference commercial master; AX5000 and AX8000 servo drives are benchmark EtherCAT slave products |
| [acontis technologies](https://www.acontis.com) | EC-Master commercial EtherCAT master stack; widely used in semiconductor, medical, and robotics OEM applications; supports Windows, Linux, VxWorks, INtime |
| [Omron](https://www.ia.omron.com) | Sysmac NJ/NX series machine controllers with native EtherCAT master |
| [Bosch Rexroth](https://www.boschrexroth.com) | ctrlX CORE controller; IndraDrive servo drives with EtherCAT |
| [Lenze](https://www.lenze.com) | i700 servo drives; EtherCAT master in i950 controllers |

### Slave Device Vendors (Servo Drives & Motion)

| Company | Product | Notes |
|---|---|---|
| [Beckhoff](https://www.beckhoff.com) | AX5000, AX8000 series | Reference implementation; broad EtherCAT feature coverage |
| [Yaskawa](https://www.yaskawa.com) | Sigma-7 servo drives | EtherCAT option widely deployed in semiconductor and robotics |
| [Panasonic Industry](https://industry.panasonic.eu) | MINAS A6 / A6B servo | Common in collaborative robot joints |
| [Kollmorgen](https://www.kollmorgen.com) | AKD2G servo drives | High-end motion control, FSoE safety support |
| [Synapticon](https://www.synapticon.com) | SOMANET Motion series | Compact integrated servo drives designed for robot joints; FSoE support; notable in humanoid robot development |
| [Elmo Motion Control](https://www.elmomc.com) | Gold Twitter, Platinum series | High-density servo controllers; semiconductor, aerospace |
| [Maxon](https://www.maxongroup.com) | EPOS4 controllers | EtherCAT option; compact drives for surgical and collaborative robots |
| [Delta Electronics](https://www.deltaww.com) | ASDA-A3 servo | Growing EtherCAT adoption; cost-competitive |
| [Novanta / Celera Motion](https://www.novanta.com) | Ingenia servo drives | Compact EtherCAT servo for surgical robotics and precision motion |

### ASIC / IP Core Vendors (Slave Hardware)

EtherCAT slave controllers require dedicated silicon — a general-purpose Ethernet MAC cannot implement the on-the-fly processing. This is a meaningful barrier to custom device development.

| Company | Product |
|---|---|
| [Beckhoff](https://www.beckhoff.com) | ET1100, ET1200 EtherCAT Slave Controller ASICs — the original and most widely deployed |
| [Hilscher](https://www.hilscher.com) | netX series — multi-protocol ASIC supporting EtherCAT slave and other industrial Ethernet protocols |
| [Texas Instruments](https://www.ti.com) | PRU-ICSS (Programmable Real-Time Unit Industrial Communication Subsystem) in AM335x / AM57x / AM64x SoCs — software-defined EtherCAT slave without external ASIC |
| [Microchip Technology](https://www.microchip.com) | LAN9252, LAN9253 EtherCAT slave controllers |
| Intel / Altera / Xilinx FPGAs | EtherCAT slave IP cores for custom applications |

### Open-Source Master Implementations

| Project | License | Notes |
|---|---|---|
| [SOEM (Simple Open EtherCAT Master)](https://github.com/OpenEtherCATsociety/SOEM) | GPLv2 with linking exception | C library; user-space; cross-platform; actively maintained by rt-labs; v2.0 released 2024 with major architecture improvements; widely used in robotics and ROS 2 integrations |
| [IgH EtherCAT Master / EtherLab](https://etherlab.org/en_GB/ethercat) | GPLv2 | Linux kernel-space module; supports Preempt RT; stronger real-time guarantees than SOEM but harder to port; original open-source EtherCAT master dating to 2006 |

SOEM is the more common choice in robotics and embedded applications due to its portability. IgH is preferred in Linux-only environments where kernel-space real-time is required.

## Use Cases in Robotics

### Industrial Robot Arms

All major industrial robot OEMs use EtherCAT internally for joint servo communication or expose EtherCAT as the external fieldbus interface. KUKA's KR C4/C5 controllers, FANUC's R-30iB, ABB's IRC5/OmniCore, and Yaskawa's YRC1000 all support EtherCAT. The protocol allows tight synchronization of 6+ axes at 1 kHz or faster — essential for coordinated path following and force control.

### Collaborative Robots (Cobots)

Universal Robots (UR3/UR5/UR10/UR16/UR20) expose an EtherCAT master port for connecting external devices (grippers, F/T sensors, vision systems) and accept an EtherCAT slave interface for integration into external machine controllers. Compact EtherCAT servo drives (Synapticon SOMANET, Maxon EPOS4, Panasonic MINAS) are a common choice for custom cobot joint actuators.

### Humanoid Robots

EtherCAT is increasingly the fieldbus of choice for humanoid robot development due to its ability to synchronize large numbers of joints (20–40+ in a full humanoid) at high update rates. Key data points:

- Boston Dynamics moved from CAN bus in PETMAN to EtherCAT in Atlas, enabling higher update rates and tighter synchronization
- Research humanoids (LOLA, TOCABI) report 2–4 kHz joint update rates over EtherCAT
- Synapticon SOMANET drives are specifically marketed for humanoid robot joints with integrated FSoE safety

### Semiconductor Equipment

One of EtherCAT's largest non-robot markets. Wafer handling, die bonding, wire bonding, and lithography sub-systems require sub-100 µs cycle times and sub-microsecond synchronization across multiple positioning axes. The semiconductor equipment market is a primary driver of EtherCAT's high-end performance requirements and is where the most demanding implementations exist.

### CNC Machine Tools

Multi-axis machining centers, EDM systems, and grinding machines use EtherCAT for coordinated axis motion. The protocol's distributed clock enables nanometer-scale synchronization relevant to precision machining.

### Test & Measurement

High-speed data acquisition systems and motion simulators (flight simulators, hardware-in-the-loop test rigs) use EtherCAT for deterministic, high-rate sensor data collection synchronized with motion commands.

## Functional Safety: FSoE

Safety over EtherCAT (FSoE, also called FailSafe over EtherCAT) is the functional safety extension of the EtherCAT protocol, standardized as ETG.5100 and IEC 61784-3. It was developed per IEC 61508 and is TÜV Süd Rail certified for use up to **SIL 3** (Safety Integrity Level 3) — the highest level applicable to discrete manufacturing systems.

FSoE uses a **black channel** approach: safety data is encapsulated in a protected frame with CRC and sequence counters and transmitted over the standard EtherCAT network. The safety layer detects all eight error categories defined in IEC 61508: falsification, repetition, incorrect sequence, message loss, impermissible delay, insertion, masking, and addressing errors. No separate safety cabling is required.

FSoE is widely deployed in collaborative robot cells (safe torque off, safe speed monitoring) and integrated into drives from Beckhoff, Kollmorgen, Synapticon, KEB, and others. It is the dominant functional safety protocol in EtherCAT-based machine tools and robotics.

## Best Practices

**Network topology:** Run EtherCAT in a pure line or ring topology — never through Ethernet switches. Switches add forwarding delay and jitter that violate real-time timing. Use fiber segments only where electrical isolation is needed; maintain line topology through the fiber junction.

**Cable and shielding:** Use Cat 5e or Cat 6 shielded twisted pair (STP/FTP) in electrically noisy environments (servo cabinets, motor leads). Keep EtherCAT cables physically separated from power cables where possible. EtherCAT is standard 100BASE-TX electrically — good EMC practice applies.

**Real-time OS:** EtherCAT masters require a real-time or near-real-time execution environment. Common choices: Preempt RT Linux (widely used in robotics), Xenomai, VxWorks, INtime on Windows. On standard Linux or Windows without RT patches, cycle time consistency degrades under load — acceptable for commissioning tools, not for production.

**Cycle time selection:** Match cycle time to the application. 1 ms is sufficient for most pick-and-place and logistics robots. Motion control with force feedback or impedance control typically wants 500 µs or 250 µs. High-dynamic humanoid balance and semiconductor precision stages may need 125 µs or 62.5 µs. Shorter cycles increase CPU load linearly — benchmark before committing.

**Distributed clocks:** Always enable distributed clocks for multi-axis motion. Without DC synchronization, servo drives operate from their own local clocks and inter-axis jitter accumulates. DC is what makes EtherCAT suitable for coordinated motion — it is not optional for serious applications.

**Hot connect / redundancy:** EtherCAT supports cable redundancy (ring topology with a second Ethernet port on the master) and hot-connect groups (slave segments that can be disconnected and reconnected at runtime). Use cable redundancy in applications where network faults are safety-critical. Hot connect is useful for tool changers and mobile platforms where segments physically disconnect.

**Conformance:** Test new slave devices with the ETG Conformance Test Tool (CTT) ET9400 before integrating into production networks. Non-conformant slaves are a common source of subtle interoperability problems.

## Limitations

**Proprietary slave hardware:** Every EtherCAT slave requires a dedicated EtherCAT Slave Controller (ESC) — either an ASIC (Beckhoff ET1100, Hilscher netX, Microchip LAN9252) or FPGA/SoC with ESC IP core (TI PRU-ICSS). You cannot implement a high-performance EtherCAT slave on a general-purpose microcontroller with a standard Ethernet MAC. This adds BOM cost and component sourcing risk compared to protocols like EtherNet/IP.

**No switches allowed:** The prohibition on Ethernet switches means EtherCAT segments are physically isolated from standard IT/OT networks. Connecting EtherCAT to a plant SCADA or MES network requires a gateway device. This is intentional (isolation improves determinism) but adds integration complexity.

**EMI sensitivity:** Standard copper Ethernet cabling is susceptible to electromagnetic interference. Servo drive switching noise, VFD harmonics, and inductive loads in manufacturing environments can corrupt frames if cabling practice is poor. FSoE and hardware redundancy mitigate this for safety applications but not for general data integrity without good EMC discipline.

**Master software complexity:** Implementing a correct EtherCAT master — state machines, distributed clock synchronization, CoE object dictionary management, hot-connect — is non-trivial. Commercial stacks (acontis EC-Master, Beckhoff TwinCAT) handle this at cost; open-source stacks (SOEM, IgH) require significant engineering investment to use correctly in production.

**No native wireless:** EtherCAT is inherently wired. Wireless EtherCAT bridges exist but introduce latency and jitter that compromise real-time guarantees. Mobile and untethered applications typically use a different fieldbus (EtherNet/IP, PROFINET, or proprietary) for wireless segments, with an EtherCAT segment on the robot body.

**Not ideal for process automation:** EtherCAT's line topology and lack of switch support make large-scale process plant applications (chemical, oil & gas) awkward compared to PROFINET or EtherNet/IP, which tolerate standard managed switches and star wiring. EtherCAT is optimized for machine-level motion control, not plant-wide sensor/actuator networks.

## Comparison to Competing Protocols

| | EtherCAT | PROFINET IRT | EtherNet/IP | CAN / CANopen |
|---|---|---|---|---|
| **Cycle time** | 62.5 µs–1 ms | 250 µs–1 ms | 1–10 ms | 1–10 ms |
| **Jitter** | <1 µs | ~1 µs (IRT) | ~1 ms | ~100 µs |
| **Node count** | 65,535/segment | Hundreds | Hundreds | 127/bus |
| **Switches** | Not allowed | Allowed | Allowed | N/A |
| **Slave hardware** | Dedicated ESC required | Standard Ethernet MAC | Standard Ethernet MAC | CAN transceiver |
| **Ecosystem** | Motion, robotics | Siemens PLCs | Rockwell PLCs | Legacy, embedded |
| **Safety** | FSoE (SIL 3) | PROFIsafe (SIL 3) | CIP Safety (SIL 3) | CANopen Safety |
| **Market share** | 17% | 27% | 23% | Legacy declining |

CAN/CANopen is the legacy alternative most relevant in robotics — still found in older robot generations, lighter-weight embedded joints, and automotive applications. EtherCAT has largely superseded CAN in new high-performance robot designs due to higher bandwidth, more nodes, and better synchronization.

## Entries

- [Protocol Guide: Configuration and Communication]({{< relref "protocol-guide.md" >}}) — Step-by-step walkthrough of EtherCAT network startup, ESM state machine, CoE SDO/PDO, CiA 402 servo enabling, distributed clocks, and cyclic loop implementation with annotated SOEM C code

## Resources

- [EtherCAT Technology Group](https://www.ethercat.org) — Specifications, conformance tools, product guide, FAQs
- [ETG Technology Overview](https://www.ethercat.org/en/technology.html) — Official technical introduction
- [SOEM on GitHub](https://github.com/OpenEtherCATsociety/SOEM) — Open-source master library
- [acontis: EtherCAT Master Options Compared](https://www.acontis.com/en/ethercat-master-options-ec-master-vs-open-source-etherlab-SOEM.html) — SOEM vs IgH vs commercial stacks
- [FSoE Overview (ETG)](https://www.ethercat.org/en/safety.html) — Safety over EtherCAT specification and certification
- [Dewesoft: What is EtherCAT?](https://dewesoft.com/blog/what-is-ethercat-protocol) — Accessible technical introduction
- [control.com: EtherCAT Advantages, Challenges, and Specs](https://control.com/technical-articles/introduction-to-ethercat/) — Independent overview including limitations
