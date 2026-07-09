---
title: "Local AI Tools"
date: 2026-07-09
lastmod: 2026-07-09
draft: false
description: "Open-source and independently developed applications for running AI models entirely on local hardware — voice, text, and multimodal tools that compete with cloud-hosted equivalents."
research_area: "local-ai-tools"
last_reviewed: 2026-07-09
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.8
  disable: false
---

{{<steering>}}

## Local AI Tools Section — Steering Instructions

**Scope:** End-user and developer-facing applications that run AI inference entirely on local hardware, as an alternative to cloud-hosted equivalents (ElevenLabs, OpenAI, etc.). In scope: local model-serving apps and studios (voice cloning/TTS/STT, image generation, chat UIs), inference runtimes and servers (Ollama, LM Studio, llama.cpp, vLLM), and the MCP/agent-integration layer that lets local models plug into AI coding agents. Out of scope: the fine-tuning/training process itself (see [Local LLM Fine-Tuning]({{< relref "../local-llm-finetuning/_index.md" >}})), and datacenter-scale inference infrastructure (see [AI Accelerators]({{< relref "../ai-accelerators/_index.md" >}}) and [Datacenters]({{< relref "../datacenters/_index.md" >}})).

**Editorial focus:** This is a fast-moving, largely open-source and indie-developer space rather than a traditional company landscape. Prioritize documenting the tool itself — architecture, supported models, licensing, and genuine capability — over marketing copy. Many entries will be solo or small-team open-source projects rather than funded companies; do not force a company profile where none exists. Note funding, monetization model (open-core, optional cloud tier, donations, tokens), and licensing explicitly, since these affect long-term viability and trust.

**Claim verification for this section:** Performance claims (tokens/sec, "realtime" multiples, download/user counts) should be checked against the project's own site or release notes at minimum; flag as unverified where no independent benchmark exists. Distinguish "fully local" claims from features that silently call out to a cloud API — verify from documentation, not marketing language.

**Entry types:**
- **Local application / studio** — a complete end-user app (e.g., Voicebox) that wraps one or more local models with a UI
- **Inference runtime** — a server or library that serves models locally (Ollama, llama.cpp, vLLM)
- **Company** — where a tool has a company behind it, use the standard company entry template

**Tags:** `voice-ai`, `tts`, `stt`, `local-inference`, `mcp`, `open-source`, `inference-runtime`, `model-serving`

**Review cadence:** 90 days — this space ships new releases and competing tools quickly.

{{</steering>}}

## Overview

This section tracks local-first AI applications and tooling: software that runs models entirely on the user's own hardware rather than calling a cloud API. The current focus is local voice AI (TTS/STT/voice cloning), with room to expand into local chat/LLM front-ends, image generation studios, and the inference runtimes underneath them (Ollama, llama.cpp, LM Studio) as entries are added.

## Entries

- [Voicebox]({{< relref "voicebox.md" >}}) — open-source local voice AI studio: 7-engine TTS voice cloning, Whisper-based dictation, and an MCP server that gives AI coding agents a spoken voice
