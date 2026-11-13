---
title: "x402: Machine-to-Machine Payments"
date: 2026-08-04
lastmod: 2026-11-12
draft: false
description: "x402 — created by Coinbase and governed since 2026 by the Linux Foundation's x402 Foundation — revives the unused HTTP 402 'Payment Required' status code to let AI agents pay per API call in stablecoins with no account or human approval step; the leading candidate settlement layer for an ad-hoc inference-compute marketplace, with more than 196 million transactions and $42 million settled by November 2026 but sharply lower activity since its late-2025 peak."
research_area: "compute-marketplaces"
source_urls:
  - "https://docs.cdp.coinbase.com/x402/welcome"
  - "https://www.chainalysis.com/blog/x402-agentic-payments-adoption/"
  - "https://finance.yahoo.com/markets/crypto/articles/coinbase-expands-x402-ai-agent-123512115.html"
  - "https://decrypt.co/resources/what-is-x402-how-ai-agents-pay-with-crypto"
  - "https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol"
  - "https://docs.cdp.coinbase.com/x402/bazaar"
last_reviewed: 2026-11-12
stale_after_days: 90
related:
  - "compute-marketplaces/openrouter.md"
  - "compute-marketplaces/ietf-ai-service-discovery-drafts.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Glossary

- **HTTP 402** — The "Payment Required" HTTP status code, reserved in the original HTTP specification but left undefined and essentially unused since the 1990s until x402 revived it as a machine-readable payment challenge.
- **Facilitator** — A service (Coinbase runs one; the protocol allows others) that verifies and settles an x402 payment on a seller's behalf, so the seller doesn't need to run its own blockchain infrastructure.
- **CAIP-2** — A chain-agnostic network identifier format (e.g., `eip155:8453` for Base) that lets a single x402 client address multiple blockchains without protocol-specific branching.
- **Bazaar** — x402's discovery layer: a catalog of payment-gated services indexed by Coinbase's facilitator, queryable by search, listing, or merchant address — the piece of the protocol most directly relevant to a compute marketplace's discovery layer.
- **x402 Foundation** — The Linux Foundation-hosted body that has governed the protocol since Coinbase contributed it in 2026.

## Summary

x402 is an open payment protocol, created by Coinbase, released in May 2025 and governed since July 2026 by the x402 Foundation under the Linux Foundation, that lets a server demand payment for an API call by responding with the long-dormant HTTP 402 status code and a machine-readable payment specification; the requesting client (human-operated or a fully autonomous AI agent) constructs and signs a stablecoin payment, resubmits the request with proof of payment attached, and receives the resource once the seller verifies settlement. It is the most advanced production example of the third layer this section tracks — machine-to-machine settlement — and on-chain data shows genuine, still-small-but-growing adoption rather than a purely theoretical protocol: over 100 million agentic transactions on the Base network within roughly three quarters of launch, per independent on-chain analysis from Chainalysis, and more than 196 million transactions across 12 chains by November 1, 2026 — though monthly activity has fallen far below its late-2025 peak, to about 5.1 million transactions worth roughly \$274,000 in October 2026.

## Key Facts

- Type: open payment protocol (not a company; created by Coinbase's Developer Platform team)
- Governance: x402 Foundation, hosted by the Linux Foundation — launch announced April 2, 2026 with supporters including Amazon Web Services, Google, Microsoft, Stripe, Visa, Mastercard, Circle and Cloudflare; fully operational July 14, 2026 with 40 member organizations (57 by November 2026, per Decrypt); Michael Hursta has been executive director since October 1, 2026
- Released: May 2025 (per Decrypt's November 2026 explainer and other secondary sources; Coinbase's original launch page was not readable when checked). Version 2, adding wallet-based identity, automatic service discovery and more chains, followed in December 2025; batch settlement of signed vouchers was added in May 2026
- Primary chain: Base (Coinbase's Ethereum L2), with payments mostly in USDC; the protocol is chain-agnostic via CAIP-2 identifiers and was in use on 12 chains as of November 1, 2026, including Solana, Polygon and Arbitrum
- Settlement assets: any ERC-20 via Permit2, or EIP-3009 tokens (USDC, EURC) for the smoothest flow — no custom token; uses existing stablecoins
- Independent on-chain adoption metric (Chainalysis, using on-chain transaction signatures, published 2026-06-03): agentic x402 transactions on Base crossed 100 million cumulative transactions within about three quarters of going live, after a surge in Q4 2025 driven substantially by a speculative "pay-to-mint" meme-coin campaign (PING) rather than organic commerce
- Self-reported adoption metric (Coinbase, as of April 21, 2026, per Yahoo Finance/Cryptonews coverage of the Agent.market launch): ~69,000 active AI agents on x402, 165 million cumulative transactions, ~\$50 million cumulative volume — an average call value under \$0.31, confirming the protocol is still calibrated for micropayments rather than bulk settlement
- Latest cumulative figures (Fireblocks, citing tracker agenteconomy.to, as relayed by Decrypt): more than 196 million transactions and more than \$42 million settled across 12 chains as of November 1, 2026; October 2026 alone saw about 5.1 million transactions worth about \$274,000. More than half of lifetime transactions came from a two-month burst of automated PING token trading in late 2025. Coinbase says more than 97% of on-chain agent transactions in Q2 2026 used x402 — a vendor claim

## What It Is / How It Works

**The core flow.** A buyer (an AI agent, in the use case most relevant here) requests a resource — an API call, a data feed, a compute job — from a server. If payment is required, the server responds with HTTP 402 and a `PAYMENT-REQUIRED` header specifying price, accepted assets, and network. The buyer's client constructs a signed stablecoin payment payload (`PAYMENT-SIGNATURE` header) and resubmits the request. The server verifies and settles the payment through a **facilitator** — Coinbase runs a hosted facilitator (documented in mid-2026 with a free tier of 1,000 transactions/month, then \$0.001/transaction; pricing was not re-confirmed at this review) — so a seller never has to run their own blockchain node or wallet infrastructure to accept payment. The entire loop happens inside a single HTTP request/response cycle with no account creation, session, or API key exchange beforehand, which is the specific friction x402 is designed to remove: per Coinbase's own docs, the protocol targets "API services paid per request," "AI agents that autonomously pay for API access," and "microservices and tooling monetized via microtransactions."

**Why this matters for an inference marketplace specifically.** A buyer's agent discovering an inference provider through any of the discovery mechanisms elsewhere in this section (OpenRouter's directory, a DHT-based swarm, a future IETF Resource Provider Card) still needs a way to actually pay that provider per call, without a pre-negotiated contract or a human approving each transaction — exactly the gap x402 targets. Coinbase also documents a **discovery layer called Bazaar** — a catalog of payment-gated services discovered by its facilitator, searchable with relevance ranking that blends query match with usage signals such as 30-day call counts and unique payers, and reachable through an SDK, REST APIs, or an MCP server without an API key — meaning the same stack that solves settlement is also positioning itself to solve discovery, which would collapse two of this section's three layers (discovery and payment) into a single vendor-provided stack if it gains adoption. Coinbase's documentation describes working interfaces but does not label Bazaar's release status, and no usage figures for it were found.

**Adoption reality check.** Independent on-chain data (Chainalysis, analyzing wallets that interact directly with the x402 contract on Base) shows real but immature adoption: transaction volume surged from near-zero in mid-2025 to over 100 million cumulative transactions by Q1 2026, but a large share of the Q4 2025 surge was driven by PING, a speculative "pay-to-mint" meme-coin campaign that turned the 402 payment loop into a repeatable game rather than genuine machine-to-machine commerce — one campaign alone processed over 150,000 transactions in its first month. Growth moderated in Q1 2026 as speculative activity cooled, and by October 2026 monthly volume was about 5.1 million transactions worth roughly \$274,000 — an average of about five cents per transaction, and a small fraction of the late-2025 peak. More encouraging signals in the same data: the share of transaction volume from calls worth \$1 or more rose from 49% (early 2025) to 95% (early 2026), meaning the protocol's economic weight has shifted toward real value transfer rather than sub-cent novelty transactions; wallets that test the protocol once are converting to repeat payers four times faster than they did six months earlier; and week-over-week wallet retention, while volatile, is trending upward. Chainalysis's own read: "x402 on Base has moved beyond proof-of-concept... but mass adoption remains distant," with the current user base skewing toward crypto-native, newly created wallets rather than established institutional participants.

**The discovery+payment product that already exists.** In April 2026, Coinbase launched **Agent.market** (called Agentic.Market in some later coverage), described in coverage as an "AI agent app store" — a permissionless, browsable directory of x402-payable services across seven categories (reasoning, data, media, search, social, infrastructure, and trading), with providers reportedly including OpenAI, Bloomberg, CoinGecko, and AWS Lambda listed at launch. Listing is permissionless — any service provider can add itself without Coinbase's approval — which directly reduces the discovery friction this section identifies as unsolved elsewhere; x402 creator Erik Reppel is quoted framing this as reducing "customer acquisition activation costs for businesses, as robots can now access services at a very low setup cost without needing API keys." Agent.market is the closest existing product to a combined discovery-plus-payment layer for machine-to-machine commerce, though it launched alongside — not as a replacement for — the self-reported adoption figures above, and no inference-compute-specific category is confirmed among the seven listed as of this review.

**Governance and competing rails.** Coinbase contributed x402 to the Linux Foundation in 2026, and the x402 Foundation became operational in July 2026 with 40 members spanning card networks, cloud providers and payment processors. Neutral governance has not ended competition: Stripe's Machine Payments Protocol (co-developed with Tempo) also uses HTTP 402 but adds session-based billing; the Agentic Commerce Protocol comes from Stripe and OpenAI; Visa has its Trusted Agent Protocol; and Google's Agent Payments Protocol (AP2) uses an A2A x402 extension, built with Coinbase, the Ethereum Foundation and MetaMask, for crypto settlement between agents. **⚑ Shared theme:** Stripe — a supporter of the x402 Foundation and developer of a rival protocol — acquired the inference router [OpenRouter]({{< relref "openrouter.md" >}}) in 2026, linking this section's routing and payment layers through a single owner.

## Notable Developments

- **2026-11-01:** Cumulative x402 activity passed 196 million transactions and \$42 million settled across 12 chains (Fireblocks data relayed by Decrypt); October 2026 volume was about 5.1 million transactions worth about \$274,000.
- **2026-10-01:** Michael Hursta became executive director of the x402 Foundation.
- **2026-07-14:** The x402 Foundation became fully operational under the Linux Foundation with 40 member organizations, completing Coinbase's contribution of the protocol.
- **2026-06-03:** Chainalysis published independent on-chain analysis showing x402 agentic transactions on Base crossed 100 million cumulative transactions, with the PING meme-coin campaign identified as a major driver of the Q4 2025 volume surge, and \$1+-transaction share rising from 49% to 95% of volume between early 2025 and early 2026.
- **2026-05:** Batch settlement added, letting agents hand sellers signed vouchers that are settled in bulk.
- **2026-04-21:** Coinbase launched Agent.market, a permissionless x402-payable service directory spanning seven categories; self-reported concurrent adoption figures of ~69,000 active agents, 165 million cumulative transactions, and ~\$50 million cumulative volume.
- **2026-04-02:** The Linux Foundation announced the x402 Foundation and Coinbase's contribution of the protocol, with initial support from Amazon Web Services, Google, Microsoft, Stripe, Visa, Mastercard and others.
- **2025-12:** x402 V2 released, adding wallet-based identity, automatic service discovery, and support for more chains.
- **2025-05:** x402 released by Coinbase's Developer Platform team.

## Sources

- [Welcome to x402 — Coinbase Developer Documentation](https://docs.cdp.coinbase.com/x402/welcome) — protocol overview and facilitator model (fee details are on a separate facilitator page)
- [Agentic Payments Cross the Threshold: Inside x402's Path to Meaningful Adoption — Chainalysis](https://www.chainalysis.com/blog/x402-agentic-payments-adoption/) — independent on-chain transaction analysis, PING campaign, value-transfer concentration, retention/conversion metrics, wallet demographic profile
- [Coinbase Expands x402 With AI Agent App Store — Yahoo Finance/Cryptonews](https://finance.yahoo.com/markets/crypto/articles/coinbase-expands-x402-ai-agent-123512115.html) — Agent.market launch details, self-reported adoption figures, Erik Reppel quote
- [What Is x402? How AI Agents Pay With Crypto — Decrypt](https://decrypt.co/resources/what-is-x402-how-ai-agents-pay-with-crypto) — November 2026 explainer: launch and V2 dates, foundation timeline and membership, executive director, cumulative and October 2026 volumes, competing protocols
- [Linux Foundation is Launching the x402 Foundation and Welcoming the Contribution of the x402 Protocol — Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol) — April 2, 2026 announcement and list of initial supporters
- [x402 Bazaar — Coinbase Developer Documentation](https://docs.cdp.coinbase.com/x402/bazaar) — discovery catalog: search, list and merchant-lookup interfaces, ranking signals
