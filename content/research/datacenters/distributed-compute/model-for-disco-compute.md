---
title: "Model for DisCo Compute"
date: 2026-07-18
lastmod: 2026-07-19
draft: false
description: "Engineering and cost model for a self-contained, liquid-cooled, battery-buffered residential inference unit (DisCo — distributed colocation) sharing a Texas home's 200A service, replicating the Span XFRA offering with currently purchasable hardware; includes solar-augmented variants with 40–50 kWh storage."
research_area: "datacenters/distributed-compute"
source_urls:
  - "https://www.nvidia.com/en-us/data-center/rtx-pro-6000-blackwell-server-edition/"
  - "https://www.tomshardware.com/pc-components/gpus/nvidia-raises-rtx-pro-6000-blackwell-gpu-pricing-to-usd13-250-55-percent-increase-over-msrp-in-a-years-time"
  - "https://www.choosetexaspower.org/energy-resources/average-electricity-usage/"
  - "https://www.globenewswire.com/news-release/2026/05/12/3292920/0/en/mojave-energy-systems-launches-aquadry.html"
  - "https://developer.nvidia.com/blog/deploying-nvidia-h200-nvl-at-scale-with-new-enterprise-reference-architecture/"
  - "https://jarvislabs.ai/blog/h200-price"
  - "https://www.hpcwire.com/2025/09/25/microfluidics-offers-3x-better-cooling-than-cold-plates-microsoft-says/"
  - "https://jetcool.com/smartplate-system/"
  - "https://journals.plos.org/water/article?id=10.1371%2Fjournal.pwat.0000133"
last_reviewed: 2026-07-19
stale_after_days: 90
related:
  - "datacenters/distributed-compute/span.md"
  - "datacenters/distributed-compute/_index.md"
  - "energy/batteries/base-power.md"
  - "atmospheric-water-generation/uravu-labs.md"
  - "atmospheric-water-generation/mof-801.md"
  - "atmospheric-water-generation/atoco.md"
  - "datacenters/cooling/mojave-energy-systems.md"
  - "datacenters/cooling/blue-frontier.md"
  - "datacenters/cooling/corintis.md"
  - "datacenters/cooling/liquid-cooling-interconnects.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

> **Note on entry type:** This is a working engineering/cost model, not a company profile. Unless a figure is tied to a cited source, every number below is a **planning estimate** intended for scenario comparison, not a quote. Component prices move quickly (the anchor GPU rose 55% in 16 months).

## Summary

This model tests what can be built today, with purchasable hardware, to replicate [Span]({{< relref "span.md" >}})'s XFRA offering: a self-contained, liquid-cooled AI inference unit deployed at Texas homes, sharing the home's standard 200A electrical service without overload risk during summer air-conditioning peaks. The design point that emerges is an 8-GPU RTX PRO 6000 Blackwell Server Edition unit drawing ~6.1 kW at the wall on a 40A/240V branch circuit, buffered by a 45 kWh battery (40–50 kWh class), at an estimated build-plus-install cost of **\~$187k retail / ~$136k at fleet volume**, hosting models up to ~405B parameters at FP8 and producing tokens at an estimated **$0.26–0.38 per million** at ideal utilization. An iso-power 8× H200 NVL variant (§9) matches the D8's wall draw on the same 40A circuit, needs ~1.7× its throughput to match cost per token, and is bought for frontier-model reach (1.1 TB VRAM, NVLink) rather than cheaper tokens; §8 explodes the balance-of-system BOM and flags what must be engineered versus bought; §13 models waste-heat atmospheric water generation to potable standard, which produces ~50–170 L/day depending on absolute humidity but never beats municipal water on cost.

## 1. Power Envelope: What a Texas Home Can Spare

A 200A/240V service is 48 kW nominal; NEC continuous-load rules (80%) cap sustained draw at **38.4 kW**. The compute unit is a continuous load, so it must fit inside the gap between that ceiling and the home's own summer peak — with margin, because summer peaks in Texas are AC-driven and coincident across the neighborhood.

Average monthly usage by home size ([Choose Texas Power](https://www.choosetexaspower.org/energy-resources/average-electricity-usage/), 2020–2024 marketplace data; peak-kW column is a derived estimate):

| Home size | Summer monthly kWh (est.) | Est. summer peak demand | Headroom vs. 38.4 kW ceiling (25% margin on peak) | Qualifies for |
|---|---|---|---|---|
| <1,500 sq ft | ~1,100–1,400 | ~6 kW | ~30.9 kW | Any unit size |
| 1,500–2,500 sq ft | ~1,400–2,000 | ~9 kW | ~27.2 kW | Any unit size |
| 2,500–3,500 sq ft | ~2,200–2,600 | ~12 kW | ~23.4 kW | Any unit size |
| >3,500 sq ft, all-electric | ~2,800+ | ~16 kW | ~18.4 kW | D4/D6 only (see §7 caveat) |

**The optimal host is not the biggest house.** It is a small-to-mid, newer, well-insulated home with gas heat/appliances, no EV charger (or a managed one), and 200A service — maximum service capacity relative to its own load. The practical qualification gate is not measured demand but the **NEC 220.83 calculated load** the permitting authority applies: large all-electric homes with EV chargers can calculate to 150A+, leaving too little calculated headroom for a 40A continuous branch circuit even though measured headroom exists. Assume a meaningful fraction of homes (plausibly 30–50%, unverified estimate) fail qualification on calculated load, panel condition, or siting.

## 2. GPU Options

Datacenter-class PCIe cards compared (specs from [NVIDIA](https://www.nvidia.com/en-us/data-center/rtx-pro-6000-blackwell-server-edition/) for RTX PRO 6000 SE; others are search-derived estimates):

| GPU | TDP | Memory | FP8 dense | Street price (est.) | $/GB VRAM | Notes |
|---|---|---|---|---|---|---|
| **RTX PRO 6000 Blackwell SE** | 600W (config.) | 96 GB GDDR7, 1.6 TB/s | ~1 PFLOPS (2 PFLOPS w/ sparsity) | ~$13,250–15,000 | ~$150 | Span's actual XFRA silicon; liquid SKU is **single-slot** |
| H200 NVL | 450–600W (config.) | 141 GB HBM3e, 4.8 TB/s | ~1.67 PFLOPS dense | ~$30,000–35,000 | ~$230 | 3× memory bandwidth; NVLink bridge 2–4 way |
| H100 NVL | 400W | 94 GB HBM3, 3.9 TB/s | ~1.6 PFLOPS w/ sparsity | ~$25,000–30,000 | ~$290 | Prior gen; poor value vs. H200 NVL now |
| L40S | 350W | 48 GB GDDR6, 864 GB/s | ~0.7 PFLOPS w/ sparsity | ~$7,000–8,000 | ~$155 | More cards per kW but small VRAM fragments models |

**Selection: RTX PRO 6000 Blackwell SE.** Best $/GB and $/FP8-FLOP of the set, matches Span's own choice, and the liquid-cooled variant's single-slot FHXL form factor is what makes an 8-GPU board layout physically possible. H200 NVL is the upgrade path when the workload is large-model, long-context inference where HBM bandwidth dominates — an iso-power 8× H200 NVL variant is compared apples-to-apples in §9. H100 NVL is dominated by H200 NVL at similar power. L40S maximizes card count per kW but 48 GB fragments large models across too many PCIe hops.

## 3. Unit Configurations

Wall draw = (GPUs + CPU + platform + pumps) / 94% PSU efficiency + dry-cooler fans. Breaker sized so continuous draw ≤ 80% of rating.

| Config | GPUs | Total VRAM | IT load | Wall draw | Branch circuit | 45 kWh battery ride-through |
|---|---|---|---|---|---|---|
| D4 | 4× RTX PRO 6000 | 384 GB | 2.9 kW | ~3.3 kW | 20A @ 240V | ~13.5 h |
| D6 | 6× RTX PRO 6000 | 576 GB | 4.1 kW | ~4.7 kW | 25–30A @ 240V | ~9.7 h |
| **D8 (design point)** | 8× RTX PRO 6000 | 768 GB | 5.4 kW | ~6.1 kW | 40A @ 240V | ~7.3 h |
| H4 | 4× H200 NVL | 564 GB | 2.9 kW | ~3.3 kW | 20A @ 240V | ~13.5 h |
| H8 (§9) | 8× H200 NVL @ 600W | 1,128 GB | 5.4 kW | ~6.1 kW | 40A @ 240V | ~7.3 h |
| H8-eco (§9) | 8× H200 NVL @ 450W | 1,128 GB | 4.2 kW | ~4.8 kW | 30A @ 240V | ~9.4 h |

**Battery-buffered power strategy.** The unit runs at constant wall draw off-peak. During the ERCOT summer peak window (~3–7 p.m.), the orchestrator drops grid draw to zero and runs the unit from the battery — the home keeps its full 200A service exactly when the AC needs it, and the compute never throttles. The standard pack is **45 kWh (40–50 kWh class)** across all configs: a Powerwall 3 + three expansions (13.5 kWh modules, ~$998/kWh installed per EnergySage 2026 data) or a ~45 kWh EG4-class LFP stack (\~$600–800/kWh installed). That covers the full 4-hour peak window for every config with margin (7.3h ride-through even on D8), leaves surplus capacity for arbitrage/ancillary services, and doubles as a UPS. §10 examines adding rooftop solar on top of this storage.

## 4. Cooling

D8 rejects ~5.4 kW of heat continuously into 40–45°C Texas summer ambient.

| Approach | Est. CAPEX (D8) | Pros | Cons |
|---|---|---|---|
| **Direct-to-chip loop (selected)** | ~$6,000 retail | Liquid SE cards ship cold-plated; 3–5× cheaper than immersion; serviceable; 30–45°C coolant tolerates 45°C ambient with a properly sized dry cooler | Fittings/leak points; pump is a single point of failure (dual pumps specified) |
| Single-phase immersion | ~$14,000 retail | Sealed, silent, dust/vandal/weather tolerant — attractive for an unattended outdoor pad | Dielectric fluid is a major line item (hundreds of $/gal); heavy (pad load); messy service; still needs an external heat rejection loop |

Direct-to-chip wins on cost and serviceability for a fleet product; immersion is worth revisiting if field failure data shows enclosure ingress or acoustic complaints dominate. Heat rejection is a ~6 kW dry cooler (roughly a 2-ton condenser footprint) at ~15°C approach; fan noise at property lines (~50 dBA class) is a deployment constraint to verify against local ordinance.

**4.1 The Loop, Component by Component**

The full chain: GPU/CPU cold plates → flexible EPDM hose with dry-break quick disconnects → chassis manifold → CDU (pumps, plate heat exchanger, reservoir, sensors) → insulated line set → outdoor dry cooler. Vendors below are representative, not exhaustive; see [Liquid Cooling Interconnects]({{< relref "../cooling/liquid-cooling-interconnects.md" >}}) for the full connector landscape.

| Component | Spec at D8 scale | Who makes it | Est. retail | Notes |
|---|---|---|---|---|
| GPU cold plates | Factory-fitted on RTX PRO 6000 SE liquid SKU | NVIDIA/OEM (built-in) | in GPU price | The reason the liquid SKU was selected |
| CPU cold plate | 280W EPYC SP5 | CoolIT, Boyd, JetCool, Corintis | $150–400 | Commodity part |
| Quick disconnects | ~20× OCP UQD04 (1/4") dry-break | Stäubli, CPC (Everis), Danfoss, Parker | $1,200–2,500 | Non-negotiable for field service; no drips in a homeowner's yard |
| Chassis manifold | 8+1 branch supply/return log | CoolIT/Motivair rack manifolds (oversized) or custom stainless weldment | $500–1,500 | Rack manifolds are 42U-scale — this is a semi-custom part |
| CDU / pump module | ~6 kW, 15–25 L/min, dual redundant pumps, PG25-rated | **Market gap** — smallest commercial CDUs are ~30 kW rack-scale (Eaton 10U L2A ~32 kW, Motivair 4U in-rack, JetCool SmartSense, DCX, CoolIT CHx) | $3,000–8,000 (adapted) or custom | See build-vs-buy, §8 |
| Coolant | ~40–60 L PG25 (25% propylene glycol + inhibitors) | Dow (Dowfrost), Koolance-class | $300–500 | Glycol for freeze events (Uri) even in Texas |
| Dry cooler | 6–8 kW @ 15°C approach, EC fans, optional adiabatic spray kit | Güntner, Kelvion, Alfa Laval, Modine | $2,000–4,000 | EC fans for noise-throttled night operation |
| Leak detection | Rope sensor around chassis floor + flow/pressure/ΔT sensors, auto-shutoff solenoid | TTK, RLE Technologies (sensors); loop controller custom | $400–800 | Ties into fleet telemetry; a leak alarm is a truck roll, not a flood |
| Line set + insulation | ~2× 15–25 ft insulated EPDM/PEX to pad edge | HVAC commodity | $300–600 | Below-dew-point operation must be avoided or condensation forms on lines |

Two topology choices worth recording: a **single loop** (cold plates straight to dry cooler, one fluid) deletes the CDU heat exchanger and its ~2–3°C penalty but puts the full loop volume outdoors through Texas temperature swings; a **two-loop** design (CDU with plate HX isolating a small indoor IT loop from the outdoor glycol loop) is standard datacenter practice, isolates the GPUs from outdoor fluid quality, and is what the heat-reuse tie-ins in §12 want to tap. The model assumes two-loop.

**4.2 Microfluidic Cold Plates: Commercial Status and What They Buy**

Short answer: **yes, commercially available today as drop-in cold plates — but the win at DisCo scale is loop temperature, not capacity.**

Two commercial paths exist. [Corintis]({{< relref "../cooling/corintis.md" >}}) sells drop-in microfluidic copper cold plates (AI-optimized ~100 µm channel topologies; 10,000+ shipped, ramping toward ~1M/yr capacity by end-2026, with Microsoft placing volume orders after their joint demo). [JetCool](https://jetcool.com/smartplate-system/) sells microconvective (jet-impingement) SmartPlate cold plates and self-contained chassis systems, UL-certified and shipping in Dell PowerEdge configurations, claiming ~15% average system power savings. The [Microsoft–Corintis results](https://www.hpcwire.com/2025/09/25/microfluidics-offers-3x-better-cooling-than-cold-plates-microsoft-says/) are the best public numbers: up to 3× better heat removal than conventional cold plates, 65% lower peak silicon ΔT, 55% lower pressure drop, and tolerance of meaningfully warmer coolant.

What that does for this system: the D8's constraint is not heat flux (600W across a big die is easy for any decent cold plate) but **rejecting 5.4 kW into 45°C ambient through a dry cooler the neighbors can't hear**. Microfluidics attacks that indirectly, by letting the loop run hotter at the same silicon temperature:

- **Raise supply coolant from ~40°C to ~55–60°C** and the dry-cooler approach at 45°C ambient roughly doubles — meaning a smaller, slower, quieter dry cooler, or full capacity on design days without adiabatic assist.
- **Hotter return (60–70°C) transforms the heat-reuse paths in §12**: it moves desiccant regeneration (Mojave's 43–82°C window, Uravu's 35–60°C) from the marginal bottom of the band to the comfortable middle, and makes DHW preheat hotter than the tank setpoint. The microfluidics dividend is collected in §13's water model, not in the GPU.
- Pump power and fan power drop modestly (tens of watts — real but not decisive).

The catch: the RTX PRO 6000 SE liquid SKU arrives with factory cold plates, and stripping them voids warranty/support — so gen-1 microfluidics insertion is realistically limited to the CPU plate and any fleet-built module. At fleet volume, specifying Corintis/JetCool plates through the system integrator at build time is plausible gen-2 work. **Verdict: commercial option — yes; gen-1 retrofit — no; the efficiency story is a hotter loop feeding the §12/§13 heat-reuse stack, worth pursuing at volume.**

## 5. Platform: Motherboard, CPU, Memory

The liquid-cooled single-slot cards allow all eight GPUs on one board without PLX switches:

- **Motherboard:** ASRock Rack **GENOAD8X-2T** (SP5, 7× PCIe 5.0 x16) — seven slots direct; the eighth GPU rides a x16 riser off an MCIO port, or step up to a Supermicro H13/H14 GPU server board. Single-socket EPYC provides 128 PCIe 5.0 lanes — the reason EPYC owns this niche.
- **CPU:** AMD EPYC 9354P (32C, 280W) — inference hosts are GPU-bound; cores mostly feed tokenization, batching, and network.
- **System memory:** **768 GB DDR5 RDIMM (12× 64 GB)** — sized 1:1 with aggregate VRAM so any hosted model can be staged/hot-swapped from RAM; 1.5× (1.15 TB) if model-swap agility matters more than cost.
- **Storage:** 2× 7.68 TB NVMe U.2 (model library + OS, RAID1).
- **PSU:** 2× 3.2 kW titanium CRPS, redundant; 240V input.

## 6. Cost Model (D8 design point)

Retail = buy-it-today street pricing; Volume = estimated fleet pricing (~25% off, unverified estimate). GPU price anchored to [NVIDIA marketplace/Newegg listings via Tom's Hardware](https://www.tomshardware.com/pc-components/gpus/nvidia-raises-rtx-pro-6000-blackwell-gpu-pricing-to-usd13-250-55-percent-increase-over-msrp-in-a-years-time); all other line items are planning estimates.

| Line item | Retail | % | Volume | % |
|---|---|---|---|---|
| 8× RTX PRO 6000 Blackwell SE (liquid) | $116,000 | 62.1% | $88,000 | 64.8% |
| Battery: 45 kWh LFP + hybrid inverter | $35,000 | 18.7% | $22,500 | 16.6% |
| Installation (pad, 40A subpanel, permits, labor, commissioning) | $6,500 | 3.5% | $4,500 | 3.3% |
| Cooling: D2C loop, CDU, manifolds, dry cooler | $6,000 | 3.2% | $4,200 | 3.1% |
| Vandal-resistant pad-mount enclosure (NEMA 3R, steel, locked, alarmed) | $5,000 | 2.7% | $3,200 | 2.4% |
| RAM: 768 GB DDR5 RDIMM | $4,600 | 2.5% | $3,400 | 2.5% |
| Orchestration: smart panel / CT metering / remote mgmt controller | $4,000 | 2.1% | $2,800 | 2.1% |
| CPU: EPYC 9354P | $2,800 | 1.5% | $2,100 | 1.5% |
| PSUs: 2× 3.2 kW titanium | $1,800 | 1.0% | $1,300 | 1.0% |
| Storage: 2× 7.68 TB NVMe | $1,700 | 0.9% | $1,300 | 1.0% |
| Motherboard: GENOAD8X-2T | $1,400 | 0.7% | $1,050 | 0.8% |
| Chassis, risers, cabling | $1,200 | 0.6% | $900 | 0.7% |
| Networking: 25GbE NIC, router, fiber CPE | $700 | 0.4% | $500 | 0.4% |
| **Total** | **$186,700** | 100% | **$135,750** | 100% |

```mermaid
pie showData title D8 unit cost allocation (retail, $186.7k)
    "GPUs (8x RTX PRO 6000)" : 116000
    "Battery 45 kWh + inverter" : 35000
    "Compute platform (CPU/MB/RAM/stor/PSU/chassis/net)" : 14200
    "Installation" : 6500
    "Cooling (D2C + dry cooler)" : 6000
    "Enclosure" : 5000
    "Orchestration/metering" : 4000
```

**Justification of the allocation.** GPUs are ~62–65% of the build regardless of pricing tier, which is why the GPU choice (§2) dominates every other engineering decision — a 10% GPU discount is worth more than eliminating the enclosure entirely. The 45 kWh battery is the second-largest item at ~17–19% and is the price of the "never threatens the AC" guarantee plus surplus capacity for arbitrage; a curtailment-only (Span-style orchestrated throttling) variant deletes $35k/$22.5k but reintroduces throttling during exactly the hours ERCOT prices and grid stress peak. Everything else — the entire computer around the GPUs — is under 10% of the system.

```mermaid
flowchart LR
    G[Grid meter 200A] --> SP[Smart panel / orchestrator]
    SP --> H[House loads incl. AC]
    SP --> B40[40A branch circuit]
    B40 --> INV[Hybrid inverter]
    BAT[45 kWh LFP battery] <--> INV
    INV --> PSU[2x 3.2 kW PSU]
    PSU --> IT[EPYC host + 8x RTX PRO 6000]
    IT --> CDU[CDU / pumps]
    CDU --> DC[Outdoor dry cooler ~6 kW]
    SP -. "peak window: grid draw to 0" .-> INV
```

**Installation and enclosure.** Texas electrician rates run ~$85–125/hr; a subpanel install is typically $500–1,750 before trenching, so the $6,500 retail line assumes: concrete pad, 40A/240V branch circuit with disconnect, permit and inspection, crane-less two-person set, and commissioning. The enclosure is a pad-mounted steel telecom-style cabinet (NEMA 3R minimum, 4X if coastal), three-point locking, tamper/tilt alarm, and a fenced or anchored footprint — the same class of hardware utilities use for pad transformers, which have survived decades of public siting.

## 7. What It Can Host (FP8/INT8) and Token Economics

768 GB of aggregate VRAM on the D8, FP8 ≈ 1 byte/param:

| Model | Precision | Weights | GPUs used | Fits? | Serving layout | Est. agg. tok/s† |
|---|---|---|---|---|---|---|
| Llama 3.3 70B | FP8 | ~70 GB | 1 (tight) or 2 | Yes | 4× two-GPU replicas — the workhorse config | ~5,000 (anchor) |
| GPT-OSS 120B | MXFP4/INT8 | ~65–120 GB | 2 | Yes | 4 replicas | ~5,000–6,500 (BW-bound) |
| Qwen3 235B (MoE) | FP8 | ~235 GB | 4 | Yes | 2 replicas | ~4,000–7,000 |
| Llama 3.1 405B | FP8 | ~405 GB | 8 (TP8) | Yes, ~360 GB KV headroom | 1 instance | ~500–600 |
| DeepSeek-R1 671B | FP8/INT8 | ~671 GB | 8 | Marginal (~97 GB KV — short context only) | 1 instance | ~1,500–2,500 |
| DeepSeek-R1 671B | INT4 | ~336 GB | 6–8 | Yes | 1 instance, comfortable | ~2,500–3,500 |

† Unverified planning estimates: aggregate decode throughput at high concurrency, taken as the lower (binding) of two bounds. Compute bound: T_c = N_GPU × F_FP8 × MFU / (2 × P_active), with F_FP8 ≈ 1 PFLOPS/card dense and MFU ≈ 9% — calibrated so the 70B row reproduces the ~5,000 tok/s anchor used in the token economics below. Bandwidth bound: T_b = R × B × (MBU × BW_replica / W_bytes), with MBU ≈ 50%, BW = 1.6 TB/s/card, R = replicas, and B = concurrent sequences the replica's KV headroom sustains. Adjustments: MoE models use active parameters (P_active) with a ~0.7 routing-efficiency factor; PCIe tensor parallelism takes a ×0.6 (TP8) to ×0.8 (TP4) interconnect haircut.

**Token cost at ideal use.** Assumptions: 70B-class FP8 serving at high concurrency, ~5,000 aggregate tok/s across 4 replicas (extrapolated from published single-card Pro 6000 vLLM results of ~5,200–9,000 tok/s on 8–14B models and single-card 70B FP8 viability; unverified estimate), 90% utilization → **~389M tokens/day**. Energy: 147 kWh/day at $0.135/kWh ≈ $20/day. Volume CAPEX $135,750 amortized straight-line, $5/day maintenance/network allowance:

| Amortization | CAPEX/day | All-in cost per 1M tokens |
|---|---|---|
| 3 years | $124 | **~$0.38** |
| 4 years | $93 | **~$0.30** |
| 5 years | $74 | **~$0.26** |

Energy alone is only ~$0.05/M tokens — this is a CAPEX-dominated business, which is the economic logic of Span's subsidize-the-panel model.

**Utilization sensitivity.** Because ~85% of daily cost is fixed CAPEX, cost per token is nearly inversely proportional to utilization. Modeling wall draw as ~1.5 kW idle + load-proportional to 6.1 kW full (so energy falls somewhat at low duty), D8 volume build:

| Utilization | Energy/day | Tokens/day | $/M tokens (3yr) | $/M tokens (5yr) | Daily cost (3yr) |
|---|---|---|---|---|---|
| 40% | 80 kWh ($10.9) | 173M | $0.81 | $0.52 | ~$140 |
| **60%** | 103 kWh ($13.9) | 259M | **$0.55** | **$0.36** | ~$143 |
| **80%** | 125 kWh ($16.9) | 346M | **$0.42** | **$0.28** | ~$146 |
| 90% (ideal) | 136 kWh ($18.4) | 389M | $0.38 | $0.25 | ~$147 |

Note the daily cost column barely moves (~$140–147) while output doubles — idle hardware costs almost as much as busy hardware. Against mid-2026 API pricing for 70B-class open models (roughly $0.60–0.90/M output tokens, unverified estimate): at 80% the unit clears a healthy margin, at 60% it still clears the low end of market pricing, and the **3-year breakeven sits at ~55% utilization** at a $0.60/M market price. On 5-year amortization even 60% utilization is comfortably economic. **Utilization, not hardware, is the whole game** — consistent with the subsection steering's warning that consumer-earnings claims in this space rest on utilization assumptions, not observed data — and it is why the monetization stack in §14 is designed around backfilling idle capacity.

## 8. Balance-of-System BOM and Build-vs-Buy

§6 aggregates everything around the compute box into single lines. This section explodes the **balance of system** — every subsystem outside the server itself — with vendor classes and planning-estimate pricing, then flags what can be bought versus what has to be engineered. All figures are retail planning estimates.

**8.1 Balance-of-System BOM (D8)**

| Subsystem | Item | Est. retail | Representative vendors |
|---|---|---|---|
| **Electrical** | 40A/240V 2-pole breaker, 8 AWG THHN run (~75 ft), conduit | $600 | Square D, Eaton |
| | Fused AC disconnect at pad + surge protection (Type 2 SPD) | $350 | Eaton, Siemens, Midnite |
| | 8-space NEMA 3R subpanel at pad | $400 | Square D QO |
| | Permits, inspection, licensed electrician labor | $2,500–4,000 | local |
| **Power/battery** | 45 kWh LFP rack battery (3× 15 kWh modules) | $18,000–27,000 | EG4, HomeGrid, Fortress; Powerwall 3 ×3.3 at premium |
| | 10–12 kW hybrid inverter/charger, UL 9540 listed w/ battery | $4,000–6,000 | Sol-Ark 12K, EG4 12000XP, Tesla |
| | Smart panel / CT metering / curtailment control | $3,500–4,500 | Span panel, Savant, Emporia + custom |
| **Cooling loop** | Full §4.1 stack (QDs, manifold, CDU, coolant, dry cooler, leak detection, line set) | $6,000–12,000 | see §4.1 |
| **Enclosure & civil** | Pad-mount steel cabinet, NEMA 3R/4X, 3-pt lock, tamper + tilt alarm | $3,500–5,000 | Saginaw, Hoffman/nVent, DDB Unlimited, telecom-surplus |
| | Concrete pad (~4×8 ft, 4–6"), anchors, trenching | $1,500–2,500 | local concrete |
| | Cabinet ventilation/filtration for battery + electronics bay (sealed IT bay is liquid-cooled) | $400–800 | nVent, Delta fans/filters |
| **Network & mgmt** | Router/firewall + LTE/5G out-of-band failover | $400–700 | Ubiquiti, Teltonika, Cradlepoint |
| | 25GbE NIC + fiber CPE interface | $300 | Intel/NVIDIA (used market) |
| | Remote power control (per-outlet switched PDU) + IP-KVM/BMC access | $400–600 | APC, Raritan; ASPEED BMC on board |
| **Safety & monitoring** | Smoke/heat sensor, cabinet door + tilt sensors, e-stop, camera | $500–900 | Ajax/commercial alarm parts |
| | Environmental telemetry (temps, humidity, flow, power metering) | $300–600 | Shelly Pro/industrial Modbus + custom controller |
| **Water/heat tie-ins (optional)** | Double-wall brazed-plate HX, 3-way diverting valve, DHW pump group | $2,000–3,500 | Alfa Laval, Caleffi, Taco, Grundfos |
| **Total balance-of-system** | | **~$45,000–70,000** | vs. ~$65,700 implied by the §6 aggregate lines — consistent |

**8.2 Build vs. Buy**

Straight off the market, no engineering beyond selection: GPUs/platform, battery modules and hybrid inverter (UL 9540 pairings), cold plates, UQD04 disconnects, dry cooler, cabinet, leak-detection sensors, network gear, DHW heat exchanger and valves.

**Design-it-yourself list** — the gaps where no product exists at this scale, ordered by how much they matter:

1. **Sub-10 kW residential CDU / pump module.** Commercial CDUs start at ~30 kW and assume a 19" rack and a facility tech. Needed: a compact dual-pump, dual-loop skid with PG25, potable-safe HX isolation, and quiet operation. Closest COTS starting points: Eaton's 10U liquid-to-air CDU (~32 kW class) or PC-watercooling-industrial hybrids. This is a genuine fleet-product engineering item — and the single most re-usable one across every DisCo variant.
2. **Power orchestration / EMS controller.** The §3 battery strategy (peak-window grid-zero, ERCOT signal response, §1 headroom enforcement, curtailment presented as scheduled availability to marketplaces) does not exist as a product. Span's software *is* this; replicating it is the hardest build in the project (see §14 software planes).
3. **Loop controller + safety interlocks.** Pump speed vs. ΔT, dry-cooler fan curves vs. noise windows, leak response (isolate, drain-down, alert), heat-reuse diverter priority logic (§12). PLC-class build (Codesys/ESPHome-industrial); nothing off-the-shelf integrates IT + hydronics + battery at this scale.
4. **Thermal/acoustic enclosure integration.** Cabinet is COTS; the layout (battery thermal envelope vs. Texas ambient, IT bay sealing, hose routing, service access, 50 dBA at property line) is custom mechanical engineering per SKU.
5. **Desiccant AWG regenerator module** (§13). Uravu builds MW-scale, Mojave builds air handlers; a ~5 kW(th) residential regenerator + contactor is a from-scratch prototype.
6. **Fleet telemetry, attestation, and trust plane** (§14) — software build.

Rule of thumb that falls out: **everything that touches water-to-chip or power-to-grid as a *system* must be designed; every component inside those systems can be bought.**

## 9. H200 NVL Variant: An Iso-Power, Apples-to-Apples Comparison

The scarce resource in this model is not budget — it is the **40A/240V continuous envelope (~6.1 kW at the wall)**. A fair comparison therefore holds wall power constant and asks what each architecture returns per watt-year. The H200 NVL is TDP-configurable from 450–600W ([NVIDIA H200](https://www.nvidia.com/en-us/data-center/h200/)), so eight cards at 600W present exactly the D8's IT load (5.4 kW) on the same breaker, battery, and cooling loop — a true iso-power swap.

**9.1 The Exotic-Hardware Tax**

The RTX PRO 6000 SE is a workstation-channel card with a factory liquid single-slot SKU; the H200 NVL is enterprise-channel silicon with real deployment baggage:

- **No factory liquid SKU.** H200 NVL ships only as a passive dual-slot FHFL card designed for server airflow ([NVIDIA's enterprise reference architecture](https://developer.nvidia.com/blog/deploying-nvidia-h200-nvl-at-scale-with-new-enterprise-reference-architecture/) is a 4U, high-static-pressure-fan chassis — an acoustic non-starter in a yard cabinet). Liquid operation means third-party cold-plate conversion (system integrators do this; strips warranty unless contracted through the SI), estimated **+$8,000–12,000** for 8 cards including plates and labor. Once converted the cards are effectively single-slot, so the 8-on-one-board layout survives.
- **NVLink bridges.** Eight cards form two 4-way NVLink domains via [4-way bridges](https://www.hpe.com/psnow/doc/PSN1014856854VNEN) (900 GB/s/GPU intra-domain, 1.8 TB/s bisection): ~**$4,000–5,000** for the bridge sets. Cross-domain traffic falls back to PCIe — model placement must respect the 2×4 topology.
- **Enterprise channel only.** No retail box: procurement via OEM/distributor with lead times, and 2026 supply for the high-memory Hopper part remains tight (AWS raised H200 instance pricing 15% in January 2026 per [Jarvis Labs' price tracking](https://jarvislabs.ai/blog/h200-price)). Street price ~$28,000–35,000/card.
- **Dual 12V-2×6/EPS cabling and higher transient spikes** than the workstation card — the 2× 3.2 kW PSU spec holds but with less margin at 600W×8.

**9.2 Iso-Power Configurations and Cost**

Same platform, battery, enclosure, and balance of system as §6 and §8 (non-GPU base $70.7k retail / $47.8k volume), plus bridges and conversion:

| Config | GPUs | VRAM (domains) | Aggregate HBM BW | IT / wall | Circuit | Total (retail / volume) |
|---|---|---|---|---|---|---|
| D8 (ref.) | 8× RTX PRO 6000 @ 600W | 768 GB (8× PCIe) | 12.8 TB/s | 5.4 / 6.1 kW | 40A | $186.7k / $135.8k |
| **H8** | 8× H200 NVL @ 600W | 1,128 GB (2× 564 GB NVLink) | 38.4 TB/s | 5.4 / 6.1 kW | 40A | ~$325.7k / ~$250.8k |
| H8-eco | 8× H200 NVL @ 450W | 1,128 GB (2× 564 GB NVLink) | 38.4 TB/s | 4.2 / 4.8 kW | 30A | ~$325.7k / ~$250.8k |

**H8-eco is the quietly interesting row.** Power-capping Hopper to 450W leaves HBM bandwidth untouched, and decode-heavy inference is bandwidth-bound — the cap costs ~10–20% on prefill-heavy work and almost nothing on decode throughput (planning estimate), while cutting wall power 21%, dropping to a 30A circuit, and stretching battery ride-through to ~9.4 h. Per unit of scarce power, a capped H200 is the efficiency king of this comparison.

**9.3 Model Menu at 1,128 GB**

Where the D8 is memory-*capacity* constrained, H8 is not — and NVLink TP4 inside each 564 GB domain removes the PCIe tensor-parallel penalty that throttles the D8 on big models:

| Model | Precision | Weights | Layout on H8 | vs. D8 | Est. agg. tok/s‡ |
|---|---|---|---|---|---|
| Llama 3.3 70B | FP8 | ~70 GB | **8 single-card replicas** (no TP at all; ~65 GB KV each) | D8 needs 2-GPU TP; H8 serves it per-card with huge batch KV | ~7,500–10,000 |
| Qwen3 235B (MoE) | FP8 | ~235 GB | 2 replicas (one per NVLink domain, TP4) | D8: 2 replicas over PCIe TP4 — H8 domain is NVLink-native | ~12,000–19,000 |
| Llama 3.1 405B | FP8 | ~405 GB | 1 replica in **one** domain (TP4, ~159 GB KV) — second domain free for other models | D8 needs all 8 GPUs over PCIe | ~700–900 (one domain) |
| DeepSeek-R1 671B | FP8 | ~671 GB | 1 instance across both domains (~450 GB KV headroom — full 128k contexts) | D8: marginal, short-context only | ~5,000–7,000 |
| 1T-class open MoE (Kimi-K2-class) | INT4 | ~550–600 GB | Comfortable across the two domains | Does not fit D8 at all | ~4,000–6,000 |

‡ Same two-bound method and calibration as the §7 table (MFU ≈ 9%, MBU ≈ 50%), substituting H200 NVL card constants — F_FP8 ≈ 1.67 PFLOPS dense, BW = 4.8 TB/s — with these interconnect adjustments: single-card replicas and NVLink TP4 within a 564 GB domain take no haircut (×1.0); models spanning both domains take ×0.6 for cross-domain traffic falling back to PCIe. The wide Qwen3 band reflects the compounding of NVLink TP4 (vs. D8's PCIe haircut) and abundant KV headroom, which lifts both bounds simultaneously; the 405B figure is one domain only, leaving the second domain free to serve other rows concurrently. All figures are unverified planning estimates.

**9.4 Per-Token Economics, Honestly**

Throughput calibration (planning estimates, same method as §7): on 70B-class FP8 serving, H200's 3× per-card bandwidth and single-card serving layout plausibly yield **1.5–2× the D8's aggregate tokens** (~7,500–10,000 tok/s vs. ~5,000); on 405B+ long-context work the gap widens (D8's PCIe TP8 decode is interconnect- and bandwidth-strangled). At 90% utilization, volume pricing, $0.135/kWh, $5/day maintenance:

| Scenario | Tokens/day | $/M tokens (3yr / 4yr / 5yr) |
|---|---|---|
| D8, 70B-class (ref.) | ~389M | $0.38 / $0.30 / $0.26 |
| H8 @ 1.0× D8 throughput (pessimistic) | ~389M | $0.65 / $0.51 / $0.42 |
| H8 @ 1.5× | ~583M | $0.44 / $0.34 / $0.28 |
| **H8 @ 1.7× (break-even)** | ~661M | **$0.38 / $0.30 / $0.25** |
| H8 @ 2.0× (bandwidth-bound best case) | ~778M | $0.33 / $0.25 / $0.21 |

**The break-even is ~1.7×:** H8 must sustain 1.7× the D8's system throughput just to match its cost per token, because its volume capex is ~1.85× ($250.8k vs. $135.8k). On commodity 70B serving that is the *top* of the plausible range — so the honest verdict is that **H200 does not buy cheaper commodity tokens; it buys model-class reach on the same 40A circuit**: 405B at full context, 671B FP8 comfortably, 1T-class MoE at all, plus single-card 70B serving simplicity. Choose H8 when the product is frontier-scale open models or long-context/latency-sensitive serving priced above commodity rates ($2–5/M-token classes); choose D8 when the product is bulk 70B–235B tokens. Model-selection rule: **if the roadmap's flagship model exceeds ~500 GB of weights+KV, the D8 can't follow — that, not $/token, is the H200's case.**

## 10. Solar-Augmented Options: 12 kW PV on the 45 kWh Base

Texas residential solar systems now average ~12 kW DC (largest in the US, driven by AC loads) at an installed cost of roughly **$2.20–2.85/W** in 2026; Texas yield is ~1,450–1,600 kWh/kW/yr (search-derived estimates; see Sources). Against the D8's 147 kWh/day appetite, a 12 kW array delivers ~49 kWh/day annual average and ~62 kWh/day in summer — **~32% annual / ~40% summer coverage** at 95% self-consumption (achievable because the standard 45 kWh battery absorbs essentially all midday surplus).

Scenario comparison, D8 design point (retail / volume; solar at $2.75/$2.00 per watt):

| Scenario | Added CAPEX (retail / volume) | Total (retail / volume) | Net grid energy | $/M tokens (3yr / 4yr / 5yr, volume) |
|---|---|---|---|---|
| **A** — baseline: 45 kWh battery, grid-only (§6) | — | $186.7k / $135.8k | 147 kWh/day | $0.38 / $0.30 / $0.26 |
| **B** — + 12 kW solar | +$33.0k / +$24.0k | $219.7k / $159.8k | ~100 kWh/day | $0.42 / $0.33 / $0.27 |
| **C** — as B, fleet-owned with ~30% ITC + MACRS (~45% net reduction on PV+storage, unverified estimate) | — | net ~$138.8k volume | ~100 kWh/day | $0.37 / $0.29 / $0.24 |

**The headline result is negative on pure token economics: solar does not pay for itself inside this model.** At $0.135/kWh, 12 kW of PV saves only ~$6.6/day of energy while adding ~$24–33k of CAPEX — and this is a CAPEX-dominated system (§7). Homeowner-priced solar (scenario B) makes tokens ~7–10% *more* expensive; only fleet-owned solar capturing the commercial 48E ITC and MACRS depreciation (scenario C) gets slightly below the grid-only baseline. Solar is not an energy-cost play here.

What the solar-augmented configuration actually buys:

- **Summer grid-zero operation.** Solar (62 kWh) + 45 kWh of storage lets the D8 run **grid-zero for ~17 of 24 hours** on a summer day — the unit disappears from the feeder during the entire stressed period, the strongest possible answer to the utility/AHJ overload objection and a qualification unlock for homes that fail the §1 calculated-load screen.
- **A near-off-grid D4.** The 4-GPU unit needs only ~80 kWh/day; 12 kW PV + 50 kWh storage covers ~77% of summer load and ~61% annually, with grid draw only in overnight tails. A D4 at a solar home adds almost no net annual load — the "infinite headroom" qualification case.
- **Price-spike hedge and islanding.** Retail energy exposure drops ~⅓; during Uri-class events the unit islands with the home rather than competing with it — the battery + inverter become a whole-home resilience asset that is part of the homeowner compensation story.
- **ERCOT arbitrage/ancillary capacity.** 45–50 kWh with only ~25 kWh committed to peak ride-through leaves ~20+ kWh/day for price arbitrage or ancillary services (unmodeled revenue; on volatile ERCOT days plausibly rivals the token-cost delta between scenarios A and B).
- **New-construction synergy.** On a Pulte-style build (Span's actual channel), solar, storage, smart panel, and interconnection agreement are installed once, together — the marginal orchestration and install lines in §6 shrink, and scenario C's tax treatment applies by default since the fleet owns the equipment.

**Verdict:** grid-only (A) remains the cost-per-token floor for retrofit deployments; solar-augmented (C) is the fleet configuration for new construction and for homes that can't otherwise qualify — bought for headroom, resilience, and grid-relations value rather than for the energy savings.

## 11. Secondary-Market GPU Options

The 2026 refresh cycle (hyperscalers moving to Blackwell/B300) is pushing large volumes of Ampere and early Hopper hardware onto the secondary market. Since DisCo's target workload is inference only, used datacenter GPUs are worth modeling. Street pricing (search-derived from [Hashrate Index](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/) and broker listings; wide bands, treat as indicative):

| Used part | Typical 2026 price | Memory | Inference-relevant limits |
|---|---|---|---|
| A100 80GB PCIe | ~$4,000–7,000 | 80 GB HBM2e, 2.0 TB/s | **No FP8** (Ampere): INT8/BF16 only; 300W |
| A100 80GB SXM4 (module) | ~$5,000–9,000 | 80 GB HBM2e | Requires HGX baseboard + host; 400W |
| H100 SXM5 (module) | ~$6,000–15,000 | 80 GB HBM3, 3.35 TB/s | FP8 yes; requires HGX baseboard; 700W |
| Complete used H100 HGX server | ~$150,000–180,000 | 640 GB | Turnkey but oversized pricing vs. parting out |

**NVLink supporting equipment — counted in all three budgets.** PCIe A100s interconnect only in bridged pairs (3× NVLink bridges per pair, ~$1,500 for four pairs; no switch involved, cross-pair traffic falls back to PCIe). SXM modules require an **HGX baseboard whose 6 (A100) or 4 (H100) integrated NVSwitch chips are part of the deal**: they add ~400–500W of continuous draw to the power budget, their heat lands in the same liquid loop (cold-plate kits must cover the switch ASICs, +\~$3,000–3,500 retrofit line), and the baseboard itself is a ~$10,000–15,000 used line item when parting out modules. External NVLink Switch appliances are multi-node equipment and are *not* required at single-unit scale — no rack switch line item beyond ordinary Ethernet.

Configurations on the same platform/enclosure base as §6, all with the standard 45 kWh battery (non-GPU base: $70.7k retail / $47.8k volume):

| Config | GPUs + fabric | Wall draw / breaker | Heat to loop | 45 kWh ride-through | Total (retail / volume) | Est. 70B-class throughput | $/M tok (3yr / 5yr, volume) |
|---|---|---|---|---|---|---|---|
| D8 (new, ref.) | 8× RTX PRO 6000 | 6.1 kW / 40A | 5.4 kW | ~7.3 h | $186.7k / $135.8k | ~5,000 tok/s | **$0.38 / $0.26** |
| U8P | 8× used A100 PCIe + bridges | 3.4 kW / 20A | 3.0 kW | ~13.2 h | $124.2k / $93.3k | ~2,000 tok/s (INT8) | $0.65 / $0.43 |
| U8S | used HGX A100 8× SXM4 (incl. 6× NVSwitch) | 4.9 kW / 30A | 4.3 kW | ~9.2 h | $136.2k / $100.8k | ~2,400 tok/s (INT8) | $0.60 / $0.41 |
| UH8 | used HGX H100 8× SXM5 (incl. 4× NVSwitch), $10k modules | 7.7 kW / 50A | 6.8 kW | ~5.8 h | $185.2k / $142.8k | ~4,200 tok/s (FP8) | $0.49 / $0.33 |
| UH8-low | same, $6k modules (bottom of range) | 7.7 kW / 50A | 6.8 kW | ~5.8 h | $153.2k / $110.8k | ~4,200 tok/s (FP8) | **$0.40 / $0.28** |

Throughput figures are unverified planning estimates scaled from the §7 baseline (H100 ≈ 0.85× Pro 6000 per card on FP8 serving; A100 ≈ 0.4× — Ampere pays twice, running INT8/BF16 without a transformer-engine FP8 path and with half the compute per watt).

**Verdict: cheap capacity, not cheap tokens — with one exception.** Used Ampere looks tempting on sticker but loses ~60–70% on $/M tokens against new Blackwell: token cost is driven by throughput per dollar *and per watt*, and a 2020 architecture without FP8 trails on both. Where used A100s do win decisively is **$/GB of VRAM** (\~$71–83/GB vs. ~$115/GB volume for the Pro 6000) — the right tool if the business is hosting many long-tail models warm, batch/offline inference, or capacity resale where utilization (not throughput) is the product. Used H100 HGX is the genuine opportunity: at the bottom of the current module price band (\~$6k) it comes within ~5–8% of the new-Blackwell token cost, keeps FP8 and a full 900 GB/s all-to-all NVSwitch fabric (better 405B-class TP8 serving than the PCIe-attached D8), at the price of a 50A circuit, ~25% more heat rejection, and a shorter (~5.8h) ride-through on the standard 45 kWh battery. Fleet risks unique to secondary sourcing: no warranty (self-insure ~2–4% annual failure allowance), provenance/firmware verification, HBM wear from training duty, and air-to-liquid retrofit labor at scale — none modeled above.

## 12. Waste-Heat Recovery: Hot Water, Space Heating, Dehumidification, and Water Generation

The D8 rejects ~5.4 kW continuously — **~130 kWh of thermal energy per day** already collected in a liquid loop at 45–55°C. That temperature is the key asset: it is directly usable, and there is commercial precedent — Qarnot (France) has sold compute-as-boiler since 2015 with water exiting at 65°C and ~95% heat capture; Heata (UK) mounts compute nodes on domestic hot water cylinders, saving households ~£250/yr; Deep Green heats swimming pools; UK Power Networks piloted residential compute-as-heating in 2025; and the EU's EnEfG requires new datacenters to utilize waste heat from 2026 (search-derived; see Sources).

**Path 1 — Domestic hot water (works everywhere, including Texas).** A double-wall brazed-plate heat exchanger (potable-water code requirement) tees the GPU return loop into a preheat tank ahead of the existing water heater; a 3-way diverting valve sends unneeded heat onward to the dry cooler. A typical household draws only ~12–15 kWh(th)/day for hot water, so DHW absorbs barely **10%** of the unit's output — but it does so year-round, displaces ~$1.60–2.00/day of resistance water heating (\~$600–700/yr), and the hardware adder is small: ~$2,000–3,500 retail for HX, valve, pump, and controls. On the homeowner-compensation ledger, "your water heating is free" is a concrete, legible benefit that costs the fleet almost nothing.

**Path 2 — Hydronic space heating (the cold-climate variant).** 5.4 kW is ~18,400 BTU/hr of continuous output — roughly a third to half of the design-day heating load of a well-insulated 2,000–2,500 sq ft home in a cold climate, and essentially all of its shoulder-season load. The 45–55°C loop matches low-temperature hydronic emitters directly (radiant floor at 35–45°C supply, modern panel radiators); legacy high-temp baseboard needs a small water-to-water heat pump boost (COP 5+ for a 45→65°C lift). Integration is a buffer tank plus either radiant loops or a hydronic air-handler coil. In a ~6,500 HDD climate the unit displaces an estimated 20–25 MWh(th)/yr — worth ~$2,700–3,400/yr against resistance heat or ~$800–1,200/yr against gas (unverified estimates). Cold climates also improve the cooling side: the dry cooler runs far below Texas design ambients, and winter grid peaks (heating-driven) complement the battery strategy.

**Path 3 — Desiccant dehumidification (the Texas-summer path).** In humid Texas (Houston, Gulf Coast, much of the Triangle), a large share of summer AC energy — commonly estimated at roughly a third of the load (unverified estimate) — goes to removing moisture (latent load), not lowering temperature. Desiccants strip that moisture directly, and the heat required to regenerate the desiccant is exactly what DisCo has in surplus. The temperature match is real and current: [Mojave Energy Systems]({{< relref "mojave-energy-systems.md" >}})' AquaDry (launched May 12, 2026; shipments late 2026) is a hydronic liquid-desiccant air handler explicitly designed to regenerate from **110–180°F (43–82°C) low-grade hot water** and marketed as waste-heat-compatible, with data centers named among target facilities — the DisCo loop's 45–55°C sits at the usable bottom of that band (hotter-loop operation improves regeneration margin). Supporting ecosystem: Mojave's ArctiDry DOAS claims 40–60% energy reduction and is in a DoD SERDP/ESTCP demonstration (see the [Mojave Energy Systems]({{< relref "mojave-energy-systems.md" >}}) entry for full detail); [Blue Frontier]({{< relref "blue-frontier.md" >}}) packages a related thermally-regenerated liquid-desiccant AC with built-in brine energy storage, though — unlike Mojave — with no disclosed data-center application as of this review; academic work puts optimal LiCl regeneration near [65°C](https://www.sciencedirect.com/science/article/abs/pii/S0140700719301367). Solid desiccant wheels typically want 60–120°C regeneration air — marginal for this loop; **liquid desiccant is the match**.

Indicative cost to bolt onto a DisCo host home (planning estimates — no residential-scale hydronic LD product exists yet; figures assume adapting the smallest commercial units or a purpose-built fleet module):

| Line item | Est. retail | Notes |
|---|---|---|
| Liquid-desiccant dehumidification air handler (smallest commercial class, ~300–500 CFM) | $8,000–15,000 | Commercial LD-DOAS units are 1,000+ CFM; residential scale would need a fleet-developed module |
| Hydronic tie-in: double-wall HX, pumps, 3-way valves | $1,500–2,500 | Shares the §12 Path-1 manifold |
| Ducting into home return plenum + controls integration | $2,000–4,000 | Ties to home thermostat/HVAC |
| **Total (retrofit)** | **~$12,000–21,000** | vs. ~$2,000–4,500 for a conventional 500–700W whole-house dehumidifier |

Operational concerns: LiCl/CaCl₂ solutions are chloride-corrosive (titanium or polymer heat exchangers, no carbon steel anywhere in the wetted path); desiccant carryover into supply air must be controlled (droplet eliminators); crystallization at high concentration if regeneration overruns; annual desiccant top-off; and the airflow integration means HVAC-contractor service calls, not IT service calls. The honest economics: displaced latent work is only ~1.5–2.5 kWh(e)/day of compressor energy (\~$0.20–0.35/day, summer only), so a retrofit never pays back on energy. The value is **peak coincidence**: removing latent load cuts the home's 4–7 p.m. AC draw by an estimated 0.5–1 kW exactly when the §1 headroom calculation binds — it buys qualification margin and feeder relief, which is fleet value, not homeowner savings. Plausible only as a fleet-developed module at new-construction scale.

**Path 4 — Atmospheric water generation (the on-brand speculative path).** The same liquid-desiccant chemistry pointed at water production instead of dry air. The directly relevant player is [Uravu Labs]({{< relref "uravu-labs.md" >}}), whose liquid desiccant regenerates at **35–60°C** — the DisCo loop is entirely inside that window — and whose Clausius platform claims up to 30,000 L of water per MW of IT load per day for datacenter deployments (company claim, unverified; see that entry's Claim Verification). Scaled naively to the D8's 5.4 kW of IT load, that is **~160 L/day**; a generic sorbent-energy estimate of 0.5–1.2 kWh(th)/L applied to the 130 kWh(th)/day stream gives a consistent ~110–260 L/day range (unverified estimates). MOF-based sorbents ([MOF-801]({{< relref "mof-801.md" >}}), regenerable on a ~40°C swing; [Atoco]({{< relref "atoco.md" >}}) commercially) are the other chemistry in-window.

Market benchmarks for what water-from-air costs today (search-derived; see Sources): Watergen's Genny (condensation-type, ~30 L/day residential) runs ~250 Wh(e)/L at an estimated $0.07–0.15/L; Aquaria Hydropack-class whole-home units run 245–288 Wh(e)/L; SOURCE hydropanels (solar-sorbent) cost ~$2,500–3,000/panel installed for 3–5 L/day. A DisCo-attached sorbent stage has no per-liter energy cost at all — the heat is free — but there is **no off-the-shelf waste-heat-driven residential AWG**; a fleet prototype (desiccant contactor, regenerator, condenser coil, filtration) is plausibly $10,000–20,000 (unverified estimate) against municipal water worth **$0.001–0.004/L** — i.e., ~160 L/day is worth cents. Potable use adds NSF/ANSI-class filtration, UV, mineralization, and biological-growth management in stored water.

The engineering case that survives: **close the cooling loop with the water.** Adiabatic (evaporative-assist) dry coolers are standard practice and transform hot-day performance; fully evaporating the D8's 5.4 kW for the six worst hours needs only ~48 L (0.68 kWh(th)/L latent heat), and spray-assist typically needs far less. The unit's own ~110–260 L/day sorbent output more than covers it — meaning **the heat makes the water that rejects the heat**: a smaller, quieter dry cooler that holds capacity at 45°C ambient with zero municipal water hookup, sidestepping both the noise-ordinance and the water-utility conversation. That, not drinking water, is the credible DisCo application — and it is the same argument Uravu is making at datacenter scale. A full stand-alone cost model for the potable-water version — capture, filtration, storage, and humidity sensitivity — is worked in §13.

**What it means for the model.** As a token-cost credit the effect is modest — even full winter displacement is worth only ~$0.01–0.02/M tokens on the D8, a 3–8% improvement on the 3-year figure — so heat recovery does not change the §6/§8 conclusions. Its real value is strategic: in Texas the DHW tap is a cheap homeowner-retention feature, summer heat is best spent on latent-load relief and adiabatic-assist water (Paths 3–4) rather than dumped, and in cold climates the calculus inverts enough to define a distinct **DisCo-North variant**: heat becomes a second product with an existing commercial playbook, the qualification problem eases (winter-peaking feeders, no AC-coincidence constraint), and new-construction integration (the PulteGroup pattern) can plumb the buffer tank and radiant loops at build time for near-zero marginal cost. The main engineering deltas for DisCo-North: glycol concentration for freeze protection, snow/ice-rated enclosure and dry cooler, and heat-priority (rather than dump-priority) loop controls.

## 13. Cost Model: Waste-Heat AWG to Potable Water

A stand-alone model for the §12 Path-4 idea taken to its endpoint: use the D8's ~130 kWh(th)/day of 45–55°C reject heat to drive a liquid-desiccant water harvester, then filter and store the output as **potable** water. Everything below is a planning estimate; no commercial product exists at this scale.

**13.1 System and BOM**

Chain: air contactor (ambient air over desiccant) → regenerator (heated by the GPU return loop; hotter loop per §4.2 helps directly) → condenser → raw-water tank → potable train → storage. The condensate is near-distilled: biologically clean at the moment of production but aggressive (no minerals, absorbs CO₂), and stored water is a growth medium — the potable train is mostly about **storage**, not the source.

| Item | Est. retail | Notes |
|---|---|---|
| Desiccant contactor + regenerator module (~5 kW(th)) | $10,000–20,000 | **Design-yourself** (§8.2 item 5); no residential product exists — Uravu is MW-scale, Mojave makes air handlers |
| Condenser + heat-rejection tie-in | $1,000–2,000 | Condenses against night air or loop return |
| Raw-water day tank, 200 L food-grade, level/TDS sensors | $400–700 | |
| Potable train: 5 µm sediment → activated carbon → calcite remineralization → UV (NSF/ANSI 55 Class A) | $1,200–2,000 | Viqua-class UV; remineralization protects plumbing and taste; target NSF P231 purifier performance |
| Potable storage: 500 gal NSF-61 poly tank + recirculation loop with second UV | $1,500–2,800 | Recirculating UV is what keeps stored water potable |
| Pumps, valves, food-grade plumbing | $600–1,200 | |
| Controls + water-quality telemetry (TDS, ORP, temp, level) | $500–1,000 | Folds into the §8.2 loop controller |
| **Total adder** | **~$15,000–30,000** | |
| Consumables/opex | ~$450–650/yr | Filters + UV lamps ~$300, desiccant top-off ~$100, quarterly lab water tests ~$150 |

**13.2 How Ambient Humidity Drives Output**

The physics: desiccant capture scales with the **vapor-pressure driving force between air and desiccant — i.e., absolute humidity, not relative humidity**. LiCl-class desiccants keep absorbing down to an equilibrium floor around ~11–15% effective RH, which is why the desiccant path degrades gracefully where condensation-type AWGs fall off a cliff ([US benchmark testing](https://journals.plos.org/water/article?id=10.1371%2Fjournal.pwat.0000133) shows compressor AWGs hitting zero output below ~30–40% RH). Output sits in one of two regimes: **heat-limited** in humid air (the 130 kWh(th)/day budget caps production — more moisture doesn't help, only more heat does) and **air-side limited** in dry air (energy per liter climbs and the contactor needs disproportionate airflow).

Modeled daily output for the D8's full heat budget, using computed humidity ratios and a sorbent energy intensity rising from ~0.75 kWh(th)/L (humid) toward ~2.5 kWh(th)/L (dry) — planning estimates consistent with the §12 0.5–1.2 kWh/L band:

| Condition | T / RH | Absolute humidity | Regime | Est. output |
|---|---|---|---|---|
| Houston, summer day | 33°C / 60% | ~19 g/kg | Heat-limited | ~170 L/day |
| Houston, summer night | 26°C / 85% | ~18 g/kg | Heat-limited | ~170 L/day |
| DFW, summer | 37°C / 35% | ~14 g/kg | Transitional | ~120 L/day |
| Austin, spring | 24°C / 70% | ~13 g/kg | Transitional | ~120 L/day |
| El Paso, summer | 36°C / 20% | ~7 g/kg | Air-side limited | ~85 L/day |
| Texas winter day | 12°C / 55% | ~5 g/kg | Air-side limited | ~50 L/day |
| Hard cold snap | <5°C | <4 g/kg | Effective floor | ~0–30 L/day |

Annualized planning figures: **~140–150 L/day Gulf Coast, ~100–110 L/day DFW/Austin, ~60–70 L/day far West Texas.** Airflow check: ~170 L/day at Houston humidity and 40% single-pass capture needs ~700–750 m³/h of continuous contactor airflow — a quiet, box-fan-class flow that roughly doubles-to-triples in dry-air conditions for less water, which is what "air-side limited" costs. Siting note: humidity, not heat, now enters the host-qualification calculus — the same Gulf Coast home that is worst for the §1 AC-headroom screen is best for water.

**13.3 Economics**

At ~$19k mid-range capex amortized over 10 years plus consumables: ~**$6.4/day ≈ $0.05/L ≈ $200 per 1,000 gallons** at a 120 L/day annual average — versus ~$3–6 per 1,000 gallons municipal. Potable water from waste heat is therefore **~35–65× municipal cost** and does not close economically anywhere on the grid; the free heat doesn't rescue it because the cost is all in the capture/filtration/storage hardware, not energy (the same CAPEX-dominance pattern as §7's tokens). What survives, in order of realism: (1) **adiabatic self-supply for the dry cooler** (§12 Path 4 — needs no potable train at all, deletes the noise/water-hookup problems, and is heat-positive); (2) **non-potable uses** — irrigation, pool make-up — needing only the $15–20k capture stage; (3) potable as a **resilience/marketing feature** (a DisCo host that makes its own drinking water during a Uri-class grid-and-water failure is a story, and ~150 L/day sustains a household several times over); (4) potable as economics — no. Off-grid or water-hauling sites (rural West Texas ranches) are the only geography where $0.05/L competes, and they are the worst humidity geography — the model's cleanest negative result.

**13.4 The Rationing Hedge: Where the Case Actually Lives**

§13.3's verdict priced AWG water against a tap that always flows. In much of Texas that assumption is weakening, and the honest case for the potable option is as a **hedge against rationed or interrupted municipal supply**, not as a utility substitute.

**Rationing is normal practice, not an edge case.** TCEQ requires every municipal water provider to maintain a Drought Contingency Plan with staged restrictions — typically Stage 1 (voluntary) through Stage 4 (emergency: outdoor watering bans, surcharges, in some plans hard allocation). As of this review (search-derived, July 2026), Texas is in a **seventh consecutive drought year**: the Edwards Aquifer region spent August 2025–June 2026 in Stage 4 before easing to Stage 3, with the aquifer still ~27 ft below its historical average; San Antonio (SAWS) is in Stage 3, Austin in Stage 2 since July 2025, Corpus Christi in Stage 3 with its reservoir system below 30%, and Schertz/Cibolo/Boerne spent time at Stage 4. Structurally it gets worse: Lubbock and the South Plains sit on the Ogallala Aquifer, declining roughly a foot per year with no meaningful recharge, and the Rio Grande Valley has faced repeated shortage declarations. Layer on acute interruptions — Texas's recurring boil-water notices, at their worst statewide after Uri — and "the tap always flows at $0.004/L" is a probabilistic statement, not a fact.

**Why atmospheric water is a genuine hedge and not just a backup tank.** The output is drawn from Gulf-sourced atmospheric moisture, which is largely **uncorrelated with the failure modes that trigger rationing** — reservoir levels, aquifer drawdown, and distribution-system integrity. A Texas drought is a rainfall deficit, not a humidity deficit: the §13.2 table's ~120–170 L/day Gulf Coast/I-35-corridor summer output holds through exactly the seasons when Stage 3–4 restrictions bind, because the absolute humidity that drives the desiccant comes from the Gulf, not from local rainfall. Core potable need (drinking + cooking) is ~4–10 L/person/day; even the winter-floor output of ~50 L/day covers a household several times over, and the summer output can additionally carry the hand-watering allowances that survive Stage 3–4 outdoor bans.

**How it prices.** Hedges price like insurance, not like commodities: the $0.05/L figure is irrelevant during a boil-water week or a Stage 4 summer, when the alternative is bottled water at $0.50–1.00/L, hauling, or doing without. The monetization is therefore (a) **host compensation in kind** — "your home makes its own drinking water" joins free hot water in the Tier 5 package, strongest exactly where municipal restrictions make it salient; (b) **siting and permitting currency** — jurisdictions have blocked or paused datacenter projects over water consumption (see the [Uravu Labs]({{< relref "uravu-labs.md" >}}) entry's framing), and a distributed fleet whose sites are net *producers* of potable water inverts the political sign of the water conversation in precisely the water-stressed regions where AC-driven §1 headroom is scarcest; (c) a **resilience story with a dollar anchor** — homeowners already pay $10–15k for standby generators against grid failure; a water hedge against a statistically comparable municipal failure mode rides along for a fraction of that inside the §13.1 BOM. What it is not: a revenue line. The fleet should account for it as site-acquisition and permitting cost reduction, same ledger as Tier 5.

## 14. Monetizing the Network: Revenue Stacks, Software, and Marketplace Integration

A fleet of DisCo units is a portfolio of three sellable things — compute, flexibility, and byproducts — and the §7 utilization math says the business lives or dies on stacking them so no hour goes unsold.

**14.1 Revenue Tiers**

**Tier 1 — Contracted inference capacity (the anchor, 40–60% of hours).** Span's own XFRA model: multi-year capacity contracts with hyperscalers/"neoscalers" who treat the fleet as a distributed availability zone for latency-tolerant inference and cloud gaming. This is the only tier that supports fleet financing, because it is the only one with predictable revenue. Pricing reference: dedicated RTX PRO 6000 capacity rents for ~$1.69–3.00/GPU-hr at managed providers ([RunPod](https://www.runpod.io/gpu-models/rtx-pro-6000), [Northflank](https://northflank.com/blog/how-much-does-an-nvidia-rtx-pro-6000-gpu-cost)); even at the marketplace floor a D8 grosses ~$146/day at 80% duty — right at its 3-year all-in daily cost — so the anchor contract must price above spot to carry the fleet.

**Tier 2 — Token-metered serving (the margin layer).** Operate the fleet as an inference provider: serve open-weight models (§7 table) behind an OpenAI-compatible API and list as a provider on aggregation layers (OpenRouter-style routing), where 70B-class output tokens clear ~$0.60–0.90/M (unverified estimate). At 80% utilization the D8 produces ~346M tokens/day → ~$207–310/day gross against ~$146/day cost. Token resale out-earns raw GPU rental whenever serving is efficient, because the operator captures the batching/optimization margin instead of handing it to the renter.

**Tier 3 — Spot/marketplace backfill (the utilization floor).** Idle hours list on GPU marketplaces: [Vast.ai](https://vast.ai/pricing/gpu/RTX-PRO-6000-WS) hosts RTX PRO 6000s at ~$0.97/GPU-hr (host keeps ~75–80%), [Spheron](https://www.spheron.network/gpu-rental/rtx-pro-6000/) from ~$0.91/hr; [Akash Network]({{< relref "akash-network.md" >}}) is the decentralized-marketplace path already profiled in this section; io.net and RunPod Community Cloud are equivalents. Spot rates are volatile and low, but every backfilled hour converts ~$0 marginal cost into revenue — moving realized utilization from 60% to 80% cuts token cost 24% (§7). Batch workloads (synthetic-data generation, evals, LoRA fine-tunes — feasible on 8× 96 GB) are the natural filler demand.

**Tier 4 — Grid services (the flexibility product).** The 45 kWh battery + orchestrator is an ERCOT asset independent of compute: retail price arbitrage on volatile days, ERS/demand-response enrollment, and ancillary services via an aggregator QSE — the same stack documented across the [Virtual Power Plants]({{< relref "../../energy/virtual-power-plants/_index.md" >}}) subsection and monetized residentially by [Base Power]({{< relref "../../energy/batteries/base-power.md" >}}). Order of magnitude ~$1–3k/yr per site (unverified estimate; ERCOT ancillary revenues are notoriously volatile) — small next to compute, but it monetizes exactly the hours compute is curtailed, and the utility-relations value (a fleet that *reduces* peak load on command) is what keeps interconnection approvals flowing.

**Tier 5 — Byproducts and host-side value.** §12's ledger: DHW (~$600–700/yr), cold-climate heat sales, adiabatic water self-supply, plus the homeowner compensation package itself (subsidized panel/battery/discounted power, per Span's three-way value proposition) — not revenue, but the cost of site acquisition, and cheaper than datacenter land + interconnection. In water-rationed service areas the potable-water option (§13.4) upgrades from perk to hedge — part of the same site-acquisition currency.

**14.2 Software Stack Deep Dive**

The stack splits into four planes, most of it assemblable from existing open source:

| Plane | Function | Existing components |
|---|---|---|
| Serving | Model execution, batching, KV management | vLLM / SGLang / TensorRT-LLM; OpenAI-compatible gateway |
| Fleet orchestration | Scheduling, model placement, OTA updates, node health | k3s/K8s + virtual-kubelet per site; P2P model-artifact distribution (the 768 GB RAM staging tier exists for fast model swaps); Prometheus/Grafana telemetry; BMC/remote-KVM out-of-band |
| Power orchestration | Battery EMS, peak curtailment, ERCOT signal response, §1 headroom enforcement | OpenADR 3.0 / IEEE 2030.5 client against the smart panel; aggregator/QSE API for market dispatch — this is Span's actual moat and the hardest build |
| Trust & commerce | Multi-tenant isolation on residential premises, metering, billing, marketplace listing | GPU confidential-computing modes (Hopper/Blackwell TEEs) + attestation, secure/measured boot, per-tenant vGPU or MIG partitioning; usage metering feeding marketplace provider daemons (Akash provider, Vast host agent) and direct-contract billing |

Plane by plane, what the table compresses:

**Serving plane.** Per-node: vLLM or SGLang engines (TensorRT-LLM where squeezing the last 20% matters) behind a local OpenAI-compatible gateway, with continuous batching, paged KV, prefix caching, and speculative decoding as table stakes. The DisCo-specific pieces: a **model-placement scheduler** that packs replicas against forecast demand (the §7 menu is a portfolio decision re-made hourly), and **hot-swap from the RAM staging tier** — the §5 768 GB of DDR5 exists so a 70 GB model loads to VRAM over PCIe 5.0 in a few seconds instead of minutes from NVMe, making it economical to chase demand across models. Per-tenant isolation via MIG/vGPU partitions for rental tenants, TEE sessions for weight-sensitive ones.

**Fleet plane.** k3s/virtual-kubelet per site under a central control plane; P2P artifact distribution for model weights (a 405 GB model pushed to 10,000 sites is a torrent problem, not an HTTP problem); A/B OTA updates with automatic rollback and canary cohorts; per-node PKI identity issued at manufacturing; BMC out-of-band access over the LTE failover path for when the primary link or OS is down. The custom piece is the **site agent** — one daemon that unifies IT, power, and thermal telemetry and executes curtailment orders, i.e., the software half of §8.2 items 2–3.

**Power plane — the moat.** This is not "demand response integration"; it is a continuous joint optimization per site: maximize (token revenue + grid revenue) subject to battery state-of-charge, the peak-window grid-zero commitment, thermal limits, and the §1 headroom envelope — driven by ERCOT day-ahead/real-time price forecasts, PV forecast (§10 variants), and home-load forecast. Protocol surface: OpenADR 3.0 / IEEE 2030.5 toward the smart panel and utility programs, aggregator/QSE APIs toward ERCOT markets. Failure semantics are the trust-critical part: every fault path must degrade toward *curtail compute, protect the home* — the inverse of datacenter instinct. This plane is Span's actual product and the hardest thing on this page to replicate.

**Trust & commerce plane.** Hopper/Blackwell confidential-computing TEEs with remote attestation, measured boot, no plaintext model weights at rest, and tamper-responsive enclosure integration (§6) on the trust side; per-token/per-GPU-hour metering with **signed usage receipts**, billing, and marketplace provider adapters (Akash provider daemon, Vast host agent) on the commerce side. The trust plane is the differentiator nobody in the consumer-GPU marketplace world has solved well: enterprise tenants must accept that their weights and traffic run in a box in a stranger's yard. Without attestation the fleet is limited to Tier 3 spot pricing — which the §7 table shows is roughly a breakeven business.

Build-effort shape (planning commentary, not an estimate from data): the serving and fleet planes are assemblable from mature open source in engineer-months; the power plane and attestation-backed trust plane are multi-year, and they are also the only two that competitors can't clone from GitHub — the software moat and the hardware BOM are disjoint.

**14.3 The Token Marketplace Option: Sourcing by Cost and Latency**

Tier 2 assumed listing on someone else's aggregator. The stronger version — given a fleet with thousands of metro-distributed nodes — is operating (or plugging into) a **token marketplace** where buyers source inference by explicit cost and latency policy. The mechanics:

**Price discovery.** Two working models exist today: *posted-price aggregation* (OpenRouter-style: providers publish $/M-input and $/M-output per model; the router ranks by price, uptime, and measured throughput, with buyer-selectable routing variants that optimize for cheapest or fastest) and *reverse auction* ([Akash]({{< relref "akash-network.md" >}})-style: buyers post workloads, providers bid down). A DisCo fleet should publish a **signed capability manifest** per node — models, quantizations, context lengths, price sheet, live queue depth, TEE attestation quote — as the market feed. The battery adds a product dimension no cloud provider has: **firm tokens** (battery-backed through the ERCOT peak, premium-priced) versus **interruptible tokens** (curtailment-exposed, discounted) — the compute equivalent of firm vs. interruptible power tariffs, and priceable off the §3 ride-through table.

**Latency-based sourcing.** The metrics that matter are TTFT (time to first token — dominates perceived responsiveness in interactive/agentic/voice use) and streaming tok/s. Protocol: nodes publish rolling p50/p95 TTFT and tok/s per model; buyers attach a latency class to each request (interactive vs. batch); the gateway routes geographically (anycast/geo-DNS plus client-measured RTT beacons, standard CDN practice) with admission control that never lets batch traffic degrade the interactive SLA class. The fleet's structural edge: a node physically inside the buyer's metro is single-digit-ms RTT versus tens of ms to a regional cloud AZ — for TTFT-sensitive workloads, residential siting stops being a liability and becomes the product. The §15 residential-upload constraint cuts the other way for prompt-heavy traffic; latency-priced routing lets the market sort that per-request.

**Settlement and verification.** Signed usage receipts reconcile against buyer-side counts; settlement by invoice for contracted buyers or per-call micropayment rails (x402-style pay-per-request patterns are emerging practice, search-derived) for spot. The unsolved marketplace problem is **quality verification**: open aggregators suffer silent-quantization fraud (providers serving a heavier-quantized model than advertised — a recurring complaint against open routing layers). Countermeasures worth building: TEE attestation of the loaded model hash, canary-prompt auditing, and token-level sampling audits — a fleet that can *prove* what model served each token earns a listing-quality premium that unattested competitors can't match.

**Integration reality check.** Existing marketplace tooling (Akash provider daemon, Vast.ai host agent, io.net workers) assumes an always-on host and knows nothing about power curtailment windows; the orchestrator must present curtailment as scheduled (un)availability or absorb it with the battery. NVIDIA's own DGX Cloud Lepton-style marketplace aggregation (search-derived; not independently verified this session) is the strategic wildcard: if NVIDIA brokers distributed capacity into its own demand pipeline, XFRA-class fleets plug into wholesale demand without building a sales channel — consistent with NVIDIA's role as Span's launch partner.

## 15. Sensitivities and Open Questions

- **GPU price volatility:** the anchor card rose 55% in 16 months; the entire model reprices with it.
- Residential fiber upload (often 1–5 Gbps symmetric at best) caps batch sizes for prompt-heavy workloads; fine for decode-heavy serving.
- Curtailment-only variant (no battery) saves ~$13.5–21k but needs Span-grade orchestration trust from the utility/AHJ.
- Insurance, property tax treatment, and homeowner compensation are unmodeled and could rival the install line.
- Winter (Uri-style) events: battery + unit heat become assets — the §12 heat-recovery plumbing turns the unit into a backup heat source during outages (battery-powered, islanded).
- 2026 loss of the federal residential storage credit worsens battery economics vs. 2025 builds.

## Sources

- [RTX PRO 6000 Blackwell Server Edition (NVIDIA)](https://www.nvidia.com/en-us/data-center/rtx-pro-6000-blackwell-server-edition/) — specs: 96 GB GDDR7, FP8 2 PFLOPS (sparse), 600W configurable, air dual-slot / liquid single-slot. Fetched 2026-07-18.
- [Nvidia raises RTX Pro 6000 Blackwell pricing to $13,250 (Tom's Hardware)](https://www.tomshardware.com/pc-components/gpus/nvidia-raises-rtx-pro-6000-blackwell-gpu-pricing-to-usd13-250-55-percent-increase-over-msrp-in-a-years-time) — $8,565 launch → $13,250 marketplace price. Fetched 2026-07-18.
- [Average Electricity Usage in Texas (Choose Texas Power)](https://www.choosetexaspower.org/energy-resources/average-electricity-usage/) — usage-by-home-size marketplace data. Fetched 2026-07-18.
- [Mojave Energy Systems Launches AquaDry (GlobeNewswire, May 12, 2026)](https://www.globenewswire.com/news-release/2026/05/12/3292920/0/en/mojave-energy-systems-launches-aquadry.html) — hydronic liquid-desiccant air handler; 110–180°F regeneration water; waste-heat compatible; late-2026 shipments. Fetched 2026-07-18.
- [Deploying NVIDIA H200 NVL at Scale — Enterprise Reference Architecture (NVIDIA)](https://developer.nvidia.com/blog/deploying-nvidia-h200-nvl-at-scale-with-new-enterprise-reference-architecture/) — 2-8-5 PCIe-optimized config; 4-way NVLink bridging; air-cooled 4U chassis assumption. Searched 2026-07-19.
- [NVIDIA H200 Price Guide 2026 (Jarvis Labs)](https://jarvislabs.ai/blog/h200-price) — H200 NVL ~$28–35k street; AWS raised H200 instance pricing 15% Jan 2026 on tight supply. Searched 2026-07-19.
- [4-way NVLink Bridge for H200 NVL (HPE datasheet)](https://www.hpe.com/psnow/doc/PSN1014856854VNEN) — 1.8 TB/s bidirectional across four H200 NVL. Searched 2026-07-19.
- [Microfluidics Offers 3X Better Cooling Than Cold Plates (HPCwire, Sep 2025)](https://www.hpcwire.com/2025/09/25/microfluidics-offers-3x-better-cooling-than-cold-plates-microsoft-says/) — Microsoft–Corintis results: 3× heat removal, 65% lower peak silicon ΔT, 55% lower pressure drop. Searched 2026-07-19.
- [JetCool SmartPlate System](https://jetcool.com/smartplate-system/) — commercial microconvective cold plates and self-contained chassis cooling; UL-certified in Dell PowerEdge; ~15% average power-savings claim. Searched 2026-07-19.
- [Benchmarks of production for atmospheric water generators in the United States (PLOS Water)](https://journals.plos.org/water/article?id=10.1371%2Fjournal.pwat.0000133) — condensation-AWG output collapses below ~30–40% RH; strong absolute-humidity dependence. Searched 2026-07-19.
- Additional search-derived references (2026-07-19, not independently fetched): [Boyd CDUs](https://www.boydcorp.com/thermal/liquid-cooling-systems/coolant-distribution-unit-cdu.html), [Motivair in-rack CDU/quick connects](https://www.motivaircorp.com/products/), [CoolIT rack manifolds](https://www.coolitsystems.com/product/rack-manifold-2/), [Stäubli UQD](https://www.staubli.com/global/en/fluid-connectors/products/quick-and-dry-disconnect-couplings/thermal-management/uqd-universal-quick-disconnect.html), [IEEE Spectrum on Corintis microfluidics](https://spectrum.ieee.org/microfluidics-cooling-ai-chips-corintis), [Tom's Hardware on Microsoft microfluidic cooling](https://www.tomshardware.com/pc-components/liquid-cooling/microsoft-develops-breakthrough-chip-cooling-method-microfluidic-channels-can-cut-peak-temps-by-up-to-65-percent-outperform-conventional-cold-plates-by-up-to-3x), [NSF P231 protocol (Microbac)](https://www.microbac.com/catalog/nsf-protocol-p231/), [AWG cost guide (EnergyBS)](https://energybs.com/green-living/water/atmospheric-water-generator-awg-hydropanel-guide/), [AWG performance under hot/humid climate (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S2666016422000925), [Watergen Genny product page](https://watergen.com/product-page-gen-l/), [Watergen energy/cost figures (CleanTechnica)](https://cleantechnica.com/2019/02/14/watergens-atmospheric-water-generators-pull-water-from-thin-air/), [Aquaria AWG TCO breakdown](https://www.aquaria.world/blog-posts/atmospheric-water-generator-cost-tco-breakdown), [TCEQ drought response / PWS restriction list](https://www.tceq.texas.gov/response/drought), [Edwards Aquifer Stage 4→3 after 7-year drought (Nature World News, Jun 2026)](https://www.natureworldnews.com/articles/73015/20260605/san-antonios-7-year-drought-just-eased-edwards-aquifer-lifted-stage-4-stage-3-first-time.htm), [Central Texas district nears Stage 4 emergency (KXAN)](https://www.kxan.com/texas-water/texas-water-district-nears-historic-stage-4-emergency-drought-declaration/), [Texas water supply and demand outlook (Dallas Fed)](https://www.dallasfed.org/research/swe/2025/swe2505).
- Search-derived references (not independently fetched; treat figures as secondary): [H200 NVL datasheet (PNY)](https://www.pny.com/nvidia-h200-nvl), [Pro 6000 vLLM benchmarks (Database Mart)](https://www.databasemart.com/blog/vllm-gpu-benchmark-pro6000), [RTX PRO 6000 30B/70B benchmarks (Spheron)](https://www.spheron.network/blog/rent-nvidia-rtx-pro-6000/), [Powerwall 3 review/pricing (EnergySage)](https://www.energysage.com/energy-storage/best-home-batteries/tesla-powerwall-battery-complete-review/), [EG4 battery review (OhmSnap)](https://www.ohmsnap.com/blog/eg4-battery-review-budget-lfp-2026), [D2C vs immersion cooling (Coolnet)](https://www.coolnetpower.com/blog/liquid-cooling-edge-ai-gpus-direct-to-chip-vs-immersion/), [Subpanel cost (HomeGuide)](https://homeguide.com/costs/cost-to-install-a-subpanel), [GENOAD8X-2T (ASRock Rack)](https://www.asrockrack.com/general/productdetail.asp?Model=GENOAD8X-2T%2FBCM), [Texas solar panel cost (SolarReviews)](https://www.solarreviews.com/solar-panel-cost/texas), [Texas solar cost/production (EnergySage)](https://www.energysage.com/local-data/solar-panel-cost/tx/), [Used GPU market pricing (Hashrate Index)](https://hashrateindex.com/blog/used-gpu-market-pricing-deprecation-secondary-ai/), [HGX A100 8-GPU platform specs (Flopper)](https://flopper.io/system/nvidia-hgx-a100-8-gpu), [Heata](https://www.heata.co/), [Qarnot/UKPN residential compute heating (BeBeez)](https://bebeez.eu/2025/10/06/uk-power-networks-looks-to-install-compute-nodes-in-residents-houses-to-provide-heating/), [Compute waste-heat reuse (MIT Technology Review)](https://www.technologyreview.com/2023/08/18/1077548/computer-waste-heat/).
