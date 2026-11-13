---
title: "HALE / HAPS — High-Altitude Platform Systems"
date: 2026-08-03
lastmod: 2026-11-12
draft: false
description: "High-altitude, long-endurance (HALE) uncrewed platforms — solar-electric and fuel-cell fixed-wing aircraft, autonomous stratospheric airships, and stratospheric balloons — flown as persistent telecom, Earth-observation, and ISR platforms above 60,000 ft."
research_area: "hale-haps"
last_reviewed: 2026-11-12
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9
  disable: false
---

{{<steering>}}

## HALE / HAPS — Steering Instructions

**Scope boundaries:** IN — fixed-wing, airship, and balloon platforms flown in the stratosphere (roughly 55,000–95,000 ft) for telecom relay, Earth observation, or general-purpose/defense ISR; the companies building and operating them. OUT — conventional satellites (any orbital regime); low-altitude drones and UAS below the stratosphere (see `robotics/aerial-drones`); weather balloons and sounding balloons with no persistent-platform or payload-relay mission. BORDERLINE — companies whose primary mission is counter-UAS/missile detection using a stratospheric platform: documented in `drone-detection/high-altitude-platforms` instead, with cross-links back into this section.

**Editorial framing:** As with other sections, prioritize the platform developers and startups over their large incumbent parents/investors (Airbus, BAE Systems, Thales, Leonardo). Those incumbents belong in the Incumbents table as context, not as the center of gravity. When a subsidiary is majority- or wholly-owned by a public incumbent (AALTO/Airbus, Prismatic/BAE, Mira Aerospace/Space42), document the subsidiary's own program in the Startups & Development Partners table and note the parent relationship inline.

**Claim verification flags specific to this topic area:** Endurance and altitude claims should always specify whether they were flight-demonstrated or are a stated design target — the two are routinely blended in company marketing (Stratobus's "up to one year" endurance and several companies' "months" endurance claims are design targets, not flown results, as of mid-2026). Commercial-service timelines in this space have a strong track record of slipping (Zephyr, Stratobus, SPL/World Mobile Stratospheric, and Sceye have each pushed dates back at least once) — treat future launch/commercialization dates with the same skepticism applied to nuclear SMR timelines elsewhere on this site.

**Review cadence:** 90 days — this is a fast-moving, pre-commercial space as of mid-2026 with frequent flight-test milestones, funding events, and ownership changes.

{{</steering>}}

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.

## Overview

High-Altitude Long-Endurance (HALE) platforms — commercially and in defense circles usually called High Altitude Platform Systems (HAPS) — fly in the stratosphere, typically 60,000-70,000 ft, well above commercial air traffic and most weather, where they hold station or loiter for days, weeks, or (as a design target) months at a time. The pitch across the whole category is the same: a persistent vantage point cheaper and more flexible to reposition or upgrade than a satellite, with far better sensor resolution, and far longer endurance and altitude reach than a battery-powered drone. Applications split across three overlapping missions — direct-to-handset or backhaul telecom relay, Earth observation and environmental/disaster monitoring, and defense ISR/signals intelligence — and the same company frequently pursues more than one.

This section covers the three physical platform types in use or development, organized as subsections:

- [Fixed-Wing HAPS]({{< relref "fixed-wing/_index.md" >}}) — solar-electric or hydrogen fuel-cell aircraft that fly forward continuously to generate lift (Zephyr/AALTO, PHASA-35/Prismatic, Mira Aerospace, Kea Aerospace, Swift Engineering, NewSpace Research & Technologies, World Mobile Stratospheric)
- [Stratospheric Airships]({{< relref "airships/_index.md" >}}) — lighter-than-air, helium-filled dirigibles using buoyancy for lift and propulsion only for station-keeping (Thales Alenia Space's Stratobus; Sceye, documented in Drone Detection)
- [Stratospheric Balloons]({{< relref "balloons/_index.md" >}}) — free-flying or maneuverable balloons trading persistence for lower cost and faster deployment (Near Space Labs; World View, Aerostar, Urban Sky, TCOM, Hemeria, and Kalam Labs, documented in Drone Detection)

**Scope note and cross-reference to Drone Detection:** Several balloon and airship companies (Sceye, World View/Ondas, Aerostar, Urban Sky, TCOM, Hemeria/Safran BalMan, Kalam Labs) are documented as full entries under [Drone Detection → High-Altitude Platforms]({{< relref "../drone-detection/high-altitude-platforms/_index.md" >}}) rather than here, because their primary or fastest-growing mission is counter-UAS/cruise-missile detection and ELINT. This section instead holds the platform types and companies whose mission is centered on telecom, Earth observation, or general-purpose ISR — plus cross-links out to the Drone Detection entries where the same underlying platform architecture applies to both missions. Fixed-wing HAPS companies have no equivalent overlap with Drone Detection as of this review; none of the fixed-wing entries here currently market a C-UAS payload.

## Key Themes

- **Endurance and altitude records are the industry's proof points, and they move fast.** AALTO's Zephyr held a 67-day continuous-flight record as of April 2025; Sceye (airship) followed a 12-day flight in March-April 2026 with a 30-day, nearly 30,000 km round trip between New Mexico and Japan in August-September 2026; most fixed-wing competitors are still validating 24-72 hour flights (Mira Aerospace's longest reported flight is 29 hours, September 2026) as stepping stones toward multi-month design targets. Treat every "X-day endurance" or "highest HAPS flight" claim as a snapshot, not a durable ranking.
- **Commercial telecom timelines have consistently slipped.** Zephyr/AALTO, Stratobus, and Stratospheric Platforms/World Mobile Stratospheric have each pushed back "commercial service" or "first flight" targets multiple times since their programs began (Stratobus since 2016; SPL since 2014). Sceye's own September 2024 release projected 2025 commercial launch; in September 2026 it completed a first "Service Test" flight with SoftBank over Japan rather than a commercial launch. AALTO's long-stated 2026 entry into service in Japan had not been confirmed as met by November 2026, with UK certification now expected in late 2027 or early 2028, and World Mobile Stratospheric's Islander antenna test flights, due in mid-2026, had not been publicly reported.
- **Ownership churn among independent HAPS startups is common.** Several companies in this space have been acquired by, or spun out as JVs with, larger telecom or tower operators within the past 18 months: Mira Aerospace (UAVOS-Bayanat JV → Space42 subsidiary after the 2024 Bayanat-Yahsat merger), Stratospheric Platforms Ltd (→ World Mobile Stratospheric, acquired by World Mobile + Protelindo, Aug 2025), World View (→ Ondas Holdings, 2026). The planned Airbus–Leonardo–Thales space merger announced in October 2025 would also move Thales Alenia Space, home of Stratobus, into a new jointly owned company.
- **Solar-electric and hydrogen fuel-cell propulsion serve the same mission with different trade-offs.** Solar-electric designs (Zephyr, PHASA-35, ApusNeo18, Kea Atmos, SULE, NewSpace R&T's platform) depend on III-V multijunction solar cells and lithium battery storage for night flight; the one fuel-cell design in this section (World Mobile Stratospheric) trades solar dependency for hydrogen logistics and a heavier airframe capable of carrying a large phased-array antenna.

- **Government demonstration contracts are the most concrete near-term funding.** Prismatic holds a US Air Force Research Laboratory services contract with a \$10 million ceiling (awarded 2025) and a £15.7 million UK ARIA-backed power-beaming demonstration contract (September 2026); Swift Engineering's SULE is funded through NASA SBIR awards; NewSpace Research & Technologies works under an Indian iDEX contract. None of these is recurring commercial telecom revenue.

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [AALTO HAPS]({{< relref "fixed-wing/aalto-haps.md" >}}) | UK (Farnborough) | Pre-commercial (Airbus subsidiary) | Zephyr solar-electric fixed-wing HAPS; telecom relay and Earth observation |
| [Prismatic Ltd]({{< relref "fixed-wing/prismatic.md" >}}) | UK (Alton) | Pre-operational (BAE Systems subsidiary) | PHASA-35 solar-electric fixed-wing HAPS; ISR and comms |
| [Mira Aerospace]({{< relref "fixed-wing/mira-aerospace.md" >}}) | UAE (Abu Dhabi) | Active flight-test (Space42 subsidiary) | ApusNeo18 solar-electric fixed-wing HAPS; telecom, EO, RF sensing |
| [Kea Aerospace]({{< relref "fixed-wing/kea-aerospace.md" >}}) | New Zealand (Christchurch) | Private, pre-revenue; Mk2 manufacturing site opened Aug 2026 | Kea Atmos solar stratospheric imaging aircraft |
| [Swift Engineering]({{< relref "fixed-wing/swift-engineering.md" >}}) | USA (San Clemente, CA) | Private (Matsushita International Corp-owned) | SULE solar-electric fixed-wing HAPS; EO, comms relay, defense ISR |
| [NewSpace Research & Technologies]({{< relref "fixed-wing/newspace-research-technologies.md" >}}) | India (Bengaluru) | Private, iDEX government-backed | Solar-powered fixed-wing HAPS for Indian Navy stratospheric ISR |
| [World Mobile Stratospheric]({{< relref "fixed-wing/stratospheric-platforms.md" >}}) | UK (London; successor to SPL) | Pre-flight-test (JV of World Mobile + Protelindo) | Hydrogen fuel-cell fixed-wing HAPS; direct-to-handset 5G |
| [Thales Alenia Space — Stratobus]({{< relref "airships/thales-alenia-space-stratobus.md" >}}) | France (Cannes) | Long-running R&D (Thales/Leonardo JV) | 140m autonomous helium airship; year-long station-keeping design target |
| [Near Space Labs]({{< relref "balloons/near-space-labs.md" >}}) | USA (Brooklyn, NY) | Series B (\$20M, Apr 2025) | Swift stratospheric balloon imaging (7cm resolution); P&C insurance, EO |
| [Sceye](https://sceye.com) | USA (Moriarty, NM) | Growth (Series C) | Solar-powered stratospheric airship — [full entry]({{< relref "../drone-detection/high-altitude-platforms/sceye.md" >}}) |
| [World View](https://worldview.space) | USA (Tucson, AZ) | Acquired by Ondas (2026) | Stratollite stratospheric balloon — [full entry]({{< relref "../drone-detection/high-altitude-platforms/world-view-stratollite.md" >}}) |
| [Aerostar](https://aerostar.com) | USA (Sioux Falls, SD) | Growth (division of Raven Industries/CNH) | Thunderhead stratospheric balloons/airships — [full entry]({{< relref "../drone-detection/high-altitude-platforms/aerostar.md" >}}) |

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [AVAV](https://finance.yahoo.com/quote/AVAV/) | [AeroVironment](https://www.avinc.com) | Operates Sunglider HAPS via SoftBank HAPSMobile JV — [full entry]({{< relref "../robotics/aerial-drones/aeroviroment.md" >}}) |
| [AIR](https://finance.yahoo.com/quote/AIR) | [Airbus](https://www.airbus.com/en) | Majority owner of AALTO HAPS (Zephyr program) |
| [BA.L](https://finance.yahoo.com/quote/BA.L) | [BAE Systems](https://www.baesystems.com) | Owner of Prismatic Ltd (PHASA-35 program) |
| [HO.PA](https://finance.yahoo.com/quote/HO.PA) | [Thales](https://www.thalesgroup.com) | 67% owner of the Thales Alenia Space JV behind Stratobus |
| [LDO.MI](https://finance.yahoo.com/quote/LDO.MI) | [Leonardo](https://www.leonardo.com) | 33% owner of the Thales Alenia Space JV behind Stratobus |
| [ONDS](https://finance.yahoo.com/quote/ONDS) | [Ondas Holdings](https://ondas.com) | Acquired World View (2026) for its Stratollite platform |

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
        "title": "HALE/HAPS Parents & M&A",
        "symbols": [
          {"s": "NASDAQ:AVAV", "d": "AeroVironment"},
          {"s": "EPA:AIR", "d": "Airbus"},
          {"s": "LSE:BA.", "d": "BAE Systems"},
          {"s": "EPA:HO", "d": "Thales"},
          {"s": "BIT:LDO", "d": "Leonardo"},
          {"s": "NASDAQ:ONDS", "d": "Ondas / World View"}
        ],
        "originalTitle": "HALE/HAPS Parents & M&A"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

## Supply Chain

HAPS platforms share a component stack regardless of which of the three physical platform types (fixed-wing, airship, balloon) they use:

| Layer | Key Inputs | Known Companies | Geographic Concentration |
|-------|-----------|------------------|---------------------------|
| Solar cells | III-V multijunction (GaAs-based) cells for lightweight, high-efficiency panels on fixed-wing airframes and some airships | [Azur Space]({{< relref "../energy/solar/azur-space" >}}), [SolAero Technologies]({{< relref "../energy/solar/solaero-technologies" >}}), [Spectrolab]({{< relref "../energy/solar/spectrolab" >}}) | Space-grade III-V cell manufacturing is concentrated in a small number of German and US suppliers, largely serving both the satellite and HAPS markets |
| Energy storage | Lithium-sulfur or high-density lithium-ion battery packs for overnight power on solar platforms | Sceye has publicly cited lithium-sulfur cells (~400-425 Wh/kg reported); most fixed-wing HAPS makers do not disclose their cell supplier | Lithium-sulfur remains a niche, low-supplier-count chemistry relative to conventional Li-ion |
| Lift gas | Helium for airships and balloons | Global helium supply is concentrated in a handful of sources (US, Qatar, Algeria, Russia); no HAPS-specific supplier documented in this review | Helium is a genuine geopolitical and supply-continuity risk for every airship/balloon entry in this section, though none of the companies researched here discuss their sourcing publicly |
| Propulsion (alternative) | Hydrogen fuel cells | World Mobile Stratospheric is the only entry in this section using hydrogen rather than solar-electric propulsion; no specific fuel-cell supplier disclosed in sources found | — |
| Airframe structure | Ultra-lightweight carbon-fiber composites; specialized envelope/hull fabrics for airships (Sceye claims a proprietary hull fabric, unverified against independent sources) | No dedicated airframe-material suppliers documented yet in this section | — |
| Avionics | Flight-control and mission avionics for ultra-light airframes | AERTEC (Seville, Spain) is contracted to supply the main avionics for AALTO's Zephyr (October 2026); other makers do not disclose suppliers | — |
| Payloads | EO/IR cameras, hyperspectral sensors, phased-array telecom antennas, SIGINT/ELINT receivers | Payloads are typically developed in-house or via named partners (e.g., Spectral Sciences for Sceye's NASA-funded hyperspectral sensor) rather than sourced from a common supplier base | — |
| Platform integration | The company itself | See Companies tables above | — |
| End customers | Telecom carriers, defense/ISR agencies, insurers, environmental agencies | NTT DOCOMO/Space Compass and SoftBank (telecom, AALTO/AeroVironment), Telkomsel (telecom, AALTO), Deutsche Telekom and BT (telecom, World Mobile Stratospheric), Indian Navy (defense, NewSpace R&T), US Air Force Research Laboratory (defense, Prismatic), Telespazio Ibérica (wildfire monitoring, Mira Aerospace), US EPA/NASA/USGS (environmental, Sceye), P&C insurers (Near Space Labs) | — |

**⚑ Shared supplier note:** Any HAPS company using III-V multijunction solar cells draws from the same small supplier base already documented in [Energy → Solar]({{< relref "../energy/solar/_index.md" >}}) for satellite and other space-grade applications — a structural link between the HAPS and satellite solar-cell markets worth checking whenever a new fixed-wing HAPS entry is added here.
