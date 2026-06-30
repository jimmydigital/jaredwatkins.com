---
title: "Cloud GPU Fine-Tuning"
date: 2026-06-10
lastmod: 2026-06-10
draft: false
description: "Renting GPU instances on RunPod, Lambda Labs, and Vast.ai for LLM fine-tuning: instance types, current pricing, realistic time-to-completion, and cost estimates for a 10,000-example network engineer dataset."
research_area: "local-llm-finetuning/compute-options"
source_urls:
  - "https://www.runpod.io/gpu-instance/pricing"
  - "https://lambdalabs.com/service/gpu-cloud"
  - "https://vast.ai"
  - "https://github.com/unslothai/unsloth"
last_reviewed: 2026-06-10
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

For users who want faster training or lack sufficient Apple Silicon RAM, GPU cloud rental is the practical alternative to owned hardware. Three providers dominate the accessible end of the market: RunPod, Lambda Labs, and Vast.ai. An A100 40GB is the reliable workhorse for 7B–13B fine-tuning. The total cost to fine-tune a 7B model on a 10,000-example dataset is $5–$30 depending on instance type and provider, making GPU rental cost-competitive with Apple Silicon for infrequent fine-tuning runs.

## Key Facts

- **Best value instance:** A100 40GB (RunPod ~$1.40–1.80/hr; Lambda Labs ~$1.30/hr)
- **Fastest option:** H100 80GB (~$2.50–3.50/hr) — worth it for 13B+ models or large datasets
- **Training speed (7B QLoRA, A100 40GB, Unsloth):** ~2,500–3,500 tokens/second
- **Training time (10,000 examples, 512 avg tokens, 3 epochs, A100):** ~1.5–2.5 hours
- **Total cost for a full 7B fine-tune run (A100):** $3–$10
- **Recommended framework:** Unsloth + HuggingFace Transformers + Axolotl

## What It Is / How It Works

**Provider comparison.**

*RunPod* offers on-demand and spot instances via a web console and API. GPU selection is broad; A100 40GB and 80GB are reliably available. Spot instances ("Community Cloud" in RunPod's terminology) are 30–50% cheaper but can be interrupted. For a 2-hour fine-tuning run, spot is acceptable — the risk of interruption in a 2-hour window is low. RunPod supports persistent storage volumes (pod volumes) that survive instance restarts, which is important for saving checkpoints.

*Lambda Labs* is cleaner for ML practitioners: fewer configuration options, more predictable availability, slightly lower prices on A100. No spot pricing — on-demand only. Less flexible for custom images but works out of the box with their GPU Cloud Jupyter notebooks.

*Vast.ai* is the cheapest option — consumer GPU hardware rented from individuals. RTX 4090 instances at $0.40–0.70/hr are available; 24GB VRAM fits a 7B QLoRA run. The tradeoff is reliability and security: hardware varies, instance availability fluctuates, and you're running on someone else's desktop GPU. Fine for development and testing; less appropriate for production data that's sensitive.

**Instance selection guide:**

| Model Size | Task | Recommended Instance | VRAM Needed |
|------------|------|---------------------|-------------|
| 7B QLoRA | Training | A100 40GB or RTX 4090 24GB | ~12–16 GB |
| 7B full fine-tune | Training | A100 80GB or H100 | ~60–80 GB |
| 13B QLoRA | Training | A100 40GB (tight) or 80GB | ~20–28 GB |
| 13B full fine-tune | Training | H100 80GB or multi-GPU | ~120+ GB |

For the network engineer specialist use case (7B QLoRA), an A100 40GB is comfortable and well-supported by all frameworks.

**Tooling stack for cloud GPU training.**

The recommended stack for cloud GPU is Unsloth + Axolotl:

*Unsloth* is a drop-in replacement for HuggingFace PEFT that provides 2x training speed and ~60% less VRAM usage through custom CUDA kernels. As of 2025 it supports Llama 3.x, Mistral, Gemma 2, Phi-3, and most major 7B–70B models. Works on any NVIDIA GPU with CUDA 11.8+.

*Axolotl* is a configuration-driven fine-tuning framework that wraps HuggingFace Transformers and PEFT. You write a YAML config file specifying model, dataset, LoRA parameters, and training options — it handles the training loop, checkpointing, and logging. Strong community and Docker images pre-configured for most GPU instances.

**Example Axolotl config for Juniper expert fine-tuning on A100:**

```yaml
# axolotl_juniper.yml
base_model: meta-llama/Llama-3.1-8B-Instruct
model_type: LlamaForCausalLM
tokenizer_type: AutoTokenizer

load_in_4bit: true
strict: false

datasets:
  - path: ./data/juniper-expert/train.jsonl
    type: chat_template
    chat_template: llama3

val_set_size: 0.1
output_dir: ./output/juniper-expert-v1

adapter: lora
lora_r: 16
lora_alpha: 32
lora_dropout: 0.05
lora_target_linear: true  # targets all linear layers

sequence_len: 2048
sample_packing: true     # packs short examples into one sequence — big throughput gain
pad_to_sequence_len: true

micro_batch_size: 2
gradient_accumulation_steps: 8
num_epochs: 3
learning_rate: 2e-4
lr_scheduler: cosine
warmup_steps: 100
optimizer: adamw_8bit    # 8-bit optimizer saves ~4GB VRAM

logging_steps: 10
eval_steps: 100
save_steps: 500
save_total_limit: 3

bf16: true               # A100 supports bfloat16 natively
tf32: true
flash_attention: true    # FlashAttention 2 — significant speed improvement on A100
```

**RunPod setup workflow:**

```bash
# 1. Launch RunPod instance: A100 40GB, RunPod PyTorch 2.2 image
# 2. SSH in and set up environment

pip install unsloth axolotl

# 3. Upload your dataset (or clone from private repo)
git clone https://your-private-repo/network-expert-data.git ./data

# 4. Download the base model
huggingface-cli login  # need HF token for gated Llama 3 models
huggingface-cli download meta-llama/Llama-3.1-8B-Instruct

# 5. Run training
axolotl train axolotl_juniper.yml

# 6. Merge LoRA adapter and export
python -c "
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained('./output/juniper-expert-v1/checkpoint-final')
model.save_pretrained_merged('./output/juniper-expert-v1-merged', tokenizer, save_method='merged_16bit')
"

# 7. Convert to GGUF for local deployment on Mac
python llama.cpp/convert_hf_to_gguf.py ./output/juniper-expert-v1-merged --outtype q4_k_m --outfile juniper-expert-v1.gguf

# 8. Download the GGUF to your Mac via scp or Cloudflare tunnel
scp user@runpod-ip:~/juniper-expert-v1.gguf ~/models/
```

**Cost estimates (2025–2026 prices; verify current prices before use):**

| Provider | Instance | Price/hr | 2-hr run | 5-hr run |
|----------|----------|----------|---------|---------|
| RunPod | A100 40GB (on-demand) | ~$1.50 | ~$3 | ~$7.50 |
| RunPod | A100 40GB (spot) | ~$0.90 | ~$2 | ~$4.50 |
| Lambda Labs | A100 40GB | ~$1.30 | ~$2.60 | ~$6.50 |
| Vast.ai | RTX 4090 | ~$0.55 | ~$1.10 | ~$2.75 |
| RunPod | H100 80GB | ~$3.00 | ~$6 | ~$15 |

Additional costs: egress bandwidth for downloading the trained model (typically negligible at <10 GB), persistent storage (~$0.07/GB/month on RunPod, worth having for checkpoints during long runs).

**Training speed and time estimates (A100 40GB, Unsloth, bfloat16, FlashAttention 2):**

| Dataset size | Avg seq length | Epochs | Tokens total | ~Time on A100 |
|-------------|---------------|--------|-------------|--------------|
| 5,000 examples | 512 tokens | 3 | 7.7M tokens | ~45 min |
| 10,000 examples | 512 tokens | 3 | 15.4M tokens | ~1.5 hr |
| 10,000 examples | 1024 tokens | 3 | 30.7M tokens | ~2.5 hr |
| 20,000 examples | 1024 tokens | 3 | 61.4M tokens | ~4.5 hr |

Note: Sample packing (packing multiple short examples into one sequence) significantly improves throughput by reducing padding waste. Enable it in Axolotl for datasets with many short examples.

**Monitoring training on a remote instance.** Use Weights & Biases (free tier) or TensorBoard for training metrics. Key metrics to watch: training loss (should decrease), validation loss (stop if it starts increasing — sign of overfitting), and gradient norm (should stay under 1.0; spikes indicate instability). For a 2-hour run, connect `wandb` to Axolotl config with two lines and monitor from your phone if desired.

**Security note for network data.** If your training data contains real network configurations, IP addresses, credentials, or proprietary topology information, do not upload it to a cloud GPU instance without appropriate scrubbing. Sanitize all IPs, hostnames, credentials, and identifying information before training on rented infrastructure. The cloud GPU instance's storage is not private.

## Sources

- [RunPod GPU Instances](https://www.runpod.io/gpu-instance/pricing)
- [Lambda Labs GPU Cloud](https://lambdalabs.com/service/gpu-cloud)
- [Vast.ai](https://vast.ai)
- [Unsloth GitHub](https://github.com/unslothai/unsloth)
- [Axolotl GitHub](https://github.com/OpenAccess-AI-Collective/axolotl)
- [FlashAttention 2 paper](https://arxiv.org/abs/2307.08691) — speed improvement technique used in training
