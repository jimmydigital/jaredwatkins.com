---
title: "WiBotic"
date: 2026-03-31
lastmod: 2026-03-31
draft: false
description: "Seattle startup (University of Washington spinout) providing adaptive resonant inductive wireless charging systems for autonomous drones and ground robots; OC-110/TR-110 system supports up to 125W; Series A funded; remains independent as of March 2026."
tags: ["robotics", "power-systems", "us", "wireless-charging"]
categories: ["company"]
research_area: "robotics/power-systems"
source_urls:
  - "https://www.wibotic.com/about-us/"
  - "https://www.wibotic.com/products/tr-100/"
  - "https://www.therobotreport.com/wibotic-raises-series-a-funding-expand-wireless-robot-charging/"
last_reviewed: 2026-03-31
stale_after_days: 180
related: []
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

WiBotic is a Seattle, Washington startup founded in 2015 as a spinout from the University of Washington's Sensor Systems Lab (Professor Joshua Smith's lab). The company develops adaptive resonant inductive wireless charging systems for autonomous mobile robots and drones, allowing robots to autonomously charge without plug-in intervention. Its OC-110 onboard charger (up to 125W) and TR-110 transmitter pad form the core product for lighter robot and drone applications; the TR-110 PowerPad can be embedded in floors or landing pads for fully autonomous charge cycles. WiBotic remains a private independent company as of March 2026, having raised a Series A in 2022 and additional seed funding through 2024–2025. A strategic partnership with Nabtesco Corporation for distribution in Japan was announced in 2023. **Note:** The task briefing stated WiBotic was "Acquired by Vertiv Holdings (VRT) in 2023" — no public record of such an acquisition was found; available sources confirm WiBotic remains independent.

## Key Facts

- **Founded:** 2015 (Seattle, WA; UW spinout)
- **HQ:** Seattle, WA
- **Type:** Private; Series A funded
- **Key backers:** Series A (2022); Nabtesco Corporation (distribution partnership, Japan, 2023); seed investors including Flying Fish VC and others; $13M+ total raised through Series A and subsequent rounds
- **Key products:** TR-110 Transmitter (up to 125W, floor/pad mount); OC-110 Onboard Charger (robot-side receiver); TR-1000 / TR-3000 higher power transmitters (for larger robots, up to 1000W+); PowerPad landing pad for drones; OmniCharge software
- **Co-founders:** Ben Waters (CEO) and Joshua Smith (Professor of Electrical Engineering, UW)
- **Commercial status:** Active; partnership with Nabtesco for Japan sales; products available through distributors including InDro Robotics

## What It Is / How It Works

WiBotic's wireless charging technology is based on resonant inductive coupling — the same physical principle as consumer wireless phone chargers (Qi standard) but engineered for significantly larger power transfer, longer range, and tolerance to lateral misalignment between the transmitter coil and receiver coil. In a standard inductive charger, the transmitter and receiver must be nearly co-planar and precisely aligned. WiBotic's "adaptive" approach uses a resonant circuit that maintains efficient power transfer across a range of alignment offsets of up to approximately three times the transmitter coil diameter — important because autonomous robots and drones do not dock with millimeter precision.

The system works as follows: AC grid power is converted to a high-frequency wireless power signal by the transmitter (TR-110 or higher); the robot-mounted onboard charger (OC-110) receives this wireless signal and converts it back to DC at the appropriate voltage and current to charge the robot's battery. The OC-110 communicates with the transmitter over a Bluetooth or BLE-based sideband channel to coordinate charge parameters — voltage, current, charge state — enabling a full intelligent charge cycle without any physical connection.

For drone applications, the WiBotic PowerPad is embedded in the landing surface of a drone nest or hangar. When the drone lands (autonomously, within the alignment tolerance), it begins charging without operator intervention. This enables continuous autonomous inspection cycles, extending BVLOS flight time by allowing automatic recharge between missions.

The OC-110 / TR-110 combination supports up to 125W — appropriate for lightweight drones (up to approximately 5 kg) and smaller AMRs. Larger systems (TR-1000, TR-3000) scale to industrial robot power levels. WiBotic's OmniCharge software provides fleet-level charging management, scheduling charge cycles across multiple pads.

## Notable Developments

- **2024-12:** WiBotic raises additional seed funding (~$2M). ([Fundz](https://app.fundz.net/fundings/wibotic-funding-round-0f33d7))
- **2023-11:** Strategic distribution partnership with Nabtesco Corporation announced for WiBotic products in Japan. ([WiBotic](https://www.wibotic.com/news-releases/wibotic-signs-partnership-with-nabtesco-corporation-for-sales-in-japan/))
- **2022:** Series A funding ($5.7M) closed; investors include Flying Fish, Catapult Ventures, and others. ([Automated Warehouse](https://www.automatedwarehouseonline.com/wibotic-gets-a-jolt-to-wireless-battery-charging-with-5-7m-series-a-round/))
- **2015:** WiBotic founded by Ben Waters and Joshua Smith; commercializing UW Sensor Systems Lab wireless power technology originally developed for implanted cardiac devices (LVAD).

## Key People

### Ben Waters — Co-Founder and CEO
- **LinkedIn:** [linkedin.com/in/benwaters](https://www.linkedin.com/in/benwaters/)
- **Education:** Occidental College (BA Electrical Engineering and Physics); Columbia University (MS); University of Washington (PhD Electrical Engineering — wireless power for implanted medical devices, Professor Joshua Smith's lab)
- **Career (reverse-chronological):**
  - WiBotic (2015–present): Co-founder and CEO
  - University of Washington Sensor Systems Lab (PhD research): Wireless power transfer for implanted devices
- **Notes:** Waters is a Puget Sound Business Journal "40 Under 40" honoree (2016). The technology WiBotic commercialized was originally developed to power an LVAD (left ventricular assist device) — a mechanical heart pump — without transcutaneous cables. Robotics companies approached the lab team after seeing the flexible, high-range wireless power transfer capability, and WiBotic was founded on that market demand.

### Professor Joshua Smith — Co-Founder
- **LinkedIn:** Not found (academic profile at UW ECE)
- **Education:** MIT (BS); Harvard (PhD)
- **Role:** Professor of Electrical Engineering at University of Washington; co-founder of WiBotic
- **Notes:** Smith's Sensor Systems Lab is the academic origin of WiBotic's technology. He continues in his academic role while WiBotic commercializes the research.

### People — Last Reviewed: 2026-03-31

## Supply Chain Position

WiBotic operates at the **Subsystem Supplier** layer in the robotics power chain: it sells charging hardware (transmitter + onboard charger + software) to robot OEMs and fleet operators. The transmitter hardware is manufactured by contract (not disclosed). The onboard charger is designed to be integrated into robot platforms by OEMs at design time, requiring both mechanical integration (antenna coil mounting) and electrical integration (DC output wiring to the battery management system). **⚑ Shared supply chain:** WiBotic and Wiferion (German competitor) both operate in the same resonant inductive AMR charging space, targeting the same robot OEM integration opportunity; Wiferion has stronger penetration in European automotive and logistics facilities; WiBotic has stronger drone and lightweight robot market position. Nabtesco's distribution partnership gives WiBotic access to Nabtesco's Japanese AMR OEM customer relationships.

## Claim Verification

### Claim: WiBotic's adaptive wireless charging supports misalignment of up to "three times the diameter of the transmitting coil"
**Status:** Partially verified

**Supporting sources:**
- [WiBotic How It Works page](https://www.wibotic.com/learn/how-it-works/) — Company states "adaptive" range across wide alignment offsets; "up to three times the diameter" is the company specification
- [UW ECE WiBotic profile](https://www.ece.uw.edu/entrepreneurship/wibotic-charged-up-about-wireless-power-for-robots/) — Confirms the technical claim from the lab origin

**Refuting / questioning sources:**
- No independent third-party validation of the specific 3× diameter claim in a controlled test environment has been published; efficiency at maximum offset is not documented in publicly available test reports

**Summary:** The alignment tolerance claim is consistent with the physics of resonant inductive coupling and is the company's stated specification; independent efficiency-vs-offset characterization is not publicly available.

## Sources

- [About WiBotic — WiBotic](https://www.wibotic.com/about-us/)
- [TR-110 Product Page — WiBotic](https://www.wibotic.com/products/tr-100/)
- [Series A Funding — Automated Warehouse / Robot Report](https://www.therobotreport.com/wibotic-raises-series-a-funding-expand-wireless-robot-charging/)
- [Nabtesco Japan Partnership — WiBotic (Nov 2023)](https://www.wibotic.com/news-releases/wibotic-signs-partnership-with-nabtesco-corporation-for-sales-in-japan/)
- [Ben Waters LinkedIn](https://www.linkedin.com/in/benwaters/)
- [UW ECE WiBotic Profile](https://www.ece.uw.edu/entrepreneurship/wibotic-charged-up-about-wireless-power-for-robots/)
