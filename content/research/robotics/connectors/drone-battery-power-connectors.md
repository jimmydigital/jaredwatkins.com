---
title: "Drone Battery Power Connectors (XT/AS/Molex/Smart-Battery Series)"
date: 2026-07-14
lastmod: 2026-07-14
draft: false
description: "The commodity battery quick-disconnect layer for commercial and hobbyist drones — XT60/XT90, AS150, Molex, ACES, and emerging smart-battery power+data connectors — almost entirely designed and manufactured in China."
research_area: "robotics/connectors"
source_urls:
  - "https://www.grepow.com/blog/what-are-commercial-drone-battery-connector-types.html"
  - "https://www.china-amass.net/xt60/"
last_reviewed: 2026-07-14
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Unlike the mil-spec Micro-D/circular connector tier used in defense and high-reliability robotics ([Micro-D / Nano-D Connectors]({{< relref "micro-d-connectors.md" >}})), the battery quick-disconnect connectors used in commercial and hobbyist drones are a commodity layer dominated by a small number of bullet-and-socket connector families — XT-series, AS-series, and Molex-style balance connectors — almost all originating from and manufactured in China.

## Key Facts

- Type: Connector standard family / technology (not a single mil-spec standard; these are de facto industry standards set by manufacturer adoption)
- Status: Active; XT-series and AS-series in near-universal use across commercial and hobbyist drones as of 2025
- Key manufacturers: Amass (China; Changzhou, Jiangsu — manufacturer of the XT and AS connector families), various Chinese connector OEMs producing XT/AS-compatible parts, Molex (balance/signal connectors), Power Data Connectors (PDC1810F0002 smart battery connector)
- Key metric(s): XT60 rated ~60A continuous; XT90 up to 90A continuous (120A peak); AS150 ~150A continuous; AS150U ~70–75A continuous (140–150A instantaneous) with added BMS signal pins

## What It Is / How It Works

Drone battery connectors fall into a few current-rating tiers depending on platform size and power draw. The XT-series (XT30, XT60, XT90) uses gold-plated bullet-and-socket contacts in a polarized nylon housing and is the most widely used family across mid-range RC vehicles and drones; XT90S adds anti-spark technology (a resistor-mediated pre-connection sequence) to reduce arcing damage when connecting high-voltage LiPo packs (6S–12S). The AS-series (AS150, AS150U) steps up to heavy-duty 7mm gold-plated bullet contacts for high-current, high-voltage industrial and agricultural drones, with AS150U adding smaller signal pins alongside the main power pins so a smart battery can relay temperature, voltage, and cell-health telemetry to the drone or charger via its battery management system (BMS).

Separately, Molex-brand connectors (not a single connector but a family, e.g. the Mini-Fit Jr. series) are commonly used for balance-charging leads, BMS signal cables, and ESC (electronic speed controller) signal interfaces rather than main battery power, valued for secure locking and configurable pin count/pitch. ACES (Advanced Connector Engineering Systems) connectors are a smaller, higher-reliability category used in aerospace, medical, and high-reliability drone applications, offering high mating-cycle counts, IP-rated sealing, and EMI shielding closer in spirit to the mil-spec tier, though less standardized and documented than Micro-D.

A newer category — smart battery connectors — combines high-current power delivery with CAN/SMBus data pins in a single compact shell, purpose-built for autonomous battery-swap docking stations used in BVLOS (beyond visual line of sight) commercial drone operations. The PDC1810F0002 connector from Power Data Connectors is one documented example, designed for plug-and-play smart battery integration in enterprise-level autonomous drone systems.

The defining supply chain fact about this connector tier is geographic: Amass, headquartered in Changzhou, Jiangsu, China, manufactures the XT and AS connector families that have become the de facto global standard for drone and RC battery quick-disconnects, including a documented "Intelligent robots" and "Model aircraft drone" solutions line on its own corporate site. This stands in sharp contrast to the mil-spec Micro-D/circular connector tier, which is manufactured almost entirely in the US and Western Europe — see the parent [Robotics Connectors]({{< relref "_index.md" >}}) supply chain section for the fuller comparison. Company-published claims about Amass's founding history, exact XT60 introduction date, and named OEM customers (e.g. DJI, Parrot, Ninebot) circulate in secondary sources but could not be independently confirmed against a primary company source in this session; treat such specifics as unverified pending direct confirmation.

## Sources

- [Common Commercial Drone Battery Connector Types | Grepow](https://www.grepow.com/blog/what-are-commercial-drone-battery-connector-types.html) — XT/AS/Molex/ACES/PDC1810F0002 connector type descriptions, current ratings, anti-spark technology, and application guidance
- [AMASS Xt60 Manufacturer and Supplier, Factory Pricelist | Amass](https://www.china-amass.net/xt60/) — Amass corporate site confirming Changzhou, Jiangsu manufacturing location and robotics/drone product solution lines
