---
title: "LinkedIn draft: Local AI hardware guide - October update"
date: 2026-10-13
draft: true
description: LinkedIn post draft for the October 2026 refresh of the local AI hardware guide (M5 Ultra/M6 Macs, Framework 192GB, current open models).
---

A $5,499 Mac Studio now holds three times the AI model an RTX 5090 can, and once you count the PC the card needs, it's cheaper too.

I just updated my local AI hardware guide with all the latest model and hardware info: the M5 Max and M5 Ultra Mac Studio, the M6 Mac mini, Framework's new 192GB Desktop and the current performance and requirements of the open models (Qwen3.6 and 3.8, DeepSeek V4, Gemma 4, GLM-5.2). Llama got demoted to a footnote since Meta went closed with Muse Spark.

A few things that surprised me:

- MoE changed the math. DeepSeek V4-Flash needs ~170GB to load but only reads 13B parameters per token, so big-memory, modest-bandwidth boxes got a lot more useful.
- Memory prices are biting. The 128GB Framework Desktop went from $1,999 to $3,449, and the 192GB is $6,799.
- I updated some overly optimistic tok/s numbers with a new model that's now used throughout the guide.

Rebuilt cost vs capability chart, model-by-memory-tier guide, and buy links here:

https://www.jaredwatkins.com/posts/2026/04/local-ai-hardware-guide/

#LocalAI #AIHardware #LLM #OpenSource #Apple #AMD #NVIDIA
