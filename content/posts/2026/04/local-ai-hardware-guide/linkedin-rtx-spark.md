---
title: "LinkedIn draft: Local AI hardware guide - RTX Spark update"
date: 2026-06-02
draft: true
description: LinkedIn post draft for the RTX Spark update to the local AI hardware guide.
tags:
  - ai
  - hardware
  - nvidia
  - local-inference
categories:
  - Computing and Tech
---

Your feed is likely littered with bold claims from Jensen Huang around the new RTX Spark. That it will run "every Windows app ever made" and deliver 1 petaflop of AI performance in a laptop. Both claims deserve a closer look.

The 1 petaflop figure is FP4 with structured sparsity enabled, a 2x multiplier that only applies when model weights are at least 50% zeros. Most aren't. At FP16 the number is closer to 250 teraflops. NVIDIA has been doing this with GPU TOPS figures for years; the RTX Spark version is just more brazen because FP4 inference pipelines aren't as established yet.

The Windows on ARM story is actually better than its history suggests. Surface RT was a disaster, Windows 10 ARM was painful, but the current Prism emulator runs most x86 apps with around 10 to 15% overhead with over 93% of commonly used apps run natively today. The remaining gap is kernel-mode drivers: anti-cheat, some corporate security tools, certain audio plugins. Jensen's "every app ever made" claim runs into that wall, but for most developer and productivity workflows it's close to true.

The harder problem is what 273 GB/s actually means when you're waiting on output. On a 70B model, the DGX Spark (same silicon, same bandwidth as RTX Spark) does around 3 tokens per second which is more like a demo. The Mac Studio M4 Max does 20 to 25 on the same model, at $2,000, which is likely less than an RTX Spark laptop will cost. If you need the full CUDA stack in a portable Windows device, RTX Spark is the only way to get it. If you're buying for throughput on the models that actually use that memory, the math doesn't work in its favor.

Full breakdown for every platform worth knowing about in the updated post:

https://www.jaredwatkins.com/posts/2026/04/local-ai-hardware-guide/

#LocalAI #NVIDIA #RTXSpark #AIHardware
