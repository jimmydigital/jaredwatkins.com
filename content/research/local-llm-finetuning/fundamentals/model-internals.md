---
title: "Model Internals: Weights, MoE, and How Inference Works"
date: 2026-06-10
lastmod: 2026-06-10
draft: false
description: "What a trained model actually is on disk, how transformer layers are structured beyond 'a matrix of weights', how Mixture of Experts builds on dense transformers, and how a model server turns a text query into output tokens — including what's different about serving MoE vs. dense models."
research_area: "local-llm-finetuning/fundamentals"
source_urls:
  - "https://arxiv.org/abs/1706.03762"
  - "https://arxiv.org/abs/2101.03961"
  - "https://arxiv.org/abs/2407.06204"
  - "https://llama.cpp/docs"
  - "https://ollama.com/docs"
last_reviewed: 2026-06-10
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

"A model is a matrix of weights" is true but too compressed to be useful for understanding how inference actually works, why MoE architectures behave differently from dense models, or what a model server is actually doing when it processes a query. This entry unpacks the structure: what the weight files actually contain, how the transformer computation flows through them, how Mixture of Experts extends that computation by adding conditional routing, what the training output looks like on disk, and how serving infrastructure manages the problem of running these models efficiently at query time.

## Key Facts

- **A model file is not one matrix** — it is hundreds of named tensors organized into a specific repeating layer structure
- **Dense transformer inference** is a fixed sequence of matrix multiplications through every layer, every token, every time
- **MoE inference** adds a learned routing step that selects a subset of "expert" sub-networks per token — most parameters are bypassed per forward pass
- **The KV cache** is the most important inference optimization and the primary reason context length drives memory requirements
- **GGUF** is the standard on-disk format for quantized local model deployment; model servers like llama.cpp and Ollama load and execute it
- **MoE serving challenges** differ fundamentally from dense: the experts that get activated vary per token, creating irregular memory access patterns that hurt GPU utilization

---

## Part 1: What a Model Actually Is

### The weight files

When you download a model from HuggingFace, you get a collection of files. The substantive content — the learned parameters — typically lives in `.safetensors` files. A 7B model might be split across 4–8 such files for download convenience; they are loaded and concatenated at runtime.

The `.safetensors` format was introduced by HuggingFace in 2022 to replace the older `.pt` (PyTorch) format. The distinction matters for security, not performance. `.pt` files are serialized Python objects, loaded using Python's `pickle` module. Pickle is a general-purpose Python serialization mechanism that can encode arbitrary Python objects — including executable code. A malicious `.pt` file can run arbitrary code on your machine the moment you load it, with no warning and no sandbox. This is not theoretical: loading a model file from an untrusted source with `torch.load()` is equivalent to running an executable from that source. The attack surface is real because model files are large, opaque binaries that users routinely download and load without inspection.

`.safetensors` solves this by storing only raw tensor data — the arrays of numbers — with a simple header describing their names, shapes, and data types. There is no executable content, no Python objects, no deserialization of arbitrary code. The file format is a strict schema: header (JSON) + raw binary tensor data. A `.safetensors` loader reads the header to find each tensor's byte offset and shape, then memory-maps the raw bytes directly into the process. It cannot execute code because the format has no mechanism for encoding code. Loading a `.safetensors` file from an untrusted source is no more dangerous than opening a JPEG — the worst it can do is contain wrong numbers, not execute malware.

For the network engineer specialist use case, where you are downloading base models from HuggingFace and running them on a laptop with direct access to network infrastructure, the security property matters: prefer `.safetensors` sources, and be cautious about any workflow that uses `torch.load()` on files from unverified origins.

Each file is a collection of named tensors. A tensor is an n-dimensional array of floating-point numbers. For a transformer layer, the named tensors look something like:

```
model.layers.0.self_attn.q_proj.weight        shape: [4096, 4096]
model.layers.0.self_attn.k_proj.weight        shape: [1024, 4096]
model.layers.0.self_attn.v_proj.weight        shape: [1024, 4096]
model.layers.0.self_attn.o_proj.weight        shape: [4096, 4096]
model.layers.0.mlp.gate_proj.weight           shape: [14336, 4096]
model.layers.0.mlp.up_proj.weight             shape: [14336, 4096]
model.layers.0.mlp.down_proj.weight           shape: [4096, 14336]
model.layers.0.input_layernorm.weight         shape: [4096]
model.layers.0.post_attention_layernorm.weight shape: [4096]
```

This is one layer of Llama 3.1 8B. There are 32 such layers. Plus the token embedding table, the final normalization, and the output projection (the "language model head" that maps from model dimension to vocabulary size). In total, approximately 8 billion floating-point numbers.

The shape `[4096, 4096]` means 4096 rows × 4096 columns = 16.7 million numbers in that one tensor. At 16-bit (bfloat16) that is 33 MB. In 4-bit quantization it is ~8 MB. This is why quantization has such a large effect: each tensor shrinks by 4x.

### What each component does

**Token embeddings.** Before any transformer computation, each input token (an integer from 0 to 127,999 for Llama 3) is looked up in an embedding table — a matrix of shape `[vocab_size, model_dim]` = `[128000, 4096]`. The result is a dense vector of 4096 floating-point numbers. This vector is the token's initial representation entering the transformer stack.

**Layer normalization (`layernorm.weight`).** A 1D tensor of 4096 numbers. Applied before the attention and feed-forward operations in each layer. Stabilizes training by normalizing activations. The weight tensor is learned — it scales the normalized values. Small and cheap; negligible contribution to parameter count.

**Attention: Q, K, V, O projections.** This is the heart of the transformer. Given the current token's representation vector (4096 numbers), three separate linear projections produce:
- **Q (query):** "What am I looking for?"
- **K (key):** "What information do I hold?"
- **V (value):** "What information will I contribute?"

Each projection is a matrix multiply: input vector (4096) × weight matrix (4096 × 4096) = output vector (4096). This is expensive — it is the dominant compute cost per layer.

The attention mechanism then computes: for each token, compare its Q vector against all previous tokens' K vectors to produce attention scores (how much does this token "attend to" each prior token?). Softmax those scores into weights summing to 1. Take the weighted sum of all prior tokens' V vectors. This produces a context-aware output — a new representation for the current token that incorporates information from everything it attended to.

**Grouped-query attention (GQA).** Modern models like Llama 3 use fewer K and V projection matrices than Q matrices. Where Q has a `[4096, 4096]` projection, K and V use `[1024, 4096]` — one-quarter the size. Multiple "query heads" share a single "key-value head." This reduces memory and compute at minor quality cost. It is why the K and V weight shapes are smaller than Q in the example above.

**Feed-forward / MLP layers.** After attention, each token passes through a feed-forward network with three weight matrices (gate, up, down projections). These are the largest tensors in the model: `[14336, 4096]` is 58 million numbers — about 3.5× the size of each attention projection. They function as a kind of "storage" layer — if attention is about routing information between tokens, the feed-forward layers are where the model stores and retrieves factual associations and domain knowledge. The large size of these layers is why fine-tuning the MLP layers in addition to attention layers significantly improves domain adaptation.

**The output projection (LM head).** After all transformer layers, a final linear projection maps the last token's representation from model_dim (4096) to vocabulary size (128,000). The result is a vector of 128,000 logit scores — one per token in the vocabulary. Softmax converts these to probabilities. Sampling then picks the next token from this distribution.

### The forward pass, step by step

For a query "show bgp summary" (4 tokens after tokenization):

1. Each token is converted to a 4096-dimensional embedding vector. You now have 4 vectors.
2. These 4 vectors are fed into layer 0 of 32. Each layer:
   a. Apply layer norm
   b. Compute Q, K, V projections for all tokens simultaneously
   c. Compute attention scores between all token pairs (each attends to all preceding tokens)
   d. Weight and sum the V vectors to produce attention output
   e. Add residual connection (add the input back to the attention output)
   f. Apply layer norm
   g. Feed through MLP (gate, up, down projections)
   h. Add residual connection
3. After layer 32, apply final layer norm and LM head projection
4. The result is a probability distribution over the vocabulary. Sample a token. This is the first output token.
5. Add the new token to the input sequence. Repeat from step 2.

This is **autoregressive generation**: one token at a time, each token conditioned on all previous tokens. Generating 100 tokens means running the full forward pass 100 times. This is why generation speed is measured in tokens per second rather than queries per second.

---

## Part 2: The KV Cache

The KV cache is the single most important optimization in LLM inference, and it is the direct reason why memory requirements scale with context length.

During step 2c above, the attention computation requires the K and V vectors for every prior token in the sequence. If you are generating token 500 in a long response, you need the K and V for all 499 prior tokens to compute attention for token 500. Without caching, you would recompute all 499 K and V projections on every generation step — extremely wasteful since those tokens are not changing.

The KV cache stores the K and V tensors from every previous computation so they only need to be computed once. For a sequence of length N, the cache stores 2 (K and V) × 32 (layers) × N (tokens) × 1024 (head dimension) × 2 bytes (bfloat16) of data.

For a 7B model at context length 4096: 2 × 32 × 4096 × 1024 × 2 = **536 MB**. At 128K context: **16.8 GB**. This is why context length has such a dramatic effect on total memory requirements — a 7B model's weights are ~4 GB in 4-bit, but running it at 128K context requires another 16+ GB for the KV cache. On Apple Silicon with unified memory this is manageable; on a discrete GPU with 24 GB VRAM it consumes most of the available memory.

This also explains prompt processing: when you send a long prompt, the model processes all prompt tokens in parallel (one forward pass, all tokens at once — fast), populates the KV cache with all their K and V vectors, then switches to the slow autoregressive token-by-token generation phase.

---

## Part 3: Mixture of Experts

### The dense model bottleneck

In a standard dense transformer, every token is processed by every parameter on every forward pass. The feed-forward MLP layers are especially wasteful from this perspective: a question about JunOS OSPF and a question about Python list comprehensions both activate the same MLP weights, even though those weights cannot be simultaneously specialized for both. The model must find parameter settings that are mediocre for everything rather than excellent for specific domains.

This is the problem MoE solves.

### The MoE substitution

Mixture of Experts replaces the single feed-forward MLP in each transformer layer with a set of N independent feed-forward networks ("experts") plus a small learned router network. For Mixtral 8x7B: 8 expert MLPs per layer instead of 1, plus a router.

The router is a small linear layer (shape: `[model_dim, num_experts]` = `[4096, 8]`) that takes the current token's representation vector and outputs a score for each expert. Softmax converts these to routing weights. Only the **top-k experts** (typically k=2) are selected and activated. Their outputs are weighted by their routing scores and summed.

```
token representation (4096 dims)
        │
        ├──→ Router (4096 × 8 linear) → [score_0, ..., score_7]
        │           → top-2 experts selected: say experts 3 and 6
        │
        ├──→ Expert 3 MLP (full-size feed-forward network) → output_3
        │
        └──→ Expert 6 MLP (full-size feed-forward network) → output_6
                    │
                    ↓
        weighted_sum(output_3 × score_3, output_6 × score_6)
```

For Mixtral 8x7B:
- Each expert is a full-size MLP comparable to the MLP in a 7B dense model
- 8 experts × ~7B parameters each ≈ 46.7B total parameters
- But only 2 experts are activated per token: ~12.9B parameters actually compute
- The model has the *capacity* of 46.7B but the *compute cost* of ~13B

### What the router learns

The routing is fully learned during training — there are no hard-coded topic assignments. The model naturally develops expert specialization through training dynamics: tokens that co-occur frequently (code tokens, specific syntactic constructs, domain-specific vocabulary) tend to get routed to the same experts over time, because that expert's weights get updated together and become tuned for those patterns.

In practice, analysis of trained MoE models shows:
- Experts do develop loose specializations (syntax vs. semantics, languages, domains) but it's gradual and overlapping, not crisp categories
- The same token can be routed to different experts depending on context (the surrounding tokens affect the representation fed to the router)
- Router load balancing is a training concern: if most tokens always route to the same 2 experts, the rest learn nothing useful. Auxiliary balancing losses during training encourage more uniform expert utilization.

### Expert granularity variants

The original MoE design uses a small number of large experts (8 experts each the size of a 7B MLP — Mixtral). Later designs diverged:

**Fine-grained MoE (DeepSeek, Qwen3.5):** Many more, smaller experts. DeepSeek-V3 uses 256 experts with 8 active per token. The experts are smaller individually, but having more of them allows finer-grained specialization. Qwen3.5 similarly uses 256 experts. This improves routing precision at the cost of increased routing overhead and more complex load balancing.

**Shared experts (DeepSeek):** Some experts are always active for every token, regardless of routing. DeepSeek-V3 has 1 shared expert plus 8 routed expert slots (from 255 non-shared experts). The shared expert handles common patterns; the routed experts handle specialization. This prevents the situation where every token's common syntactic needs must be redundantly learned by every expert.

**Alternating dense and MoE layers (Llama 4 Maverick):** Not every layer uses MoE. Maverick alternates dense attention layers with MoE MLP layers. Dense layers handle attention (which is already across all tokens and doesn't benefit from MoE the same way); MoE layers handle the feed-forward storage step.

### MoE weight file structure

In the weight files, MoE changes the structure of the MLP tensors. Instead of:
```
model.layers.0.mlp.gate_proj.weight    [14336, 4096]
```
you get:
```
model.layers.0.block_sparse_moe.gate.weight        [8, 4096]    ← router
model.layers.0.block_sparse_moe.experts.0.w1.weight [14336, 4096]  ← expert 0 gate
model.layers.0.block_sparse_moe.experts.0.w2.weight [4096, 14336]  ← expert 0 down
model.layers.0.block_sparse_moe.experts.0.w3.weight [14336, 4096]  ← expert 0 up
model.layers.0.block_sparse_moe.experts.1.w1.weight [14336, 4096]  ← expert 1 gate
... × 8 experts
```

The router is tiny (8 × 4096 = 32,768 parameters — negligible). The experts each contain the full MLP parameter set. The attention weights remain the same as in a dense model.

---

## Part 4: Training Output — What You Actually Get

### The checkpoint

During training, the framework saves **checkpoints** at regular intervals — complete snapshots of all parameter states at that point. A checkpoint for a 7B model in bfloat16 is approximately 14 GB. Checkpoints allow training to resume after interruption and provide rollback points if a later training phase degrades quality.

For LoRA fine-tuning, the checkpoint contains only the adapter weights — the low-rank matrices A and B for each targeted layer. A LoRA adapter checkpoint for a 7B model at r=16 targeting all linear layers is approximately 150–300 MB regardless of the base model size. This is the key practical advantage: you can store and distribute many domain adapters cheaply.

### The merged model

For deployment, the LoRA adapter weights are merged back into the base model weights: `W_final = W_base + B × A`. The result is a standard dense model with no adapter overhead at inference. The merged model is the same size as the original base model — it doesn't grow. The adapter was only needed during training; once merged, there is no runtime cost.

### GGUF: the deployment format

GGUF (GPT-Generated Unified Format) is the standard format for local model deployment, introduced by the llama.cpp project to replace the earlier GGML format. A GGUF file is a single binary file containing:

- **A header** with model metadata: architecture name (llama, mistral, qwen2, etc.), layer count, attention head count, context length, tokenizer vocabulary, and special token IDs
- **The tokenizer** — the vocabulary and merge rules for the BPE tokenizer, embedded directly in the file
- **All tensor data** — every weight tensor for every layer, stored contiguously, with quantization applied

GGUF supports multiple quantization levels, named by convention:

| Format | Bits per weight | Size (7B model) | Notes |
|--------|----------------|----------------|-------|
| F32 | 32 | ~28 GB | Full precision; training only |
| F16 / BF16 | 16 | ~14 GB | Half precision; fast on GPU |
| Q8_0 | 8 | ~7 GB | Near-lossless; good quality floor |
| Q6_K | 6 | ~5.5 GB | Excellent quality/size tradeoff |
| Q5_K_M | 5 | ~4.8 GB | Very good; recommended for 16GB VRAM |
| Q4_K_M | 4 | ~4.1 GB | Standard local deployment choice |
| Q3_K_M | 3 | ~3.2 GB | Noticeable quality degradation |
| Q2_K | 2 | ~2.7 GB | Significant degradation; use only if forced |
| IQ4_XS | ~4 (imatrix) | ~3.9 GB | Importance-matrix quantization; better than Q4_K_M at same size |

The `_K` suffix denotes k-quants — a more sophisticated quantization scheme that applies different precision to different tensors based on their sensitivity. Attention projection weights get higher precision than less sensitive layers. The `_M` suffix (medium) denotes a specific k-quant variant. `IQ` formats use an "importance matrix" computed from calibration data to allocate precision where it matters most.

**For the network engineer specialist deployment:** Q4_K_M is the standard recommendation — approximately 4.1 GB on disk, runs at 18–28 tokens/second on M3/M4 Pro. Q5_K_M is worth the extra ~700 MB if command accuracy on edge cases is critical.

### MoE in GGUF

MoE models in GGUF are handled transparently by the format — the expert tensors are stored individually and the routing logic is encoded in the architecture metadata. The inference engine (llama.cpp) knows from the architecture name (e.g., `mixtral`) to apply MoE routing during the forward pass. A Q4_K_M GGUF of Mixtral 8x7B is approximately 26 GB — all 46.7B parameters are on disk, but only ~12.9B are activated per forward pass. For Llama 4 Scout (109B total, 17B active), Q4_K_M is approximately 55 GB.

---

## Part 5: Model Serving — From Query to Output

### What a model server does

Ollama, llama.cpp, vLLM, and similar tools all do the same fundamental job: load the GGUF (or equivalent format) into memory, accept text queries over an API, run the forward pass to generate tokens, and return the result. But the details matter significantly for performance and behavior.

### Loading and memory layout

On startup, the model server reads the GGUF file and loads the tensor data into memory. The key decision is where each tensor lives:

**GPU VRAM:** Fastest. Matrix multiplications on GPU are 10–50× faster than CPU for large matrices. Goal: put as many layers as possible here.

**CPU RAM / unified memory:** Slower. For Apple Silicon (unified memory), CPU and GPU share the same physical memory pool — there is no PCIe transfer bottleneck. A 32 GB M4 Mac Mini effectively has 32 GB of GPU-accessible memory. For discrete NVIDIA GPUs, anything that doesn't fit in VRAM must live in system RAM and be paged in over PCIe as needed, which is dramatically slower.

**Disk:** Only as a last resort (memory-mapped files). Practical only for very fast NVMe SSDs, and still far slower than RAM.

Llama.cpp uses the `--n-gpu-layers` parameter to control how many transformer layers are offloaded to GPU. For full GPU execution on a machine with sufficient memory, set `--n-gpu-layers 99` (loads all layers). For partial GPU execution on memory-constrained hardware, a split is possible — say 20 of 32 layers on GPU, 12 on CPU — but cross-device transfers at each layer boundary create overhead.

### The inference loop

Once loaded, the server processes a query in two phases:

**Prefill (prompt processing):** All prompt tokens are processed in parallel. The transformer runs one forward pass with the entire prompt sequence, computing all attention scores and populating the KV cache for every prompt token. This is fast — modern hardware can process thousands of tokens in a fraction of a second on GPU because the computation is parallelizable across tokens.

**Decode (generation):** One token at a time. The model reads the KV cache for all prior tokens, runs the forward pass for the new token, produces the probability distribution, samples a token, adds it to the KV cache, and repeats. This is fundamentally sequential and cannot be parallelized across tokens. Generation speed (tokens/second) is determined by how fast one forward pass can execute — primarily limited by memory bandwidth, not compute throughput. Moving all those weight tensors from memory to compute units is the bottleneck, not the matrix multiplications themselves.

This is why "memory bandwidth" is more important than "FLOPS" for LLM inference at small batch sizes. An M4 Max has ~400 GB/s unified memory bandwidth; an NVIDIA A100 has 2 TB/s HBM bandwidth. The A100 generates tokens approximately 5× faster than the M4 Max on a 7B model despite not having proportionally more FLOPS.

### Batching

When multiple queries arrive simultaneously, the server can batch them — process multiple decode steps in parallel across queries. This improves GPU utilization significantly (one large matrix multiply across N queries is more efficient than N small ones) but requires all queries in the batch to take a step simultaneously, which is complicated by different sequence lengths and generation states.

**Continuous batching** (used by vLLM and modern serving systems) dynamically adds and removes requests from the active batch as they arrive and complete, maximizing GPU utilization. This is the core technique enabling production LLM serving at scale. For local single-user deployment (Ollama on a Mac), batching is not relevant — you're always one query at a time.

### How MoE serving differs

MoE changes the memory access pattern during inference in a way that creates unique serving challenges:

**All expert weights must be in memory.** Even though only 2 of 8 experts are activated per token, all 8 sets of expert weights must be loaded into memory because any expert might be selected at any time. You cannot predict which expert a given token will route to before running the router. Mixtral 8x7B requires ~26 GB in Q4 just to be loaded — the full 46.7B parameters — even though only 12.9B compute per forward pass.

**Irregular memory access pattern.** For a batch of tokens, different tokens route to different experts. If token A routes to experts {2, 5} and token B routes to experts {1, 7}, the compute operations are on different weight tensors. This means the GPU must jump around its memory space rather than streaming through contiguous data — poor cache utilization. Dense models have perfectly regular, cache-friendly memory access; MoE models are inherently less regular.

**Expert parallelism for large MoE.** For serving very large MoE models (DeepSeek V3 at 671B total parameters), a single GPU can't hold all expert weights. Expert parallelism distributes different experts to different GPUs. When a token routes to expert 3 on GPU-2, the activation is sent to GPU-2, the expert computes, and the result is sent back. This works but adds communication overhead proportional to the routing decisions. It's why DeepSeek's MLA (Multi-head Latent Attention) design compresses the KV cache — reducing communication cost in multi-GPU setups was a key design motivation.

**Practical consequence for local deployment:** For the network engineer specialist use case on a Mac laptop, avoid large MoE models. Mixtral 8x7B at 26 GB is at the edge of what a 32 GB Mac Mini can serve (leaving little room for KV cache). Llama 4 Scout at ~55 GB Q4 requires a 64 GB machine. Dense models in the 7B–14B range are far better suited to edge deployment — predictable memory layout, fully cacheable weights, no routing overhead.

### Speculative decoding

A newer inference optimization worth knowing: **speculative decoding** uses a small "draft" model to predict several tokens ahead, then verifies them all in one forward pass of the main model. If the draft was right, you get multiple tokens for roughly the cost of one forward pass. If wrong, you discard and fall back.

For a network expert model, a 1B or 3B model fine-tuned on the same domain makes an excellent draft model — it will correctly predict common CLI command completions (the continuation of `show bgp` is almost always `summary` or `neighbor`, and a small model can predict that confidently). Ollama supports speculative decoding via the `--draft-model` parameter. This can improve throughput by 1.5–3× on coherent, predictable domains like CLI commands — exactly the use case here.

---

## Putting It Together: What Happens When You Query the Network Expert

A complete trace of a single query through the full stack:

```
User types: "Show me the OSPF neighbor state on this router"

1. [Ollama API] Receives HTTP POST to /api/chat
   Looks up model name → loads Modelfile → identifies GGUF path

2. [llama.cpp engine] Tokenizes the prompt:
   ["Show", " me", " the", " OSPF", " neighbor", " state", 
    " on", " this", " router"]  → [4888, 757, 279, 3585, 15048, 
                                    1614, 389, 420, 9606]
   Prepends system prompt tokens from Modelfile
   Total prompt: ~120 tokens

3. [Prefill phase] All 120 tokens processed in one forward pass:
   - Each token looked up in embedding table → 120 × 4096 vectors
   - Through all 32 transformer layers
     - Attention: all tokens attend to all prior tokens (parallelized)
     - MLP: each token's vector passes through feed-forward network
     - KV tensors for all 120 tokens stored in KV cache
   - Duration: ~50-100ms on M3/M4 Pro

4. [Decode phase] Generate output tokens one at a time:
   Token 1: forward pass → logits → sample → "show"      (40ms)
   Token 2: forward pass → logits → sample → " ospf"     (40ms)  
   Token 3: forward pass → logits → sample → " neighbor" (40ms)
   ...continues for ~15 tokens total

5. [Output] Streamed back to client token by token as they generate
   Final response: "show ospf neighbor\n\nFor detailed output..."
   Total generation: ~600ms at 25 tokens/second
```

For a MoE model (e.g., Mistral Small 4), step 4 would additionally include:
```
   At each MLP layer:
   - Router runs: token representation → 8 expert scores
   - Top-2 selected: say experts 4 and 7
   - Expert 4 MLP computes: token_repr × expert_4_weights
   - Expert 7 MLP computes: token_repr × expert_7_weights
   - Outputs weighted and summed
   - Experts 0,1,2,3,5,6 weights are in memory but not accessed this step
```

The routing decision is different for every token and every layer — "show" routes differently than "ospf" routes differently than "neighbor", potentially hitting different expert specializations across all 32 layers, 2 experts per layer = up to 64 expert activations per output token.

## Sources

- [Attention Is All You Need (Vaswani et al. 2017)](https://arxiv.org/abs/1706.03762) — original transformer paper
- [Switch Transformers (Fedus et al. 2021)](https://arxiv.org/abs/2101.03961) — foundational MoE for LLMs paper
- [DeepSeek-V2 technical report (2024)](https://arxiv.org/abs/2405.04434) — MLA and fine-grained MoE detail
- [llama.cpp project](https://github.com/ggerganov/llama.cpp) — inference engine and GGUF format reference
- [GGUF format specification](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md)
- [vLLM: continuous batching and PagedAttention](https://arxiv.org/abs/2309.06180)
