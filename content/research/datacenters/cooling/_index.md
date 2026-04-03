---
title: Datacenter Cooling
date: 2026-03-24
lastmod: 2026-03-24
draft: false
description: Liquid cooling systems for high-density AI and HPC datacenters — immersion, direct-to-chip, rear-door heat exchangers, and the companies supplying them.
tags: ["datacenters", "cooling", "liquid-cooling"]
categories: ["overview"]
research_area: "datacenters/cooling"
last_reviewed: 2026-03-24
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---

## Overview

The shift from air to liquid cooling is the defining infrastructure transition of the AI datacenter era. Traditional air cooling hits practical limits at approximately 15–20 kW per rack; NVIDIA's current H100 and GB200 GPU clusters require 40–120 kW per rack. This density gap is forcing operators to adopt liquid cooling at scale — a transition that is technically straightforward but operationally and organizationally disruptive for facilities built around air. The cooling supply chain is fragmenting into specialists at each layer: dielectric fluid makers, immersion tank manufacturers, cold plate fabricators, CDU (cooling distribution unit) providers, and systems integrators who tie the facility-side water loop to the IT equipment.

## Key Themes

- Air cooling ceiling at ~15–20 kW/rack makes it inadequate for dense GPU clusters without liquid augmentation
- Three primary liquid approaches: immersion (servers submerged in dielectric fluid), direct-to-chip (cold plates on CPUs/GPUs, air handles the rest), rear-door heat exchangers (liquid cools rack exhaust air — lowest disruption to existing IT)
- Immersion cooling enables the lowest PUE (<1.03 theoretical) and highest density but requires purpose-built tanks and fluid management — operationally incompatible with standard rack-based tooling and robot-servicing approaches without redesigned hardware (see robotics-automation section)
- Direct-to-chip is the near-term pragmatic solution for AI clusters: NVIDIA's NVLink rack reference designs, NVIDIA GB200 NVL72, and AMD MI300X all ship with liquid-cooled reference designs; standard CDU + manifold approach fits existing facility water infrastructure
- Waste heat reuse (ERE metric) increasingly economically relevant: liquid cooling return temperatures of 40–60°C can supply district heating or industrial processes; some European operators monetizing this
- Dielectric fluid supply chain: engineered fluids (3M Novec — discontinued, creating supply chain disruption; Engineered Fluids' BitCool; Shell Immersion Cooling Fluid; Submer's SmartCoolant) are a critical dependency for single-phase immersion

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Submer](https://submer.com) | Barcelona, Spain | Series B | Single-phase immersion cooling tanks and SmartCoolant fluid; ADA autonomous robot for immersion tank servicing; deployed at HPC and AI facilities globally. |
| [LiquidStack](https://liquidstack.com) | Dallas, TX, USA | Series B | Two-phase immersion cooling (liquid boils, vapor condenses, no pump required for fluid circulation); acquired from Allied Control (formerly HKUST spinout). |
| [Iceotope](https://www.iceotope.com) | Sheffield, UK | Series B | Chassis-level precision immersion cooling ("liquid-blanketed" approach — fluid circulates around individual servers without full tank immersion). |
| [GRC (Green Revolution Cooling)](https://www.grcooling.com) | Austin, TX, USA | Growth | Single-phase immersion (CarnotJet system); pioneered immersion at scale; long deployment history at HPC and crypto mining facilities. |
| [CoolIT Systems](https://www.coolitsystems.com) | Calgary, Canada | Growth | Direct-to-chip liquid cooling; Rack DCLC system; OEM partnerships with Dell, Lenovo, HPE; widely deployed in HPC. |
| [Asetek](https://www.asetek.com) | Aalborg, Denmark | Public (Oslo: ASTK) | Liquid cooling systems for HPC and enterprise; rack CDU and direct-to-chip cold plates; significant OEM server partnerships. |
| [Engineered Fluids](https://www.engineeredfluids.com) | Minneapolis, MN, USA | Growth | BitCool and ElectroCool dielectric fluids for single-phase immersion; positioned as alternative to discontinued 3M Novec products. |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [VRT](https://finance.yahoo.com/quote/VRT) | [Vertiv Holdings](https://www.vertiv.com) | Thermal management, power, and IT infrastructure for datacenters; Liebert precision cooling, CDUs, busway; significant AI datacenter exposure. |
| [OSTK / ASTK](https://finance.yahoo.com/quote/ASTK.OL) | [Asetek](https://www.asetek.com) | HPC and enterprise liquid cooling; Oslo-listed; direct-to-chip and rack CDU products. |

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
        "title": "Datacenter Cooling",
        "symbols": [
          {"s": "NYSE:VRT", "d": "Vertiv"},
          {"s": "OSLO:ASTK", "d": "Asetek"}
        ],
        "originalTitle": "Datacenter Cooling"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [ETN](https://finance.yahoo.com/quote/ETN) | [Eaton](https://www.eaton.com) | Power distribution and cooling infrastructure; significant datacenter UPS and PDU market; expanding into liquid cooling adjacencies. |
| [SCHN](https://finance.yahoo.com/quote/SCHN) | [Schneider Electric](https://www.se.com) | APC datacenter infrastructure; EcoStruxure DCIM; cooling, power, and management systems at scale; largest legacy datacenter infrastructure vendor. |
| [NVT](https://finance.yahoo.com/quote/NVT) | [nVent Electric](https://www.nvent.com) | Thermal management and enclosures; Schroff racks; expanding into liquid cooling for high-density racks. |
| [3M](https://finance.yahoo.com/quote/MMM) | [3M](https://www.3m.com) | Novec engineered fluids (discontinued 2025 due to PFAS regulation); exit created supply gap in single-phase immersion cooling fluid market. |

## Supply Chain

### Supply Chain Layers

| Layer | Key Inputs / Outputs | Companies Operating Here | Geographic Risk |
|-------|---------------------|--------------------------|-----------------|
| **1. Raw Materials** | Fluorinated compounds (dielectric fluids), copper (cold plates, CDUs), aluminum (heat sinks), stainless steel (tanks) | 3M (Novec — exiting), Solvay (Galden), Shell, Engineered Fluids | Fluorinated fluid production: US and European chemical companies; 3M exit creating supply gap |
| **2. Dielectric Fluids** | Engineered single-phase and two-phase dielectric fluids for immersion | Engineered Fluids (BitCool), Shell Immersion Cooling Fluid, Submer SmartCoolant, Solvay Galden (two-phase) | Post-3M-Novec exit: supply more distributed but still specialty chemicals with limited producers |
| **3. Heat Transfer Components** | Cold plates (direct-to-chip), heat exchangers (CDU), manifolds | CoolIT, Aavid/Boyd (thermal management), Liqtech (ceramic membrane, adjacent) | Cold plate manufacturing: North American and Asian suppliers |
| **4. Complete Cooling Systems** | Immersion tanks, rack CDUs, RDHx units, precision air handlers | Submer, LiquidStack, GRC, Iceotope, CoolIT, Asetek, Schneider Electric (APC InRow) | Assembly: distributed; tank manufacturing requires welding/fabrication capability |
| **5. Facility Integration** | Chilled water loops, dry coolers, cooling towers, CDU interconnect | Vertiv, Schneider Electric, Johnson Controls (York chillers), CBRE (design/build) | Chillers and cooling towers: global manufacturing base |

### Key Supply Chain Notes

**3M Novec discontinuation:** 3M announced discontinuation of its PFAS-based Novec engineered fluid product line in 2025 due to regulatory pressure around per- and polyfluoroalkyl substances (PFAS). Novec was the dominant fluid for single-phase immersion cooling. Operators with existing Novec-based immersion deployments face a fluid supply transition, and new deployments are shifting to alternatives: Engineered Fluids BitCool, Shell's immersion fluid, and Submer's SmartCoolant. This represents a significant supply chain disruption for the immersion cooling sector — track replacement fluid qualification status at major operators.

**PUE reality check:** Data center operators frequently quote design PUE rather than measured operational PUE. Liquid cooling achieves genuinely low PUE (1.02–1.10 in practice), but the benefit is only real if the facility-side cooling infrastructure (chillers, cooling towers, dry coolers) is also efficient. A liquid-cooled IT load connected to an inefficient chiller plant can have worse PUE than a well-designed air-cooled facility with economizer. Verify PUE claims by asking for annualized measured figures, not design targets.

**⚑ Shared challenge — robot servicing incompatibility:** Standard single-phase immersion tanks (Submer SmartPod, GRC CarnotJet) require servers to be lifted vertically out of fluid — a fundamentally different motion than horizontal rack-slide operations. This incompatibility with conventional robot-servicing approaches (which assume rack-slide) is the core design problem that Submer's ADA robot and SoftBank's cable-less rack design address from different angles. See `robotics-automation/_index.md` and `robotics-automation/softbank-robot-rack.md`.

### Supply Chain — Last Reviewed: 2026-03-24
