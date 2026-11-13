---
title: "OpenRouter"
date: 2026-08-04
lastmod: 2026-11-12
draft: false
description: "Posted-price aggregation marketplace and routing gateway for LLM inference — 400+ models across 80+ providers, more than 10 million users — acquired by Stripe in a deal announced August 2026 and reported complete in November 2026; the largest production example of price-, speed- and reliability-weighted provider selection for inference."
research_area: "compute-marketplaces"
source_urls:
  - "https://openrouter.ai/blog/insights/model-routing/"
  - "https://techcrunch.com/2026/05/26/openrouter-more-than-doubles-valuation-to-1-3b-in-a-year/"
  - "https://alexatallah.com/"
  - "https://stripe.com/newsroom/news/stripe-agrees-to-acquire-openrouter"
  - "https://thenewstack.io/stripe-acquires-openrouter-tokens/"
  - "https://www.tokenpost.com/news/business/54344"
  - "https://openrouter.ai/blog/announcements/how-we-rebuilt-provider-routing/"
  - "https://openrouter.ai/announcements"
last_reviewed: 2026-11-12
stale_after_days: 90
related:
  - "compute-marketplaces/latency-based-matchmaking-in-multiplayer-gaming.md"
  - "compute-marketplaces/x402-machine-payments.md"
  - "datacenters/distributed-compute/akash-network.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

OpenRouter is a New York-founded AI "gateway," owned by Stripe since November 2026 — a single OpenAI-compatible API endpoint that fans requests out across 400+ language models from 80+ inference providers, automatically choosing which provider serves each request. Until October 2026 the default choice was weighted almost entirely by price; it now uses a real-time "Routing Cost" that also counts speed, rate limiting, errors and response quality, with explicit overrides for price-only, latency/throughput, cost ceilings, and compliance constraints. It is the largest production example of the "posted-price aggregation" model for an inference-compute marketplace: providers publish per-token pricing, and OpenRouter's router — not a human, and not a blockchain auction — decides which provider actually fulfills each call.

## Key Facts

- Founded: 2023
- Founders: Alex Atallah (co-founder and CEO — previously co-founder and CTO of OpenSea, the NFT marketplace; Stanford, Y Combinator, HF0, and Palantir alum), Chris Clark and Louis Vichy, the three named as founders of the company's August 2026 acquisition announcement. Atallah's role within Stripe after completion was not stated in the sources reviewed.
- Type: Company — AI inference gateway / routing marketplace (SaaS); takes a 5.5% fee on credits purchased through the platform
- Status: Subsidiary of Stripe. Stripe announced on August 19, 2026 that it had agreed to acquire OpenRouter and was reported on November 11, 2026 to have completed the deal; terms were not disclosed, and press reports put the price between more than \$7 billion and about \$8 billion. OpenRouter said its brand, product, roadmap and model-neutral approach would continue. Earlier funding: Series A (\$40M, June 2025, led by Andreessen Horowitz and Menlo Ventures, with Sequoia participating) at an estimated \$547M post-money valuation (per PitchBook); Series B (\$113M, announced May 26, 2026, led by CapitalG — Alphabet's growth fund) at an estimated \$1.3B post-money valuation (per The New York Times, cited by TechCrunch)
- Scale: at the August 2026 acquisition announcement, 400+ models from 80+ providers (Stripe), more than 10 million developers and companies, and over 10 trillion tokens a day (company figures via The New Stack). At the May 2026 funding announcement: 400+ models, 60+ providers, 8 million global users, ~100 trillion tokens processed per month (~25 trillion/week) — a 5× increase in weekly token volume over the prior six months

## What It Is / How It Works

OpenRouter presents a single API endpoint (`https://openrouter.ai/api/v1`, OpenAI SDK-compatible) in front of two independent routing decisions: **model routing** (which underlying model answers a given prompt) and **provider routing** (which of the providers serving that model actually handles this specific call). A caller either names a model explicitly or delegates model selection to OpenRouter's `openrouter/auto` router (built on NotDiamond, which picks a model per prompt from a curated pool, steerable via a cost/quality tradeoff parameter).

Provider routing — the piece most relevant to a compute marketplace — was rebuilt in October 2026. Under the original default, a request with no explicit sort or provider list was sent to a provider chosen mainly on input-token price (deprioritizing any provider with a recent outage, weighting the rest by the inverse square of price, and treating the remainder as a fallback chain). OpenRouter said that design let cheap providers win traffic even when they performed poorly and invited providers to game it by lowering input prices while raising cached- or output-token prices. The replacement computes a real-time "Routing Cost" per provider — an estimate of what a good answer costs — from effective price (using measured cache-hit rates and token mix), time to first token and throughput (waiting converted into cost), rate-limit rejections, provider errors, and a quality check that currently looks mainly at whether tool calls come back well formed. Traffic is spread across providers within a competitive band rather than sent to a single winner, with a floor so every provider keeps some traffic, back-off for failing or rate-limited providers, and a learned capacity cap; conversations stay pinned to their first provider while the prompt cache is warm. About 77% of requests go to models served by more than one provider, so the change affects most traffic. Callers can still bypass it: `provider.order` forces an explicit order, `provider.only`/`provider.ignore` filter the candidate set, an explicit `provider.sort` (`price`, `throughput`, or `latency`) or the `:floor` suffix restores single-criterion routing, and the `provider` object continues to expose quantization filtering, zero-data-retention requirements, a hard price ceiling, and `preferred_min_throughput` / `preferred_max_latency` fields — the closest a production inference marketplace gets today to letting a buyer specify a latency requirement rather than just a price ceiling.

OpenRouter explicitly does not currently route by measured physical/geographic proximity between the requester and the provider's data center — the company's June 2026 routing documentation lists geographic routing to reduce latency as a planned, not shipped, capability, and the October 2026 routing announcement does not mention it, noting that "the latency delta from serving traffic out of the wrong region is typically larger than the delta from choosing a faster model tier." Failed requests are not billed ("zero-completion insurance"), and provider-level failover is automatic and separate from model-level fallback (a `models` array tried in priority order, which survives an entire model going down, not just one provider). OpenRouter itself is a single point of failure for all of this: a company-side outage (e.g., a ~50-minute database incident in August 2025) takes down every provider and fallback path simultaneously, since all routing logic runs inside OpenRouter's own infrastructure rather than being distributed to the edge.

OpenRouter's own documentation also flags the marketplace's unresolved trust problem directly: "some providers serve more heavily quantized variants of a model that underperform the same model hosted elsewhere," and the only mitigation offered is letting a caller manually exclude or allowlist specific providers — there is no published quality score or independent attestation of what model weights a provider is actually running.

## Notable Developments

- **2026-11-10/11:** Stripe was reported to have completed its acquisition of OpenRouter, confirming that OpenRouter is now part of the company; OpenRouter's user count was given as more than 10 million developers and businesses.
- **2026-10-28:** OpenRouter replaced its price-weighted default provider routing with a "Routing Cost" algorithm that also weighs speed, rate limits, errors and response quality. In its own one-week switchback test over about 24 million requests, median time to first token fell 16.9% and requests hitting a rate limit fell 46%, while cost per million tokens rose 7.3% — self-reported figures, not independently replicated.
- **2026-10-14:** Launched Private Endpoints, letting customers bring their own fine-tuned models and capacity behind the OpenRouter API.
- **2026-08-19:** Stripe announced an agreement to acquire OpenRouter, without disclosing terms; OpenRouter's founders said the brand, product, roadmap and model-neutral approach would remain.
- **2026-05-26:** Closed \$113M Series B led by CapitalG (Alphabet's growth venture fund), reported at an approximate \$1.3B post-money valuation (The New York Times, cited by TechCrunch) — more than double the ~\$547M valuation from its Series A roughly a year earlier. Company-reported scale at announcement: 8 million users, ~100 trillion tokens/month, a 5× increase in weekly token volume over the preceding six months.
- **2025-06:** Closed \$40M Series A led by Andreessen Horowitz and Menlo Ventures, with Sequoia participating.
- **2023:** Founded by Alex Atallah.

## Key People

**Alex Atallah** — Co-founder and CEO. Previously co-founder and CTO of OpenSea (2018–2022), the NFT marketplace. Stanford University; Y Combinator and HF0 accelerator alum; earlier career included a role at Palantir.
- Personal site: [alexatallah.com](https://alexatallah.com/)
- LinkedIn: [linkedin.com/in/alexatallah](https://www.linkedin.com/in/alexatallah/)
- **⚑ Overlap:** OpenSea co-founder background is a notable prior-marketplace pattern — Atallah built and scaled a different two-sided marketplace (NFT buyers/sellers) before OpenRouter's compute-provider/model-buyer marketplace; worth cross-referencing if other marketplace-design founders with NFT/crypto-marketplace backgrounds are documented elsewhere in this knowledge base.

**Chris Clark** and **Louis Vichy** — Co-founders, named alongside Atallah as authors of the August 2026 acquisition announcement (per The New Stack). Current titles and prior employers not confirmed — TODO. LinkedIn: not found (not searched this review).

**⚑ Shared theme:** Stripe, OpenRouter's owner, is also a listed supporter of the x402 Foundation and co-developer of the competing Machine Payments Protocol (see [x402]({{< relref "x402-machine-payments.md" >}})) — putting the largest inference router and two of the candidate machine-payment rails under one company's influence.

### People — Last Reviewed: 2026-11-12

## Claim Verification

### Claim: Stripe paid more than \$7 billion for OpenRouter
**Status:** Unverified

**Supporting sources:**
- [The New Stack](https://thenewstack.io/stripe-acquires-openrouter-tokens/) — cites independent reports of about \$8 billion and calls it Stripe's largest known acquisition

**Refuting / questioning sources:**
- [Stripe newsroom](https://stripe.com/newsroom/news/stripe-agrees-to-acquire-openrouter) — the announcement discloses no price or terms

**Summary:** Every price figure is press-reported; neither company has confirmed one.

### Claim: OpenRouter remains neutral between model providers under Stripe ownership
**Status:** Unverified

**Supporting sources:**
- [The New Stack](https://thenewstack.io/stripe-acquires-openrouter-tokens/) — reports the founders' statement that brand, roadmap and model-neutral approach continue

**Refuting / questioning sources:**
- None found; the commitment is a company statement with no structural guarantee described, and Stripe has separate commercial relationships with model providers.

**Summary:** A stated intention made at announcement; too recent to assess against behaviour.

### Claim: The October 2026 routing change makes inference faster and more reliable
**Status:** Partially verified

**Supporting sources:**
- [OpenRouter: How we rebuilt provider routing](https://openrouter.ai/blog/announcements/how-we-rebuilt-provider-routing/) — one-week switchback experiment: lower time to first token, fewer rate-limit hits and retries

**Refuting / questioning sources:**
- The same post reports cost per million tokens rose 7.3%; no third-party benchmark was found.

**Summary:** Supported by the company's own controlled test, with a disclosed cost increase; not independently replicated.

## Sources

- [How OpenRouter Model Routing Works — OpenRouter Blog](https://openrouter.ai/blog/insights/model-routing/) — provider routing algorithm, `:nitro`/`:floor`, geographic routing status, outage handling
- [OpenRouter more than doubles valuation to \$1.3B in a year — TechCrunch](https://techcrunch.com/2026/05/26/openrouter-more-than-doubles-valuation-to-1-3b-in-a-year/) — Series B amount/lead investor, valuation figures, usage scale, founding year
- [Alex Atallah — personal site](https://alexatallah.com/) — founder bio, OpenSea background, education
- [Stripe agrees to acquire OpenRouter to help businesses optimize token routing and usage — Stripe newsroom](https://stripe.com/newsroom/news/stripe-agrees-to-acquire-openrouter) — August 19, 2026 announcement; 400+ models, 80+ providers; no terms disclosed
- [OpenRouter called itself the "Stripe for LLMs" — now Stripe's swooped in to buy it — The New Stack](https://thenewstack.io/stripe-acquires-openrouter-tokens/) — reported price, founders named, usage figures, 5.5% fee, neutrality statement
- [Stripe Completes OpenRouter Acquisition to Expand Its AI Infrastructure Business — TokenPost](https://www.tokenpost.com/news/business/54344) — November 11, 2026 report of completion; 10 million+ users
- [How we rebuilt provider routing for better, faster inference — OpenRouter Blog](https://openrouter.ai/blog/announcements/how-we-rebuilt-provider-routing/) — October 2026 routing algorithm change, overrides that remain, experiment results
- [OpenRouter announcements](https://openrouter.ai/announcements) — dated index of product announcements (Private Endpoints, routing rebuild, "OpenRouter is Joining Stripe")
