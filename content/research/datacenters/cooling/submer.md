---
title: "Submer Technologies"
date: 2026-03-24
lastmod: 2026-10-20
draft: false
description: "Barcelona-based single-phase immersion cooling company (SmartPod, SmartCoolant) that has expanded since 2025 into AI cloud (InferX), data-center development (Rubix, June 2026) and modular infrastructure (Corenix, September 2026); $55.5M Series C at about $500M valuation in October 2024."
research_area: "datacenters/cooling"
source_urls:
  - "https://submer.com/about-us/"
  - "https://techcrunch.com/2024/10/02/as-data-center-usage-heats-up-submer-raises-55-5m-to-cool-things-down/"
  - "https://www.datacenterdynamics.com/en/news/immersion-cooling-firm-submer-to-release-autonomous-robot/"
  - "https://www.datacenterdynamics.com/en/news/submer-launches-rubix-data-centers-claims-platform-has-8gw-powered-land-portfolio/"
  - "https://www.datacenterdynamics.com/en/news/submer-launches-corenix-to-offer-modular-data-center-infrastructure/"
  - "https://www.datacenterdynamics.com/en/news/immersion-cooling-firm-submer-launches-ai-cloud-unit/"
  - "https://www.datacenterdynamics.com/en/news/immersion-cooling-firm-submer-partners-with-indian-real-estate-developer-anant-raj-for-data-center-venture/"
last_reviewed: 2026-10-20
stale_after_days: 90
related:
  - "datacenters/robotics-automation/submer-ada.md"
  - "datacenters/cooling/_index.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.


## Summary

Submer Technologies, founded in Barcelona in 2015 by Daniel Pope and Pol Valls Soler, is a single-phase immersion cooling company whose products are the SmartPod tank line and SmartCoolant dielectric fluid. It raised a $55.5M Series C at about a $500M valuation in October 2024, led by M&G Investments. Since late 2025 it has broadened beyond cooling: InferX (sovereign AI cloud, October 2025), Rubix Data Centers (June 2026, claiming 8 GW of powered land), and Corenix (modular infrastructure, September 2026). It also says it passed 500 MW of liquid-cooled deployments in 2025. Its ADA tank-servicing robot is covered in [Submer ADA]({{< relref "submer-ada.md" >}}).

## Key Facts

- **Founded:** 2015; HQ Barcelona; regional HQs in Houston (Americas), Taipei (APAC) and Dammam (MEA); R&D labs in Sausalito and Taipei ([Submer](https://submer.com/about-us/))
- **Type:** Private
- **CEO:** Patrick Smets (quoted as CEO in June 2026 coverage); co-founders Daniel Pope and Pol Valls Soler
- **Funding:** Series C $55.5M at about $500M valuation, October 2024, led by M&G Investments with Mundi Ventures, Planet First Partners, Norrsken VC ([TechCrunch](https://techcrunch.com/2024/10/02/as-data-center-usage-heats-up-submer-raises-55-5m-to-cool-things-down/)); a further $20.9M debt financing was reported by Tracxn (not re-verified)
- **Products:** SmartPod immersion tanks (2018), SmartPod EXO hyperscale platform (2024), SmartCoolant fluid, Submer AI Cloud (2025)
- **Scale claim:** surpassed 500 MW of liquid-cooled deployments in 2025 (company statement)
- **Business expansion:** InferX AI cloud unit (Oct 2025); non-binding MoU with Anant Raj Cloud, India (Feb 2026); Rubix Data Centers, CEO John Eland, claimed 8 GW of powered land across the Americas, EMEA and APAC (2 Jun 2026); Corenix modular infrastructure, CEO Martin Renkis, built on Nvidia reference designs (late Sep 2026)
- **ADA robot:** not listed among products on Submer's About page as of 2026-10-20; see [Submer ADA]({{< relref "submer-ada.md" >}})
- **Design-basis figures (company):** PUE 1.02–1.03
- **Customers:** the company's About page names none; earlier coverage cited Telefónica, ExxonMobil and the European Commission (not re-verified)

## What It Is / How It Works

Submer's SmartPod is a single-phase immersion cooling system. "Single-phase" means the dielectric fluid remains liquid throughout the heat exchange process — it absorbs heat from servers and is pumped to a heat exchanger (chiller, dry cooler, or facility water loop) where it releases heat before recirculating. This contrasts with two-phase immersion (e.g., LiquidStack), where the fluid boils and condenses — which achieves higher heat transfer coefficients but is more complex to manage and historically used fluorocarbon fluids with supply concerns around 3M's exit from Novec fluids.

**SmartCoolant** is Submer's proprietary fluid and is the core product differentiation. Its key attributes:

- **Biodegradable:** Derived from a synthetic blend designed to break down in the environment; addresses regulatory and ESG requirements
- **Non-toxic, non-flammable:** Safe handling without hazmat protocols
- **Water viscosity:** Server pumps and fans are designed for air or water; SmartCoolant's similar viscosity to water means it doesn't stress server components (though fans are typically disabled in immersion deployments)
- **Long change interval:** Designed to remain stable for multi-year service intervals without degradation; reduces operational cost vs. frequent fluid changes

**SmartPod** tanks accommodate industry-standard servers in a horizontal submersion configuration. The tank connects to a heat exchanger — at minimum a plate heat exchanger to building chilled water, or alternatively coupled to dry coolers, free cooling, or even heat recovery systems. Submer's SmartMod product packages tanks, piping, power distribution, and monitoring into a prefabricated module for faster deployment.

The practical PUE of 1.02–1.03 in immersion systems comes from eliminating CRAC units, raised floors, and hot/cold aisle infrastructure. The only cooling-related power draw is the fluid pump, which is minimal. This compares to 1.3–1.5 PUE for well-designed air-cooled facilities and 1.1–1.2 PUE for direct-to-chip liquid cooling.

**Operational friction:** The tradeoff is servicing complexity. Servers submerged in fluid cannot be hot-swapped like rack-mounted units. Lifting a server from a tank requires PPE (dielectric fluid must be kept off skin and out of drains), vertical lift equipment, and fluid drip management. This is why Submer is developing ADA — without robotic assistance, immersion cooling scales better in density than in operational agility.

## Notable Developments

- **2026-09 (late):** Submer Group launches Corenix, a modular data center company for neoclouds, hyperscalers and AI operators; CEO Martin Renkis. ([DCD](https://www.datacenterdynamics.com/en/news/submer-launches-corenix-to-offer-modular-data-center-infrastructure/))
- **2026-06-02:** Submer launches Rubix Data Centers to develop and operate AI data centers; claims 8 GW of power available across vacant sites; CEO John Eland (formerly Stack EMEA). Backers named: M&G, Planet First, Norrsken VC, Mundi Ventures; no amounts disclosed. ([DCD](https://www.datacenterdynamics.com/en/news/submer-launches-rubix-data-centers-claims-platform-has-8gw-powered-land-portfolio/))
- **2026-02:** Non-binding MoU with Anant Raj Cloud (India); no capacity, location or financial terms disclosed. ([DCD](https://www.datacenterdynamics.com/en/news/immersion-cooling-firm-submer-partners-with-indian-real-estate-developer-anant-raj-for-data-center-venture/))
- **2025-10:** InferX sovereign AI cloud unit launched; DCD also notes a planned 56 MW Barcelona facility and a Madhya Pradesh MoU for up to 1 GW. ([DCD](https://www.datacenterdynamics.com/en/news/immersion-cooling-firm-submer-launches-ai-cloud-unit/))
- **2025-02:** DCD reports Submer plans to release its autonomous ADA robot, possibly around Q3 2025. ([DCD](https://www.datacenterdynamics.com/en/news/immersion-cooling-firm-submer-to-release-autonomous-robot/))
- **2024-10:** Series C, $55.5M at $500M valuation. ([TechCrunch](https://techcrunch.com/2024/10/02/as-data-center-usage-heats-up-submer-raises-55-5m-to-cool-things-down/))
- **2024-01:** Patrick Smets becomes CEO. **2015:** Founded in Barcelona.

## Key People

### Patrick Smets — CEO (since January 2024)
- **LinkedIn:** not found
- **Role:** CEO since January 2024; joined as COO August 2023
- **Background:** Operations and scaling executive; recruited to bring operational discipline as Submer transitioned from early-stage startup to growth-stage company; not one of the technical founders
- **Notes:** First externally recruited CEO; co-founders remain involved

### Daniel Pope — Co-Founder
- **LinkedIn:** not found
- **Role:** Co-founder; named as founder of the InferX AI cloud unit (DCD, Oct 2025)
- **Background:** Entrepreneur and datacenter sustainability advocate; co-created Submer's vision of "datacenters that make sense" — combining efficiency, sustainability, and high density

### Pol Valls Soler — Co-Founder
- **LinkedIn:** not found
- **Role:** Co-founder; technical and product leadership alongside Pope in founding years
- **Background:** Engineering background; involved in SmartCoolant chemistry and SmartPod product development

### John Eland — CEO, Rubix Data Centers
- **LinkedIn:** not found
- **Role:** CEO of Rubix since its June 2026 launch; previously CEO of Stack's EMEA business and chief strategy officer at NTT GDC ([DCD](https://www.datacenterdynamics.com/en/news/submer-launches-rubix-data-centers-claims-platform-has-8gw-powered-land-portfolio/))

### Martin Renkis — CEO, Corenix
- **LinkedIn:** not found
- **Role:** CEO of Corenix; formerly of Johnson Controls ([DCD](https://www.datacenterdynamics.com/en/news/submer-launches-corenix-to-offer-modular-data-center-infrastructure/))

Backgrounds of Smets, Pope and Valls Soler are as of the previous review and were not re-verified.

### People — Last Reviewed: 2026-10-20

## Supply Chain Position

Submer sits at the **Immersion Cooling System** layer — tank and fluid design, integration and service — and has been moving up the stack into modular infrastructure (Corenix), AI cloud (InferX) and data-center development (Rubix). Suppliers of SmartCoolant precursors, tanks, heat exchangers and pumps are not disclosed.

**⚑ SmartCoolant supply chain opacity:** the composition of SmartCoolant and its upstream supply chain are proprietary, so concentration risk cannot be assessed from public sources.

**Competitive context:** Direct competitors include LiquidStack (two-phase), GRC (single-phase) and Iceotope (chassis-level). Moving into development and cloud puts Submer in competition with some of its own potential customers, a strategic tension worth watching.

## Claim Verification

### Claim: SmartCoolant is "biodegradable" and "non-toxic"
**Status:** Company-stated; no independent third-party certification published in public materials

**Supporting:**
- Submer consistently describes SmartCoolant with these attributes in its own materials

**Refuting / questioning:**
- Specific SDS (Safety Data Sheet) data and biodegradability test methodology (e.g., OECD 301B) are not publicly available
- "Biodegradable" can range from readily biodegradable (>60% in 28 days) to ultimately biodegradable over years; Submer has not specified the standard used
- Third-party environmental certification (ECOLOGO, Nordic Swan, etc.) has not been publicized

**Summary:** Claims cannot be independently verified without SDS/test data. For operators with strict environmental compliance requirements, direct inquiry to Submer for certified test data is recommended.

### Claim: PUE of 1.02–1.03
**Status:** Design-basis figure (company); operational data not published

**Supporting:**
- Immersion removes most room-level mechanical cooling, leaving pumps and heat rejection as the cooling load; Submer states the 1.02–1.03 design range

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
- [Submer launches Rubix Data Centers — DCD (Jun 2026)](https://www.datacenterdynamics.com/en/news/submer-launches-rubix-data-centers-claims-platform-has-8gw-powered-land-portfolio/)
- [Submer launches Corenix — DCD (Sep 2026)](https://www.datacenterdynamics.com/en/news/submer-launches-corenix-to-offer-modular-data-center-infrastructure/)
- [Submer launches AI cloud unit — DCD (Oct 2025)](https://www.datacenterdynamics.com/en/news/immersion-cooling-firm-submer-launches-ai-cloud-unit/)
- [Submer partners with Anant Raj — DCD (Feb 2026)](https://www.datacenterdynamics.com/en/news/immersion-cooling-firm-submer-partners-with-indian-real-estate-developer-anant-raj-for-data-center-venture/)
- [Submer Company Profile — Tracxn](https://tracxn.com/d/companies/submer/__NjMhg1nIBsRsqjjhdeV4ghzWPXBew9KZEmoBrlrb8nI)
