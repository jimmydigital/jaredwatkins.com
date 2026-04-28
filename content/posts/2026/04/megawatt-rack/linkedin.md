---
title: "LinkedIn: What it actually takes to run a megawatt rack"
date: 2026-04-27
draft: true
description: "LinkedIn summary of the megawatt rack post — not for publishing to the blog."
tags: ["linkedin"]
categories: ["Computing and Tech"]
---

I've designed some enterprise server racks in the 10 to 15 kW range. The GPU racks going into AI data centers right now are a different animal entirely. And the ones coming next are barely recognizable as the same product.

If you like this subject check out the long-form deep dive on my site: https://www.jaredwatkins.com/posts/2026/04/megawatt-rack/

**10–15 kW (enterprise baseline):** Air cooled. Standard single or three-phase AC. 90% of installed rack capacity in the world. Facilities designed for this have been refined over 30 years and nothing about it is surprising.

**80–100 kW (what's being deployed now):** Still air-cooled, but you're fighting physics. Overhead busway instead of individual circuits. Rear-door heat exchangers capturing up to 70% of the heat load in liquid before it hits the room. Floor loads up to 3 tons per coolant unit. New-build infrastructure runs $200K to $300K per rack in facility-side capital before you touch the compute. Demanding but solvable. The design patterns are well understood.

What's less discussed at this tier: the supply chain is tighter than most people realize. The transformers, UPS semiconductors, and copper required for a 100 kW GPU hall compete directly with utility-scale solar farms for the same components. Large power transformers now take up to three years to procure in some cases. Hyperscalers have been documented outbidding the power grid for allocations. It's circular: AI drives power demand that requires renewable buildout, and both compete for the same copper, transformers, and power electronics.

**1+ MW (what's coming):** NVIDIA's GB200 NVL72 packs 72 Blackwell GPUs into one rack and draws over a megawatt. Same floor footprint as above. Air cooling is physically impossible at this density — direct liquid cooling with cold plates on every chip is the only path. Running one of these racks costs roughly $683,000/year in power alone at current rates (ha!), including cooling overhead. Per rack. Before hardware costs.

The 1 MW supply chain has its own version of the same problem: the silicon carbide power semiconductors required for 800V DC distribution are the same devices going into 800V EV traction inverters. Wolfspeed, one of the most important SiC suppliers, filed for bankruptcy restructuring earlier this year after over-betting on EV demand that slowed right as datacenter demand for the same parts accelerated. The components for a megawatt rack come from automotive tier-1 suppliers and SiC wafer fabs, not just datacenter infrastructure vendors.