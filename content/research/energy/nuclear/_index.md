---
title: Nuclear Energy Research
date: 2026-03-25
lastmod: 2026-03-25
draft: false
description: Research on nuclear power technologies, small modular reactors (SMRs), and the companies developing next-generation nuclear for AI datacenters, industrial power, and grid decarbonization.
tags: ["nuclear", "smr", "energy"]
categories: ["overview"]
research_area: "energy/nuclear"
last_reviewed: 2026-03-25
stale_after_days: 180
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---

## Overview

Tracks small modular reactor (SMR) developers and advanced nuclear technologies, with particular focus on companies pursuing faster, cheaper deployment models and the emerging AI datacenter power demand that is accelerating commercial nuclear investment. Traditional large nuclear (1 GW+ plants) is covered only where relevant to SMR supply chain or regulatory precedent.

## Key Themes

- SMR construction cost and timeline — the core claim every company must prove (target: ~$5,000/kW, 3–5 years; industry history: $13,000+/kW, 10–15 years)
- Datacenter nuclear PPAs as the first commercial demand signal for SMRs
- NRC licensing pathway evolution: Combined License (COL) vs. Construction Permit + Operating License; modular construction resequencing approvals
- HALEU fuel supply chain as a potential chokepoint for non-LWR designs
- Shipyard/modular fabrication as the cost-reduction mechanism — analogous to offshore wind jacket manufacturing

## Deployment Status Tracker

| Company | Reactor | Fuel | Key Milestone | Commercial Target |
|---------|---------|------|---------------|-------------------|
| [GE Vernova Hitachi]({{< relref "ge-hitachi-bwrx300.md" >}}) | BWRX-300 (LWR, 300 MW) | LEU | **Construction license issued April 2025** — Darlington, ON | End 2029 |
| [TerraPower]({{< relref "terrapower.md" >}}) | Natrium (SFR, 345 MW) | LEU metallic | **NRC construction permit issued late 2025** — Kemmerer, WY | 2030 |
| [Kairos Power]({{< relref "kairos-power.md" >}}) | KP-FHR (HTGR, 50 MW) | TRISO/LEU | **Nuclear construction commenced May 2025** — Hermes demo, Oak Ridge TN | Hermes 2: 2030 |
| [X-energy]({{< relref "x-energy.md" >}}) | Xe-100 (HTGR, 80 MW×4) | TRISO/HALEU | **NRC construction permit application docketed May 2025** — Seadrift, TX (Dow) | ~2030 |
| [Oklo]({{< relref "oklo.md" >}}) | Aurora (SFR, 75 MW) | HALEU metallic | **Groundbreaking September 2025** — Idaho National Laboratory | Late 2027–2028 |
| [Blue Energy]({{< relref "blue-energy.md" >}}) | Modular LWR (1.5 GW) | LEU | **NRC topical report approved** — Port of Victoria TX (Crusoe); construction Q2 2026 | Gas 2028; Nuclear 2031 |

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Technology |
|---------|-----|-------|-----------|
| [Blue Energy](https://blueenergy.co) | Edinburgh / San Antonio | Series A ($45M) | Modular LWR; shipyard construction; gas-to-nuclear conversion; 1.5 GW at Port of Victoria TX for [Crusoe]({{< relref "../../datacenters/design-construction/crusoe.md" >}}) |
| [Kairos Power](https://kairospower.com) | Alameda, CA | Private (~$650M raised) | KP-FHR fluoride salt + TRISO pebbles; Hermes nuclear construction underway Oak Ridge; Google/TVA PPA 500 MW by 2035 |
| [X-energy](https://x-energy.com) | Rockville, MD | Private (~$1.5B raised) | Xe-100 pebble-bed HTGR; Dow Seadrift TX NRC application docketed; Amazon anchor investor; TRISO-X fuel subsidiary |
| [TerraPower](https://terrapower.com) | Bellevue, WA | Private | Natrium SFR + molten salt storage; Bill Gates-backed; Kemmerer WY NRC construction permit issued; Bechtel EPC |

### Public Companies

| Ticker | Company | Technology |
|--------|---------|-----------|
| [OKLO](https://finance.yahoo.com/quote/OKLO) | [Oklo](https://oklo.com) | Aurora sodium fast microreactor (75 MW); Sam Altman chairman; groundbreaking INL Sept 2025; ~18 GW order book (mostly LOIs); HALEU fuel |
| [SMR](https://finance.yahoo.com/quote/SMR) | [NuScale Power](https://www.nuscalepower.com) | LWR SMR; first NRC Design Certification 2022; CFPP project cancelled 2023; pivoting to export markets and small-site applications |
| [GEV](https://finance.yahoo.com/quote/GEV) | [GE Vernova / GE Hitachi](https://www.gevernova.com) | BWRX-300; construction license issued Darlington ON April 2025; most advanced Western SMR with active construction authorization |
| [BWXT](https://finance.yahoo.com/quote/BWXT) | [BWX Technologies](https://www.bwxt.com) | Nuclear component manufacturer; only US TRISO fuel producer; DoD microreactor program; critical supply chain player for Kairos, X-energy |

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
        "title": "Nuclear",
        "symbols": [
          {"s": "NYSE:OKLO", "d": "Oklo"},
          {"s": "NYSE:SMR", "d": "NuScale Power"},
          {"s": "NYSE:GEV", "d": "GE Vernova"},
          {"s": "NYSE:BWXT", "d": "BWX Technologies"}
        ],
        "originalTitle": "Nuclear"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [LEU](https://finance.yahoo.com/quote/LEU) | [Centrus Energy](https://www.centrusenergy.com) | Only NRC-licensed US HALEU enricher; critical chokepoint for Oklo, X-energy, Kairos commercial scale-up |
| [WSTG](https://finance.yahoo.com/quote/WSTG) | [Westinghouse](https://www.westinghousenuclear.com) | AP300 SMR (derivative of NRC-certified AP1000); multiple LOIs; established regulatory relationships; not yet at construction permit stage |

## Supply Chain Notes

- **Reactor pressure vessels and heavy forgings:** Japan Steel Works and Doosan Heavy Industries are primary sources; lead times 3–5+ years; Hitachi relationship gives GEH priority access
- **HALEU fuel:** Required for Oklo (Aurora), X-energy (Xe-100 via TRISO-X), Kairos (KP-FHR pebbles); Centrus is the only NRC-licensed US HALEU enricher; X-energy's TRISO-X TX-1 facility in Oak Ridge is the only US HALEU fuel fabrication plant under construction
- **TRISO fuel:** BWXT (Lynchburg VA) is the only US TRISO particle manufacturer; Kairos and X-energy both depend on BWXT; capacity expansion underway but timeline must pace with multiple reactor programs simultaneously
- **Li-7 enrichment:** Required for Kairos's fluoride salt coolant (FLiBe); no US commercial Li-7 enrichment capability currently; DOE/ORNL developing domestic capability
- **Turbine generators:** GE Vernova, Siemens Energy (X-energy/Oklo named); standard power gen supply chain; less constrained than nuclear-specific components
- **Sodium systems expertise:** TerraPower (Natrium) and Oklo (Aurora) both use sodium cooling; limited number of qualified fabricators and constructors with sodium fast reactor experience in the US