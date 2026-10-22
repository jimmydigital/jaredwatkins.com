---
title: "SoftBank Robot-Friendly Cable-Less Server Rack"
date: 2026-03-24
lastmod: 2026-10-20
draft: false
description: "SoftBank Corp.'s cable-less, robot-friendly server rack (announced September 2025): bus-bar power, blind-mate optical and liquid-cooling connectors, OCP ORV3-based; to be tested at the Hokkaido Tomakomai AI Data Center, which DCD says opens in 2027 at an initial 50 MW."
research_area: "datacenters/robotics-automation"
source_urls:
  - "https://www.softbank.jp/en/sbnews/entry/20250917_01"
  - "https://www.softbank.jp/en/sbnews/entry/20251215_01"
  - "https://www.datacenterdynamics.com/en/news/softbank-develops-cableless-server-rack-for-data-center-robots/"
  - "https://www.senko.com/senkos-newly-developed-blind-mate-connectivity-powers-softbanks-robot-friendly-server-rack-for-next-generation/"
  - "https://www.eenewseurope.com/en/softbank-taps-zutacore-foxconn-for-robot-ai-datacentre-first/"
  - "https://tech-insider.org/softbank-roze-ai-100-billion-ipo-data-center-robotics-2026/"
last_reviewed: 2026-10-20
stale_after_days: 90
related:
  - "datacenters/robotics-automation/senko.md"
  - "datacenters/robotics-automation/submer-ada.md"
  - "datacenters/cooling/_index.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

SoftBank Corp. announced its "robot-friendly" cable-less server rack in September 2025 — a concrete realization to date of the infrastructure-first automation philosophy for datacenters. The design eliminates all traditional cable connections from the server-to-rack interface: power, networking, and liquid cooling are all delivered through blind-mate connectors that self-align and engage automatically when a server is pushed into position. A robot can install or replace a server with a single push/pull motion, with no cable manipulation required. The rack conforms to OCP ORV3 specifications and accommodates standard 19-inch servers. Real-world testing was planned at SoftBank facilities in late 2025; deployment at the Hokkaido Tomakomai AI Data Center is planned for FY2026 (fiscal year ending March 2027). SENKO Advanced Components supplies the blind-mate optical connectors — see [SENKO Advanced Components]({{< relref "senko.md" >}}).

## Key Facts

- **Announced:** September 17, 2025
- **Operator:** SoftBank Corp. (Tokyo: 9434)
- **Design goal:** Enable robots to install and replace servers without cable handling steps
- **Standard compliance:** OCP ORV3 (Open Compute Project Open Rack v3); 19-inch server compatible
- **Connector types:** Three simultaneous blind-mate connection systems:
  1. **Power:** Metal bus bar clips — server slides onto a rear bus bar for power delivery, no power cable
  2. **Networking:** Blind-mate optical connector (SENKO states its connectors are used) — optical signals, no data cables
  3. **Liquid cooling:** Blind-mate quick-connect fluid couplings — water cooling connection on insertion
- **Deployment target:** Hokkaido Tomakomai AI Data Center, under construction; DCD reports an initial 50 MW and a 2027 opening, while SENKO's release says fiscal 2026 (sources differ)
- **Robot integration:** Pairs with a container robot (CTU) and lifter robot using QR-code recognition and laser positioning; automated guided forklifts anticipated
- **Validation status:** SoftBank said in December 2025 that testing at Tomakomai would run "over the next couple of months" and that it plans to standardize the design for its other data centers; no results were found as of October 2026

## What It Is / How It Works

Traditional server racks require a technician to physically attach several cables when installing a server: a power cable (typically IEC C13/C19), one or more data network cables (RJ45 or fiber), and — in liquid-cooled racks — cooling hoses. These steps are straightforward for trained humans but extremely difficult for robot arms, which lack the dexterity and tactile feedback needed to route and seat cables reliably at speed.

SoftBank's cable-less rack solves this by moving all connections to the rear of the rack in a single integrated adapter plane that engages automatically on insertion. The three systems work as follows:

**Bus bar power:** A set of metal conducting bars runs vertically along the rear of the rack at fixed positions. The server's power inlet is replaced with a spring-loaded clip that contacts the bus bar as the server slides home. This eliminates the IEC power connector entirely. Bus bar power distribution is not new (it is used in blade server enclosures and some OCP designs), but integrating it into a standard-format rack that also handles optical and liquid cooling in one insert motion is novel.

**SENKO blind-mate optical connectors:** Networking is handled by optical connectors that use guide pins and tapered alignment features to self-center when the server is inserted. SENKO's design provides insertion force feedback and alignment tolerance to accommodate the positioning accuracy of robot arms. Standard MPO/MTP fiber connectors require line-of-sight alignment that is impractical for robots; SENKO's connectors tolerate angular and lateral misalignment. Optical transceivers are built into the rear of the server rather than using external cables.

**Blind-mate liquid cooling:** A manifold at the rear of the rack connects to a building water loop. The server has a rear-mounted cooling inlet/outlet plate. Proprietary quick-connect couplings (details not publicly disclosed) seal on insertion and disconnect cleanly on extraction, with minimal fluid spillage. This enables liquid cooling of high-density AI servers without any hose-connection steps.

The result is a rack where a robot only needs to perform a single push motion (aligning a server with the rack slot and pushing it home until the bus bar, optical, and cooling connectors engage) to bring a server online. Extraction is the reverse — a pull motion that disconnects all three systems simultaneously.

## Notable Developments

- **2026-04-29 (reported):** The Financial Times reports SoftBank Group plans a US-listed robotics spin-off, Roze AI, targeting a roughly $100B IPO valuation as soon as the second half of 2026 (possibly 2027), to automate data center construction with autonomous robots (cabinet installation, cable routing, busway assembly). SoftBank declined to comment; no robot shipped or data center completed. This concerns construction, not the rack. ([Tech Insider summary](https://tech-insider.org/softbank-roze-ai-100-billion-ipo-data-center-robotics-2026/))
- **2026 (to October):** No Tomakomai test results, rack standardization or deployment announcement was found.
- **2025-12-15:** SoftBank feature: rack to be tested at Tomakomai over the next couple of months for reliability, connection stability, fleet management and interface compatibility, then standardized for rollout; safety features include LiDAR and emergency stops. ([SoftBank News](https://www.softbank.jp/en/sbnews/entry/20251215_01))
- **2025-12-01:** SENKO announces its blind-mate optical connectivity powers the rack. ([SENKO](https://www.senko.com/senkos-newly-developed-blind-mate-connectivity-powers-softbanks-robot-friendly-server-rack-for-next-generation/))
- **2025-02 (demo; reported 2025-02-28):** SoftBank, ZutaCore and Foxconn demonstrate a robot-friendly, ORV3-based rack with two-phase direct liquid cooling and Foxconn H200 servers at a SoftBank data center; measured partial PUE 1.03; Blackwell version planned. ([eeNews Europe](https://www.eenewseurope.com/en/softbank-taps-zutacore-foxconn-for-robot-ai-datacentre-first/))
- **2025-09-17:** SoftBank Corp. announces the robot-friendly cable-less server rack; DCD (2025-09-29) names no partners and notes the design may not be fully cableless. ([SoftBank News](https://www.softbank.jp/en/sbnews/entry/20250917_01))
- **2025-05-01:** Construction begins at the Hokkaido Tomakomai AI Data Center; the robot-friendly rack is planned for it. ([SoftBank News](https://www.softbank.jp/en/sbnews/entry/20250501_01))

## Key People

No individual engineers or executives specifically associated with the rack design program have been named in public disclosures. SoftBank Corp. CEO Junichi Miyakawa has discussed the company's AI datacenter investment strategy broadly. The rack development appears to have been conducted by SoftBank's internal technology and datacenter engineering teams.

### People — Last Reviewed: 2026-10-20

## Supply Chain Position

This design sits at the **Rack & Connectivity Infrastructure** layer. Key upstream dependencies:

| Component | Supplier | Risk |
|-----------|----------|------|
| Blind-mate optical connectors | [SENKO Advanced Components]({{< relref "senko.md" >}}) | Specialist supplier; limited alternatives at this specification |
| Bus bar power components | Not disclosed | Unknown |
| Liquid cooling blind-mate couplings | Not publicly disclosed | Unknown |
| Rack chassis and structure | OCP ORV3-compliant fabricators | Commodity; multiple suppliers |
| Liquid cooling infrastructure | SoftBank facility water loop (vendor not disclosed) | Standard datacenter infrastructure |

SoftBank's rack design is currently proprietary (it follows OCP ORV3 with proprietary additions). If it were adopted into open standards, the component ecosystem would expand significantly as other manufacturers develop compatible alternatives to SENKO's connectors and the unnamed bus bar and coupling suppliers.

**⚑ Strategic chokepoint — SENKO connector:** SENKO is the only named component supplier and the most technically differentiated element. SENKO states it is a partner for the rack; whether it is the sole supplier is not stated. See [SENKO Advanced Components]({{< relref "senko.md" >}}).

## Claim Verification

### Claim: Robot can install/replace a server "simply by pushing it into place"
**Status:** Plausible; not independently verified at production scale

**Supporting:**
- SoftBank's own technical description and videos demonstrate the concept
- The three blind-mate systems (bus bar, optical, liquid) are each individually proven in adjacent applications; the innovation is combining all three in one motion
- OCP ORV3 compliance indicates the design has been reviewed against a public standard

**Refuting / questioning:**
- As of late 2025 the rack is in real-world testing, not yet deployed at scale in an operational AI datacenter
- The reliability of blind-mate optical connectors under thousands of robot-insertion cycles is unproven in production; SENKO has not published cycle-life validation data
- Full automation of server servicing requires more than rack design — robot arm precision, computer vision, fleet coordination, and DCIM integration are separate unsolved problems

**Summary:** The concept is technically sound and the components are individually proven. The "simply push" claim is accurate for the mechanical connection step but understates the full automation challenge. Real-world validation at Tomakomai will be the first meaningful test at AI datacenter scale.

### Claim: OCP ORV3 compliance
**Status:** Stated by SoftBank; OCP ORV3 is a published specification that can be independently verified against

**Summary:** OCP ORV3 is a public specification. SoftBank's stated compliance implies the rack dimensions, power bus, and server form factor are interoperable with other ORV3-compliant equipment. This is verifiable but has not been independently confirmed in published OCP documentation as of this writing.

## Sources

- [SoftBank taps ZutaCore, Foxconn for robot AI datacentre first — eeNews Europe (Feb 2025)](https://www.eenewseurope.com/en/softbank-taps-zutacore-foxconn-for-robot-ai-datacentre-first/)
- [SoftBank's $100B Roze IPO — Tech Insider (Apr 2026)](https://tech-insider.org/softbank-roze-ai-100-billion-ipo-data-center-robotics-2026/)
- [SoftBank Develops "Robot-friendly" Server Rack — SoftBank News (Sep 2025)](https://www.softbank.jp/en/sbnews/entry/20250917_01)
- [Inside Look: How SoftBank is Creating Robot-Friendly Environments at Data Centers — SoftBank News (Dec 2025)](https://www.softbank.jp/en/sbnews/entry/20251215_01)
- [SoftBank Develops Cableless Server Rack for Data Center Robots — Data Center Dynamics](https://www.datacenterdynamics.com/en/news/softbank-develops-cableless-server-rack-for-data-center-robots/)
- [SENKO's Blind-Mate Connectivity Powers SoftBank's Robot Friendly Server Rack — SENKO (Dec 2025)](https://www.senko.com/senkos-newly-developed-blind-mate-connectivity-powers-softbanks-robot-friendly-server-rack-for-next-generation/)
- [Construction Begins at Hokkaido Tomakomai AI Data Center — SoftBank News (May 2025)](https://www.softbank.jp/en/sbnews/entry/20250501_01)
