---
title: "Network Engineer Specialist Models"
date: 2026-06-10
lastmod: 2026-06-10
draft: false
description: "End-to-end design for Juniper and Cisco specialist network engineer models: base model selection, training data requirements, fine-tuning parameters, edge deployment, and integration with attached network devices."
tags: ["specialist-models", "network-engineering", "juniper", "cisco", "edge-deployment", "llm", "junos", "ios"]
categories: ["overview"]
research_area: "local-llm-finetuning/specialist-models"
last_reviewed: 2026-06-10
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.8
  disable: false
---

## Overview

The network engineer specialist models are the end application of the fine-tuning pipeline — a Juniper expert and a Cisco expert, each deployed disconnected on a Mac laptop and given direct access to connected network devices.

## Entries

- [Juniper Expert Model]({{< relref "juniper-expert.md" >}}) — JunOS-specific design, training data specification, and deployment
- [Cisco Expert Model]({{< relref "cisco-expert.md" >}}) — IOS/IOS-XE/NX-OS/ASA design, multi-platform coverage, and deployment
- [Edge Deployment and Device Integration]({{< relref "edge-deployment.md" >}}) — Running disconnected on a MacBook, connecting to network devices, and building an agentic command loop
- [Context Window Management]({{< relref "context-window-management.md" >}}) — Handling long show command output, sliding-window conversation trimming, two-pass summarization, and performance impact of context length on Apple Silicon
- [LoRA Adapter Versioning and Rollback]({{< relref "adapter-versioning.md" >}}) — Directory layout for base/adapter separation, training run metadata, registering multiple versions in Ollama, rollback procedure, and what to keep vs. delete
