---
title: "llm-d"
date: 2026-08-15
lastmod: 2026-08-15
draft: false
description: "CNCF sandbox project — founded by Red Hat, Google Cloud, IBM Research, CoreWeave, and NVIDIA — providing a production-grade, open-source distributed inference serving stack for Kubernetes, built on vLLM and the Gateway API Inference Extension. Its KV-cache-aware routing and disaggregated prefill/decode scheduling are the most mature non-blockchain reference implementation in this section of the 'route each inference request to whichever backend can serve it fastest' matchmaking problem."
research_area: "compute-marketplaces"
source_urls:
  - "https://github.com/llm-d/llm-d"
  - "https://www.redhat.com/en/about/press-releases/red-hat-launches-llm-d-community-powering-distributed-gen-ai-inference-scale"
  - "https://kgateway.dev/blog/llm-d-kgateway/"
  - "https://developers.redhat.com/articles/2025/10/07/master-kv-cache-aware-routing-llm-d-efficient-ai-inference"
last_reviewed: 2026-08-15
stale_after_days: 90
related:
  - "compute-marketplaces/gateway-api-inference-extension.md"
  - "compute-marketplaces/openrouter.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

llm-d is an open-source, Kubernetes-native distributed inference serving stack that sits on top of model servers like vLLM to optimize how requests are routed and executed across a fleet of GPU-backed replicas. It is a Cloud Native Computing Foundation (CNCF) sandbox project founded by Red Hat, Google Cloud, IBM Research, CoreWeave, and NVIDIA (with AMD, Cisco, Hugging Face, Intel, Lambda, Mistral AI, and academic partners UC Berkeley and University of Chicago also contributing). It is the most developed concrete implementation of the [Gateway API Inference Extension]({{< relref "gateway-api-inference-extension.md" >}})'s routing model documented in this section — a non-blockchain, vendor-neutral counterpart to how OpenRouter or Akash solve the same "get this request to the right backend" problem.

## Key Facts

- Type: Technology — open-source project (CNCF sandbox), not a company
- Founding backers: Red Hat, Google Cloud, IBM Research, CoreWeave, NVIDIA; additional contributors include AMD, Cisco, Hugging Face, Intel, Lambda, Mistral AI, UC Berkeley, and University of Chicago
- Announced: May 20, 2025, at Red Hat Summit (Boston)
- Status: Active CNCF sandbox project; v0.7 as of a May 2026 release cycle
- License: Open source (Apache-2.0, per CNCF sandbox project norms)

## What It Is / How It Works

llm-d's core technical contribution is routing requests *within* a fleet of model-server replicas based on where the work will execute fastest, rather than treating every replica as interchangeable. Its **KV-cache-aware routing** tracks which backend already holds the key-value cache for a given conversation or prompt prefix and preferentially routes follow-up requests there, avoiding redundant recomputation — the same "hot cache" locality problem a CDN solves for static content, applied to inference state. Its **disaggregated prefill/decode** architecture splits the two phases of generating a response — the initial, compute-heavy prefill pass over the prompt, and the subsequent token-by-token decode pass — across separate GPU pools sized and scheduled differently for each phase's distinct resource profile; llm-d's own published benchmarks report up to 70% higher tokens/sec versus a standard (non-disaggregated) vLLM deployment, and elsewhere up to 3x improvement in time-to-first-token with roughly double throughput under service-level-objective constraints, though these are project-reported figures, not independently audited.

The routing intelligence is implemented as an endpoint-picker component for the [Gateway API Inference Extension]({{< relref "gateway-api-inference-extension.md" >}}), commonly deployed via the kgateway gateway controller: the gateway examines the model name, LoRA adapter requirement, and request criticality for each incoming call, then the picker scores available backends on queue depth, KV-cache state, and adapter availability before selecting a destination. This makes llm-d a concrete answer to a question the rest of this section largely leaves open — what does purpose-built, criteria-based inference routing actually look like in production — implemented as Kubernetes-native infrastructure an operator runs themselves rather than a hosted marketplace or a token-incentivized network.

llm-d has no discovery or payment layer of its own: it assumes the operator already controls the fleet of model servers being routed across (a single company's or a single cloud's GPU capacity), which distinguishes it from this section's cross-provider marketplace entries (OpenRouter, Akash) that coordinate hardware belonging to otherwise-unaffiliated parties.

## Notable Developments

- **2026-05 (approx.):** Project at v0.7, per public release notes; ongoing integration work with KServe for combined model-serving/inference-scheduling deployments and multi-turn/batch inference support on OpenShift AI.
- **2025-10:** Red Hat publishes detailed technical guidance on configuring KV-cache-aware routing in llm-d deployments.
- **2025-05-20:** Publicly launched at Red Hat Summit as the "llm-d community," with Red Hat, Google Cloud, IBM Research, CoreWeave, and NVIDIA as founding partners.

## Sources

- [GitHub — llm-d/llm-d](https://github.com/llm-d/llm-d) — project overview, backers, architecture, benchmark claims
- [Red Hat — Red Hat Launches the llm-d Community](https://www.redhat.com/en/about/press-releases/red-hat-launches-llm-d-community-powering-distributed-gen-ai-inference-scale) — launch date, founding partners
- [kgateway — llm-d + kgateway](https://kgateway.dev/blog/llm-d-kgateway/) — routing mechanics, integration with Gateway API Inference Extension, benchmark figures
- [Red Hat Developer — Master KV cache aware routing with llm-d](https://developers.redhat.com/articles/2025/10/07/master-kv-cache-aware-routing-llm-d-efficient-ai-inference) — KV-cache routing technical detail
