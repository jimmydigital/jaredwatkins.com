---
title: Datacenter Power Infrastructure
date: 2026-03-24
lastmod: 2026-03-24
draft: false
description: Power sourcing, behind-the-meter generation, grid interconnection, and energy storage for AI-scale datacenters.
tags: ["datacenters", "power-infrastructure"]
categories: ["overview"]
research_area: "datacenters/power-infrastructure"
last_reviewed: 2026-03-24
stale_after_days: 90
---

## Overview

Power availability has displaced fiber connectivity as the primary datacenter site selection constraint. A 1 GW campus (now routinely announced by hyperscalers) requires as much electricity as a medium-sized city. Grid interconnection queues in the US now run 4–7 years in many regions, forcing operators to source power through alternative pathways: behind-the-meter natural gas turbines, nuclear power purchase agreements (PPAs), and — increasingly — commitments to small modular reactors (SMRs). The energy intensity of AI workloads (GPU clusters running 24/7 at near-maximum utilization) also eliminates the load variability that traditional demand-response programs relied on, making power infrastructure planning more deterministic but also more demanding.

## Key Themes

- Grid interconnection delays (4–7 years in constrained US markets) forcing behind-the-meter power sourcing
- Natural gas combustion turbines as the near-term solution for large campuses — faster to permit and build than grid upgrades
- Nuclear PPAs: Microsoft (Three Mile Island restart), Amazon (Susquehanna), Google (Kairos Power SMR) — establishing nuclear as a mainstream datacenter power source
- SMRs: NuScale (cancelled first project), TerraPower, X-energy, Kairos Power all pursuing datacenter-adjacent deployments; 2030–2035 timeframe realistic for first commercial SMR datacenter power
- Battery energy storage (BESS): used primarily for ride-through and UPS replacement rather than capacity; LFP-based BESS replacing traditional VRLA UPS in new builds
- PUE implications of power sourcing: behind-the-meter gas turbines have waste heat that can improve facility ERE (Energy Reuse Effectiveness) if captured
- "24/7 clean power" vs. REC (Renewable Energy Certificate) accounting — a significant integrity gap in sustainability claims

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Kairos Power](https://kairospower.com) | Alameda, CA, USA | Late Private | Molten salt-cooled fluoride high-temperature reactor (FHR); Google signed first commercial SMR power purchase agreement with Kairos (December 2023); first unit targeting 2030. |
| [X-energy](https://x-energy.com) | Rockville, MD, USA | Late Private | Xe-100 pebble bed high-temperature gas-cooled reactor; Amazon Web Services announced investment and power agreement (2023). |
| [TerraPower](https://www.terrapower.com) | Bellevue, WA, USA | Late Private (Bill Gates-backed) | Natrium sodium fast reactor; Wyoming plant under construction (DOE funded); not specifically datacenter-focused but relevant as near-term SMR. |
| [Bloom Energy](https://www.bloomenergy.com) | San Jose, CA, USA | Public (NYSE: BE) | Solid oxide fuel cells for on-site power generation; growing datacenter deployments as behind-the-meter alternative; Microsoft and other hyperscalers as customers. |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [BE](https://finance.yahoo.com/quote/BE) | [Bloom Energy](https://www.bloomenergy.com) | Fuel cell power for datacenters; on-site generation avoiding grid interconnection delays; natural gas or hydrogen-ready. |
| [CEG](https://finance.yahoo.com/quote/CEG) | [Constellation Energy](https://www.constellationenergy.com) | Largest US nuclear fleet operator; Three Mile Island Unit 1 restart (Crane Clean Energy Center) for Microsoft 20-year PPA; direct nuclear-to-datacenter contracting model. |
| [VST](https://finance.yahoo.com/quote/VST) | [Vistra Corp](https://www.vistracorp.com) | Power generation including nuclear (Comanche Peak); pursuing datacenter PPAs; large Texas power generation footprint relevant to AI datacenter clustering in Texas. |

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
        "title": "Power Infrastructure",
        "symbols": [
          {"s": "NYSE:BE", "d": "Bloom Energy"},
          {"s": "NASDAQ:CEG", "d": "Constellation Energy"},
          {"s": "NYSE:VST", "d": "Vistra"}
        ],
        "originalTitle": "Power Infrastructure"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [ETN](https://finance.yahoo.com/quote/ETN) | [Eaton](https://www.eaton.com) | UPS systems, PDUs, busway, switchgear for datacenter power distribution; transitioning customers to LFP-based UPS from legacy VRLA. |
| [SCHN](https://finance.yahoo.com/quote/SCHN) | [Schneider Electric](https://www.se.com) | Galaxy UPS, PDUs, busway, DCIM power monitoring; largest legacy datacenter power infrastructure vendor. |
| [VRT](https://finance.yahoo.com/quote/VRT) | [Vertiv Holdings](https://www.vertiv.com) | UPS (Liebert), power distribution, DC power; significant AI datacenter power infrastructure exposure. |
| [GE](https://finance.yahoo.com/quote/GE) | [GE Vernova](https://www.gevernova.com) | Gas turbines, transformers, grid interconnection equipment; critical supplier for behind-the-meter generation and grid connection infrastructure. |

## Supply Chain

### Power Sourcing Options and Trade-offs

| Source | Time to Power | Cost | Carbon Profile | Availability |
|--------|--------------|------|----------------|--------------|
| Grid interconnection (utility) | 4–7 years (US constrained markets) | Lowest ongoing cost | Depends on grid mix | Constrained by queue |
| Behind-the-meter natural gas turbine | 2–3 years | Moderate capex, fuel cost | Carbon-intensive unless CCS | Broadly available |
| Nuclear PPA (existing plant) | 1–2 years (contract negotiation) | Premium pricing | Carbon-free 24/7 | Limited to operators near plants |
| Onsite fuel cells (Bloom Energy) | 12–18 months | High capex, fuel cost | Lower carbon than grid average (nat gas) | Broadly available |
| SMR (small modular reactor) | 8–12 years (development + construction) | Unknown (first-of-kind premium) | Carbon-free 24/7 | 2030–2035 earliest |
| Solar + BESS | 2–3 years | Moderate | Carbon-free when generating | Intermittent; BESS required for 24/7 |

### Key Supply Chain Notes

**Transformer shortage:** Large power transformers (>100 MVA) have lead times of 2–3 years from US manufacturers (ABB, Siemens Energy, GE Vernova). This is a binding constraint for large campus buildout — the transformer must be ordered before site selection is finalized. Transformer manufacturing capacity is limited and primarily located in the US, Germany, and South Korea. Chinese transformer manufacturers (TBEA, CHINT) are not typically used in US datacenter supply chains for security reasons.

**Three Mile Island restart precedent:** Microsoft's 20-year PPA with Constellation for the Crane Clean Energy Center (restarted TMI Unit 1) established the template for large-scale nuclear datacenter contracts. The deal (announced September 2023, plant restarted September 2024) demonstrated that existing nuclear facilities can be commercially restarted specifically to serve datacenter demand. Watch for similar restart announcements at other prematurely shuttered plants (Palisades, Duane Arnold).

**LFP displacing VRLA in UPS:** Traditional valve-regulated lead-acid (VRLA) batteries in datacenter UPS systems are being replaced by lithium iron phosphate (LFP) battery systems in new builds. LFP offers longer cycle life, smaller footprint, faster charge acceptance, and no off-gassing. Eaton, Schneider Electric, and Vertiv all offer LFP UPS options. This creates overlap with the energy/batteries supply chain — the same CATL, BYD, and Samsung SDI cell manufacturers supplying EV and grid storage are supplying LFP UPS batteries.

**⚑ Shared supply chain — LFP cells:** LFP cells for datacenter UPS/BESS from CATL and BYD are the same cells used in grid-scale storage and increasingly in AMR robot batteries (see robotics/power-systems). A supply crunch in LFP cells would simultaneously affect datacenter UPS infrastructure, grid storage deployments, and industrial robotics.

### Supply Chain — Last Reviewed: 2026-03-24
