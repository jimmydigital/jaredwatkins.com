---
title: "Rugged & Edge Compute"
date: 2026-03-25
lastmod: 2026-03-26
description: "Rugged compute platforms, AI inference at the edge, military/maritime/aviation deployments, man-portable compute"
tags: ["rugged", "edge-compute", "mil-spec", "ai-inference", "defense"]
categories: ["overview"]
research_area: "datacenters/rugged-edge-compute"
last_reviewed: 2026-03-26
stale_after_days: 180
---

## Overview

Compute platforms designed to operate outside controlled datacenter environments — aboard aircraft, naval vessels, ground vehicles, and in field-portable configurations. The primary driver is AI inference at the tactical edge: military/intelligence customers need GPU-accelerated processing co-located with sensors (radar, sonar, EO/IR cameras) rather than transmitting data to a cloud datacenter. The secondary driver is commercial aviation/maritime AI (predictive maintenance, autonomous navigation support). All companies here sell primarily to defense primes or directly to DoD/allied militaries.

The market stratifies by integration tier. At the component/module end, Mercury Systems and Curtiss-Wright supply individual VPX compute cards that primes slot into their chassis. At the system end, One Stop Systems builds complete AI compute servers; Anduril's Menace platform is a complete deployable C4 system with software and networking included. At the man-portable extreme, EDT/EDGETAK is a body-worn AI inference node for dismounted soldiers. These tiers address structurally different SWaP constraints and procurement channels.

## Deployment Context Tracker

| Company | Form Factor | GPU/NPU | Key Platform | Key Customer |
|---------|-------------|---------|--------------|--------------|
| Mercury Systems (MRCY) | VPX modules, rackmount subsystems | NVIDIA H-series, Intel/Xilinx FPGA | RES Trust XR6 | Navy, Army, classified programs |
| One Stop Systems (OSTO) | Rackmount AI compute servers | NVIDIA H100/H200 | AI on the Fly (AIFLY) | P-8A Poseidon, Virginia-class sub, USSOCOM |
| Curtiss-Wright (CW) | VPX modules, tactical servers | NVIDIA RTX PRO 5000 Blackwell | VPX3-730, PacStar 431/452 | DoD primes, SOSA programs |
| EDT / EDGETAK (HEI) | Man-portable / wearable | NVIDIA Jetson Orin NX | EDGETAK, EDGETAK RF | SOCOM, dismounted soldiers |
| Anduril Industries | C4 systems (vehicle + man-portable), autonomous platforms | NVIDIA Jetson (edge); Klas Voyager compute | Menace-T, Menace-X, Lattice OS | US Army ($20B), US Space Force, USSOCOM, allied MoDs |

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Anduril Industries](https://www.anduril.com) | Costa Mesa, CA, USA | Late Private (~$28–30B valuation, Series G) | Defense technology prime; Lattice OS autonomous C2 platform; Menace-T/X rugged C4 systems on Klas Voyager hardware; $20B Army enterprise contract (March 2026); autonomous aerial, surface, and undersea vehicles. |
| [EDT / EDGETAK](https://edt.com) | Hillsboro, OR, USA | Private (HEICO subsidiary) | Man-portable wearable tactical AI inference platform (EDGETAK, launched April 2025); NVIDIA Jetson Orin NX; ATAK compatible; EDGETAK RF SDR variant (Summer 2026). |
| [Systel](https://www.systelusa.com) | San Marcos, TX, USA | Private | Kite-Strike rugged AI server; small-form-factor tactical compute for defense ground vehicles and maritime platforms. |
| [Kontron](https://www.kontron.com) | Augsburg, Germany | Public (SDAX: KTN) | European COTS rugged embedded compute; µDARC microserver for tactical edge; established embedded compute and VME/VPX board supplier to defense primes globally. |

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
| **8. Thermal Management** | Conduction-cooled chassis, cold plate assemblies, liquid cooling modules for high-density GPU | [Aavid / Boyd Corporation](https://www.boydcorp.com), internal engineering at Mercury/Curtiss-Wright; [Cryogenic Control Systems](https://www.crycon.com) | Distributed; largely US and European |
| **9. System Integration** | Qualified complete systems for specific platforms (aircraft, submarine, vehicle bay installation) | Defense primes (Lockheed Martin, Boeing, Northrop Grumman, BAE Systems) integrating COTS rugged compute; [Anduril](https://www.anduril.com) as vertically integrated exception | — |

### Key Supply Chain Notes

**⚑ NVIDIA GPU supply as critical dependency:** Mercury, OSS, and Curtiss-Wright all depend on NVIDIA GPU availability. NVIDIA allocates H100/H200 production capacity primarily to hyperscaler data center customers (Microsoft, Google, Amazon) — defense suppliers are smaller customers. During periods of GPU supply constraint (2023–2024), defense program GPU delivery was delayed. This is a structural supply chain risk for all rugged AI compute programs that is not resolved by US domestic policy, since NVIDIA GPUs are fabricated at TSMC in Taiwan.

**⚑ TSMC Taiwan concentration:** Every NVIDIA GPU, AMD/Xilinx FPGA, and a large share of Intel components used in rugged compute systems are fabricated at TSMC in Taiwan. Any disruption to TSMC production — geopolitical, natural disaster, or technical — would simultaneously affect GPU availability for commercial cloud, automotive AI, and military rugged compute. There is no near-term alternative to TSMC for leading-edge GPU nodes. The CHIPS Act is funding Intel and TSMC US fab capacity, but these facilities are years from producing GPUs at volume.

**⚑ MOSA/SOSA transition as supply chain reshaper:** DoD's push to SOSA-aligned, open-architecture components is gradually ending sole-source positions for proprietary VPX architectures. Mercury's legacy sole-source positions are at risk as programs refresh under SOSA requirements. Curtiss-Wright's first-mover advantage with Blackwell SOSA-aligned modules (VPX3-730, VPX6-731) positions it well for new SOSA program starts, but incumbent Mercury is also releasing SOSA-aligned products. The SOSA transition is structurally good for the competitive market but compresses margins as sole-source premiums erode.

**Anduril vertical integration exception:** Anduril's acquisition of Klas (Voyager ruggedized compute) is moving it out of the standard supply chain — it is increasingly its own rugged compute supplier rather than a customer of Mercury, OSS, or Curtiss-Wright. If Lattice becomes the dominant Army C2 platform, Klas Voyager hardware could displace third-party rugged servers in Army deployments.

### Supply Chain — Last Reviewed: 2026-03-26
