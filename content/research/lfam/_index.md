---
title: Large Format Additive Manufacturing (LFAM)
date: 2026-06-29
lastmod: 2026-06-29
draft: false
description: Industrial 3D printing systems capable of producing parts meters in scale — composite tooling, structural hulls, aerospace molds, and defense components. Covers gantry and robotic pellet extrusion, wire arc additive manufacturing (WAAM), key system vendors, materials supply chain, and defense/aerospace applications.
research_area: "lfam"
last_reviewed: 2026-06-29
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9
  disable: false
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


## Overview

Large Format Additive Manufacturing (LFAM) refers to industrial 3D printing systems capable of depositing material at high volumetric rates to produce parts measuring meters — or tens of meters — in a single build. The defining constraint that separates LFAM from conventional additive manufacturing is scale: parts too large for standard build volumes, typically requiring either a gantry system spanning meters or a 6-axis robotic arm mounted on a linear track.

The primary process is pellet extrusion (also called large-scale material extrusion, or ME-LFAM), where thermoplastic composite pellets are melted and deposited at deposition rates of 50–500+ kg/hour — orders of magnitude faster than filament-based desktop printing. A second major process is Wire Arc Additive Manufacturing (WAAM), which uses electric arc welding to deposit metal wire layer by layer, producing large near-net-shape metal components.

LFAM is moving from tooling and prototype applications toward direct end-use structural parts, driven by three converging pressures: defense supply chain shortfalls (particularly US Navy submarine component backlogs), aerospace composite tooling cost reduction, and the emergence of defense programs like Anduril's Ghost Shark that explicitly used LFAM to achieve a multi-year production ramp in months.

## Key Themes

- **Tooling vs. end-use parts:** LFAM is mature for composite molds and cure tooling; direct end-use structural parts (pressure hulls, structural spars) are the emerging frontier
- **Pellet extrusion vs. WAAM:** Thermoplastic composites dominate aerospace/marine tooling; WAAM dominates metal structural replacement parts for naval and defense
- **Defense pull:** US Navy submarine component shortfalls (17-month traditional lead times → weeks via WAAM) are the strongest near-term demand signal; AUKUS partnership explicitly routing AM components through AML3D
- **Anduril Ghost Shark as proof case:** First major defense program to cite LFAM as the production-enabling technology — composite pressure hulls on a weekly cadence, cost competitive with traditional fabrication
- **Robotic vs. gantry:** Robotic arm systems (Caracol, CEAD) offer unconstrained part geometry and footprint; gantry systems (Thermwood, Ingersoll) offer larger Z-height and higher repeatability for flat tooling
- **Materials concentration:** PEEK resin supply is >90% controlled by three Western companies (Victrex, Syensqo, Evonik); carbon fiber supply is heavily Chinese; both are strategic vulnerabilities for defense LFAM
- **Deployable manufacturing:** Ingersoll MasterPrint Deployable and containerized LFAM concepts enabling forward-deployed manufacturing for military logistics

## Process Technologies

| Process | Full Name | Material | Deposition Rate | Primary Use |
|---------|-----------|----------|-----------------|-------------|
| **ME-LFAM** | Material Extrusion LFAM (pellet) | Thermoplastic composites (CF-ABS, CF-PA, CF-PEEK, CF-PEI) | 50–500+ kg/hr | Tooling, molds, structural composite parts |
| **WAAM** | Wire Arc Additive Manufacturing | Steel, aluminum, Ti, Cu-Ni, Inconel | 2–10 kg/hr (metal) | Near-net-shape metal parts, naval/aerospace structural components |
| **MAAM** | Metal Arc Additive Manufacturing | Steel, stainless, Cu alloys | 2–8 kg/hr | Naval structural replacement parts |
| **Continuous fiber LFAM** | Continuous fiber reinforcement | CF/GF tapes in thermoplastic matrix | Low | High-strength structural parts with directional fiber control |

## System Vendors

### Gantry Systems (Thermoplastic Composite)

| Company | System | Build Volume | Deposition Rate | Key Customers |
|---------|--------|-------------|-----------------|---------------|
| [Thermwood](https://www.thermwood.com) | LSAM / LSAM AP510 | Up to 40 ft+ table | ~100–150 kg/hr | Boeing, Bell, Air Force Research Lab, General Atomics |
| [Ingersoll Machine Tools](https://en.machinetools.camozzi.com) | MasterPrint 3X | 450 m³ build volume | High | UMaine, Bell, TPI Composites, wind turbine mold work |
| [Cincinnati Incorporated](https://www.e-ci.com) | BAAM | ~1.8 × 3.8 × 0.9 m | ~36 kg/hr | ORNL collaboration; multi-material research |

### Robotic Systems (Thermoplastic Composite)

| Company | HQ | Key System | Notes |
|---------|-----|-----------|-------|
| [Caracol AM](https://www.caracol-am.com) | Milan, Italy | Heron AM (robotic 6-axis) | $40M Series B; ESA AIMIS grant; aerospace, marine, space applications; US presence via RAPID+TCT 2025 |
| [CEAD B.V.](https://ceadgroup.com) | Delft, Netherlands | Flexbot / AM Flexbot | Maritime Application Center for boatbuilding; microfactory model with multiple robotic cells; continuous-fiber capable |
| [Rapid Fusion](https://rapidfusion.co.uk) | Exeter, UK | Extrusion robotic system | Partnered with PADT for US market entry; defense and industrial focus |

### Wire Arc Additive Manufacturing (WAAM / Metal)

| Company | HQ | System | Key Programs |
|---------|-----|--------|-------------|
| [AML3D](https://aml3d.com) | Adelaide, Australia / Ohio, USA | Arcemy WAAM | Virginia-class submarine Cu-Ni tailpiece (5 weeks vs. 17 months); US Navy LOI projecting 400 components in 2026, 1,600 by 2030; AUKUS supply chain integration |
| [Rosotics](https://rosotics.com) | Chandler, AZ, USA | Mantis (induction-heated WAAM) | Naval steel AM program; fabrication and testing phase 2025 |

## Key Defense & Aerospace Applications

### Composite Pressure Hulls (AUV)
Anduril's Ghost Shark XL-AUV uses LFAM-produced composite pressure hulls. The LFAM process — developed by Dive Technologies before Anduril's acquisition — enabled production of a new AUV class in under three years, and ramp to weekly hull production at Anduril's $60M Sydney facility. This is the most prominent proof case that LFAM can be a production-enabling technology, not just a prototyping tool, for defense hardware. See [Anduril Undersea]({{< relref "../robotics/undersea-drones/anduril-undersea.md" >}}).

### Aerospace Composite Tooling
The primary commercial application. Autoclave cure tools for composite aerospace parts (fuselage skins, wing skins, blade molds) traditionally machined from Invar steel — expensive, long lead time, heavy. LFAM-printed composite tools (CF-ABS, CF-PEEK) cut tooling cost by 50–80% and lead time from months to days. Boeing 777X and AFRL programs validated autoclave-capable LFAM tooling.

### Naval Metal Components (WAAM)
US Navy submarine programs have acute supply chain shortfalls for copper-nickel alloy propulsion components. Traditional casting/machining: 12–17 month lead times. AML3D WAAM: 3–5 weeks. The AUKUS partnership is explicitly routing AM component qualification through AML3D as a near-term supply chain fix.

### Wind Turbine Blade Tooling
Full-chord wind blade molds (60–100m blades require tooling exceeding 6m width) are a natural LFAM application. Ingersoll MasterPrint's 6.7m width exceeds chord dimensions of modern blades. UMaine/ORNL/TPI Composites partnership targeting 50% tooling cost reduction and 100% recyclable tooling materials.

### Deployable Forward Manufacturing
Ingersoll's MasterPrint Deployable — a containerized combined additive/subtractive system — targets military forward manufacturing: printing replacement parts in theater rather than waiting for supply chain delivery.

## Materials Supply Chain

### Thermoplastic Composites

| Material | Primary Use in LFAM | Key Suppliers | Supply Risk |
|---------|---------------------|---------------|------------|
| CF-ABS | Tooling patterns, non-structural | Multiple | Low |
| CF-Nylon (PA6/PA12) | Structural tools, jigs | Techmer PM, SABIC, Airtech | Low–medium |
| CF-PEI (ULTEM) | Autoclave tooling (>180°C) | SABIC | Medium (SABIC concentration) |
| CF-PEEK | High-performance structural, pressure-rated parts | Victrex, Syensqo, Evonik | **High** — 3 suppliers control >90% of global PEEK resin |
| CF-PEKK | Aerospace structural | Arkema | Medium |

**Critical supply risk — PEEK:** Victrex (UK) holds ~60% of global PEEK resin capacity. Syensqo (Belgium, formerly Solvay) and Evonik (Germany) hold most of the remainder. No significant US or Asian alternative at scale. For defense LFAM applications requiring high-temperature, pressure-rated composite structures, this is a single-supplier-class vulnerability.

### Metal Feedstock (WAAM)

| Material | Use | Supply Notes |
|---------|-----|-------------|
| Copper-Nickel (Cu-Ni 70/30) | Naval propulsion components, piping | Specialty alloy; US domestic supply adequate |
| Titanium wire | Aerospace structural | US supply exists; Russian feedstock historically significant |
| Steel (ER70S, 316L SS) | Structural naval components | Domestic supply |
| Inconel 625/718 | High-temp aerospace | Specialty; Haynes/Special Metals domestic |

## Sources

- [VoxelMatters — How LFAM enabled Anduril's Ghost Shark Program of Record](https://www.voxelmatters.com/how-lfam-enabled-andurils-ghost-shark-program-of-record/)
- [Additive Manufacturing Media — WAAM specialist AML3D opens US facility](https://www.additivemanufacturing.media/articles/waam-specialist-aml3d-opens-us-facility-to-support-industrial-partnerships)
- [3D Printing Industry — Airtech and Evergreen Additive defense/maritime LFAM partnership](https://3dprintingindustry.com/news/airtech-and-evergreen-additive-partner-to-advance-defense-and-maritime-lfam-251899/)
- [CompositesWorld — CEAD Maritime Application Center](https://www.compositesworld.com/news/cead-launches-the-maritime-application-center-dedicated-to-industrial-3d-printing-boat-hulls)
- [CompositesWorld — TPI/UMaine/ORNL wind turbine tooling](https://www.compositesworld.com/news/tpi-umaine-ornl-to-leverage-worlds-largest-polymer-3d-printer-for-wind-turbine-tooling)
- [Advanced Manufacturing — AML3D delivers Virginia-class submarine components](https://www.advancedmanufacturing.org/news-desk/aml3d-delivers-3d-printed-parts-for-nuclear-submarines/article_b1a4a592-ceac-11ef-81f3-a7733aac375c.html)
- [Thermwood — LSAM product page](https://www.thermwood.com/lsam_home.htm)
- [Caracol AM — technologies](https://www.caracol-am.com/technologies)
- [Rapid Fusion — LFAM guide 2026](https://rapidfusion.co.uk/blogs/news/large-format-additive-manufacturing-guide)
