---
title: "Stratospheric Airships"
date: 2026-08-03
lastmod: 2026-08-03
draft: false
description: "Autonomous, lighter-than-air stratospheric airships (dirigibles) designed for long-duration station-keeping at 18-20km altitude, carrying telecom, Earth-observation, or ISR payloads."
research_area: "hale-haps/airships"
last_reviewed: 2026-08-03
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.7
  disable: false
---

# Stratospheric Airships

Unlike fixed-wing HAPS, which fly forward continuously to generate lift, stratospheric airships are lighter-than-air (typically helium-filled) dirigibles that use their own buoyancy for lift and rely on electric propulsion only for station-keeping and maneuvering against high-altitude winds. That different lift model generally trades some efficiency for a larger payload bay and a more stable sensor platform — the two entries in this subsection sit at opposite ends of the development spectrum: one flying multi-day missions today, the other still working toward a first flight after a decade of state-funded R&D.

## Entries

- [Thales Alenia Space — Stratobus]({{< relref "thales-alenia-space-stratobus.md" >}}) — 140-metre autonomous helium airship (JV: Thales 67% / Leonardo 33%); year-long station-keeping design target; €17M French PIA funding (2016) + €43M EU EuroHAPS contract (2023); no confirmed flight date as of 2026

**Documented elsewhere on this site:** [Sceye]({{< relref "../../drone-detection/high-altitude-platforms/sceye.md" >}}) — New Mexico-built solar-powered stratospheric airship; completed a 12-day, 6,400-mile flight (Mar-Apr 2026); EO/IR, methane, and hyperspectral payloads. Sceye's full entry lives in the Drone Detection section because its persistent-altitude architecture is directly relevant to C-UAS/missile-detection payload integration, alongside its civil Earth-observation and telecom missions documented there.

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Sceye](https://sceye.com) | USA (Moriarty, NM) | Growth (Series C, NASA award) | Solar-powered stratospheric airship; Earth observation, methane/emissions, comms relay — [full entry]({{< relref "../../drone-detection/high-altitude-platforms/sceye.md" >}}) |

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [HO.PA](https://finance.yahoo.com/quote/HO.PA) | [Thales](https://www.thalesgroup.com) | 67% owner of the Thales Alenia Space JV; majority partner behind Stratobus |
| [LDO.MI](https://finance.yahoo.com/quote/LDO.MI) | [Leonardo](https://www.leonardo.com) | 33% owner of the Thales Alenia Space JV |

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
        "title": "Stratospheric Airship Parents",
        "symbols": [
          {"s": "EPA:HO", "d": "Thales"},
          {"s": "BIT:LDO", "d": "Leonardo"}
        ],
        "originalTitle": "Stratospheric Airship Parents"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->
