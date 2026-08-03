---
title: Market Info
date: 2016-12-17
menu: main
weight: 10
disable_comments: true
---
One page reference for various market info<!--more-->

## Currency

<div style="display:flex; gap:10px; flex-wrap:wrap; align-items:flex-start;">
  <a href="http://www.weblinks247.com/exrate/24hr-gbp-large.gif"><img src="http://www.weblinks247.com/exrate/24hr-gbp-small.gif" style="height:160px; width:auto;"></a>
  <a href="http://www.weblinks247.com/exrate/24hr-euro-large.gif"><img src="http://www.weblinks247.com/exrate/24hr-euro-small.gif" style="height:160px; width:auto;"></a>
  <a href="http://www.weblinks247.com/exrate/24hr-jpy-large.gif"><img src="http://www.weblinks247.com/exrate/24hr-jpy-small.gif" style="height:160px; width:auto;"></a>
</div>

## US Bonds

**Treasury yields — trailing 12 months**

All four maturities on one axis. Click through for the interactive version on FRED.

<div style="margin-bottom:1.5em;">
{{< fredgraph id="DGS3MO,DGS2,DGS10,DGS30" months="12" title="US Treasury yields (3mo, 2yr, 10yr, 30yr), trailing 12 months" >}}
</div>

**Current yield curve** — today in blue vs. one year ago

<div style="margin-bottom:0.5em;">
  <iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vS76exe-zQWeIvIKuq86Fw0YyqxHeHdB4YKQ0l6sHD_h7tTxU6FtnrxBlBYsawje8a2gofZirmh8nZ5/pubchart?oid=1592400845&amp;format=interactive" width="100%" height="450" frameborder="0" scrolling="no" title="US Treasury Yield Curve"></iframe>
</div>

<p style="font-size:0.85em;">Yield curve chart via <a href="https://www.retirebeforedad.com/yield-curve-chart">RetireBeforeDad.com</a>, data from <a href="https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics">US Treasury</a>. Long-run history: <a href="https://fred.stlouisfed.org/graph/?id=DGS3MO,DGS2,DGS10,DGS30">FRED</a>.</p>

**10y − 2y spread** — negative means an inverted curve

<iframe src="https://govspending.org/embed/yield-curve/" width="100%" height="300" frameborder="0" title="Yield Curve (10y - 2y Spread) - via govspending.org"></iframe>

## Money Supply

**M2** — 5yr, monthly, seasonally adjusted

<div style="margin-bottom:1.5em;">
{{< fredgraph id="M2SL" months="60" title="M2 money supply, billions of dollars, 5 years" >}}
</div>

## Equities

<iframe src="https://s.tradingview.com/embed-widget/mini-symbol-overview/?symbol=AMEX%3ASPY&locale=en&colorTheme=light&dateRange=12M&isTransparent=false&autosize=true&largeChartUrl=" width="100%" height="220" frameborder="0" allowtransparency="true" scrolling="no"></iframe>

## Crypto

<iframe src="https://s.tradingview.com/embed-widget/mini-symbol-overview/?symbol=COINBASE%3ABTCUSD&locale=en&colorTheme=light&dateRange=12M&isTransparent=false&autosize=true&largeChartUrl=" width="100%" height="220" frameborder="0" allowtransparency="true" scrolling="no"></iframe>

## Energy

**Crude Oil (WTI)**

<iframe src="https://s.tradingview.com/embed-widget/mini-symbol-overview/?symbol=TVC%3AUSOIL&locale=en&colorTheme=light&dateRange=12M&isTransparent=false&autosize=true&largeChartUrl=" width="100%" height="220" frameborder="0" allowtransparency="true" scrolling="no"></iframe>

**Natural Gas** — Henry Hub spot, trailing 12 months

<div style="margin-bottom:1.5em;">
{{< fredgraph id="DHHNGSP" months="12" title="Henry Hub natural gas spot price, trailing 12 months" >}}
</div>

**Uranium** — no public spot price feed exists, so this tracks the Global X Uranium ETF (URA) as a proxy

<iframe src="https://s.tradingview.com/embed-widget/mini-symbol-overview/?symbol=AMEX%3AURA&locale=en&colorTheme=light&dateRange=12M&isTransparent=false&autosize=true&largeChartUrl=" width="100%" height="220" frameborder="0" allowtransparency="true" scrolling="no" title="Global X Uranium ETF (URA)"></iframe>

## Metals

**Gold** — 24h · 6mo · 1yr · 5yr

<div style="display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin-bottom:1.5em;">
  <a href="https://www.kitco.com/charts/gold"><img src="https://www.kitco.com/chart-images/images/live/gold.gif" style="width:100%; height:auto; display:block;"></a>
  <a href="https://www.kitco.com/charts/gold"><img src="https://www.kitco.com/chart-images/LFgif/AU0182nyb.gif" style="width:100%; height:auto; display:block;"></a>
  <a href="https://www.kitco.com/charts/gold"><img src="https://www.kitco.com/chart-images/LFgif/AU0365nyb.gif" style="width:100%; height:auto; display:block;"></a>
  <a href="https://www.kitco.com/charts/gold"><img src="https://www.kitco.com/chart-images/LFgif/AU1825nyb.gif" style="width:100%; height:auto; display:block;"></a>
</div>

**Silver** — 24h · 6mo · 1yr · 5yr

<div style="display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin-bottom:1.5em;">
  <a href="https://www.kitco.com/charts/silver"><img src="https://www.kitco.com/chart-images/images/live/silver.gif" style="width:100%; height:auto; display:block;"></a>
  <a href="https://www.kitco.com/charts/silver"><img src="https://www.kitco.com/chart-images/LFgif/AG0182nyb.gif" style="width:100%; height:auto; display:block;"></a>
  <a href="https://www.kitco.com/charts/silver"><img src="https://www.kitco.com/chart-images/LFgif/AG0365nyb.gif" style="width:100%; height:auto; display:block;"></a>
  <a href="https://www.kitco.com/charts/silver"><img src="https://www.kitco.com/chart-images/LFgif/AG1825nyb.gif" style="width:100%; height:auto; display:block;"></a>
</div>

**Palladium** — 6mo · 1yr · 5yr

<div style="display:grid; grid-template-columns:repeat(3,1fr); gap:8px; margin-bottom:1.5em;">
  <a href="https://www.kitco.com/charts/palladium"><img src="https://www.kitco.com/chart-images/LFgif/PD0182nyb.gif" style="width:100%; height:auto; display:block;"></a>
  <a href="https://www.kitco.com/charts/palladium"><img src="https://www.kitco.com/chart-images/LFgif/PD0365nyb.gif" style="width:100%; height:auto; display:block;"></a>
  <a href="https://www.kitco.com/charts/palladium"><img src="https://www.kitco.com/chart-images/LFgif/PD1825nyb.gif" style="width:100%; height:auto; display:block;"></a>
</div>

**Copper**

<iframe src="https://s.tradingview.com/embed-widget/mini-symbol-overview/?symbol=COPPER&locale=en&colorTheme=light&dateRange=12M&isTransparent=false&autosize=true&largeChartUrl=" width="100%" height="220" frameborder="0" allowtransparency="true" scrolling="no"></iframe>

**Aluminum**

<iframe src="https://s.tradingview.com/embed-widget/mini-symbol-overview/?symbol=ALUMINUM&locale=en&colorTheme=light&dateRange=12M&isTransparent=false&autosize=true&largeChartUrl=" width="100%" height="220" frameborder="0" allowtransparency="true" scrolling="no" title="Aluminum (ALIUSD)"></iframe>
