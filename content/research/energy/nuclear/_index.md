---
title: "Nuclear Energy Research"
date: 2026-03-25
lastmod: 2026-08-27
draft: false
description: "Research on nuclear power technologies, small modular reactors (SMRs), and the companies developing next-generation nuclear for AI datacenters, industrial power, and grid decarbonization."
research_area: "energy/nuclear"
last_reviewed: 2026-08-27
stale_after_days: 180
sitemap:
  changefreq: "monthly"
  priority: 0.9          # Higher for important research landing pages
  disable: false         # Set to true to exclude a page
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.


## Overview

Tracks small modular reactor (SMR) developers and advanced nuclear technologies, with particular focus on companies pursuing faster, cheaper deployment models and the emerging AI datacenter power demand that is accelerating commercial nuclear investment. Traditional large nuclear (1 GW+ plants) is covered only where relevant to SMR supply chain or regulatory precedent.

## Key Themes

- SMR construction cost and timeline — the core claim every company must prove (target: ~$5,000/kW, 3–5 years; industry history: $13,000+/kW, 10–15 years)
- Datacenter nuclear PPAs as the first commercial demand signal for SMRs
- NRC licensing pathway evolution: Combined License (COL) vs. Construction Permit + Operating License; modular construction resequencing approvals
- HALEU fuel supply chain as a potential chokepoint for non-LWR designs
- Shipyard/modular fabrication as the cost-reduction mechanism — analogous to offshore wind jacket manufacturing
- **The 2026 criticality wave and the DOE authorization track.** Five reactors reached criticality between June 4 and August 6, 2026 under DOE's Reactor Pilot Program (EO 14301, May 2025) and the Nuclear Energy Launch Pad: Antares Nuclear (June 4), Valar Atomics (June 18), Deployable Energy (June 30), Aalo Atomics (July 4) and Oklo's Groves isotope test reactor (Aug 5–6). This is the single largest development in the section since it was created — and the most easily misread. **Four of the five were zero-power or near-zero-power test reactors**, and none is a licensed commercial plant. DOE authorization is a separate, faster track from NRC commercial licensing and must never be conflated with it: as ANS puts it, "without NRC approval, none of the companies involved will be able to deploy their designs commercially."
- **"Criticality" is a low bar and is being marketed as a high one.** Katy Huff (former DOE Assistant Secretary for Nuclear Energy): a zero-power criticality test "can be achieved without making real engineering progress on fuel or design; it simply checks if you can multiply neutrons." INL Director John Wagner on the Antares milestone: "This is not electricity generation." Every company entry in this section now carries an explicit note on what its criticality event did and did not demonstrate.
- **Capital has decoupled from demonstrated output.** Valar Atomics raised $1B at a $6B valuation six weeks after a 100 kWt zero-power test; Antares raised $470M; X-energy IPO'd at ~$9.1B. Meanwhile Deep Fission's IPO was cut ~75% and trades ~57% below issue, Terrestrial Energy trades ~83% below its post-listing high, and Hadron Energy ~82% below. Private valuations and public marks are pricing the same sector very differently.
- **Defence procurement has become a second demand channel alongside datacenters.** The Army's **Janus Program** (Aug 26, 2026) commits up to **$2.2B** across five vendors — Radiant (Fort Benning), Antares (Fort Bragg), BWXT (Fort Campbell), General Atomics (Fort Hood), Westinghouse (Fort Drum) — for >20 microreactors, targeting one operating reactor by September 30, 2028. These reactors will be **regulated by the Army**, contractor-owned and contractor-operated: a **third** regulatory regime alongside DOE authorization and NRC licensing, with no civilian-nuclear precedent.
- **Fuel choice is now the clearest differentiator of schedule risk.** Developers using standard LEU and conventional fabrication (Aalo Atomics, Deep Fission, Terrestrial Energy, Blue Energy, Applied Atomics/mPower) sit outside both the HALEU allocation queue and the BWXT TRISO chokepoint. Developers using TRISO or HALEU (Kairos, X-energy, Radiant, NuCube, Antares, Oklo, Valar) do not. Antares' case is the sharpest: 2028 deployment targets against a Urenco HALEU contract whose UK source does not open until 2031.
- **Non-binding pipelines are being reported as capacity.** Deep Fission's own disclosure states its 18.5 GW pipeline is entirely non-binding LOIs "with no commitments to purchase electricity"; Terrestrial's 4 GW Riot Platforms arrangement is an MOU contemplating a gas bridge; Aalo's Crusoe partnership and Valar's Nvidia collaboration are both exploratory. Across the seven newest entries in this section, **executed PPAs total zero.**
- **The public-market cohort arrived in 2026.** X-energy (Nasdaq: XE, April), Deep Fission (FISN, June), Hadron Energy (HDRN, May SPAC) joined Terrestrial Energy (IMSR, Oct 2025 SPAC), Oklo (OKLO) and NuScale (SMR). SEC filings now provide a level of financial visibility this sector previously lacked — including going-concern warnings and ineffective disclosure controls at two of them.
- DOE's Reactor Pilot Program (Executive Order 14301, May 2025) and its successor Nuclear Energy Launch Pad (April 2026) as an accelerant for microreactor demonstration — DOE-authorized criticality/testing at national labs is a faster, separate track from full NRC commercial licensing, and should not be conflated with it
- **Regulatory challenge as strategy.** Valar Atomics is co-plaintiff with Last Energy and the states of Texas and Utah in a federal suit arguing the NRC lacks licensing authority over reactors below a defence-significance threshold. The Nuclear Innovation Alliance warns a plaintiff win could produce "a patchwork of state-level oversight."

## Deployment Status Tracker

### Grid-scale and commercial plants (NRC/CNSC licensed track)

| Company | Reactor | Fuel | Key Milestone | Commercial Target |
|---------|---------|------|---------------|-------------------|
| [GE Vernova Hitachi]({{< relref "ge-hitachi-bwrx300.md" >}}) | BWRX-300 (LWR, 300 MW) | LEU | **Construction underway** — Darlington ON (CNSC licence Apr 2025); **TVA Clinch River mandatory hearing held Aug 13, 2026, permit decision targeted Fall 2026** | Darlington 2029–2030 |
| [TerraPower]({{< relref "terrapower.md" >}}) | Natrium (SFR, 345 MW) | LEU metallic | **Nuclear construction commenced April 2026** — Kemmerer, WY; UK GDA Step 1 began June 2026 | 2030 |
| [Kairos Power]({{< relref "kairos-power.md" >}}) | KP-FHR (FHR, 50 MW) | TRISO/HALEU | Hermes nuclear construction underway; **⚑ NRC extended completion deadline to April 2029**; Hermes 2 construction began April 2026 | Hermes 2028; Hermes 2: 2030 |
| [X-energy]({{< relref "x-energy.md" >}}) (Nasdaq: XE) | Xe-100 (HTGR, 80 MW×4) | TRISO/HALEU | **NRC Final Safety Evaluation expected Nov 2026** — Seadrift, TX (Dow); permit anticipated H1 2027 | ~2030 |
| [Blue Energy]({{< relref "blue-energy.md" >}}) | **Now BWRX-300 ×5** (was modular LWR) | LEU | **⚑ Restructured Aug 13, 2026** as a 2.5 GW gas-plus-nuclear project with GE Vernova Hitachi, Victoria TX; FID targeted 2027 | Gas 2030; Nuclear from 2032 |
| [Terrestrial Energy]({{< relref "terrestrial-energy.md" >}}) (Nasdaq: IMSR) | IMSR (MSR, 2×195 MWe) | SALEU <5% | **Binding 77-acre ground lease, Texas A&M RELLIS (June 2026)**; two NRC topical reports approved; **no construction permit filed** | Early 2030s |
| [Applied Atomics]({{< relref "applied-atomics.md" >}}) | mPower (iPWR, 195 MWe) | LEU | **Exclusive land-based BWXT licence June 17, 2026**; **no NRC docket, no DOE authorization** | Not stated |
| [Hadron Energy]({{< relref "hadron-energy.md" >}}) (Nasdaq: HDRN) | Halo (iPWR, 10 MWe) | LEU+ 8% | NRC pre-application only (Project 99902144); PDC white paper under review; **no application filed** | 2030 (not credible) |

### DOE-authorized test reactors — the 2026 criticality cohort

**⚑ Read this table carefully.** Every entry below reached criticality under **DOE authorization**, not an NRC licence. Four of the five were zero-power or near-zero-power test reactors that generated little or no electricity. None can sell power commercially.

| Company | Reactor | Criticality | Site | What it was |
|---------|---------|-------------|------|-------------|
| [Antares Nuclear]({{< relref "antares-nuclear.md" >}}) | Mark-0 (Na heat-pipe, TRISO/HALEU) | **June 4, 2026** — 1st | INL Materials and Fuels Complex | **Zero power.** No power conversion system, no heat removal system |
| [Valar Atomics]({{< relref "valar-atomics.md" >}}) | Ward 250 (He HTGR, TRISO, 100 kWt) | **June 18, 2026** — 2nd | Utah San Rafael Energy Lab, Orangeville UT | **Zero-power fuelled criticality demo** (DOE's wording); a July 2 demo later drove a thermoelectric generator |
| [Deployable Energy]({{< relref "deployable-energy.md" >}}) | Unity (gas-cooled, 1 MWe) | **June 30, 2026** — 3rd | INL / NRIC | The only power-rated unit of the cohort; ~150 days from project kickoff; **first under the Nuclear Energy Launch Pad** |
| [Aalo Atomics]({{< relref "aalo-atomics.md" >}}) | Critical Test Reactor (Na thermal, LEU) | **July 4, 2026** — 4th | Aalo-X Campus, INL | **Full-scale zero-power** critical assembly — *not* the 10 MWe Aalo-X, which is not yet built |
| [Oklo]({{< relref "oklo.md" >}}) (NYSE: OKLO) | Groves Isotope Test Reactor (pool-type, 15 MWt) | **August 5–6, 2026** — 5th | Lockhart, TX (private land) | Isotope-production test reactor; **first DOE-authorized reactor critical on private land**; ~11 months greenfield to criticality |

### Other DOE-track and pre-criticality programmes

| Company | Reactor | Fuel | Key Milestone | Commercial Target |
|---------|---------|------|---------------|-------------------|
| [Oklo]({{< relref "oklo.md" >}}) | Aurora (SFR, 75 MW) | HALEU metallic | **DOE Preliminary Documented Safety Analysis approved June 11, 2026** — INL; excavation near complete; NRC PDC topical report approved May 2026; **no COLA docketed** | 2028 |
| [Radiant Industries]({{< relref "radiant-industries.md" >}}) | Kaleidos (He, portable, >1 MWe) | TRISO | Shipped to INL DOME; **first TRISO fuel delivered July 1, 2026**; five-phase test programme underway; **⚑ Army Janus award Aug 26, 2026 — Fort Benning, up to $750M, 15 units by 2030** | First units 2028 |
| [Deep Fission]({{< relref "deep-fission.md" >}}) (Nasdaq: FISN) | Gravity (borehole PWR, 45 MWt / 15 MWe) | LEU | **DOE Nuclear Safety Design Agreement Aug 6, 2026 — Gate 1 of 4, authorizes nothing operational**; **⚑ missed its own July 4, 2026 criticality target entirely** | 2027 (not credible) |
| [Terrestrial Energy]({{< relref "terrestrial-energy.md" >}}) | Project TETRA (MSR test reactor) | SALEU | DOE OTA executed Jan 6, 2026; **site and criticality date not disclosed**. Separate Project TEFLA fuel-salt pilot OTA Jan 22, 2026 | n/a (test) |
| [NuCube Energy]({{< relref "nucube-energy.md" >}}) | ART Reactor (heat-pipe HTGR) | TRISO | DOE Nuclear Energy Launch Pad **USA** selection April 2026 — deployment at Idaho State University, Pocatello | Not disclosed |
| [General Matter]({{< relref "general-matter.md" >}}) | *Enrichment, not a reactor* | — | $900M DOE award (Jan 2026); 100-acre DOE lease at Paducah KY; exploring Hanford FMEF; **no NRC licence issued** | 2029+ |

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Technology |
|---------|-----|-------|-----------|
| [Valar Atomics](https://www.valaratomics.com) | El Segundo, CA | Private ($1B Series B at $6B valuation, Aug 2026, led by Sequoia) | Helium HTGR microreactor, TRISO; Ward 250 zero-power criticality Utah June 2026; **sells synthetic fuels and heat, not reactors**; in-house TRISO fabrication; **suing the NRC over licensing authority** |
| [Antares Nuclear](https://antaresindustries.com) | Torrance, CA | Private (>$600M raised; $470M Series C Jul 2026) | Sodium heat-pipe TRISO/HALEU microreactor; **first criticality of the 2026 cohort**; Army Janus (Fort Bragg) and Air Force ANPI (JBSA); Urenco HALEU contract |
| [Aalo Atomics](https://www.aalo.com) | Austin, TX | Private ($136M confirmed; "$300M+" claimed) | Sodium-cooled, graphite-moderated, **LEU oxide** 10 MWe Aalo-1 in five-unit 50 MWe Pods; Crusoe partnership; **no HALEU or TRISO dependency** |
| [Deployable Energy](https://www.deployable.energy) | Houston, TX | Private (Solaris Energy Infrastructure & Hornbeck Offshore strategic investments, Aug 2026) | Unity Nuclear Battery — 1 MWe gas-cooled container-scale microreactor on LEU; criticality INL June 2026; $22.5B GridMarket pipeline; maritime programme |
| [Radiant Industries](https://www.radiantnuclear.com) | Los Angeles, CA | Private (~$525M+ through Series D) | Kaleidos — portable TRISO/helium microreactor >1 MWe; testing in DOE's DOME at INL; NRC R-50 Part 70 review; **Army Janus Fort Benning, up to $750M** |
| [Blue Energy](https://blueenergy.co) | Edinburgh / San Antonio | Series A ($45M) | Shipyard modular construction and gas-to-nuclear conversion; **flagship Victoria TX project restructured Aug 2026 around GE Vernova Hitachi BWRX-300s** |
| [Kairos Power](https://kairospower.com) | Alameda, CA | Private (~$650M raised) | KP-FHR fluoride salt + TRISO pebbles; Hermes construction underway Oak Ridge (deadline extended to 2029); Google/TVA PPA 500 MW by 2035 |
| [TerraPower](https://terrapower.com) | Bellevue, WA | Private | Natrium SFR + molten salt storage; Bill Gates-backed; **nuclear construction underway at Kemmerer WY**; UK GDA; Hyundai E&C EPC framework for up to 8 reactors |
| [Applied Atomics](https://www.appliedatomics.com) | Anchorage, AK / Los Angeles | Private (~$12M seed) | Exclusive land-based licence to BWXT's shelved **mPower** iPWR (195 MWe, LEU); vertically integrated IPP model; **no NRC docket** |
| [NuCube Energy](https://www.nucube.energy) | Pasadena, CA / Idaho Falls, ID | Private (~$13M raised) | Idealab Studio spinout; heat-pipe TRISO microreactor to 1,100 °C; DOE Launch Pad USA with Idaho State University |
| [General Matter](https://en.wikipedia.org/wiki/General_Matter) | Los Angeles, CA | Private (~$50M Series A + $900M DOE IDIQ) | Domestic LEU/HALEU enrichment at Paducah KY; **fuel-supply layer, not a reactor developer**; enrichment agreements signed with X-energy |

### Public Companies

| Ticker | Company | Technology |
|--------|---------|-----------|
| [OKLO](https://finance.yahoo.com/quote/OKLO) | [Oklo]({{< relref "oklo.md" >}}) | Aurora sodium fast microreactor (75 MW); Sam Altman chairman; **Groves isotope test reactor critical Aug 2026**; $3.0B liquidity; ~18 GW order book (mostly LOIs) |
| [XE](https://finance.yahoo.com/quote/XE) | [X-energy]({{< relref "x-energy.md" >}}) | **IPO April 2026 at $23/share, ~$1.02B raised**; Xe-100 pebble-bed HTGR; Dow Seadrift FSER due Nov 2026; TRISO-X TX-1 in interior build-out; ~$2.115B total DOE ARDP support |
| [SMR](https://finance.yahoo.com/quote/SMR) | [NuScale Power](https://www.nuscalepower.com) | LWR SMR; US600 design certification (2022) and **US460 Standard Design Approval (77 MWe/module, 2025)** — note these are different instruments; RoPower Doicești FID Feb 2026 with confidential conditions; ENTRA1/TVA PPA still not definitive; $1.9B cash |
| [IMSR](https://finance.yahoo.com/quote/IMSR) | [Terrestrial Energy]({{< relref "terrestrial-energy.md" >}}) | IMSR molten salt, 390 MWe plant, SALEU <5%, 7-year replaceable core-unit; $283.4M cash — strongest balance sheet of the recent listings; binding Texas A&M RELLIS lease; trades ~83% below post-listing high |
| [FISN](https://finance.yahoo.com/quote/FISN) | [Deep Fission]({{< relref "deep-fission.md" >}}) | Gravity borehole PWR (45 MWt / 15 MWe, LEU) a mile underground; **going-concern warning, ineffective disclosure controls**; IPO cut ~75%; trades ~57% below issue |
| [HDRN](https://finance.yahoo.com/quote/HDRN) | [Hadron Energy]({{< relref "hadron-energy.md" >}}) | Halo 10 MWe iPWR on 8% LEU+; NRC pre-application docket; senior hires from Westinghouse/TerraPower/NuScale; **$22.2M cash and $1.6M H1 R&D against a 2030 COD target** |
| [GEV](https://finance.yahoo.com/quote/GEV) | [GE Vernova / GE Hitachi]({{< relref "ge-hitachi-bwrx300.md" >}}) | BWRX-300; Darlington under construction; **TVA Clinch River permit decision targeted Fall 2026**; Blue Energy 2.5 GW Texas gas-plus-nuclear |
| [BWXT](https://finance.yahoo.com/quote/BWXT) | [BWX Technologies](https://www.bwxt.com) | Only US TRISO fuel producer; licensed mPower to Applied Atomics (retaining IP, manufacturing and royalties); **Army Janus Fort Campbell (BANR 20 MWe)**; backlog $8.4B; Q2 revenue $901.6M (+18%) |

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
    "height": "550",
    "tabs": [
      {
        "title": "Nuclear",
        "symbols": [
          {"s": "NYSE:OKLO", "d": "Oklo"},
          {"s": "NASDAQ:XE", "d": "X-energy"},
          {"s": "NYSE:SMR", "d": "NuScale Power"},
          {"s": "NASDAQ:IMSR", "d": "Terrestrial Energy"},
          {"s": "NASDAQ:FISN", "d": "Deep Fission"},
          {"s": "NYSE:GEV", "d": "GE Vernova"},
          {"s": "NYSE:BWXT", "d": "BWX Technologies"},
          {"s": "NYSEAMERICAN:LEU", "d": "Centrus Energy"}
        ],
        "originalTitle": "Nuclear"
      }
    ]
  }
  </script>
</div>
<!-- TradingView Widget END -->

### Incumbents

| Ticker | Company | Relevance |
|--------|---------|-----------|
| [LEU](https://finance.yahoo.com/quote/LEU) | [Centrus Energy](https://www.centrusenergy.com) | Only NRC-licensed US HALEU enricher; **$900M DOE task order July 2026** to move from demonstration to commercial-scale production at Piketon OH (plus up to $170M of HALEU purchase options); backlog $4.5B to 2040; supply agreement with X-energy Aug 2026 |
| [WSTG](https://finance.yahoo.com/quote/WSTG) | [Westinghouse](https://www.westinghousenuclear.com) | AP300 SMR; **eVinci microreactor selected for Army Janus at Fort Drum**; IMSR fuel plant contract with Terrestrial Energy at Springfields UK; established regulatory relationships |
| — | [BWXT Advanced Technologies](https://www.bwxt.com) | BANR 20 MWe HTGR selected for Army Janus at Fort Campbell; groundbreaking targeted late 2028, operations early 2030s |
| — | [General Atomics](https://www.ga.com) | GA-TES (5–20 MWe) selected for Army Janus at Fort Hood |
| — | [Urenco](https://www.urenco.com) | Urenco USA (Eunice NM) supplies LEU to Aalo Atomics and Deep Fission; a fifth enrichment cascade is being added toward 700,000 SWU over two years by early 2027; a **HALEU advanced fuels facility at Capenhurst, England is targeted operational 2031** and is Antares' commercial HALEU source |

## Supply Chain Notes

- **Reactor pressure vessels and heavy forgings:** Japan Steel Works and Doosan Heavy Industries are primary sources; lead times 3–5+ years; Hitachi relationship gives GEH priority access. **New in 2026:** TerraPower has added **HD Hyundai Heavy Industries** as preferred manufacturer for Natrium Reactor Enclosure System components and **Hyundai E&C** as EPC for up to eight reactors — Korean heavy industry is becoming a significant second source for US advanced reactor fabrication.
- **HALEU fuel:** Required for Oklo (Aurora), X-energy (Xe-100 via TRISO-X), Kairos (KP-FHR pebbles) and [Antares Nuclear]({{< relref "antares-nuclear.md" >}}) (TRISO at 19.75%). **Centrus** remains the only currently NRC-*licensed* US HALEU enricher and in July 2026 received a **$900M DOE task order** to expand the American Centrifuge Plant at Piketon, OH — first new commercial capacity expected **2029**, initially targeting 12 MT/yr. X-energy's TRISO-X TX-1 in Oak Ridge is the only US HALEU **fuel fabrication** plant under construction and holds the first NRC Category 2 fuel facility licence to process HALEU. [General Matter]({{< relref "general-matter.md" >}}) holds a $900M DOE award and a 100-acre DOE lease at Paducah but **had not received an NRC licence** as of last review. Urenco's UK HALEU facility does not open until **2031**.
  - **⚑ The near-term HALEU pool is federally allocated, not commercial.** Antares' Mark-0 ran on DOE-allocated HALEU downblended from NNSA scrap; Oklo's first Aurora core will use recovered EBR-II material. Multiple 2028-target programmes are drawing against the same finite, politically allocated inventory while their commercial contracts do not deliver until 2029–2031. **This is the tightest timing risk in the section.**
- **TRISO fuel:** **BWXT** (Lynchburg, VA) remains the primary US TRISO particle manufacturer, now supplying Kairos, X-energy, [Radiant Industries]({{< relref "radiant-industries.md" >}}), [NuCube Energy]({{< relref "nucube-energy.md" >}}) and Antares — five simultaneous first-of-a-kind programmes on one line. BWXT Advanced Fuels LLC (launched Aug 2025) is "exploring" a greenfield TRISO facility; **no site, investment figure or timeline has been announced.** Two partial alternatives have now emerged: **Standard Nuclear** (Oak Ridge, TN) fabricated Radiant's first TRISO delivery in July 2026, and [Valar Atomics]({{< relref "valar-atomics.md" >}}) is building its own co-located TRISO line in Utah on licensed German HOBEG technology.
  - **⚑ BWXT is simultaneously supplier and competitor.** It is Antares' sole fuel fabricator and, since August 2026, a direct competitor to Antares for Army Janus work.
- **Standard LEU — the quiet advantage:** [Aalo Atomics]({{< relref "aalo-atomics.md" >}}) (Urenco USA feedstock, **Global Nuclear Fuel** fabrication), [Deep Fission]({{< relref "deep-fission.md" >}}) (Urenco USA, standard PWR assemblies), [Terrestrial Energy]({{< relref "terrestrial-energy.md" >}}) (SALEU <5%), [Blue Energy]({{< relref "blue-energy.md" >}}) and [Applied Atomics]({{< relref "applied-atomics.md" >}}) (mPower, <5%) all avoid the HALEU and TRISO queues entirely. Aalo went from fuel contract signature to delivery in roughly a month — a schedule structurally impossible on either constrained pathway. **⚑ [Hadron Energy]({{< relref "hadron-energy.md" >}}) is the exception that proves the rule:** its 8% "LEU+" sits above the standard 5% ceiling, and no US commercial LEU+ enrichment or fabrication line operates at scale.
- **Fuel salt (new layer):** Terrestrial Energy's IMSR requires uranium dissolved in fluoride salt — a first-of-a-kind industrial process with no commercial precedent. Being addressed via **Westinghouse** at Springfields, UK and DOE's **Project TEFLA** fuel-line pilot. Neither facility exists yet.
- **Li-7 enrichment:** Required for Kairos's fluoride salt coolant (FLiBe); no US commercial Li-7 enrichment capability currently; DOE/ORNL developing domestic capability.
- **Nuclear-grade graphite:** Moderator for Aalo, Antares, Valar, Terrestrial and the HTGR designs generally. X-energy is investing up to $8M with **SGL Carbon** to double EU NBG-18 billet capacity by 2030 (enough for up to 8 reactors/yr); Aalo sources from **Amsted Graphite**; NRG Petten conducts irradiation testing for Terrestrial. Graphite behaviour under sustained flux is also a recurring open technical question for these designs.
- **Turbine generators:** GE Vernova, Siemens Energy (X-energy/Oklo named); **Baker Hughes** supplying Aalo's 10 MWe set and engaged by Terra Innovatum on sCO2 conversion; standard power gen supply chain, less constrained than nuclear-specific components.
- **Instrumentation & control — an emerging shared dependency:** **Paragon Energy Solutions** (a Mirion company) now appears across three unrelated programmes in this section — NuScale (HIPS platform: Module Protection System, Safety Display and Indication System, Plant Protection System, contracted June 2026), [Aalo Atomics]({{< relref "aalo-atomics.md" >}}), and [Hadron Energy]({{< relref "hadron-energy.md" >}}). Worth tracking as a potential single-vendor concentration at the I&C layer.
- **EPC and construction:** **Kiewit** appears twice (Oklo's Aurora at INL, Valar's Utah site). **Bechtel** (TerraPower), **Hyundai E&C** (TerraPower, up to 8 reactors with completion/price/performance guarantees), **Day & Zimmermann** (Deep Fission, above-ground scope only), **Clark Construction** (TRISO-X TX-1), **Fluor** and **Geiger Brothers** (Centrus Piketon expansion). **⚑ Deep Fission has no named drilling contractor** despite drilling being its entire critical path.
- **Sodium systems expertise:** TerraPower (Natrium), Oklo (Aurora), Aalo Atomics (thermal-spectrum pool) and Antares (heat pipes) all use sodium in some form; limited number of qualified fabricators and constructors with sodium reactor experience in the US.
- **Shared federal test infrastructure:** DOE/NRIC's DOME test bed and the Materials and Fuels Complex at Idaho National Laboratory are shared by multiple companies under the Reactor Pilot Program and Nuclear Energy Launch Pad — Antares, Deployable Energy, Aalo Atomics and Radiant Industries have all tested or are testing at INL. DOE authorization to test there is a separate, faster pathway than NRC commercial licensing and should not be read as commercial approval.

## Subsections

Individual company entries are listed in the tables above. See the [Energy]({{< relref "../_index.md" >}}) section for adjacent research on grid markets, batteries, solar and virtual power plants.
