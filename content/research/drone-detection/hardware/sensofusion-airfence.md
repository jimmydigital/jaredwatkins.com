---
title: "Sensofusion Airfence"
date: 2026-07-07
lastmod: 2026-07-07
draft: false
description: "Finnish passive drone detection system, in commercial deployment since 2016, that locates drones and their pilots by monitoring control-link RF rather than relying on cooperative Remote ID broadcasts."
research_area: "drone-detection/hardware"
source_urls:
  - "https://sensofusion.com/"
  - "https://sensofusion.com/airfence-productline/"
  - "https://sensofusion.com/military/"
last_reviewed: 2026-07-07
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Sensofusion is a Finnish company (headquartered in Vantaa) whose Airfence system is a passive RF drone detection platform used by military and law enforcement customers. Airfence has been in commercial deployment since 2016 across Europe, North America, the Middle East, and Asia — one of the longer operational track records in this category. It provides real-time location of both the drone and its pilot by passively monitoring control-link RF emissions, independent of whether the drone broadcasts Remote ID. **Limitation:** as with all RF-based detection, effectiveness depends on the drone actively transmitting a control or video link; it cannot see fiber-optic tethered or fully autonomous RF-silent drones.

## Key Facts

- **Manufacturer:** Sensofusion, Vantaa, Finland
- **Type:** Company — passive RF detection hardware + software (Airfence product line)
- **Flagship product:** Airfence (civilian/government edition) and Airfence Military Edition
- **Deployment history:** In commercial use since 2016; government customers across Europe, North America, the Middle East, and Asia
- **Status:** Active; positioned for both civilian/government security customers and military use with a separate "Military Edition" offering integrated countermeasures

## How It Works

Airfence passively monitors RF spectrum for drone control-link and video-downlink emissions, using this to compute real-time positions for both the drone and its remote pilot without needing to decode or rely on any cooperative identification signal from the drone itself. This distinguishes it from Remote ID receivers, which depend on the drone voluntarily broadcasting ASTM F3411 telemetry — Airfence's detection works against any drone actively using its RF control link, compliant or not.

The base Airfence product line is detection-and-locate only, aimed at security and law enforcement customers who need situational awareness but not interdiction authority. **Airfence Military Edition** extends the same detection core with an integrated set of countermeasures, positioned by Sensofusion as "combat-proven," for customers with legal authority to interdict (a distinction relevant to this section's US legal-authority steering, though Sensofusion's countermeasure availability is governed by the purchaser's own jurisdiction, not US law).

## Capabilities

- **Passive RF detection:** Locates drones via control-link/video-link RF emissions without needing Remote ID cooperation
- **Pilot geolocation:** Locates the operator's control unit alongside the drone itself
- **Tiered product line:** Civilian/government detection-only edition (Airfence) and a military edition with integrated countermeasures
- **Export controls:** Sensofusion states it does not sell to organizations facing EU sanctions, and requires purchasers to pre-qualify via official organizational email before purchase

## Limitations

- **RF-only:** No stated capability against fiber-optic tethered or fully RF-silent autonomous drones — the same physics limitation shared by every RF-based system in this section
- **Limited public technical detail:** Unlike Aaronia or CRFS, Sensofusion publishes comparatively little public specification data (frequency range, precise detection range, geolocation technique) — most detail is behind a sales-qualification process
- **Detection-only base product:** Countermeasure capability is reserved for the Military Edition and is likely restricted to government/military purchasers with appropriate legal authority

## Notable Developments

- **2026-04:** Launched Sensofusion Aviation, extending counter-drone systems to aviation-specific use cases, alongside acquisition of Atol Aviation
- **2025:** Received the Newcomer Company Award from the President of Finland; reported 2024 turnover of €20.8M with exports accounting for nearly 100% of revenue

## Key People

- **Tuomas Rasila** — Founder and CEO (founded Sensofusion in 2014); background in defense/radio technology, became interested in drones and subsequently counter-drone systems

### People — Last Reviewed: 2026-07-07

## Claim Verification

### Claim: 2024 turnover of €20.8M, nearly 100% export revenue
**Status:** Reported via a Finnish government award announcement, a more independent source than typical vendor marketing.
**Supporting sources:** Finnish Government internationalization award coverage (via search; primary government URL not directly captured in this review — verify at valtioneuvosto.fi).
**Refuting/questioning sources:** None found.
**Summary:** More credible than a bare company claim given the government source, but the entry should be updated with a direct link once the primary announcement is re-verified.

## Sources

- [Sensofusion — company homepage](https://sensofusion.com/)
- [Airfence product line](https://sensofusion.com/airfence-productline/)
- [Airfence Military Edition](https://sensofusion.com/military/)
