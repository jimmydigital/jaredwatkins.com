---
title: "Submer Technologies"
date: 2026-03-24
lastmod: 2026-03-24
draft: false
description: "Barcelona-based single-phase immersion cooling specialist; $500M valuation at October 2024 Series C ($55.5M); SmartCoolant proprietary biodegradable dielectric fluid; customers include at least one hyperscaler, Telefónica, ExxonMobil, and the European Commission. Also developing ADA robotic assistant for autonomous tank servicing."
tags: ["datacenters", "cooling", "immersion-cooling", "spain", "startup"]
categories: ["company"]
research_area: "datacenters/cooling"
source_urls:
  - "https://submer.com/about-us/"
  - "https://techcrunch.com/2024/10/02/as-data-center-usage-heats-up-submer-raises-55-5m-to-cool-things-down/"
  - "https://www.datacenterdynamics.com/en/news/immersion-cooling-firm-submer-to-release-autonomous-robot/"
last_reviewed: 2026-03-24
stale_after_days: 90
related:
  - "datacenters/robotics-automation/submer-ada.md"
  - "datacenters/cooling/_index.md"
---

## Summary

Submer Technologies is a Barcelona, Spain-based single-phase immersion cooling company founded in 2015 by Daniel Pope and Pol Valls Soler. It is one of the leading independent pure-plays in liquid immersion cooling for datacenters — a market that has moved from niche to mainstream as AI accelerator rack densities exceed what air cooling can handle. Submer's core products are its SmartPod immersion tanks and SmartCoolant proprietary dielectric fluid. The company raised $55.5M in Series C funding in October 2024 at a $500M valuation, led by M&G Investments. Its customer base includes at least one unnamed hyperscaler, Telefónica, ExxonMobil, and the European Commission. Submer is also developing ADA, an autonomous robot designed to insert and remove servers from immersion tanks — see [Submer ADA]({{< relref "/research/datacenters/robotics-automation/submer-ada.md" >}}).

## Key Facts

- **Founded:** 2015
- **HQ:** Barcelona, Spain
- **Type:** Private
- **CEO:** Patrick Smets (joined as COO August 2023; became CEO January 2024)
- **Co-Founders:** Daniel Pope and Pol Valls Soler
- **Total funding:** ~$110M across 7+ rounds (Series C $55.5M Oct 2024 + $20.9M debt Dec 2024)
- **Valuation:** ~$500M (at Series C, October 2024)
- **Series C lead:** M&G Investments; participants include Mundi Ventures, Planet First Partners, Norrsken VC
- **Core products:** SmartPod (single-phase immersion tank), SmartCoolant (proprietary dielectric fluid), SmartMod (prefabricated modular datacenter unit incorporating SmartPod)
- **Coolant:** SmartCoolant — proprietary synthetic, biodegradable, non-flammable, non-toxic, water-viscosity, non-ozone-depleting; designed for long service life between changes
- **PUE range (design):** 1.02–1.03 (immersion cooling nearly eliminates mechanical cooling overhead)
- **Supported rack density:** Up to 200+ kW per tank (AI GPU configurations)
- **Robotics program:** ADA (Autonomous Datacenter Assistant) — vertical-lift robot for immersion tank servicing; revealed OCP Summit 2021, commercial target ~Q3 2025
- **Key customers (disclosed):** At least one unnamed hyperscaler; Telefónica; ExxonMobil; European Commission; major HPC research centers
- **OCP alignment:** Active participant in Open Compute Project; SmartPod design has OCP lineage

## What It Is / How It Works

Submer's SmartPod is a single-phase immersion cooling system. "Single-phase" means the dielectric fluid remains liquid throughout the heat exchange process — it absorbs heat from servers and is pumped to a heat exchanger (chiller, dry cooler, or facility water loop) where it releases heat before recirculating. This contrasts with two-phase immersion (e.g., LiquidStack), where the fluid boils and condenses — which achieves higher heat transfer coefficients but is more complex to manage and historically used fluorocarbon fluids with supply concerns (3M Novec line discontinued, though alternatives exist from Solvay and others).

**SmartCoolant** is Submer's proprietary fluid and is the core product differentiation. Its key attributes:

- **Biodegradable:** Derived from a synthetic blend designed to break down in the environment; addresses regulatory and ESG requirements
- **Non-toxic, non-flammable:** Safe handling without hazmat protocols
- **Water viscosity:** Server pumps and fans are designed for air or water; SmartCoolant's similar viscosity to water means it doesn't stress server components (though fans are typically disabled in immersion deployments)
- **Long change interval:** Designed to remain stable for multi-year service intervals without degradation; reduces operational cost vs. frequent fluid changes

**SmartPod** tanks accommodate industry-standard servers (including OCP-format hardware) in a horizontal submersion configuration. The tank connects to a heat exchanger — at minimum a plate heat exchanger to building chilled water, or alternatively coupled to dry coolers, free cooling, or even heat recovery systems. Submer's SmartMod product packages tanks, piping, power distribution, and monitoring into a prefabricated module for faster deployment.

The practical PUE of 1.02–1.03 in immersion systems comes from eliminating CRAC units, raised floors, and hot/cold aisle infrastructure. The only cooling-related power draw is the fluid pump, which is minimal. This compares to 1.3–1.5 PUE for well-designed air-cooled facilities and 1.1–1.2 PUE for direct-to-chip liquid cooling.

**Operational friction:** The tradeoff is servicing complexity. Servers submerged in fluid cannot be hot-swapped like rack-mounted units. Lifting a server from a tank requires PPE (dielectric fluid must be kept off skin and out of drains), vertical lift equipment, and fluid drip management. This is why Submer is developing ADA — without robotic assistance, immersion cooling scales better in density than in operational agility.

## Notable Developments

- **2024-12:** Submer raises $20.9M in conventional debt financing — additional capital beyond Series C. ([Tracxn](https://tracxn.com/d/companies/submer/__NjMhg1nIBsRsqjjhdeV4ghzWPXBew9KZEmoBrlrb8nI))
- **2024-10:** Series C — $55.5M at $500M valuation; led by M&G Investments. Proceeds directed toward scaling manufacturing, expanding North America and Asia operations, and accelerating ADA robotics development. ([TechCrunch](https://techcrunch.com/2024/10/02/as-data-center-usage-heats-up-submer-raises-55-5m-to-cool-things-down/))
- **2024-01:** Patrick Smets promoted to CEO; co-founders Pope and Valls Soler shift to product/strategy roles.
- **2023-08:** Patrick Smets joins as COO (first C-suite hire from outside founding team).
- **2021-10:** ADA robotic assistant unveiled at OCP Global Summit 21. ([Submer Labs / X](https://x.com/submertech/status/1458404816095428617))
- **2015:** Founded in Barcelona by Daniel Pope and Pol Valls Soler.

## Key People

### Patrick Smets — CEO (since January 2024)
- **LinkedIn:** [linkedin.com/in/patricksmets](https://www.linkedin.com/in/patricksmets/) *(confirm; not independently verified in this review)*
- **Role:** CEO since January 2024; joined as COO August 2023
- **Background:** Operations and scaling executive; recruited to bring operational discipline as Submer transitioned from early-stage startup to growth-stage company; not one of the technical founders
- **Notes:** First externally recruited CEO; co-founders remain involved

### Daniel Pope — Co-Founder
- **LinkedIn:** [linkedin.com/in/danielpope](https://www.linkedin.com/in/danielpope/) *(confirm; common name, verify carefully)*
- **Role:** Co-founder; early CEO/Chief Visionary; current role title not confirmed post-Smets appointment
- **Background:** Entrepreneur and datacenter sustainability advocate; co-created Submer's vision of "datacenters that make sense" — combining efficiency, sustainability, and high density

### Pol Valls Soler — Co-Founder
- **LinkedIn:** Not confirmed; search for "Pol Valls Soler Submer" on LinkedIn
- **Role:** Co-founder; technical and product leadership alongside Pope in founding years
- **Background:** Engineering background; involved in SmartCoolant chemistry and SmartPod product development

### People — Last Reviewed: 2026-03-24

## Supply Chain Position

Submer sits at the **Immersion Cooling System** layer of the datacenter supply chain — designing tanks and fluid, integrating components, and delivering systems to datacenter operators and hyperscalers.

| Layer | Detail |
|-------|--------|
| **SmartCoolant raw materials** | Proprietary synthetic blend; Submer does not disclose chemical suppliers; single-source risk if key precursors are from limited suppliers |
| **Tank fabrication** | Custom stainless or composite tank construction; likely outsourced to contract fabricators in Spain/Europe |
| **Heat exchangers** | Standard plate heat exchangers from Alfa Laval, Danfoss, or similar; commodity layer |
| **Pumps and fluid management** | Industrial pump suppliers (Grundfos, Xylem, or similar) |
| **Sensors and monitoring** | SmartCoolant monitoring instruments; likely third-party sensors integrated in Submer software |
| **Submer's position** | Fluid chemistry (proprietary), system design, software monitoring, integration, and service |
| **Customers (downstream)** | Hyperscalers, telecoms, enterprise, HPC/research, government |

**⚑ SmartCoolant supply chain opacity:** The chemical composition of SmartCoolant is proprietary and its upstream raw material supply chain is not disclosed. If key precursor chemicals are sourced from a limited number of suppliers (or from China), this is an unquantified risk. This is worth monitoring as Submer scales.

**Competitive context:** Submer's primary direct competitor is LiquidStack (two-phase immersion; Wiwynn-backed). GRC (Green Revolution Cooling, Austin, TX; single-phase, ElectroSafe fluid) and Iceotope (chassis-level immersion, UK) are also in the market but with different system architectures. **3M's discontinuation of Novec fluorocarbon fluids** has created a gap in the two-phase market that benefits single-phase vendors including Submer, as operators concerned about two-phase fluid supply security consider single-phase alternatives.

## Claim Verification

### Claim: SmartCoolant is "biodegradable" and "non-toxic"
**Status:** Company-stated; no independent third-party certification published in public materials

**Supporting:**
- Submer consistently describes SmartCoolant with these attributes across investor materials, product documentation, and press
- The company markets to ESG-conscious enterprise and government customers where false environmental claims would carry reputational and legal risk
- The general category of synthetic ester dielectric fluids (which SmartCoolant appears to belong to) does include genuinely biodegradable variants

**Refuting / questioning:**
- Specific SDS (Safety Data Sheet) data and biodegradability test methodology (e.g., OECD 301B) are not publicly available
- "Biodegradable" can range from readily biodegradable (>60% in 28 days) to ultimately biodegradable over years; Submer has not specified the standard used
- Third-party environmental certification (ECOLOGO, Nordic Swan, etc.) has not been publicized

**Summary:** Claims are plausible for synthetic ester-type fluids but cannot be independently verified without SDS/test data. For operators with strict environmental compliance requirements, direct inquiry to Submer for certified test data is recommended.

### Claim: PUE of 1.02–1.03
**Status:** Design-basis figure; operationally achievable but depends on facility configuration

**Supporting:**
- Thermodynamically accurate: single-phase immersion eliminates virtually all mechanical cooling infrastructure power; the only electrical overhead is fluid pumps, which consume <2% of total IT load in well-designed systems
- Consistent with published academic and industry data on immersion-cooled facility energy performance

**Refuting / questioning:**
- Operational PUE at a specific facility depends on the heat rejection system used (free cooling vs. mechanical chiller), climate, and load factor; actual facility PUE may be higher
- 1.02–1.03 likely requires favorable climate (free cooling hours) and consistently high server utilization; partial-load operation and warm-climate facilities will see higher PUE

**Summary:** The PUE figure is a best-case design target, not a guaranteed operational outcome. It is directionally accurate and among the best achievable in the industry for high-density compute. Verify against operational data from customer deployments when available.

## Sources

- [About Submer — Submer Technologies](https://submer.com/about-us/)
- [Submer Raises $55.5M to Cool Things Down — TechCrunch (Oct 2024)](https://techcrunch.com/2024/10/02/as-data-center-usage-heats-up-submer-raises-55-5m-to-cool-things-down/)
- [Submer $55.5M Series C at $500M Valuation — FinSMEs (Oct 2024)](https://www.finsmes.com/2024/10/submer-raises-55-5m-in-series-c-funding-at-500m-valuation.html)
- [Submer Raises $55.5M — SiliconANGLE (Oct 2024)](https://siliconangle.com/2024/10/03/submer-raises-55-5m-scale-sustainable-immersion-cooling-ai-data-center-servers/)
- [Immersion Cooling Firm Submer to Release Autonomous Robot — Data Center Dynamics](https://www.datacenterdynamics.com/en/news/immersion-cooling-firm-submer-to-release-autonomous-robot/)
- [Submer Company Profile — Tracxn](https://tracxn.com/d/companies/submer/__NjMhg1nIBsRsqjjhdeV4ghzWPXBew9KZEmoBrlrb8nI)
