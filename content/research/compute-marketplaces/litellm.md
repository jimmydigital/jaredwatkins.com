---
title: "LiteLLM"
date: 2026-08-15
lastmod: 2026-08-15
draft: false
description: "Open-source LLM gateway/SDK (BerriAI, YC W23) that gives a buyer a unified, OpenAI-compatible interface to 100+ inference providers with built-in latency-, cost-, and least-busy-based routing and automatic failover — functionally the self-hosted, non-blockchain equivalent of OpenRouter's provider-routing algorithm, run as infrastructure the buyer controls rather than a third-party marketplace."
research_area: "compute-marketplaces"
source_urls:
  - "https://github.com/BerriAI/litellm"
  - "https://www.ycombinator.com/companies/litellm"
  - "https://app.dealroom.co/news/feed/litellm-raises-1-6m-seed-funding-amid-security-challenges-hits-7m-arr"
  - "https://docs.litellm.ai/blog/security-update-march-2026"
  - "https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/"
last_reviewed: 2026-08-15
stale_after_days: 90
related:
  - "compute-marketplaces/openrouter.md"
  - "compute-marketplaces/gateway-api-inference-extension.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

LiteLLM is an open-source AI gateway — deployable as a self-hosted proxy server or embedded as a Python SDK — that gives a developer a single OpenAI-compatible interface to 100+ LLM providers (OpenAI, Anthropic, Bedrock, Azure, Vertex AI, Cohere, and others). Its Router implements the same category of provider-selection logic OpenRouter runs as a hosted marketplace — latency-based, cost-optimized, and least-busy routing with automatic fallback across providers — but as infrastructure a buyer deploys and operates themselves, with no marketplace operator, token, or blockchain in the path. It is built and maintained by BerriAI, a 2023 Y Combinator (W23) company.

## Key Facts

- Founded: 2023; YC Winter 2023 batch
- Founders: Krrish Dholakia and Ishaan Jaffer
- Type: Company (BerriAI) / open-source project (LiteLLM, Apache-licensed core)
- Status: Private, early-stage. Seed round of $1.6M from Y Combinator, Gravity Fund, and Pioneer Fund; reported ~$7M ARR (both figures per a single third-party report — not independently corroborated in sources reviewed for this entry)
- Scale: 100+ supported providers; 53.8k GitHub stars / 9.8k forks as of this review; cited enterprise users include Stripe, Netflix, and Adobe (per company/third-party materials, not independently verified)

## What It Is / How It Works

LiteLLM's core function is translating calls to 100+ different provider APIs into and out of a single OpenAI-compatible request/response format, so an application written against one interface can call any supported provider without per-provider integration work. On top of that translation layer, the **Router** component implements the marketplace-relevant piece: it can distribute requests across multiple configured deployments of a model using weighted load balancing, route to whichever configured endpoint currently reports the lowest latency, route to minimize cost against a configured price table, or route to whichever backend is least busy — with configurable fallback chains so a request automatically retries against a secondary provider if the first fails. This is architecturally the same decision OpenRouter's provider-routing algorithm makes (inverse-price-weighted selection with outage deprioritization and an explicit `preferred_max_latency` override, per that entry) — LiteLLM just runs it as code the buyer configures and operates, in a YAML/GitOps-compatible deployment, rather than as a hosted service with its own pricing.

The self-hosted, YAML-config production build (as opposed to LiteLLM's SDK/library mode) also ships virtual API keys, per-key spend tracking, request guardrails, and an admin dashboard — the operational tooling a buyer would otherwise have to build to run their own multi-provider routing layer at all. Because it is self-hosted, LiteLLM has no built-in discovery mechanism for unaffiliated third-party compute (a buyer must already know and configure the providers it can route to) and no native payment/settlement layer — it complements, rather than replaces, the discovery and payment entries elsewhere in this section.

## Claim Verification

### Claim: LiteLLM is safe/production-appropriate infrastructure to route API credentials and inference traffic through

**Status:** Disputed / actively contested as of this review

**Supporting sources:**
- [GitHub — BerriAI/litellm](https://github.com/BerriAI/litellm) — large, active open-source project (53.8k stars) with a documented post-incident remediation program (credential rotation, Mandiant-assisted forensics, signed Docker images via cosign, hardened CI/CD).

**Refuting / questioning sources:**
- [LiteLLM — Security Update: Suspected Supply Chain Incident](https://docs.litellm.ai/blog/security-update-march-2026) — LiteLLM's own disclosure that a maintainer's PyPI account was compromised on March 24, 2026, and used to publish two malicious package versions (v1.82.7, v1.82.8) live on PyPI for roughly 40 minutes before quarantine; the payload was designed to harvest SSH keys, cloud credentials (AWS/GCP/Azure), Kubernetes tokens, and database passwords and exfiltrate them, and — where Kubernetes access was available — to attempt lateral movement by deploying privileged pods.
- [Dealroom — LiteLLM raises $1.6M seed funding amid security challenges](https://app.dealroom.co/news/feed/litellm-raises-1-6m-seed-funding-amid-security-challenges-hits-7m-arr) — reports litigation was filed against BerriAI in Texas federal court in April 2026 in connection with the incident.

**Summary:** LiteLLM disclosed and responded to a real, credential-harvesting supply-chain compromise of its official PyPI package in March 2026, and the incident produced litigation as of April 2026. Given that LiteLLM's entire value proposition in this section is routing a buyer's inference traffic and provider credentials through it, this is a directly material trust flag — treat "self-hosted means the buyer controls the trust boundary" as true of the deployment model in principle, but not as a track-record guarantee; verify current patch status (v1.83.0+ or pre-v1.82.7) before deploying.

## Notable Developments

- **2026-04 (approx.):** Litigation filed against BerriAI in Texas federal court in connection with the March 2026 supply-chain incident, per third-party reporting.
- **2026-03-24:** Suspected supply-chain attack compromised a maintainer's PyPI account; malicious code was live in two published package versions for approximately 40 minutes before removal. See Claim Verification above.
- **2023:** BerriAI founded by Krrish Dholakia and Ishaan Jaffer; admitted to Y Combinator's Winter 2023 batch.

## Key People

**Krrish Dholakia** — Co-founder, BerriAI/LiteLLM.
- LinkedIn: not found — TODO: verify current profile

**Ishaan Jaffer** — Co-founder & CTO, BerriAI/LiteLLM.
- LinkedIn: [linkedin.com/in/reffajnaahsi](https://www.linkedin.com/in/reffajnaahsi/) (unverified — handle appears reversed/obfuscated; confirm this is genuinely Ishaan Jaffer's profile before citing further)

### People — Last Reviewed: 2026-08-15

## Sources

- [GitHub — BerriAI/litellm](https://github.com/BerriAI/litellm) — routing strategies, scale, provider count, license
- [Y Combinator — LiteLLM company page](https://www.ycombinator.com/companies/litellm) — founders, batch, founding year, seed investors
- [Dealroom — LiteLLM raises $1.6M seed funding amid security challenges](https://app.dealroom.co/news/feed/litellm-raises-1-6m-seed-funding-amid-security-challenges-hits-7m-arr) — funding amount, investors, ARR figure, litigation
- [LiteLLM — Security Update: Suspected Supply Chain Incident](https://docs.litellm.ai/blog/security-update-march-2026) — official incident disclosure and remediation
- [FutureSearch — litellm 1.82.8 Supply Chain Attack on PyPI (March 2026)](https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/) — independent technical analysis of the malicious payload
