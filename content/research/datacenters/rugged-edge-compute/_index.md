---
title: "Rugged & Edge Compute"
date: 2026-03-25
lastmod: 2026-04-25
description: "Rugged compute platforms, AI inference at the edge, military/maritime/aviation deployments, man-portable compute, semi-industrial fanless edge AI servers"
tags: ["rugged", "edge-compute", "mil-spec", "ai-inference", "defense", "fanless", "industrial"]
categories: ["overview"]
research_area: "datacenters/rugged-edge-compute"
last_reviewed: 2026-04-25
stale_after_days: 180
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


## Overview

Compute platforms designed to operate outside controlled datacenter environments — aboard aircraft, naval vessels, ground vehicles, and in field-portable configurations. The primary driver is AI inference at the tactical edge: military/intelligence customers need GPU-accelerated processing co-located with sensors (radar, sonar, EO/IR cameras) rather than transmitting data to a cloud datacenter. The secondary driver is commercial aviation/maritime AI (predictive maintenance, autonomous navigation support). All companies here sell primarily to defense primes or directly to DoD/allied militaries.

The market stratifies by integration tier. At the component/module end, Mercury Systems and Curtiss-Wright supply individual VPX compute cards that primes slot into their chassis. At the system end, One Stop Systems builds complete AI compute servers; Anduril's Menace platform is a complete deployable C4 system with software and networking included. At the man-portable extreme, EDT/EDGETAK is a body-worn AI inference node for dismounted soldiers. These tiers address structurally different SWaP constraints and procurement channels.

Below the full MIL-spec tier sits a second market of semi-industrial and commercial edge AI platforms — fanless, wide-temperature, vibration-qualified compute from vendors like Neousys (Taiwan, Advantech subsidiary), Premio (San Jose), ADLINK (Taiwan), and DFI (Taiwan). These platforms serve transportation, ITS, industrial AI, and defense-adjacent applications (base security, training simulation, non-deployed AI workstations) where full MIL-STD-810H qualification depth is not required but commercial hardware is still inadequate. Crystal Group (Cedar Rapids, IA) bridges the gap: a US-owned rugged server maker with full MIL-STD-810H and MIL-STD-901D (shipboard shock) qualification, serving Navy surface ships and Army vehicles at a price and procurement tier below Mercury and OSS.

A separate but related subsection — [Edge AI Accelerators](../edge-ai-accelerators/) — covers dedicated M.2 and PCIe inference chips (Hailo-8/10/15, EdgeCortix SAKURA) that add AI inference capacity to existing compute platforms without requiring a GPU or a full system replacement.

## Deployment Context Tracker

| Company | Form Factor | GPU/NPU | Key Platform | Key Customer |
|---------|-------------|---------|--------------|--------------|
| Mercury Systems (MRCY) | VPX modules, rackmount subsystems | NVIDIA H-series, Intel/Xilinx FPGA | RES Trust XR6 | Navy, Army, classified programs |
| One Stop Systems (OSTO) | Rackmount AI compute servers | NVIDIA H100/H200 | AI on the Fly (AIFLY) | P-8A Poseidon, Virginia-class sub, USSOCOM |
| Curtiss-Wright (CW) | VPX modules, tactical servers | NVIDIA RTX PRO 5000 Blackwell | VPX3-730, PacStar 431/452 | DoD primes, SOSA programs |
| EDT / EDGETAK (HEI) | Man-portable / wearable | NVIDIA Jetson Orin NX | EDGETAK, EDGETAK RF | SOCOM, dismounted soldiers |
| Anduril Industries | C4 systems (vehicle + man-portable), autonomous platforms | NVIDIA Jetson (edge); Klas Voyager compute | Menace-T, Menace-X, Lattice OS | US Army ($20B), US Space Force, USSOCOM, allied MoDs |
| Crystal Group | Rackmount + vehicle-mount servers | NVIDIA RTX, Intel Xeon | RE4100 Series (shipboard), RE1900M (vehicle) | US Navy, Army, allied militaries |
| Neousys Technology (Advantech) | Fanless semi-industrial AI edge servers | NVIDIA RTX discrete GPU | SEMIL-2200, SEMIL-2200GC | ITS, transportation, defense-adjacent |
| Premio | Fanless appliance + rackmount with EDGEBoost | NVIDIA Jetson Orin / RTX discrete | JCO-6000-ORN, JCO-3000-ORN, RCO Series | Transportation, defense-adjacent, industrial AI |
| ADLINK Technology | COM Express modules, OpenVPX boards, AI edge servers | NVIDIA RTX / Jetson Orin | AXE Series, DLAP Series, OpenVPX GPU boards | Defense primes (OpenVPX), autonomous vehicles, industrial AI |
| DFI | Fanless industrial computers + GPU edge AI systems | NVIDIA RTX discrete GPU | EC/IPC Series (industrial), GPU AI series | Gaming/amusement, industrial automation, transportation |
| GMS | Ultra-compact mission computer (1"×4") | Intel Xeon W | X7 RAPTOR | Small UAS, manpack, wearable soldier compute |
| Core Systems | Stackable rugged servers | Intel Xeon Scalable | ATMOS Series | Command vehicles, airborne, maritime |
| Annapolis Micro Systems | FPGA boards + liquid-cooled VPX chassis | AMD/Xilinx UltraScale+ / Versal | WILD100 WC34D0 (LFT chassis) | Defense DSP, SIGINT, EW |
| LCR Embedded Systems | ATR chassis integrator | N/A (chassis only) | 3U VPX conduction/AFT/LFT ATR | Defense primes (chassis for Mercury/CW modules) |
| 7Starlake | Self-contained liquid-cooled VPX ATR | VPX module-dependent | 7SL-3500-L2L (500W TDP) | Radar, EW, UAS, hypersonic |

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Anduril Industries](https://www.anduril.com) | Costa Mesa, CA, USA | Late Private (~$28–30B valuation, Series G) | Defense technology prime; Lattice OS autonomous C2 platform; Menace-T/X rugged C4 systems on Klas Voyager hardware; $20B Army enterprise contract (March 2026); autonomous aerial, surface, and undersea vehicles. |
| [EDT / EDGETAK](https://edt.com) | Hillsboro, OR, USA | Private (HEICO subsidiary) | Man-portable wearable tactical AI inference platform (EDGETAK, launched April 2025); NVIDIA Jetson Orin NX; ATAK compatible; EDGETAK RF SDR variant (Summer 2026). |
| [Systel](https://www.systelusa.com) | San Marcos, TX, USA | Private | Kite-Strike rugged AI server; small-form-factor tactical compute for defense ground vehicles and maritime platforms. |
| [Kontron](https://www.kontron.com) | Augsburg, Germany | Public (SDAX: KTN) | European COTS rugged embedded compute; µDARC microserver for tactical edge; established embedded compute and VME/VPX board supplier to defense primes globally. |
| [Crystal Group](https://www.crystalrugged.com) | Cedar Rapids, IA, USA | Private | Rugged servers and vehicle-mount compute; RE4100 Series shipboard AI rackmount (MIL-STD-901D); RE1900M vehicle-mount server; US-owned with Buy American compliance; Navy surface ship and Army ground vehicle programs. |
| [VadaTech](https://www.vadatech.com) | Henderson, NV, USA | Private | Largest dedicated MicroTCA platform vendor in North America; full-stack MCH + chassis + AMC modules across MTCA.0/1/3/4 variants; UTC040C conduction-cooled MCH (Apr 2024); defense, scientific instruments, telecom, and industrial markets. See [entry]({{< relref "vadatech.md" >}}). |
| [N.A.T. GmbH (NAT Europe)](https://nateurope.com) | Hennef, Germany | Private | Reference MicroTCA Carrier Hub (MCH) specialist; NAT-MCH-G4 with 100 GbE optical uplinks, GPS/PTP/SyncE timing, PCIe Gen 4/5; primary MCH for European particle accelerator control (DESY, CERN, PSI) and 5G RAN timing. See [entry]({{< relref "nat-europe.md" >}}). |
| [Pixus Technologies](https://pixustechnologies.com) | Waterloo, ON, Canada | Private | Custom MicroTCA shelf, backplane, and enclosure design; 1U–8U in MTCA.0 and MTCA.4 formats; 40 GbE and PCIe Gen 3 backplanes; serves quantum computing, high-energy physics, and mission-critical communications customers. |
| [EMCOMO Solutions AG](https://emcomo.com) | Switzerland | Private | MicroTCA system integrator and AMC module reseller; full portfolio across MTCA.0/1/2/3/4 including AMC CPUs, FPGAs, networking, and RTM modules; serves physics labs, defense/avionics, industrial/IoT, and space applications. |
| [General Micro Systems (GMS)](https://www.gms4sbc.com) | Rancho Dominguez, CA, USA | Private | Ultra-compact rugged mission computers; patented RuggedCool 4-sided conduction cooling (+75°C operation); X7 RAPTOR (1"×4", Intel Xeon W, <$10K, announced Oct 2025); targets small UAS, manpack, wearable platforms. See [entry]({{< relref "general-micro-systems.md" >}}). |
| [Core Systems](https://core-systems.com) | San Diego, CA, USA | Private | ATMOS Series stackable rugged servers for vehicle, airborne, and maritime deployments; proprietary airflow/heat-dissipation for +60°C GPU operation; modular Chassis Rail System enables in-field node swaps; ISO 9001:2015. See [entry]({{< relref "core-systems.md" >}}). |
| [Annapolis Micro Systems](https://www.annapmicro.com) | Annapolis, MD, USA | Private | FPGA-based rugged OpenVPX boards and chassis; WILD100 EcoSystem (SOSA-aligned); WC34D0 liquid-cooled 3U VPX chassis (VITA 48.4 LFT, 100 GbE fabric); signal processing specialist. See [entry]({{< relref "annapolis-micro-systems.md" >}}). |
| [LCR Embedded Systems](https://www.lcrembeddedsystems.com) | USA | Private | 35+ year defense ATR chassis and backplane integrator; conduction, AFT, and LFT VPX chassis; VITA 46.11 chassis manager with open-source firmware (Oct 2025); US-manufactured; supply chain chassis enabler for Mercury/Curtiss-Wright compute modules. See [entry]({{< relref "lcr-embedded-systems.md" >}}). |

### Semi-Industrial & Commercial Edge AI Platforms

Mid-tier platforms between full MIL-spec defense compute and commercial servers — fanless, wide-temperature, vibration-qualified for transportation, defense-adjacent, and industrial AI deployments.

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Neousys Technology](https://www.neousys-tech.com) | New Taipei City, Taiwan | Private (Advantech subsidiary) | Fanless semi-industrial GPU AI edge servers; SEMIL-2200/SEMIL-2200GC Series; IP54-rated wide-temperature AI inference; transportation, ITS, and defense-adjacent markets; Advantech ecosystem. |
| [Premio](https://premioinc.com) | San Jose, CA, USA | Private | JCO Series (NVIDIA Jetson Orin NX/AGX Orin fanless AI systems; JCO-6000-ORN, JCO-3000-ORN); RCO Series rackmount with EDGEBoost modular I/O expansion; MIL-STD-810H, E-Mark; transportation, industrial AI, defense-adjacent. |
| [ADLINK Technology](https://www.adlinktech.com) | Taipei, Taiwan | Public (TWSE: 6166) | AXE Series rugged AI edge servers; DLAP deep learning inference platforms (Jetson Orin NX/AGX + discrete GPU); OpenVPX defense modules (SOSA-aligned); COM Express SoMs; dual commercial industrial and defense embedded computing markets. |
| [DFI](https://www.dfi.com) | Taipei, Taiwan | Private | Industrial fanless embedded computers and GPU AI systems; EC/IPC Series wide-temperature; gaming/amusement, industrial automation, transportation; RTX GPU-capable edge AI tier; ASRock Industrial / AAEON ecosystem-adjacent. |

### Public Companies

| Ticker | Company | Location | Focus | Notes |
|--------|---------|----------|-------|-------|
| [MRCY](https://finance.yahoo.com/quote/MRCY) | [Mercury Systems](https://www.mrcy.com) | Andover, MA | Rugged embedded computing; VPX modules and rackmount subsystems; Navy/Army programs | Sole-source supplier on key programs; RES Trust XR6; SOSA transition underway |
| [OSTO](https://finance.yahoo.com/quote/OSTO) | [One Stop Systems](https://onestopsystems.com) | Escondido, CA | "AI on the Fly" (AIFLY) rackmount AI compute servers | P-8A Poseidon, Virginia-class submarine, USSOCOM CRADA; Q4 2025 +70% YoY |
| [CW](https://finance.yahoo.com/quote/CW) | [Curtiss-Wright Defense Solutions](https://defense-solutions.curtisswright.com) | Davidson, NC | Defense electronics; VPX3-730/VPX6-731 Blackwell SOSA-aligned modules; PacStar 431/452 tactical AI servers | Established defense prime; both VPX module and integrated server tiers |

<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container" style="margin: 20px 0;">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
  {
    "colorTheme": "light",
    "dateRange": "12M",
    "showChart": true,
    "locale": "en",
    "showSymbolLogo": true,
    "showFloatingTooltip": true,
    "width": "100%",
    "height": "500",
    "tabs": [
      {
        "title": "Rugged Edge Compute",
        "symbols": [
          {"s": "NASDAQ:MRCY", "d": "Mercury Systems"},
          {"s": "NASDAQ:OSTO", "d": "One Stop Systems"},
          {"s": "NYSE:CW", "d": "Curtiss-Wright"}
        ],
        "originalTitle": "Rugged Edge Compute"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents

| Company | Relevance |
|---------|-----------|
| [L3Harris Technologies (LHX)](https://www.l3harris.com) | Defense prime with embedded computing and EW systems; Aerojet Rocketdyne acquisition; competes with Mercury on select signal processing programs |
| [Elbit Systems of America (ESLT)](https://www.elbitsystems.com) | Israeli defense prime with US operations; rugged compute and EO/IR systems for airborne and ground platforms; DRS Technologies (now Leonardo DRS) lineage |
| [Abaco Systems (AMETEK)](https://www.abaco.com) | COTS rugged VPX SBC and GPU compute boards; acquired by AMETEK 2021; competes with Mercury and Curtiss-Wright at the VPX module tier |
| [Elma Electronic](https://www.elma.com) | VPX backplane and chassis manufacturer; supplies chassis that integrate Mercury and Curtiss-Wright compute modules; a necessary supply chain layer for any VPX-based system |
| [Pixus Technologies](https://www.pixustechnologies.com) | OpenVPX chassis, backplane, and enclosure supplier; critical supply chain enabler for VPX compute module integrators |

## Supply Chain

The rugged edge compute supply chain starts with commercial silicon (NVIDIA GPUs, Intel/AMD processors, Xilinx FPGAs) and adds military-grade environmental qualification, thermal management, structural ruggedization, and MIL-spec power and connector systems. The critical bottleneck is NVIDIA GPU supply: NVIDIA does not produce defense-specific SKUs for its GPU cards — defense suppliers (Mercury, OSS, Curtiss-Wright) must qualify commercial silicon for MIL-STD-810 compliance, and commercial GPU supply allocation decisions at NVIDIA can directly affect defense program delivery timelines.

### Supply Chain Layers

| Layer | Key Inputs / Outputs | Companies Operating Here | Geographic Risk |
|-------|---------------------|--------------------------|-----------------|
| **1. GPU / AI Accelerators** | NVIDIA H100/H200 (rackmount), NVIDIA RTX PRO 5000 Blackwell (VPX), NVIDIA Jetson Orin NX (man-portable) | NVIDIA (design); TSMC (H100/H200 fabrication); Samsung (Jetson DRAM) | GPU design: US (NVIDIA); fabrication: Taiwan (TSMC) — critical single point of geographic concentration |
| **2. FPGA / Signal Processing** | Xilinx/AMD Versal and UltraScale+ FPGAs; Intel Agilex FPGAs; used in radar, EW, and sonar front-end processing | AMD/Xilinx, Intel | FPGA design: US; fabrication: TSMC (AMD/Xilinx), Intel Foundry (Intel) |
| **3. Ruggedized Compute Modules** | VPX 3U/6U GPU compute cards, embedded SBCs, conduction-cooled module assemblies | [Mercury Systems](https://www.mrcy.com), [Curtiss-Wright Defense Solutions](https://defense-solutions.curtisswright.com), [Abaco Systems (AMETEK)](https://www.abaco.com) | Module assembly: US-dominant for DoD-relevant programs |
| **4. VPX Chassis & Backplanes** | OpenVPX chassis, power backplanes, thermal management structures | [Elma Electronic](https://www.elma.com), [Pixus Technologies](https://www.pixustechnologies.com), [Mercury Systems](https://www.mrcy.com) (Themis acquisition) | US and European suppliers; no single dominant geographic concentration |
| **5. Integrated Rugged Servers** | Complete GPU compute servers and tactical C4 systems qualified to MIL-STD-810 | [One Stop Systems](https://onestopsystems.com) (AIFLY), [Mercury Systems](https://www.mrcy.com) (Themis rackmount), [Curtiss-Wright](https://defense-solutions.curtisswright.com) (PacStar), [Anduril / Klas](https://www.klasgov.com) (Voyager/Menace) | US-centric; UK and European suppliers present but smaller share |
| **6. Ruggedized Power Electronics** | Mil-spec DC/DC converters, power conditioning, EMI filters for vehicle and aircraft bus power | [Vicor](https://www.vicorpower.com) (NASDAQ: VICR), [SynQor](https://www.synqor.com), [Behlman Electronics](https://www.behlman.com) | US-dominant; specific to military power bus standards (28VDC vehicle, 270VDC aircraft) |
| **7. MIL-Spec Connectors** | Ruggedized connector systems for VPX backplanes, server bays, and wearable units | [Amphenol](https://www.amphenol.com) (NYSE: APH), [SOURIAU/Esterline](https://www.souriau.com), [Smiths Interconnect](https://www.smithsinterconnect.com) | US and European suppliers; Amphenol dominant by volume |
| **8. Thermal Management** | Conduction-cooled chassis, cold plate assemblies, liquid cooling modules for high-density GPU; VITA 48.4 LFT chassis (Elma, Annapolis Micro Systems, 7Starlake); self-contained closed-loop ATR systems | [Aavid / Boyd Corporation](https://www.boydcorp.com), internal engineering at Mercury/Curtiss-Wright; [Cryogenic Control Systems](https://www.crycon.com); [Elma Electronic](https://www.elma.com); [7Starlake](https://7starlake.com) (7SL-3500 VITA 48.4); [Annapolis Micro Systems](https://www.annapmicro.com) (WC34D0) | Distributed; US and European dominant; Taiwan (7Starlake) growing |
| **9. System Integration** | Qualified complete systems for specific platforms (aircraft, submarine, vehicle bay installation) | Defense primes (Lockheed Martin, Boeing, Northrop Grumman, BAE Systems) integrating COTS rugged compute; [Anduril](https://www.anduril.com) as vertically integrated exception | — |

### Key Supply Chain Notes

**⚑ NVIDIA GPU supply as critical dependency:** Mercury, OSS, and Curtiss-Wright all depend on NVIDIA GPU availability. NVIDIA allocates H100/H200 production capacity primarily to hyperscaler data center customers (Microsoft, Google, Amazon) — defense suppliers are smaller customers. During periods of GPU supply constraint (2023–2024), defense program GPU delivery was delayed. This is a structural supply chain risk for all rugged AI compute programs that is not resolved by US domestic policy, since NVIDIA GPUs are fabricated at TSMC in Taiwan.

**⚑ TSMC Taiwan concentration:** Every NVIDIA GPU, AMD/Xilinx FPGA, and a large share of Intel components used in rugged compute systems are fabricated at TSMC in Taiwan. Any disruption to TSMC production — geopolitical, natural disaster, or technical — would simultaneously affect GPU availability for commercial cloud, automotive AI, and military rugged compute. There is no near-term alternative to TSMC for leading-edge GPU nodes. The CHIPS Act is funding Intel and TSMC US fab capacity, but these facilities are years from producing GPUs at volume.

**⚑ MOSA/SOSA transition as supply chain reshaper:** DoD's push to SOSA-aligned, open-architecture components is gradually ending sole-source positions for proprietary VPX architectures. Mercury's legacy sole-source positions are at risk as programs refresh under SOSA requirements. Curtiss-Wright's first-mover advantage with Blackwell SOSA-aligned modules (VPX3-730, VPX6-731) positions it well for new SOSA program starts, but incumbent Mercury is also releasing SOSA-aligned products. The SOSA transition is structurally good for the competitive market but compresses margins as sole-source premiums erode.

**Anduril vertical integration exception:** Anduril's acquisition of Klas (Voyager ruggedized compute) is moving it out of the standard supply chain — it is increasingly its own rugged compute supplier rather than a customer of Mercury, OSS, or Curtiss-Wright. If Lattice becomes the dominant Army C2 platform, Klas Voyager hardware could displace third-party rugged servers in Army deployments.

**⚑ Thermal inflection point — liquid cooling required for AI GPU payloads:** GPU TDPs in 3U VPX form factor have crossed the practical ceiling of conduction cooling (~150 W per slot). Modern AI accelerator cards (NVIDIA RTX PRO 5000 Blackwell in VPX form, forthcoming GPU modules) run 200–400 W per slot. VITA 48.4 Liquid Flow-Through (LFT) is no longer experimental — it is the required cooling method for new AI-GPU-equipped VPX programs. The transition is in progress: at AUSA 2025 (November), nVent SCHROFF, Elma Electronic, 7Starlake, and Annapolis Micro Systems all demonstrated or highlighted VITA 48.4 LFT products. The supply chain consequence is that ATR chassis integrators (Elma, LCR Embedded Systems, 7Starlake) now require liquid cooling engineering competency alongside VPX mechanical integration. Chassis designs without LFT capability will not be selected for new high-density AI programs.

### Supply Chain — Last Reviewed: 2026-04-25
