---
title: "NANDA (Networked Agents and Decentralized AI)"
date: 2026-08-15
lastmod: 2026-08-15
draft: false
description: "MIT Media Lab research project proposing the 'NANDA Index' — a DNS-like, cryptographically (not blockchain) verified discovery and resolution layer for AI agents and services at internet scale, plus 'AgentFacts' capability records. General-purpose agent-discovery infrastructure rather than a compute-marketplace product, but the most concrete non-blockchain discovery-layer proposal documented in this section beyond the IETF's individual drafts."
research_area: "compute-marketplaces"
source_urls:
  - "https://www.media.mit.edu/publications/beyond-dns-unlocking-the-internet-of-ai-agents-via-the-nanda-index-and-verified-agentfacts/"
  - "https://thenewstack.io/how-mits-project-nanda-aims-to-decentralize-ai-agents/"
  - "https://nanda.mit.edu/"
  - "https://nanda.media.mit.edu/web3quilt"
last_reviewed: 2026-08-15
stale_after_days: 90
related:
  - "compute-marketplaces/ietf-ai-service-discovery-drafts.md"
  - "compute-marketplaces/p2p-discovery-protocols-libp2p-kademlia.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Project NANDA is an MIT Media Lab research effort, led by Ramesh Raskar, proposing infrastructure for discovering and verifying AI agents and services at a scale current DNS was not designed for — "billions to trillions of autonomous AI agents," in the project's own framing. Its core technical proposals are the **NANDA Index**, a lean, rapidly-resolving discovery index, and **AgentFacts**, dynamic and cryptographically verifiable capability/identity records for individual agents. It is explicitly positioned by its own researchers as cryptographically grounded rather than blockchain-dependent, and — unlike this section's other discovery-layer entries — has a live, if early, running deployment rather than existing only as a draft. It targets general AI-agent discovery and interoperability, not compute/inference-marketplace matching specifically, so it belongs in this section as an adjacent discovery-layer building block rather than a marketplace product.

## Key Facts

- Type: Technology — academic research project / open protocol proposal (not a company)
- Institution: MIT Media Lab
- Lead: Ramesh Raskar, Associate Professor, MIT Media Lab
- Status: Active research/pilot deployment as of mid-2026 — the Index is reported hosted across roughly 15 university and partner institutions, with a developer-facing pilot registry ("Join39"/"List39") reporting over 1,000 registered agents
- Blockchain: No — discovery/resolution relies on a CRDT-based update protocol and cryptographic verification of AgentFacts records, not a distributed ledger; a separate, optional "Web3 Quilt" RFP track (led jointly with the Decentralized AI Society) explores bridging NANDA-style registries to Web3 identity systems, but this is described by its own organizers as building interoperability with existing Web3 registries, not a blockchain requirement for NANDA's core index

## What It Is / How It Works

NANDA's starting premise is that DNS — built for a world of comparatively stable, human-registered domains — cannot handle a population of AI agents that can be created, negotiate, delegate tasks, and disappear again within milliseconds. The **NANDA Index** is proposed as a minimal, fast-resolving index (rather than a full-featured registry itself) that points to where an agent's actual record lives, using "adaptive resolvers" and a CRDT (conflict-free replicated data type)-based update mechanism intended to let records propagate and update quickly across a distributed set of index nodes without requiring blockchain-style global consensus. **AgentFacts** are the records themselves — dynamic, cryptographically verifiable statements of an agent's identity and capabilities that a requester can check without a central authority vouching for them.

The project explicitly frames itself as protocol-bridging infrastructure rather than a competitor to existing agent-communication protocols: public materials describe NANDA's Index as designed to interoperate with Anthropic's Model Context Protocol (MCP), Google's Agent2Agent (A2A) protocol, and NLWeb, functioning as the discovery/lookup layer underneath whichever task or tool-calling protocol two agents actually use to talk to each other once they've found one another. This is a materially different scope than this section's other discovery entries: the IETF's individual drafts and the libp2p/Kademlia DHT stack used by Petals/Hivemind are both narrower and more infrastructure-focused (finding a peer or a service endpoint), where NANDA is pitching a broader identity-and-capability-verification layer for a general agent economy, of which discovering available inference compute would be one applicable use case rather than the primary design target.

As of mid-2026, NANDA is best understood as an early, multi-institution research pilot rather than a finished or widely adopted protocol — it has a live index and a growing registered-agent count, but no evidence in sources reviewed for this entry of production use for routing or discovering commercial inference-compute supply specifically.

## Notable Developments

- **2026 (ongoing):** MIT Media Lab publishes "Beyond DNS: Unlocking the Internet of AI Agents via the NANDA Index and Verified AgentFacts," detailing the Index/AgentFacts architecture; separately, NANDA and the Decentralized AI Society issue a "Web3 Quilt" RFP (submissions due June 14, 2025) seeking proposals to bridge NANDA-style registries with existing Web3/blockchain agent-registry ecosystems — an optional interoperability track, not a core dependency of the Index itself.
- **2025 (approx.):** Public presentations describe the project as "a new project out of MIT"; Index reported hosted at roughly 15 university/partner institutions; Join39/List39 pilot registry passes 1,000+ registered agents.

## Key People

**Ramesh Raskar** — Associate Professor, MIT Media Lab; project lead.
- LinkedIn: not found — TODO: verify current profile

### People — Last Reviewed: 2026-08-15

## Sources

- [MIT Media Lab — Beyond DNS: Unlocking the Internet of AI Agents via the NANDA Index and Verified AgentFacts](https://www.media.mit.edu/publications/beyond-dns-unlocking-the-internet-of-ai-agents-via-the-nanda-index-and-verified-agentfacts/) — Index/AgentFacts architecture, CRDT-based resolution, non-blockchain framing
- [The New Stack — How MIT's Project NANDA Aims To Decentralize AI Agents](https://thenewstack.io/how-mits-project-nanda-aims-to-decentralize-ai-agents/) — project lead, pilot deployment scale, protocol-bridging scope (MCP/A2A/NLWeb)
- [NANDA — project site](https://nanda.mit.edu/) — project overview
- [NANDA — Web3 Quilt RFP](https://nanda.media.mit.edu/web3quilt) — optional Web3-interoperability track, scope and framing
