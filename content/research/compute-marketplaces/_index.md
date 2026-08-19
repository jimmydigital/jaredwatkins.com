---
title: "Compute Marketplaces"
date: 2026-08-04
lastmod: 2026-08-15
draft: false
description: "Technology enabling on-demand, ad-hoc marketplaces for inference compute: discovery and latency-based routing, price/auction matchmaking, and machine-to-machine payment rails — plus prior-art comparables from multiplayer game server matchmaking."
research_area: "compute-marketplaces"
last_reviewed: 2026-08-15
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.8
  disable: false
---

> **⚠ Disclaimer:** This section may contain incomplete, out of date, or inaccurate entries. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the source materials listed in individual entries.

## Overview

If inference compute is going to trade in an open, ad-hoc market — buyers and sellers who have never met, matched request-by-request across whichever provider can serve fastest or cheapest — three technical layers have to exist: a way for a buyer to **discover** who can serve a given request nearby or cheaply, a **matchmaking/pricing** mechanism that decides who actually gets the job, and a **payment/settlement** layer that lets machines pay machines per request without a human in the loop. This section tracks the state of each layer as of mid-2026.

None of the three layers has a dominant, standardized answer yet. Two production-scale marketplaces exist — [OpenRouter]({{< relref "openrouter.md" >}}) (posted-price aggregation across 60+ inference providers) and [Akash Network]({{< relref "../datacenters/distributed-compute/akash-network.md" >}}) (on-chain reverse auction) — but neither routes on measured physical latency the way a CDN or a multiplayer game network does. That gap is the section's organizing question, which is why [latency-based matchmaking in multiplayer gaming]({{< relref "latency-based-matchmaking-in-multiplayer-gaming.md" >}}) — a problem the game industry solved decades ago for a similarly real-time, similarly ad-hoc matching problem — is documented here as the closest existing design comparable, alongside the decentralized [libp2p/Kademlia DHT discovery stack]({{< relref "p2p-discovery-protocols-libp2p-kademlia.md" >}}) used by peer-to-peer inference swarms, the emerging [IETF AI discovery drafts]({{< relref "ietf-ai-service-discovery-drafts.md" >}}), and [x402]({{< relref "x402-machine-payments.md" >}}), the leading candidate for the machine-payment layer.

This section is the coordination-layer counterpart to [Distributed & Decentralized Compute]({{< relref "../datacenters/distributed-compute/_index.md" >}}), which covers where distributed inference hardware is physically sited and powered. This section covers how a buyer finds that hardware and pays for the tokens it produces.

A separate, non-blockchain lineage of this problem is emerging out of Kubernetes-native AI infrastructure. The [Gateway API Inference Extension]({{< relref "gateway-api-inference-extension.md" >}}) is an open, vendor-neutral Kubernetes SIG specification (GA as of v1.5.0, April 2026) for criteria-based inference routing — matching a request to a backend by model name, LoRA adapter, request priority, queue depth, and KV-cache locality — and [llm-d]({{< relref "llm-d.md" >}}) is the CNCF-backed reference implementation built on top of it, adding KV-cache-aware and disaggregated prefill/decode routing. Neither has a discovery or payment layer of its own; both assume the operator already controls the fleet being routed across, which is the main way this pair differs from a cross-provider marketplace like OpenRouter or Akash. On the buyer-facing routing side, [LiteLLM]({{< relref "litellm.md" >}}) is the closest thing to a self-hosted, open-source OpenRouter — the same latency-/cost-aware provider routing logic, run as infrastructure the buyer deploys and controls rather than a third-party marketplace. On the discovery side, [NANDA]({{< relref "nanda.md" >}}) — MIT Media Lab's proposed "Internet of AI Agents" index — offers a DNS-like, cryptographically (not blockchain) verified resolution layer for agent/service discovery, though it targets general agent interoperability rather than compute-marketplace matching specifically.

## Key Themes

- Two working price-discovery models exist in production — posted-price aggregation (OpenRouter) and on-chain reverse auction (Akash) — but "route to the physically nearest/lowest-latency provider" is still mostly borrowed CDN practice (anycast, GeoDNS, client-measured RTT) rather than a purpose-built inference-marketplace protocol
- Kubernetes-native standardization is furthest along on the routing/matchmaking layer specifically, and it is entirely non-blockchain: the Gateway API Inference Extension (Kubernetes SIG, Apache-2.0, GA as of v1.5.0/April 2026) defines vendor-neutral primitives (InferencePool, endpoint picker) for routing by model, LoRA adapter, queue depth, and KV-cache locality; llm-d (CNCF sandbox, backed by Red Hat, Google Cloud, IBM Research, CoreWeave, NVIDIA, and others) is the most mature reference implementation, reporting up to 3x time-to-first-token improvement and roughly double throughput under SLO constraints in its own (unaudited) benchmarks
- Self-hosted, open-source routers are a non-blockchain alternative to a hosted marketplace: LiteLLM (BerriAI, YC W23) implements the same latency-, cost-, and least-busy routing logic as OpenRouter's provider-selection algorithm across 100+ providers, but as infrastructure the buyer deploys and controls — worth flagging that LiteLLM suffered a real supply-chain compromise of its official PyPI package in March 2026 (credential-harvesting malware live for roughly 40 minutes before quarantine, followed by litigation), a concrete illustration of the trust/security burden that shifts to the buyer under a self-hosted model
- Discovery standardization now has a concrete, non-blockchain running pilot beyond the IETF's individual drafts: NANDA (MIT Media Lab) proposes a DNS-like "Index" plus cryptographically verifiable "AgentFacts" records for agent/service discovery at internet scale — explicitly not blockchain-dependent — though as of mid-2026 it targets general AI-agent interoperability rather than compute/inference-marketplace matching specifically, and remains an early research deployment (~15 partner institutions, ~1,000 registered agents via its pilot registry)
- The multiplayer gaming industry solved a structurally similar problem — real-time, latency-sensitive matching of ad-hoc clients to the best available server — starting with ping-sorted server browsers in 1996 and maturing into relay networks (Valve's Steam Datagram Relay) that separate generic latency-measurement/relay transport from game-specific matchmaking policy; that split is a direct design analogy for a compute marketplace, and is echoed in how the Gateway API Inference Extension separates gateway/proxy transport from pluggable routing-policy logic
- Peer-to-peer inference swarms (Petals/Hivemind and derivatives) use a libp2p + Kademlia DHT stack for node discovery — a mechanism borrowed wholesale from BitTorrent/IPFs-style file sharing, distinct from and not interoperable with OpenRouter's, Akash's, or the Kubernetes-native routing stack's coordination models
- Standards work is nascent: IETF has multiple individual (non-working-group) drafts proposing AI/agent discovery mechanisms as of early-to-mid 2026, none adopted
- Machine-to-machine micropayment rails (x402, built on the revived HTTP 402 status code) are the leading candidate for a settlement layer that lets an AI agent pay per inference call without an account or human approval step — live in production since mid-2025 with meaningful but still small transaction volume as of early 2026
- Unsolved marketplace problem common to every posted-price aggregator: quality/fraud verification (a provider silently serving a more heavily quantized model than advertised) has no standard countermeasure yet

## Companies

### Startups & Development Partners

| Company | HQ | Stage | Mission |
|---------|-----|-------|---------|
| [OpenRouter](https://openrouter.ai/) | New York, US | Series B (~$1.3B valuation, May 2026) | Posted-price, multi-provider LLM inference routing gateway/marketplace — 400+ models, 60+ providers. |
| [Akash Network](https://akash.network/) | Distributed/DAO (Overclock Labs, San Francisco) | Live mainnet, token-governed | On-chain reverse-auction marketplace for GPU/CPU compute; see full entry in [Distributed & Decentralized Compute]({{< relref "../datacenters/distributed-compute/akash-network.md" >}}). |
| [LiteLLM](https://www.litellm.ai/) (BerriAI) | US | Seed ($1.6M, YC W23) | Open-source, self-hosted LLM gateway with latency-/cost-/least-busy-based routing across 100+ providers — the non-blockchain, self-hosted counterpart to OpenRouter's hosted router. |

### Public Companies

| Ticker | Company | Mission |
|--------|---------|---------|
| [COIN](https://finance.yahoo.com/quote/COIN) | [Coinbase](https://www.coinbase.com/) | Developer of x402, the leading HTTP-402-based machine-payment protocol used for per-request AI agent payments. |

### Incumbents

| Company | Relevance |
|---------|-----------|
| [Valve Corporation](https://www.valvesoftware.com/) | Operates Steam Datagram Relay, the most mature production example of latency-measured relay routing for real-time, ad-hoc client-to-server matching — the closest existing design comparable for latency-aware compute-marketplace routing. Privately held; no public ticker. |

Update all tables whenever a new entry is added that introduces a new company.
