---
title: Picking hardware for local AI inference in 2026
date: 2026-04-07
draft: false
description: A practical guide to choosing local AI hardware -- what actually matters, what fits where, and why hardware vendors keep getting away with marketing nonsense.
tags:
  - ai
  - hardware
  - llm
  - local-inference
  - nvidia
  - apple
  - amd
  - tenstorrent
categories:
  - Computing and Tech
---

Nobody buying AI hardware in 2026 is short on opinions. Everyone has a take. The forums are full of people who swear by their setup and can't understand why anyone would choose differently. Most of those arguments are happening across completely different use cases which raises the noise floor for this subject.

<!--more-->

"What's the best hardware for running AI locally?" is roughly as useful as asking what's the best vehicle without mentioning whether you're hauling gravel or commuting to an office. The answer depends entirely on what you're trying to do, and getting that wrong wastes real money.

Here's my attempt to cut through it.

## The three things that actually matter

Local AI hardware comes down to three variables: capacity, bandwidth, and software stack.

**Capacity** is whether the model fits in memory at all. If it doesn't fit, nothing else matters. You're either offloading to disk (more on that disaster in a bit) or you need a bigger box.

**Bandwidth** is how fast the hardware can feed data to the compute units. This is the single best first-pass predictor of how fast tokens actually come out. Memory bandwidth is not the same as tokens per second, but it's the cleanest way to sort real performance tiers before you waste a weekend arguing with someone posting single-prompt screenshots.

**Software stack** is how much of the spec sheet you can actually cash out. A card with strong bandwidth numbers on paper does nothing useful if the inference framework doesn't support it. This is still where CUDA's dominance matters, and it's where Tenstorrent's fully open source stack is a genuine long-term bet worth watching.

## The hardware landscape

Five distinct markets, same buzzword. Here's what each one is actually good for.

### Raw speed when the model fits: discrete GPUs

If the model fits in VRAM, discrete GPUs are still the fastest thing by a wide margin. Nothing else comes close on a per-token basis.

NVIDIA's RTX PRO 6000 Blackwell (96GB, 1792 GB/s, around $8,000 to $9,200 retail right now) and the RTX 5090 (32GB, 1792 GB/s, street price has been running $3,000 to $5,000 and climbing due to supply issues) share identical bandwidth. The difference is capacity. The PRO 6000 can hold a 70B model at Q4 comfortably; the 5090 tops out around 30B quantized. The RTX 4090 (24GB, 1008 GB/s) is still worth knowing about if you find one at a good price on the secondary market.

AMD's discrete cards deserve more credit than they typically get. The RX 7900 XTX (24GB, 960 GB/s) is genuinely competitive on bandwidth per dollar. The Radeon PRO W7900 (48GB, 864 GB/s) doubles the memory at workstation pricing. The newer AI PRO R9700 (32GB, 640 GB/s) sits in between. ROCm support has improved enough that AMD is a real option now, especially with llama.cpp and Ollama.

Intel showed up too. The Arc Pro B65 (32GB, ~608 GB/s) and B60 (24GB, ~456 GB/s) are interesting if you're following where Intel's headed with this. Not my first choice today, but they're not irrelevant.

Discrete GPUs win because they can drink from a firehose. They lose the moment the model doesn't fit.

### Biggest one-box memory: Apple Silicon

Apple's pitch is "not the fastest, but usable"  combined with "more unified memory in a quiet box than anything else you can buy."

The Mac Studio M3 Ultra is still the headliner here. Up to 512GB of unified memory at 819 GB/s. That's enough to run a Llama 4 Maverick (400B MoE) at quantization, or DeepSeek-V3 (671B MoE) with aggressive quantization. Nothing else in a single consumer box gets anywhere near that capacity. The 512GB config is reportedly hard to find right now. Apple briefly pulled that upgrade option but the 96GB base config starts around $3,999 and the 192GB/256GB configs sit in the $6,000 to $10,000 range depending on CPU tier.

Below that you've got the Mac Studio M4 Max (up to 128GB, 546 GB/s, from around $2,000), MacBook Pro M5 Max (up to 128GB, 460 to 614 GB/s, from around $3,900), MacBook Pro M5 Pro (up to 64GB, 307 GB/s, from around $2,200), and Mac mini M4 Pro (up to 64GB, 273 GB/s, from around $1,400).

Apple wins when you want one box, you want silence, and you want to run models that simply won't fit on a normal GPU. It loses when raw tokens per second and concurrency start to matter more than everything else.

### Coherent NVIDIA appliance: DGX Spark

The DGX Spark (128GB unified, 273 GB/s) launched at $3,999 and has since been bumped to $4,699 due to memory supply constraints. It's not a bandwidth monster. What it is, is a compact NVIDIA CUDA appliance with 128GB of coherent memory and NVFP4 support that hasn't fully matured yet but is genuinely interesting for the future of quantization.

This is a developer appliance first. It's for people who need the full NVIDIA stack, want 128GB in a small box, and aren't optimizing for raw decode speed. The GB10-class machines like the ASUS Ascent GX10 live in the same category.

### First real x86 unified-memory contender: Strix Halo

AMD's Ryzen AI Max / Strix Halo is the most interesting new category in local AI hardware, in my opinion. Up to 128GB of LPDDR5X at ~256 GB/s, with up to ~96GB assignable as GPU memory on Windows. The Framework Desktop implements this starting at $1,099 for 32GB, $1,599 for 64GB, and $1,999 for the 128GB config.

This is not just another mini PC. It's the first mainstream x86 box where local AI starts feeling like a serious hardware class rather than a laptop pretending very hard. The value proposition at 128GB for $1,999 is hard to beat, especially if you're running MoE models where capacity matters more than raw bandwidth.

### The fully open source bet: Tenstorrent

Tenstorrent's Wormhole n300 (24GB, 576 GB/s, around $1,400) and Blackhole p150 (32GB, 512 GB/s, around $1,400 with 800G interconnect) run a fully open source stack from top to bottom. I'm genuinely rooting for this one to mature. The AI world needs more fully open stacks, and the bandwidth is competitive with mid-tier discrete GPUs. The Blackhole's interconnect makes multi-card scaling worth watching as the software ecosystem develops.

### The AI PC trap

Most machines wearing an "AI PC" sticker are still bandwidth-starved in any practical sense. Snapdragon X Elite (~135 GB/s), Intel Lunar Lake (~136 GB/s), MacBook Air M5 (~153 GB/s), Snapdragon X2 Elite (~152 to 228 GB/s depending on SKU). These are fine machines. They're fine for small models, personal assistants, edge workloads. They are not serious local inference hardware for anything larger than a 7 to 8B dense model. Physics still applies, which is inconvenient but consistent.

## The gimmicks section (or: technically possible doesn't mean useful)

A pattern keeps coming up in local AI discussions that I want to name directly, because it costs people a lot of time and money chasing a thing that doesn't actually work well in practice.

The pitch goes like this: "My hardware doesn't have enough memory, but I can still run a big model by only loading part of it at a time." This is usually presented as a clever hack. Sometimes it is. More often it's a performance cliff dressed up as a feature.

**Layer offloading.** Tools like llama.cpp let you split model layers between GPU VRAM, system RAM, and even disk. The flag is `-ngl` (number of GPU layers). When you don't have enough VRAM for the whole model, you offload some layers to CPU RAM. The problem is that every token generation step has to shuffle data across the PCIe bus between GPU and CPU. Real-world numbers here are brutal -- people running 70B models with partial CPU offloading report around 1--3 tokens per second. That's technically running the model. It's also roughly the speed of reading text out loud to yourself. Not useful for interactive work.

**Disk offloading.** Some tools and frameworks support streaming model weights from NVMe directly. Modern NVMe drives can hit 7 GB/s reads in ideal conditions, which sounds fast until you realize your GPU memory bandwidth is 10 to 100x that. The energy penalty alone is significant -- recent research puts SSD-offloaded decode at roughly 3 to 4x the energy cost versus in-memory inference on comparable hardware. Token generation with disk offload in practice tends to land below 1 token per second. I've seen people run 405B models this way. I've also seen them wait two minutes for a 60-token response.

**Extreme quantization.** Quantization is genuinely useful and I'm not criticizing it wholesale.  Q4 is excellent, Q5 and Q8 are great when you can afford the memory for them. The cliff is at the bottom. Q2 quantization degrades quality enough that for many use cases you'd be better off running a smaller, better-quantized model. A Q2 70B model often loses to a Q4 7B on reasoning tasks while using four times the memory. The tradeoff is real.

**The 30 tokens-per-second floor.** For interactive use actual back-and-forth conversation or coding assistance where you're watching the output stream 30 tok/s is roughly where it starts feeling like a tool rather than a waiting exercise. Below 15 tok/s it becomes noticeable. Below 5 tok/s it's painful regardless of model quality. For batch processing or background tasks, slower is tolerable. But if you're evaluating a hardware setup for daily driving, "it runs" and "it's usable" are different things.

The test I'd apply: if your setup produces tokens slower than you read them, you're probably past the gimmick threshold for interactive use.

## What models are you actually trying to run?

Hardware decisions only make sense relative to the models you're targeting. The good news is that open source models in 2026 have gotten genuinely good close enough to frontier API models on many tasks that the conversation has shifted from "is open source good enough?" to "which open source model is right for this?"

The big architectural shift is MoE (Mixture of Experts). These models have enormous total parameter counts but only activate a fraction of them per token. That changes the capacity-vs-speed tradeoff dramatically. A model that "needs" 192GB to load might only activate 17B parameters per forward pass.

**24 to 32GB (RTX 5090, RX 7900 XTX, Arc Pro B65, MacBook Air M5 max):** This is Llama 4 Scout territory at Q4 (109B total, 17B active -- fits in roughly 55 to 60GB quantized, so you need a second GPU or larger box), or more realistically: Qwen3 30B-A3B (only 3B active per token), Gemma 4 26B MoE (~14GB at Q4, 85+ tok/s on consumer hardware, genuinely excellent for the size), Phi-4 14B for reasoning, and Qwen2.5-Coder 14B for coding work. Useful territory, not the frontier.

**48 to 64GB (Mac Studio M4 Max, MacBook Pro M5 Pro, Framework Desktop 64GB):** Dense 30 to 40B models at Q4 land comfortably here. Llama 4 Scout (109B MoE, 17B active) fits at reasonable quantization. Qwen3 235B-A22B MoE needs more room, but the smaller Qwen3 variants are excellent here. This is where local AI starts feeling like a real tool rather than an experiment.

**96 to 128GB (RTX PRO 6000, Mac Studio M3 Ultra base, DGX Spark, Framework Desktop 128GB):** Llama 4 Scout at Q8, DeepSeek-R1 70B for serious reasoning, Qwen3 235B-A22B MoE with 22B active parameters. The DGX Spark's CUDA stack gives it an edge for frameworks that are optimized for NVIDIA. GPT-OSS-120B (OpenAI's first open-weights release in years) also fits here. Single 80GB GPU in FP8, or 128GB unified at Q4.

**192 to 512GB (Mac Studio M3 Ultra maxed, multi-GPU rigs):** Llama 4 Maverick (400B MoE, 17B active), DeepSeek-V3 (671B MoE) at aggressive quantization, Qwen3 235B at higher precision. If you need frontier-class open source models running locally with zero cloud dependency, this is currently the only consumer-ish path to get there.

## The quadrant chart

Here's how these platforms map when you combine memory capacity, bandwidth, and cost into a single picture. The vertical axis is a synthesized "memory performance" score explained in detail in the collapsed section below. The horizontal axis is platform cost. Only min and max configs are shown for platforms with multiple options.

```mermaid
quadrantChart
    title Local AI Hardware - Memory Performance vs Cost 2026
    x-axis Low Cost --> High Cost
    y-axis Low Performance --> High Performance
    quadrant-1 High Perf High Cost
    quadrant-2 High Perf Low Cost
    quadrant-3 Low Perf Low Cost
    quadrant-4 Low Perf High Cost
    RTX PRO 6000: [0.98, 0.75]
    Mac Ultra 192GB: [0.94, 0.7]
    RTX 5090: [0.45, 0.52]
    MBP M5 Max 128GB: [0.61, 0.43]
    Mac Ultra 96GB: [0.42, 0.42]
    DGX Spark: [0.51, 0.35]
    Radeon PRO W7900: [0.37, 0.29]
    Framework 128GB: [0.16, 0.34]
    RTX 4090: [0.23, 0.26]
    RX 7900 XTX: [0.04, 0.38]
    Framework 64GB: [0.13, 0.32]
    TT Wormhole: [0.09, 0.25]
    TT Blackhole: [0.15, 0.19]
    Arc Pro B65: [0.03, 0.13]
    Mac mini M4 Pro: [0.1, 0.08]
    MacBook Air M5: [0.06, 0.05]
```

<details>
<summary>How the memory performance score is calculated + data table</summary>

The score on the vertical axis synthesizes two things: memory capacity (GB) and memory bandwidth (GB/s). Neither alone tells the full story,  A box with massive bandwidth but tiny capacity runs out of useful models quickly, and a box with massive capacity but slow bandwidth produces tokens at a crawl.

**Scoring method:**

I normalized both dimensions independently across the full set of platforms (0 = worst in set, 1 = best in set), then combined them with equal weighting (50/50). The formula is:

```
capacity_score = (GB - min_GB) / (max_GB - min_GB)
bandwidth_score = (GB_s - min_GB_s) / (max_GB_s - min_GB_s)
memory_performance = (capacity_score + bandwidth_score) / 2
```

The dataset spans 24GB (low end) to 192GB (practical max shown) for capacity, and 153 GB/s (MacBook Air M5) to 1792 GB/s (RTX 5090 / PRO 6000) for bandwidth.

**Cost axis:** Normalized from ~$750 (Arc Pro B65) to ~$8,500 (RTX PRO 6000). I used street price midpoints where ranges exist.

| Platform | Memory (GB) | Bandwidth (GB/s) | Cap Score | BW Score | Mem Score | Cost ($) | Cost Score |
|---|---|---|---|---|---|---|---|
| RTX PRO 6000 | 96 | 1792 | 0.43 | 1.00 | 0.71 | 8,500 | 1.00 |
| Mac Studio M3 Ultra 192GB | 192 | 819 | 1.00 | 0.41 | 0.70 | 8,000 | 0.94 |
| RTX 5090 | 32 | 1792 | 0.05 | 1.00 | 0.52 | 4,200 | 0.45 |
| MacBook Pro M5 Max 128GB | 128 | 546 | 0.62 | 0.24 | 0.43 | 5,500 | 0.61 |
| Mac Studio M3 Ultra 96GB | 96 | 819 | 0.43 | 0.41 | 0.42 | 3,999 | 0.42 |
| DGX Spark | 128 | 273 | 0.62 | 0.07 | 0.35 | 4,699 | 0.51 |
| Framework 128GB | 128 | 256 | 0.62 | 0.06 | 0.34 | 1,999 | 0.16 |
| Radeon PRO W7900 | 48 | 864 | 0.14 | 0.43 | 0.29 | 3,600 | 0.37 |
| RTX 4090 | 24 | 1008 | 0.00 | 0.52 | 0.26 | 2,500 | 0.23 |
| RX 7900 XTX | 24 | 960 | 0.00 | 0.49 | 0.25 | 950 | 0.03 |
| Mac mini M4 Pro 64GB | 64 | 273 | 0.24 | 0.07 | 0.16 | 1,400 | 0.08 |
| Arc Pro B65 | 32 | 608 | 0.05 | 0.28 | 0.16 | 750 | 0.00 |
| Framework 64GB | 64 | 256 | 0.24 | 0.06 | 0.15 | 1,599 | 0.11 |
| TT Blackhole p150 | 32 | 512 | 0.05 | 0.22 | 0.13 | 1,400 | 0.08 |
| TT Wormhole n300 | 24 | 576 | 0.00 | 0.26 | 0.13 | 1,400 | 0.08 |
| MacBook Air M5 32GB | 32 | 153 | 0.05 | 0.00 | 0.02 | 1,100 | 0.05 |

Note: Cap Score of 0.00 for 24GB cards means that's the minimum in the dataset -- not that they have no capacity. Everything is relative to the range of platforms compared here.

</details>


A few things jump out. The RX 7900 XTX is the best value pure-bandwidth play if 24GB is enough for your models. The Framework 128GB is quietly the best price-to-capacity ratio in the whole field. The bandwidth score drags it down but nothing else gives you 128GB assignable to a GPU for $1,999. The DGX Spark is the most interesting chart anomaly: high capacity, middling bandwidth, high cost, and a software stack that might eventually justify all of it. The Mac Studio M3 Ultra at 192GB represents the upper right of what's achievable in a single consumer box, and the price reflects it.

## Which bottleneck are you buying?

Stop asking which hardware is best. Start asking which bottleneck you're willing to pay to solve.

If you're doing multi-agent workflows where you need fast concurrent inference, with multiple agents running in parallel each waiting on responses,  bandwidth wins and you want discrete NVIDIA. If you're running a single large reasoning model for deep analysis or long-context work, capacity wins and you want unified memory. If you're experimenting and want the best flexibility per dollar, the Framework Desktop at 128GB or a Mac mini M4 Pro are hard to beat as starting points.

The local AI hardware market in 2026 is finally interesting enough that there's no single right answer. That's actually a good thing. It means the space has matured past the point where CUDA was the only viable path and a $10,000 GPU was the only serious option.

## Sources and where to buy

### Primary references

- [NVIDIA RTX PRO 6000 Blackwell](https://www.nvidia.com/en-us/design-visualization/rtx-pro-6000/)
- [NVIDIA RTX 5090](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/)
- [NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)
- [Apple Mac Studio](https://www.apple.com/mac-studio/)
- [Apple MacBook Pro](https://www.apple.com/macbook-pro/)
- [Apple Mac mini](https://www.apple.com/mac-mini/)
- [AMD Ryzen AI Max (Strix Halo)](https://www.amd.com/en/products/processors/laptop/ryzen/ryzen-ai-max.html)
- [Framework Desktop](https://frame.work/desktop)
- [AMD Radeon PRO W7900](https://www.amd.com/en/products/graphics/workstations/radeon-pro/w7900.html)
- [AMD Radeon AI PRO R9700](https://www.amd.com/en/products/graphics/workstations/radeon-pro/radeon-ai-pro-r9700.html)
- [Intel Arc Pro B-Series](https://www.intel.com/content/www/us/en/products/docs/discrete-gpus/arc/workstation/pro-b-series.html)
- [Tenstorrent Blackhole](https://tenstorrent.com/en/hardware/blackhole)
- [Tenstorrent Wormhole](https://tenstorrent.com/en/hardware/wormhole)
- [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)
- [Qwen3 technical report](https://arxiv.org/html/2505.09388v1)
- [NVIDIA on Llama 4 inference](https://developer.nvidia.com/blog/nvidia-accelerates-inference-on-meta-llama-4-scout-and-maverick/)
- [RTX PRO 6000 pricing detail](https://www.thundercompute.com/blog/nvidia-rtx-pro-6000-pricing)
- [DGX Spark price change](https://forums.developer.nvidia.com/t/2-23-2026-price-change-announcement/361713)

### Where to buy

- **NVIDIA RTX 5090** -- [Best Buy](https://www.bestbuy.com/site/searchpage.jsp?st=RTX+5090), [Newegg](https://www.newegg.com/p/N82E16814133983), [B&H Photo](https://www.bhphotovideo.com/c/product/1798852-REG) (stock is spotty, prices above MSRP)
- **NVIDIA RTX PRO 6000 Blackwell** -- [Newegg](https://www.newegg.com/p/1FT-000S-003H5), [Amazon RTX PRO 6000](https://www.amazon.com/s?k=RTX+PRO+6000+Blackwell), [Micro Center](https://www.microcenter.com/search/search_results.aspx?Ntt=RTX+PRO+6000), [B&H Photo RTX PRO 6000](https://www.bhphotovideo.com/c/search?q=RTX+PRO+6000&sort=PRICE_LOW_TO_HIGH)
- **RTX 4090** -- secondary market, [eBay RTX 4090](https://www.ebay.com/sch/i.html?_nkw=RTX+4090+GPU), [Newegg used](https://www.newegg.com/p/N82E16814133937)
- **Apple Mac Studio** -- [Mac Studio 128GB config](https://www.apple.com/shop/buy-mac/mac-studio), [Mac Studio 192GB config](https://www.apple.com/shop/buy-mac/mac-studio)
- **Apple MacBook Pro** -- [MacBook Pro 16" M5 Max 128GB](https://www.apple.com/shop/buy-mac/macbook-pro)
- **Apple Mac mini** -- [Mac mini M4 Pro config selector](https://www.apple.com/shop/buy-mac/mac-mini)
- **Apple MacBook Air** -- [MacBook Air M5 configs](https://www.apple.com/shop/buy-mac/macbook-air)
- **NVIDIA DGX Spark** -- [NVIDIA Marketplace direct](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/dgx-spark/) (enterprise ordering)
- **ASUS Ascent GX10** -- [ASUS store](https://www.asus.com/us/commercial-servers/asus-ascent-gx10/) (system integrator quotes)
- **Framework Desktop** -- [Framework order page](https://frame.work/desktop) (direct from manufacturer, 128GB config available)
- **AMD RX 7900 XTX** -- [Newegg RX 7900 XTX](https://www.newegg.com/p/N82E16814161643), [Amazon RX 7900 XTX](https://www.amazon.com/s?k=RX+7900+XTX), [B&H Photo RX 7900 XTX](https://www.bhphotovideo.com/c/search?q=RX+7900+XTX)
- **AMD Radeon PRO W7900** -- [AMD.com Radeon PRO](https://www.amd.com/en/products/graphics/workstations/radeon-pro/w7900.html), [CDW PRO W7900](https://www.cdw.com/search/?searchscope=all&keyword=Radeon+PRO+W7900), [B&H Photo PRO W7900](https://www.bhphotovideo.com/c/search?q=Radeon+PRO+W7900)
- **AMD Radeon AI PRO R9700** -- [AMD.com AI PRO](https://www.amd.com/en/products/graphics/workstations/radeon-pro/radeon-ai-pro-r9700.html), [CDW R9700](https://www.cdw.com/search/?searchscope=all&keyword=Radeon+AI+PRO+R9700)
- **Intel Arc Pro B65** -- [Intel Arc Pro B-series](https://www.intel.com/content/www/us/en/ark/products/code/244396/intel-arc-pro-b65.html), [CDW Arc Pro B65](https://www.cdw.com/search/?searchscope=all&keyword=Intel+Arc+Pro+B65)
- **Tenstorrent Wormhole / Blackhole** -- [Tenstorrent store](https://tenstorrent.com/en/store) (direct ordering)
