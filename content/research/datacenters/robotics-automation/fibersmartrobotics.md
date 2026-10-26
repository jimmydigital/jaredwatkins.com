---
title: "FiberSmart Robotics"
date: 2026-03-25
lastmod: 2026-10-23
draft: false
description: "Robotic fiber patch management company (formerly Wave2Wave Solution); ROME robotic optical switch (200 to 2,000+ fibers per unit, 1 µm positioning claimed), ROMER mobile robot (launch pending), DC Twin digital twin; customer logos include Microsoft, Vodafone, NTT, Juniper and Booking.com; $500K annual savings per unit claimed; HQ listed as San Francisco on company site and Napa by CB Insights."
research_area: "datacenters/robotics-automation"
source_urls:
  - "https://fibersmartrobotics.ai/"
  - "https://fibersmartrobotics.ai/rome/"
  - "https://fibersmartrobotics.ai/about/"
  - "https://blog.fibersmart.ai/rome-from-fibersmart-the-coolest-tech-you-didnt-know-you-needed/"
  - "https://convergedigest.com/wave2wave-expands-its-line-of-robotic/"
  - "https://www.cbinsights.com/company/fibersmart"
  - "https://fibersmart.net/"
last_reviewed: 2026-10-23
stale_after_days: 180
related:
  - "datacenters/robotics-automation/_index.md"
  - "datacenters/robotics-automation/senko.md"
  - "datacenters/robotics-automation/softbank-robot-rack.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

FiberSmart Robotics, formerly Wave2Wave Solution, makes software-directed robotic fiber switches that reconfigure optical patch connections in datacenters and carrier facilities without a technician handling cables. The flagship ROME (Robotic Optical Management Engine) comes in sizes from about 200 fibers (ROME Mini) to up to 2,000 fibers in a single bay (ROME MAX), with a mobile robot, ROMER, listed as "expected to launch soon" and a cloud digital twin, DC Twin. The company shows logos for Microsoft, Vodafone, KPN, NTT, Salesforce, Juniper, Ciena and others and states a lights-out datacenter goal. Revenue, headcount and funding were not found in any source reviewed; the company's own figures (100+ customers, $500,000 annual savings per unit) are unaudited.

## Key Facts

- **Name history:** Wave2Wave Solution (David Wang, President and CEO in 2018), now FiberSmart Robotics; founding year not stated on the company's About page
- **HQ:** San Francisco, CA per the company's website; Napa, CA (1300 1st St., Suite 368) per CB Insights
- **Type:** Private; no funding disclosure found
- **Products:** ROME (robotic optical switch), ROMER (mobile datacenter robot, not yet launched per the website), DC Twin (cloud 3D digital twin with port-level visibility)
- **ROME models (per company):**
  - ROME Mini: 7RU, 200 fibers
  - ROME 500: 10+1RU, 512 fibers
  - ROME Q: 64Q or 128Q, MPO interfaces for QSFP devices
  - ROME MAX: up to 2,000 fibers in one bay
- **Company-stated performance:** 1 µm positioning accuracy; 50–150 W power; 3 million connect/disconnect cycles; passive mechanical latching keeps circuits up during power loss; single-mode and multi-mode fiber
- **Customer logos shown:** Hitachi Vantara, Virgin Media, Vodafone, KPN, Ciena, Salesforce, Fujitsu, NTT, Booking.com, Juniper Networks, Microsoft
- **Company-stated outcome:** $500,000 savings per ROME unit per year (the website attributes it to Microsoft in one place and Juniper in another)
- **Competitors named by CB Insights:** SENKO Advanced Components, Telescent, Summit Infrastructure Group

## What It Is / How It Works

Fiber patch panels connect servers, switches and optical transport gear through manually placed jumpers. Changing a circuit means a technician finds the ports, moves the jumper and reseats the connectors, which is slow in dense panels and a common source of errors.

**ROME** replaces that step with robots inside a rack-mounted unit. Per the company, two robots in each unit handle hundreds of fibers, and a software interface lets an operator or automation system request a connection that ROME makes physically. The system keeps a live record of what is connected to what, and passive latching holds circuits when power is lost. The company says ROME is protocol agnostic and works with both single-mode and multi-mode fiber.

**ROMER** is described as a mobile robot for cabling, equipment swaps and diagnostics across a datacenter. The website says it is "expected to launch soon"; the About page calls it recent without a date. It remains unlaunched in sources reviewed.

**DC Twin** is a cloud-based 3D model synchronized to port-level connection data.

**Context.** ROME manages existing patch-panel plant and complements approaches that remove patch cables, such as the blind-mate optical connections in the [SoftBank Robot Rack]({{< relref "softbank-robot-rack.md" >}}). Connector makers such as [Senko]({{< relref "senko.md" >}}) address the same layer from the connector side.

## Notable Developments

- **2025-09:** Company website last updated; positions ROME as part of a "lights-out" datacenter goal and lists ROMER as expected to launch soon. ([FiberSmart](https://fibersmartrobotics.ai/))
- **2025-03:** Company blog post describes ROME as protocol agnostic, citing 800G and beyond, with no named customers or measurements. ([FiberSmart blog](https://blog.fibersmart.ai/rome-from-fibersmart-the-coolest-tech-you-didnt-know-you-needed/))
- **2024-08:** Lightstorm launches the Polarin DCI Wave, a Layer 1 product built with FiberSmart that lets enterprises self-provision optical connections across more than 60 datacenters in India in about 10 minutes (per CB Insights). ([CB Insights](https://www.cbinsights.com/company/fibersmart))
- **2018-11:** Wave2Wave adds ROME 64Q and ROME 128Q with MPO interfaces (512 and 1,024 fiber connections). ([Converge Digest](https://convergedigest.com/wave2wave-expands-its-line-of-robotic/))
- **2014:** Wave2Wave acquires a company in Israel, according to the company's About page. ([FiberSmart](https://fibersmartrobotics.ai/about/))

## Key People

### David Wang — President and CEO (as of November 2018)
- **LinkedIn:** not found
- **Role:** President and CEO of Wave2Wave Solution in 2018 per Converge Digest; current title not confirmed on the company's website, which lists no leadership
- **Source:** [Converge Digest](https://convergedigest.com/wave2wave-expands-its-line-of-robotic/)

No other people were confirmed from fetched sources.

### People — Last Reviewed: 2026-10-23

## Supply Chain Position

| Layer | Detail |
|-------|--------|
| **Hardware (ROME unit)** | Servo-driven robots, encoders and fiber-compatible end effectors; component suppliers not disclosed |
| **Connectors supported** | MPO interfaces on ROME Q; other connector types not stated on the product page |
| **Software** | Connection management, analytics and DC Twin; details not published |
| **Customers (downstream)** | Hyperscale, carrier and enterprise logos listed; NTT says testing and deployment at select facilities per FiberSmart |
| **Competitors** | Telescent, SENKO and others per CB Insights |

**⚑ Shared theme:** Robotic fiber patching is one of several approaches to removing manual cabling in this section; see [SoftBank Robot Rack]({{< relref "softbank-robot-rack.md" >}}) for the blind-mate alternative.

## Claim Verification

### Claim: $500,000 annual savings per ROME unit

**Status:** Unverified

**Supporting sources:**
- [FiberSmart website](https://fibersmartrobotics.ai/) — states the figure and attributes it to Microsoft in one section

**Refuting / questioning sources:**
- The same page attributes the figure to Juniper Networks in another section. No customer statement or audit was found.

**Summary:** A company-published number with inconsistent attribution.

### Claim: Human error causes 70–75% of network downtime

**Status:** Unverified

**Supporting sources:**
- [FiberSmart website](https://fibersmartrobotics.ai/) — cites the Uptime Institute for 70–75%; the ROME page cites "industry studies" for 70%

**Refuting / questioning sources:**
- The underlying Uptime Institute figure was not retrieved. The figure covers human-caused downtime generally, not only patching.

**Summary:** A third-party statistic repeated by the company; it does not show how much downtime ROME removes.

### Claim: 1 µm positioning accuracy and 3 million cycles

**Status:** Unverified

**Supporting sources:**
- [ROME product page](https://fibersmartrobotics.ai/rome/) — 1 µm from servo control and encoders; 3 million connect/disconnect cycles

**Refuting / questioning sources:**
- The same page elsewhere describes accuracy as "sub-millimeter," and the page gives no insertion loss, switching speed or test data.

**Summary:** Specifications are claims without published test results.

### Claim: Earthquake and cyber resilience

**Status:** Unverified

**Supporting sources:**
- [ROME product page](https://fibersmartrobotics.ai/rome/) — claims shake-table tests to magnitude 7.0 with no signal loss afterward

**Refuting / questioning sources:**
- No test report or third-party certification found.

**Summary:** Marketing claim only.

## Sources

- [FiberSmart Robotics](https://fibersmartrobotics.ai/)
- [FiberSmart — ROME](https://fibersmartrobotics.ai/rome/)
- [FiberSmart — About](https://fibersmartrobotics.ai/about/)
- [FiberSmart blog — ROME (Mar 2025)](https://blog.fibersmart.ai/rome-from-fibersmart-the-coolest-tech-you-didnt-know-you-needed/)
- [Converge Digest — Wave2Wave expands robotic patch panels (Nov 2018)](https://convergedigest.com/wave2wave-expands-its-line-of-robotic/)
- [CB Insights — FiberSmart](https://www.cbinsights.com/company/fibersmart)
- [FiberSmart Networks](https://fibersmart.net/)
