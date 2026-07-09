---
title: "Voicebox"
date: 2026-07-09
lastmod: 2026-07-09
draft: false
description: "Open-source, local-first AI voice studio: multi-engine voice cloning and TTS, Whisper-based dictation, and a built-in MCP server that gives AI coding agents a spoken voice."
research_area: "local-ai-tools"
source_urls:
  - "https://github.com/jamiepine/voicebox"
  - "https://voicebox.sh"
  - "https://github.com/jamiepine"
last_reviewed: 2026-07-09
stale_after_days: 90
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Voicebox is an open-source, local-first "AI voice studio" — a free desktop alternative to ElevenLabs (voice output) and WisprFlow (voice input) that runs the entire voice I/O stack on the user's own machine. It clones voices, generates speech across seven TTS engines, provides global system-wide dictation, and exposes a built-in MCP server so AI coding agents (Claude Code, Cursor, Cline) can speak back in a cloned voice.

## Key Facts

- **Developed by:** Jamie Pine (GitHub: `jamiepine`), also founder of Spacedrive Technology Inc.
- **Type:** Local application / studio (desktop voice AI)
- **Status:** Active — v0.5.0 latest release (Apr 25, 2026), 605+ commits
- **License:** MIT (fully open source)
- **Platform:** Tauri (Rust) desktop app — macOS (Apple Silicon MLX/Metal, Intel), Windows (CUDA/DirectML), Linux (build from source), Docker; also AMD ROCm and Intel Arc
- **Popularity:** 37.9k GitHub stars, 4.6k forks (as of 2026-07-09); voicebox.sh states 1M+ downloads
- **Monetization:** Free and open source ("free forever" per project site); optional paid cloud tier and a $VOICEBOX token on Solana exist alongside the core open-source app

## What It Is / How It Works

Voicebox frames itself as covering both halves of the "voice I/O loop" that cloud incumbents split between two products: ElevenLabs handles voice output (TTS/cloning) and WisprFlow handles voice input (dictation). Voicebox does both locally, bridging them with a small bundled local LLM (Qwen3, 0.6B/1.7B/4B) for transcript cleanup and per-voice "personalities."

**Voice cloning and TTS.** The app ships seven interchangeable TTS engines, selectable per-generation: Qwen3-TTS and Qwen CustomVoice (Alibaba), Chatterbox and Chatterbox Turbo (Resemble AI), LuxTTS (ZipVoice), TADA (Hume AI), and Kokoro (hexgrad, Apache 2.0). Coverage ranges from Kokoro's tiny 82M-parameter CPU-realtime model to Chatterbox Multilingual's 23-language support. Voice cloning works from as little as 3 seconds of reference audio; generation supports post-processing effects (pitch shift, reverb, compression, filters via Spotify's `pedalboard` library) and unlimited-length output through sentence-boundary auto-chunking with crossfade.

**Dictation and STT.** A global hotkey triggers push-to-talk or toggle dictation from anywhere on the OS; on macOS the transcript pastes directly into the focused text field via an accessibility-verified injection path. Transcription runs on OpenAI Whisper (Base through Large, plus a Turbo variant ~8x faster than Large) via MLX on Apple Silicon or PyTorch elsewhere. An optional local-LLM refinement pass cleans up filler words and false starts before paste.

**Agent voice output via MCP.** Voicebox bundles a Model Context Protocol server so any MCP-aware agent can call `voicebox.speak({ text, profile })` to talk back in a cloned voice — exposed as both an HTTP MCP endpoint and a stdio binary for clients that don't speak HTTP MCP. A per-client voice binding lets a user assign, for example, Claude Code to one voice profile and Cursor to another. The same underlying REST API (`/generate`, `/speak`, `/transcribe`, `/profiles`) is usable directly by scripts, games, or other apps without going through MCP at all.

**Tech stack:** Tauri/Rust desktop shell, React/TypeScript/Tailwind frontend, FastAPI (Python) backend, SQLite storage, FastMCP for the MCP server.

## Claim Verification

### Claim: LuxTTS runs "150x realtime on CPU" with ~1GB VRAM
**Status:** Partially verified

**Supporting sources:**
- [voicebox.sh](https://voicebox.sh) — states "Exceeds 150x realtime on CPU with ~1GB VRAM" for LuxTTS, consistent across the marketing site and GitHub README
- [GitHub README](https://github.com/jamiepine/voicebox) — repeats the same figure with the same VRAM footprint

**Refuting / questioning sources:**
- No independent third-party benchmark of LuxTTS/ZipVoice throughput was found in this session; the figure traces only to the project's own site and README, both controlled by the same team

**Summary:** The claim is consistent across the developer's own channels but has no independent confirmation; treat as a vendor-reported figure pending third-party benchmarking.

## Notable Developments

- **2026-04-25:** v0.5.0 released — latest tagged release as of this entry.
- **2026 (ongoing):** Project surpasses 37.9k GitHub stars and 1M+ downloads per voicebox.sh; covered by several independent YouTube walkthroughs comparing it to ElevenLabs.

## Key People

- **Jamie Pine** — creator and primary maintainer. Also founder of Spacedrive Technology Inc. (maker of the open-source Spacedrive file explorer) and Spacebot, an AI agent for teams. Based in Vancouver, BC.
  - GitHub: [jamiepine](https://github.com/jamiepine)
  - X: [@jamiepine](https://x.com/jamiepine)
  - Personal site: [jamiepine.com](https://jamiepine.com)
  - LinkedIn: not found

### People — Last Reviewed: 2026-07-09

## Sources

- [Voicebox GitHub repository](https://github.com/jamiepine/voicebox) — README, feature list, tech stack, license (MIT)
- [voicebox.sh](https://voicebox.sh) — official project site: features, download counts, pricing/cloud tier, token info
- [Jamie Pine's GitHub profile](https://github.com/jamiepine) — maintainer identity, affiliations, links
