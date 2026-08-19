---
title: "Gateway API Inference Extension"
date: 2026-08-15
lastmod: 2026-08-15
draft: false
description: "Open, vendor-neutral Kubernetes SIG specification (WG-Serving/SIG-Network) that extends the standard Gateway API with criteria-based routing for self-hosted LLM inference — matching requests to backend model servers by model name, LoRA adapter, request priority, queue depth, and KV-cache locality. GA as of v1.5.0 (April 2026); the closest thing in this section to a standardized, non-blockchain protocol for the matchmaking/routing layer of an inference marketplace."
research_area: "compute-marketplaces"
source_urls:
  - "https://gateway-api-inference-extension.sigs.k8s.io/"
  - "https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/"
  - "https://github.com/kubernetes-sigs/gateway-api-inference-extension"
  - "https://kgateway.dev/blog/llm-d-kgateway/"
last_reviewed: 2026-08-15
stale_after_days: 90
related:
  - "compute-marketplaces/openrouter.md"
  - "compute-marketplaces/litellm.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

The Gateway API Inference Extension is an official Kubernetes project (maintained under WG-Serving and SIG-Network) that adds AI-inference-aware routing primitives on top of the standard Kubernetes Gateway API. Where a generic load balancer routes on HTTP path or round-robins across identical backends, this extension lets a routing layer make a request-by-request placement decision based on which model is requested, which LoRA adapter it needs, how urgent it is, and which backend already has a "hot" KV cache for that prompt prefix — the specific technical routing/matchmaking problem this section's other entries solve with a posted price (OpenRouter) or an on-chain auction (Akash). It is open-source (Apache-2.0), has no token or blockchain component, and is designed to be implemented by any compliant gateway rather than tied to a single vendor.

## Key Facts

- Type: Technology — open standard / Kubernetes API extension (not a company or product)
- Governance: Kubernetes SIG-Network and WG-Serving; hosted at `kubernetes-sigs/gateway-api-inference-extension` on GitHub
- Status: General Availability as of v1.5.0 (April 19, 2026); Apache-2.0 licensed
- Announced: June 5, 2025
- Reference implementations: Envoy Gateway, kgateway, and GKE Gateway all implement the extension via Envoy's External Processing (ext-proc) filter

## What It Is / How It Works

The extension introduces two core custom resources on top of the base Gateway API. An **InferencePool** groups the set of backend endpoints (model server replicas, e.g. running vLLM) that can serve a given workload. An **endpoint picker (EPP)** — a pluggable scheduling component — sits in front of the pool and makes the actual per-request routing decision by scoring candidate endpoints against live signals rather than static configuration: current queue depth and GPU/accelerator load, KV-cache/prefix-cache state (so a follow-up request in a multi-turn conversation can be routed to the backend that already has the relevant context cached, avoiding redundant recomputation), and whether a requested LoRA adapter is already loaded on a given endpoint. Requests can also be tagged by criticality — a latency-sensitive interactive chat request can be prioritized over a throughput-tolerant batch summarization job competing for the same GPU pool — and the extension supports gradual, criteria-based traffic splitting for model version rollouts.

Architecturally, the extension does not replace a gateway/proxy — it augments one. A compliant Gateway API implementation (Envoy Gateway, kgateway, or GKE's managed Gateway) uses Envoy's ext-proc protocol to hand routing decisions to the endpoint picker rather than making them internally, so the intelligence is pluggable and can evolve independently of the underlying proxy. This is the same "separate the generic transport/relay layer from the domain-specific matchmaking policy" split this section's [latency-based matchmaking in multiplayer gaming]({{< relref "latency-based-matchmaking-in-multiplayer-gaming.md" >}}) entry documents for Valve's Steam Datagram Relay — applied here to inference traffic instead of game traffic.

The extension is explicitly scoped to routing *within* a cluster or fleet of self-hosted model servers that an operator already controls — it is not itself a discovery mechanism for finding unaffiliated third-party compute (that remains the IETF drafts/NANDA/libp2p problem documented elsewhere in this section), and it has no notion of price or payment. It is best understood as the open, standardized matchmaking/routing component a compute-marketplace operator could build on top of, rather than a marketplace itself — [llm-d]({{< relref "llm-d.md" >}}) is the most developed example of doing exactly that.

## Notable Developments

- **2026-04-19:** Reached v1.5.0, marked General Availability.
- **2025-06-05:** Publicly announced and introduced via the official Kubernetes blog.

## Sources

- [Gateway API Inference Extension — official docs](https://gateway-api-inference-extension.sigs.k8s.io/) — concepts (InferencePool, endpoint picker), routing criteria
- [Kubernetes Blog — Introducing Gateway API Inference Extension](https://kubernetes.io/blog/2025/06/05/introducing-gateway-api-inference-extension/) — announcement, problem statement
- [GitHub — kubernetes-sigs/gateway-api-inference-extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension) — release status (v1.5.0, GA), license, implementing gateways
- [kgateway — llm-d + kgateway](https://kgateway.dev/blog/llm-d-kgateway/) — worked example of the extension routing real distributed-inference traffic
