---
title: "IETF AI Service Discovery Drafts"
date: 2026-08-04
lastmod: 2026-11-12
draft: false
description: "IETF work on how AI agents, models, and resource providers discover each other: a fast-growing set of individual Internet-Drafts — including a well-known-endpoint capability descriptor and a layered discovery architecture — and, since October 2026, a chartered working group (DAWN) with no adopted protocol yet and milestones running to 2027–2028."
research_area: "compute-marketplaces"
source_urls:
  - "https://www.ietf.org/archive/id/draft-aiendpoint-ai-discovery-00.html"
  - "https://datatracker.ietf.org/doc/draft-am-layered-ai-discovery-architecture/"
  - "https://global-chat.io/experiments/ietf-expiry"
  - "https://datatracker.ietf.org/doc/draft-aiendpoint-ai-discovery/"
  - "https://datatracker.ietf.org/wg/dawn/about/"
  - "https://datatracker.ietf.org/doc/charter-ietf-dawn/history/"
  - "https://datatracker.ietf.org/doc/bofreq-farrel-discovery-of-agents-workloads-and-named-entities/"
  - "https://datatracker.ietf.org/wg/agentproto/about/"
  - "https://datatracker.ietf.org/doc/charter-ietf-agentproto/history/"
last_reviewed: 2026-11-12
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
- **DAWN** — Discovery of Agents, Workloads, and Named entities: the IETF working group (Internet Area) chartered in October 2026 to define how a client discovers public information about AI resources such as agents before interacting with them.
- **BoF** — "Birds of a Feather": an IETF meeting session used to test whether there is enough agreement to form a working group.

## Summary

As of November 2026, "how should an AI agent or service discover another AI agent, model, or compute resource on the open internet" still has no adopted IETF standard, but the work has moved from scattered individual submissions toward a formal venue. The IESG approved the charter of a dedicated working group, DAWN (Discovery of Agents, Workloads, and Named entities), on 22 October 2026, two weeks after chartering a sibling group for agent communication protocols (agentproto). DAWN's own milestones put protocol specifications at the end of 2027, and its charter is limited to initial discovery — explicitly not open-ended search, ranking, or selection. The individual Internet-Drafts that preceded it remain just that: individually submitted, mutually non-interoperable, and subject to six-month expiry. Two drafts fetched directly for this entry illustrate the range of approaches: a lightweight, single-endpoint capability descriptor (`draft-aiendpoint-ai-discovery`, still active) and a more ambitious layered architecture explicitly designed to cover compute-resource discovery, not just agent-to-agent discovery (`draft-am-layered-ai-discovery-architecture`, now expired, though it is listed among the DAWN BoF's candidate solutions and its authors are DAWN proponents). For anyone designing a compute marketplace the practical position is unchanged: there is no standard to adopt yet, only a newly chartered process and a set of competing proposals to watch.

## Key Facts

- Type: standard/specification (proposed, not adopted)
- Status: A working group now exists — DAWN, Internet Area, charter approved 22 October 2026 (chairs Dapeng Liu and Frank Brockners; responsible AD Éric Vyncke) — but as of this review no protocol document has been adopted or published. The two drafts documented below remain individual submissions with no formal standing, citable only as "work in progress" per IETF's own boilerplate
- DAWN scope and schedule: initial discovery of AI resources in three settings (local network, within an organization, and between trusting parties over the public Internet), building on existing IETF protocols with DNS and mDNS to be considered; planned outputs are terminology and use-case documents, an architecture document, and a Standards Track protocol document, with milestones of June 2027 (optional terminology and use cases), December 2027 (protocol specification) and January 2028 (architecture)
- Draft status at this review: `draft-aiendpoint-ai-discovery` is active at version -01 (updated 28 July 2026, expires 29 January 2027); `draft-am-layered-ai-discovery-architecture` expired in September 2026 without a new version
- Related group: agentproto (Agent Communication Protocols; Applications and Real-Time Area; chairs Leslie Daigle and Orie Steele), charter approved 8 October 2026; its charter lists agent discovery as a coordination topic with the Internet and Operations areas rather than as its own deliverable
- Scale of fragmentation: a third-party tracker (Global Chat, a commercial AI-agent discovery product — treat as a self-interested secondary source) counted 11+ competing IETF drafts for AI agent discovery/policy as of early-to-mid 2026 (the DAWN BoF request of June 2026 separately lists 14 relevant drafts), covering mechanisms as varied as file-based well-known policies (agents.txt), DNS-inspired approaches with PKI (ANS), decentralized identifiers (AID), and DNS-based capability records (ACDP) — notably, neither of the two drafts documented in depth below (`draft-aiendpoint-ai-discovery`, `draft-am-layered-ai-discovery-architecture`) appears in that particular tracker's list, which is itself evidence of how scattered this space is even among people trying to catalog it
- Review cadence for this entry: 90 days — drafts expire on a six-month clock and the landscape is changing quickly

## What It Is / How It Works

**`draft-aiendpoint-ai-discovery`** ("The AI Discovery Endpoint," Y. Choi; version -00 published 2026-03-23, renewed as -01 on 2026-07-28, expiring 2027-01-29; not among the drafts listed in the DAWN BoF request) proposes the simplest mechanism in this space: a well-known URI, `/.well-known/ai`, that any web service can serve to expose a structured JSON document describing "the service's identity, available actions, authentication requirements, and operational hints optimized for large language model (LLM) token efficiency." The stated problem is narrow and pragmatic — today an AI agent has to either scrape human-oriented documentation/HTML or rely on a proprietary integration to learn what an API can do; this draft proposes a single, predictable, machine-readable location for that description, directly modeled on the existing `/.well-known/` convention (RFC 8615) used by `security.txt` and ACME.

**`draft-am-layered-ai-discovery-architecture-00`** ("A Layered Approach to AI discovery," Hesham Moussa and Arashmid Akhavain, Huawei Canada, submitted 2026-03-14; expired September 2026 with no successor version, though it is listed under potential solutions in the DAWN BoF request) is a more architecturally ambitious proposal, and the one most directly relevant to a compute marketplace: it explicitly lists "applications discovering model providers or inference endpoints," "workflows discovering compute, storage, or accelerator resources," and "training pipelines discovering data sources" alongside agent-to-agent discovery as instances of the same underlying problem, and argues that today's landscape (DNS-SD, mDNS, CoRE Resource Directory, model hubs, data catalogs, and agent-specific mechanisms like A2A and MCP) is fragmented because each was designed for one object type rather than a general-purpose discovery substrate. Its proposed fix is to split discovery into two layers: a **Discovery Transport Layer (DTL)** that is completely agnostic to what it's carrying — supporting generic operations (advertise, query, resolve, subscribe, update, revoke) over pluggable transports (HTTP, pub/sub, multicast, overlays) — and a **Discovery Client Layer (DCL)** that defines typed, versioned schemas for each kind of discoverable object: an Agent Card, Model Card, Data Provider Card, and — the one of direct interest here — a **Resource Provider Card**, described as covering "compute resources, accelerators, storage, availability, and cost models." Notably, the draft explicitly flags several operational problems a real inference/compute discovery mechanism would need to solve that narrower proposals ignore: **state-dependent responses** (a provider exposing live load/queue-depth/availability rather than a static record), **notification-driven interaction** (subscribing to be told when a busy provider becomes available, rather than polling), **partial information disclosure** (a provider revealing only a minimal "busy" status until it's actually available), **wide-scope query protection** (preventing a vague query like "find an agent who can fix my car" from triggering an unbounded, resource-exhausting search), and **exploratory/delegated discovery** via autonomous crawler agents that roam the network reporting findings back asynchronously. The draft explicitly notes blockchain as a candidate mechanism for the "reliability and service guarantee" problem, without committing to it.

**Why this matters for a compute marketplace specifically.** Both drafts, and the layered-architecture one in particular, are attacking exactly the discovery-protocol gap this section's overview identifies: today's inference marketplaces either hardcode their own provider list (OpenRouter) or use a blockchain's on-chain state as the registry (Akash) — neither exposes a general, IETF-standardized "here is a machine-readable card describing what compute I have, at what price, with what current queue depth" that a buyer's client could discover the same way it discovers, say, a mail server via DNS. If a Resource Provider Card–style schema were ever adopted, it would plug directly into the same three-layer problem (discovery → matchmaking → payment) this section tracks, without requiring every marketplace to invent its own discovery format. As of this review, that remains a proposal, not a deployed reality — and DAWN's charter, by excluding search, ranking and selection, leaves the price- and load-aware matchmaking a compute marketplace needs outside its stated scope.

**From fragmentation to a chartered process.** Through mid-2026 every draft in this area was an individual submission with no IETF working group behind it, and a third-party tracker counted 11+ separate, non-interoperable AI-discovery-related drafts — covering everything from simple well-known-file policy declarations to DNS-inspired PKI schemes to decentralized-identifier approaches — several already lapsed or about to lapse. A WG-forming BoF request for DAWN (editor Adrian Farrel; proponents including both authors of the layered-architecture draft) was approved for IETF 126, chartering review began in August 2026, and the IESG approved the charter on 22 October 2026. A chartered group is the start of standardization, not its result: DAWN has yet to adopt documents, its candidate inputs still disagree on mechanism (DNS-based records, directories, well-known URIs, identifier schemes), and its first protocol milestone is more than a year out. Anyone designing a compute-marketplace discovery mechanism today should still expect to build something bespoke, while tracking DAWN for the eventual common format.

## Notable Developments

- **2026-10-22:** IESG approved the DAWN working group charter (`charter-ietf-dawn-01`), after internal review from 24 August and external review from 9 October.
- **2026-10-08:** IESG approved the charter of the agentproto (Agent Communication Protocols) working group.
- **2026-09:** `draft-am-layered-ai-discovery-architecture-00` expired without renewal.
- **2026-07-28:** `draft-aiendpoint-ai-discovery-01` published, extending that draft to 29 January 2027.
- **2026-06-12:** DAWN BoF request (version 08) approved as WG-forming, listing 14 relevant Internet-Drafts including a DAWN problem statement co-authored by Akhavain and Moussa.
- **2026-03-23:** `draft-aiendpoint-ai-discovery-00` published (Y. Choi), proposing the `/.well-known/ai` capability endpoint.
- **2026-03-14/15:** `draft-am-layered-ai-discovery-architecture-00` published (Moussa & Akhavain, Huawei Canada), proposing the DTL/DCL layered discovery architecture including a Resource Provider Card object type.
- **Early-to-mid 2026 (exact date range unconfirmed):** Third-party tracking site Global Chat counts 11+ competing IETF drafts touching AI agent/service discovery and policy, none interoperable, with the earliest (an unrelated `agents.txt`-style policy draft) already lapsed as of that snapshot — cited here as directional evidence of fragmentation, not as an authoritative or complete IETF record.

## Key People

**Yeongjae Choi** — Author of `draft-aiendpoint-ai-discovery`, submitted individually under "AIEndpoint" (no organizational affiliation stated in the draft). No further biographical information independently confirmed as of this review — TODO.

**Hesham Moussa and Arashmid Akhavain** — Authors of `draft-am-layered-ai-discovery-architecture`, both affiliated with Huawei Canada per the draft's author addresses (the Datatracker record now shows a personal email address for Moussa and a Huawei address for Akhavain). Both are listed as proponents of the DAWN BoF and as co-authors of its problem-statement draft. No further biographical information independently confirmed as of this review — TODO.

**Dapeng Liu and Frank Brockners** — Chairs of the DAWN working group; **Éric Vyncke** — responsible Area Director; **Adrian Farrel** — editor of the DAWN BoF request. Affiliations not confirmed in this review — TODO.

### People — Last Reviewed: 2026-11-12

## Sources

- [The AI Discovery Endpoint — IETF Internet-Draft](https://www.ietf.org/archive/id/draft-aiendpoint-ai-discovery-00.html) — full text of `draft-aiendpoint-ai-discovery-00`
- [A Layered Approach to AI discovery — IETF Datatracker](https://datatracker.ietf.org/doc/draft-am-layered-ai-discovery-architecture/) — full text and status of `draft-am-layered-ai-discovery-architecture-00` (shown as expired at this review)
- [State of Agent Protocol Standardization — Global Chat](https://global-chat.io/experiments/ietf-expiry) — third-party (commercially interested) count and comparison of competing IETF agent-discovery drafts; used here only for directional fragmentation evidence, not as an authoritative IETF record
- [The AI Discovery Endpoint — IETF Datatracker](https://datatracker.ietf.org/doc/draft-aiendpoint-ai-discovery/) — current version (-01), update and expiry dates
- [DAWN working group — IETF Datatracker](https://datatracker.ietf.org/wg/dawn/about/) — charter text, chairs, area, milestones
- [DAWN charter history — IETF Datatracker](https://datatracker.ietf.org/doc/charter-ietf-dawn/history/) — review and approval dates
- [BoF request: Discovery of Agents, Workloads, and Named entities — IETF Datatracker](https://datatracker.ietf.org/doc/bofreq-farrel-discovery-of-agents-workloads-and-named-entities/) — proponents and the list of relevant drafts
- [agentproto working group — IETF Datatracker](https://datatracker.ietf.org/wg/agentproto/about/) and [charter history](https://datatracker.ietf.org/doc/charter-ietf-agentproto/history/) — sibling group for agent communication protocols; approval date
