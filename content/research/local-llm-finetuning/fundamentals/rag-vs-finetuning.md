---
title: "RAG vs. Fine-Tuning: Choosing the Right Approach"
date: 2026-06-10
lastmod: 2026-06-10
draft: false
description: "When to use retrieval-augmented generation vs. fine-tuning to adapt an LLM for a specialist domain — and how the two approaches combine for a network engineer expert model that needs both current device knowledge and deep CLI intuition."
research_area: "local-llm-finetuning/fundamentals"
source_urls:
  - "https://arxiv.org/abs/2005.11401"
  - "https://arxiv.org/abs/2312.10997"
  - "https://www.pinecone.io/learn/retrieval-augmented-generation/"
last_reviewed: 2026-06-10
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

RAG (Retrieval-Augmented Generation) and fine-tuning are the two primary ways to make a general-purpose LLM useful in a specific domain. They solve different problems: fine-tuning changes what a model *knows how to do* (its skills, reasoning patterns, and domain fluency); RAG changes what a model *has access to* at query time (current facts, specific documents, live data). For a network engineer specialist model, the distinction matters practically: the model needs fine-tuning to speak JunOS and IOS fluently and reason through diagnostic workflows — but it may also benefit from RAG to access the current running configuration of a specific device it's been asked to troubleshoot.

## Key Facts

- **Fine-tuning** modifies model weights to encode skills, patterns, and domain fluency
- **RAG** retrieves relevant text at query time and injects it into the prompt — weights unchanged
- **Neither is always better** — the right choice depends on what type of knowledge is needed
- **They compose:** a fine-tuned model can also use RAG; the approaches are not mutually exclusive
- **For the network expert model:** fine-tuning is the primary investment; targeted RAG is a useful augmentation for device-specific context

---

## How RAG Works

RAG was formally introduced by Lewis et al. (Facebook AI Research, 2020) as a method to give language models access to an external knowledge store without retraining. The mechanism:

1. **Index:** A corpus of documents (vendor docs, config files, runbooks) is split into chunks and converted into vector embeddings using an embedding model. These embeddings are stored in a vector database (Chroma, FAISS, Qdrant, pgvector).
2. **Retrieve:** When a query arrives, it is embedded the same way and compared against the stored vectors. The top-k most semantically similar chunks are retrieved.
3. **Augment:** The retrieved chunks are prepended to the prompt: "Given the following context: [retrieved text], answer: [user question]."
4. **Generate:** The model answers using both its parametric knowledge (weights) and the retrieved context.

The model's weights are never modified. Adding new documents to the index is instant — no training required. Removing or updating documents is equally immediate.

**What RAG is good at:**
- Keeping the model current without retraining (add new firmware release notes to the index, done)
- Grounding responses in specific authoritative documents (the answer cites the exact Juniper TechLibrary page)
- Reducing hallucination on factual lookups where the answer is explicitly in a document
- Accessing private or proprietary information that was never in training data (internal runbooks, your organization's specific topology docs)
- Variable knowledge requirements — different deployments need access to different document sets

**Where RAG falls short:**
- It cannot teach the model a new skill. Retrieving a page about JunOS commit syntax does not make the model better at writing JunOS config — it gives the model the text to read at query time, but whether it uses that text correctly depends entirely on the base model's existing capabilities.
- Retrieved context competes with the model's own knowledge in the context window. If the retrieved chunk is noisy or partially irrelevant, it can degrade answer quality.
- For long troubleshooting sessions that accumulate many turns of context, RAG retrieval can push earlier conversation history out of the context window.
- Retrieval quality gates answer quality: if the vector search returns the wrong chunk, the model confidently uses wrong information. Embedding-based retrieval struggles with highly technical queries where the vocabulary is precise and specialized (e.g., "why does `rpd` log a NOTIFICATION message when the BGP session resets" is a specific enough query that a general embedding model may not find the right document).
- Latency: a round-trip to the vector database and embedding lookup adds 50–500ms per query. Negligible for interactive use but relevant for high-frequency agentic loops.

---

## How Fine-Tuning Compares

Fine-tuning encodes knowledge and skills directly into the model's weights through continued training. The model does not look anything up at inference time — it draws on what its weights learned.

**What fine-tuning is good at:**
- Teaching the model a new skill or reasoning pattern — not just facts, but *how to think* about a domain
- Domain vocabulary and syntax: after fine-tuning on JunOS examples, the model generates `set protocols bgp group external-peers neighbor` without needing to be shown a reference — it's internalized the pattern
- Response format and style: fine-tuning trains the model to respond like an expert engineer rather than a generic assistant — giving commands in the right mode, flagging destructive operations, explaining the why behind each step
- Troubleshooting reasoning chains: a fine-tuned model learns the diagnostic decision tree for "OSPF neighbor stuck in EXSTART" through exposure to many resolved examples; it doesn't retrieve a document about it, it has internalized the pattern
- No retrieval latency or failure modes at inference — the skill is always there, no database required
- Works fully disconnected — critical for the edge deployment use case

**Where fine-tuning falls short:**
- Static knowledge. The training data has a cutoff. If Juniper ships a new platform (PTX10008 with a new linec ard) after the training data was collected, the model has no knowledge of it unless retrained.
- Cannot inject proprietary real-time state. The running configuration of a specific device — its current IP assignments, BGP peer list, active filters — is not in the training data. The model can reason about configuration in general but cannot reason about *your* specific device without that context being provided somehow.
- Retraining cost. Adding new knowledge requires a new fine-tuning run, which takes hours and some compute budget. It's practical to do quarterly or for major new platform support, but not for keeping up with daily changes.
- Risk of encoding incorrect information. If the training data contains wrong commands, the model learns them. RAG-based approaches surface the source document so errors are auditable.

---

## The Core Tradeoff: Skills vs. Facts

The most useful mental model for choosing between RAG and fine-tuning:

**Fine-tuning is for skills.** The network expert model needs to *know how to* translate English intent into JunOS syntax, *know how to* read a BGP summary and identify a stuck session, *know how to* structure a troubleshooting workflow from symptom to root cause. These are procedural and reasoning capabilities. They cannot be retrieved from a document — they have to be trained in.

**RAG is for facts.** The current running configuration of `router1.dc1`. The content of a specific Juniper advisory bulletin. The list of interfaces on a switch you're being asked to troubleshoot. The IP addressing scheme for your organization's network. These are factual lookups. The model doesn't need to have them memorized — it needs them in context at query time.

A useful test: *If the relevant information appeared verbatim in the prompt, would the model be able to use it correctly?* If yes, RAG can deliver that information. If no — if the model doesn't have the underlying skill to reason with the information even when given it — fine-tuning is what's needed.

For example: pasting a block of `show ospf neighbor` output into a conversation with a base Llama 3.1 8B model will get a reasonable response, because the base model already has enough OSPF vocabulary to parse it. But asking that same base model to generate a complete multi-area OSPF configuration with area types, authentication, and route summarization will produce plausible-but-wrong JunOS — it doesn't have the JunOS configuration syntax skill. Fine-tuning adds that skill.

---

## Applied to the Network Engineer Specialist

The network expert model is primarily a **fine-tuning problem**, with specific **RAG augmentations** that add high value at low cost.

### Why fine-tuning is the primary investment

The core value of the network expert model is *skills*:

- JunOS and IOS CLI fluency — correct syntax across dozens of command families
- Troubleshooting methodology — the structured diagnostic approach that a senior engineer applies
- Platform awareness — knowing that `show ip ospf neighbor` is IOS but `show ospf neighbor` is JunOS, and never mixing them
- Output interpretation — reading `show interfaces` counters and knowing which error types matter
- Operational discipline — flagging `commit confirmed 5` before applying changes, noting when a command is service-affecting

None of these can be retrieved. They must be trained in. A base model given a JunOS command reference page via RAG will still produce IOS syntax if it hasn't been fine-tuned — it doesn't know how to *use* the reference correctly because it doesn't have the underlying skill.

### Where RAG adds value for the network expert

**Device-specific context.** The most immediate RAG use case: before a troubleshooting session, retrieve the device's current running configuration and inject it into the context window. The fine-tuned model can then reason about *this specific device* — "your BGP peer 10.0.0.1 is configured with a route-map that filters /24s, which may explain why you're seeing 0 prefixes received."

```
[System context from RAG]:
Device: router1.dc1 (Juniper MX204)
Running config excerpt — BGP section:
  group upstream-provider {
    type external;
    neighbor 192.0.2.1 {
      peer-as 65001;
      import bgp-import-strict;
    }
  }
  policy-options {
    policy-statement bgp-import-strict {
      term reject-default { from route-filter 0.0.0.0/0 exact; then reject; }
      term accept-long-prefixes { from route-filter 0.0.0.0/0 prefix-length-range /25-/32; then reject; }
      term accept { then accept; }
    }
  }

[User]: Why am I only seeing 3 prefixes from my upstream when they say they're sending 12?
```

With this context injected, the fine-tuned model can immediately identify that `bgp-import-strict` is rejecting /25–/32 prefixes and the default route — without the running config in context, it could only ask general diagnostic questions.

**Vendor advisories and release notes.** A Juniper PSN (Problem Support Notice) or Cisco Field Notice describing a bug in a specific software version is high-value, time-sensitive content that won't be in the training data. Adding these to a RAG index means the model can flag "this symptom matches Juniper PR 1234567 — there's a known bug in JunOS 22.3R1 for this scenario" — grounded in the actual advisory document.

**Internal runbooks and SOPs.** Organization-specific procedures (change management templates, escalation paths, site-specific topology notes) are never in training data. RAG makes them accessible without any retraining.

**Firmware and platform compatibility matrices.** "What's the minimum JunOS version that supports EVPN Type-5 routes on QFX5120?" is a factual lookup that RAG handles better than fine-tuning — the answer may change with each new software release.

### What RAG *cannot* substitute for here

RAG cannot fix a base model that doesn't speak JunOS. Giving a model a page from the Juniper CLI reference doesn't make it produce correct JunOS configuration — it produces text that references the document but still applies IOS patterns. The model must have the underlying syntax skill from fine-tuning. This is the key failure mode to watch for when evaluating whether to invest in fine-tuning vs. just building a RAG pipeline on top of a base model.

Similarly, the troubleshooting methodology — the step-by-step diagnostic reasoning that characterizes a senior engineer — cannot be retrieved. It's a skill that emerges from fine-tuning on many resolved troubleshooting sessions.

---

## Practical Architecture for the Network Expert Model

The recommended architecture combines fine-tuning as the foundation with targeted RAG for device-specific context:

```
[Query arrives]
       │
       ▼
[RAG retrieval layer]
  - Vector search against: device running configs,
    vendor advisories, internal runbooks
  - Top-3 most relevant chunks retrieved
  - Injected into system context
       │
       ▼
[Fine-tuned model inference]
  - Llama 3.1 8B Instruct + JunOS domain adapter
  - Draws on: trained CLI skills, troubleshooting
    patterns, platform knowledge (from fine-tuning)
    + device-specific facts (from RAG context)
       │
       ▼
[Human review → optional device execution]
  - Proposed commands reviewed before execution
  - Output fed back into conversation
```

**Implementation:** For the disconnected Mac laptop deployment, a local vector database is straightforward to run. ChromaDB is a pure-Python embedded vector store with no server process — it runs in-process alongside the inference call. Ollama serves the model; ChromaDB provides the retrieval; a small Python script coordinates the two.

```python
import chromadb
from chromadb.utils.embedding_functions import OllamaEmbeddingFunction

# Initialize local ChromaDB (persists to disk)
client = chromadb.PersistentClient(path="./network-knowledge-base")

# Use a small local embedding model (nomic-embed-text via Ollama)
embed_fn = OllamaEmbeddingFunction(
    url="http://localhost:11434/api/embeddings",
    model_name="nomic-embed-text"
)

collection = client.get_or_create_collection(
    name="device-configs",
    embedding_function=embed_fn
)

# Index device configuration (run once per device config update)
def index_device_config(hostname: str, config_text: str):
    # Split config into sections (each stanza is a chunk)
    chunks = split_junos_config(config_text)
    collection.upsert(
        documents=chunks,
        ids=[f"{hostname}-chunk-{i}" for i, _ in enumerate(chunks)],
        metadatas=[{"hostname": hostname} for _ in chunks]
    )

# Retrieve relevant context before each query
def retrieve_context(query: str, hostname: str, n_results: int = 3) -> str:
    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        where={"hostname": hostname}
    )
    if results["documents"]:
        return "\n\n".join(results["documents"][0])
    return ""
```

**Embedding model for technical content.** Standard embedding models (OpenAI text-embedding-ada, sentence-transformers) are trained on general web text and perform poorly on highly technical CLI queries. For network content, `nomic-embed-text` (runs locally via Ollama, 137M parameters) performs adequately. For higher retrieval precision, fine-tuning an embedding model on network documentation is a separate project worth pursuing if retrieval precision proves to be the bottleneck.

---

## Decision Matrix

| Scenario | RAG | Fine-tune | Notes |
|----------|-----|-----------|-------|
| Model needs JunOS CLI syntax skills | ✗ | ✓ | Skills must be trained; cannot be retrieved |
| Model needs to know this device's current config | ✓ | ✗ | Device state changes; RAG delivers current state |
| Model needs step-by-step troubleshooting methodology | ✗ | ✓ | Procedural skill; must be trained |
| Model needs current Juniper software release notes | ✓ | ✗ | Time-sensitive facts; add to index as published |
| Model needs to flag a known platform bug | ✓ | ✗ | PSN/advisory content; index vendor bulletins |
| Model needs to know org-specific IP addressing | ✓ | ✗ | Private data; fine-tuning would expose it to model |
| Model is producing IOS syntax for JunOS questions | ✗ | ✓ | Platform confusion is a skill gap; requires training |
| Model doesn't know what changed in JunOS 23.4R2 | ✓ | ✗ | Release notes in the index |
| Model cannot interpret `show chassis fpc` output | ✗ | ✓ | Output interpretation is a skill |

## Sources

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (Lewis et al. 2020)](https://arxiv.org/abs/2005.11401) — original RAG paper
- [Retrieval-Augmented Generation for Large Language Models: A Survey (Gao et al. 2023)](https://arxiv.org/abs/2312.10997) — comprehensive survey of RAG methods
- [ChromaDB documentation](https://docs.trychroma.com/) — local embedded vector database
- [nomic-embed-text (Ollama)](https://ollama.com/library/nomic-embed-text) — local embedding model for RAG
- [Pinecone RAG explainer](https://www.pinecone.io/learn/retrieval-augmented-generation/) — accessible overview of RAG architecture
