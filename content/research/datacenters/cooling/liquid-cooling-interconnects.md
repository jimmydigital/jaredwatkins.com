---
title: "Liquid Cooling Interconnects: Connector Types and Standards"
date: 2026-06-07
lastmod: 2026-06-07
draft: false
description: "Survey of the connector families, standards bodies, and form factors used at both the rack and server level in liquid-cooled AI and HPC datacenters — and why their proliferation is creating supply chain and interoperability problems."
tags: ["liquid-cooling", "direct-to-chip", "blind-mate", "cooling", "datacenters", "high-density", "ai-datacenter"]
categories: ["technology"]
research_area: "datacenters/cooling"
source_urls:
  - "https://www.opencompute.org/documents/open-rack-v3-blind-mate-manifold-specification-rev-1-0-review-april05-2024-pdf"
  - "https://www.opencompute.org/documents/ocp-large-quick-connector-specification-052223-pdf"
  - "https://www.connectortips.com/what-is-the-role-of-liquid-cooling-connectors-in-ai-data-centers/"
  - "https://insidehpc.com/2025/09/cpc-and-the-critical-role-of-the-connector-in-the-liquid-cooled-ai-data-center/"
  - "https://amphenol-industrial.com/ocp-compliant-liquid-cooling-quick-disconnects/"
  - "https://www.danfoss.com/en/about-danfoss/news/dps/new-blind-mate-quick-connector-from-danfoss-power-solutions-simplifies-chassis-to-manifold-connections-in-data-center-liquid-cooling-applications/"
  - "https://www.staubli.com/global/en/fluid-connectors/products/quick-and-dry-disconnect-couplings/thermal-management/uqd-universal-quick-disconnect.html"
  - "https://rapidaccu.com/liquid-cooling-connectors/"
  - "https://www.sciencedirect.com/science/article/abs/pii/S0360132326002465"
  - "https://tonecooling.com/nvidia-gb200-nvl72-cooling-requirements/"
last_reviewed: 2026-06-07
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

As datacenters shift from air to liquid cooling to support GPU rack densities exceeding 100 kW, the physical connectors that join cold plates to manifolds, manifolds to CDUs, and CDUs to the facility water loop have proliferated into an incompatible zoo of proprietary and semi-standard form factors. Unlike electrical interconnects — where USB, PCIe, and Ethernet achieved global convergence — liquid cooling connectors still lack a single unified standard. Multiple OCP specifications, vendor-proprietary families, and cross-industry standards borrowed from automotive and industrial applications coexist in the same rack deployments, creating interoperability headaches, inventory fragmentation, and supply chain concentration risk.

## Key Facts

- **Type:** Technology / standard — connector hardware and specifications
- **Status:** Active, rapidly evolving
- **Key standards bodies:** Open Compute Project (OCP), ASHRAE, JEDEC (water quality only)
- **Primary deployment context:** Direct-to-chip (cold plate) cooling in AI/HPC racks; also applicable to immersion cooling distribution loops
- **Market:** UQD coupling segment valued ~$95M in 2024; projected to reach $2.6B by 2031 (46% CAGR) per Valuates Reports

## What It Is / How It Works

### The Connector Problem in Liquid-Cooled Racks

A direct-to-chip liquid cooling system contains three distinct fluid loops, each with its own connector requirements:

**Loop 1 — Facility water loop:** Large-bore piping connecting the building's chilled water plant or cooling tower to the Coolant Distribution Units (CDUs). Connection frequency is extremely low (once at installation); connectors here prioritize sealing integrity and flow capacity over quick serviceability. Typical: large threaded fittings, flanged connections, or large ball-valve couplings. Not a connector diversity problem.

**Loop 2 — CDU-to-rack manifold loop:** The CDU pumps conditioned coolant (typically 30–45°C water-glycol, per ASHRAE W55) to each rack via a supply/return manifold. Connection frequency is low-to-moderate — on the order of rack additions and decommissions. Connectors here must handle higher pressure (up to 6 bar operating per NVIDIA GB200 NVL72 spec) and support rack-level hot swap in some designs. The OCP Large Quick Connector (LQC) targets this layer with a screw-to-connect design, ≥100 LPM flow, max 12 bar burst, and ≤0.15 mL fluid loss per disconnect.

**Loop 3 — In-rack server-to-manifold loop:** Short flexible hose assemblies connecting individual server cold plates to the rack's internal manifold. This is the highest-frequency connection point — every server swap or board replacement touches these connectors. Connectors must be small (to fit dense server trays), quick (to enable serviceability), and spillage-free (fluid on electronics is catastrophic). This is where connector diversity is most acute and most operationally consequential.

### The OCP Standard Families

The Open Compute Project has produced several connector specifications, but they address different points in the system and are not mutually interchangeable:

**UQD (Universal Quick Disconnect):** The foundational OCP server-level coupling, defined as a push-to-connect, pull-to-release design with a standardized interface geometry. Versions available in multiple nominal flow sizes (UQD02 through UQD06, approximately 1/8" to 3/8" flow path). Designed for manual connection at the server-to-manifold interface. Stäubli originated the UQD architecture and has ~30 years of liquid cooling history; multiple vendors now produce OCP-compliant UQD connectors. The UQD04 size (1/4" flow path) became the de facto standard for 1U/2U server cold plates in Gen-4 and Gen-5 GPU platforms.

**UQDB (Universal Quick Disconnect, Blind-Mate):** A blind-mate variant of the UQD that aligns and connects automatically as a server tray slides into a rack. Designed for high-density GPU sleds (NVIDIA NVL72 and similar) where manual connection in a 1U server bay is mechanically impractical. Tolerates ±5 mm radial and ±2.7° angular misalignment to absorb rack mounting tolerances. Stäubli and Danfoss both produce UQDB Series products; Rev 2.0 added cross-vendor hybrid mating (UQD plug to UQDB socket).

**BMQC (Blind-Mate Quick Connector):** Defined specifically for the OCP Open Rack V3 (ORv3) rack architecture — the blind-mate interface between the server sled and the rack-integrated manifold. The ORv3 Blind Mate Manifold Specification (Rev 1.0, April 2024) defines the mechanical envelope, misalignment tolerances (same ±5 mm / ±2.7°), flow requirements, and coding options to prevent cross-connection. Parker Hannifin, Danfoss, and others produce ORv3-compliant BMQC connectors. Importantly, BMQC at the ORv3 interface is specified as interchangeable across compliant vendors — the one layer where cross-vendor interoperability is strongest.

**LQC (Large Quick Connector):** A screw-to-connect, higher-flow coupling targeting the CDU-to-manifold trunk connection. 20 mm nominal flow path, designed for the higher pressure and flow rates on the facility side of the loop. Not a blind-mate design; intended for less-frequent connection by a technician.

**MQD (Mini Quick Disconnect):** A compact variant for tightly packaged server trays and blade systems where the UQD04 is too large. Used in high-density blade designs and where the server manufacturer has minimized the server-side connector footprint.

### Non-OCP Connector Families in Active Use

OCP specifications cover ORv3-format racks deployed by hyperscalers building to that standard. A large fraction of AI datacenter hardware is not ORv3-format, generating demand for non-OCP connector families:

**Proprietary OEM designs:** NVIDIA's GB200 NVL72 rack publishes manifold flow requirements (CDU output ≥750–800 LPM, manifold pressure drop 1.5–2.5 bar, cold plate burst pressure ≥12 bar) but does not mandate a specific connector for the cold-plate-to-manifold interface. Individual OEMs (Supermicro, Dell, HPE, Foxconn) implement their own cold plate assemblies with their own connector choices. The result: a Supermicro GB200 tray uses different connectors from an HPE GB200 tray even though the underlying GPU is identical.

**CPC Everis Series:** CPC (Colder Products Company, a Dover subsidiary) offers its Everis UQD/UQDB/BLQ blind-mate family, OCP-compliant in the UQD geometry but manufactured by CPC. The Everis BLQ6 (3/8" flow path) was specifically developed for exascale supercomputer deployments where no off-the-shelf connector met the combined flow/form-factor requirements. The BLQ series is widely deployed in US national laboratory HPC clusters.

**VDA Connectors (automotive origin):** The VDA quick connector standard, developed for automotive engine and battery cooling circuits, has been adapted for server cooling in some non-hyperscaler deployments, particularly in European systems integrators. VDA connectors are push-to-connect, available in multiple sizes, and widely manufactured in China and Europe. They are NOT cross-compatible with OCP UQD geometry despite serving a similar functional role.

**Industrial / hydraulic fittings:** Legacy installations and some edge compute deployments use standard industrial quick-connect fittings (Parker, Eaton, Stäubli RBE/RBI series) originally designed for industrial hydraulics or pneumatics. These are generally too large, too high-pressure-rated, or too service-unfriendly for dense server environments but appear in first-generation installations and DIY direct-liquid-cooling retrofits.

### Why So Many Standards?

The proliferation has structural causes:

1. **Speed of GPU power density escalation:** From NVIDIA A100 (300–400W) to H100 (700W) to GB200 (1200W+ per module) happened in three product generations, forcing cooling connector redesigns before any single standard could consolidate. Each generation brought larger required flow rates, pushing the UQD04 to its limits and driving the UQD06 introduction.

2. **Market incumbency vs. OCP timing:** OCP began producing liquid cooling connector specs only in 2022–2024. Before those specs existed, OEMs and HPC system builders had already chosen connectors from whoever had appropriate products — CPC, Stäubli, Parker, or off-catalog Chinese manufacturers. Those choices are locked into existing infrastructure.

3. **Different mechanical constraints at different rack scales:** A 1U server tray, a 4U sled, and an ORv3 rack sled have fundamentally different space envelopes and insertion vectors. No single connector geometry serves all three use cases optimally. The UQD/UQDB/BMQC family is an attempt to define a minimal set of three, but OEM customization continually produces variants.

4. **Proprietary CDU interfaces:** CDU manufacturers (Vertiv, nVent, LiquidStack, CoolIT, Motivair) have their own preferred manifold connector choices on the facility side of the CDU heat exchanger. These are customer-facing and subject to lock-in.

5. **Cross-industry borrowing:** Automotive (VDA), industrial (Parker, Eaton), and semiconductor equipment markets use liquid cooling connectors at scale. When datacenters ramped liquid cooling demand in 2022–2023, those established supply chains were the fastest path to components — even if the form factors weren't ideal for datacenter use.

### Operational Consequences

A ScienceDirect study of a supercomputing center's liquid cooling infrastructure (published March 2026) documented the real-world cost of this fragmentation: the facility employed multiple incompatible connector protocols across clusters installed in different years, leading to expanded spare parts inventories, extended mean-time-to-repair (the technician must identify the connector type before selecting the replacement), and increased risk of mis-mating (connecting a plug and socket from different families that physically fit but leak under pressure). The study called for a single cross-platform fluid connector standard as an industry priority.

Hyperscale operators with procurement leverage (Google, Microsoft, Meta) are driving ORv3 BMQC adoption through their OEM RFPs as a condition of supply, which is gradually standardizing the newest deployments. Older installations, colocation customers, and non-hyperscale enterprise buyers remain on a fragmented landscape indefinitely.

## Notable Developments

- **2026-03:** ScienceDirect published study documenting real-world incompatibility costs in supercomputing liquid cooling deployments; called for unified standard specification.
- **2026-01:** Schneider Electric published liquid cooling reference designs for AI datacenters specifying preferred connector interfaces for CDU-to-rack connections.
- **2025-10:** Schneider Electric reported 60% organic orders growth and 1.4× book-to-bill for liquid cooling infrastructure, indicating supply-constrained demand through 2025.
- **2025-09:** CPC announced Everis UQDB06 and UQD06 (3/8" flow path), expanding the UQD family to handle higher flow rates required by GB200-class AI workloads.
- **2025-07:** CPC released Everis UQDB06/UQD06 Connector Set, driven by demand from hyperscale AI datacenter deployments.
- **2024-04:** OCP published Open Rack V3 Blind Mate Manifold Specification Rev 1.0, the most detailed standardization of the server-to-rack interface to date.
- **2024-02:** Danfoss introduced ORv3-compliant UQD couplings with 25% higher flow rate than prior industry standard.
- **2024-01:** NVIDIA contributed GB200 NVL72 rack design specifications to OCP, anchoring ORv3 BMQC as the target standard for Blackwell-generation clusters.

## Key Organizations

- **Open Compute Project (OCP):** Publishes the UQD, UQDB, BMQC, LQC specifications; Rack and Power subproject group maintains liquid cooling connector standards. Major contributors: Meta, Microsoft, Google, Intel, AMD.
- **NVIDIA:** GB200 NVL72 and NVLink rack architectures set de facto flow and pressure requirements that downstream connector manufacturers must meet, regardless of OCP conformance.
- **ASHRAE:** W55 water quality standard defines the coolant chemistry that all datacenter liquid cooling connector materials must be compatible with.

## Sources

- [OCP ORv3 Blind Mate Manifold Specification Rev 1.0](https://www.opencompute.org/documents/open-rack-v3-blind-mate-manifold-specification-rev-1-0-review-april05-2024-pdf) — April 2024 release; defines BMQC geometry, tolerances, flow requirements
- [OCP Large Quick Connector Specification](https://www.opencompute.org/documents/ocp-large-quick-connector-specification-052223-pdf) — facility-side LQC spec, ≥100 LPM, ≤0.15 mL loss per disconnect
- [CPC: Critical Role of the Connector in Liquid-Cooled AI Data Center](https://insidehpc.com/2025/09/cpc-and-the-critical-role-of-the-connector-in-the-liquid-cooled-ai-data-center/) — InsideHPC, Sept 2025; CPC exascale supercomputer case study
- [What is the role of liquid cooling connectors in AI data centers?](https://www.connectortips.com/what-is-the-role-of-liquid-cooling-connectors-in-ai-data-centers/) — ConnectorTips, Feb 2025; design requirements survey
- [Amphenol OCP-Compliant Liquid Cooling Quick Disconnects](https://amphenol-industrial.com/ocp-compliant-liquid-cooling-quick-disconnects/) — product family overview; UQD, UQDB, BMQC, LQC, MQD comparison
- [Danfoss BMQC announcement](https://www.danfoss.com/en/about-danfoss/news/dps/new-blind-mate-quick-connector-from-danfoss-power-solutions-simplifies-chassis-to-manifold-connections-in-data-center-liquid-cooling-applications/) — ORv3 BMQC specifications
- [Stäubli UQD/UQDB](https://www.staubli.com/global/en/fluid-connectors/products/quick-and-dry-disconnect-couplings/thermal-management/uqd-universal-quick-disconnect.html) — originator of UQD architecture; 30+ years liquid cooling history
- [NVIDIA GB200 NVL72 Cooling Requirements](https://tonecooling.com/nvidia-gb200-nvl72-cooling-requirements/) — manifold pressure, flow, and burst requirements
- [Novel Compatible Fluid Connector for Liquid Cooling (ScienceDirect, 2026)](https://www.sciencedirect.com/science/article/abs/pii/S0360132326002465) — March 2026; documents supercomputing center multi-protocol incompatibility
- [Revolutionizing Data Center Cooling: Rise of UQD Couplings](https://www.intelmarketresearch.com/blog/60/universal-quick-disconnect-coupling-for-liquid-cooling-market) — market sizing, CAGR, top vendor share
