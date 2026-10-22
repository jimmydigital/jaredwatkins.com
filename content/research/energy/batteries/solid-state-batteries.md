---
title: "Solid-State Batteries"
date: 2026-03-23
lastmod: 2026-10-20
draft: false
description: "Overview of solid-state battery technology: pilot-line production at QuantumScape and Solid Power, Factorial's June 2026 Nasdaq listing, and the 2027 and later automotive timelines that remain company targets."
research_area: "energy/batteries"
source_urls:
  - "https://www.idtechex.com/en/research-article/solid-state-battery-commercialization-mass-production-taking-off/32942"
  - "https://interactanalysis.com/insight/when-will-solid-state-batteries-enter-commercial-production/"
  - "https://electrek.co/2025/10/08/toyota-aims-to-launch-worlds-first-all-solid-state-ev-batteries/"
  - "https://www.sec.gov/Archives/edgar/data/0001811414/000119312526312423/qs-ex99_1.htm"
  - "https://www.nasdaq.com/press-release/solid-power-reports-second-quarter-2026-results-2026-08-04"
  - "https://electrek.co/2026/06/08/solid-state-ev-battery-maker-joins-nasdaq-after-745-mi-range-test/"
  - "https://electrek.co/2026/03/23/donut-lab-solid-state-battery-5-tests-no-energy-density-cycle-life/"
  - "https://www.press.bmwgroup.com/usa/article/detail/T0453702EN_US/bmw-group-and-solid-power-take-next-step-in-assb-development-path:-new-partner-samsung-sdi-joins-the-effort"
last_reviewed: 2026-10-20
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Solid-state batteries replace the liquid or gel electrolyte in conventional lithium-ion cells with a solid material, aiming at higher energy density, better thermal safety and longer cycle life. As of October 2026 the technology is moving from advanced prototypes to pilot-scale production: QuantumScape is ramping a pilot line and shipping samples to automakers, Solid Power is installing a continuous electrolyte pilot line, and Factorial Energy went public in June 2026. Automotive mass-production dates remain company announcements, generally 2027 or later, and the term "solid-state" in announcements often includes semi-solid cells.

## Key Facts

- **Key difference from Li-ion:** a solid electrolyte instead of liquid or gel, which makes a lithium metal anode practical
- **Energy density:** company-reported cell figures vary by platform and by whether the cell is semi-solid or all-solid-state; see the individual entries for [QuantumScape]({{< relref "quantumscape.md" >}}), [Factorial Energy]({{< relref "factorial-energy.md" >}}) and [Donut Lab]({{< relref "donut-lab.md" >}}) rather than a single range
- **Commercial status:** pilot-line production and sample shipments; vehicle programs targeting 2027 and later; no independently confirmed automotive-scale production as of this review
- **Stated timelines:** Toyota aims to launch its first all-solid-state battery EV in 2027 or 2028 ([Electrek](https://electrek.co/2025/10/08/toyota-aims-to-launch-worlds-first-all-solid-state-ev-batteries/)); Samsung SDI targets mass production of all-solid-state batteries by 2027 from its Suwon "S-Line" pilot line ([IDTechEx](https://www.idtechex.com/en/research-article/solid-state-battery-commercialization-mass-production-taking-off/32942)); Hyundai plans partial mass production by 2027 and full-scale operations by 2030 ([IDTechEx](https://www.idtechex.com/en/research-article/solid-state-battery-commercialization-mass-production-taking-off/32942)); BYD and CATL plan small-scale production around 2027 ([Interact Analysis](https://interactanalysis.com/insight/when-will-solid-state-batteries-enter-commercial-production/))
- **Main electrolyte approaches:** oxide (e.g., LLZO), sulfide and polymer, each with distinct trade-offs

## What It Is / How It Works

In a conventional lithium-ion battery, lithium ions move between electrodes through a liquid electrolyte. That liquid is flammable, degrades over cycles, and effectively limits the cell to a graphite anode, because lithium metal reacts badly with the liquid. Solid-state cells swap the liquid for a solid ionic conductor, which removes the flammability risk, allows a lithium metal anode (roughly 10 times the theoretical capacity of graphite) and enables higher cell voltages.

**Oxide electrolytes** (e.g., LLZO) are chemically stable with wide electrochemical windows, but are brittle, hard to make in thin layers and have high interface resistance. Toyota and several academic groups work extensively in this area.

**Sulfide electrolytes** have ionic conductivity close to liquid electrolytes and are the most performance-competitive, but they react with moisture and air, which complicates manufacturing. [Solid Power]({{< relref "solid-power.md" >}}) and [Idemitsu Kosan]({{< relref "idemitsu-solid-state.md" >}}) are sulfide-route developers, and the lithium sulfide precursor is a supply bottleneck; see [Sulfur]({{< relref "../resources/sulfur.md" >}}).

**Polymer electrolytes** are flexible and easier to process but typically need elevated operating temperatures and have lower ionic conductivity. They are the most commercially mature but offer less dramatic performance gains.

The key open challenges are low interface resistance between the solid electrolyte and the electrodes (especially at the anode), thin and uniform solid electrolyte layers at scale, and managing lithium metal volume change during cycling, which can crack solid electrolytes. Timelines are also affected by upstream inputs, notably [lithium]({{< relref "../resources/lithium.md" >}}) metal, sulfur-derived Li₂S, and cathode materials from suppliers such as [POSCO Future M]({{< relref "../resources/posco-future-m.md" >}}).

## Notable Developments

- **2026-08-04:** Solid Power reports Q2 2026: SK On line installation agreement complete, Joint Evaluation Agreement with Samsung SDI and BMW advancing, pilot line startup planned Q4 2026, liquidity $419.3 million. ([Nasdaq](https://www.nasdaq.com/press-release/solid-power-reports-second-quarter-2026-results-2026-08-04))
- **2026-07:** QuantumScape's Q2 shareholder letter reports Eagle Line core tool uptime above 90%, plans to double cell output again in H2 2026, an updated PowerCo arrangement, and liquidity of $859.0 million. ([SEC](https://www.sec.gov/Archives/edgar/data/0001811414/000119312526312423/qs-ex99_1.htm))
- **2026-06-18:** Honda announces a multi-year agreement with QuantumScape on solid-state lithium-metal batteries. ([SEC](https://www.sec.gov/Archives/edgar/data/0001811414/000119312526312423/qs-ex99_1.htm))
- **2026-06-08:** Factorial Energy begins trading on Nasdaq (FAC) after a merger with SPAC Cartesian Growth Corp III, valued at about $1.3 billion with about $110 million in gross proceeds. ([Electrek](https://electrek.co/2026/06/08/solid-state-ev-battery-maker-joins-nasdaq-after-745-mi-range-test/))
- **2026-03-23:** Donut Lab's fifth VTT test report released; none of the five tests measured the claimed 400 Wh/kg energy density or 100,000-cycle life. ([Electrek](https://electrek.co/2026/03/23/donut-lab-solid-state-battery-5-tests-no-energy-density-cycle-life/))
- **2025-10-31:** Samsung SDI joins the BMW and Solid Power all-solid-state effort. ([BMW Group Press](https://www.press.bmwgroup.com/usa/article/detail/T0453702EN_US/bmw-group-and-solid-power-take-next-step-in-assb-development-path:-new-partner-samsung-sdi-joins-the-effort))
- **2025-10:** Toyota, Sumitomo Metal Mining and Idemitsu detail their path to the first all-solid-state battery EV in 2027 or 2028, including a planned 1,000 t per year lithium sulfide plant. ([Electrek](https://electrek.co/2025/10/08/toyota-aims-to-launch-worlds-first-all-solid-state-ev-batteries/))

## Key Organizations

**Startups and development partners (primary focus):**

- **Factorial Energy** (Nasdaq: FAC) — FEST® semi-solid platform and Solstice™ all-solid-state platform; multi-OEM joint development agreements; listed June 2026. See [dedicated entry]({{< relref "factorial-energy.md" >}}).
- **Donut Lab** — claims production-vehicle deployment through Verge Motorcycles; thermal and fast-charge tests published via VTT, energy density and cycle life unverified. See [dedicated entry]({{< relref "donut-lab.md" >}}).
- **ProLogium** — oxide-based solid-state developer. See [dedicated entry]({{< relref "prologium.md" >}}).
- **Adden Energy** — Harvard spinout developing thin-film solid-state cells. See [dedicated entry]({{< relref "adden-energy.md" >}}).
- **Lyten** — lithium-sulfur with 3D graphene, adjacent to solid-state. See [dedicated entry]({{< relref "lyten.md" >}}).
- **Idemitsu Kosan** — lithium sulfide and sulfide electrolyte supplier tied to Toyota. See [dedicated entry]({{< relref "idemitsu-solid-state.md" >}}).

**Public pure-plays:**

- **QuantumScape** (NYSE: QS) — see [dedicated entry]({{< relref "quantumscape.md" >}}).
- **Solid Power** (NASDAQ: SLDP) — electrolyte supplier model; see [dedicated entry]({{< relref "solid-power.md" >}}).

**Incumbents (context only):**

- **Toyota** — targets first all-solid-state BEV in 2027 or 2028.
- **Samsung SDI** — S-Line pilot line in Suwon; stated 2027 mass-production goal.
- **CATL** 🇨🇳 and **BYD** 🇨🇳 — small-scale production planned around 2027 per Interact Analysis; treat company-issued claims with additional skepticism.

## Claim Verification

### Claim: All-solid-state batteries will reach automotive mass production in 2027–2028
**Status:** Unverified

**Supporting sources:**
- [Electrek](https://electrek.co/2025/10/08/toyota-aims-to-launch-worlds-first-all-solid-state-ev-batteries/) — Toyota states a 2027 or 2028 launch target and has METI certification to manufacture the batteries in Japan
- [IDTechEx](https://www.idtechex.com/en/research-article/solid-state-battery-commercialization-mass-production-taking-off/32942) — Samsung SDI and Hyundai state 2027 targets

**Refuting / questioning sources:**
- [Electrek](https://electrek.co/2025/10/08/toyota-aims-to-launch-worlds-first-all-solid-state-ev-batteries/) — notes Toyota has promised this technology for years and that Mercedes-Benz has already claimed a first on-road car with a lithium-metal solid-state battery
- [Interact Analysis](https://interactanalysis.com/insight/when-will-solid-state-batteries-enter-commercial-production/) — timelines are company announcements rather than confirmed schedules, and "solid-state" announcements include semi-solid cells

**Summary:** The 2027–2028 dates are stated targets without independently confirmed production; pilot-line progress at QuantumScape and Solid Power is real but sub-commercial.

## Sources

- [Solid-State Battery Commercialization: Mass Production Taking Off — IDTechEx](https://www.idtechex.com/en/research-article/solid-state-battery-commercialization-mass-production-taking-off/32942)
- [When Will Solid-State Batteries Enter Commercial Production? — Interact Analysis](https://interactanalysis.com/insight/when-will-solid-state-batteries-enter-commercial-production/)
- [Toyota aims to launch world's first all-solid-state EV batteries — Electrek (Oct 2025)](https://electrek.co/2025/10/08/toyota-aims-to-launch-worlds-first-all-solid-state-ev-batteries/)
- [QuantumScape Q2 2026 shareholder letter — SEC](https://www.sec.gov/Archives/edgar/data/0001811414/000119312526312423/qs-ex99_1.htm)
- [Solid Power Reports Second Quarter 2026 Results — Nasdaq](https://www.nasdaq.com/press-release/solid-power-reports-second-quarter-2026-results-2026-08-04)
- [Solid-state EV battery maker joins Nasdaq — Electrek (Jun 2026)](https://electrek.co/2026/06/08/solid-state-ev-battery-maker-joins-nasdaq-after-745-mi-range-test/)
- [Donut Lab: 5 independent tests in, still no energy density or cycle life data — Electrek (Mar 2026)](https://electrek.co/2026/03/23/donut-lab-solid-state-battery-5-tests-no-energy-density-cycle-life/)
- [BMW and Solid Power: New Partner Samsung SDI Joins — BMW Group Press (Oct 2025)](https://www.press.bmwgroup.com/usa/article/detail/T0453702EN_US/bmw-group-and-solid-power-take-next-step-in-assb-development-path:-new-partner-samsung-sdi-joins-the-effort)
