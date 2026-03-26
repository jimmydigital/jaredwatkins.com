---
title: "One Stop Systems"
date: 2026-03-25
lastmod: 2026-03-26
draft: false
description: "Escondido, CA rugged AI compute company (NASDAQ: OSTO); 'AI on the Fly' (AIFLY) rackmount GPU servers for airborne and maritime military platforms; P-8A Poseidon maritime patrol aircraft, Virginia-class submarine sonar, USSOCOM CRADA; Q4 2025 revenue $12M (+70% YoY); 2026 guidance of 20–25% growth."
tags: ["rugged", "edge-compute", "mil-spec", "ai-inference", "defense", "us", "public", "rack-server"]
categories: ["company"]
research_area: "datacenters/rugged-edge-compute"
source_urls:
  - "https://onestopsystems.com/"
  - "https://finance.yahoo.com/quote/OSTO"
last_reviewed: 2026-03-26
stale_after_days: 90
---

## Summary

One Stop Systems (NASDAQ: OSTO) builds rugged GPU compute servers — branded "AI on the Fly" (AIFLY) — that run at altitude, in submarine electronics bays, and inside ground vehicles where commercial servers would fail. The company occupies the rack/server tier of rugged compute, integrating high-density NVIDIA GPU clusters into conduction-cooled or air-cooled enclosures qualified to MIL-STD-810 standards. Revenue is accelerating sharply on defense AI demand: Q4 2025 saw 70% year-over-year growth, and the company is targeting 20–25% growth in 2026. Its USSOCOM cooperative R&D agreement and deployments on major Navy platforms (P-8A Poseidon, Virginia-class submarines) validate its positioning at the frontier of military AI inference.

## Key Facts

- **Founded:** 1998 (originally high-density compute; pivoted to rugged defense AI focus under current leadership)
- **HQ:** Escondido, CA (San Diego area)
- **Ticker:** NASDAQ: OSTO
- **Value chain position:** Component/subsystem supplier — complete rugged AI compute servers and storage systems to defense primes and system integrators
- **CEO:** Mike Knowles (since June 2023)
- **Revenue:** Q4 2025: $12.0M (+70.2% YoY); FY2025 full year approximately $57–60M; 2026 guidance: 20–25% growth, ~40% gross margin, positive EBITDA
- **Balance sheet (end 2025):** $31.2M cash, $45.3M working capital — no debt pressure
- **Flagship product:** "AI on the Fly" (AIFLY) — rackmount GPU servers designed for extreme environments (altitude, vibration, humidity, temperature)
- **Performance spec:** Up to 9.9 PetaOPS INT8 at maximum GPU density configuration
- **Platform tier:** Rack/server tier — complete integrated systems, not individual VPX modules
- **Standards compliance:** MIL-STD-810 (environmental); conduction-cooled variants for sealed enclosures; air-cooled variants for accessible bays
- **Key programs:**
  - P-8A Poseidon: ~$4M contract for data recording and compute on Boeing maritime patrol aircraft (US Navy, Royal Australian Air Force, UK RAF)
  - Virginia-class submarine: ~$2M sonar upgrade contract — GPU-accelerated underwater acoustic processing in one of the world's most demanding environments
  - US Army combat vehicles: $1.2M order
  - USSOCOM: CRADA (Cooperative Research and Development Agreement) — joint R&D for special operations compute requirements
- **Divestiture (Dec 2025):** Sold Bressner Technology (European commercial division) for $22.4M, booking $8.2M gain; sharpens focus on US defense market

## What It Is / How It Works

One Stop Systems builds GPU compute servers for the spaces where commercial servers cannot operate. A commercial NVIDIA H100 server is designed for a climate-controlled datacenter: air-cooled fans, standard rack mounting, no vibration hardening. An AIFLY server from OSS takes equivalent GPU compute density and re-engineers the thermal management, structural mounting, power distribution, and connector systems for operation in an aircraft avionics bay at 40,000 feet, a submarine electronics room subject to shock and vibration, or an armored vehicle computer bay at desert temperatures.

The **P-8A Poseidon deployment** is the clearest illustration of the value proposition. The P-8A is a Boeing 737-derived maritime patrol aircraft that uses sonobuoys to detect and track submarines. OSS's system sits in the aircraft's electronics bay, processing acoustic sensor data in flight using GPU-accelerated AI algorithms that classify acoustic signatures in real time. Prior generations used specialized DSP hardware; OSS replaces those with general-purpose GPU inference that can be updated with new algorithms via software without hardware changes — a critical operational flexibility advantage.

The **Virginia-class submarine contract** is a particularly strong validation signal. Submarine electronics bays have extreme volume constraints and among the strictest EMI requirements of any military platform (submarine systems must not radiate signals detectable by adversaries). An OSS win in this environment confirms ruggedization capability at the high end of the MIL-spec spectrum.

**USSOCOM CRADA:** A Cooperative Research and Development Agreement is not a production contract — it is a collaborative R&D mechanism where DoD and a commercial company jointly develop technology. The company retains some intellectual property rights. SOCOM CRADAs are a strong pipeline signal: SOCOM brings operational requirements; OSS brings commercial AI compute engineering; the result typically leads to a production contract if the collaboration succeeds.

**SWaP constraint:** OSS systems must deliver GPU compute performance within the fixed size, weight, and power budget of a military platform bay. At 9.9 PetaOPS INT8 in a rackmount form factor, OSS is approaching the practical limit of what current GPU generations can deliver in a ruggedized enclosure — future growth in this metric will depend on NVIDIA's next-generation GPU architectures (Blackwell successors) reducing power-per-FLOP.

## Notable Developments

- **2026-03:** Full year 2025 results announced — FY2025 revenue trajectory confirmed; 2026 guidance of 20–25% growth and ~40% gross margin
- **2025-Q4:** $12.0M revenue, +70.2% YoY — record quarterly growth driven by custom server production for defense, defense prime data storage, and medical/maritime AI applications
- **2025-12:** Bressner Technology (European commercial division) divested for $22.4M; $8.2M gain — strategic refocus on US defense
- **2025:** $4M P-8A Poseidon data recording and compute contract
- **2025:** $2M Virginia-class submarine sonar upgrade contract
- **2025:** $1.2M US Army combat vehicle order
- **Active:** USSOCOM CRADA — joint R&D for special operations tactical compute requirements

## Key People

**Mike Knowles** — President & CEO (June 2023–present)
- LinkedIn: [linkedin.com/in/michael-knowles-cubic](https://www.linkedin.com/in/michael-knowles-cubic/)
- Education: BS Aerospace Engineering (US Naval Academy); MS Aerospace Engineering (Naval Postgraduate School); MBA (George Mason University)
- Prior employment (reverse-chronological):
  - One Stop Systems: President & CEO (June 2023–present)
  - Cubic Corporation: President and General Manager, Mission and Performance Solutions (~$700M business unit, ~2,000 employees)
  - Curtiss-Wright Defense Solutions: Senior leadership roles
  - Rockwell Collins: Senior leadership roles
  - Lockheed Martin: Senior leadership roles
  - US Navy: Retired officer; Naval Test Pilot School graduate; operational flying roles
- **⚑ Overlap:** Mike Knowles previously held senior leadership roles at Curtiss-Wright Defense Solutions, another company documented in this section.

### People — Last Reviewed: 2026-03-26

## Claim Verification

### Claim: 9.9 PetaOPS inference performance

**Status:** Partially verified

**Supporting sources:**
- [One Stop Systems AIFLY product documentation](https://onestopsystems.com/) — company cites 9.9 PetaOPS for maximum-density GPU configuration; NVIDIA H200 SXM specification is approximately 3.958 PetaOPS INT8 per card, meaning 2–3 H200 SXM GPUs in a ruggedized chassis could approach this figure at INT8 precision

**Refuting / questioning sources:**
- No independent third-party benchmark of AIFLY systems in ruggedized deployment has been identified; figure is from OSS marketing materials
- PetaOPS figures for ruggedized systems may not account for thermal throttling under sustained inference load — military systems often operate at elevated ambient temperatures that reduce GPU boost frequency; sustained (not burst) throughput may be materially lower

**Summary:** The 9.9 PetaOPS figure is plausible based on GPU specifications but represents peak theoretical throughput at maximum GPU density — sustained performance in a deployed military environment may be lower due to thermal constraints; no independent lab validation found.

### Claim: P-8A Poseidon and Virginia-class deployments

**Status:** Verified

**Supporting sources:**
- [One Stop Systems press releases](https://onestopsystems.com/) — company has formally announced both the P-8A Poseidon contract (~$4M) and the Virginia-class submarine sonar upgrade contract (~$2M) via press releases and SEC disclosures

**Summary:** Both platform deployments are confirmed via company press releases and are consistent with the platforms' known upgrade cycles.

## Sources

- [One Stop Systems — Official Website](https://onestopsystems.com/)
- [One Stop Systems — NASDAQ: OSTO](https://finance.yahoo.com/quote/OSTO)
- [NVIDIA H200 SXM Datasheet](https://www.nvidia.com/en-us/data-center/h200/) — basis for PetaOPS cross-check
- [US Navy P-8A Poseidon Program](https://www.navair.navy.mil/product/P-8A-Poseidon) — platform context
