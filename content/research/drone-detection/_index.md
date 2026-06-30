---
title: "Drone Detection"
date: 2026-06-05
lastmod: 2026-06-05
draft: false
description: "Detection methods, hardware, software, and open-source tools for identifying unauthorized drones at critical infrastructure, including drone-vs-bird discrimination."
research_area: "drone-detection"
last_reviewed: 2026-06-05
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9
  disable: false
---

{{<steering>}}

## Drone Detection Section — Steering Instructions

This section covers counter-UAS (C-UAS) detection as applied to **critical infrastructure protection**: identifying unauthorized surveillance drones and potential attack drones, with emphasis on systems deployable today.

### Editorial Focus

**Primary use case:** Protecting fixed critical infrastructure (power substations, water treatment, emergency shelters, data centers, government facilities) from unauthorized drone surveillance and armed drone threats.

**Key threat model:**
- Drones **with no direct RF control link** — fiber-optic tethered or pre-programmed autonomous waypoint flights (cannot be detected by RF monitoring)
- Compliant US drones broadcasting FAA Remote ID (detectable but low priority threat)
- Consumer/commercial drones with RF control (standard threat)

**Prioritize:**
- Open-source detection projects (software-usable today)
- Multi-sensor fusion systems that discriminate drones from birds
- Micro-Doppler radar as the primary detection method vs. alternatives
- Counter-drone-drone (interceptor drone) approaches
- Solutions deployable without DoD/federal authorization (note legal constraints)

**Important legal context for entries:** Under the FAA Reauthorization Act and current federal law, RF jamming and drone takeover (cyber) countermeasures are **only authorized for federal agencies** (DOD, DHS, DOJ, FAA, Secret Service). Critical infrastructure operators typically may only detect and track — not interdict — unless specifically authorized. Document this constraint in relevant entries.

### Subtopic Structure

```
content/research/drone-detection/
  _index.md                          ← this file
  detection-methods/
    _index.md                        ← overview of detection modalities
    micro-doppler-radar.md           ← primary detection method entry
    rf-detection.md                  ← RF/Remote ID monitoring
    acoustic-detection.md            ← acoustic signature analysis
    optical-thermal-detection.md     ← EO/IR camera approaches
    multi-sensor-fusion.md           ← sensor fusion architectures
  open-source/
    _index.md
    opendroneid.md                   ← OpenDroneID stack
    dji-droneid-decoder.md           ← DJI proprietary DroneID decoding
    ardupilot-remoteid.md            ← ArduPilot RemoteID
  hardware/
    _index.md
    dedrone.md                       ← Dedrone by Axon
    droneshield.md                   ← DroneShield (ASX:DRO)
    fortem-technologies.md           ← Fortem SkyDome + DroneHunter
    d-fend-solutions.md              ← D-Fend EnforceAir
    aaronia-aartos.md                ← Aaronia AARTOS
    robin-radar-iris.md              ← Robin Radar IRIS
    marduk-technologies.md           ← Marduk Piraya (passive optical)
  counter-drone-platforms/
    _index.md
    fortem-dronehunter.md            ← DroneHunter F700 interceptor
    rafael-hunter-eagle.md           ← Rafael Hunter Eagle / Ghost Hunter
```

### Tags for This Section

- Detection method: `micro-doppler`, `rf-detection`, `acoustic`, `optical`, `thermal`, `multi-sensor-fusion`, `remote-id`
- Threat type: `fiber-optic-threat`, `rf-dark`, `autonomous-waypoint`, `swarm`
- Platform: `fixed-site`, `mobile`, `man-portable`, `vehicle-mounted`
- Application: `critical-infrastructure`, `defense`, `public-safety`
- Regulatory: `dhs-authorized`, `dod-authorized`, `commercial-legal`

### Review Cadence

90 days — fast-moving space with regulatory changes and new threat vectors (fiber-optic FPV drone proliferation).

{{</steering>}}

# Drone Detection

A knowledge base on detecting unauthorized drones at critical infrastructure — power, water, emergency shelters, and secure facilities. Covers detection physics (micro-Doppler radar, RF, acoustic, optical), open-source tools, commercial hardware, and counter-drone-drone platforms.

**Scope:** Detection and classification systems usable today, with emphasis on drone-vs-bird discrimination and threats that assume no RF control link.

---

## Topic Areas

- [Detection Methods]({{< relref "detection-methods/_index.md" >}}) — Micro-Doppler radar, RF/Remote ID, acoustic, optical, and sensor fusion
- [Threat Taxonomy]({{< relref "threat-taxonomy.md" >}}) — Classification of drone threats: surveillance, RF attack, fiber-optic FPV, autonomous, and swarms
- [Regulatory Framework]({{< relref "regulatory-framework.md" >}}) — US C-UAS legal landscape: who can detect, who can interdict, applicable statutes, CISA guidance
- [Open Source Projects]({{< relref "open-source/_index.md" >}}) — OpenDroneID, DJI DroneID decoders, acoustic ML pipeline, and community tools
- [Commercial Hardware]({{< relref "hardware/_index.md" >}}) — Dedrone, DroneShield, Fortem, D-Fend, Aaronia, Robin Radar, Marduk, AeroDefense, Sentrycs, Skydio
- [Deployment Architecture]({{< relref "deployment-architecture.md" >}}) — Design pattern for fixed-site C-UAS: sensor placement, integration, power/networking, maintenance
- [Counter-Drone Platforms]({{< relref "counter-drone-platforms/_index.md" >}}) — Interceptor drones and kinetic/non-kinetic response
- [Ukraine Lessons Learned]({{< relref "ukraine-lessons-learned.md" >}}) — Battlefield results 2024–2026: what works, what doesn't, kinetic/electronic/passive countermeasures

---

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Allen Control Systems](https://allencontrolsystems.com) | USA | Series B ($200M, $2.2B, Jun 2026) | Bullfrog autonomous kinetic weapon station; M240/M2/M230/M134; SOCOM + Army contracts |
| [Fortem Technologies](https://fortemtech.com) | USA | Growth (Lockheed $25M, 2026) | Radar + AI + DroneHunter interceptor drone C-UAS system |
| [D-Fend Solutions](https://d-fendsolutions.com) | Israel | Growth | Cyber-takeover counter-drone for critical infrastructure |
| [Aaronia AG](https://aaronia.com) | Germany | Private | RF spectrum monitoring-based drone detection (AARTOS) |
| [Robin Radar Systems](https://robinradar.com) | Netherlands | Private | 3D micro-Doppler radar with bird/drone classification (IRIS) |
| [Marduk Technologies](https://marduk.ee) | Estonia | Early | Passive electro-optical detection — counters RF-dark/fiber-optic threats |
| [AeroDefense](https://aerodefense.tech) | USA | Private | AirWarden Remote ID receiver and RF sensor network |
| [Dronetag](https://dronetag.com) | Czech Republic | Private | Remote ID hardware (BS base station receiver) |
| [Sentrycs](https://sentrycs.com) | Israel | Acquired (Ondas, Nov 2025) | Cyber-over-RF protocol manipulation — detect/ID/mitigate without jamming; 25+ countries |
| [Skydio](https://skydio.com) | USA | Growth (Series F, $4.4B) | Autonomous drone-in-a-box patrol; X10/X10D; AI anomaly detection; Blue UAS listed |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [DRO](https://finance.yahoo.com/quote/DRO) | [DroneShield](https://droneshield.com) | AI-powered C-UAS: RF, radar, acoustic, computer vision |
| [AXON](https://finance.yahoo.com/quote/AXON) | [Axon Enterprise (Dedrone)](https://dedrone.com) | Multi-sensor drone detection platform (acquired Dedrone Oct 2024) |
| [ONDS](https://finance.yahoo.com/quote/ONDS) | [Ondas Holdings](https://ondas.com) | Parent of Sentrycs (CoRF C-UAS) and Iron Drone Raider interceptor |

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [LMT](https://finance.yahoo.com/quote/LMT) | [Lockheed Martin](https://lockheedmartin.com) | $25M investment in Fortem Technologies (Apr 2026); own C-UAS programs |
| [RTX](https://finance.yahoo.com/quote/RTX) | [RTX](https://rtx.com) | Coyote interceptor drone program; C-UAS integration |

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
        "title": "Drone Detection",
        "symbols": [
          {"s": "ASX:DRO", "d": "DroneShield"},
          {"s": "NASDAQ:AXON", "d": "Axon / Dedrone"},
          {"s": "NASDAQ:ONDS", "d": "Ondas / Sentrycs"}
        ],
        "originalTitle": "Drone Detection"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->
