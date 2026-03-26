---
title: Datacenter Design & Construction
date: 2026-03-24
lastmod: 2026-03-24
draft: false
description: Next-generation datacenter design approaches — modular construction, faster time-to-power, lower cost per MW, and smarter facility architectures for AI workloads.
tags: ["datacenters", "design-construction"]
categories: ["overview"]
research_area: "datacenters/design-construction"
last_reviewed: 2026-03-24
stale_after_days: 90
---

## Overview

The conventional datacenter construction playbook — custom-designed facility, long procurement cycles, sequential trades — is being disrupted by the pace of AI infrastructure demand. McKinsey projects $6.7 trillion in cumulative global datacenter capex through 2030, with demand growing at 22% CAGR. Operators cannot build fast enough using traditional methods. The response is a shift toward modular/prefabricated construction, standardized designs that can be replicated across sites, and early contractor involvement to compress timelines. The intersection of high-density AI workloads and construction timelines is creating demand for purpose-designed AI datacenter facilities that differ significantly from legacy enterprise colocation buildings.

## Key Themes

- Traditional datacenter construction: 24–36 months from greenfield to live; AI urgency pushing toward 12–18 month targets
- Prefabricated and modular datacenter (PFMD) construction: factory-built power and cooling modules reduce on-site labor and compress schedule
- Zoned hybrid design: air-cooled zones for legacy/moderate-density workloads alongside liquid-cooled zones for AI/HPC — phased transition rather than all-or-nothing
- AI datacenter power density planning: designing for 30–100+ kW/rack from the start, not retrofitting
- Site selection criteria shifting: power availability > fiber availability; proximity to generation, substation capacity, and water supply now primary constraints
- Design standardization and replication: hyperscalers using "copy-exact" facility designs across global sites to compress schedule and reduce engineering cost
- Time-to-power as a competitive differentiator: colocation operators who can deliver power faster win hyperscaler commitments

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [MODLOGIQ](https://www.modlogiq.com) | Bend, OR, USA | Growth | Modular datacenter construction; prefabricated mechanical and electrical (M&E) modules for accelerated deployment. |
| [Compass Datacenters](https://compassdatacenters.com) | Dallas, TX, USA | Private (OMERS Infrastructure) | Purpose-built wholesale colocation; single-tenant design optimized for hyperscaler and large enterprise tenants; known for fast delivery cycles. |
| [Stack Infrastructure](https://www.stackinfra.com) | Chicago, IL, USA | Private (IFM Investors) | Wholesale colocation with AI-optimized facilities; partnership with hyperscalers for dedicated campuses. |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [DLR](https://finance.yahoo.com/quote/DLR) | [Digital Realty](https://www.digitalrealty.com) | Largest global colocation/interconnection REIT; PlatformDIGITAL modular design approach; relevant for construction/design trends at scale. |
| [EQIX](https://finance.yahoo.com/quote/EQIX) | [Equinix](https://www.equinix.com) | Global colocation and interconnection; xScale hyperscaler joint ventures; International Business Exchange (IBX) standardized design. |
| [IRON](https://finance.yahoo.com/quote/IRON) | [Ironmountain](https://www.ironmountain.com) | Data management and datacenter; Project Raven AI-optimized datacenter development. |

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
        "title": "Design & Construction",
        "symbols": [
          {"s": "NYSE:DLR", "d": "Digital Realty"},
          {"s": "NASDAQ:EQIX", "d": "Equinix"},
          {"s": "NYSE:IRON", "d": "Iron Mountain"}
        ],
        "originalTitle": "Design & Construction"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [CBRE](https://finance.yahoo.com/quote/CBRE) | [CBRE Group](https://www.cbre.com) | Largest commercial real estate firm; datacenter advisory, development management, and construction management services; Data Center Solutions practice. |
| [Mortenson](https://www.mortenson.com) | Mortenson (private) | One of the largest US datacenter construction contractors; hyperscaler campus builder; modular construction expertise. |
| [Turner Construction](https://www.turnerconstruction.com) | Turner (HOCHTIEF subsidiary) | Major datacenter construction contractor; AI campus construction experience. |

## Key Design Approaches Being Tracked

### Zoned Hybrid Cooling Design
The emerging standard for new AI datacenters mixes cooling technologies by zone rather than committing to a single approach. Air-contained zones handle legacy and moderate-density workloads; rear-door heat exchanger (RDHx) zones handle 20–40 kW/rack AI inference; direct-to-chip liquid zones handle 40–120 kW/rack GPU training clusters. A shared warm-water secondary loop connects the liquid zones to a central cooling plant (dry coolers preferred for water efficiency, chillers for hot climates). This approach allows phased densification as workloads evolve without stranded cooling infrastructure.

### Prefabricated Mechanical and Electrical (M&E) Modules
Factory-built modules containing complete power (switchgear, UPS, PDU) or cooling (CDU, dry coolers, piping) subsystems are delivered to site pre-tested and pre-commissioned, then craned into position and connected. This approach reduces on-site labor (skilled labor is the construction timeline bottleneck), improves quality consistency, and compresses schedule. Schneider Electric, Vertiv, and specialist PFMD contractors (MODLOGIQ, Corscale) offer modular approaches. Hyperscalers have largely developed proprietary modular designs.

### Copy-Exact Facility Design
Hyperscalers (Google, Microsoft, Amazon) increasingly deploy standardized facility designs across global sites rather than custom-engineered buildings. A proven design that meets power, cooling, and construction requirements is replicated with minimal modification at each new site. This compresses design timeline, enables contractor familiarity, and reduces commissioning risk. The design-standardization trend is relevant to construction contractors and M&E suppliers who gain volume through preferred vendor relationships.

### Supply Chain — Last Reviewed: 2026-03-24
