---
title: "P2P Discovery for Inference: libp2p + Kademlia DHT Swarms"
date: 2026-08-04
lastmod: 2026-08-04
draft: false
description: "The libp2p/Kademlia distributed-hash-table peer-discovery stack — borrowed from BitTorrent/IPFS — used by Hivemind, Petals, and derivative projects (e.g. KwaaiNet) to let volunteer GPU/CPU nodes find each other and jointly serve large models; distinct from and not interoperable with Akash's blockchain-based marketplace matching."
research_area: "compute-marketplaces"
source_urls:
  - "https://github.com/learning-at-home/hivemind"
  - "https://github.com/bigscience-workshop/petals"
  - "https://akash.network/docs/node-operators/architecture/overview"
  - "https://github.com/Kwaai-AI-Lab/KwaaiNet"
last_reviewed: 2026-08-04
stale_after_days: 180
related:
  - "compute-marketplaces/openrouter.md"
  - "compute-marketplaces/latency-based-matchmaking-in-multiplayer-gaming.md"
  - "datacenters/distributed-compute/akash-network.md"
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Glossary

- **libp2p** — A modular peer-to-peer networking stack (originally built for IPFS) providing transport, encryption, NAT traversal, and peer-discovery primitives that applications compose rather than a single protocol.
- **Kademlia DHT** — A distributed hash table design (Maymounkov & Mazières, 2002) that lets a large set of peers collectively store and look up key/value data — here, "which peer is serving which model layer" — without any central directory; the same lookup structure underlies BitTorrent's trackerless mode.
- **DHT swarm** — The set of peers participating in a given Kademlia DHT instance; "joining the swarm" means bootstrapping into that peer set.
- **Block sharding** — Splitting a large model's transformer layers across multiple peers, each hosting a contiguous subset ("blocks"), so no single machine needs enough memory for the whole model.

## Summary

A cluster of open-source projects — most originating from Hivemind (a PyTorch decentralized-training library) and its downstream application Petals — let volunteer GPU owners collectively serve models too large for any one machine, using a libp2p-based Kademlia distributed hash table for peer discovery instead of a central registry, blockchain, or company-run matchmaking service. This is architecturally the closest thing to a fully decentralized "discovery protocol" for inference compute that exists in production-adjacent form today, and it is a different mechanism entirely from either OpenRouter's posted-price aggregation or Akash Network's on-chain reverse auction — it has no pricing layer at all, being built for volunteer/donated compute rather than a paid marketplace.

## Key Facts

- Type: open-source protocol/library stack (not a company)
- Origin: Hivemind, developed by the Learning@home research collective (contributors including Max Ryabinin, Alexander Borzunov, and collaborators, with sponsorship from Yandex Research and, as of this review, compute sponsorship from Prime Intellect via Modal for CI); Petals built on top of Hivemind by the BigScience workshop
- Status: Both are active open-source projects (Hivemind: 2.5k GitHub stars, most recent tagged release January 2026 per its release history; Petals: 10.1k GitHub stars, most recent tagged release September 2023) rather than commercial products — treat as research-stage/community infrastructure, not a marketplace with pricing or SLAs
- Key mechanism: peer discovery and model-layer location via a Kademlia DHT, transported over libp2p (specifically, Hivemind bundles a precompiled `go-libp2p-daemon` binary rather than a pure-Python libp2p implementation)
- Reported throughput (Petals, single-batch inference, unverified beyond the project's own README): up to ~6 tokens/sec for Llama 2 70B and ~4 tokens/sec for Falcon 180B when run across the public volunteer swarm

## What It Is / How It Works

**The core mechanism.** Hivemind's stated key feature is "distributed training without a master node: Distributed Hash Table allows connecting computers in a decentralized network." Concretely, when a node joins, it bootstraps into a Kademlia DHT swarm — the same style of structure BitTorrent uses for trackerless peer discovery — and both queries and advertises key/value records into that DHT: which model a peer can serve, which specific transformer-layer blocks it is hosting, and (for training use cases) gradient/parameter-averaging coordination data. There is no central server tracking swarm membership; any peer can look up "who is hosting layers 40–48 of this model" by querying the DHT, and any peer can leave or join without a coordinator needing to be informed first.

**Petals' inference application.** Petals uses Hivemind's DHT to implement block-sharded LLM inference and fine-tuning "BitTorrent-style": a large model's layers are split into contiguous blocks, and volunteers each load and serve a subset sized to their own GPU memory. A client wanting to run inference discovers, via the DHT, a chain of peers collectively covering the full model, and streams activations through that chain sequentially — the project's own description claims this is "up to 10x faster" than local CPU/disk offloading for models that don't fit on a single machine, though this is the project's own benchmark claim rather than an independently audited figure. Petals explicitly frames this as **volunteer computing**, not a paid marketplace — its README asks users to "help serving one of the available models" and thanks contributors by name on a public swarm-health monitor, with no pricing, billing, or payment mechanism of any kind. Petals' own security documentation warns that swarm operators can, in principle, see the data passing through blocks they host, and offers a "private swarm" mode (a DHT restricted to a trusted peer set) as the mitigation for sensitive data — the discovery mechanism does not itself provide confidentiality.

**Derivative projects extend the same DHT for discovery beyond training/inference.** KwaaiNet, an early-stage project from the Kwaai AI Lab / GliaNet Foundation, explicitly states it runs "a libp2p + Kademlia DHT swarm compatible with Petals/Hivemind for node discovery and health checks," and layers additional discovery use cases onto the same DHT — for example, a `kwaainet vpk discover` command that finds encrypted-vector-storage-capable peers on the DHT and returns their peer ID, storage mode, and capacity with no IP addresses exposed, and DHT-based announcement of a signed "fiduciary pledge" credential attached to each node's identity. This illustrates the DHT-as-discovery-substrate pattern generalizing beyond model-layer lookup to other resource-discovery use cases (storage, in this case) using the identical underlying mechanism — directly analogous to the IETF drafts' proposed separation of a generic "discovery transport layer" from object-specific "discovery client" schemas (see [IETF AI Service Discovery Drafts]({{< relref "ietf-ai-service-discovery-drafts.md" >}})).

**What this is not.** This DHT-based discovery mechanism is architecturally unrelated to Akash Network's marketplace matching. Akash is a Cosmos SDK/CometBFT (formerly Tendermint) blockchain: its P2P layer uses CometBFT's own gossip protocol for block/transaction propagation and its own "PeX" (peer exchange) for validator/full-node discovery, and marketplace matching (bids, leases, provider discovery) happens through on-chain state — deployment requests, bids, and leases recorded as blockchain transactions and queried via gRPC/REST/RPC — not through a Kademlia DHT. A libp2p/Kademlia swarm and a CometBFT-based blockchain are both "peer-to-peer" in the loose sense but solve discovery in incompatible ways: one is a pure key/value lookup structure with no consensus or pricing, the other is a full blockchain with consensus, an on-chain order book, and token-denominated settlement. A system wanting both trust-minimized peer discovery *and* priced, auctioned matching would need to combine mechanisms like these rather than picking one off the shelf.

## Notable Developments

- **2026-01-03:** Hivemind 1.1.12 released — cross-platform build fixes, minor refactors (most recent tagged release as of this review).
- **2023-09-06 (most recent tagged release as of this review):** Petals v2.2.0 — added Falcon support, macOS support.
- **2023:** Petals paper "Distributed Inference and Fine-tuning of Large Language Models Over The Internet" presented at NeurIPS, formalizing the block-sharding-over-DHT approach documented here.
- **2022:** Original Petals paper ("Petals: Collaborative Inference and Fine-tuning of Large Models") published and demonstrated at ACL 2023.
- **2020-04:** Hivemind's foundational "Towards Crowdsourced Training of Large Neural Networks using Decentralized Mixture-of-Experts" work published, establishing the DHT-based decentralized-training approach Petals later applied to inference.

## Key Organizations

**Learning@home / Hivemind maintainers** — Open-source research collective (Max Ryabinin, Alexander Borzunov, Michael Diskin, and collaborators named in the project's citation list); not a commercial entity. As of this review, Prime Intellect sponsors compute resources (via Modal) for Hivemind's CI pipeline — a notable connection given Prime Intellect's own work in decentralized-training compute marketplaces, though no further corporate relationship is confirmed.

**BigScience workshop** — The research collective (a Hugging Face-affiliated open collaboration) responsible for Petals, built on top of Hivemind.

**Kwaai AI Lab / GliaNet Foundation** — Early-stage, pre-1.0 project (KwaaiNet) extending the Petals/Hivemind-compatible DHT to additional discovery use cases (encrypted vector storage, credentialed peer trust scoring); appears to be a nonprofit/foundation-structured research lab rather than a venture-backed company — treat scale and adoption claims as unverified pre-release figures until independently confirmed.

## Sources

- [Hivemind — GitHub](https://github.com/learning-at-home/hivemind) — DHT-based decentralized training architecture, libp2p daemon dependency, release history, sponsorship note
- [Petals — GitHub](https://github.com/bigscience-workshop/petals) — block-sharded inference over the Hivemind DHT, throughput claims, private-swarm security model, release history
- [Akash Network Node Architecture Overview](https://akash.network/docs/node-operators/architecture/overview) — CometBFT/Cosmos SDK P2P and on-chain marketplace-module architecture, cited here to establish the contrast with DHT-based discovery
- [KwaaiNet — GitHub](https://github.com/Kwaai-AI-Lab/KwaaiNet) — libp2p/Kademlia DHT swarm compatible with Petals/Hivemind, extended discovery use cases (storage peer discovery, credentialed trust scoring)
