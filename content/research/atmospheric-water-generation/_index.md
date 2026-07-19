---
title: "Atmospheric Water Generation"
date: 2026-07-15
lastmod: 2026-07-18
draft: false
description: "Technologies and companies extracting potable water directly from air humidity, with a focus on metal-organic framework (MOF) sorbent materials and the startups commercializing them."
research_area: "atmospheric-water-generation"
last_reviewed: 2026-07-16
stale_after_days: 180
sitemap:
  changefreq: "monthly"
  priority: 0.8
  disable: false
---

{{<steering>}}

## Atmospheric Water Generation Section — Steering Instructions

**Scope:** Technologies that extract fresh water directly from atmospheric humidity, rather than from surface water, groundwater, or desalination. In scope: sorbent-based atmospheric water harvesting (AWH) — metal-organic frameworks (MOFs), zeolites, hygroscopic salts, and other desiccant materials — plus the cooling/condensation-based atmospheric water generators (AWGs) they compete with, and the companies commercializing either approach. Out of scope: desalination (a separate water-source technology; document under a future `research/water/` desalination section if warranted), municipal water treatment, and general HVAC dehumidification with no drinking-water application.

**Editorial focus:** This is an early-stage, thin field — most activity traces back to a small number of academic labs (notably Omar Yaghi's group at UC Berkeley) and the startups spun out of them. Prioritize the sorbent material entries and the startups commercializing them over incumbent bottled-water or desalination companies, which belong only as market context if a genuinely relevant crossover exists.

**Entry types:** **Material/technology** (e.g., a specific MOF or sorbent class) and **Company** (startups commercializing AWH/AWG hardware). Use the standard entry template for both; material entries can omit the Key People section and instead note the originating lab/researcher in Notable Developments.

**Claim verification for this section:** AWH performance claims are usually reported as liters of water per kilogram of sorbent per day, or liters per day per unit — these two units are not interchangeable and must not be conflated. Distinguish lab/prototype results (often per-kilogram sorbent figures from peer-reviewed papers) from company-reported unit-level production claims (often per-device-per-day figures from press materials), and note which regime (relative humidity, temperature swing, energy input) each claim was measured under. "Off-grid" or "ambient energy" claims should specify the actual energy source (passive solar heating, waste heat) rather than being taken as literally energy-free.

**Tags:** `atmospheric-water-harvesting`, `mof`, `reticular-chemistry`, `desiccant`, `water-scarcity`

**Review cadence:** 90 days — this is a fast-moving field with active commercialization following Omar Yaghi's 2025 Nobel Prize in Chemistry.

{{</steering>}}

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.

## Overview

This section tracks technologies for generating fresh water from atmospheric humidity — primarily sorbent-based atmospheric water harvesting (AWH) using metal-organic frameworks (MOFs) — and the companies commercializing them for arid-region and off-grid deployment. The field traces back to foundational MOF water-uptake research from Omar Yaghi's lab at UC Berkeley, whose 2025 Nobel Prize in Chemistry for MOF development has accelerated commercial interest.

## Key Themes

- Sorbent materials engineered for sharp water uptake at low relative humidity (as low as 20%) and easy release under modest heating
- Passive/ambient-energy water release (solar heating, waste heat) as an alternative to energy-intensive refrigerant condensation
- Commercialization path from academic MOF research to containerized industrial hardware
- Applications in controlled-environment agriculture, off-grid/emergency water supply, and arid-region infrastructure

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Atoco]({{< relref "atoco.md" >}}) | Irvine (Orange County), CA, USA | Private | Commercializes Omar Yaghi's reticular-chemistry MOF research for atmospheric water harvesting and carbon capture; on-grid and off-grid AWH systems targeting late-2026 commercial rollout. |
| [WaHa](https://www.wahainc.com/) | Fremont, CA, USA | Private (Series A-1, $8M, Jul 2025) | Founded 2018 by Omar Yaghi; heat-pump-driven regeneration engine compatible with silica gel, SAPO-34, and MOF desiccants; recapitalized under new leadership, first commercial unit unveiled Sep 2025. |
| [Uravu Labs](https://www.uravulabs.com/) | Bengaluru, India | Private (Seed, $2.3M+) | Liquid-desiccant AWH; pivoting from hospitality drinking-water units to "Clausius," a water-positive cooling platform for AI data centers using server waste heat. |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [AIRJ](https://finance.yahoo.com/quote/AIRJ) | [AirJoule Technologies]({{< relref "airjoule-technologies.md" >}}) | Sorbent/MOF-based AWH and dehumidification; PNNL-licensed technology; 50/50 joint ventures with GE Vernova (Americas/Africa/Australia) and CATL 🇨🇳 (Asia); Carrier and BASF partnerships. |

### Incumbents

No large diversified incumbents are yet directly active in sorbent-based atmospheric water harvesting; condensation-based atmospheric water generator (AWG) companies such as Watergen, SOURCE Global, and Genesis Systems use older refrigerant-condensation technology and are tracked as market context rather than detailed entries, consistent with this section's focus on sorbent/desiccant-based approaches.

## Entries

- [MOF-801]({{< relref "mof-801.md" >}}) — zirconium-fumarate metal-organic framework material behind the leading AWH approach; sharp water uptake at low humidity, low-temperature regeneration
- [Atoco]({{< relref "atoco.md" >}}) — Omar Yaghi-founded company commercializing MOF-based atmospheric water harvesting and carbon capture
- [AirJoule Technologies]({{< relref "airjoule-technologies.md" >}}) — NASDAQ-listed (AIRJ) PNNL-licensed sorbent AWH platform; GE Vernova and CATL 🇨🇳 joint ventures
- [WaHa]({{< relref "waha.md" >}}) — Fremont, CA; also Omar Yaghi-founded (2018); heat-pump desiccant regeneration engine, now under new leadership
- [Uravu Labs]({{< relref "uravu-labs.md" >}}) — Bengaluru liquid-desiccant AWH, pivoting toward data center water-positive cooling; cross-linked to [Mojave Energy Systems]({{< relref "../datacenters/cooling/mojave-energy-systems.md" >}}) and [Blue Frontier]({{< relref "../datacenters/cooling/blue-frontier.md" >}}) in `datacenters/cooling`, which apply the same waste-heat-driven liquid-desiccant mechanism to building dehumidification/AC rather than water production
