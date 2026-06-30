---
title: "LoRA Adapter Versioning and Rollback"
date: 2026-06-11
lastmod: 2026-06-11
draft: false
description: "How to version, store, and swap LoRA adapters as you iterate on a fine-tuned network expert model — keeping the base model separate from adapters, testing a new adapter before switching, and rolling back when a new version regresses."
research_area: "local-llm-finetuning/specialist-models"
source_urls: []
last_reviewed: 2026-06-11
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

A fine-tuned specialist model is not a one-time artifact — you'll iterate on the training data, fix systematic errors, add new command coverage, and re-train. Without a versioning discipline from the start, you lose the ability to compare versions, roll back to a working model, or understand what changed between a good version and a broken one. This entry covers the directory structure and naming convention for adapter versions, the workflow for safely swapping a new adapter into production, and how to maintain multiple named Ollama models pointing to different versions simultaneously.

## Key Facts

- **The base model never changes** — always keep the original downloaded base model intact and separate from any adapter
- **LoRA adapters are small** — a 7B model adapter at r=16 is approximately 100–200 MB; storage cost of keeping every version is minimal
- **Merged GGUF files are larger** — a merged 7B Q4_K_M model is ~4.5 GB; keep only the versions you actually use in production
- **Rollback is only possible if you kept the old adapter** — this seems obvious but is easy to skip when iterating quickly
- **Test the new adapter against eval before swapping** — never replace the production model without running the eval suite on the new version

---

## Keeping Base and Adapter Separate

LoRA training produces two artifacts: the base model weights and the adapter weights. The adapter is a set of small matrices that modify the base model's behavior. These should be stored separately:

```
~/models/
  base/
    llama-3.1-8b-instruct/           ← original downloaded base model, never modified
      model.safetensors (shards)
      tokenizer.json
      config.json
      ...
    qwen3-8b/                        ← another base model option
      ...
  adapters/
    juniper-expert/
      v1/
        adapter_config.json          ← LoRA hyperparameters (r, alpha, target modules)
        adapter_model.safetensors    ← the actual adapter weights
        system_prompt.txt            ← exact system prompt used in training data
        train_run.json               ← training metadata: dataset path, epochs, loss curve
        eval_results.json            ← eval scores from evaluation-and-testing pipeline
      v2/
        ...
      v3/
        ...
    cisco-expert/
      v1/
        ...
  merged/
    juniper-expert-v3-q4km.gguf     ← merged + quantized, for Ollama deployment
    juniper-expert-v2-q4km.gguf     ← previous version, kept for rollback
```

**Why keep the raw adapter separate from the merged GGUF?** The merged GGUF is produced by applying the adapter to the base model and quantizing. If you need to re-merge (different quantization level, different base model version, apply adapter to a newer base), you need the raw adapter. Keeping only the merged GGUF means re-training if anything changes in the merge pipeline.

---

## Training Run Metadata

Every training run should produce a metadata file alongside the adapter. This makes it possible to understand what changed between versions without digging through commit history:

```json
{
  "version": "v3",
  "date": "2026-06-15",
  "base_model": "meta-llama/Llama-3.1-8B-Instruct",
  "base_model_sha": "abc123...",
  "training_data": {
    "path": "datasets/juniper-expert/train_v3.jsonl",
    "examples": 12450,
    "sha256": "def456..."
  },
  "hyperparameters": {
    "lora_r": 16,
    "lora_alpha": 32,
    "lora_dropout": 0.05,
    "target_modules": ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    "learning_rate": 2e-4,
    "epochs": 3,
    "batch_size": 4,
    "sequence_length": 2048
  },
  "training_duration_hours": 6.2,
  "final_train_loss": 0.42,
  "changes_from_v2": "Added 2,000 BGP troubleshooting examples; fixed 150 firewall filter examples with incorrect term syntax"
}
```

The `changes_from_v2` field is the most valuable entry — written in plain language, it makes the version history readable without needing to diff JSONL training files.

---

## Merging and Quantizing for Deployment

The trained LoRA adapter must be merged into the base model and quantized to GGUF format before Ollama can serve it. The merge step applies the adapter matrices to the base weights to produce a single unified model file:

```bash
# Step 1: Merge adapter into base model (produces a full float16 model)
# Using Unsloth:
python -c "
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    'meta-llama/Llama-3.1-8B-Instruct',
    load_in_4bit=False
)
model.load_adapter('~/models/adapters/juniper-expert/v3/')
model.save_pretrained_merged(
    '~/models/merged-fp16/juniper-expert-v3',
    tokenizer,
    save_method='merged_16bit'
)
"

# Step 2: Convert to GGUF and quantize (using llama.cpp)
cd ~/llama.cpp
python convert_hf_to_gguf.py ~/models/merged-fp16/juniper-expert-v3 \
  --outfile ~/models/merged/juniper-expert-v3-f16.gguf \
  --outtype f16

# Quantize to Q4_K_M (4-bit, best quality/size tradeoff for deployment)
./llama-quantize \
  ~/models/merged/juniper-expert-v3-f16.gguf \
  ~/models/merged/juniper-expert-v3-q4km.gguf \
  Q4_K_M

# Clean up the intermediate f16 (large — ~16 GB for 8B model)
rm ~/models/merged/juniper-expert-v3-f16.gguf
```

Keep the Q4_K_M GGUF for both the new version and the previous version until the new version passes eval:

```
~/models/merged/
  juniper-expert-v3-q4km.gguf    ← new version (under test)
  juniper-expert-v2-q4km.gguf    ← current production version (keep until v3 is validated)
```

---

## Registering Multiple Versions in Ollama

Ollama identifies models by name. You can register multiple versions simultaneously with distinct names, which makes A/B comparison and rollback fast:

```bash
# Register v3 under a test name (don't overwrite production yet)
cat > /tmp/Modelfile.juniper-v3 << 'EOF'
FROM /Users/yourname/models/merged/juniper-expert-v3-q4km.gguf

SYSTEM """[exact system prompt text — must match training data]"""

PARAMETER temperature 0.1
PARAMETER top_p 0.9
PARAMETER top_k 40
PARAMETER num_ctx 4096
PARAMETER repeat_penalty 1.1
EOF

ollama create juniper-expert-v3 -f /tmp/Modelfile.juniper-v3

# Production model still points to v2
ollama list
# NAME                   ID            SIZE    MODIFIED
# juniper-expert         abc123...    4.5 GB  2 weeks ago   ← current production (v2)
# juniper-expert-v3      def456...    4.5 GB  just now      ← under test
```

Run the eval suite against both `juniper-expert` (v2) and `juniper-expert-v3`:

```python
v2_results = run_eval("juniper-expert", eval_set_path)
v3_results = run_eval("juniper-expert-v3", eval_set_path)

print_comparison(v2_results, v3_results)
# Expected output:
# Metric                  v2      v3      delta
# Exact match accuracy   82%     87%     +5%
# Command presence        71%     75%     +4%
# General reasoning      -3%     -2%     +1%
```

Only after confirming improvement do you swap production to v3:

```bash
# Swap production to v3
# Option A: re-create the production model name pointing to v3 GGUF
cat > /tmp/Modelfile.juniper << 'EOF'
FROM /Users/yourname/models/merged/juniper-expert-v3-q4km.gguf
[... same params ...]
EOF
ollama create juniper-expert -f /tmp/Modelfile.juniper

# Option B: rename models (Ollama doesn't support rename directly; use cp)
# Just update the Modelfile FROM path

# Keep the v3 name as a backup reference
# You can now delete juniper-expert-v3 if you want to clean up
```

---

## Rollback Procedure

If the new version causes problems in actual use (produces wrong commands that a domain expert catches, or behaves strangely on edge cases not covered by eval), rollback is a single command:

```bash
# Rollback: restore production to v2
cat > /tmp/Modelfile.juniper-rollback << 'EOF'
FROM /Users/yourname/models/merged/juniper-expert-v2-q4km.gguf
[... same params ...]
EOF
ollama create juniper-expert -f /tmp/Modelfile.juniper-rollback
```

Rollback takes under 30 seconds. The reason rollback is this fast is that the GGUF file already exists — Ollama's `create` command just writes a new manifest pointing to the existing file, it doesn't re-copy or re-process the model weights.

**After rolling back:** note the specific failure that triggered the rollback in the training run metadata. Then either:
1. Add examples to the training data specifically targeting the failure mode, retrain, and re-evaluate
2. If the failure was in the eval set but not caught, add that case to the eval set before retraining

---

## Automating the Version and Deploy Workflow

A simple shell script captures the full workflow: merge → quantize → register in Ollama under a versioned name → run eval → report:

```bash
#!/bin/bash
# deploy_adapter.sh VERSION
# Usage: ./deploy_adapter.sh v4

VERSION=$1
ADAPTER_DIR=~/models/adapters/juniper-expert/$VERSION
MERGED_PATH=~/models/merged/juniper-expert-$VERSION-q4km.gguf
MODELFILE_PATH=/tmp/Modelfile.juniper-$VERSION

echo "=== Merging adapter $VERSION ==="
python merge_adapter.py \
  --base meta-llama/Llama-3.1-8B-Instruct \
  --adapter $ADAPTER_DIR \
  --output-gguf $MERGED_PATH

echo "=== Registering in Ollama ==="
cat > $MODELFILE_PATH << EOF
FROM $MERGED_PATH
SYSTEM "$(cat $ADAPTER_DIR/system_prompt.txt)"
PARAMETER temperature 0.1
PARAMETER top_p 0.9
PARAMETER num_ctx 4096
PARAMETER repeat_penalty 1.1
EOF
ollama create juniper-expert-$VERSION -f $MODELFILE_PATH

echo "=== Running eval ==="
python run_eval.py \
  --model juniper-expert-$VERSION \
  --eval-set datasets/juniper-expert/eval_v1.jsonl \
  --compare-to juniper-expert \
  --output $ADAPTER_DIR/eval_results.json

echo "=== Done. Review eval_results.json before promoting to production. ==="
```

Running `./deploy_adapter.sh v4` produces a versioned model in Ollama and an eval comparison report. Promoting to production is a separate manual step requiring a human decision — never auto-promote.

---

## What to Keep and What to Delete

As versions accumulate:

**Always keep:**
- All raw adapter directories (tiny, ~150 MB each)
- Training run metadata JSON for every version
- The system prompt text for every version
- The eval results JSON for every version
- The GGUF for the current production version
- The GGUF for the immediately prior version (rollback target)

**Safe to delete after promotion:**
- Merged F16 GGUFs (large — 16 GB — and reproducible from the adapter)
- Ollama model registrations for versions older than 2 prior (they consume disk via manifest entries but negligible)
- GGUF files for versions older than the current production and one prior

**Never delete:**
- The base model download
- Any adapter whose GGUF has already been deleted (you'd need to re-run merge from it)
