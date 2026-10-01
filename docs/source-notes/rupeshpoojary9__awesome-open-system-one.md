# rupeshpoojary9/awesome-open-system-one
- **One-liner:** Small curated list of the *open* System One ecosystem: open Jev-like models, independent benchmarks, calibration/abstention tooling, and constrained-decoding libraries.
- **Language(s):** English
- **Type:** curated-list
- **Scale:** ~28 entries. Sections: What Is a System One Model; Open Models and Reproductions (12); Independent Benchmarks and Evaluations (4); Calibration and Selective Prediction (3); Constrained and Structured Decoding (5); Reference and Reading (4).
- **Quality flags:** Hand-curated, concise, lint workflow. First entry (poorjev) is the maintainer's own project (not disclosed as such). NanoJev is linked to `chenyangcun/NanoJev`, whereas every other list in this batch links `TianyuCodings/NanoJev` — possibly a fork/mirror or wrong link. Small; some overlap with other lists.
- **Unique value:** Only list that frames Jev within the broader technical lineage — conformal prediction (Angelopoulos & Bates, MAPIE), temperature scaling/ECE (Guo et al. 2017), constrained decoding (Outlines, XGrammar, Instructor, Guidance, LM Format Enforcer). Includes niche open System One models: Thai/English (OpenThai-SystemOne), Japanese (sokudan), audio-native (Prosodia).

## Facts claimed about Jev
- "System One models" is a term from TypeSafe's Jev launch, after Kahneman's System 1.
- Jev "is closed, hosted, and waitlisted".
- A System One model takes state + typed questions and returns, **in one parallel pass**, a typed answer per question with calibrated confidence; output schema-valid by construction.
- Open-model claims (author-reported): poorjev ECE 0.170 → 0.071; von sub-15 ms, non-autoregressive; Laya 421M, RLCD-trained, multilingual; OpenThai-SystemOne 0.8B with 256-way slot head (Apache-2.0); jevos 1B (MiniCPM5, 17 layers), GGUF, CPU-only, MIT; sokudan 314.6M ModernBERT-ja, bool AUROC 0.844 on bench_ja, "bool under-predicts true".

## Key insights / patterns
- The ingredients predate the name: zero-shot classification, calibrated probabilities, constrained decoding, conformal abstention — useful as fallbacks/alternatives and for evaluating Jev claims.
- Use conformal methods / MAPIE for principled "escalate when unsure" paths; calibrate thresholds and monitor drift (jevcal).
- Instructor/structured-output LLMs are the natural baseline to compare Jev against.
- Pre-registered independent evals on Banking77/CLINC150 are a recurring evaluation standard.

## Standout entries
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post (official)
- [System One (TypeSafe docs)](https://docs.typesafe.ai/concepts/system-one) — concept definition (official)
- [Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev) — LangChain walkthrough (tutorial)
- [On Calibration of Modern Neural Networks](https://arxiv.org/abs/1706.04599) — temperature scaling & ECE (paper)
- [conformal-prediction](https://github.com/aangelopoulos/conformal-prediction) — conformal prediction notes/notebooks (technique)
- [MAPIE](https://github.com/scikit-learn-contrib/MAPIE) — coverage-guaranteed prediction sets (technique)
- [Outlines](https://github.com/dottxt-ai/outlines) — constrained generation (technique)
- [jev-baselines-eval](https://github.com/ickma2311/jev-baselines-eval) — pre-registered Jev vs LLMs vs encoder on Banking77/CLINC150 (benchmark)
- [jev-eval](https://github.com/4esv/jev-eval) — Jev vs frontier LLM accuracy/calibration/latency/cost (benchmark)
- [OpenThai-SystemOne](https://github.com/iapp-technology/openthai-systemone) — Thai/English open System One model (open model)
- [sokudan](https://github.com/hiroki-abe-58/sokudan) — Japanese open System One model (open model)
- [Prosodia](https://github.com/alperiox/audio-jevlike) — audio-native System One model (open model)
- [Laya](https://laya.convaiinnovations.com/) — 421M RLCD-trained open decision engine (open model)
- [jevcal](https://github.com/abhixhek/jevcal) — threshold/drift tooling (tool)
