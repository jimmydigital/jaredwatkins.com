---
title: "io.net"
date: 2026-08-15
lastmod: 2026-08-15
draft: false
description: "Solana-based decentralized GPU network (DePIN) that aggregates idle GPU capacity from data centers, crypto miners, and individual owners into on-demand clusters, verified by hourly proof-of-work checks and settled in the IO token — the largest token-incentivized example of automated supplier discovery and clustering for AI compute."
research_area: "compute-marketplaces"
source_urls:
  - "https://io.net/about-us"
  - "https://io.net/docs/guides/inception.md"
  - "https://io.net/docs/guides/workers/proof-of-work.md"
  - "https://io.net/docs/guides/architecture/io-network.md"
  - "https://www.coingecko.com/learn/what-is-io-net-io-token"
  - "https://ionet.medium.com/io-net-raises-30m-to-solve-the-ai-compute-shortage-by-building-the-internet-of-gpus-f9c5167c9f6e"
  - "https://www.theblock.co/post/280665/solana-depin-io-net-1-billion-token-valuation-funding"
  - "https://decrypt.co/315993/io-net-co-founder-tory-green-appointed-as-chair-of-io-net-foundation-gaurav-sharma-appointed-ceo-to-drive-next-phase-of-growth"
  - "https://crypto.news/ahmad-shadid-resigns-as-ceo-of-io-net/"
  - "https://cointelegraph.com/news/io-net-responds-to-gpu-metadata-attack"
  - "https://io.net/blog/io-net-20m-in-annualized-on-chain-revenue"
last_reviewed: 2026-08-15
stale_after_days: 90
related:
  - "compute-marketplaces/openrouter.md"
  - "compute-marketplaces/p2p-discovery-protocols-libp2p-kademlia.md"
  - "datacenters/distributed-compute/akash-network.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

io.net is a Solana-based decentralized physical infrastructure network (DePIN) that pools idle GPU capacity from independent data centers, crypto-mining operations, and individual hardware owners into on-demand compute clusters for AI/ML workloads. It is a token-incentivized alternative to OpenRouter's and Akash's coordination models: rather than posted-price aggregation or on-chain reverse auction, io.net verifies supplier hardware via recurring proof-of-work checks and lets suppliers self-organize into clusters that developers rent by the hour, settled in the IO token.

## Key Facts

- Founded: 2023, publicly launched at Solana Breakpoint (Amsterdam) after winning the 2023 Solana Grizzlython hackathon
- Type: Company / protocol — decentralized GPU compute marketplace (DePIN)
- Status: Private company (IO Research) operating a public, token-governed network; live mainnet
- Funding: $30M Series A, announced March 5, 2024, led by Hack VC with Multicoin Capital, 6th Man Ventures, M13, Delphi Digital, Solana Labs, Aptos Labs, and others participating; reported at roughly $1B fully-diluted token valuation (most of the round priced at an earlier $500M FDV, with only the final tranche reaching $1B)
- Scale claims: io.net's own materials cite "over 1 million idle GPUs accessible globally" and $20M+ in annualized on-chain revenue as of a 2026 blog post — see Claim Verification below before treating these as durable figures

## What It Is / How It Works

io.net sources GPU/CPU capacity from three pools: independent data centers with unsold capacity, cryptocurrency mining operations repurposing hardware, and individual owners running the **IO Worker** client. Suppliers are ranked by a combination of security compliance and measured upload/download speed, which feeds into the price offered for their hardware — the closest io.net gets to automated, criteria-based routing, though this is a supply-ranking mechanism rather than a per-request latency router in the CDN sense.

Hardware authenticity is checked through an hourly **proof-of-work verification** cycle: a binary-checker API issues a cryptographic puzzle (similar in spirit to Bitcoin/early-Ethereum PoW), a challenges API distributes it, and a results-submission API scores the response, confirming both claimed VRAM capacity and real-world performance. Devices are labeled Verified, Awaiting Verification, or Verification Failed, and a failed device loses block rewards and hiring eligibility until it passes again — a direct, purpose-built answer to the "is this GPU actually what it claims to be" trust problem that OpenRouter's documentation flags as unsolved for its own posted-price model.

Networking runs over a mesh VPN (io.net calls it the "IO Network") that connects nodes directly to one another and uses reverse tunnels to route around firewalls/NAT, plus a Ray-based clustering layer (io.net's own account credits adopting Ray — the open-source library OpenAI used to distribute GPT-3/4 training across 300,000+ CPUs/GPUs — with cutting its cluster-orchestration build time from over six months to under sixty days). Developers can provision a cluster via bare-metal deployment, on-demand VMs, or containers, and can pay in USDC or other accepted tokens with a 2% fee, or in IO with zero transaction fees; suppliers are paid out in IO tokens only.

## Claim Verification

### Claim: "Over 1 million idle GPUs accessible globally"

**Status:** Unverified / disputed

**Supporting sources:**
- [CoinGecko — What Is io.net?](https://www.coingecko.com/learn/what-is-io-net-io-token) — repeats the 1M+ figure from io.net's own materials.

**Refuting / questioning sources:**
- [Cointelegraph — io.net responds to GPU metadata attack](https://cointelegraph.com/news/io-net-responds-to-gpu-metadata-attack) — documents an April 25, 2024 SQL-injection attack on io.net's GPU metadata system; io.net's own X account acknowledged "virtual GPU abuse on the network that is spoofing approximately 400,000 workers," and active GPU connections reported by the network fell from roughly 600,000 to 10,000 once the resulting security fix forced a re-verification.

**Summary:** io.net's own security incident disclosure shows headline network-size figures have previously included large numbers of spoofed/fake workers; any current total-GPU claim from io.net's own dashboards should be treated as a marketing figure pending independent, third-party verification, consistent with this section's general skepticism toward self-reported DePIN network-size counters.

## Notable Developments

- **2026 (date of blog post unconfirmed in fetched content):** io.net reports surpassing $20M in annualized on-chain revenue — see Claim Verification note above; figure is self-reported and on-chain but not independently audited in sources reviewed for this entry.
- **2025-04-23:** Leadership change — co-founder Tory Green moved from CEO to Chairperson of the newly renamed io.net Foundation; Gaurav Sharma (former io.net CTO, prior senior roles at Binance, Agoda, and Amazon) appointed CEO.
- **2024-06-09:** Founder Ahmad Shadid resigned as CEO, citing "the best interest of the community and the project's future success"; COO Tory Green assumed the CEO role. Shadid separately contributed 1 million IO tokens to io.net's GPU Internet Foundation.
- **2024-04-25:** SQL-injection attack altered GPU metadata network-wide; io.net confirmed roughly 400,000 spoofed/fake workers had been present on the network and implemented Auth0/OKTA-based authentication and additional API hardening in response.
- **2024-03-05:** Closed $30M Series A led by Hack VC at a reported ~$1B fully-diluted token valuation; network reported at over 25,000 GPUs and 40,000 compute hours processed at announcement.
- **2023:** Founded (as IO Research); won the Solana Grizzlython hackathon and launched publicly at Solana Breakpoint in Amsterdam.

## Key People

**Gaurav Sharma** — CEO (since April 2025). Former CTO of io.net; prior senior roles in distributed systems and high-performance computing at Binance, Agoda, and Amazon.
- LinkedIn: not found (unable to confirm a verified profile URL — search results returned only ambiguous or unverified matches)

**Tory Green** — Chairperson, io.net Foundation (since April 2025); previously CEO (2024–2025). Stanford graduate; previously COO at Tiller Partners.
- LinkedIn: [linkedin.com/in/torygreen](https://www.linkedin.com/in/torygreen/)

**Ahmad Shadid** — Founder; former CEO (2023–June 2024), now departed from an operating role. Previously a quantitative engineer at Antbit, the trading firm io.net evolved out of.
- LinkedIn: not found — TODO: verify current profile

### People — Last Reviewed: 2026-08-15

## Sources

- [io.net — About Us](https://io.net/about-us) — company positioning, mission
- [io.net Docs — Inception](https://io.net/docs/guides/inception.md) — Ray adoption and clustering rationale
- [io.net Docs — Proof of Work](https://io.net/docs/guides/workers/proof-of-work.md) — worker verification mechanism
- [io.net Docs — IO Network architecture](https://io.net/docs/guides/architecture/io-network.md) — mesh VPN networking model
- [CoinGecko — What Is io.net (IO)?](https://www.coingecko.com/learn/what-is-io-net-io-token) — supplier sourcing, PoTL, payment mechanics, funding, network scale
- [io.net (Medium) — io.net Raises $30M to Solve the AI Compute Shortage](https://ionet.medium.com/io-net-raises-30m-to-solve-the-ai-compute-shortage-by-building-the-internet-of-gpus-f9c5167c9f6e) — Series A amount, investors, date, early network scale
- [The Block — Solana DePIN io.net hits $1 billion token valuation](https://www.theblock.co/post/280665/solana-depin-io-net-1-billion-token-valuation-funding) — valuation structure (FDV, tranches)
- [Decrypt — Tory Green appointed Chair, Gaurav Sharma appointed CEO](https://decrypt.co/315993/io-net-co-founder-tory-green-appointed-as-chair-of-io-net-foundation-gaurav-sharma-appointed-ceo-to-drive-next-phase-of-growth) — 2025 leadership transition
- [crypto.news — Ahmad Shadid resigns as CEO of io.net](https://crypto.news/ahmad-shadid-resigns-as-ceo-of-io-net/) — 2024 leadership transition
- [Cointelegraph — io.net responds to GPU metadata attack](https://cointelegraph.com/news/io-net-responds-to-gpu-metadata-attack) — spoofed-worker incident, remediation
- [io.net — io.net Breaks $20M in Annualized On-Chain Revenue](https://io.net/blog/io-net-20m-in-annualized-on-chain-revenue) — revenue claim (self-reported)
