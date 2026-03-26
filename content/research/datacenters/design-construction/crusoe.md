---
title: "Crusoe"
date: 2026-03-25
lastmod: 2026-03-25
draft: false
description: "Denver-based AI Factory developer and cloud provider; co-founded 2018 by Chase Lochmiller and Cully Cavness; $2.77B raised; primary developer for OpenAI's Stargate campus in Abilene, TX ($11.6B financing, ~$15B total committed); zero-water-evaporation direct-to-chip cooling; vertically integrated from power sourcing through managed AI inference. Divested bitcoin mining to NYDIG in 2024 to focus entirely on AI infrastructure."
tags: ["datacenters", "design-construction", "us", "ai-datacenter", "cooling", "direct-to-chip", "power-infrastructure", "startup"]
categories: ["company"]
research_area: "datacenters/design-construction"
source_urls:
  - "https://www.crusoe.ai/"
  - "https://www.datacenterdynamics.com/en/news/crusoe-secures-116bn-in-debt-and-equity-for-openais-stargate-data-center-campus-in-abilene-texas/"
  - "https://www.businesswire.com/news/home/20241015910376/en/Crusoe-Blue-Owl-Capital-and-Primary-Digital-Infrastructure-Enter-%243.4-billion-Joint-Venture-for-AI-Data-Center-Development"
  - "https://www.crusoe.ai/resources/newsroom/crusoe-series-c-bloomberg"
last_reviewed: 2026-03-25
stale_after_days: 90
related:
  - "datacenters/design-construction/_index.md"
  - "datacenters/design-construction/applied-digital.md"
  - "datacenters/cooling/_index.md"
  - "datacenters/power-infrastructure/_index.md"
  - "energy/nuclear/blue-energy.md"
---

## Summary

Crusoe is a Denver, Colorado AI Factory developer and cloud provider co-founded in 2018 by Chase Lochmiller (CEO) and Cully Cavness. The company began as a stranded natural gas monetization play — deploying mobile compute infrastructure at oil well flare sites to mine bitcoin using gas that would otherwise be burned off — and has since pivoted entirely to AI infrastructure. Crusoe divested its bitcoin mining operations to NYDIG in 2024 and is now focused on designing, building, and operating large-scale AI datacenters, operating a cloud platform (Crusoe Cloud), and providing managed AI inference services. Its most significant project is serving as primary developer for OpenAI's Stargate campus in Abilene, Texas — an 800-acre site with $11.6B in debt and equity financing secured in 2025, bringing total committed capital for the campus to ~$15B. The facility uses zero-water-evaporation direct-to-chip liquid cooling. Crusoe's positioning is vertically integrated from power sourcing through managed inference — differentiating it from Applied Digital (developer/operator only) and traditional colocation operators.

## Key Facts

- **Founded:** 2018
- **HQ:** Denver, CO
- **Type:** Private
- **Co-Founders:** Chase Lochmiller (CEO), Cully Cavness (COO)
- **Total raised:** ~$2.77B (equity); plus ~$11.6B in project-level debt/equity for Abilene
- **Series C:** $350M (2022), G2 Venture Partners lead; valuation $1.75B
- **Series D:** $600M (2024); valuation $2.8B
- **Additional 2025 funding:** $1.3B equity raise (October 2025)
- **Flagship project:** Stargate Abilene campus — primary developer for OpenAI; 800 acres; 8 planned high-performance data halls; up to 50,000 NVIDIA GB200 NVL72 nodes per hall; first 206 MW phase activated mid-2025; full buildout projected mid-2026
- **Abilene financing:** $11.6B in debt and equity via Blue Owl Capital Real Assets and Primary Digital Infrastructure; total committed capital ~$15B
- **Joint venture:** $3.4B JV with Blue Owl Capital and Primary Digital Infrastructure (announced October 2024) for broader AI datacenter development program
- **Cooling:** Zero-water-evaporation closed-loop direct-to-chip liquid cooling (chilled liquid sealed circuit onto GPU cold plates; no cooling towers)
- **Cloud platform:** Crusoe Cloud IaaS — GPU compute, 99.98% uptime claim; NVIDIA GB200 NVL72, B200, AMD MI355x, MI300x
- **Inference product:** Crusoe Managed Inference — MemoryAlloy technology for low-latency large-context workloads; Llama, DeepSeek, Nemotron models
- **Power strategy:** Vertically controlled power including stranded natural gas, wind, solar, hydropower; Form Energy iron-air battery and Redwood Materials recycled battery partnerships
- **Nuclear power partnership:** [Blue Energy]({{< relref "../../energy/nuclear/blue-energy.md" >}}) — 1.5 GW SMR plant at Port of Victoria, TX; gas bridge to Crusoe campus 2028, nuclear generation 2031
- **Crusoe Spark:** Modular edge computing unit for distributed/edge deployments
- **Bitcoin mining exit:** Divested to NYDIG in 2024; full pivot to AI infrastructure

## What It Is / How It Works

Crusoe is the most vertically integrated player in the AI Factory category. Where Applied Digital operates at the developer/operator layer (build-and-lease to tenants), Crusoe extends both upstream (power sourcing and procurement) and downstream (cloud platform and managed inference services directly to AI developers). This creates a different risk and margin profile.

**The stranded energy origin:** Crusoe's founding insight was that oil fields "flare" (burn off) natural gas that would cost money to capture and pipe — creating cheap, stranded power near the wellhead. Crusoe deployed mobile bitcoin miners at flare sites, monetizing the gas while reducing methane emissions vs. open flaring. This "energy-first" philosophy — find underpriced or stranded power, build compute around it — carried forward into the AI infrastructure pivot even after bitcoin mining was shed.

**Abilene / Stargate:** The Abilene campus is Crusoe's defining project. Located on the former Lancium Clean Campus south of Abilene, Texas, the site benefits from West Texas wind power (ERCOT grid, among the lowest industrial power rates in the US) and proximity to OpenAI's technical teams. Crusoe broke ground on undeveloped land in June 2024; the first 206 MW phase came online by mid-2025 — approximately 12 months from bare land to live AI compute, which is exceptionally fast for a facility of this scale. The $11.6B financing (Blue Owl Real Assets + Primary Digital Infrastructure) makes this one of the largest single-site AI infrastructure financing events on record.

**Zero-water-evaporation cooling:** The Abilene facility uses closed-loop direct-to-chip liquid cooling with no evaporative water loss. Chilled fluid is piped directly to GPU cold plates; the loop is sealed and circulates without cooling towers. After an initial fill (approximately 1 million gallons at campus scale), top-up is minimal maintenance only. In a water-scarce West Texas environment, zero-evaporation cooling is both an operational requirement (municipal water supply is insufficient for traditional cooling tower volumes) and a regulatory/permitting advantage.

**Crusoe Cloud:** The cloud platform provides IaaS GPU compute to AI developers — a different business from the datacenter developer/operator model. Crusoe Cloud competes with CoreWeave, Lambda Labs, and to some extent the hyperscalers for AI training and inference workloads. The "MemoryAlloy" inference engine claims ultra-low latency for large-context workloads, targeting inference serving rather than just training.

**Vertical integration rationale:** By controlling power (not just buying it from utilities), building facilities, operating a cloud platform, and selling managed inference, Crusoe captures margin at multiple layers. The tradeoff is capital intensity and execution complexity. The Stargate relationship — where OpenAI is the anchor tenant — de-risks the facility layer while Crusoe builds its cloud/inference business alongside.

## Notable Developments

- **2025-10:** $1.3B equity raise to accelerate large-scale AI datacenter buildout. ([SiliconANGLE](https://siliconangle.com/2025/10/23/crusoe-lands-1-3b-accelerate-buildout-large-scale-ai-data-centers/))
- **2025 (mid):** Abilene Stargate campus Phase 1 (206 MW) activated — approximately 12 months from bare land to live compute.
- **2025:** $11.6B in debt and equity secured for Abilene campus expansion; total committed capital ~$15B; Blue Owl Real Assets and Primary Digital Infrastructure as capital partners. ([Data Center Dynamics](https://www.datacenterdynamics.com/en/news/crusoe-secures-116bn-in-debt-and-equity-for-openais-stargate-data-center-campus-in-abilene-texas/))
- **2024-10:** $3.4B joint venture with Blue Owl Capital and Primary Digital Infrastructure announced for AI datacenter development program. ([BusinessWire](https://www.businesswire.com/news/home/20241015910376/en/Crusoe-Blue-Owl-Capital-and-Primary-Digital-Infrastructure-Enter-%243.4-billion-Joint-Venture-for-AI-Data-Center-Development))
- **2024:** Series D — $600M; valuation $2.8B. Bitcoin mining operations divested to NYDIG; full AI infrastructure pivot completed.
- **2024-06:** Ground broken at Abilene Stargate campus on undeveloped land.
- **2022:** Series C — $350M; G2 Venture Partners lead; $1.75B valuation.
- **2018:** Founded by Chase Lochmiller and Cully Cavness; initial focus on stranded natural gas monetization via mobile bitcoin mining at oil flare sites.

## Key People

### Chase Lochmiller — Co-Founder and CEO
- **LinkedIn:** [linkedin.com/in/chaselochmiller](https://www.linkedin.com/in/chaselochmiller/) *(confirm)*
- **Role:** Co-founder and CEO since founding
- **Background:** Technology investor and entrepreneur prior to Crusoe; co-created the stranded gas / flare mitigation concept that became Crusoe's founding model
- **Notes:** Lochmiller has been the primary external voice on Crusoe's energy-first philosophy and the AI infrastructure pivot; the OpenAI/Stargate relationship is his flagship customer win

### Cully Cavness — Co-Founder and COO
- **LinkedIn:** Search "Cully Cavness Crusoe"
- **Role:** Co-founder and COO
- **Background:** Operational leadership; manages day-to-day execution of facility development and power procurement
- **Notes:** Less externally profiled than Lochmiller; operational rather than strategic/external-facing

### Michael Gordon — COO/CFO
- **LinkedIn:** Search "Michael Gordon Crusoe AI"
- **Role:** COO and CFO (dual role)
- **Background:** Finance and operations executive; joined as Crusoe scaled from Series C to Stargate

### Erwan Menard — SVP Product Management
- **LinkedIn:** Search "Erwan Menard Crusoe"
- **Role:** SVP Product Management
- **Background:** Product leadership for Crusoe Cloud and managed inference products

### People — Last Reviewed: 2026-03-25

## Supply Chain Position

Crusoe sits at multiple layers simultaneously due to vertical integration:

| Layer | Crusoe's role |
|-------|--------------|
| **Power sourcing** | Direct ownership/control of power assets — stranded gas, wind PPAs, solar; Form Energy iron-air battery partnership for storage |
| **Facility developer** | Design and construction of AI Factory campuses (Abilene and future sites) |
| **Facility operator** | Long-term operation; zero-water-evaporation cooling system operation |
| **Cloud IaaS** | Crusoe Cloud GPU compute platform (NVIDIA GB200, B200, AMD MI355x, MI300x) |
| **Managed inference** | Crusoe Managed Inference — end-customer-facing AI API |
| **Key upstream hardware** | NVIDIA GPU allocations (GB200 NVL72 at Abilene — same hardware as hyperscale AI training clusters; allocation access is competitive) |
| **Anchor tenant** | OpenAI (Stargate) — single-tenant relationship for Abilene campus |

**⚑ OpenAI concentration risk:** The Abilene campus is built around OpenAI as anchor tenant. OpenAI's capital commitments, compute roadmap, and continued growth are the primary revenue drivers for Crusoe's largest asset. Any OpenAI financial stress, model architecture shift away from dense GPU training, or competitive loss to open-source alternatives propagates directly to Crusoe's facility utilization.

**⚑ NVIDIA supply dependency:** The Abilene facility is spec'd for NVIDIA GB200 NVL72 nodes. NVIDIA GPU allocation — for both Crusoe's own facility buildout and the cloud platform — is subject to NVIDIA's production capacity and allocation priorities. Crusoe also offers AMD MI355x/MI300x on its cloud platform, which partially mitigates single-vendor dependency, but the Abilene hardware spec is NVIDIA-centric.

**⚑ Shared power thesis with Applied Digital:** Both Crusoe and Applied Digital are pursuing low-cost stranded/renewable power in non-coastal markets (West Texas for Crusoe, North Dakota for Applied Digital). This is the right strategy given the grid interconnection crisis in coastal markets. If West Texas ERCOT rates rise materially (possible given ERCOT grid stress during extreme weather events), Crusoe's power cost advantage narrows.

## Claim Verification

### Claim: 12-month bare land to live compute at Abilene (206 MW)
**Status:** Reported; not independently timed but consistent with available timeline data (ground broken June 2024; phase 1 live mid-2025)

**Supporting:**
- Ground breaking confirmed June 2024 per public announcements; first phase operational mid-2025 is consistent with the 12-month claim
- 12 months for 206 MW is genuinely fast — most comparable facilities take 18–24+ months from ground break to commissioning

**Refuting / questioning:**
- "Bare land" to "activated" could include pre-construction site prep and utility interconnect work that began before the June 2024 ground breaking; true timeline from land acquisition to power-on may be longer
- Lancium Clean Campus was an existing site with some infrastructure; Crusoe may have inherited permitting and utility work

**Summary:** The speed claim is directionally accurate and notable even with caveats. Crusoe's execution pace at Abilene is a legitimate competitive differentiator.

### Claim: Zero-water-evaporation cooling
**Status:** Company-stated; technically credible for closed-loop direct-to-chip systems; operational WUE not independently published

**Supporting:**
- Closed-loop sealed cooling circuits do not evaporate water — this is a definitional property of the architecture, not a performance claim
- West Texas water scarcity context makes this a practical necessity, not just a marketing claim; the regulatory environment reinforces it
- 1-million-gallon initial fill figure suggests the system has been engineered at campus scale

**Refuting / questioning:**
- "Zero-water-evaporation" is accurate for the sealed loop but does not account for water used in building construction, landscaping, or facility HVAC for humans (offices, etc.); these are minor relative to cooling loads but WUE metrics should be specified precisely
- Heat rejection from a sealed loop still requires a heat sink — West Texas ambient air via dry coolers in summer (40°C+) will be thermally stressed; mechanical cooling energy overhead during summer peak may be significant

**Summary:** Technically accurate as stated. The relevant question for operational performance is PUE during West Texas summer peaks, which has not been published.

### Claim: "Up to 20x faster" model deployment, "81% cost reduction" (Crusoe Managed Inference)
**Status:** Marketing claims; no independent benchmark published

**Supporting:** Not independently verifiable from public sources

**Refuting:** "Up to" framing allows cherry-picking of best-case comparisons; the baseline comparison (vs. which provider, for which model, under what load) is not specified

**Summary:** Treat as unverified marketing claims until independent benchmarks are published.

## Sources

- [Crusoe AI — crusoe.ai](https://www.crusoe.ai/)
- [Crusoe Secures $11.6B for Abilene Stargate Campus — Data Center Dynamics](https://www.datacenterdynamics.com/en/news/crusoe-secures-116bn-in-debt-and-equity-for-openais-stargate-data-center-campus-in-abilene-texas/)
- [$3.4B Joint Venture with Blue Owl Capital — BusinessWire (Oct 2024)](https://www.businesswire.com/news/home/20241015910376/en/Crusoe-Blue-Owl-Capital-and-Primary-Digital-Infrastructure-Enter-%243.4-billion-Joint-Venture-for-AI-Data-Center-Development)
- [Crusoe Series C ($350M) — Crusoe Newsroom](https://www.crusoe.ai/resources/newsroom/crusoe-series-c-bloomberg)
- [Crusoe $686M Filing — TechCrunch (Nov 2024)](https://techcrunch.com/2024/11/21/crusoe-a-rumored-openai-data-center-supplier-has-secured-686m-in-new-funds-filing-shows/)
- [Crusoe Lands $1.3B — SiliconANGLE (Oct 2025)](https://siliconangle.com/2025/10/23/crusoe-lands-1-3b-accelerate-buildout-large-scale-ai-data-centers/)
- [Inside Crusoe's Energy-First Approach — Latitude Media](https://www.latitudemedia.com/news/catalyst-inside-crusoes-energy-first-approach-to-data-centers/)
- [Abilene 3 Data Center — Baxtel](https://baxtel.com/data-center/crusoe-abilene-3)
