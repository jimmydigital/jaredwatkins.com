---
title: "LinkedIn: Building an SMB inference stack"
date: 2026-05-23
draft: true
description: "LinkedIn summary of the local AI inference stack post."
tags:
  - ai
  - llm
  - local-inference
categories:
  - Computing and Tech
---

Your AI token bill is about to come under ROI scrutiny.

A 10-person team doing active AI use across docs, summarization, and code review burns through around 100 million output tokens a month. Using GPT-4o that's $1,000/month. Sonnet 4.6 is about $1,500/month and with Opus 4.7 it climbs to $2,500/month. That might not be ruinous today, but it scales with adoption, and Anthropic just shifted enterprise billing to usage-based consumption on top of seat fees, so those numbers are getting more visible.

The math changes when you own the hardware. I put together a breakdown of three tiers: Mac Studio M4 Ultra at around $15K for small teams, four L40S cards in a Supermicro at $60K to $80K for 20 to 50 concurrent users, and H100 SXM nodes at $500K+ for multi-tenant MSP work. The H100 tier is where most write-ups lowball the costs: total system draw per 8-GPU node is 10.2 kW.  Colo hosting for a fully loaded rack runs $68K to $119K per year in power alone before you count cross-connects and remote hands.

The sweet spot for most businesses is the $60K to $80K four-L40S config. It fits in a standard half-rack without any high-density facility negotiation, serves a 20 to 50-person team or a handful of MSP clients, and pays back in under six months at serious API volumes. That's the tier where the economics work without the operational complexity of multi-node distributed inference.

The piece most first-time builders skip is the gateway layer. LiteLLM in front of your inference server handles auth, rate limiting, model routing, and cloud fallback. 

Full post covers hardware comparisons, inference engine tradeoffs, routing strategies, power math, and model selection by task type: [jaredwatkins.com](https://jaredwatkins.com/posts/2026/05/smb-inference-stack/)
