---
title: "Compute Options for Fine-Tuning"
date: 2026-06-10
lastmod: 2026-06-10
draft: false
description: "Apple Silicon (Mac Mini / MacBook) vs. rented cloud GPU instances for LLM fine-tuning: hardware capabilities, time estimates, cost, and practical setup for each path."
tags: ["compute", "apple-silicon", "gpu", "cloud-gpu", "fine-tuning", "mac-mini", "runpod", "lambda-labs"]
categories: ["overview"]
research_area: "local-llm-finetuning/compute-options"
last_reviewed: 2026-06-10
stale_after_days: 90
sitemap:
  changefreq: "monthly"
  priority: 0.8
  disable: false
---

## Overview

Two practical paths for fine-tuning a 7B–13B specialist LLM without building a GPU server: Apple Silicon Macs (Mac Mini or MacBook Pro with 32–128 GB unified memory) and rented GPU cloud instances (RunPod, Lambda Labs, Vast.ai). This section covers both paths with realistic time and cost estimates.

## Entries

- [Apple Silicon Fine-Tuning]({{< relref "apple-silicon.md" >}}) — Mac Mini M4 Pro/Max and MacBook Pro: MLX, Unsloth, capabilities, and realistic throughput
- [Cloud GPU Fine-Tuning]({{< relref "cloud-gpu.md" >}}) — RunPod, Lambda Labs, Vast.ai: instance types, costs per hour, and time-to-completion estimates
