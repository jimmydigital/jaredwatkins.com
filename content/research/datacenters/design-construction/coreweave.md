---
title: "CoreWeave"
date: 2026-04-02
lastmod: 2026-04-02
draft: false
description: "Livingston, NJ GPU cloud company; co-founded 2017 (as Atlantic Crypto) by Michael Intrator, Brian Venturo, Brannin McBee, and Peter Salanki; pivoted from Ethereum mining to AI cloud 2019; IPO March 2025 (CRWV, ~$35B market cap); $5.1B revenue FY2025; $66.8B contracted backlog; designs entire data centers for 130kW+ liquid-cooled racks; NVIDIA strategic partner and preferred GPU allocatee; 5 GW capacity expansion target by 2030; largest 'neocloud' in the AI infrastructure market."
tags: ["datacenters", "design-construction", "us", "uk", "ai-datacenter", "high-density", "liquid-cooling", "power-infrastructure", "public"]
categories: ["company"]
research_area: "datacenters/design-construction"
source_urls:
  - "https://www.coreweave.com/"
  - "https://www.sec.gov/Archives/edgar/data/1769628/000119312525044231/d899798ds1.htm"
  - "https://investors.coreweave.com/governance/executive-management/default.aspx"
  - "https://www.datacenterdynamics.com/en/news/coreweave-aims-to-add-5gw-more-data-center-capacity-by-2030-anticipates-capex-in-2026-to-double/"
  - "https://nvidianews.nvidia.com/news/nvidia-and-coreweave-strengthen-collaboration-to-accelerate-buildout-of-ai-factories"
last_reviewed: 2026-04-02
stale_after_days: 60
related:
  - "datacenters/design-construction/_index.md"
  - "datacenters/design-construction/crusoe.md"
  - "datacenters/cooling/_index.md"
  - "datacenters/power-infrastructure/_index.md"
---

## Summary

CoreWeave is the largest "neocloud" — a specialized AI GPU cloud provider sitting between traditional hyperscalers (AWS, Azure, GCP) and pure colocation operators — in the AI infrastructure market. The company was founded in 2017 in New Jersey as Atlantic Crypto by four commodities traders: Michael Intrator (CEO), Brian Venturo (Chief Strategy Officer), Brannin McBee (Chief Development Officer), and Peter Salanki (CTO). At its peak in 2018, Atlantic Crypto was one of the largest Ethereum miners in North America, deploying thousands of NVIDIA GPUs across seven data centers. The 2018–2019 "crypto winter" triggered the pivot: the founders recognized their GPU hardware inventory was more valuable as cloud compute infrastructure than as mining equipment, and in 2019 they pivoted to offering GPU-as-a-service (GPUaaS) to AI and HPC customers, rebranding as CoreWeave in 2021. This origin story — a crypto mining company that accidentally became AI infrastructure — closely parallels Crusoe's stranded-gas-to-AI-factory arc.

CoreWeave went public on March 28, 2025 on Nasdaq (ticker: CRWV), pricing at $40/share and targeting a ~$35B market cap, making it one of the largest tech IPOs of 2025. Revenue has grown at extraordinary pace: $16M (2022), $229M (2023), $1.9B (2024), and ~$5.1B estimated for FY2025 — a 737% YoY increase from 2023 to 2024 alone. The company carries a $66.8B contracted revenue backlog (as of December 31, 2025), anchored by OpenAI (~$22.4B committed) and Meta (~$14.2B through 2031), with Microsoft historically accounting for ~70% of annual revenue. Despite top-line hypergrowth, CoreWeave remains unprofitable: net loss widened to $1.167B in FY2025, driven by $1.2B+ in annual interest expense on $11B+ in debt. The $30–35B CapEx guidance for 2026 — more than double 2025 — signals continued aggressive investment in a race to deploy capacity ahead of demand.

CoreWeave's technical differentiation is its facility design philosophy: rather than retrofitting colocation space for AI workloads, CoreWeave builds entire data centers from the ground up around liquid-cooled, high-density GPU racks. Its newer facilities target 130kW+ per rack, matching the thermal envelope of the NVIDIA GB300 NVL72 system (~140kW at full load). Most facilities opening in 2025 and beyond include full liquid cooling infrastructure from foundation to roof — a design decision that separates CoreWeave from most traditional colocation operators whose legacy air-cooled infrastructure tops out at 10–30kW/rack. CoreWeave's relationship with NVIDIA is both its key strategic advantage (early GPU allocation, preferred partner status) and a significant single-vendor concentration risk.

## Key Facts

- **Founded:** 2017 (as Atlantic Crypto)
- **Rebranded:** CoreWeave (2021); rebranded from Atlantic Crypto after 2019 pivot away from crypto mining
- **HQ:** Livingston, NJ
- **Type:** Public (Nasdaq: CRWV; IPO March 28, 2025)
- **Co-Founders:** Michael Intrator (CEO), Brian Venturo (CSO), Brannin McBee (CDO), Peter Salanki (CTO)
- **IPO:** March 28, 2025; priced $40/share; ~$35B market cap at IPO
- **Revenue (FY2022–FY2025):** $16M → $229M → $1.9B → ~$5.1B (FY2025 estimated)
- **Net loss (FY2022–FY2025):** -$31M → -$594M → -$863M → -$1.167B
- **Adjusted EBITDA FY2025:** $3.093B (vs. $1.219B in FY2024)
- **Revenue backlog:** $66.8B as of December 31, 2025 (up from $55.6B at Q3 2025 end)
- **Anchor customers:** OpenAI (~$22.4B total committed); Meta (~$14.2B through Dec 14, 2031); Microsoft (historically ~70% of annual revenue)
- **NVIDIA relationship:** NVIDIA invested $2B in CoreWeave Class A stock (January 2026); NVIDIA signed $6.3B capacity purchase deal (September 2025, through April 2032 — NVIDIA buys unused CoreWeave capacity); CoreWeave receives early access to new NVIDIA GPU generations before hyperscalers
- **Total debt:** ~$11.17B (June 30, 2025); $1.21–$1.25B annual interest expense
- **2026 CapEx guidance:** $30–35B (more than double 2025 levels)
- **Data centers:** 28+ US facilities as of late 2024; expanding to UK (£1B committed), Norway/Sweden/Spain ($2.2B committed)
- **Capacity target:** 5 GW of AI factory capacity by 2030 (in conjunction with NVIDIA investment)
- **Core Scientific hosting:** 500 MW of critical IT load across six Core Scientific sites (former Bitcoin mining sites converted for HPC); $8.7B over 12-year contract terms
- **Lancaster, PA campus:** Up to $6B committed; 100 MW initial phase, expandable to 300 MW
- **Rack density:** Designs new facilities for 130kW+ per rack; NVIDIA GB300 NVL72 target rack (~140kW at full load); Vertiv CoolChip CDUs (121kW rejection capacity per unit) as primary CDU
- **Cooling strategy:** Liquid cooling designed in from the ground up; no legacy air-cooled retrofit dependency; most 2025+ facilities opened with liquid cooling
- **GPU access:** NVIDIA preferred partner for H100, GB200, GB300 allocations; early access to Rubin, Vera CPU, BlueField storage ahead of hyperscaler availability
- **NVIDIA $8.5B debt facility:** GPU-backed term loan (DDTL 4.0); received investment-grade rating (A3, Moody's) — first HPC-asset-backed loan to achieve investment-grade in history

## What It Is / How It Works

CoreWeave occupies a unique structural position in the AI infrastructure stack: it is the category-defining "neocloud" — a GPU cloud provider purpose-built for AI/HPC that competes neither as a hyperscaler (no general-purpose compute, no enterprise software stack, no global CDN) nor as a traditional colocation operator (CoreWeave does not sell rack space; it sells GPU compute access). The core product is GPU instances rented by the hour, day, or year, with workload orchestration layered on top. CoreWeave claims GPU instances priced approximately 66% cheaper than equivalent hyperscaler offerings — an advantage that stems from specialization (no overhead for general-purpose services), NVIDIA preferred pricing, and GPU-asset-backed debt financing.

**The crypto-to-cloud pivot:** CoreWeave's founding asset was a large inventory of NVIDIA GPUs deployed for Ethereum mining. When Ethereum's proof-of-work mining economics collapsed in 2018–2019, the founders faced a choice: sell the hardware or find another use. They recognized that the same GPU parallelism that made mining profitable was exactly what AI training and VFX rendering customers needed, and pivoted to offering GPUaaS. This is structurally similar to Crusoe's insight about stranded natural gas — finding an underpriced asset (GPUs in crypto bear market) and arbitraging its value into a different market (AI compute). Where Crusoe's ongoing asset is stranded power, CoreWeave's ongoing advantage is NVIDIA GPU allocation priority — earned through being one of NVIDIA's earliest and largest customers.

**Facility design philosophy — high-density liquid cooling from the ground up:** CoreWeave's clearest technical differentiation from legacy colocation operators is facility architecture. Traditional colocation data centers were designed for 5–10kW/rack enterprise workloads. Even aggressive retrofits rarely achieve more than 30–50kW/rack without structural modifications, and air cooling becomes thermally unviable above ~25–30kW/rack. CoreWeave's newest facilities are designed for 130kW+ per rack from the outset — matching the ~140kW thermal envelope of the NVIDIA GB300 NVL72 system. This requires embedded liquid cooling infrastructure (chilled water loops, cooling distribution units, facility-level secondary loops) built into the facility design before a single GPU is installed. Vertiv CoolChip CDUs (121kW liquid-to-liquid heat rejection, sized for GB300 NVL72 cabinets, ASHRAE W5 inlet water temperature, redundant pumps and dual heat exchangers) are CoreWeave's primary CDU platform in newest facilities. The practical implication: a legacy colocation operator cannot compete for the highest-density GPU workloads regardless of how much they spend on retrofit — the physical design of the building limits them.

**The Core Scientific partnership — repurposing Bitcoin mining infrastructure:** CoreWeave's most strategically interesting infrastructure deal is its hosting arrangement with Core Scientific (CORZ), the publicly traded Bitcoin mining company. Core Scientific operates large-scale power infrastructure at multiple US sites — originally deployed for mining, which has broadly similar power delivery requirements to GPU clusters (dense, high-power, 24/7 load). Starting in mid-2024, CoreWeave contracted to convert Core Scientific sites from Bitcoin mining to GPU hosting, exercising options in stages to reach approximately 500 MW of critical IT load across six Core Scientific sites (total potential revenue $8.7B over 12 years). CoreWeave even made a $1 billion acquisition offer for Core Scientific (declined), instead settling on the hosting contract expansion. The arrangement gives CoreWeave access to operational power infrastructure faster than greenfield construction allows, at sites Core Scientific had already secured grid interconnections and power contracts for — a significant shortcut given the 18–24 month typical timeline for new substation and interconnect construction.

**NVIDIA strategic relationship:** CoreWeave's relationship with NVIDIA is the deepest in the neocloud category and functions as both the company's greatest competitive moat and its most significant risk. NVIDIA has invested directly in CoreWeave at multiple stages (including a $2B investment in Class A stock in January 2026), signed a $6.3B capacity purchase agreement (September 2025, where NVIDIA commits to buy unused CoreWeave capacity through April 2032), and gives CoreWeave early deployment rights to new GPU generations (Rubin platform, Vera CPUs, BlueField storage) before hyperscalers. CoreWeave's GPU-backed debt facilities — rated investment-grade (A3, Moody's) based on the underlying GPU asset value and contracted revenue — are only achievable because NVIDIA GPU supply is both credible collateral and a scarce good. The relationship began because CoreWeave was an early large NVIDIA GPU customer during the crypto era; it has evolved into a symbiotic arrangement where NVIDIA uses CoreWeave as a preferred deployment vehicle for next-generation silicon, and CoreWeave uses NVIDIA access as its primary barrier to entry against competitors.

**Business model and capital structure:** CoreWeave earns revenue from long-term GPU compute contracts (typically 12-month+ commitments) at rates significantly below hyperscaler list prices. The $66.8B backlog represents multi-year committed contract value, not just pipeline — the majority is under executed contracts with OpenAI, Meta, and Microsoft. CoreWeave finances GPU purchases through asset-backed debt facilities where the GPU inventory is the collateral — a novel structure that received investment-grade ratings in 2025. The core financial risk is that GPU depreciation cycles (typically 3–5 years for a generation) are shorter than debt repayment timelines, and interest expense ($1.2B+ annually on $11B+ debt) consumes a substantial share of revenue. The 2026 CapEx guidance of $30–35B implies continued rapid expansion of this debt-financed model at a scale that will require sustained hyperscaler commitments and contract renewals to service.

## Notable Developments

- **2026-01:** NVIDIA invests $2B in CoreWeave Class A common stock at $87.20/share (~23M shares); gives NVIDIA 5+ GW of AI factory exposure by 2030. CoreWeave gets early deployment rights for NVIDIA Rubin, Vera CPU, BlueField storage. ([NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-and-coreweave-strengthen-collaboration-to-accelerate-buildout-of-ai-factories))
- **2025-12:** $2.25B in 1.75% convertible senior notes due 2031 issued.
- **2025-11 (Q3 earnings):** Revenue backlog reaches $56.6B; Q3 revenue up 420% YoY; stock slides on guidance revision below analyst consensus. ([Data Center Dynamics](https://www.datacenterdynamics.com/en/news/coreweaves-revenue-up-420-yoy-in-first-earnings-call-since-ipo/))
- **2025-09:** CoreWeave and NVIDIA sign $6.3B capacity purchase deal — NVIDIA commits to buy unused CoreWeave capacity through April 2032. ([datacenters.com](https://www.datacenters.com/news/coreweave-nvidia-s-6-3b-capacity-deal))
- **2025-07:** $1.75B in 9.000% Senior Notes due 2031 issued.
- **2025-03-28:** IPO on Nasdaq (CRWV) at $40/share; ~$35B market cap. First major AI infrastructure IPO of 2025. S-1 reveals Microsoft at 62% of 2024 revenue and single-customer concentration risk. ([SEC S-1](https://www.sec.gov/Archives/edgar/data/1769628/000119312525044231/d899798ds1.htm))
- **2025-01:** First UK data centers (Crawley and London Docklands) come live. ([TechCrunch](https://techcrunch.com/2025/01/13/coreweaves-first-international-data-centers-are-now-live-in-the-uk/))
- **2024-10:** CoreWeave exercises final option in Core Scientific hosting contract, reaching ~500 MW of critical IT load across 6 Core Scientific sites; $8.7B in potential cumulative revenue over 12 years. ([BusinessWire](https://www.businesswire.com/news/home/20241022927349/en/Core-Scientific-Announces-Exercise-of-Final-Contract-Option-by-CoreWeave))
- **2024-05:** Series C close at $19B valuation; $1.1B raised; Coatue lead. ([SiliconANGLE](https://siliconangle.com/2024/05/01/coreweave-raises-1-1b-19b-valuation-grow-gpu-cloud/))
- **2024:** $2.2B European expansion committed — Norway, Sweden, Spain data centers; targeting end-of-2025 opening. ([PR Newswire](https://www.prnewswire.com/news-releases/coreweave-announces-significant-european-expansion-commits-an-incremental-2-2-billion-to-meet-surging-demand-for-ai-infrastructure-in-the-region-302164149.html))
- **2024-06:** Core Scientific initial 200 MW hosting contract signed; CoreWeave makes unsuccessful $1B acquisition offer for Core Scientific.
- **2023-06:** Microsoft signs multi-billion dollar deal for GPU cloud capacity to support Azure AI/OpenAI demand. ([CNBC](https://www.cnbc.com/2023/06/01/microsoft-inks-deal-with-coreweave-to-meet-openai-cloud-demand.html))
- **2021:** Rebranded as CoreWeave; fully pivoted to GPU cloud; begins systematic scaling from 7 data centers to current 28+ US footprint.
- **2019:** Company pivots from Ethereum mining to GPU cloud; renames entity from Atlantic Crypto to CoreWeave; leverages existing GPU inventory to serve AI training and VFX rendering customers.
- **2017:** Founded as Atlantic Crypto in New Jersey by Michael Intrator, Brian Venturo, Brannin McBee, Peter Salanki; initially targets Ethereum mining at scale.

## Key People

### Michael Intrator — Co-Founder and CEO
- **LinkedIn:** Search "Michael Intrator CoreWeave"
- **Role:** Co-founder and CEO since founding
- **Background:** Commodities trader prior to Atlantic Crypto/CoreWeave; no prior technology background; one of four founders who pivoted from commodities to crypto to AI infrastructure
- **Notes:** As of mid-2025, Intrator's net worth exceeded $10B following CoreWeave's post-IPO stock surge (~300% from IPO price through June 2025). Primary external face of CoreWeave in press and investor communications; has spoken publicly about power constraints as the primary limiter on AI infrastructure expansion.

### Brian Venturo — Co-Founder and Chief Strategy Officer
- **Role:** Co-founder and CSO
- **Background:** Commodities trading background; co-founded Atlantic Crypto; CSO role focuses on strategic partnerships, customer relationships, and business development
- **Notes:** Net worth estimated at $6.4B as of mid-2025 per Bloomberg. Less externally visible than Intrator.

### Brannin McBee — Co-Founder and Chief Development Officer
- **Role:** Co-founder and CDO; responsible for data center development, construction, and real estate
- **Background:** One of the original four founders; CDO role is operationally critical given CoreWeave's aggressive facility construction program
- **Notes:** Net worth estimated at $4.7B as of mid-2025. Directly oversees the data center design and construction program that is CoreWeave's primary capital deployment vehicle.

### Peter Salanki — Co-Founder and CTO
- **Role:** Co-founder and CTO; responsible for technology platform, software stack, and infrastructure engineering
- **Background:** Technical co-founder; the engineering counterpart to the three commodities-trader co-founders
- **Notes:** Architects CoreWeave's software layer — the orchestration, scheduling, and reliability engineering that the company argues differentiates it from simpler GPU resellers.

### People — Last Reviewed: 2026-04-02

## Supply Chain Position

CoreWeave occupies the "specialized AI cloud" layer — a neocloud, not a hyperscaler, not a colocation operator:

| Layer | CoreWeave's role |
|-------|-----------------|
| **GPU hardware** | Customer of NVIDIA (preferred partner); receives early allocations of H100, GB200, GB300, and next-gen Rubin before hyperscalers; AMD GPUs available on platform but secondary |
| **Facility developer/operator (owned)** | CoreWeave-designed and operated high-density AI data centers; 28+ US sites, expanding to UK, Norway, Sweden, Spain; new builds designed for 130kW+ liquid-cooled racks |
| **Facility operator (hosted)** | GPU deployment in Core Scientific-operated sites (500 MW contracted); CoreWeave owns GPUs, Core Scientific owns/operates the facility and power infrastructure |
| **Cooling infrastructure** | Liquid cooling built in from foundation; Vertiv CoolChip CDUs at newest facilities; no reliance on legacy air-cooled retrofit |
| **Cloud platform** | CoreWeave Cloud — GPU instances (H100, GB200, GB300, AMD MI300x) billed hourly/on-demand or long-term contract; workload orchestration layer |
| **Network** | NVIDIA InfiniBand fabric within clusters; low-latency interconnect for distributed AI training |
| **Anchor customers** | OpenAI ($22.4B committed), Meta ($14.2B), Microsoft (~70% of 2024 revenue); NVIDIA (buys unused capacity at $6.3B commitment) |
| **Debt structure** | GPU-asset-backed term loan facilities ($8.5B DDTL 4.0, investment-grade rated A3); Senior Notes ($1.75B at 9%); convertible notes ($2.25B at 1.75%) |

**⚑ Microsoft revenue concentration:** Microsoft represented approximately 62% of FY2024 revenue and ~70% of Q2 2025 revenue. This is single-customer concentration at a level that makes CoreWeave's near-term financials almost entirely a function of Microsoft's AI infrastructure spend trajectory. Microsoft has its own GPU infrastructure (Azure), its own NVIDIA allocations, and its own data center buildout. If Microsoft reduces CoreWeave capacity purchases — due to improved direct NVIDIA access, Azure buildout completion, or budget reallocation — CoreWeave's revenue would fall sharply.

**⚑ NVIDIA dual dependency (supplier and customer):** CoreWeave is simultaneously NVIDIA's largest external GPU customer and one of its GPU compute customers (NVIDIA buys excess capacity). This creates a deeply intertwined relationship where NVIDIA's GPU production volumes, pricing, and allocation decisions directly determine CoreWeave's product availability and cost structure. The $6.3B NVIDIA capacity purchase agreement provides revenue floor insurance but does not address the supplier-side concentration: CoreWeave's product is NVIDIA GPUs. An alternative GPU architecture gaining traction (AMD, Google TPU, custom ASIC proliferation) that shifted AI training workloads away from NVIDIA GPUs would simultaneously hit CoreWeave's product supply and customer demand.

**⚑ GPU depreciation vs. debt duration mismatch:** CoreWeave's debt is collateralized by GPU hardware that depreciates on a 3–5 year cycle (GPU generations: H100 → GB200 → GB300 → Rubin). The debt facilities extend to 2031–2032. If AI compute shifts to the next GPU generation faster than the debt amortizes, or if GPU prices decline materially (due to increased supply or reduced demand), the collateral value supporting CoreWeave's debt deteriorates faster than the debt is paid down. This is the core structural risk identified in short-seller research (Kerrisdale Capital, September 2025).

**⚑ Power constraint as scaling limiter:** CoreWeave CEO Michael Intrator has explicitly identified power availability as the primary constraint on CoreWeave's expansion. The company's $30–35B 2026 CapEx plan is partially limited by how much power capacity it can secure. Grid interconnection queues in most US markets are multi-year; CoreWeave's strategy of using Core Scientific's existing power infrastructure (already interconnected) is one response to this constraint. European expansion into Norway and Sweden targets hydropower-rich markets specifically because power is more available and renewable.

## Claim Verification

### Claim: CoreWeave is "the largest AI GPU cloud provider" / leading neocloud
**Status:** Directionally accurate in the neocloud category; requires context about the category definition

**Supporting:**
- Revenue ($5.1B estimated FY2025) and backlog ($66.8B) substantially exceed Lambda Labs, Together AI, and other neocloud competitors
- 28+ US data centers and multi-billion dollar European expansion represent the largest neocloud physical footprint
- NVIDIA's $2B direct equity investment and preferred partner status are consistent with CoreWeave being NVIDIA's primary external GPU deployment vehicle

**Refuting / questioning:**
- "Largest AI GPU cloud" depends on whether AWS, Azure, and GCP are included — they are all larger by GPU capacity in absolute terms; CoreWeave is the largest *specialized* neocloud, not the largest GPU cloud operator overall
- The neocloud category is relatively new; competitive dynamics with hyperscalers building dedicated AI infrastructure divisions are evolving rapidly

**Summary:** Accurate within the neocloud / specialized AI cloud category. Not the largest GPU cloud operator in absolute terms when hyperscalers are included.

### Claim: 130kW+ rack density support; NVIDIA GB300 NVL72 racks at ~140kW
**Status:** Technically credible; NVIDIA GB300 NVL72 thermal envelope is independently specified

**Supporting:**
- NVIDIA GB300 NVL72 system specifications are publicly available; full-load power draw of ~140kW is consistent with the NVIDIA specification
- Vertiv CoolChip CDU specifications (121kW liquid-to-liquid rejection, ASHRAE W5 compatible) are independently verifiable product specs
- Building new data centers around liquid cooling is a design choice — not a marketing claim subject to operational variation in the way cooling efficiency claims are
- Dell and CoreWeave showcased the first NVIDIA GB300 NVL72 rack deployment, confirming actual hardware is being installed at this density ([ServeTheHome](https://www.servethehome.com/dell-and-coreweave-show-off-first-nvidia-gb300-nvl72-rack/))

**Refuting / questioning:**
- "130kW+ rack support" describes the facility design envelope, not average deployed density; actual average facility density across CoreWeave's full portfolio (which includes older, lower-density sites) will be lower than the design maximum of newest facilities
- Heat rejection at 130kW+ per rack requires facility-level heat rejection infrastructure (dry coolers or chillers) that must be sized appropriately; PUE at high ambient temperatures in non-coastal sites has not been independently published

**Summary:** The density claims are technically accurate for the design envelope of newest facilities. The portfolio-wide average density is lower. The heat rejection infrastructure claim is credible but PUE performance at extreme ambient conditions has not been published.

### Claim: $66.8B revenue backlog (as of December 31, 2025)
**Status:** Reported as contracted backlog in public earnings; realizability and timing are uncertain

**Supporting:**
- $66.8B backlog figure is from CoreWeave's public earnings reporting (Q3 2025 earnings, November 2025); consistent with OpenAI ~$22.4B and Meta ~$14.2B disclosed contract values from S-1
- Backlog is contractually committed revenue, not pipeline — these are executed agreements, not LOIs

**Refuting / questioning:**
- "Backlog" realizability depends on customer ability and willingness to take and pay for contracted capacity; customer cancellation provisions, force majeure clauses, and financial health of counterparties (particularly AI startups) are not fully disclosed
- OpenAI's financial trajectory is a backlog concentration risk — OpenAI's ability to deploy and pay for ~$22.4B of committed compute depends on OpenAI's ongoing funding and business model success
- Backlog revenue recognition is spread over multi-year periods; near-term realized revenue is a fraction of total backlog

**Summary:** The $66.8B figure is from audited financial reporting and reflects executed contracts, not pipeline. Near-term realizability risk exists around customer financial health and capacity deployment timing.

### Claim: GPU-backed debt receives investment-grade rating (first time for HPC assets)
**Status:** Confirmed by S&P Global Ratings and Moody's (A3)

**Supporting:**
- S&P Global Ratings published analysis of CoreWeave's $2.25B senior unsecured notes
- Moody's A3 rating for the DDTL 4.0 facility is independently reported and consistent with investment-grade rating criteria
- The "first HPC-asset-backed loan to receive investment-grade" claim has not been contradicted by any published analysis

**Refuting / questioning:**
- Investment-grade ratings on GPU-backed debt are novel and reflect current conditions (GPU scarcity, high contracted demand, NVIDIA preferential relationship). These conditions may not persist through 2031–2032 debt maturities
- GPU depreciation risk within debt facilities is the core concern of short-sellers; Kerrisdale Capital's September 2025 analysis argued that GPU collateral depreciation undermines the investment-grade rating thesis over the full term

**Summary:** The investment-grade rating is confirmed. The longer-term sustainability of that rating as GPUs depreciate and the compute landscape evolves is a legitimate open question.

## Sources

- [CoreWeave — coreweave.com](https://www.coreweave.com/)
- [CoreWeave S-1 Filing (February 2025) — SEC EDGAR](https://www.sec.gov/Archives/edgar/data/1769628/000119312525044231/d899798ds1.htm)
- [CoreWeave Q3 2025 10-Q — SEC EDGAR](https://www.sec.gov/Archives/edgar/data/1769628/000176962825000062/crwv-20250930.htm)
- [NVIDIA and CoreWeave Strengthen Collaboration — NVIDIA Newsroom (January 2026)](https://nvidianews.nvidia.com/news/nvidia-and-coreweave-strengthen-collaboration-to-accelerate-buildout-of-ai-factories)
- [CoreWeave and NVIDIA $6.3B Capacity Deal — datacenters.com (September 2025)](https://www.datacenters.com/news/coreweave-nvidia-s-6-3b-capacity-deal)
- [CoreWeave Revenue Up 420% YoY — Data Center Dynamics (November 2025)](https://www.datacenterdynamics.com/en/news/coreweaves-revenue-up-420-yoy-in-first-earnings-call-since-ipo/)
- [CoreWeave Aims to Add 5GW by 2030; 2026 CapEx to Double — Data Center Dynamics](https://www.datacenterdynamics.com/en/news/coreweave-aims-to-add-5gw-more-data-center-capacity-by-2030-anticipates-capex-in-2026-to-double/)
- [Core Scientific 500 MW Final Option Exercise — BusinessWire (October 2024)](https://www.businesswire.com/news/home/20241022927349/en/Core-Scientific-Announces-Exercise-of-Final-Contract-Option-by-CoreWeave)
- [Microsoft Signs Multi-Billion Dollar Deal with CoreWeave — CNBC (June 2023)](https://www.cnbc.com/2023/06/01/microsoft-inks-deal-with-coreweave-to-meet-openai-cloud-demand.html)
- [CoreWeave IPO: S-1 Breakdown — MostlyMetrics](https://www.mostlymetrics.com/p/coreweave-ipo-s1-breakdown)
- [CoreWeave $2.2B European Expansion — PR Newswire (June 2024)](https://www.prnewswire.com/news-releases/coreweave-announces-significant-european-expansion-commits-an-incremental-2-2-billion-to-meet-surging-demand-for-ai-infrastructure-in-the-region-302164149.html)
- [CoreWeave's First UK Data Centers Live — TechCrunch (January 2025)](https://techcrunch.com/2025/01/13/coreweaves-first-international-data-centers-are-now-live-in-the-uk/)
- [CoreWeave $6B Lancaster, PA Campus — CoreWeave Investor Relations](https://investors.coreweave.com/news/news-details/2025/CoreWeave-Announces-Multi-Billion-Dollar-Commitment-to-AI-Infrastructure-in-Pennsylvania/default.aspx)
- [Dell and CoreWeave First NVIDIA GB300 NVL72 Rack — ServeTheHome](https://www.servethehome.com/dell-and-coreweave-show-off-first-nvidia-gb300-nvl72-rack/)
- [When Growth Runs on Debt: CoreWeave Case Study — Level Headed Investing](https://www.levelheadedinvesting.com/p/when-growth-runs-on-debt-the-coreweave-case-study)
- [CoreWeave Data Center Locations — dgtlinfra.com](https://dgtlinfra.com/coreweave-data-center-locations/)
- [Kerrisdale Capital — CoreWeave Short Report (September 2025)](https://www.kerrisdalecap.com/wp-content/uploads/2025/09/Kerrisdale-CoreWeave.pdf)
- [CoreWeave — Wikipedia](https://en.wikipedia.org/wiki/CoreWeave)
