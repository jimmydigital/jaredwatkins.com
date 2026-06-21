---
title: "LinkedIn: Clustering local AI, what nobody tells you before you buy the hardware"
date: 2026-06-20
draft: true
description: "LinkedIn post on AI inference clustering, model-dependent tradeoffs and what to know before buying."
tags:
  - ai
  - llm
  - local-inference
  - hardware
categories:
  - Computing and Tech
---

Have you thought about clustering local machines to run bigger AI models? A few things worth knowing before you go buy a second box.

Clustering works, but it's not a simple upgrade. Whether it helps depends almost entirely on which kinds of models you're running and what hardware platform you have. Do it wrongly and your performance can actually get worse with additional nodes.

The big open-source models today come in two flavors. Dense models use all their parameters on every request (they're memory-hungry all the time). Mixture-of-experts (MoE) models carry a large total parameter count but only activate a fraction of it per request. DeepSeek, Qwen3-235B, Kimi K2 are MoE. Llama 3.1 70B and 405B are dense.

That distinction matters a lot for clustering. MoE models are well-suited to spreading across machines because the inter-node communication is relatively light. You're passing routing decisions and partial activations, not the full weight matrix on every token. Dense models need the nodes to talk to each other constantly and heavily, which means the network between your machines becomes the bottleneck almost immediately.

The network is where most small cluster builds go wrong. For Apple Silicon Macs, you need Thunderbolt 5 cables between every machine. There are no switches, it's point-to-point, and you're capped at four nodes with today's hardware. For NVIDIA, you need at least 25GbE between nodes, and ideally InfiniBand if you're serious about it. Running two H100 servers over a consumer switch kills most of the gains you paid for.

The software layer also matters more than people expect. llama.cpp's built-in clustering sends model layers from one machine to the next in sequence, which gets slower as you add nodes. Tools like exo use a different approach that computes in parallel across nodes and actually speeds up as you add hardware, but only with the right network and the right model type.

The short version: if you're thinking about clustering two Mac Studios to run a bigger model, make sure it's a MoE model, connect them with proper Thunderbolt 5 cables, and use exo rather than llama.cpp. If you're on NVIDIA, the interconnect budget is not optional.

Full breakdown on hardware tiers, networking requirements, software stack, and what to realistically expect from purchasable hardware:

https://www.jaredwatkins.com/posts/2026/05/smb-inference-stack/
