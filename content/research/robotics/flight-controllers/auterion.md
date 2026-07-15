---
title: "Auterion"
date: 2026-07-15
lastmod: 2026-07-15
draft: false
description: "Commercializer of the open-source PX4 autopilot; maker of the Skynode flight controller/mission computer and Nemyx multi-domain swarm coordination software, deployed in Ukraine and backed by a $130M Series B."
research_area: "robotics/flight-controllers"
source_urls:
  - "https://auterion.com/auterion-raises-130-million-series-b-as-their-ai-enabled-software-powering-low-cost-commercial-hardware-at-scale-transforms-warfare/"
last_reviewed: 2026-07-15
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Auterion is a software company that commercializes PX4, the open-source autopilot originated by its founder Lorenz Meier at ETH Zurich, into AuterionOS and the Skynode autopilot/mission computer hardware line. It has pivoted increasingly toward defense, positioning its Nemyx product as software for coordinating autonomous drone swarms across air, land, and sea domains, and its technology is deployed in active combat use in Ukraine.

## Key Facts

- Founded: 2017, in Zurich, Switzerland
- Type: Software/AI layer supplier (with its own hardware line, Skynode); also a flight-controller hardware vendor
- Status: Active, private, Series B ($130M raised September 2025, led by Bessemer Venture Partners, valuing the company at "north of $600 million")
- Key metric(s): $25M of the Series B is non-dilutive capital from the US Department of War's Office of Strategic Capital; company states it is delivering "tens of thousands" of AI "strike kits" to Ukrainian forces under a Pentagon contract
- Value chain position: Software/AI layer (AuterionOS, Nemyx) plus companion/mission-computer hardware (Skynode), sitting above the raw PX4 flight-control layer described in [Flight Controllers & Autopilot Hardware]({{< relref "_index.md" >}})

## What It Is / How It Works

Auterion's foundational product, AuterionOS, is a commercial distribution of PX4 — adding enterprise features, security, and interoperability on top of the open-source core — intended to let drones from multiple hardware manufacturers run a common operating system rather than each requiring bespoke firmware. Its Skynode (and Skynode X) hardware is an all-in-one autopilot and mission computer that can be retrofitted onto existing drone airframes, adding AI-powered autonomy, secure communications, and edge computing; the company markets it as NDAA-compliant for kinetic military use and prices it "comparably to consumer electronics."

The company's more recent product, Nemyx, extends this from single-drone autopilot software toward multi-vehicle swarm coordination, reflecting a strategic shift the company describes as building "swarms, not individual drones" — letting one operator coordinate many autonomous vehicles across air, land, and sea simultaneously. Auterion frames this shift as a direct lesson from the war in Ukraine, where its technology has been deployed in active combat and where — per the company's own September 2025 funding announcement — it is delivering tens of thousands of AI-enabled "strike kits" to Ukrainian forces under a Pentagon contract, which it characterizes as the largest deployment of autonomous technology in the West to date. Auterion has documented partnerships with Rheinmetall, Lockheed Martin, and other aerospace/defense manufacturers across the US, Europe, and allied nations, consistent with its open-architecture, multi-manufacturer positioning versus proprietary single-vendor autopilot stacks.

## Notable Developments

- **2025-09-23:** Auterion raises $130 million Series B led by Bessemer Venture Partners (with continued participation from Lakestar, Mosaic Ventures, and Costanoa Ventures), including $25M in non-dilutive capital from the US Department of War's Office of Strategic Capital; valuation reported at "north of $600 million."
- **2025 (ongoing):** Company reports delivering tens of thousands of AI "strike kits" to Ukrainian forces under a Pentagon contract.
- **2017:** Auterion founded in Zurich, Switzerland, to commercialize the PX4 open-source autopilot.

## Key People / Key Organizations

- **Lorenz Meier** — Founder and CEO, Auterion; originated PX4 academically at ETH Zurich. LinkedIn: not found.
- **Alex Ferrara** — Partner, Bessemer Venture Partners; joined Auterion's board as part of the 2025 Series B. LinkedIn: not found.

**⚑ Shared technology dependency:** Auterion's entire commercial model depends on PX4, the same open-source flight-control core used by competitor ModalAI's VOXL 2 ([ModalAI]({{< relref "modalai.md" >}})) — the two companies compete on hardware and OS layers while sharing the same underlying firmware dependency.

### People — Last Reviewed: 2026-07-15

## Sources

- [Auterion raises $130 Million Series B](https://auterion.com/auterion-raises-130-million-series-b-as-their-ai-enabled-software-powering-low-cost-commercial-hardware-at-scale-transforms-warfare/) — funding details, founder statement, Skynode/AuterionOS/Nemyx product positioning, Ukraine deployment claims, HQ and engineering locations
