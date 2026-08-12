---
title: "IETF AI Service Discovery Drafts"
date: 2026-08-04
lastmod: 2026-08-04
draft: false
description: "A fragmented, fast-moving set of individual (non-working-group) IETF Internet-Drafts proposing standards for how AI agents, models, and resource providers discover each other — including a well-known-endpoint capability descriptor and a layered discovery-transport architecture — none yet adopted, none interoperable with each other."
research_area: "compute-marketplaces"
source_urls:
  - "https://www.ietf.org/archive/id/draft-aiendpoint-ai-discovery-00.html"
  - "https://datatracker.ietf.org/doc/draft-am-layered-ai-discovery-architecture/"
  - "https://global-chat.io/experiments/ietf-expiry"
last_reviewed: 2026-08-04
stale_after_days: 90
related:
  - "compute-marketplaces/p2p-discovery-protocols-libp2p-kademlia.md"
  - "compute-marketplaces/openrouter.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Glossary

- **Internet-Draft (I-D)** — A working document submitted to the IETF; anyone may submit one. An I-D has **no formal standing** in the IETF standards process until it is adopted by a working group and advances toward RFC status. Drafts expire after six months unless renewed.
- **Well-known URI** — A standardized path prefix (`/.well-known/...`, defined by RFC 8615) that lets a client find a specific resource on any domain without prior negotiation — the same pattern used by `/.well-known/security.txt` and Let's Encrypt's ACME challenge.
- **Discovery Transport Layer (DTL) / Discovery Client Layer (DCL)** — Terminology from `draft-am-layered-ai-discovery-architecture`: the DTL is the generic advertise/query/resolve/subscribe mechanism; the DCL is the object-specific schema (agent card, model card, resource-provider card) that rides on top of it.

## Summary

As of mid-2026, "how should an AI agent or service discover another AI agent, model, or compute resource on the open internet" has no adopted IETF standard — instead there is a fragmented and fast-growing set of individually submitted Internet-Drafts, none of which has working-group backing, none of which is interoperable with the others, and several of which will expire (lapse) within months of filing unless their authors renew them. Two drafts fetched directly for this entry illustrate the range of approaches on the table: a lightweight, single-endpoint capability descriptor (`draft-aiendpoint-ai-discovery`) and a more ambitious layered architecture proposal explicitly designed to cover compute-resource discovery, not just agent-to-agent discovery (`draft-am-layered-ai-discovery-architecture`). This fragmentation is itself the most important fact for anyone designing a compute marketplace today: there is no standard to adopt yet, only a set of competing proposals to watch.

## Key Facts

- Type: standard/specification (proposed, not adopted)
- Status: All known drafts in this space are individual submissions ("I-D Exists" in IETF Datatracker terms) with no assigned working group and no RFC stream — they carry no formal standing and may be cited only as "work in progress," per IETF's own boilerplate
- Scale of fragmentation: a third-party tracker (Global Chat, a commercial AI-agent discovery product — treat as a self-interested secondary source) counted 11+ competing IETF drafts for AI agent discovery/policy as of early-to-mid 2026, covering mechanisms as varied as file-based well-known policies (agents.txt), DNS-inspired approaches with PKI (ANS), decentralized identifiers (AID), and DNS-based capability records (ACDP) — notably, neither of the two drafts documented in depth below (`draft-aiendpoint-ai-discovery`, `draft-am-layered-ai-discovery-architecture`) appears in that particular tracker's list, which is itself evidence of how scattered this space is even among people trying to catalog it
- Review cadence for this entry: 90 days — drafts expire on a six-month clock and the landscape is changing quickly

## What It Is / How It Works

**`draft-aiendpoint-ai-discovery-00`** ("The AI Discovery Endpoint," Y. Choi, published 2026-03-23, expires 2026-09-24) proposes the simplest mechanism in this space: a well-known URI, `/.well-known/ai`, that any web service can serve to expose a structured JSON document describing "the service's identity, available actions, authentication requirements, and operational hints optimized for large language model (LLM) token efficiency." The stated problem is narrow and pragmatic — today an AI agent has to either scrape human-oriented documentation/HTML or rely on a proprietary integration to learn what an API can do; this draft proposes a single, predictable, machine-readable location for that description, directly modeled on the existing `/.well-known/` convention (RFC 8615) used by `security.txt` and ACME.

**`draft-am-layered-ai-discovery-architecture-00`** ("A Layered Approach to AI discovery," Hesham Moussa and Arashmid Akhavain, Huawei Canada, last updated 2026-03-14, expires 2026-09-16) is a more architecturally ambitious proposal, and the one most directly relevant to a compute marketplace: it explicitly lists "applications discovering model providers or inference endpoints," "workflows discovering compute, storage, or accelerator resources," and "training pipelines discovering data sources" alongside agent-to-agent discovery as instances of the same underlying problem, and argues that today's landscape (DNS-SD, mDNS, CoRE Resource Directory, model hubs, data catalogs, and agent-specific mechanisms like A2A and MCP) is fragmented because each was designed for one object type rather than a general-purpose discovery substrate. Its proposed fix is to split discovery into two layers: a **Discovery Transport Layer (DTL)** that is completely agnostic to what it's carrying — supporting generic operations (advertise, query, resolve, subscribe, update, revoke) over pluggable transports (HTTP, pub/sub, multicast, overlays) — and a **Discovery Client Layer (DCL)** that defines typed, versioned schemas for each kind of discoverable object: an Agent Card, Model Card, Data Provider Card, and — the one of direct interest here — a **Resource Provider Card**, described as covering "compute resources, accelerators, storage, availability, and cost models." Notably, the draft explicitly flags several operational problems a real inference/compute discovery mechanism would need to solve that narrower proposals ignore: **state-dependent responses** (a provider exposing live load/queue-depth/availability rather than a static record), **notification-driven interaction** (subscribing to be told when a busy provider becomes available, rather than polling), **partial information disclosure** (a provider revealing only a minimal "busy" status until it's actually available), **wide-scope query protection** (preventing a vague query like "find an agent who can fix my car" from triggering an unbounded, resource-exhausting search), and **exploratory/delegated discovery** via autonomous crawler agents that roam the network reporting findings back asynchronously. The draft explicitly notes blockchain as a candidate mechanism for the "reliability and service guarantee" problem, without committing to it.

**Why this matters for a compute marketplace specifically.** Both drafts, and the layered-architecture one in particular, are attacking exactly the discovery-protocol gap this section's overview identifies: today's inference marketplaces either hardcode their own provider list (OpenRouter) or use a blockchain's on-chain state as the registry (Akash) — neither exposes a general, IETF-standardized "here is a machine-readable card describing what compute I have, at what price, with what current queue depth" that a buyer's client could discover the same way it discovers, say, a mail server via DNS. If a Resource Provider Card–style schema were ever adopted, it would plug directly into the same three-layer problem (discovery → matchmaking → payment) this section tracks, without requiring every marketplace to invent its own discovery format. As of this review, that remains a proposal, not a deployed reality.

**The fragmentation problem, honestly.** Both drafts are individual submissions with no IETF working group behind them, and a third-party tracker counted 11+ separate, non-interoperable AI-discovery-related drafts circulating in the IETF process as of early-to-mid 2026 — covering everything from simple well-known-file policy declarations to DNS-inspired PKI schemes to decentralized-identifier approaches. Several of those tracked drafts carry six-month expiry clocks that had already lapsed or were about to lapse as of that tracker's snapshot. The realistic read: this is a "many flowers blooming, none yet chosen" phase, not a standards process converging on an answer, and anyone designing a compute-marketplace discovery mechanism today should expect to build something bespoke rather than adopt an IETF standard that doesn't yet exist.

## Notable Developments

- **2026-03-23:** `draft-aiendpoint-ai-discovery-00` published (Y. Choi), proposing the `/.well-known/ai` capability endpoint; expires 2026-09-24 absent renewal.
- **2026-03-14/15:** `draft-am-layered-ai-discovery-architecture-00` published (Moussa & Akhavain, Huawei Canada), proposing the DTL/DCL layered discovery architecture including a Resource Provider Card object type; expires 2026-09-16 absent renewal.
- **Early-to-mid 2026 (exact date range unconfirmed):** Third-party tracking site Global Chat counts 11+ competing IETF drafts touching AI agent/service discovery and policy, none interoperable, with the earliest (an unrelated `agents.txt`-style policy draft) already lapsed as of that snapshot — cited here as directional evidence of fragmentation, not as an authoritative or complete IETF record.

## Key People

**Yeongjae Choi** — Author of `draft-aiendpoint-ai-discovery`, submitted individually under "AIEndpoint" (no organizational affiliation stated in the draft). No further biographical information independently confirmed as of this review — TODO.

**Hesham Moussa and Arashmid Akhavain** — Authors of `draft-am-layered-ai-discovery-architecture`, both affiliated with Huawei Canada per the draft's author addresses. No further biographical information independently confirmed as of this review — TODO.

### People — Last Reviewed: 2026-08-04

## Sources

- [The AI Discovery Endpoint — IETF Internet-Draft](https://www.ietf.org/archive/id/draft-aiendpoint-ai-discovery-00.html) — full text of `draft-aiendpoint-ai-discovery-00`
- [A Layered Approach to AI discovery — IETF Datatracker](https://datatracker.ietf.org/doc/draft-am-layered-ai-discovery-architecture/) — full text and status of `draft-am-layered-ai-discovery-architecture-00`
- [State of Agent Protocol Standardization — Global Chat](https://global-chat.io/experiments/ietf-expiry) — third-party (commercially interested) count and comparison of competing IETF agent-discovery drafts; used here only for directional fragmentation evidence, not as an authoritative IETF record
