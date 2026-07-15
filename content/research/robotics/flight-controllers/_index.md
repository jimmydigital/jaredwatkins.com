---
title: Flight Controllers & Autopilot Hardware
date: 2026-07-15
lastmod: 2026-07-15
draft: false
description: Flight control and companion computer hardware for drones and robots — the Pixhawk/PX4/ArduPilot open-hardware ecosystem, Blue UAS-compliant autopilots, and the software layer that runs on top of them.
research_area: "robotics/flight-controllers"
last_reviewed: 2026-07-15
stale_after_days: 180
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


## Overview

The flight controller is the compute layer that everything else in a drone or robot's electronics stack ultimately serves: sensors ([Robotics Sensors]({{< relref "../sensors/_index.md" >}})) feed it, connectors ([Robotics Connectors]({{< relref "../connectors/_index.md" >}})) wire it in, actuators ([Robotics Actuators]({{< relref "../actuators/_index.md" >}})) take orders from it. The dominant hardware standard is Pixhawk — an open-hardware specification produced by multiple competing manufacturers — running one of two open-source autopilot firmware stacks, PX4 or ArduPilot. Above the raw flight-control layer sits a newer category of AI-capable "companion computers" and mission computers that add onboard autonomy, vision-based navigation, and secure communications for defense and BVLOS commercial use.

## Key Themes

- Pixhawk is an open-hardware standard, not a single product: Holybro, CUAV, and others manufacture competing Pixhawk-compliant boards to the same reference design, mostly out of China/Hong Kong.
- PX4 and ArduPilot are the two dominant open-source autopilot firmware stacks; PX4 is stewarded by the Dronecode Foundation (part of the Linux Foundation) and originated from Lorenz Meier's academic work at ETH Zurich.
- The Blue UAS Framework (US DoD Defense Innovation Unit initiative) has created a distinct, NDAA-compliant tier of US-made autopilots (ModalAI VOXL, Auterion Skynode) explicitly positioned as an alternative to Chinese-manufactured flight controller hardware.
- Companion/mission computers (ModalAI VOXL 2, Auterion Skynode X) now integrate the real-time flight controller function alongside a separate high-performance AI compute core (e.g. Qualcomm QRB5165) on one board, blurring the historical line between "flight controller" and "companion computer."
- Software is consolidating around fleet-level operating systems: Auterion's shift from single-autopilot software (AuterionOS) toward multi-vehicle swarm coordination (Nemyx) reflects a broader move from individual-drone autonomy to coordinated fleet autonomy, particularly in defense contexts.
- War in Ukraine has accelerated defense procurement of low-cost, software-defined autopilot stacks at scale, with Auterion citing tens of thousands of units delivered under a Pentagon contract.

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [ModalAI](https://www.modalai.com) | San Diego, CA, USA | Private (founded 2018 by ex-Qualcomm engineers) | VOXL/VOXL 2 Blue UAS Framework autopilots and companion computers; PX4 flight controller plus onboard AI compute in a single SWaP-optimized module; assembled in the USA. |
| [Auterion](https://auterion.com) | Arlington, VA, USA (engineering in Zurich, Switzerland and Munich, Germany) | Private, Series B ($130M, Sept. 2025, led by Bessemer Venture Partners; ~$600M+ valuation) | AuterionOS (commercial PX4 distribution) and Skynode all-in-one autopilot/mission computer; Nemyx multi-domain swarm coordination software; deployed in Ukraine. |
| [Holybro](https://holybro.com) | Hong Kong / Shenzhen, China | Private | Pixhawk-standard flight controllers (Pixhawk 4, Pixhawk 6C) manufactured in official collaboration with the PX4 development team. |
| [CUAV](https://www.cuav.net) | Guangdong, China | Private | Trademark-authorized Pixhawk manufacturer (Pixhack, CUAV V5/X7 series); also produces GNSS modules and wireless data/video links for the same platforms. |

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [QCOM](https://finance.yahoo.com/quote/QCOM) | [Qualcomm](https://www.qualcomm.com) | QRB5165 SoC powers ModalAI's VOXL 2 companion computer; broader Snapdragon Flight/RB5 platform push into drone and robotics compute. |
| [STM](https://finance.yahoo.com/quote/STM) | [STMicroelectronics](https://www.st.com) | STM32 microcontrollers are the dominant MCU family underlying classic Pixhawk-series flight controller boards. |

## Supply Chain

### Supply Chain Layers

| Layer | Key Inputs / Outputs | Companies Operating Here | Geographic Risk |
|-------|---------------------|--------------------------|-----------------|
| **1. Flight-control silicon** | Real-time MCUs (STM32-class) for classic Pixhawk boards; AI-capable SoCs (Qualcomm QRB5165) for companion computers | [STMicroelectronics](https://www.st.com), [Qualcomm](https://www.qualcomm.com) | MCU/SoC design is US/EU-based; fabrication is concentrated at Asian foundries (see [Semiconductors]({{< relref "../../semiconductors/_index.md" >}}) section) |
| **2. Open-source autopilot firmware** | PX4, ArduPilot flight-control software stacks | Dronecode Foundation (Linux Foundation project, stewards PX4), ArduPilot open-source community | Globally distributed open-source development; not a single-company or single-country dependency |
| **3. Flight controller hardware manufacturing** | Pixhawk-standard circuit boards and enclosures | [Holybro](https://holybro.com), [CUAV](https://www.cuav.net), other Pixhawk-compliant manufacturers | Manufacturing concentrated in China/Hong Kong for the commodity/hobbyist tier |
| **4. Companion / mission computers** | AI-capable onboard compute combining flight control with vision-based autonomy, secure comms, and edge inference | [ModalAI](https://www.modalai.com) (VOXL/VOXL 2), [Auterion](https://auterion.com) (Skynode) | US-designed and assembled specifically to create an alternative to layer 3's Chinese-concentrated hardware base |
| **5. Fleet/OS software layer** | Commercial autopilot OS distributions, multi-vehicle swarm coordination software | [Auterion](https://auterion.com) (AuterionOS, Nemyx) | US/EU-based software vendors |

### Key Supply Chain Notes

**Blue UAS as a deliberate supply chain intervention:** The Blue UAS Framework, run by the DoD Defense Innovation Unit, exists specifically because the dominant Pixhawk-hardware manufacturing base (Holybro, CUAV) is Chinese/Hong Kong-based, creating the same category of supply chain and data-security concern documented elsewhere in this robotics knowledge base (see DJI in [Aerial Drones]({{< relref "../aerial-drones/_index.md" >}}) and Quectel in [Communications]({{< relref "../communications/_index.md" >}})). ModalAI's VOXL was explicitly developed as "the first Blue UAS Framework autopilot," and its VOXL 2 press materials state it "addresses supply chain concerns around unreliable, unsecure components from foreign manufacturers."

**⚑ Shared open-source dependency — PX4:** Both ModalAI's VOXL 2 and Auterion's Skynode run PX4 at their core (Auterion's entire commercial model is built on commercializing PX4, which its founder Lorenz Meier originated academically). A vulnerability or architectural limitation in PX4 itself would ripple across both companies' product lines simultaneously, despite their otherwise-competing market positions.

**Open hardware ≠ open supply chain:** Because Pixhawk is a published open-hardware reference design, any manufacturer can produce compliant boards — in practice this has meant the actual manufacturing base skews heavily toward Chinese/Hong Kong contract producers even though the standard itself and its firmware are open and globally governed.

### Supply Chain — Last Reviewed: 2026-07-15
