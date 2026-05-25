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

Frontier API costs are fine when you're experimenting. They get painful once you're running a real workload. A 10-person team doing active AI use  (writing docs, summarization, code reviews, etc) will generate somewhere around 100 million output tokens a month. At Claude Sonnet's $15 per million output tokens, that's $1,500/month. At GPT-4o it's $1,000/month. Not ruinous, but it's a recurring bill that scales directly with adoption, and adoption tends to grow.

The math changes when you own the hardware. A $15K server starts paying for itself in months at meaningful API volumes. You also get things you can't buy from a cloud API: no data egress, no retention concerns, the ability to fine-tune on your own data.

I put together a breakdown of three hardware tiers: Mac Studio at $15K for small teams, four L40S cards in a Supermicro at around $60K for 20 to 50 concurrent users, two 4x H100 nodes at $250K for multi-tenant MSP work. I also talk about the software stack, query routing, and the economics at each scale.

The piece most first-time builders skip is the gateway layer. LiteLLM in front of your inference server handles auth, rate limiting, routing between models, and fallback to cloud when local is overwhelmed. Better to have this in place from the start. 

The hard part isn't the hardware. It's the operational layer: monitoring, model updates without dropping requests, building enough around LiteLLM to actually invoice clients. Budget that engineering time before assuming the hardware cost is the whole story.

Full post with hardware comparison tables, inference engine tradeoffs, routing strategies, and model selection by task type: [jaredwatkins.com](https://jaredwatkins.com/posts/2026/05/smb-inference-stack/)
