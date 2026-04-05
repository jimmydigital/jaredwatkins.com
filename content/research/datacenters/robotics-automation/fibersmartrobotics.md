---
title: "FiberSmart Robotics"
date: 2026-03-25
lastmod: 2026-03-25
draft: false
description: "Napa, CA robotic fiber patch management company; founded 2003 (as Wave2Wave Solution Corp); CEO David Wang; ROME (Robotic Optical Management Engine) automates optical fiber connections — two robots per unit managing hundreds of fibers with software-directed precision; 100+ customers including Microsoft, Booking.com, Vodafone, NTT; $500K annual savings per unit claimed; $35M revenue (2025)."
tags: ["datacenters", "robotics-automation", "connectivity", "fiber-optic", "us"]
categories: ["company"]
research_area: "datacenters/robotics-automation"
source_urls:
  - "https://fibersmartrobotics.ai/"
  - "https://fibersmart.net/"
last_reviewed: 2026-03-25
stale_after_days: 180
related:
  - "datacenters/robotics-automation/_index.md"
  - "datacenters/robotics-automation/senko.md"
  - "datacenters/robotics-automation/softbank-robot-rack.md"
---

## Summary

FiberSmart Robotics (formerly Wave2Wave Solution Corp) is a Napa, California company founded in 2003 by David Wang that automates optical fiber patch management in datacenters and carrier facilities. Its flagship product, ROME (Robotic Optical Management Engine), deploys two precision robots per unit to manage hundreds of fiber optic patch connections under software control — enabling network reconfiguration via drag-and-drop GUI without human technicians touching physical cables. The company has 100+ customers including Microsoft, Booking.com, Vodafone, KPN, NTT Group, Salesforce, and Fujitsu; Microsoft has cited $500,000 in annual savings per unit. FiberSmart had approximately $35M revenue and 201 employees as of early 2025, operating across North America, Asia, and Europe. A second-generation mobile robot (ROMER) is in development to extend beyond fixed fiber patch panels to free-navigation datacenter tasks. FiberSmart occupies a distinct and commercially proven niche in datacenter automation — not server handling or cooling (like SoftBank/Submer's focus), but the fiber connectivity layer that is currently one of the most labor-intensive and error-prone aspects of datacenter operations.

## Key Facts

- **Founded:** 2003 (as Wave2Wave Solution Corp; rebranded to FiberSmart Robotics)
- **HQ:** Napa, California
- **Type:** Private
- **Founder / CEO:** David Wang
- **Revenue:** ~$35M (as of early 2025)
- **Employees:** ~201 across North America, Asia, and Europe
- **Customers:** 100+ (named: Microsoft, Booking.com, Vodafone, KPN, Ciena, Salesforce, Fujitsu, NTT Group, Hitachi Vantara, Virgin Media, Juniper Networks)
- **Flagship product:** ROME — Robotic Optical Management Engine
- **In-development product:** ROMER — mobile free-navigation datacenter robot
- **Digital twin product:** DC Twin — cloud-based 3D virtual model with port-level visibility
- **Key customer metric:** $500,000 annual savings per ROME unit (Microsoft-cited)
- **Claimed downtime reduction:** 70–75% reduction in human-caused network downtime
- **Provisioning speed:** Reduces fiber reconfiguration from hours to seconds
- **Deployment scope:** Edge computing, hyperscale, carrier/telecom facilities

## What It Is / How It Works

Fiber optic patch management is one of the most persistent operational pain points in large datacenters and carrier facilities. In a typical installation, hundreds to thousands of fiber patch cables connect servers, switches, routers, and optical transport equipment through a patch panel — a physical matrix where any port can be connected to any other port via a jumper cable. When network topology needs to change (new circuit provisioned, equipment replaced, capacity rebalanced), a technician must physically locate the correct fiber port, remove the existing jumper, route a new jumper, and seat both connectors — all while managing the physical density of cables that makes errors highly likely and the root cause of a large fraction of unplanned network outages.

**ROME** replaces this human operation with software-directed robotics:

- Two precision robots are mounted to a frame that spans the patch panel
- Each robot can navigate to any port in the panel, pick up a fiber jumper, and seat it with sufficient accuracy and consistent insertion force to make a low-loss optical connection
- Circuit reconfiguration is initiated through a drag-and-drop GUI — an operator (or an automated system) specifies the desired connection, and ROME executes the physical patch change
- The system maintains a real-time digital record of every physical connection — eliminating the "as-built vs. as-documented" discrepancy that plagues manually patched facilities
- Real-time analytics on circuit utilization and device connectivity are derived from the physical connection map

The $500,000 annual savings per unit (Microsoft) primarily reflects reduced headcount for fiber operations and the elimination of costly network outages caused by human patching errors. The "hours to seconds" provisioning claim is accurate for the physical patch step — automated robots can execute a patch change in seconds; human technicians may take 30–60 minutes to locate, manage, and seat fibers correctly in a dense panel.

**ROMER** (in development) extends the ROME concept from fixed patch panels to free navigation. Where ROME is a fixed-installation robot that can only service the panel it's mounted to, ROMER is a mobile robot designed to navigate datacenter aisles and handle cabling, equipment swaps, and diagnostics at any location. This is a substantially harder problem (navigation, collision avoidance, diverse connector types across manufacturers) and represents FiberSmart's longer-term roadmap toward a more general datacenter robotics platform.

**DC Twin** provides a cloud-based 3D virtual model of the physical datacenter synchronized with ROME's physical connection data — port-level visibility of what is physically connected where, accessible remotely. For large distributed datacenter estates, this remote management capability was highlighted by Booking.com as critical during COVID lockdowns when on-site access was restricted.

**Positioning relative to other approaches:** FiberSmart addresses the fiber connectivity layer specifically — the software-defined networking world has abstracted routing and switching, but physical fiber connections remain manual. SoftBank's cable-less rack (see [SoftBank Robot Rack]({{< relref "softbank-robot-rack.md" >}})) eliminates fiber patch cables at the server level via blind-mate optical connectors — a different approach to the same underlying problem. At hyperscale, the cable-less rack approach (no patch panels, blind-mate at server insertion) and ROME (robotic management of existing patch panels) are complementary: cable-less racks eliminate new patch requirements for AI compute servers; ROME manages the existing legacy fiber plant that will persist in mixed-technology facilities for years.

## Notable Developments

- **2025 (early):** Revenue at ~$35M; 201 employees; 100+ ROME installations across 3 continents
- **Active (2025):** ROMER mobile robot in development; no commercial release date announced
- **~2020 (COVID):** Booking.com deployment highlighted as enabling remote datacenter management during facility access restrictions — important reference case for the value of remote fiber management
- **~2019–2021 (rebrand):** Wave2Wave Solution Corp rebrands to FiberSmart Robotics; signals strategic shift from services to product company identity
- **2003:** Founded by David Wang as Wave2Wave Solution Corp

## Key People

### David Wang — Founder and CEO
- **LinkedIn:** Search "David Wang FiberSmart" (common name — verify carefully against Napa, CA location)
- **Role:** Founder and CEO since 2003
- **Background:** Founded Wave2Wave; built the company from a services business to a product company with a proprietary robotic platform over 20+ years; the long tenure suggests deep domain expertise in fiber connectivity operations at scale
- **Notes:** No public investor relations profile or frequent media presence; the company appears to have grown primarily through product adoption and word-of-mouth rather than venture capital and PR

### People — Last Reviewed: 2026-03-25

## Supply Chain Position

FiberSmart is a robotics hardware and software company. Its position in the datacenter automation supply chain:

| Layer | Detail |
|-------|--------|
| **Hardware (ROME unit)** | Precision robotic arms, linear motion systems, fiber-compatible end effectors; component suppliers not disclosed |
| **Optical connectors** | ROME handles standard LC, SC, MPO/MTP fiber connectors — it works with existing fiber plant, not a proprietary connector format |
| **Software** | Proprietary GUI, connection management database, analytics platform, DC Twin digital twin |
| **FiberSmart's position** | Full-stack (hardware + software + service) for robotic fiber patch management |
| **Customers (downstream)** | Hyperscalers, telecoms, carriers, enterprise IT; named customers span multiple verticals |
| **Competitors** | No direct named competitor in robotic fiber patching occupies the same commercial scale; Telescent (acquired by AFL) is in a related space; manual patching services from CDW, Siemon, Panduit are the primary alternative |

**⚑ Telescent / AFL as indirect competitor:** AFL (a subsidiary of Fujikura, Japan) acquired Telescent, a robotic fiber patching startup. Fujikura is one of the world's largest fiber optic cable manufacturers. This acquisition means FiberSmart faces a well-capitalized competitor backed by a fiber industry incumbent. The fact that Fujitsu is a named FiberSmart customer despite the Fujikura/AFL/Telescent competitive dynamic is worth monitoring.

**⚑ No VC funding identified:** FiberSmart does not appear to have raised venture capital. $35M revenue with 201 employees over 20 years suggests a bootstrapped or organically funded company — which means its growth is constrained by cash flow rather than runway burn. This is unusual in the current robotics investment environment and could reflect either deliberate independence or difficulty raising institutional capital for a 20-year-old company that doesn't fit typical VC investment profiles.

## Claim Verification

### Claim: $500,000 annual savings per ROME unit (Microsoft)
**Status:** Customer-attributed; not independently audited; plausible given the cost components

**Mechanism:** Savings attributed to headcount reduction (fiber operations technicians are specialized and expensive, especially in Microsoft's Seattle/Bay Area/Dublin facility locations) and reduced outage cost (human patching errors are a leading cause of network incidents).

**Supporting:**
- Microsoft is a named customer — this is not an anonymous case study
- The cost of a single high-severity network outage in a hyperscale facility (lost compute time, engineer response, customer SLA penalties) can easily reach or exceed $500K; preventing even one such incident per year covers the savings claim
- Fiber technician labor in high-cost-of-living markets where hyperscalers operate is $80,000–$150,000+ annually; replacing 3–5 FTE's workload on a panel achieves the savings

**Refuting / questioning:**
- "Per unit" savings assume the unit is serving a high-density, high-change-rate environment; a ROME unit on a rarely-touched legacy panel would show much lower savings
- Microsoft may be the best-case customer (large, dense facility, high labor cost geography); savings at a regional enterprise datacenter would be lower

**Summary:** The $500K figure is credible for hyperscale deployment in a high-labor-cost location. Apply a discount for enterprise or lower-change-rate environments.

### Claim: "70–75% reduction in human-caused network downtime"
**Status:** Company-stated; no methodology published; directionally credible

**Supporting:** Physical patching errors (incorrect port, damaged connector, inadequate insertion) are well-documented causes of network incidents; removing human hands from the operation eliminates this class of errors

**Refuting / questioning:** Residual downtime causes (software, hardware failure, power) are unaffected by ROME; the 70–75% figure applies only to the subset of downtime attributable to human patching, not total downtime

**Summary:** Directionally accurate for the specific failure mode addressed. Total facility downtime reduction would be a smaller percentage.

## Sources

- [FiberSmart Robotics — fibersmartrobotics.ai](https://fibersmartrobotics.ai/)
- [FiberSmart Products — fibersmart.net](https://fibersmart.net/)
- [FiberSmart LinkedIn (formerly Wave2Wave Solution) — LinkedIn](https://es.linkedin.com/company/wave-2-wave-solution)
- [Wave2Wave / FiberSmart Crunchbase Profile](https://www.crunchbase.com/organization/wave2wave)
