---
title: "Future Value of GPU Compute - LinkedIn"
date: 2026-06-01
draft: true
description: "LinkedIn summary for Future Value of GPU Compute post"
tags: ["AI", "GPUs", "datacenter", "economics"]
categories: ["Computing and Tech"]
---

What's new AI infrastructure hardware worth in year four?

I spent some time working through the full picture. Datacenter build costs have nearly tripled per megawatt since 2023, and that's before the chip. Deploying a B300 GPU slot costs roughly 3.5x more in facility capital than an H100 slot did two years ago, even though the H100 already required liquid cooling and purpose-built power infrastructure. Each generation locks operators into infrastructure that only makes economic sense if the next generation ships on schedule and commands premium rates long enough to amortize it. That's a ratchet.

On the revenue side: H100 rental rates are down 70 to 80% from peak. The A100 traced the same arc before it. The realistic economic peak for hardware deployed today is 2 to 3 years, not the 6-year depreciation schedules Meta, Microsoft, and Google are booking. Amazon went the other direction and shortened their useful life estimate, citing the pace of AI development. One of these approaches reflects reality.

The financial engineering layer is worth its own read. Sale-leasebacks, GPU-backed securitization, SPVs partly funded by the manufacturer selling into them. The risk in these deals doesn't disappear, it moves down the chain until it lands with whoever has the least visibility into GPU economics. There's a reason one auditor described signing off on these transactions as an "Arthur Andersen moment".

There's also a secondary market exit most operators haven't fully priced in yet, and a density wall that makes the long-term trajectory of facility costs dangerous waters.

Full breakdown with data and the financial mechanics:
https://www.jaredwatkins.com/posts/2026/06/future-value-gpu-compute/
