---
title: "How LLMs Are Trained: Pretraining"
date: 2026-06-10
lastmod: 2026-06-10
draft: false
description: "The pretraining process that produces a base language model: data scale, tokenization, next-token prediction, transformer architecture, and what the model actually learns."
tags: ["llm", "pretraining", "transformers", "tokenization", "machine-learning"]
categories: ["technology"]
research_area: "local-llm-finetuning/fundamentals"
source_urls:
  - "https://arxiv.org/abs/1706.03762"
  - "https://arxiv.org/abs/2005.14165"
  - "https://arxiv.org/abs/2302.13971"
  - "https://huggingface.co/docs/transformers/main/en/model_doc/llama"
last_reviewed: 2026-06-10
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

A large language model begins as a transformer neural network trained on trillions of tokens of text via a self-supervised objective: predict the next token in a sequence. This process, called pretraining, is what gives base models their broad knowledge of language, facts, and reasoning patterns — before any fine-tuning or instruction-following behavior is applied.

## Key Facts

- **Objective:** Next-token prediction (autoregressive language modeling)
- **Architecture:** Transformer (attention-based; "Attention Is All You Need," Vaswani et al. 2017)
- **Typical data scale:** 1–15 trillion tokens (Llama 3.1 used ~15T tokens)
- **Typical compute scale:** Thousands of GPUs for weeks to months
- **Output:** A base model — a general-purpose text completion engine, not yet an assistant

## What It Is / How It Works

**The transformer architecture.** Every modern open-source LLM is a transformer: a deep neural network built from stacked layers of multi-head self-attention and feed-forward subnetworks. Attention allows each token in a sequence to "look at" every other token when computing its representation, capturing long-range dependencies that prior architectures (RNNs, LSTMs) struggled with. The parameters of these layers — the weight matrices — are what gets learned during training and what fine-tuning later modifies.

**Tokenization.** Raw text is never fed directly into the model. It is first tokenized: split into sub-word units called tokens using an algorithm like Byte-Pair Encoding (BPE) or SentencePiece. A typical vocabulary is 32,000–128,000 tokens. Each token maps to an integer ID, and those IDs are converted to dense vector embeddings (learned representations) before entering the transformer. The way technical content tokenizes matters for fine-tuning: Cisco IOS commands like `show ip bgp summary` tokenize into a predictable set of tokens that the model learns to associate with specific contexts.

**The pretraining objective.** Given a sequence of tokens `[t1, t2, t3, ..., tn]`, the model is trained to predict `t_n+1`. The loss function (cross-entropy) measures how wrong the prediction was; gradients flow backward through the network via backpropagation, and the optimizer (AdamW) nudges each weight slightly in the direction that reduces loss. Repeat this over trillions of examples and the model's weights encode a compressed statistical model of language and the world described in that text.

**What a base model learns.** By the end of pretraining, a base model has learned: grammar and syntax across many languages; factual associations (capitals, dates, technical relationships); code patterns and formal languages; reasoning patterns present in training text; and the statistical texture of many domains — including networking, programming, and technical documentation. It has not learned to be helpful or to follow instructions. A base model will complete a prompt literally: given `show ip route`, it will continue generating plausible IOS output or documentation, not explain what to do.

**Scale and the emergent capability curve.** Capability does not scale linearly with model size or compute. Smaller models below certain parameter thresholds lack the capacity to reliably perform multi-step reasoning. The Chinchilla scaling laws (Hoffmann et al. 2022) provided the first systematic analysis of the compute-optimal ratio of model parameters to training tokens: roughly 20 tokens per parameter. Models trained on too little data for their size are "undertrained" — the weights have capacity that was never filled. This matters when selecting a base model for fine-tuning: a well-trained 7B model often outperforms a poorly-trained 13B on domain-specific tasks.

**Instruction tuning and RLHF.** A base model becomes an assistant through a second training stage: supervised fine-tuning (SFT) on instruction-following examples, optionally followed by reinforcement learning from human feedback (RLHF) or direct preference optimization (DPO). Open-source base models like Llama 3.1 8B Base are the raw pretrained weights before this stage. Instruction-tuned variants (Llama 3.1 8B Instruct) have already been through SFT and alignment. When building a specialist model, you typically start from an Instruct variant and apply further fine-tuning to add domain knowledge — you're building on top of existing instruction-following behavior, not rebuilding it from scratch.

## Notable Developments

- **2025:** Llama 3.1 (Meta) — 8B/70B/405B models trained on 15.6T tokens; multilingual; 128K context; released under a permissive license enabling fine-tuning
- **2024:** Mistral 7B v0.3 and Mixtral 8x7B — strong base models at the 7B scale; sliding window attention; Apache 2.0 license
- **2024:** Gemma 2 (Google DeepMind) — 2B/9B/27B models; strong performance per parameter; permissive license
- **2023:** Llama 2 (Meta) — first widely-adopted open-weight model at 7B/13B/70B scales
- **2022:** Chinchilla (DeepMind) — scaling law paper showing most models were undertrained relative to compute budget
- **2017:** "Attention Is All You Need" (Vaswani et al.) — transformer architecture paper that all modern LLMs are based on

## Sources

- [Attention Is All You Need (Vaswani et al. 2017)](https://arxiv.org/abs/1706.03762) — original transformer paper
- [GPT-3: Language Models are Few-Shot Learners (Brown et al. 2020)](https://arxiv.org/abs/2005.14165) — established scale = capability
- [LLaMA (Touvron et al. 2023)](https://arxiv.org/abs/2302.13971) — open-weight models competitive with proprietary at reasonable scale
- [Chinchilla Scaling Laws (Hoffmann et al. 2022)](https://arxiv.org/abs/2203.15556) — optimal compute allocation for pretraining
