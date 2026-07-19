---
title: "High-Altitude Platforms (Airships & Balloons)"
date: 2026-07-17
lastmod: 2026-07-17
draft: false
description: "Stratospheric airships and balloons (HAPS) as persistent sensor platforms for drone and cruise-missile detection — including dual-use systems originally built for imagery, comms, or ELINT."
research_area: "drone-detection/high-altitude-platforms"
last_reviewed: 2026-07-17
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.7
  disable: false
---

# High-Altitude Platforms (Airships & Balloons)

Stratospheric airships and balloons — High Altitude Platform Systems (HAPS) — flown at 60,000–95,000 ft to provide a persistent, elevated vantage point for radar, RF/ELINT, and EO/IR sensors. Unlike ground-based or tower-mounted C-UAS sensors, altitude lets these platforms see over the horizon and look down on low-flying threats (drones, cruise missiles) that terrain and curvature hide from ground radar — the same physics that made tethered aerostats like [JLENS](#legacy-context-jlens) attractive for cruise-missile defense, now applied with free-flying, station-keeping stratospheric platforms instead of tethers.

**Scope note:** Few of these companies market themselves primarily as drone/missile-detection vendors — most were built for earth observation, telecom relay, or general ISR/ELINT, and are being pulled toward the C-UAS and integrated-air-defense mission as a secondary or emerging use case. That crossover is itself the story: persistent stratospheric sensing is being recognized as a missing layer between ground-based C-UAS ([Hardware]({{< relref "../hardware/_index.md" >}})) and satellites, and several vendors here are now integrating directly with counter-drone companies elsewhere in this section (see [Ondas/World View/Sentrycs](#ondas-world-view-sentrycs-integration) below).

## Entries

- [Sceye]({{< relref "sceye.md" >}}) — New Mexico-built solar-powered stratospheric airship (HAPS); 12-day, 6,400-mile test flight (Mar 2026); EO/IR, methane, and hyperspectral payloads; NASA-funded sensor work
- [World View / Ondas Stratollite]({{< relref "world-view-stratollite.md" >}}) — Tucson stratospheric balloon (EO/IR/SIGINT); acquired by Ondas (ONDS) in 2026 and integrated with Sentrycs counter-UAS and Palantir AIP into a stratosphere-to-ground ISR/C-UAS stack
- [Aerostar]({{< relref "aerostar.md" >}}) — Sioux Falls-based stratospheric balloon and airship maker (Thunderhead); Airbus U.S. partnership; flying Army HELIOS/HAP-DS experimentation missions over the Pacific
- [Urban Sky]({{< relref "urban-sky.md" >}}) — Denver Microballoon (mHAB); AFRL STRATFI-funded; Project Wallabee paired its balloon with Applied Intuition's autonomous target-recognition sensor for the Army/Joint Staff J-7
- [TCOM]({{< relref "tcom.md" >}}) — Maryland tethered aerostat maker; radar/SIGINT payloads for cruise-missile, drone, and low-flying-aircraft detection; direct descendant of the JLENS mission set
- [Hemeria / Safran BalMan]({{< relref "hemeria-balman.md" >}}) — French maneuverable stratospheric balloon with Safran.AI-enabled real-time ELINT/EW signal detection and classification
- [Kalam Labs]({{< relref "kalam-labs.md" >}}) — India (Lucknow) balloon-launched stratospheric UAV; EO/IR/hyperspectral payloads; deployed at Pokhran and along the Line of Actual Control

## Government Programs Driving This Market

These aren't companies, but they explain why the vendors above are pivoting toward detection missions — noted here for context, not as standalone entries:

- **Army HELIOS / HAP-DS** — High-Altitude Extended-Range Long-Endurance Intelligence Observation System and its Deep Sensing experimentation line; soliciting sub-15-lb radar, COMINT, and ELINT payloads for balloons at 60,000+ ft, explicitly to "detect, locate, identify, and track" targets including for air/missile defense cueing
- **COLD STAR** — DoD's Covert Long-Dwell Stratospheric Architecture; originally counter-narcotics balloon surveillance (2019, ~25 balloons over South Dakota), transitioned toward broader military use
- **Project Wallabee** — Army G-2 / Joint Staff J-7 test pairing Urban Sky's balloon with an Applied Intuition autonomous target-recognition sensor (2026)
- **JLENS** (legacy) — Army's tethered-aerostat Joint Land Attack Cruise Missile Defense Elevated Netted Sensor; proved the concept (elevation solves the low-altitude cruise-missile/drone detection problem) but was cancelled after a 2015 tether-break incident; TCOM's current radar aerostat line is the closest commercial descendant

## Ondas / World View / Sentrycs Integration

Worth calling out explicitly because it directly connects this subtopic to the rest of the section: after acquiring World View in 2026, Ondas (ONDS) — already the parent of [Sentrycs]({{< relref "../hardware/sentrycs.md" >}}) — began integrating World View's Stratollite stratospheric ISR with Sentrycs' ground-based Cyber-over-RF counter-drone system and Ondas' own Optimus tactical drone platform, with Palantir's AIP tying the layers together. This is the clearest example of a stratospheric sensor company being folded directly into a counter-drone product line rather than staying a standalone earth-observation or comms business.

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Sceye](https://sceye.com) | USA (Roswell, NM) | Growth (Series funding + NASA award, 2026) | Solar-powered stratospheric airship (HAPS); Earth observation, methane/emissions, comms relay |
| [Aerostar](https://aerostar.com) | USA (Sioux Falls, SD) | Growth (division of Raven Industries/CNH) | Stratospheric balloons and airships (Thunderhead); Airbus partnership; Army HELIOS experimentation |
| [Urban Sky](https://www.urbansky.com) | USA (Denver, CO) | Series B ($30M, Feb 2025) | Microballoon (mHAB) stratospheric imaging/sensing; AFRL STRATFI contract; Project Wallabee |
| [Hemeria](https://www.hemeria-group.com) | France | Private (Safran MoU, Jun 2026) | BalMan maneuverable stratospheric balloon; AI-enabled ELINT/EW with Safran.AI |
| [Kalam Labs](https://kalamlabs.io) | India (Lucknow) | Early (~$2M raised, Lightspeed) | Balloon-launched stratospheric UAV; EO/IR/hyperspectral; defense deployments at Pokhran/LAC |
| [Near Space Labs](https://www.nearspacelabs.com) | USA (Brooklyn, NY) | Series B ($20M) | Swift stratospheric balloon imaging (7cm resolution); insurance/earth observation today, dual-use sensing platform |

### Public Companies / Recent M&A

| Ticker | Company | Mission |
|--------|---------|---------|
| [ONDS](https://finance.yahoo.com/quote/ONDS) | [Ondas Holdings](https://ondas.com) | Acquired World View (2026, ~$150M) for its Stratollite stratospheric ISR platform; integrating with Sentrycs C-UAS and DZYNE ISR under one multi-domain stack |

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| — (private) | [TCOM, L.P.](https://tcomlp.com) | Tethered aerostat radar systems; missile/cruise-missile/drone detection; direct heritage from the Army's JLENS program |
| [AIR](https://finance.yahoo.com/quote/AIR) | [Airbus U.S. Space & Defense](https://www.airbus.com/en) | Partnered with Aerostar on stratospheric systems demos for US defense applications (2024–2026) |
| [SAF.PA](https://www.google.com/finance/quote/SAF:EPA) | [Safran Electronics & Defense](https://www.safran-group.com) | Safran.AI partnership with Hemeria on BalMan ELINT/EW balloon (2026) |

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
        "title": "Stratospheric ISR",
        "symbols": [
          {"s": "NASDAQ:ONDS", "d": "Ondas / World View"},
          {"s": "EPA:AIR", "d": "Airbus"},
          {"s": "EPA:SAF", "d": "Safran"}
        ],
        "originalTitle": "Stratospheric ISR"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->
