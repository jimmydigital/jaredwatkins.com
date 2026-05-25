---
title: "LinkedIn: Picking hardware for local AI inference in 2026"
date: 2026-04-07
draft: true
description: "LinkedIn version of the local AI hardware guide -- shorter form suitable for social sharing with link back to full post."
tags: ["ai", "hardware", "linkedin"]
categories: ["Computing and Tech"]
---

**Picking hardware for local AI inference

Everyone asks "what's the best hardware for running AI locally?" and gets a non-answer. The real problem is that local AI in 2026 is five different markets wearing the same buzzword and most people are arguing past each other because they're optimizing for completely different things.

Here's the quick version of how I think about it:

**Raw speed when the model fits:** Discrete NVIDIA GPUs win here. RTX 5090 and RTX PRO 6000 both hit 1792 GB/s.  The difference is 32GB vs 96GB of VRAM, which determines what you can load in the first place.

**Biggest one-box memory:** Apple Silicon. The Mac Studio M3 Ultra goes up to 512GB of unified memory (the 512GB config is reportedly hard to find right now, but the 192GB sits around $8,000). It's the only consumer-ish path to running genuine frontier-class open source models (Llama 4 Maverick, DeepSeek-V3) without going full multi-GPU server.

**Coherent NVIDIA appliance:** DGX Spark. 128GB + CUDA stack in a compact box. Launched at $3,999, now $4,699. Not a bandwidth monster, but that software ecosystem matters.

**First real x86 unified-memory play:** Framework Desktop with AMD Strix Halo. Up to 128GB assignable as GPU memory on Windows for $1,999. Genuinely the most interesting price-to-capability ratio right now for anyone who's been waiting for x86 to matter again in local AI.

**Fully open source stack:** Tenstorrent. Wormhole and Blackhole cards at competitive bandwidth for ~$1,400. Root for these guys.

A few things worth knowing: MoE models have changed everything. A 400B parameter Llama 4 Maverick activates only 17B parameters per token so capacity requirements are more nuanced than they used to be. And "technically runs" is not the same as "useful." Partial layer offloading and disk-based inference can get a huge model nominally running on small hardware, but once you're below ~5 tokens/second it's basically a demo, not a tool.

I put together a longer breakdown with a cost-vs-memory-performance chart, a scoring methodology, model-to-hardware mapping by memory tier, and buy links for everything discussed.

More detail: https://jaredwatkins.com/posts/2026/04/local-ai-hardware-guide/

#AI #LocalAI #LLM #Hardware #OpenSource #MachineLearning #NVIDIA #Apple #AMD #Tenstorrent
