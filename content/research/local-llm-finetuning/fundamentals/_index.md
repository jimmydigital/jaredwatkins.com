---
title: "LLM Fundamentals & Fine-Tuning Methods"
date: 2026-06-10
lastmod: 2026-06-10
draft: false
description: "How large language models are trained from scratch, what fine-tuning modifies at a parameter level, and the efficient methods (LoRA, QLoRA) that make specialist fine-tuning practical on consumer hardware."
research_area: "local-llm-finetuning/fundamentals"
last_reviewed: 2026-06-10
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.8
  disable: false
---

## Overview

How language models learn, and what fine-tuning does to that knowledge.

## Entries

- [How LLMs Are Trained]({{< relref "llm-pretraining.md" >}}) — Pretraining, tokenization, next-token prediction, and what a base model knows
- [Fine-Tuning Mechanics]({{< relref "finetuning-mechanics.md" >}}) — What fine-tuning changes, instruction tuning vs. domain adaptation, catastrophic forgetting
- [LoRA and QLoRA]({{< relref "lora-qlora.md" >}}) — Low-rank adaptation for dense and MoE models: how they work, why MoE fine-tuning is harder, target module configs per model family, memory requirements
- [Base Models for Fine-Tuning]({{< relref "base-models.md" >}}) — Survey of Llama, Mistral, Gemma, Phi, Qwen, and DeepSeek: who makes them, architecture, licensing, and suitability for specialist fine-tuning
- [RAG vs. Fine-Tuning]({{< relref "rag-vs-finetuning.md" >}}) — When to use retrieval-augmented generation vs. fine-tuning, how they compose, and the practical architecture for a network engineer specialist model
- [Config Generation vs. Troubleshooting]({{< relref "config-generation-vs-troubleshooting.md" >}}) — Why these are two different tasks with different training data, interaction patterns, and quality criteria — and the case for separate LoRA adapters
- [Model Internals: Weights, MoE, and Inference]({{< relref "model-internals.md" >}}) — What a model file actually contains, how transformer layers work beyond "a matrix of weights", how MoE routing works, GGUF quantization formats, and a full trace of a query through the inference stack
- [Temperature and Sampling]({{< relref "temperature-and-sampling.md" >}}) — What temperature actually is (logit scaling before softmax), how it reshapes probability distributions, top-p and top-k sampling, and why the right setting depends on the task
- [Evaluating a Fine-Tuned Model]({{< relref "evaluation-and-testing.md" >}}) — Building a domain-specific eval set, exact-match and semantic scoring for CLI output, regression testing for general capability, and what "good enough" looks like before deployment
- [System Prompt Engineering]({{< relref "system-prompt-engineering.md" >}}) — Writing the system prompt for a specialist model, the mandatory training-inference consistency requirement, few-shot examples in the system prompt, and testing before generating training data
