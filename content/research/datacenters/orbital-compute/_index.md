---
title: "Orbital Compute"
date: 2026-04-29
lastmod: 2026-04-30
# changelog:
# 2026-04-30: Cross-linked GaAs solar panel manufacturer entries (Spectrolab, Azur Space, SolAero Technologies)
# 2026-04-29: Added supply chain inputs and launch provider capacity section (10-year speculative outlook)
draft: false
description: "Space-based compute infrastructure: satellite data centers, orbital AI clusters, and the emerging race to move ML workloads into low Earth orbit."
research_area: "datacenters/orbital-compute"
last_reviewed: 2026-04-29
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.9
  disable: false
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.

## Overview

Orbital compute covers satellite-based data centers and AI inference/training systems operating in low Earth orbit (LEO). The core proposition: solar irradiance in LEO is roughly 5–8× more intense than at mid-latitude Earth surface, continuous (no night/weather loss in sun-synchronous orbits), and paired with vacuum-based passive heat rejection — potentially addressing the two binding constraints on terrestrial AI infrastructure (power availability and thermal density). Launch costs are the principal economic barrier; most analysis treats ~$200/kg to LEO as the threshold at which space-based compute becomes cost-competitive with terrestrial power costs on a per-kW-year basis.

As of early 2026, the sector spans early-stage startups (Starcloud's first GPU satellite launched November 2025), research moonshots (Google's Project Suncatcher targeting a 2027 prototype mission with Planet Labs), and large-scale ambitions (SpaceX FCC filings for up to one million orbital compute satellites). Lunar data storage is an adjacent niche covered under Lonestar Data Holdings.

## Key Themes

- Launch cost trajectory is the critical gating factor: SpaceX learning-curve analysis projects <$200/kg to LEO by mid-2030s at ~180 Starship launches/year; current Falcon 9 pricing is ~$3,600/kg
- Solar power in LEO: up to 8× annual energy per panel vs. mid-latitude ground; no weather or day/night loss in dawn-dusk sun-synchronous orbit
- Vacuum thermal management: heat rejection via radiators in vacuum avoids the cooling water and energy overhead of terrestrial data centers (PUE = 1.0 in principle)
- Inter-satellite optical links: achieving ML cluster-class bandwidth (multi-Tbps) requires formation flying at <300 km separation — far tighter than any current constellation
- Radiation hardening: commercial GPU/TPU dies survive LEO radiation environments for 5-year mission lifetimes, though HBM memory is the most sensitive subsystem
- Regulatory environment: FCC spectrum and orbital slot filings are the near-term regulatory bottleneck; debris and orbital sustainability are emerging concerns at constellation scale

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [Starcloud](https://www.starcloud.com/) | Redmond, WA, US | Series A ($170M, unicorn) | Builds and operates orbital data centers; first GPU satellite (H100) launched Nov 2025 |
| [Aetherflux](https://www.aetherflux.com/) | US | Series A ($50M) | Space-based solar power + orbital data center; "Galactic Brain" constellation targeting Q1 2027 commercial ops |
| [Lonestar Data Holdings](https://www.lonestarlunar.com/) | US | Early stage | Lunar and cislunar data storage; first payload flew on Intuitive Machines Athena mission Feb 2026 |
| [Kepler Communications](https://www.keplercommunications.com/) | Toronto, Canada | Growth | Space networking constellation; launched largest orbital compute cluster (40× NVIDIA Orin on 10 sats) in Jan 2026 |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [PL](https://finance.yahoo.com/quote/PL) | [Planet Labs](https://www.planet.com/) | Earth observation; Google's Project Suncatcher prototype partner for 2027 launch |
| [SPCE](https://finance.yahoo.com/quote/SPCE) | [Virgin Galactic](https://www.virgalactic.com/) | Space tourism; tangential — included for completeness only |

<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container" style="margin: 20px 0;">
  <div class="tradingview-widget-container__widget"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js" async>
  {
    "colorTheme": "light",
    "dateRange": "12M",
    "showChart": true,
    "locale": "en",
    "showSymbolLogo": true,
    "showFloatingTooltip": true,
    "width": "100%",
    "height": "500",
    "tabs": [
      {
        "title": "Orbital Compute",
        "symbols": [
          {"s": "NYSE:PL", "d": "Planet Labs"}
        ],
        "originalTitle": "Orbital Compute"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [GOOGL](https://finance.yahoo.com/quote/GOOGL) | [Alphabet / Google](https://abc.xyz/) | Project Suncatcher: TPU satellite constellation research moonshot; Planet Labs partnership for 2027 prototype |
| [SPCE](https://finance.yahoo.com/quote/SPCE) | [SpaceX](https://www.spacex.com/) | FCC filing for up to 1M orbital compute satellites; Terafab D3 chip program targeting orbital AI; dominant launch provider |
| [NVDA](https://finance.yahoo.com/quote/NVDA) | [NVIDIA](https://www.nvidia.com/) | H100 and Blackwell chips deployed in space by Starcloud and Kepler; NVIDIA Space Computing initiative; Inception program partner |

## Supply Chain Inputs and Launch Capacity (Speculative 10-Year Outlook)

The following section examines the upstream supply chain constraints that will govern how quickly orbital compute can scale, and the launch provider capacity required to field constellations at commercially meaningful size. All figures here are speculative projections based on current industry trajectories extended to 2036 — actual outcomes will depend heavily on Starship ramp rate, GPU roadmaps, and investment flows into space manufacturing.

### Satellite-Grade Solar Arrays

The power subsystem is the most specialized upstream dependency. Orbital compute satellites require triple-junction gallium arsenide (GaAs) solar cells, not commercial silicon panels. GaAs cell production is currently dominated by a short list of suppliers — [Spectrolab]({{< relref "/research/energy/solar/spectrolab" >}}) (a Boeing subsidiary), [Azur Space]({{< relref "/research/energy/solar/azur-space" >}}) (Germany), and [SolAero Technologies]({{< relref "/research/energy/solar/solaero-technologies" >}}) (now part of Rocket Lab) — with total industry production in the low tens of megawatts per year. Terrestrial commercial solar production is measured in terawatts. This is not a cost problem; it is a volume problem: the GaAs cell supply chain is sized for government and commercial satellite programs numbering in the hundreds of satellites, not tens of thousands.

Scaling to constellations of 1,000–10,000 compute satellites over 2030–2036 would require GaAs cell production to grow by 10–100× from current levels. That expansion requires capital investment in epitaxial growth reactors (MOCVD systems), long lead times (3–5 years to build and qualify new manufacturing lines), and significant demand visibility for suppliers to commit capital. Absent a clear anchor customer (analogous to what Starlink was for Starlink's own manufacturing), GaAs supply will likely be the first physical bottleneck encountered after launch cost.

An alternative path — thin-film perovskite arrays at space-relevant specific power — could open up a different supply chain rooted in commercial photovoltaics scale. But space-qualified perovskite arrays do not exist as a production product in 2026; they are at TRL 4–5 at best. Realistic production readiness is 2030–2033. The window between "GaAs supply wall" and "perovskite alternative available" is a genuine 2028–2031 risk zone for fast-scaling constellation operators.

### High-Bandwidth Memory (HBM) for Space

Every GPU generation from H100 onward runs HBM as its primary memory fabric — H100 carries HBM2e at 80 GB; B200 runs HBM3e at 192 GB. The HBM supply chain is an extreme oligopoly: SK Hynix, Samsung, and Micron are the only manufacturers, with SK Hynix holding the largest share of HBM3e production. Total industry HBM output is constrained by the extreme complexity of die-stacking and the limited number of CoWoS advanced packaging lines at TSMC.

For orbital compute, HBM introduces two supply chain issues beyond the standard terrestrial scarcity. First, there is no space-qualified HBM product: radiation-tested, TID-characterized, SEU-rate-characterized HBM at GPU-class bandwidth densities does not exist commercially. Any operator flying COTS GPUs (as Starcloud does) is accepting uncharacterized radiation risk in the memory stack. Developing a space-qualified HBM variant would require a custom program with one of the three HBM vendors — a multi-year, multi-hundred-million-dollar effort that is not currently funded or announced by any party. By 2032–2035, if orbital compute scales to meaningful GPU counts, this gap will become acute: either a qualified HBM variant exists or operators accept systemic reliability risk.

Second, HBM in orbit represents hardware that cannot be refreshed. Each HBM generation (HBM2e → HBM3e → HBM4 → HBM4E) roughly doubles bandwidth and energy efficiency. A satellite launched in 2030 with HBM4 will be flying HBM4 in 2037 while the terrestrial market has moved two or three generations further. This memory-bandwidth aging amplifies the compute-density disadvantage noted in the economics analysis.

### Radiation-Hardened Control Electronics

The compute payload (GPUs, HBM) runs COTS in current designs. But the satellite bus — attitude control, power management, communications, fault detection and recovery — requires radiation-tolerant or rad-hard components. This supply chain is mature but constrained: key suppliers include Microchip Technology (formerly Microsemi/Actel FPGAs), BAE Systems, Texas Instruments Hi-Rel, and Teledyne. Production volumes are low, lead times are 26–52 weeks for rad-hard FPGAs and power management ICs, and prices are 10–50× their commercial equivalents.

At constellation scale (thousands of satellites), bus electronics procurement becomes a meaningful supply chain management challenge. SpaceX has largely solved this by designing Starlink around commercially-tolerant parts with software-based fault recovery rather than hardware rad-hardness. Orbital compute operators targeting commercial GPU clusters would likely adopt the same philosophy — but this shifts reliability risk from hardware to software, requiring robust in-orbit fault management stacks that do not yet exist in production form for compute satellites.

### Structural and Thermal Materials

Satellite structures are primarily aluminum alloys (6061, 7075) and carbon fiber composites — both commodity materials with no supply constraint at constellation scale. Thermal management is the more specialized dependency: vapor chamber assemblies and heat pipes for GPU-to-radiator thermal pathways are produced by companies including Thermacore (now part of Curtiss-Wright), Fujikura, and ACT (Advanced Cooling Technologies). These supply chains serve aerospace and high-reliability markets and are not sized for high-volume production. Custom heat pipe assemblies at $5K–$20K per satellite are not a cost problem for a $1M satellite, but delivery timelines of 20–40 weeks per order would constrain production line throughput for any operator building more than a few dozen satellites per year.

Radiator panels — the primary heat rejection surface — are simpler: they are aluminum honeycomb panels coated with high-emissivity optical surface film (e.g., Astroflon or black-anodized surfaces). These are standard satellite components with no unusual supply constraint.

### Launch Provider Capacity: Speculative Outlook to 2036

The launch capacity picture through 2036 is dominated by two realities: SpaceX's growing but uncertain Starship ramp, and a set of emerging competitors that provide redundancy but not yet volume.

**SpaceX / Starship.** Boca Chica production is targeting a throughput of roughly one Starship per week by the late 2020s — a goal consistent with the manufacturing infrastructure being built but not yet demonstrated. At that rate, assuming 70–80% launch success, the system could support 40–50 flights per year by 2028 and 100–200 by 2031. Each Starship can lift ~100–150 metric tons to LEO. At 200 kg per compute satellite, a single Starship could deliver 500–750 satellites per flight. Two hundred flights per year at this payload density equals 100,000–150,000 compute satellites per year — far more than current demand suggests will exist by 2031. The constraint will be satellites manufactured, not launch slots. This changes the optimization problem: satellite manufacturing throughput, not launch availability, will gate constellation size through the early 2030s.

**Blue Origin / New Glenn.** New Glenn began commercial launches in early 2025 with a 45-ton to LEO capacity. At current cadence (targeting ~12 launches per year by 2027), it provides meaningful launch redundancy for compute satellite operators who cannot depend solely on SpaceX pricing or schedule. New Glenn pricing is not publicly disclosed but is widely estimated at $50–$70M per launch, implying $1,100–$1,500/kg — competitive with Falcon 9 dedicated but not yet competitive with Starship projections. By 2030–2032, New Glenn could offer a credible second-source option for operators willing to pay a premium for supply chain independence.

**Rocket Lab / Neutron.** Neutron, targeting ~13 tons to LEO and designed for reusability, is in development with a target first launch around 2026–2027. At scale, Neutron's economics target roughly $50M per launch (~$3,800/kg) — not price-competitive with Starship for large constellation deployments, but relevant for small batches (50–100 compute satellites) where delivery flexibility and dedicated launch scheduling have operational value.

**Arianespace / Ariane 6.** Europe's Ariane 6 provides medium-heavy lift (10.3–21.6 tons to LEO depending on configuration) and is operational as of 2024. It is relevant as a geopolitical alternative for European or sovereignty-sensitive orbital compute operators, but its economics (~$75–115M per launch) are not competitive with SpaceX for commodity LEO deployment.

**Chinese launch vehicles.** Long March 8 rideshare offers competitive pricing (~$3,000–$5,000/kg) and increasing cadence, but US export controls on NVIDIA and other advanced GPU silicon effectively preclude US-origin compute payloads on Chinese rockets. Operators using domestically-produced Chinese AI accelerators (e.g., Huawei Ascend, Biren) face no such restriction — creating a bifurcated market where Western and Chinese orbital compute ecosystems develop largely independently.

### Constellation-Scale Manufacturing: The Missing Industry

The most underappreciated supply chain gap is satellite manufacturing itself. SpaceX's Starlink factory in Redmond, WA is the only facility in the world producing commercial satellites at automotive-like volume (20–40 per week). No orbital compute company has announced, funded, or broken ground on a comparable facility. Starcloud, Aetherflux, and Kepler are building satellites in the dozens, not thousands.

Standing up a high-volume satellite production line — from design freeze to a 10-per-week production rate — typically takes 4–7 years for a new entrant, requires $300M–$1B in capital depending on automation level, and requires stable, predictable component supply chains across solar panels, bus electronics, thermal hardware, and compute payload. Based on current announced investment levels (Starcloud: $170M Series A; Aetherflux: $50M Series A), none of the orbital compute startups are capitalized anywhere near the level needed to build this manufacturing infrastructure independently.

The most likely path to constellation-scale production is either (a) SpaceX vertically integrating orbital compute into its existing satellite manufacturing ecosystem — consistent with the FCC filing for 1M orbital compute satellites — or (b) a hyperscaler (Google, Microsoft, Amazon) funding a vertically integrated satellite manufacturing and operations company from scratch, as they have funded terrestrial data center construction. Neither path is announced; both remain speculative as of 2026. By 2030–2032, the absence of a credible manufacturing scale-up path would be a clear signal that orbital compute is a niche product rather than a mainstream infrastructure play.

## Analysis

- [**Orbital Compute: First-Principles Economics**]({{< relref "orbital-compute-economics.md" >}}) — Energy physics (LEO solar, GPU thermal budgets), satellite build and launch cost models, technology gaps (ISLs, radiation hardening, HBM, manufacturing scale), and 10-year cost trajectory projections through 2036.
