---
title: "x402: Machine-to-Machine Payments"
date: 2026-08-04
lastmod: 2026-08-04
draft: false
description: "Coinbase's x402 protocol — reviving the unused HTTP 402 'Payment Required' status code to let AI agents pay per API call in stablecoins with no account or human approval step — is the leading candidate settlement layer for an ad-hoc inference-compute marketplace, live since mid-2025 and past 100 million on-chain transactions on Base by mid-2026."
research_area: "compute-marketplaces"
source_urls:
  - "https://docs.cdp.coinbase.com/x402/welcome"
  - "https://www.chainalysis.com/blog/x402-agentic-payments-adoption/"
  - "https://finance.yahoo.com/markets/crypto/articles/coinbase-expands-x402-ai-agent-123512115.html"
last_reviewed: 2026-08-04
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
- **Bazaar** — x402's planned discovery extension: a directory letting buyers (human or agent) find x402-payable services, the piece of the protocol most directly relevant to a compute marketplace's discovery layer.

## Summary

x402 is an open payment protocol, created by Coinbase and released in May 2025, that lets a server demand payment for an API call by responding with the long-dormant HTTP 402 status code and a machine-readable payment specification; the requesting client (human-operated or a fully autonomous AI agent) constructs and signs a stablecoin payment, resubmits the request with proof of payment attached, and receives the resource once the seller verifies settlement. It is the most advanced production example of the third layer this section tracks — machine-to-machine settlement — and on-chain data shows genuine, still-small-but-growing adoption rather than a purely theoretical protocol: over 100 million agentic transactions on the Base network within roughly three quarters of launch, per independent on-chain analysis from Chainalysis.

## Key Facts

- Type: open payment protocol (not a company; developed by Coinbase's Developer Platform team)
- Released: May 2025 (per multiple secondary sources; original Coinbase launch page did not return readable content when checked this session — treat the exact 2025 launch month as reported by secondary sources, not independently confirmed from Coinbase's own announcement)
- Primary chain: Base (Coinbase's Ethereum L2), though the protocol is chain-agnostic via CAIP-2 identifiers and Coinbase's facilitator supports Base, Polygon, Arbitrum, World, and Solana as of this review
- Settlement assets: any ERC-20 via Permit2, or EIP-3009 tokens (USDC, EURC) for the smoothest flow — no custom token; uses existing stablecoins
- Independent on-chain adoption metric (Chainalysis, using on-chain transaction signatures, published 2026-06-03): agentic x402 transactions on Base crossed 100 million cumulative transactions within about three quarters of going live, after a surge in Q4 2025 driven substantially by a speculative "pay-to-mint" meme-coin campaign (PING) rather than organic commerce
- Self-reported adoption metric (Coinbase, as of April 21, 2026, per Yahoo Finance/Cryptonews coverage of the Agent.market launch): ~69,000 active AI agents on x402, 165 million cumulative transactions, ~$50 million cumulative volume — an average call value under $0.31, confirming the protocol is still calibrated for micropayments rather than bulk settlement

## What It Is / How It Works

**The core flow.** A buyer (an AI agent, in the use case most relevant here) requests a resource — an API call, a data feed, a compute job — from a server. If payment is required, the server responds with HTTP 402 and a `PAYMENT-REQUIRED` header specifying price, accepted assets, and network. The buyer's client constructs a signed stablecoin payment payload (`PAYMENT-SIGNATURE` header) and resubmits the request. The server verifies and settles the payment through a **facilitator** — Coinbase runs a hosted facilitator with a free tier of 1,000 transactions/month, then $0.001/transaction — so a seller never has to run their own blockchain node or wallet infrastructure to accept payment. The entire loop happens inside a single HTTP request/response cycle with no account creation, session, or API key exchange beforehand, which is the specific friction x402 is designed to remove: per Coinbase's own docs, the protocol targets "API services paid per request," "AI agents that autonomously pay for API access," and "microservices and tooling monetized via microtransactions."

**Why this matters for an inference marketplace specifically.** A buyer's agent discovering an inference provider through any of the discovery mechanisms elsewhere in this section (OpenRouter's directory, a DHT-based swarm, a future IETF Resource Provider Card) still needs a way to actually pay that provider per call, without a pre-negotiated contract or a human approving each transaction — exactly the gap x402 targets. Coinbase's roadmap explicitly includes a **discovery layer called Bazaar**, letting buyers (human or agent) find available x402-payable services — meaning the same protocol that solves settlement is also positioning itself to solve discovery, which would collapse two of this section's three layers (discovery and payment) into a single vendor-provided stack if it ships and gains adoption. As of this review Bazaar is listed on Coinbase's roadmap, not confirmed as shipped.

**Adoption reality check.** Independent on-chain data (Chainalysis, analyzing wallets that interact directly with the x402 contract on Base) shows real but immature adoption: transaction volume surged from near-zero in mid-2025 to over 100 million cumulative transactions by Q1 2026, but a large share of the Q4 2025 surge was driven by PING, a speculative "pay-to-mint" meme-coin campaign that turned the 402 payment loop into a repeatable game rather than genuine machine-to-machine commerce — one campaign alone processed over 150,000 transactions in its first month. Growth moderated in Q1 2026 as speculative activity cooled. More encouraging signals in the same data: the share of transaction volume from calls worth $1 or more rose from 49% (early 2025) to 95% (early 2026), meaning the protocol's economic weight has shifted toward real value transfer rather than sub-cent novelty transactions; wallets that test the protocol once are converting to repeat payers four times faster than they did six months earlier; and week-over-week wallet retention, while volatile, is trending upward. Chainalysis's own read: "x402 on Base has moved beyond proof-of-concept... but mass adoption remains distant," with the current user base skewing toward crypto-native, newly created wallets rather than established institutional participants.

**The discovery+payment product that already exists.** In April 2026, Coinbase launched **Agent.market**, described in coverage as an "AI agent app store" — a permissionless, browsable directory of x402-payable services across seven categories (reasoning, data, media, search, social, infrastructure, and trading), with providers reportedly including OpenAI, Bloomberg, CoinGecko, and AWS Lambda listed at launch. Listing is permissionless — any service provider can add itself without Coinbase's approval — which directly reduces the discovery friction this section identifies as unsolved elsewhere; x402 creator Erik Reppel is quoted framing this as reducing "customer acquisition activation costs for businesses, as robots can now access services at a very low setup cost without needing API keys." Agent.market is the closest existing product to a combined discovery-plus-payment layer for machine-to-machine commerce, though it launched alongside — not as a replacement for — the self-reported adoption figures above, and no inference-compute-specific category is confirmed among the seven listed as of this review.

## Notable Developments

- **2026-04-21:** Coinbase launched Agent.market, a permissionless x402-payable service directory spanning seven categories; self-reported concurrent adoption figures of ~69,000 active agents, 165 million cumulative transactions, and ~$50 million cumulative volume.
- **2026-06-03:** Chainalysis published independent on-chain analysis showing x402 agentic transactions on Base crossed 100 million cumulative transactions, with the PING meme-coin campaign identified as a major driver of the Q4 2025 volume surge, and $1+-transaction share rising from 49% to 95% of volume between early 2025 and early 2026.
- **2025 (mid-year, exact date not independently confirmed this session):** x402 released by Coinbase's Developer Platform team.

## Sources

- [Welcome to x402 — Coinbase Developer Documentation](https://docs.cdp.coinbase.com/x402/welcome) — protocol mechanics, facilitator model, fee structure, Bazaar discovery-layer roadmap item, supported networks
- [Agentic Payments Cross the Threshold: Inside x402's Path to Meaningful Adoption — Chainalysis](https://www.chainalysis.com/blog/x402-agentic-payments-adoption/) — independent on-chain transaction analysis, PING campaign, value-transfer concentration, retention/conversion metrics, wallet demographic profile
- [Coinbase Expands x402 With AI Agent App Store — Yahoo Finance/Cryptonews](https://finance.yahoo.com/markets/crypto/articles/coinbase-expands-x402-ai-agent-123512115.html) — Agent.market launch details, self-reported adoption figures, Erik Reppel quote
