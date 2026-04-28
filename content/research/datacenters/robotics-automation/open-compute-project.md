---
title: "Open Compute Project (OCP)"
date: 2026-03-24
lastmod: 2026-03-24
draft: false
description: "Nonprofit open hardware consortium founded by Meta in 2011. Develops and publishes open specifications for datacenter infrastructure including Open Rack v3 (ORV3) — the rack standard referenced by SoftBank's robot-friendly cable-less rack. OCP's ORV3 includes a vertical DC bus bar and blind-mate power connections that are foundational to automation-ready rack design. Members include Meta, Microsoft, Google, Goldman Sachs, and most major ODMs."
tags: ["datacenters", "robotics-automation", "standards", "design-construction", "blind-mate", "high-density"]
categories: ["consortium"]
research_area: "datacenters/robotics-automation"
source_urls:
  - "https://www.opencompute.org/"
  - "https://www.opencompute.org/documents/open-rack-base-specification-version-3-pdf"
last_reviewed: 2026-03-24
stale_after_days: 180
related:
  - "datacenters/robotics-automation/softbank-robot-rack.md"
  - "datacenters/robotics-automation/_index.md"
  - "datacenters/design-construction/_index.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

The Open Compute Project (OCP) is a nonprofit consortium founded by Meta (then Facebook) in 2011 to open-source the hardware designs that hyperscalers use in their own datacenters. Rather than each operator independently engineering racks, power distribution, cooling, and servers, OCP members share specifications and collaborate on reference designs that any manufacturer can build. OCP is not a formal standards body (it does not issue ISO/ANSI standards) but its specifications function as de facto standards across the hyperscale and large enterprise datacenter industry. Its **Open Rack v3 (ORV3)** specification is the most relevant output for datacenter robotics: ORV3 defines a rack that uses a vertical DC bus bar for power — eliminating traditional power cables — and blind-mate power connections as a core design feature. This is the specification that SoftBank cited when designing its robot-friendly cable-less server rack. OCP's **DC Automation** working group is developing specifications for automated datacenter operations. Understanding OCP is essential for understanding which rack and infrastructure designs will be robotics-compatible as the industry converges on shared standards.

## Key Facts

- **Founded:** 2011 by Meta (then Facebook)
- **Type:** 501(c)(6) nonprofit consortium; not a formal ISO/ANSI standards body
- **Structure:** Tiered membership (Startup, Silver, Gold, Platinum); member voting on governance
- **Founding context:** Meta published its first-generation open server and rack designs in 2011, initially for its Prineville, OR datacenter; invited industry partners to build on and contribute to the designs
- **Headquarters:** San Jose, CA
- **Key projects:** Open Rack (v1, v2, v3); Open Server / Project Olympus; Open Networking; Cooling (immersion, cold plate, rear-door heat exchanger); AI Infrastructure; DC Automation; Chiplets; Storage
- **ORV3 key features:** 21-inch rack width (vs. standard 19-inch EIA); vertical DC bus bar power distribution; blind-mate power connections; support for liquid cooling integration; 48V DC native power delivery
- **ORV3 certified vendors:** Rittal, Eaton, Sanmina, Cheval Group, Flex, WoodenDataCenter, Emcor — multiple qualified rack manufacturers
- **SoftBank relevance:** SoftBank's cable-less robot-friendly rack design references OCP ORV3 compliance; ORV3's bus bar power and blind-mate connectors are the technical foundation for cable-less rack automation

## What It Is / How It Works

OCP operates as a collaborative R&D consortium. Member organizations propose, develop, and publish hardware specifications as open documents. The process:

1. **Working group formation:** Members with shared interest in a technical area form a working group (e.g., "Cooling," "DC Automation," "Open Rack")
2. **Specification development:** Working group members collaboratively develop a technical specification, tested against real hardware
3. **Publication:** Specifications are published on opencompute.org as freely downloadable PDFs; anyone can build to them
4. **Marketplace:** OCP maintains an AI Marketplace listing products from members that meet OCP specifications — buyers can procure OCP-compliant hardware from multiple competing vendors

**Open Rack v3 (ORV3)** is the current generation rack specification and the most automation-relevant:

- **21-inch width (vs. 19-inch EIA standard):** The wider form factor provides more internal space for power distribution and cooling manifolds. ORV3 supports 19-inch EIA equipment inside the wider rack via adapters — maintaining backward compatibility while enabling new capabilities.
- **Vertical DC bus bar:** Power is distributed via vertical copper bus bars running the height of the rack, rather than individual power cables to each server. Servers tap into the bus bar via a blind-mate power connection when inserted. This is the same bus bar concept in SoftBank's cable-less rack — ORV3's bus bar predates and informed SoftBank's design.
- **48V DC native delivery:** ORV3 operates at 48V DC rather than the traditional 12V DC used in most servers. 48V reduces current (and thus cable losses and heat) for a given power level; Google, Meta, and other hyperscalers have shifted to 48V infrastructure. Mainstream server power supplies are beginning to support 48V natively (Open Rack Bus Bar power shelf is the interface point).
- **Blind-mate power connections:** ORV3 specifies that power connections between the bus bar power shelf and server units are blind-mate — they engage automatically on insertion without cable attachment. This is the key automation-enabling feature in the power domain.
- **Liquid cooling integration:** ORV3 includes provisions for in-rack manifolds that distribute cooling fluid to server cold plates — direct-to-chip cooling. Blind-mate fluid connections on servers are anticipated in the specification's direction.

**DC Automation working group:** OCP has a dedicated working group focused on automating datacenter operations — physical hardware installation, server lifecycle management, and facility monitoring. This group is where the industry is beginning to standardize the interfaces and protocols needed for robot-performed datacenter tasks. Active as of 2025; outputs not yet published as final specifications.

**OCP vs. traditional EIA:** Traditional enterprise datacenters use 19-inch EIA racks, 12V DC or 208V AC power, and individual power cables. OCP ORV3 differs in all three dimensions. The transition is predominantly in hyperscale and AI compute environments; enterprise and colocation facilities still mostly use EIA-standard infrastructure. This matters for understanding which facilities can adopt robot-friendly rack designs: OCP-native facilities (Meta, Google, SoftBank) have a much shorter path to cable-less automation than traditional enterprise datacenters.

## Notable Developments

- **2025:** OCP AI Marketplace formalized; ORV3-compliant product listings expand across power, cooling, and rack categories from multiple vendors
- **2024–2025:** DC Automation working group active; developing specifications for automated physical infrastructure management
- **2024:** ORV3 base specification Revision 1.0 published; multiple vendors begin producing certified ORV3 hardware (Rittal, Eaton, Sanmina, Flex, Cheval, WoodenDataCenter)
- **2025-09:** SoftBank references OCP ORV3 compliance in robot-friendly cable-less rack announcement — first public confirmation of OCP ORV3 as the technical foundation for a robot-serviced production rack design
- **2011:** Meta publishes first open server and datacenter designs; OCP formally incorporated

## Key People

OCP is a consortium, not a company. Key structural roles:

- **Founding organization:** Meta (Facebook); Mark Zuckerberg and the Meta infrastructure team initiated OCP; day-to-day leadership has always been professional staff, not Facebook executives
- **OCP Foundation:** Manages operations; Executive Director role exists but individual is not widely profiled in public coverage relevant to this research
- **Working Group Chairs:** Technical leadership is distributed across member companies; ORV3 working group leadership includes engineers from Meta, Microsoft, Intel, and ODMs

Tracking OCP working group chairs for the **DC Automation** group is recommended as this group's output will most directly shape the standards that govern robot-friendly datacenter infrastructure.

### People — Last Reviewed: 2026-03-24

## Supply Chain Position

OCP is a specification organization, not a manufacturer. Its position in the supply chain is upstream of every layer — it defines the rules that hardware manufacturers build to.

| OCP specification | Downstream manufacturers |
|-------------------|-------------------------|
| ORV3 rack frame | Rittal, Sanmina, Flex, Cheval Group, WoodenDataCenter, Emcor |
| ORV3 bus bar power shelf | Eaton, Vertiv (and others — multiple certified) |
| OCP cooling specifications | Submer, Asetek, CoolIT, nVent Schroff (various cooling products) |
| OCP server/AI accelerator specs | Wiwynn, Quanta, Foxconn, Supermicro (major ODMs) |

**Strategic significance:** Because OCP specifications are open and freely available, any manufacturer can build OCP-compliant hardware. This means:

1. **No single-source risk at the spec layer** — OCP ORV3 racks are available from multiple certified vendors
2. **De facto standardization enables automation** — once SoftBank or others demonstrate robot-serviced ORV3 racks at Tomakomai, robot arm manufacturers and software vendors have a stable specification to target; this accelerates the ecosystem vs. proprietary rack designs
3. **Adoption barrier** — legacy EIA-standard datacenters cannot simply install ORV3-compliant hardware; facility renovation or new-build is required; this limits near-term robot-friendly rack adoption to greenfield AI datacenter builds

**⚑ OCP ORV3 as the converging robot-rack standard:** SoftBank's explicit claim of ORV3 compliance turns OCP into a key leverage point. If ORV3 becomes the industry standard for AI datacenter racks (which is directionally happening), it automatically becomes the standard for robot-serviceable racks — OCP's bus bar and blind-mate power are already there; SENKO-style optical and fluid blind-mate connectors are the next additions. Watch OCP's DC Automation working group outputs and any ORV3 revision that adds optical and fluid connector specifications.

## Claim Verification

### Claim: ORV3 is "the" standard for AI datacenter racks / robot-friendly racks
**Status:** Directionally accurate but contested; EIA-standard racks still dominate globally

**Supporting:**
- All major hyperscalers (Meta, Google, Microsoft) have adopted OCP-derived designs for new AI compute builds
- SoftBank's robot-friendly rack specifically cites ORV3 — validating it as the target specification for automation-ready racks
- Multiple certified ORV3 hardware vendors exist, creating a competitive ecosystem

**Refuting / questioning:**
- Traditional enterprise and colocation datacenters predominantly use 19-inch EIA racks; OCP is still hyperscale-specific outside AI builds
- NVIDIA's GPU infrastructure specifications are not always OCP-native; HGX-based systems sometimes ship in EIA-compatible form factors with modifications
- Some hyperscalers (Amazon AWS) have developed their own proprietary rack designs rather than pure OCP; OCP is influential but not universally adopted even among hyperscalers

**Summary:** OCP ORV3 is the leading open specification for the infrastructure layer where robot-friendly racks are being built. For greenfield AI datacenter construction, it is the correct reference standard. For existing facilities, EIA-standard racks will persist for years.

## Sources

- [Open Compute Project — opencompute.org](https://www.opencompute.org/)
- [Open Rack v3 Base Specification Revision 1.0 — OCP (PDF)](https://www.opencompute.org/documents/open-rack-base-specification-version-3-pdf)
- [OCP's Past, Present, and Future of Open Rack (ORV3) — OCP](https://www.opencompute.org/products/713/ocps-past-present-and-future-of-open-rack-orv3)
- [Rittal Open Rack V3 (ORV3) — OCP Marketplace](https://www.opencompute.org/products/440/rittal-open-rack-v3-orv3)
- [SoftBank Develops Robot-Friendly Server Rack — SoftBank News (Sep 2025)](https://www.softbank.jp/en/sbnews/entry/20250917_01)
