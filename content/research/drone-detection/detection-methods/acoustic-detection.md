---
title: "Acoustic Detection"
date: 2026-06-05
lastmod: 2026-11-12
draft: false
description: "Acoustic drone detection using microphone arrays and machine learning analysis of motor and rotor noise signatures — detects RF-dark and fiber-optic drones; limited range; strong bird discrimination."
research_area: "drone-detection/detection-methods"
source_urls:
  - "https://acta-acustica.edpsciences.org/articles/aacus/full_html/2026/01/aacus250134/aacus250134.html"
  - "https://www.idmt.fraunhofer.de/en/Press_and_Media/press_releases/2025/acoustic-drone-detection.html"
  - "https://arxiv.org/html/2509.04715v1"
  - "https://drone-warfare.com/counter-uas/acoustic-detection/"
last_reviewed: 2026-11-12
stale_after_days: 180
---

> **⚠ Disclaimer:** This entry may be incomplete, out of date, or inaccurate. It is AI-maintained on a best-effort basis. Do not rely on it as a sole source — verify claims independently using the sources listed below.

## Summary

Acoustic detection exploits the noise produced by drone propellers, motors, and mechanical vibrations to detect and classify drones. Unlike RF detection, it works against fiber-optic tethered and pre-programmed autonomous drones. Unlike radar, it requires no RF emissions and is passive. Practical range is limited to tens to a few hundred meters depending on ambient noise and drone size (Fraunhofer IDMT cites 50–200 m), making acoustic detection most useful as a close-in layer within a multi-sensor stack. Machine learning classifiers achieve strong drone-vs-bird discrimination on known drone types.

## Key Facts

- **Type:** Passive sensor; detects acoustic emissions from motors/rotors
- **Effective range:** about 50–200 m typical (Fraunhofer IDMT); the Acta Acustica MEMS prototype reached about 50–60 m; vendors claim 300–500 m (Robin Radar and Drone Warfare; vendor claims, not independently verified)
- **Bird discrimination:** Strong — periodic blade tone vs. irregular wingbeat; CNNs on Mel-spectrograms are widely used for bird separation in recent literature
- **Works against:** RF-dark, fiber-optic, autonomous waypoint drones — any drone that flies with a propulsion system
- **Key limitation:** Useless in high-ambient-noise environments (wind >15 mph, urban/industrial settings, heavy rain)
- **Hardware cost:** Low (unverified estimate) — MEMS microphone arrays on Raspberry Pi or similar embedded hardware; well-suited for fixed site perimeter

## What It Is / How It Works

Drones produce acoustic signatures through two primary mechanisms: (1) periodic tones from blade passage and motor rotation at harmonics of the RPM frequency, typically 50–400 Hz for the fundamental and multiple harmonics into the kHz range; and (2) broadband aerodynamic noise from turbulent airflow over the blades.

Detection systems capture audio (typically at 16–44 kHz sample rates), convert it to time-frequency representations (Mel-spectrograms or MFCC — Mel-frequency cepstral coefficients), and apply a classifier to distinguish drone vs. no-drone, and to classify the specific drone type.

**Classification architectures in current use:**
- **CNN on Mel-spectrograms:** Convolutional neural networks treating the spectrogram as an image. High accuracy; requires GPU for training; can run inference on Raspberry Pi at reduced model size.
- **Random Forest on MFCC features:** Chosen by recent MEMS-array research (Acta Acustica 2026) as the best embedded-system trade-off between performance and interpretability. Can run on a Raspberry Pi 4.
- **RF + acoustic fusion (deep neural network):** Research systems combine acoustic and RF features; reported accuracy gains are study-specific and are not reproduced here.

**Drone-vs-bird discrimination:**
Bird wingbeats are aperiodic and occupy a different frequency range (typically 5–20 Hz wingbeat fundamental) than drone blade tones. Bird calls are distinct from motor harmonics. In practice, false positives from birds are low when the classifier is trained on local bird species. The main acoustic confusers are leaf blowers, lawnmowers, and other reciprocating machinery — all of which can produce harmonic signatures similar to a drone at distance.

**Microphone array geometry:**
Multiple microphones in a known spatial arrangement enable acoustic time-difference-of-arrival (TDOA) localization — triangulating drone position. The Acta Acustica 2026 prototype (8 INMP441 MEMS microphones, ESP32-S3 plus Raspberry Pi 4) localizes in 2D only, with 91.6% reported accuracy at about 50–60 m; 3D localization generally needs spatially distributed or tetrahedral arrays.

## Datasets Available for Development

- **Wang et al. 2025 Multiclass Acoustic Dataset:** 3,200 audio recordings from 32 distinct UAV types; 16,000 seconds total; spectrograms and MFCC plots included; described in the arXiv preprint
- **Fraunhofer IDMT datasets:** Fraunhofer Institute for Digital Media Technology (IDMT) has published acoustic drone detection research and datasets; see 2025 press release for current state.

## Open-Source Implementations

Acoustic drone detection has an accessible open-source ecosystem:
- **MEMS microphone array + Raspberry Pi + Random Forest:** Well-characterized in academic literature; no dominant single open-source project but the approach is reproducible from published papers.
- **GitHub audio classification projects:** Multiple YOLO + audio / CNN on spectrogram repositories listed under `drone-detection` on GitHub. Vary in quality; most target visual not acoustic.
- The approach is low-cost and buildable: MEMS microphones (roughly \$2–5 each, unverified estimate), a Raspberry Pi 4 (roughly \$75, unverified estimate), array geometry, and a trained model from published datasets.

## Limitations

- **Range:** Effective range drops sharply with ambient noise. Urban critical infrastructure (near roads, HVAC, generators) may limit range to 50–150 m (approximate).
- **Wind:** Wind noise above ~15 mph masks drone signatures at distance.
- **Small fixed-wing drones:** Electric fixed-wing drones with folding props are nearly silent at cruise — acoustic detection is unreliable.
- **Swarms:** Overlapping signatures from multiple drones degrade classification; active research area.

## Notable Developments

- **2026-04:** A U.S. Army publication (army.mil, April 30, 2026) discusses acoustic sensor networks used against drones in Ukraine.
- **2026-01:** Acta Acustica publishes the 8-microphone MEMS detection and 2D localization study.
- **2025:** Fraunhofer IDMT publishes work on reliable acoustic drone detection, citing ranges of 50–200 m.
- **2025:** Wang et al. release the 32-class multiclass acoustic dataset (arXiv preprint; ASTESJ December 2025).

## Key Organizations

- **Fraunhofer IDMT** (Germany) — acoustic drone detection research
- **Robin Radar** — radar vendor that publishes comparisons of acoustic and radar range
- **Wang et al.** — authors of the multiclass drone acoustic dataset
- **EDP Sciences (Acta Acustica)** — publisher of the 2026 MEMS array study

## Sources

- [Passive acoustic detection and localization — Acta Acustica 2026](https://acta-acustica.edpsciences.org/articles/aacus/full_html/2026/01/aacus250134/aacus250134.html) — 8-mic MEMS prototype, 2D, about 50–60 m
- [Reliable acoustic drone detection — Fraunhofer IDMT 2025](https://www.idmt.fraunhofer.de/en/Press_and_Media/press_releases/2025/acoustic-drone-detection.html)
- [Multiclass Acoustic Dataset and Interactive Tool — arXiv 2025](https://arxiv.org/html/2509.04715v1) — 32-class UAV audio dataset
- [Counter-UAS 101: Acoustic Detection — Drone Warfare](https://drone-warfare.com/counter-uas/acoustic-detection/)
