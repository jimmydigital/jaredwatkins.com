---
title: "LoRA and QLoRA: Efficient Fine-Tuning"
date: 2026-06-10
lastmod: 2026-06-10
draft: false
description: "Low-Rank Adaptation (LoRA) and Quantized LoRA (QLoRA) for dense and MoE models — how the mechanics differ, why MoE fine-tuning is harder, practical target module configurations per model family, and memory requirements."
tags: ["lora", "qlora", "fine-tuning", "parameter-efficient", "quantization", "apple-silicon"]
categories: ["technology"]
research_area: "local-llm-finetuning/fundamentals"
source_urls:
  - "https://arxiv.org/abs/2106.09685"
  - "https://arxiv.org/abs/2305.14314"
  - "https://github.com/artidoro/qlora"
last_reviewed: 2026-06-10
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

LoRA (Low-Rank Adaptation) and its quantized extension QLoRA are the dominant methods for fine-tuning large language models without updating all of their billions of parameters. Instead of modifying the original weight matrices directly, LoRA inserts small trainable matrices alongside the frozen originals. QLoRA adds 4-bit quantization of the base model, cutting VRAM requirements by 4x and making fine-tuning a 7B model feasible on a Mac Mini with 32 GB unified memory or a single consumer GPU.

## Key Facts

- **LoRA paper:** Hu et al. (2021), "LoRA: Low-Rank Adaptation of Large Language Models"
- **QLoRA paper:** Dettmers et al. (2023)
- **Trainable parameters:** ~1–2% of total model parameters (vs. 100% for full fine-tune)
- **VRAM reduction (QLoRA vs. full FT):** ~4–8x
- **Quality vs. full fine-tune:** Within 1–3% on most benchmarks at the same data scale
- **Key hyperparameters:** rank (r), alpha (α), target modules, dropout

## What It Is / How It Works

**The LoRA idea.** In a transformer, most of the parameters live in large weight matrices (the query, key, value, and output projection matrices in attention layers, and the feed-forward layer weights). Full fine-tuning updates all of these — many billions of floating-point numbers. LoRA's insight is that the *update* to each weight matrix during fine-tuning tends to be low-rank: it can be approximated by the product of two much smaller matrices. Instead of directly updating weight matrix W (e.g., 4096×4096 = 16M parameters), LoRA freezes W and adds a parallel path: two small matrices A (4096×r) and B (r×4096) where r is a small rank like 8, 16, or 64. Only A and B are trained. Total trainable parameters per layer: 2 × 4096 × 16 = 131K vs. 16M — a 120x reduction per matrix. At inference, the LoRA weights are merged back: W_new = W + B×A. No inference overhead.

**Choosing rank (r).** Rank controls the expressivity of the adaptation. Higher rank = more trainable parameters = more flexible adaptation = higher risk of overfitting on small datasets. For a domain specialist model like a network engineer expert:
- `r=8` — minimal, good for format/style adaptation when the base model already knows the domain
- `r=16` — standard for most domain fine-tuning tasks
- `r=32` or `r=64` — justified when the target domain has significant vocabulary and command patterns not well-represented in the base model's pretraining data

For Juniper/Cisco fine-tuning, `r=16` is a reasonable default starting point. JunOS and IOS CLI are present in open-source code and documentation that ended up in pretraining data (GitHub, vendor docs) — the base model has some exposure, so you're amplifying existing knowledge rather than injecting entirely new concepts.

**Alpha (α).** The scaling factor applied to the LoRA output: effectively α/r scales the merged update. Convention: set α = 2×r. So for r=16, use α=32. This ensures the LoRA update is neither too large (destabilizing the base model) nor too small (having no effect). Many practitioners use α=r to avoid this scaling entirely; both approaches work.

**Target modules.** LoRA is applied selectively to specific weight matrices. The standard choice is the attention projection matrices: `q_proj`, `k_proj`, `v_proj`, `o_proj`. For better domain adaptation, also targeting `gate_proj`, `up_proj`, `down_proj` (the feed-forward layers) often helps — these layers store more of the factual/domain knowledge. For a network engineer specialist, targeting all linear layers typically produces better command accuracy at modest compute cost.

**QLoRA: adding quantization.** QLoRA extends LoRA by loading the base model weights in 4-bit NormalFloat (NF4) quantization rather than 16-bit bfloat16. This cuts base model VRAM from ~16 GB to ~4 GB for a 7B model. The LoRA adapter weights remain in 16-bit. Combined: a 7B model fine-tune fits in approximately 8–10 GB VRAM. On Apple Silicon (unified memory architecture), a Mac Mini with 24 GB can fine-tune a 7B model; 32 GB allows comfortable training with larger batch sizes or longer sequences.

**Practical QLoRA parameters for a 7B network expert:**

```
base model:   meta-llama/Llama-3.1-8B-Instruct  (or Mistral-7B-Instruct-v0.3)
quantization: 4-bit NF4, double quantization enabled
lora_r:       16
lora_alpha:   32
lora_dropout: 0.05
target_modules: ["q_proj","k_proj","v_proj","o_proj","gate_proj","up_proj","down_proj"]
batch_size:   2–4 (Mac Mini 32GB), 4–8 (A100 40GB)
gradient_accumulation: 8–16 (effective batch 16–32)
learning_rate: 2e-4
lr_scheduler: cosine
epochs:       2–3
sequence_length: 2048
```

**Inference with LoRA.** For deployment, the LoRA adapter is merged into the base model weights before export. The merged model runs with standard inference tools — llama.cpp, Ollama, MLX on Apple Silicon — with zero adapter overhead. The result is a single GGUF or MLX-format model file deployable on a Mac laptop. A 7B model in 4-bit quantization runs at approximately 15–25 tokens/second on an M3 Pro, which is fast enough for interactive use as a network engineer assistant.

## Fine-Tuning Dense Models vs. MoE Models

Dense and MoE transformers share the same attention architecture — the difference is entirely in the feed-forward layers. That localization shapes how fine-tuning works for each.

### Dense model fine-tuning

In a dense model, every forward pass during training touches every layer and every parameter participates in the gradient computation (or in LoRA's case, every adapter layer). The computation graph is static and predictable: input → layer 0 → layer 1 → ... → layer 31 → output, the same path every time regardless of content. This makes training straightforward to implement and reason about.

LoRA on a dense model is well-understood and highly effective. The adapter matrices sit alongside frozen base weights and receive clean gradient signals. Because every token flows through the same MLP weights, the adapter for those weights is updated on every training step — it sees the full dataset uniformly.

### MoE model fine-tuning: the routing problem

MoE fine-tuning introduces a fundamental complication: the router. During a forward pass, each token is independently routed to a subset of experts. Different tokens activate different experts. This creates several issues that don't exist in dense training:

**Uneven adapter updates.** If you place LoRA adapters on the expert weight matrices, only the adapters for the *selected* experts receive gradient updates on any given training step. An expert that the router rarely selects accumulates far fewer gradient updates than a frequently-selected expert — even though both may be relevant to the domain you're training on. In a dense model, every layer's adapter is updated on every step; in a MoE model, expert adapter updates are gated by routing decisions made by a frozen router (assuming you're not fine-tuning the router itself).

**Router drift.** The router was trained alongside the base model to route tokens to experts that handle them well. When you fine-tune the expert weights, the routing decisions that made sense for the original weights may no longer be optimal. But if you also fine-tune the router (a small linear layer — cheap to train), you risk destabilizing the routing patterns learned during pretraining, potentially causing expert collapse (most tokens routing to one or two experts) or incoherent routing that degrades general capability.

**Expert collapse during fine-tuning.** Related to router drift: if the domain-specific training data strongly activates certain experts consistently (e.g., all networking vocabulary routes to the same two experts in a well-trained MoE), fine-tuning may over-specialize those experts while leaving others stale. The auxiliary balancing losses used during pretraining to encourage uniform expert utilization are typically not applied during fine-tuning, making collapse more likely.

### Practical strategies for MoE fine-tuning

**Option 1: Treat it like a dense model, target attention only.** Place LoRA adapters only on the attention projection matrices (Q, K, V, O), which are identical to dense models and receive uniform updates. Leave the MoE expert weights frozen. This is the most conservative approach — you're fine-tuning the information routing (what each token attends to) without touching the storage layers (what each expert computes). It works adequately for style and format adaptation but may be insufficient for deep domain knowledge injection, since most factual knowledge lives in the feed-forward layers.

**Option 2: LoRA on all expert MLP weights, freeze the router.** Place adapters on every expert's gate/up/down projection matrices. Freeze the router entirely. The routing decisions stay fixed from pretraining; the experts themselves adapt. The uneven update problem is real but manageable in practice — infrequently-activated experts may simply adapt less, which is acceptable if those experts don't handle the target domain anyway. Unsloth supports this configuration with `lora_target_modules` including the expert weight names.

**Option 3: Full fine-tune the router, LoRA everything else.** Unfreeze the router weights (tiny — negligible parameter cost) while using LoRA on the expert matrices. This allows the model to adjust routing toward the target domain. Risky without careful monitoring — watch for expert load imbalance in the training logs. Add a load-balancing auxiliary loss term if expert utilization becomes highly skewed.

**Option 4: LoRA on shared experts only (DeepSeek-style MoE).** For models with shared experts (DeepSeek V3, Qwen3.5), place adapters only on the shared expert — the one that activates for every token regardless of routing. This guarantees uniform updates (the shared expert sees every training example) while leaving the routed experts frozen. Less domain depth than targeting all experts, but more stable and predictable.

### Target module names by model family

The expert weight tensor names differ across MoE architectures. When configuring LoRA target modules for MoE fine-tuning:

**Mixtral 8x7B:**
```python
target_modules = [
    "q_proj", "k_proj", "v_proj", "o_proj",      # attention (same as dense)
    "w1", "w2", "w3",                              # expert MLP weights
    # "gate" to also fine-tune the router (use cautiously)
]
```

**Llama 4 Scout / Maverick (alternating dense+MoE layers):**
```python
# Dense layers have standard MLP names; MoE layers have expert names
target_modules = [
    "q_proj", "k_proj", "v_proj", "o_proj",        # attention all layers
    "gate_proj", "up_proj", "down_proj",            # dense MLP layers
    "experts.*.gate_proj",                          # MoE expert layers (wildcard)
    "experts.*.up_proj",
    "experts.*.down_proj",
]
```

**Qwen3 / Qwen3.5 (fine-grained MoE with shared expert):**
```python
target_modules = [
    "q_proj", "k_proj", "v_proj", "o_proj",
    "shared_expert.gate_proj",                     # shared expert (always active)
    "shared_expert.up_proj",
    "shared_expert.down_proj",
    # optionally: "experts.*.gate_proj" etc. for routed experts
]
```

Check Unsloth's model-specific documentation and the `get_peft_model` output before training — it will show exactly how many trainable parameters each configuration produces and flag any unrecognized module names.

### Memory and compute implications

MoE fine-tuning has higher memory requirements than dense fine-tuning at equivalent active parameter counts, because all expert weights must be resident regardless of routing:

| Model | Active params | Total params | Min VRAM (QLoRA) | Notes |
|-------|--------------|-------------|-----------------|-------|
| Llama 3.1 8B (dense) | 8B | 8B | ~10 GB | Standard baseline |
| Mistral 7B (dense) | 7B | 7B | ~9 GB | Similar to above |
| Mixtral 8x7B (MoE) | 12.9B | 46.7B | ~28 GB | All 8 experts must be loaded |
| Llama 4 Scout 17B-16E (MoE) | 17B | 109B | ~60 GB | Not viable on single consumer GPU |
| Qwen3 30B-A3B (MoE) | 3B | 30B | ~18 GB | All 30B on disk even though 3B active |
| Qwen3 8B (dense) | 8B | 8B | ~10 GB | Better choice for local fine-tuning |

This is the clearest practical implication: **for fine-tuning on consumer hardware (Mac Mini, single A100 40GB), dense models in the 7B–14B range are significantly more accessible than equivalent-capability MoE models.** Qwen3 8B dense is a better fine-tuning target than Qwen3 30B-A3B MoE even though the MoE model has higher raw capability — the MoE fine-tune requires 2× the memory for a more complex training process.

For the network engineer specialist models in this research, this is a concrete recommendation: start with dense models (Llama 3.1 8B, Qwen3 8B, Ministral 8B). Only consider MoE fine-tuning if you have an A100 80GB or larger, and you've already validated that the dense fine-tune quality is insufficient.

### What MoE fine-tuning is actually good at

Despite the complications, there are scenarios where MoE fine-tuning is worth pursuing:

**Multi-domain specialist models.** If you want one model that handles both Juniper *and* Cisco expertise — different enough domains that a dense model may conflate their CLI syntax — a MoE base gives the fine-tune more capacity to develop separate internal representations for each vendor. The routing mechanism may naturally distribute Juniper-specific patterns to different experts than Cisco-specific patterns, producing cleaner specialization than a dense model of equivalent active parameter count.

**Very large training datasets.** At 50,000+ training examples, the expert underutilization problem shrinks — diverse data will activate most experts across the training run, producing more uniform adaptation. Fine-tuning small MoE models on small datasets is where the pathologies are worst.

**Distillation targets.** One effective approach: fine-tune a large dense teacher model (Llama 3.1 70B or Qwen2.5 72B) on your domain data first, use it to generate high-quality synthetic training data, then fine-tune a smaller MoE student on that data. The MoE gets specialist knowledge distilled from a superior teacher rather than learning directly from raw examples. This sidesteps many of the MoE fine-tuning pathologies.

## Notable Developments

- **2024:** Unsloth — open-source LoRA training library with 2x speed improvement and 60% less VRAM than standard HuggingFace PEFT on NVIDIA GPUs; also supports Apple Silicon via MLX backend
- **2024:** MLX fine-tuning (Apple) — Apple's MLX framework supports LoRA fine-tuning natively on Apple Silicon with the `mlx_lm` library; optimized for unified memory
- **2023:** QLoRA (Dettmers et al.) — 4-bit quantization + LoRA; enabled fine-tuning 65B models on a single 48GB GPU
- **2021:** LoRA (Hu et al.) — introduced the core low-rank adapter concept

## Sources

- [LoRA: Low-Rank Adaptation of Large Language Models (Hu et al. 2021)](https://arxiv.org/abs/2106.09685)
- [QLoRA: Efficient Finetuning of Quantized LLMs (Dettmers et al. 2023)](https://arxiv.org/abs/2305.14314)
- [QLoRA GitHub (artidoro)](https://github.com/artidoro/qlora)
- [Unsloth](https://github.com/unslothai/unsloth) — practical fast LoRA training
- [Apple MLX examples — LoRA fine-tuning](https://github.com/ml-explore/mlx-examples/tree/main/lora)
