---
title: Battery Technology Research
date: 2026-03-23
lastmod: 2026-04-04
draft: false
description: Research on emerging battery technologies including solid-state, flow batteries, and high-density storage.
tags: ["batteries", "energy"]
categories: ["overview"]
research_area: "energy/batteries"
last_reviewed: 2026-04-04
stale_after_days: 365
sitemap:
  changefreq: "monthly"
  priority: 0.9
  disable: false
---

## Overview

Tracks advances in battery chemistry and storage technology, with a focus on solid-state batteries, lithium-sulfur chemistry, and the companies and researchers pushing energy density and cycle life forward. Also covers the grid-scale battery energy storage (BESS) market — from Chinese factory-direct integrators to Western software-differentiated players — because stationary storage is where most battery volume is deployed today.

## Key Themes

- Solid-state electrolytes (oxide, sulfide, polymer) approaching automotive production readiness
- Lithium-sulfur chemistry (Lyten) as an alternative path eliminating cobalt, nickel, and graphite
- Chinese BESS integrators achieving cost and engineering parity with Western players — the solar-panel pattern repeating
- U.S. tariff escalation (82%+ on Chinese LFP cells as of early 2026) reshaping supply chains in real time
- Software differentiation (Autobidder, Fluence IQ) as the last defensible moat for Western integrators
- Vertical integration strategies: BYD (cell + system), CATL → CNTE (arms-length forward integration), vs. pure integrators (Fluence, HyperStrong)

---

## Value Chain Map

The battery landscape spans five distinct positions in the supply chain. Companies in this research area are organized accordingly.

| Layer | What happens here | Companies here |
|-------|------------------|----------------|
| **1–2. Materials & Precursors** | Raw lithium, sulfur, Li₂S production; cathode precursors | Idemitsu Kosan, POSCO Future M (resources section) |
| **3. Electrolyte / Active Materials** | Solid electrolyte synthesis; graphene scaffold; cathode powder | Idemitsu Kosan (sulfide SE), Solid Power (sulfide SE), Lyten (3D Graphene cathode) |
| **4. Cell Manufacturing** | Cell assembly; solid-state or Li-S chemistry | Factorial Energy, QuantumScape, ProLogium, Adden Energy, Lyten, Donut Lab / Nordic Nano |
| **5. Pack / System Integration** | Cell → container BESS or EV pack | Tesla Megapack, Sungrow, BYD Energy Storage, Fluence Energy, HyperStrong, CNTE, Orient Power, GSL Energy, Verge Motorcycles |
| **6. OEM / End Use** | Finished EV, grid asset, drone | Stellantis, Mercedes-Benz, VW/PowerCo, BMW, Karma Automotive, IQT |

A few companies straddle layers deliberately:

- **BYD Energy Storage** operates at both Layer 4 (Blade LFP cell manufacturing) and Layer 5 (full BESS system integration). This vertical integration is its primary competitive moat.
- **Lyten** operates at both Layer 3 (3D Graphene active material synthesis) and Layer 4 (Li-S cell assembly).
- **Solid Power** is a Layer 3 electrolyte materials supplier that also designs the cell architecture it licenses to Samsung SDI (Layer 4).
- **CNTE** is a Layer 5 integrator but backed by and strategically adjacent to CATL (Layer 4), making it a de-facto forward integration vehicle.

---

## Tier 1: Electrolyte and Active Materials Suppliers

These companies sit upstream of cells — they supply the materials that make advanced battery chemistries possible.

| Company | HQ | Stage | Role in Supply Chain |
|---------|-----|-------|---------------------|
| [Idemitsu Kosan]({{< relref "idemitsu-solid-state.md" >}}) | Japan | Public (TSE: 5019) | Only identified large-scale lithium sulfide (Li₂S) producer; exclusive Toyota supplier; ¥21.3B Li₂S plant (1,000 MT/year, June 2027); solid electrolyte pilot plant construction began January 2026. Critical upstream bottleneck for the entire sulfide solid-state ecosystem. |
| [Solid Power]({{< relref "solid-power.md" >}}) (SLDP) | Louisville, CO | Public (Nasdaq: SLDP) | Sulfide electrolyte supplier + technology licensor to Samsung SDI / BMW. Has pivoted away from owning cell manufacturing to a capital-light IP licensing model. Continuous electrolyte pilot line (75 MT/year) commissioning by end of 2026. New: SK On disclosed as installation partner for pilot line. |
| [Lyten]({{< relref "lyten.md" >}}) | San Jose, CA | Series B+ ($625M+) | 3D Graphene-enabled lithium-sulfur; no nickel, cobalt, or graphite. Acquired Northvolt Gdańsk BESS facility (completed Feb 2026). Commercial cells from Skellefteå H2 2026 (NMC long-life initial production). Nevada gigafactory Phase 1 targeting 2027. Competes on cobalt-free, graphite-free strategic positioning for defense and drone markets. |

**Key concern — Idemitsu Li₂S bottleneck:** Idemitsu's entire 1,000 MT/year Li₂S capacity (available by June 2027) is committed to Toyota. QuantumScape and Solid Power both rely on sulfide electrolytes requiring Li₂S as a precursor, and neither has disclosed a qualified alternative supplier. If the three largest sulfide programs (Toyota, QuantumScape, Solid Power) all scale simultaneously post-2027, Li₂S supply will be a structural chokepoint.

---

## Tier 2: Cell Manufacturers (Advanced Chemistry)

These companies make the cells — the electrochemical unit. All are pre-production or early-production scale, targeting automotive and/or adjacent markets.

| Company | HQ | Stage | Technology | Key Developments (2025–2026) |
|---------|-----|-------|------------|------------------------------|
| [Factorial Energy]({{< relref "factorial-energy.md" >}}) | Cambridge, MA | Pre-IPO (SPAC/Nasdaq FAC, ~mid-2026) | FEST® semi-solid (375 Wh/kg) + Solstice™ all-solid-state (450 Wh/kg) | Mercedes-Benz completed 1,205 km / 749-mile single-charge test (Stuttgart → Malmö) using Factorial cells. SPAC at $1.1B pre-money valuation. IQT/defense expansion, Philenergy MOU (Feb 2026), Karma Automotive validation (Feb 2026). OEM launch ~2027 targeting luxury/performance vehicles first. |
| [QuantumScape]({{< relref "quantumscape.md" >}}) | San Jose, CA | Public (NYSE: QS) | Sulfide-based ceramic separator (Cobra process) | Eagle Line pilot inaugurated Feb 2026. VW PowerCo non-exclusive license: up to 40 GWh/year (option to 80 GWh). Ducati V21L race bike full field testing 2026. Capital-light licensing pivot confirmed. Expanding to defense/drones/AI data center. FY2026 EBITDA guidance: −$250M to −$275M; $970M liquidity. **Concern:** Licensing model reduces capital requirements but introduces dependency on licensees' manufacturing ramp. |
| [ProLogium Technology]({{< relref "prologium.md" >}}) | Taiwan | Pre-IPO | Oxide-based → Superfluidized All-Inorganic (ceramic + all-silicon anode) | Dunkirk gigafactory groundbreaking February 11, 2026. Initial capacity 0.8 GWh; target 4 GWh by 2029; expandable to 48 GWh. Mass production of 4th-gen cells: 2028. Patent leadership claim (cost + scale limits). Claimed 57 mS/cm ionic conductivity remains unverified by independent lab. |
| [Adden Energy]({{< relref "adden-energy.md" >}}) | Waltham, MA | Series A ($20M) | Thin-film solid-state (Harvard SEAS spinout) | Pilot line commissioned Feb 2025. Lab-validated: 10-min charge and 10,000 cycles at coin-cell scale. Behind Factorial and QuantumScape in OEM pipeline by ~1–2 years. No new disclosed funding or OEM agreements. |
| [Donut Lab]({{< relref "donut-lab.md" >}}) / [Verge Motorcycles]({{< relref "verge-motorcycles.md" >}}) | Estonia / Finland | Private | TiO₂ nanostructure pseudocapacitance | TS Pro deliveries commenced Q1 2026 (claimed world-first production solid-state motorcycle). VTT confirmed: fast charge (0–80% in 4.5 min, 11C) and thermal stability (107% capacity at 100°C). **Key concern:** Five independent VTT test reports released through March 2026 — none measure 400 Wh/kg energy density or 100,000-cycle life. Svolt chairman called 400 Wh/kg "physically impossible." Headline claims remain unverified; verified claims are genuine but modest. |

**Cross-cutting concern — sulfide programs (QuantumScape, Solid Power, Idemitsu/Toyota):** All three depend on Li₂S precursor supply from a single identified large-scale source (Idemitsu) that is committed exclusively to Toyota. This shared upstream dependency is the most underappreciated concentration risk in the solid-state sector.

---

## Tier 3: BESS System Integrators

These companies assemble cells into grid-scale or commercial battery storage systems. The BESS market is where battery volume is currently deployed at scale. **The dominant market story of 2024–2026 is Chinese integrators achieving cost and technical parity with Western players, replicating the solar panel commoditization arc.**

### Chinese Integrators — Vertically Integrated

| Ticker | Company | Key Differentiator | Notable (2025–2026) |
|--------|---------|-------------------|---------------------|
| [1211.HK](https://finance.yahoo.com/quote/1211.HK) | [BYD Energy Storage]({{< relref "byd-energy.md" >}}) 🇨🇳 | **Uniquely dual-layer:** manufactures own Blade LFP cells AND integrates into BESS systems. 10,000-cycle 2,710 Ah Blade cell (Haohan system). | Haohan (14.5 MWh DC/unit, 52.1% VCTS) launched Sept 2025. Saudi Electricity Company 12.5 GWh contract (5 sites). Full-year 2025 ranking: #3 globally by InfoLink; #2 in Q3 utility-scale. NDAA FY2024 prohibits US DoD procurement. |

### Chinese Integrators — Pure Integrators (Cell Buyers)

| Ticker | Company | Key Differentiator | Notable (2025–2026) |
|--------|---------|-------------------|---------------------|
| [300274.SZ](https://finance.yahoo.com/quote/300274.SZ) | [Sungrow]({{< relref "sungrow.md" >}}) 🇨🇳 | #1 or #2 globally by volume; PowerTitan 3.0 (7.14 MWh/20-ft, grid-forming, SiC PCS); 21% European share 2024 | 43 GWh shipped 2025; guiding 60–65 GWh (+40–50%) for 2026. Egypt factory partnership (MENA first BESS mfg, Suez Canal Economic Zone). Hong Kong listing announced Aug 2025. Energy storage surpassed solar inverters as largest revenue segment in Q3 2025. |
| — | [HyperStrong]({{< relref "hyperstrong.md" >}}) (688411.SS) 🇨🇳 | Top-5 globally; #1 in China cumulative installed; IPO Jan 2025 (+229% first day) | 200 GWh CATL supply agreement (2026–2035, ~$2.8B). EVE Energy 50 GWh supply deal (2025–2027, diversification signal). MagicBlock 10-ft container launched 2025. US and EMEA expansion active. |
| — | [CNTE]({{< relref "cnte.md" >}}) 🇨🇳 | CATL-backed system integrator; CATL's forward-integration vehicle without cannibalizing integrator customers | STAR H-PLUS (125 kW/254 kWh, liquid-cooled) unveiled KEY ENERGY 2026, Rimini. YOU.ON ENERGIA partnership (European distribution). 12 GWh annual capacity. |
| — | [Orient Power]({{< relref "orient-power.md" >}}) 🇨🇳 | Factory-direct LiFePO4 BESS; cost and procurement simplicity | CE certification on MW-class container systems April 2026, opening European market. |
| — | [GSL Energy]({{< relref "gsl-energy.md" >}}) 🇨🇳 | Factory-direct LiFePO4; 5.8 GWh capacity; 138+ countries, 4,500+ installations | UL9540/UL1973 certification April 2026, accelerating North American expansion. Liquid-cooled 5 MWh container now in market. |

### Western Integrators

| Ticker | Company | Key Differentiator | Notable (2025–2026) |
|--------|---------|-------------------|---------------------|
| [TSLA](https://finance.yahoo.com/quote/TSLA) | [Tesla Megapack]({{< relref "tesla-megapack.md" >}}) | #1/#2 globally; Autobidder software; U.S. domestic IRA content; 39% North America share | Texas Megafactory (Brookshire) ramping late 2026; 50 GWh/year target. LFP cell tariff hit: ~$200M in Q3 2025 alone; 82.4% effective tariff on Chinese LFP by early 2026. $4B LG Energy Solution contract (decade-long) to diversify from CATL. CATL pre-commitment: 20 GWh/year (2026–2028, ~30% of projected needs). Megapack 3 introduced (up to 5 MWh/unit). **Concern:** tariff exposure is material and ongoing; software moat (Autobidder) is the key Western differentiator. |
| [FLNC](https://finance.yahoo.com/quote/FLNC) | [Fluence Energy]({{< relref "fluence-energy.md" >}}) | Fluence IQ software platform; FEOC-compliant supply chain; Western bankability | Q1 2026 results: record backlog. Arizona factory ramping toward FEOC-compliant cell sourcing. Now offering 100% non-Chinese products qualifying for ITC under IRA. FY2026 guidance: $3.2–3.6B revenue; $40–60M EBITDA (thin margins at ~1.5% EBITDA). FEOC regulations taking effect 2026 are a near-term tailwind for domestic-content compliance. **Concern:** margins remain extremely thin; any share loss to Chinese competitors quickly turns unprofitable. |

---

## Incumbents (Contextual Reference)

These are the established players whose timelines and decisions set the context for advanced chemistry commercialization.

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [TM](https://finance.yahoo.com/quote/TM) | Toyota | Largest solid-state patent holder; 2027–2028 commercial target; exclusive Idemitsu sulfide electrolyte supplier. Signal: when Toyota ships, the technology has cleared automotive grade. |
| [006400.KS](https://finance.yahoo.com/quote/006400.KS) | Samsung SDI | Cell manufacturing partner for Solid Power (BMW i7 program); 500 Wh/kg solid-state target. Signal: validates Solid Power's licensing model if integration succeeds. |
| [PCRFY](https://finance.yahoo.com/quote/PCRFY) | Panasonic | Tesla supplier; solid-state R&D ongoing; no firm timeline. Signal: mainstream tier-1 supply chain readiness. |
| [300750.SZ](https://finance.yahoo.com/quote/300750.SZ) | CATL 🇨🇳 | World's largest EV battery maker; solid-state target ~2027; ~22% BESS cell market share (H1 2025). **⚑ Shared supplier:** supplies Tesla Megapack, Sungrow, HyperStrong, Fluence, and directly through CNTE — creating shared upstream dependency across competing integrators. |

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
        "title": "Batteries — Public Pure-Plays",
        "symbols": [
          {"s": "NASDAQ:FLNC", "d": "Fluence Energy"},
          {"s": "NYSE:QS", "d": "QuantumScape"},
          {"s": "NASDAQ:SLDP", "d": "Solid Power"}
        ],
        "originalTitle": "Batteries"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

<!-- TradingView Widget for Incumbents BEGIN -->
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
        "title": "BESS Incumbents",
        "symbols": [
          {"s": "NASDAQ:TSLA", "d": "Tesla"},
          {"s": "NASDAQ:TM", "d": "Toyota"},
          {"s": "SEHK:1211", "d": "BYD Energy Storage"},
          {"s": "SZSE:300274", "d": "Sungrow"}
        ],
        "originalTitle": "BESS Incumbents"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

---

## Cross-Cutting Insights (Updated April 2026)

### The Tariff Shock Is Real and Reshaping Supply Chains

U.S. tariffs on Chinese LFP batteries reached an effective rate of ~82.4% by early 2026 (stacking Section 301, reciprocal tariffs, and a battery-specific 25% tranche). This is materially changing sourcing decisions in real time:

- **Tesla** incurred ~$200M in tariff costs in Q3 2025 alone and has contracted LG Energy Solution for $4B in LFP cells. It retains a 20 GWh/year CATL commitment (2026–2028) representing ~30% of projected needs — the exact proportion it cannot yet substitute.
- **Fluence** has positioned itself as FEOC-compliant and able to offer 100% non-Chinese product qualification for ITC credits. This is a near-term structural advantage in the U.S. market.
- **Chinese integrators** (Sungrow, BYD, HyperStrong, CNTE) are largely unaffected in non-U.S. markets and continue aggressive expansion in Europe, Middle East, Australia, and Latin America. The tariff wall partially protects U.S. Western integrators while ceding the rest of the world to Chinese competition.

### The Solid-State Race Has Two Sub-Stories

The **cell chemistry** race (who achieves automotive-grade solid-state first) and the **business model** race (who captures value from the technology) are diverging:

- Factorial Energy's Mercedes EQS real-world test (1,205 km, no charge stop) is the most significant real-world solid-state demonstration to date — a validation milestone that press releases cannot replicate.
- QuantumScape is explicitly pivoting to a capital-light licensing model (like ARM in semiconductors) rather than owning cell fabs. The VW PowerCo license (40–80 GWh/year) is the first concrete expression of this. Success here depends on whether licensees can execute manufacturing ramp independently.
- ProLogium is the only company with a **construction permit and groundbreaking** (Feb 2026) for a GWh-scale solid-state gigafactory outside its home country, making it the furthest along on the manufacturing path — despite its claimed 57 mS/cm conductivity figure remaining unverified.
- Solid Power remains the most cautious of the pure-plays: it outsources cell manufacturing to Samsung SDI and focuses on electrolyte IP, limiting capital risk but increasing dependence on Samsung SDI's integration timeline. The Ford JDA is winding down; the BMW/Samsung SDI tripartite program is the primary vehicle.

### Donut Lab / Verge — Verified Claims Are Real, Headline Claims Are Not

After five independent VTT test reports through March 2026, Donut Lab has independently confirmed fast-charging (0–80% in 4.5 min, 11C) and thermal stability at 100°C. These are genuine differentiators. What remains completely untested is the 400 Wh/kg energy density and 100,000-cycle life — the claims that generated the most coverage. The conflict of interest (same corporate family controls both the battery developer and the launch customer) makes it difficult to assess production-volume claims. The VTT omission of energy density tests — which requires only a scale and a discharge measurement — is conspicuous.

### BYD's Vertical Integration Advantage Is Conditional

BYD's Blade LFP cell + system integration model is a genuine structural moat *when cell prices are elevated or supply is constrained*. But when LFP cell prices collapsed in 2023–2024, vertically integrated suppliers lost market share to pure integrators who could source cheaper cells externally. The advantage is resilience and innovation control, not a consistently lower unit cost. BYD's 10,000-cycle Haohan cell is unverified by independent testing — if the figure is accurate, it represents a category shift in BESS economics (infrastructure-grade asset life), but it has not been corroborated beyond BYD product launch materials.

### Lyten's European Expansion Is More Significant Than It Appears

Lyten completing the Northvolt Gdańsk acquisition (Feb 2026) and announcing commercial cell delivery from Skellefteå in H2 2026 means that a U.S. lithium-sulfur startup now operates the largest BESS manufacturing facility in Europe and a separate Swedish R&D hub. The commercial deliveries from Skellefteå will initially be long-life NMC cells (using the facility's existing chemistry infrastructure), not Li-S cells — but this gives Lyten a revenue-generating European footprint and manufacturing experience while its core Li-S technology matures.

---

## Supply Chain

The supply chains for solid-state and lithium-sulfur batteries diverge significantly from conventional lithium-ion at the electrolyte and cathode layers. This section maps the chain from raw materials to OEM integration for the technologies documented here.

### Supply Chain Layers

| Layer | Key Inputs / Outputs | Companies Operating Here | Geographic Concentration Risk |
|-------|---------------------|--------------------------|-------------------------------|
| **1. Raw Materials** | Lithium (spodumene / brine), Sulfur, Cobalt, Nickel, Manganese | [SQM](https://www.sqm.com), [Albemarle](https://www.albemarle.com), [Ganfeng Lithium](https://www.ganfenglithium.com), [Pilbara Minerals](https://www.pilbaraminerals.com.au), [Tianqi Lithium](https://www.tianqilithium.com.au), [Glencore](https://www.glencore.com) | Lithium mining: Australia (~50% hard rock), Chile/Argentina/Bolivia (brine); Lithium refining: China (~65%+); Cobalt: DRC ~75%; Nickel: Indonesia ~40% |
| **2. Precursor Chemicals** | Lithium sulfide (Li₂S), NMC precursor (pCAM), lithium carbonate / lithium hydroxide | [Idemitsu Kosan]({{< relref "idemitsu-solid-state.md" >}}) (Li₂S), [Umicore](https://www.umicore.com) (pCAM), [Sumitomo Metal Mining](https://www.smm.co.jp/E/) (cathode precursor for Toyota) | Li₂S: Idemitsu is the only named large-scale supplier (1,000 MT/year by June 2027, committed to Toyota); pCAM: China and South Korea dominant |
| **3. Electrolyte / Active Materials** | Sulfide solid electrolyte, oxide ceramic electrolyte, Li-S cathode (sulfur + graphene scaffold), NMC / NCA / LFP cathode powder | [Idemitsu Kosan]({{< relref "idemitsu-solid-state.md" >}}) (sulfide SE for Toyota), [Solid Power]({{< relref "solid-power.md" >}}) (sulfide SE for BMW/Samsung SDI; SK On pilot line partner), [Lyten]({{< relref "lyten.md" >}}) (3D Graphene Li-S cathode), [POSCO Future M]({{< relref "../resources/posco-future-m.md" >}}) (NMC cathode + anode) | Sulfide SE supply is a critical bottleneck; Idemitsu at meaningful scale exclusively for Toyota; ceramic oxide SE: ProLogium proprietary |
| **4. Cell Manufacturing** | Assembled solid-state or Li-S pouch / prismatic cells | [Factorial Energy]({{< relref "factorial-energy.md" >}}) (FEST® semi-solid), [QuantumScape]({{< relref "quantumscape.md" >}}) (QSE-5 ceramic separator cell), [Adden Energy]({{< relref "adden-energy.md" >}}) (thin-film solid-state), [ProLogium]({{< relref "prologium.md" >}}) (oxide ASSB), Samsung SDI (integrating Solid Power electrolyte), [Lyten]({{< relref "lyten.md" >}}) (Li-S cells) | ASSB cell manufacturing: Japan (Toyota/Idemitsu), US (Factorial, QuantumScape, Adden), Taiwan (ProLogium), scaling to Europe (Lyten Gdańsk/Skellefteå, ProLogium Dunkirk) |
| **5. Pack Assembly** | Cell-to-pack integration; thermal management; BMS | [Verge Motorcycles]({{< relref "verge-motorcycles.md" >}}) / [Donut Lab]({{< relref "donut-lab.md" >}}) (motorcycle pack), FEV Group (ProLogium module engineering), Factorial OEM partners (Stellantis, Karma) | Incumbent tier-1 pack assemblers (Panasonic, Samsung SDI, CATL) dominate conventional Li-ion; ASSB pack integration is OEM-specific |
| **6. OEM Integration** | Finished EV, motorcycle, drone, satellite, grid storage | Stellantis, Mercedes-Benz, Hyundai, Kia (Factorial); VW/PowerCo (QuantumScape license); BMW (Solid Power via Samsung SDI); Toyota (Idemitsu/ASSB); IQT defense/drone (Factorial, QuantumScape); Tesla, Sungrow, BYD, Fluence (grid storage) | OEM integration timelines: 2027–2028 for Toyota/VW/BMW; 2027 for Stellantis; BESS integrations already at commercial scale |

### Key Supply Chain Notes

**Lithium:** All documented companies require lithium. China controls ~65%+ of lithium chemical refining (conversion to lithium hydroxide and lithium carbonate), creating a chokepoint even for Western-mined material. No documented battery company in this knowledge base has publicly disclosed a specific lithium supply agreement at the raw materials level.

**Sulfur:** Sulfur is a byproduct of petroleum and natural gas refining — abundant and cheap globally. This is a strategic advantage for lithium-sulfur (Lyten) and sulfide solid electrolyte programs (Solid Power, QuantumScape, Idemitsu). **⚑ Vertical integration note:** Idemitsu's unique position as both an oil company (producing sulfur as a refining byproduct) and a solid electrolyte manufacturer gives it a vertically integrated sulfur-to-Li₂S supply chain that no other documented electrolyte maker replicates.

**Cobalt:** Most documented companies eliminate cobalt entirely. Lyten (Li-S) and solid-state programs using Li metal anodes avoid cobalt by design. DRC cobalt export quota system (2025) and price recovery (~$24/lb Dec 2025 from 2024 trough) are relevant context but do not directly affect most companies here.

**Lithium Sulfide (Li₂S) — Critical Precursor:** Idemitsu's 1,000 MT/year (by June 2027) is committed exclusively to Toyota. As QuantumScape and Solid Power scale, the absence of a second qualified Li₂S supplier will become a material supply chain risk. **⚑ Shared supplier risk:** All three sulfide programs (Toyota, QuantumScape, Solid Power) are converging on a single-source precursor with no identified backup.

**Ceramic Separators:** QuantumScape / Murata Manufacturing (JDA Oct 2025) is the only documented third-party ceramic separator scale-up partnership. Murata's ceramics precision manufacturing experience maps directly to the requirements.

**Cathode and Anode Materials:** [POSCO Future M]({{< relref "../resources/posco-future-m.md" >}}) supplies both Factorial Energy (MOU Dec 2025) and Samsung SDI (Solid Power's cell manufacturing partner), creating an indirect materials supply overlap between Factorial and Solid Power. **⚑ Shared supplier flag.**

**Graphite (Conventional Anode):** Conventional graphite anodes are ~65%+ China-sourced. The shift to lithium metal anodes (solid-state) or sulfur cathodes (Li-S) largely sidesteps this risk — a strategic advantage of next-generation chemistries.

**U.S. Tariff Escalation (2025–2026):** Effective tariff on Chinese LFP batteries reaching ~82.4% by early 2026 (stacking multiple Section 301 layers) is accelerating supply chain diversification among Western BESS integrators. LG Energy Solution, Samsung SDI, and domestic U.S. capacity are beneficiaries; CATL and other Chinese cell makers face reduced access to U.S. market via Western integrators. Chinese integrators competing directly in European, Middle Eastern, and Latin American markets are largely unaffected.

### Supply Chain — Last Reviewed: 2026-04-04
