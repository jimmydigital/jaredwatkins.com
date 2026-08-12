---
title: "OpenRouter"
date: 2026-08-04
lastmod: 2026-08-04
draft: false
description: "New York-based posted-price aggregation marketplace and routing gateway for LLM inference — 400+ models across 60+ providers, ~100 trillion tokens/month, $1.3B valuation as of a May 2026 Series B — the largest production example of price/latency-weighted provider selection for inference."
research_area: "compute-marketplaces"
source_urls:
  - "https://openrouter.ai/blog/insights/model-routing/"
  - "https://techcrunch.com/2026/05/26/openrouter-more-than-doubles-valuation-to-1-3b-in-a-year/"
  - "https://alexatallah.com/"
last_reviewed: 2026-08-04
stale_after_days: 90
related:
  - "compute-marketplaces/latency-based-matchmaking-in-multiplayer-gaming.md"
  - "compute-marketplaces/x402-machine-payments.md"
  - "datacenters/distributed-compute/akash-network.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

OpenRouter is a New York-based company operating an AI "gateway" — a single OpenAI-compatible API endpoint that fans requests out across 400+ language models from 60+ inference providers, automatically choosing which provider serves each request by a price-weighted default algorithm (with explicit overrides for latency/throughput, cost ceilings, and compliance constraints). It is the largest production example of the "posted-price aggregation" model for an inference-compute marketplace: providers publish per-token pricing, and OpenRouter's router — not a human, and not a blockchain auction — decides which provider actually fulfills each call.

## Key Facts

- Founded: 2023
- Founder/CEO: Alex Atallah — previously co-founder and CTO of OpenSea (the NFT marketplace); Stanford, Y Combinator, HF0, and Palantir alum. Additional co-founders are referenced in press coverage but not independently confirmed via a current-dated primary source as of this review — TODO: verify full founding team.
- Type: Company — AI inference gateway / routing marketplace (SaaS)
- Status: Private, growth-stage. Series A ($40M, June 2025, led by Andreessen Horowitz and Menlo Ventures, with Sequoia participating) at an estimated $547M post-money valuation (per PitchBook); Series B ($113M, announced May 26, 2026, led by CapitalG — Alphabet's growth fund) at an estimated $1.3B post-money valuation (per The New York Times, cited by TechCrunch)
- Scale (as of the May 2026 funding announcement): 400+ models, 60+ providers, 8 million global users, ~100 trillion tokens processed per month (~25 trillion/week) — a 5× increase in weekly token volume over the prior six months

## What It Is / How It Works

OpenRouter presents a single API endpoint (`https://openrouter.ai/api/v1`, OpenAI SDK-compatible) in front of two independent routing decisions: **model routing** (which underlying model answers a given prompt) and **provider routing** (which of the providers serving that model actually handles this specific call). A caller either names a model explicitly or delegates model selection to OpenRouter's `openrouter/auto` router (built on NotDiamond, which picks a model per prompt from a curated pool, steerable via a cost/quality tradeoff parameter).

Provider routing — the piece most relevant to a compute marketplace — runs a default three-step algorithm on every request unless overridden: first, deprioritize (not remove) any provider with a significant outage in the preceding 30 seconds; second, among the remaining stable providers, select probabilistically weighted by the *inverse square* of price, so that a provider at $1/M tokens is roughly 9× more likely to be tried first than one at $3/M; third, treat the rest as an ordered fallback chain. Callers can override this default via a `provider` object exposing fields for explicit ordering, allow/deny lists, quantization-level filtering, zero-data-retention requirements, a hard price ceiling, and — notably — `preferred_min_throughput` and `preferred_max_latency` fields, which is the closest a production inference marketplace gets today to letting a buyer specify a latency requirement rather than just a price ceiling. Two shorthand suffixes exist for the common cases: appending `:nitro` to a model name is exactly `provider.sort: "throughput"` (optimize for speed), and `:floor` is exactly `provider.sort: "price"` (optimize for cost).

OpenRouter explicitly does not currently route by measured physical/geographic proximity between the requester and the provider's data center — the company's own documentation lists geographic routing to reduce latency as a planned, not shipped, capability as of this review, noting that "the latency delta from serving traffic out of the wrong region is typically larger than the delta from choosing a faster model tier." Failed requests are not billed ("zero-completion insurance"), and provider-level failover is automatic and separate from model-level fallback (a `models` array tried in priority order, which survives an entire model going down, not just one provider). OpenRouter itself is a single point of failure for all of this: a company-side outage (e.g., a ~50-minute database incident in August 2025) takes down every provider and fallback path simultaneously, since all routing logic runs inside OpenRouter's own infrastructure rather than being distributed to the edge.

OpenRouter's own documentation also flags the marketplace's unresolved trust problem directly: "some providers serve more heavily quantized variants of a model that underperform the same model hosted elsewhere," and the only mitigation offered is letting a caller manually exclude or allowlist specific providers — there is no published quality score or independent attestation of what model weights a provider is actually running.

## Notable Developments

- **2026-05-26:** Closed $113M Series B led by CapitalG (Alphabet's growth venture fund), reported at an approximate $1.3B post-money valuation (The New York Times, cited by TechCrunch) — more than double the ~$547M valuation from its Series A roughly a year earlier. Company-reported scale at announcement: 8 million users, ~100 trillion tokens/month, a 5× increase in weekly token volume over the preceding six months.
- **2025-06:** Closed $40M Series A led by Andreessen Horowitz and Menlo Ventures, with Sequoia participating.
- **2023:** Founded by Alex Atallah.

## Key People

**Alex Atallah** — Co-founder and CEO. Previously co-founder and CTO of OpenSea (2018–2022), the NFT marketplace. Stanford University; Y Combinator and HF0 accelerator alum; earlier career included a role at Palantir.
- Personal site: [alexatallah.com](https://alexatallah.com/)
- LinkedIn: [linkedin.com/in/alexatallah](https://www.linkedin.com/in/alexatallah/)
- **⚑ Overlap:** OpenSea co-founder background is a notable prior-marketplace pattern — Atallah built and scaled a different two-sided marketplace (NFT buyers/sellers) before OpenRouter's compute-provider/model-buyer marketplace; worth cross-referencing if other marketplace-design founders with NFT/crypto-marketplace backgrounds are documented elsewhere in this knowledge base.

### People — Last Reviewed: 2026-08-04

## Sources

- [How OpenRouter Model Routing Works — OpenRouter Blog](https://openrouter.ai/blog/insights/model-routing/) — provider routing algorithm, `:nitro`/`:floor`, geographic routing status, outage handling
- [OpenRouter more than doubles valuation to $1.3B in a year — TechCrunch](https://techcrunch.com/2026/05/26/openrouter-more-than-doubles-valuation-to-1-3b-in-a-year/) — Series B amount/lead investor, valuation figures, usage scale, founding year
- [Alex Atallah — personal site](https://alexatallah.com/) — founder bio, OpenSea background, education
