---
title: "Base Models for Fine-Tuning"
date: 2026-06-10
lastmod: 2026-06-10
draft: false
description: "A survey of the popular open-weight base models available for fine-tuning as of mid-2026: who makes them, their architectures, release history, licensing terms, and practical suitability for specialist domain fine-tuning on consumer hardware."
research_area: "local-llm-finetuning/fundamentals"
source_urls:
  - "https://huggingface.co/meta-llama"
  - "https://huggingface.co/mistralai"
  - "https://huggingface.co/google"
  - "https://huggingface.co/microsoft"
  - "https://huggingface.co/Qwen"
  - "https://huggingface.co/deepseek-ai"
  - "https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"
last_reviewed: 2026-06-10
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

The open-weight LLM landscape as of mid-2026 is dominated by model families from Meta, Mistral AI, Google DeepMind, Microsoft Research, Alibaba Cloud, and DeepSeek. The pace of releases has accelerated: the current generation (Llama 4, Gemma 4, Qwen3.5, Mistral Small 4, Phi-4 reasoning variants) landed between late 2024 and mid-2026, largely superseding models referenced in older fine-tuning guides. For fine-tuning a specialist model on consumer or prosumer hardware, the relevant range is 7B–17B active parameters — large enough for strong reasoning and language capability, small enough to train with QLoRA on a Mac Mini or a rented A100.

## Key Facts

- **Dominant architecture shift:** MoE (Mixture of Experts) is now standard at the frontier; dense models remain better understood for fine-tuning
- **Licensing landscape:** Apache 2.0 (Mistral, Qwen, Gemma 4, DeepSeek); gated permissive (Llama 4); MIT (Phi, some DeepSeek)
- **Sweet spot for local fine-tuning:** 7B–14B dense or 17B-active MoE with 4-bit QLoRA
- **Primary distribution:** HuggingFace Hub for all families
- **Framework support:** All models below are supported by Unsloth and Axolotl as of mid-2026; MLX support varies (Llama and Mistral best-supported on Apple Silicon)

---

## Model Families

### Meta — Llama 4

**Organization:** Meta AI (Meta Platforms, Inc.) — Menlo Park, California. The Fundamental AI Research (FAIR) team originated the LLaMA series in 2023; Llama 4 came from Meta's broader internal AI division. Note: Meta announced a separate "Meta Superintelligence Labs" unit in April 2026, releasing a closed-weight model (Muse Spark) — but the Llama open-weight line continues in parallel.

**Release history:**
- **February 2023** — LLaMA 1 (7B–65B); research-only license
- **July 2023** — Llama 2 (7B–70B); permissive commercial license
- **April 2024** — Llama 3 (8B, 70B); strong 8B baseline; 8K context
- **July 2024** — Llama 3.1 (8B, 70B, 405B); 128K context; 15.6T token training
- **September 2024** — Llama 3.2 (1B, 3B, 11B vision, 90B vision)
- **December 2024** — Llama 3.3 70B Instruct; improved instruction following
- **April 5, 2025** — Llama 4 Scout and Maverick; first MoE architecture in the Llama line; natively multimodal (text + image)

**Architecture (Llama 4):** First Llama generation to use sparse Mixture of Experts. Both Scout and Maverick have **17B active parameters** per forward pass regardless of total parameter count — the compute cost is that of a 17B model. Scout uses 16 experts (109B total); Maverick alternates dense and MoE layers with 128 experts (400B total). Pretrained on 40 trillion tokens across 200 languages (data cutoff August 2024). Native multimodal: image + text input is supported at base model level, not a separate vision adapter.

**Available models (Llama 4, current):**

| Model | Active params | Total params | Context | Notes |
|-------|--------------|-------------|---------|-------|
| Llama 4 Scout 17B-16E | 17B | 109B | 10M tokens | 16 experts; fits single server GPU at int4/int8 |
| Llama 4 Maverick 17B-128E | 17B | 400B | 1M tokens | Alternating dense+MoE; BF16 and FP8 formats |
| Llama 4 Behemoth | ~288B active | ~2T total | — | Announced; not yet released as of June 2026 |

Llama 3.1 8B Instruct remains widely used and supported for fine-tuning, particularly on Apple Silicon, where Llama 4's MoE architecture has less mature MLX support as of mid-2026.

**Licensing:** Llama 4 Community License Agreement — permissive for commercial use, gated (HuggingFace access agreement required). Includes a 700M monthly active users threshold clause above which additional terms apply. Not OSI open-source. Cannot be used to train competing foundation models.

**Suitability for specialist fine-tuning:** Llama 4 Scout (17B active) is the current recommended base for users with A100 40GB access — strong capability with manageable active-parameter count. For Apple Silicon (Mac Mini/MacBook), **Llama 3.1 8B Instruct remains the more practical choice** due to mature MLX support and lower memory overhead. Unsloth has published Llama 4 fine-tuning tutorials as of mid-2025; verify Apple Silicon support before starting a Scout fine-tune on Mac hardware.

---

### Mistral AI — Mistral 3 and Small 4

**Organization:** Mistral AI — Paris, France. Founded April 2023 by Arthur Mensch (CEO, ex-DeepMind), Guillaume Lample (ex-Meta FAIR), and Timothée Lacroix (ex-Meta FAIR). Series A €105M (June 2023); Series B €600M at €6B valuation (June 2024). Backed by a16z, Lightspeed, Nvidia, Salesforce, and others. Maintains a dual strategy: Apache 2.0 open-weight community models plus proprietary API models for enterprise.

**Release history:**
- **September 2023** — Mistral 7B v0.1; released via torrent link with no announcement; outperformed Llama 2 13B at half the size
- **December 2023** — Mixtral 8x7B; sparse MoE; 12.9B active / 46.7B total; Apache 2.0
- **March 2024** — Mistral 7B v0.3; updated tokenizer; function calling
- **April 2024** — Mixtral 8x22B; 39B active / 141B total; 64K context
- **July 2024** — Mistral NeMo 12B (with Nvidia); 128K context; Apache 2.0
- **September 2024** — Mistral Small 3 24B; 128K context; Apache 2.0
- **December 2025** — Mistral 3 family: Ministral 3B/8B/14B (dense) + Mistral Large 3 (MoE); Apache 2.0
- **March 16, 2026** — Mistral Small 4; merges Magistral (reasoning), Pixtral (vision), Devstral (agentic coding) into a single model
- **March 23, 2026** — Voxtral TTS; audio model; 9-language zero-shot voice cloning

**Architecture (current generation):** Mistral Small 4 and Mistral Large 3 use a "granular Mixture of Experts" design. Mistral Large 3: 41B active / 675B total parameters; 256K context window. Ministral 14B (dense) achieves 85% on AIME 2025, outperforming Qwen 14B (73.7%), making it one of the strongest small reasoning models available. Mistral Small 4 is a unified multimodal model (text + vision + reasoning + code agent).

**Available models (current):**

| Model | Parameters (active) | Context | License | Released |
|-------|-------------------|---------|---------|---------|
| Ministral 3B | 3B | 128K | Apache 2.0 | Dec 2025 |
| Ministral 8B | 8B | 128K | Apache 2.0 | Dec 2025 |
| Ministral 14B | 14B | 128K | Apache 2.0 | Dec 2025 |
| Mistral Large 3 | 41B active / 675B total | 256K | Apache 2.0 | Dec 2025 |
| Mistral Small 4 | — | 128K | Apache 2.0 | Mar 16, 2026 |

Mistral 7B v0.3 and Mixtral 8x7B remain available and widely supported by fine-tuning frameworks for users who need proven, battle-tested checkpoints.

**Licensing:** Apache 2.0 for all open-weight models — the most permissive of any major family. No HuggingFace gating, no access agreement, genuine OSI-compatible open source. Mistral's commitment to Apache 2.0 is a differentiator. Voxtral and proprietary API models (Mistral Large API, Le Chat) are commercial.

**Suitability for specialist fine-tuning:** Ministral 8B (December 2025, Apache 2.0) is the current best Apache 2.0 alternative to Llama-family models for the 7B–8B tier — no license friction, strong reasoning per the AIME benchmark results. Ministral 14B is compelling for users with A100 access who want best-in-class small-model reasoning without the Qwen Chinese-origin caveat.

---

### Google DeepMind — Gemma 4

**Organization:** Google DeepMind — London, UK / Mountain View, CA. Formed April 2023 by merging Google Brain (founded 2011) and DeepMind (acquired 2014 for ~$500M). Demis Hassabis is CEO. Gemma models originate from the Google Brain lineage of the combined organization and are described as sharing architecture with the Gemini family.

**Release history:**
- **February 2024** — Gemma 1 (2B, 7B); first open-weight from Google; Gemma Terms of Use
- **June 2024** — Gemma 2 (2B, 9B, 27B); Gemma 2 9B outperformed Llama 3.1 8B; 8K context
- **March 12, 2025** — Gemma 3 (1B, 4B, 12B, 27B); 128K context; multimodal; 140+ languages; Gemma 3n sub-family for mobile
- **April 2, 2026** — Gemma 4 (E2B, E4B, 26B MoE, 31B Dense); Apache 2.0 for the first time; multimodal (images + audio)
- **June 3, 2026** — Gemma 4 12B; unified multimodal architecture; processes images and audio without separate encoders

**Architecture (Gemma 4):** Gemma 4 uses interleaved local/global attention (alternating sliding window and full attention layers) and logit soft-capping, both carried forward from Gemma 2. The 26B model is a sparse MoE with only 3.8B active parameters per forward pass. The 31B Dense has no MoE — all parameters active every token, simpler to fine-tune. 256K context on the 26B MoE and 31B Dense. E2B and E4B ("Effective" sizes — parameter counts after efficient architecture) support audio input natively.

**Available models (Gemma 4, current):**

| Model | Parameters (active) | Context | Notes |
|-------|-------------------|---------|-------|
| Gemma 4 E2B | ~2.3B | 128K | Text + image + audio; phone-deployable |
| Gemma 4 E4B | ~4.5B | 128K | Text + image + audio; strong for size |
| Gemma 4 26B MoE | 3.8B active / 26B total | 256K | Efficient; frontier reasoning at low compute cost |
| Gemma 4 31B Dense | 31B | 256K | Best for fine-tuning; 85.2% MMLU Pro; #3 Arena AI |
| Gemma 4 12B | 12B | 128K | Released June 3, 2026; unified multimodal |

**Licensing:** Apache 2.0 for the entire Gemma 4 family — a significant policy change from Gemma 1/2/3 which used the more restrictive Gemma Terms of Use. Gemma 4 Apache 2.0 means unrestricted fine-tuning, commercial deployment, and redistribution. No gating.

**Suitability for specialist fine-tuning:** Gemma 4 31B Dense is the most capable model in the 30B parameter class that fits on an A100 40GB with QLoRA (Unsloth reports 16 GB VRAM needed). The move to Apache 2.0 removes the prior license concern. 256K context comfortably handles long troubleshooting sessions. The 26B MoE has even lower inference cost (3.8B active) but MoE fine-tuning is more complex and less well-supported in community tooling. For Mac-based fine-tuning, Gemma 3 12B (March 2025, supported by MLX) may be the better choice until Gemma 4 MLX support matures.

---

### Microsoft Research — Phi-4

**Organization:** Microsoft Research — Redmond, Washington. The Phi series comes from MSR's AI group, with key contributions from Sebastien Bubeck (VP of Generative AI at Microsoft) and Ronen Eldan. The "textbook quality" data philosophy — training on synthetically generated high-quality text rather than raw web scale — is the defining characteristic of the Phi line.

**Release history:**
- **June 2023** — Phi-1 (1.3B); synthetic Python textbook training; outperformed larger models on coding benchmarks
- **September 2023** — Phi-1.5 (1.3B); extended to common sense reasoning
- **December 2023** — Phi-2 (2.7B); strong reasoning for its size; MIT license
- **April 2024** — Phi-3 Mini/Small/Medium (3.8B, 7B, 14B); 128K context variants; MIT license
- **August 2024** — Phi-3.5 Mini + Phi-3.5 MoE (3.8B; 6.6B active / 42B total)
- **December 12, 2024** — Phi-4 (14B); synthetic data pipeline; strong STEM reasoning; MIT license
- **February 2025** — Phi-4-mini (3.8B) and Phi-4-multimodal; vision + audio + text
- **May 1, 2025** — Phi-4-reasoning (14B), Phi-4-reasoning-plus (14B), Phi-4-mini-reasoning (3.8B); RL-trained reasoning; outperform DeepSeek-R1-Distill-Llama-70B on several benchmarks; beat full DeepSeek-R1 on AIME 2025
- **March 2026** — Phi-4-Reasoning-Vision-15B; visual reasoning; available via HuggingFace and Azure AI Foundry

**Architecture:** Phi-4 and Phi-4-reasoning are standard dense transformers at 14B parameters — same architecture class as Llama 3. Phi-4-reasoning-plus uses reinforcement learning (RL with extended chain-of-thought budget) to produce more accurate step-by-step reasoning at 1.5x more output tokens. Phi-3.5-MoE remains available as a 6.6B active / 42B total sparse model. All Phi models use synthetic training data generated from diverse high-quality sources — a deliberate counter to web-scale noisy pretraining.

**Available models (current):**

| Model | Parameters | Context | License | Released |
|-------|-----------|---------|---------|---------|
| Phi-4-mini | 3.8B | 128K | MIT | Feb 2025 |
| Phi-4-mini-reasoning | 3.8B | 128K | MIT | May 2025 |
| Phi-4 | 14B | 16K | MIT | Dec 12, 2024 |
| Phi-4-reasoning | 14B | 32K | MIT | May 1, 2025 |
| Phi-4-reasoning-plus | 14B | 32K | MIT | May 1, 2025 |
| Phi-4-Reasoning-Vision-15B | 15B | — | MIT | Mar 2026 |
| Phi-3.5 MoE | 6.6B active / 42B total | 128K | MIT | Aug 2024 |

**Licensing:** MIT license across the entire Phi family — the most unrestricted license of any major model family. No gating, no access agreement, fully open source by OSI standards.

**Suitability for specialist fine-tuning:** Phi-4-reasoning (14B, May 2025) is particularly relevant for network troubleshooting: it applies step-by-step chain-of-thought reasoning trained via RL, producing structured diagnostic reasoning before answering. At 14B with a MIT license, it fits in an A100 40GB via QLoRA. Phi-4-mini-reasoning (3.8B) is worth considering for very constrained edge deployments — requires under 3 GB RAM in Q4 quantization but trades quality for footprint. The 16K context window on base Phi-4 is a limitation for long troubleshooting sessions; Phi-4-reasoning extends this to 32K.

---

### Alibaba Cloud — Qwen3 and Qwen3.5

**Organization:** Alibaba Cloud Intelligence (阿里云), a division of Alibaba Group — Hangzhou, China. Developed by the Alibaba DAMO Academy AI research group (Discovery, Adventure, Momentum, Outlook). Alibaba Group is publicly traded (NYSE: BABA; HKEX: 9988). The Qwen team operates under Alibaba Cloud's AI business unit.

**Release history:**
- **September 2023** — Qwen 1.0 (7B–72B); Alibaba's first open-weight release
- **March 2024** — Qwen 1.5 (0.5B–110B); multilingual improvements; chat variants
- **June 2024** — Qwen2 (0.5B–72B); Apache 2.0; strong 7B benchmarks
- **September 2024** — Qwen2.5 (0.5B–72B + Coder and Math variants); frequently outperforms Llama 3.1 8B on technical tasks; Apache 2.0
- **January 2025** — Qwen2.5-VL (3B–72B); vision-language models
- **April 28, 2025** — Qwen3 (0.6B–32B dense; 30B-A3B and 235B-A22B MoE); hybrid thinking mode; Apache 2.0
- **July 2025** — Qwen3-Coder 480B-A35B; code-specialized MoE
- **February 16, 2026** — Qwen3.5 (397B total / 17B active MoE); 256K native context; 256 experts
- **April 2026** — Qwen3.5-Omni (multimodal, proprietary) and Qwen3.6-Plus (proprietary)
- **May 20, 2026** — Qwen3.7-Max announced at Apsara Summit; details limited

**Architecture (Qwen3 / Qwen3.5):** Qwen3 uses standard dense transformer architecture for smaller models and fine-grained MoE for larger ones. Key capability: **hybrid thinking mode** — models can switch between chain-of-thought ("thinking") and direct-answer ("non-thinking") mode by changing chat template, without separate model weights. Qwen3.5 uses 256 experts with 8 routed + 1 shared expert per token; 397B total parameters but only 17B active. 256K token native context window. Tokenizer vocabulary: 150K+ tokens (better CJK and technical coverage than Llama's 128K).

**Available models (Qwen3 series, current open-weight):**

| Model | Parameters (active) | Context | License | Released |
|-------|-------------------|---------|---------|---------|
| Qwen3 0.6B / 1.7B / 4B | 0.6B–4B | 128K | Apache 2.0 | Apr 28, 2025 |
| Qwen3 8B Instruct | 8B | 128K | Apache 2.0 | Apr 28, 2025 |
| Qwen3 14B Instruct | 14B | 128K | Apache 2.0 | Apr 28, 2025 |
| Qwen3 32B Instruct | 32B | 128K | Apache 2.0 | Apr 28, 2025 |
| Qwen3 30B-A3B MoE | 3B active / 30B total | 128K | Apache 2.0 | Apr 28, 2025 |
| Qwen3 235B-A22B MoE | 22B active / 235B total | 128K | Apache 2.0 | Apr 28, 2025 |
| Qwen3.5 | 17B active / 397B total | 256K | Apache 2.0 | Feb 16, 2026 |
| Qwen2.5 7B / 14B Instruct | 7B / 14B | 128K | Apache 2.0 | Sep 2024 |

Qwen2.5 7B and 14B remain widely used as fine-tuning bases given their strong benchmark numbers and mature framework support.

**Licensing:** Apache 2.0 for the core open-weight line (Qwen2.5, Qwen3 dense models, Qwen3.5). Proprietary API-only models (Qwen3.5-Omni, Qwen3.6-Plus, Qwen3.7-Max) are not open weight. As a Chinese company's product, compliance review is appropriate for regulated industries or government deployments.

**Suitability for specialist fine-tuning:** Qwen3 14B (Apache 2.0, April 2025) is a strong current recommendation — top-tier technical benchmark performance, hybrid thinking mode useful for troubleshooting scenarios, 128K context, no license gating. Qwen2.5 7B remains the best Apache 2.0 option at the 7B tier if framework stability is the priority. Qwen3.5 (17B active MoE) is compelling if A100 hardware is available and you want the best open-weight base short of frontier-scale models.

---

### DeepSeek — V3.1, V4, and R1 Distillations

**Organization:** DeepSeek (深度求索) — Hangzhou, China. A subsidiary of High-Flyer (幻方科技), a Chinese quantitative hedge fund. Founded 2023. CEO: Liang Wenfeng (also CEO of High-Flyer). Approximately 300 employees as of early 2025. Notable for achieving frontier-quality results with reported training costs dramatically lower than US competitors.

**Release history:**
- **November 2023** — DeepSeek 7B / 67B; initial open-weight release
- **May 2024** — DeepSeek-V2 (21B active / 236B total MoE); Multi-head Latent Attention (MLA) introduced
- **December 26, 2024** — DeepSeek-V3 (37B active / 671B total); MLA + MoE; trained on 14.8T tokens; FP8 mixed precision training; strong benchmark results at reported $5–6M training cost
- **January 20, 2025** — DeepSeek-R1; reasoning model trained via RL (GRPO); competitive with OpenAI o1; R1 distillations into Llama 3.1 8B, Llama 3.3 70B, and Qwen2.5 1.5B–32B released simultaneously; MIT license
- **August 2025** — DeepSeek-V3.1; hybrid model combining V3 general-purpose + R1 reasoning; one model, two modes via chat template; 671B total / 37B active; 128K context
- **December 1, 2025** — DeepSeek-V3.2; performance update; V3.2-Speciale variant with relaxed length constraints achieves gold-medal performance on 2025 IMO and IOI
- **April 24, 2026** — DeepSeek-V4 and V4-Pro; 1M token native context; trained on 32T+ tokens; architectural leap for ultra-long context production use

**Architecture:** DeepSeek's key architectural contribution is Multi-head Latent Attention (MLA) — compresses the key-value cache by projecting K and V through a low-rank latent space, dramatically reducing memory bandwidth requirements for long contexts. DeepSeek MoE uses fine-grained expert partitioning with many small experts rather than fewer large ones, improving expert specialization. V3.1 introduced a unified thinking/non-thinking mode identical in concept to Qwen3's hybrid approach.

**Available models (current):**

| Model | Parameters (active) | Context | License | Released |
|-------|-------------------|---------|---------|---------|
| DeepSeek-R1-Distill-Qwen-7B | 7B | 128K | MIT | Jan 20, 2025 |
| DeepSeek-R1-Distill-Qwen-14B | 14B | 128K | MIT | Jan 20, 2025 |
| DeepSeek-R1-Distill-Llama-8B | 8B | 128K | MIT | Jan 20, 2025 |
| DeepSeek-R1-Distill-Llama-70B | 70B | 128K | MIT | Jan 20, 2025 |
| DeepSeek-V3.1 | 37B active / 671B total | 128K | MIT | Aug 2025 |
| DeepSeek-V3.2 | 37B active / 671B total | 128K | MIT | Dec 1, 2025 |
| DeepSeek-V4 | — / large MoE | 1M | MIT | Apr 24, 2026 |

The full V3.x/V4 models are impractical for consumer fine-tuning (hundreds of GB). The R1 distillation series are the relevant options for specialist fine-tuning.

**Licensing:** MIT license for V3, R1, distillations, V3.1, V3.2, and most of the stack — genuinely permissive. As a Chinese company's product, compliance review is appropriate for regulated or government deployments.

**Suitability for specialist fine-tuning:** The R1 distilled models are the most relevant for network troubleshooting. **DeepSeek-R1-Distill-Qwen-14B** (January 2025, MIT) is the strongest option: reasoning capability distilled from R1 into a 14B body, Apache-permissive MIT license. The chain-of-thought reasoning baked into distilled models suits multi-step diagnostic workflows — the model naturally works through possibilities before committing to an answer. Tradeoff: verbose responses and somewhat slower interaction than a standard instruct model. Worth running as a parallel fine-tune alongside a Llama/Mistral base to compare troubleshooting quality.

---

### Other Notable Models

**Falcon (Technology Innovation Institute, UAE).** TII is a government-funded research organization in Abu Dhabi. Falcon 7B, 40B, and 180B (2023) were strong early open-weight models, notable for the RefinedWeb training dataset. Largely superseded on benchmarks by Qwen3, Llama 4, and Mistral 3 as of 2025–2026. Apache 2.0 license.

**Command R (Cohere).** Cohere — Toronto, founded 2019 by Aidan Gomez, Nick Frosst, Ivan Zhang (all ex-Google Brain). Command R (35B) and Command R+ (104B) open-weight models specialize in retrieval-augmented generation (RAG) with native tool use. Less relevant for fine-tuning a local specialist but notable for production RAG deployments. Non-restrictive research license.

**OLMo 2 (Allen Institute for AI).** AllenAI (Seattle) is a nonprofit founded by Paul Allen in 2014. OLMo 2 7B and 13B (November 2024) are the only major models with fully public training data (Dolma dataset), training code, and intermediate checkpoints. Competitive benchmark performance with Llama 3.1 8B. Apache 2.0. Worth considering for fine-tuning in contexts where full data transparency matters for compliance or auditability.

---

## Selection Guide for Network Engineer Specialist Models

Given the specific requirements — consumer hardware deployment, strong technical reasoning, active fine-tuning framework support, disconnected edge inference — the practical ranking as of **June 2026**:

**First choice (Apple Silicon / Mac Mini): Llama 3.1 8B Instruct**
Mature MLX and Unsloth support on Apple Silicon, well-documented fine-tuning results, 128K context. Llama 4 Scout has higher capability but MoE MLX support is less mature. The gated license is minor friction.

**First choice (A100 cloud GPU): Qwen3 14B or DeepSeek-R1-Distill-Qwen-14B**
Qwen3 14B for best general technical capability with hybrid thinking mode; R1-Distill-Qwen-14B if troubleshooting quality and step-by-step reasoning are the priority. Both Apache 2.0 / MIT, no gating.

**Best Apache 2.0 at 7B–8B tier: Ministral 8B (December 2025)**
Strongest Apache 2.0 small model at time of writing; no license friction; AIME benchmark results suggest strong reasoning.

**Best reasoning quality at 14B: Phi-4-reasoning (May 2025, MIT)**
RL-trained reasoning that outperforms DeepSeek-R1-Distill-Llama-70B on several benchmarks. MIT license. 32K context. Strong choice for troubleshooting-heavy workloads.

**Best quality if hardware allows 30B+: Gemma 4 31B Dense (April 2026, Apache 2.0)**
Apache 2.0, no gating, 256K context, #3 on Arena AI leaderboard. Fits A100 40GB with QLoRA via Unsloth (16 GB VRAM reported). The first Gemma generation with a genuinely open license.

**For chain-of-thought troubleshooting on constrained hardware: Phi-4-mini-reasoning (3.8B, May 2025)**
Under 3 GB RAM in Q4 quantization. Lower quality than 14B but runs on any Mac and provides structured reasoning output.

## Sources

- [Meta Llama 4 blog post (April 5, 2025)](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)
- [Llama 4 on HuggingFace](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E)
- [Mistral AI News](https://mistral.ai/news/)
- [Mistral Models Overview](https://docs.mistral.ai/models/overview)
- [Gemma releases (Google)](https://ai.google.dev/gemma/docs/releases)
- [Gemma 4 (Google DeepMind)](https://deepmind.google/models/gemma/)
- [Phi-4-reasoning Technical Report (Microsoft Research, May 2025)](https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-technical-report/)
- [Phi Open Models (Microsoft Azure)](https://azure.microsoft.com/en-us/products/phi/)
- [Qwen3 GitHub](https://github.com/QwenLM/qwen3)
- [DeepSeek-V3.2 Release Notes](https://api-docs.deepseek.com/news/news251201)
- [Open LLM Leaderboard (HuggingFace)](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
