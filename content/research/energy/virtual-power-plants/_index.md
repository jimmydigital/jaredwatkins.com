---
title: "Virtual Power Plants"
date: 2026-07-18
lastmod: 2026-07-18
draft: false
description: "Companies aggregating distributed energy resources — home batteries, smart thermostats, EV chargers, and commercial/industrial load — into virtual power plants (VPPs) sold to utilities and, increasingly, to AI datacenter operators as fast-to-market grid capacity."
research_area: "energy/virtual-power-plants"
last_reviewed: 2026-07-18
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9
  disable: false
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.

## Overview

A virtual power plant (VPP) aggregates many small, customer-sited energy resources — home batteries, smart thermostats, EV chargers, rooftop solar, and commercial/industrial curtailable load — and operates them together as if they were a single power plant, bidding the combined flexibility into utility programs or wholesale electricity markets. This section tracks the companies building and operating VPPs in North America, split roughly into two models: **residential/behind-the-meter aggregators** ([Sunrun]({{< relref "sunrun.md" >}}), [Tesla Energy]({{< relref "tesla-energy-vpp.md" >}}), [Renew Home]({{< relref "renew-home.md" >}}), and — covered in [Energy/Batteries]({{< relref "../batteries/_index.md" >}}) — [Base Power]({{< relref "../batteries/base-power.md" >}})) that own or partner on home hardware directly, and **commercial/industrial (C&I) demand-response platforms** ([Voltus]({{< relref "voltus.md" >}}), [Enel North America]({{< relref "enel-north-america-vpp.md" >}}), [CPower]({{< relref "cpower.md" >}}), [Uplight]({{< relref "uplight.md" >}})) that aggregate business and industrial load rather than individual homes.

As of mid-2026, the space has been reshaped by AI datacenter demand: hyperscalers facing multi-year grid interconnection queues are increasingly financing VPP capacity as a faster alternative, most visibly in the June 24, 2026 Sunrun/Tesla/Renew Home joint 16.8 GW program explicitly marketed to data center operators, and Voltus's "bring-your-own-capacity" product (first customer: Google). This reframes VPPs from a rooftop-solar-adjacent grid-services niche into direct competition for datacenter power dollars — the same demand pool that companies like [Base Power]({{< relref "../batteries/base-power.md" >}}) and [Span]({{< relref "../../datacenters/distributed-compute/span.md" >}}) are also pursuing from different angles (residential battery VPP and distributed AI compute siting, respectively).

## Key Themes

- **Two distinct aggregation models:** residential/behind-the-meter (batteries, thermostats, owned or partnered hardware in individual homes) vs. commercial/industrial demand response (curtailable load at businesses and factories) — different customer relationships, different regulatory pathways, different economics
- **AI datacenter demand is the current growth driver:** VPP capacity is increasingly sold directly to hyperscalers and AI cloud operators as a faster alternative to new generation or transmission, not just to utilities for peak shaving
- **Consolidation is common:** several major players here are themselves the product of mergers/acquisitions (Renew Home = Google Nest Renew + OhmConnect; CPower = Comverge + Constellation C&I demand response, later LS Power-owned; Uplight = six-company merger, later acquired AutoGrid, later majority-acquired by Octopus Energy) — track ownership carefully, as "who owns whom" changes the incentive structure
- **Scale claims vary widely in what they measure:** installed capacity, enrolled/connected capacity, and actually-dispatched capacity are three different numbers that get blended in press materials — flag which one a company is citing
- **PJM is the current epicenter:** rising PJM capacity prices driven by datacenter load growth are the immediate commercial trigger for most of 2026's major VPP announcements

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Renew Home](https://www.renewhome.com) | Palo Alto, CA, USA | Private (SIP-majority-owned) | Smart-thermostat residential VPP; spinout/merger of Google's Nest Renew and OhmConnect; targeting 50 GW managed demand by 2030. |
| [Voltus]({{< relref "voltus.md" >}}) | San Francisco, CA, USA | Private (Series C-stage; SPAC merger terminated 2022) | C&I demand-response/VPP technology platform; "bring-your-own-capacity" product for hyperscalers (Google first customer). |
| [CPower]({{< relref "cpower.md" >}}) | Baltimore, MD, USA | Private (LS Power-owned) | C&I demand response and DER aggregation; formed from Comverge + Constellation demand-response units. |
| [Uplight]({{< relref "uplight.md" >}}) | Boulder, CO, USA | Private (Octopus Energy majority stake, 2026) | Utility-facing DERMS/VPP software platform; owns AutoGrid (acquired 2024). |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [RUN](https://finance.yahoo.com/quote/RUN) | [Sunrun]({{< relref "sunrun.md" >}}) | Largest US residential solar/storage installer; operates a battery-based VPP ("Shift") across multiple states. |
| [TSLA](https://finance.yahoo.com/quote/TSLA) | [Tesla Energy]({{< relref "tesla-energy-vpp.md" >}}) | Powerwall residential battery VPPs orchestrated via Autobidder software, alongside the separate Megapack utility-scale storage business. |

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
        "title": "Virtual Power Plants",
        "symbols": [
          {"s": "NASDAQ:RUN", "d": "Sunrun"},
          {"s": "NASDAQ:TSLA", "d": "Tesla"}
        ],
        "originalTitle": "Virtual Power Plants"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [ENEL.MI](https://finance.yahoo.com/quote/ENEL.MI) | [Enel North America]({{< relref "enel-north-america-vpp.md" >}}) | US/Canada subsidiary of Italian utility giant Enel; VPP Connect/Enel X Flex is a top-3-ranked North American C&I VPP aggregator (Wood Mackenzie). |
