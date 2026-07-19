---
title: "Tesla Energy — Virtual Power Plants"
date: 2026-07-18
lastmod: 2026-07-18
draft: false
description: "Tesla's residential Powerwall fleet, orchestrated by its Autobidder software into virtual power plants across California, Texas, New England, Puerto Rico, and the UK; joined a 16.8 GW joint VPP program with Sunrun and Renew Home in June 2026 aimed at AI datacenter demand. Distinct from Tesla's separate Megapack utility-scale storage business."
research_area: "energy/virtual-power-plants"
source_urls:
  - "https://www.canarymedia.com/articles/virtual-power-plants/tesla-sunrun-renewhome-vpp"
  - "https://www.tesla.com/support/energy/virtual-power-plant/dsgs"
  - "https://chargedevs.com/newswire/tesla-autobidder-software-aggregates-solar-and-storage-into-a-giant-virtual-utility/"
last_reviewed: 2026-07-18
stale_after_days: 90
related:
  - "_index.md"
  - "sunrun.md"
  - "renew-home.md"
  - "../batteries/tesla-megapack.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Glossary

- **Autobidder** — Tesla's AI-driven software platform that autonomously bids and dispatches battery assets (Powerwall fleets and Megapack installations) into wholesale energy markets and grid-services programs in real time.
- **DSGS** — Distributed Storage Grid Services; Tesla's branding for the utility/grid-program layer that lets enrolled Powerwall owners opt into VPP participation.

## Summary

Tesla's residential energy business — distinct from its separate [Megapack]({{< relref "../batteries/tesla-megapack.md" >}}) utility-scale storage product line — operates virtual power plants built from customer-owned Powerwall home batteries, coordinated by Tesla's Autobidder software. Tesla has run Powerwall-based VPPs in California, Texas, New England, and Puerto Rico, and in March 2026 obtained an electricity supply license in the UK to operate one there as well. In June 2026, Tesla joined Sunrun and Renew Home in a joint 16.8 GW VPP program explicitly marketed to hyperscalers and AI datacenter operators.

## Key Facts

- **Business unit:** Tesla Energy (part of Tesla, Inc., NASDAQ: TSLA); shares a software platform with the separate Megapack utility-storage business but operates a distinct residential VPP product
- **Core hardware:** Powerwall home battery (paired with or without solar)
- **Core software:** Autobidder (autonomous real-time market bidding/dispatch) and DSGS (Distributed Storage Grid Services, the utility-program enrollment layer)
- **Fleet scale (2025, company-reported):** More than 1 million Powerwalls installed globally, supporting over 89,000 VPP dispatch events, with a company-stated $1 billion+ in cumulative homeowner electricity bill savings
- **Geographic footprint:** Active VPP programs in California, Texas, New England, and Puerto Rico (US); UK electricity supply license granted by Ofgem effective March 11, 2026, enabling a UK VPP
- **2026 joint program:** Part of the Sunrun/Tesla/Renew Home 16.8 GW joint VPP announcement (June 24, 2026) aimed at AI datacenter and hyperscaler demand

## What It Is / How It Works

Tesla Energy's residential VPP model enrolls Powerwall owners into utility or grid-operator programs, then uses the Autobidder software platform to autonomously dispatch the aggregated fleet — discharging to the grid or reducing home draw — in response to real-time price signals or grid operator calls, without requiring manual intervention from either Tesla or the homeowner. The same Autobidder platform also manages Tesla's grid-scale Megapack installations, giving Tesla a shared software layer spanning both ends of the storage market. Participating homeowners are typically compensated via bill credits, direct payments, or reduced electricity rates in exchange for enrolling their battery in the program (mechanics vary by program/region and were not independently itemized for every market as of this review).

The June 2026 joint announcement with Sunrun and Renew Home follows the same overall logic described in [Sunrun's entry]({{< relref "sunrun.md" >}}): existing residential fleets are increasingly being repackaged and marketed directly to hyperscalers and AI datacenter developers as fast, flexible capacity that sidesteps multi-year grid interconnection queues, rather than being sold only into traditional utility peak-shaving programs.

## Notable Developments

- **2026-06-24:** Joined Sunrun and Renew Home in announcing a joint 16.8 GW VPP program (combined ~7.8 GW of batteries from Sunrun/Tesla, ~9 GW of smart thermostats from Renew Home) marketed to hyperscalers, utilities, and PJM's upcoming reliability backstop procurement; the group claims 300+ MW immediately available in northern Virginia's "Data Center Alley."
- **2026-03-11:** Ofgem granted Tesla Energy Ventures Limited an electricity supply license in the UK, effective this date, enabling Tesla to operate a Powerwall-based VPP there in exchange for tariff economics for participating owners.
- **2025:** Global Powerwall network passed 1 million installed units and supported more than 89,000 VPP events in the year, per company-reported figures.

## Key People

Tesla Energy's VPP business does not have a dedicated, separately disclosed leadership team distinct from Tesla's overall executive structure as of this review — TODO: identify and verify the specific Tesla Energy VPP/Autobidder product leadership if a future update requires it.

### Key People — Last Reviewed: 2026-07-18

## Claim Verification

### Claim: Tesla's global Powerwall VPP network supported "over 89,000 VPP events" across "over 1 million installed units" in 2025, saving homeowners "over $1 billion" in electricity costs

**Status:** Unverified

**Supporting sources:**
- Company-reported figures circulated in industry coverage (e.g., Charged EVs, 24/7 Wall St.) attributed to Tesla's own disclosures; no Tesla-issued press release or SEC filing with this exact figure set was independently fetched and confirmed in this session.

**Refuting / questioning sources:**
- None found; but this entry could not trace the figures to a single, dated, primary Tesla source fetched during this review — TODO: locate and cite the specific Tesla shareholder deck, impact report, or press release containing these numbers.

**Summary:** These are widely repeated company-attributed figures, but this review could not confirm them against a fetched primary Tesla source. Treat as company-reported and unverified pending direct citation.

## Sources

- [Tesla, Sunrun, Renew Home team up on massive 16GW virtual power plant (Canary Media, Jun 24, 2026)](https://www.canarymedia.com/articles/virtual-power-plants/tesla-sunrun-renewhome-vpp)
- [Tesla Virtual Power Plant With DSGS (Tesla Support)](https://www.tesla.com/support/energy/virtual-power-plant/dsgs)
- [Tesla Autobidder software aggregates solar and storage into a giant virtual utility (Charged EVs)](https://chargedevs.com/newswire/tesla-autobidder-software-aggregates-solar-and-storage-into-a-giant-virtual-utility/)
