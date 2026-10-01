# notsointresting/awesome-jev-family
- **One-liner:** An awesome list of Jev-*like* decision models: open replicas, local runtimes and ports, SDKs, calibration benchmarks and architecture discussions. It covers the models, not the apps that use them.
- **Language(s):** English
- **Type:** curated-list (focused on open alternatives)
- **Scale:** 78 entries in 5 categories: Open Alternatives & Replicas (21), Ports & Local Runtimes (7), SDKs & Integrations (23), Benchmarks & Calibration (14), Related Practices & Discussions (13). The README is regenerated from the category files by `scripts/build_readme.py`.
- **Quality flags:** Clear inclusion criteria, plus a strong "listing is not endorsement" warning and an adoption checklist (are the weights downloadable and licensed, is there a runnable check, are numbers sourced, is calibration fitted in-distribution). Numbers are quoted, not re-measured. Several entries are X posts. Some self-reported claims are bold (openJev-verdict-2.0 "beats Jev and Laya"). No obvious fabrication; small and focused.
- **Unique value:** The best map in this batch of the **open System-One model family**, with parameter counts, latencies and parity numbers. It also has an **architecture-inference discussion** section (archerhume "Architecture Unmasked" from ~10K API calls, the "it's the inference technique" argument), edge deployment (ESP32), and SQL-engine integrations (sqlite-jev, duckdb-jev, jevql).

## Facts claimed about Jev
- Launch post: typesafe.ai/blog/introducing-system-one-models-and-jev.
- Shape: unstructured state plus a typed question (choice/score/noul), returning a typed decision with confidence in a single forward pass with no generated text.
- Architecture inference (archerhume.com): from ~10,000 API calls, "keeps LLM knowledge but removes token generation entirely". @anderslie argues the speed comes from **parallel decoding, not training**.
- `typesafe-ai/system-one-adapter-python` is TypeSafe's official open-source drop-in adapter for running and benchmarking System One decisions.
- Comparisons to open models (self-reported by each project):
  - **Laya**: 421M English / 322M multilingual / 421M typed-decisions checkpoints, Apache-2.0, ~33 ms single forward pass, 100+ languages, trained with RLCD proper-scoring-rule rewards. laya-mlx: 13.4 ms median (7.4 ms multilingual), 63/63 parity.
  - **kev**: 0.8B/4B/9B Qwen3.5 LoRA plus pointer head, exposes `POST /v1/systemone`, so TypeSafe's SDK can point at a local server.
  - **Bespoke Nimble-9B**: 90.1% reference-label agreement on 324 held-out examples against Jev.
  - **SemIf** (formerly OpenJev): 0.845 modal agreement with Jev.
  - **von**: 395M, <15 ms. **minojev**: 547k params, 2–255 candidates. **CUA-S1-FORMS**: 706,048 params, 99.7% on its own form eval, one 50 ms pass vs an LLM agent's 23 turns / 39.6 s.
  - **poorjev**: NLI models plus temperature scaling and conformal abstention, ECE 0.170 → 0.071.
- A public System-One-shaped API backed by open Qwen3.6-35B-A3B (ekzhang).
- Spanish audit (jev-acento): a Spanish `state` costs accuracy and roughly **doubles ECE** on XNLI and PAWS-X (3,200 human-labelled items).
- jev-orderby-bench: a DuckDB extension's default **row-batching fails** the ranking gate, while one row per request passes.
- LangChain blog: the decision model is a cheaper and more consistent judge for online evals.

## Key insights / patterns
- Many replicas use the same recipe: **read the option-token logits of an open LLM in one forward pass** (SemIf, mini-jev, LitJev), or train a LoRA plus a decision/pointer head (kev, Nimble, Luce), then fit a temperature on a dev set. Warning: in-distribution temperature fits can still be dishonest on your data.
- **Drop-in compatibility**: many serve `/v1/systemone`, so the official SDK can be pointed at them (kev, jev-local, LitJev, FastJev, jeff).
- **Specialist tiny models** can beat general models on home turf (CUA-S1-FORMS). Check the license of the weights, not only the code.
- Non-English state can hurt calibration (Spanish study). Batching rows in SQL extensions can break ranking fidelity.
- SDK design ideas: **hysteresis enter/exit thresholds** (huncho), **offline lint rules for question sets** (jevkit, 13 rules), typed branches where anything below the threshold must be handled (discern), and `decide` as a first-class inference type next to generate/stream (juspay/neurolink).
- Per-question threshold fitting with CI regression (jevcal) is a recurring best practice.
- Framing (cocktailpeanut): the novelty is that arbitrary classification becomes a **runtime-defined, type-safe programmable primitive**. HN discussion proposes Noul as a general software primitive.

## Standout entries
- [Laya](https://github.com/NandhaKishorM/laya) — leading Apache-2.0 open System One model (open model)
- [kev](https://github.com/jaredpalmer/kev) — trainable 0.8B/4B/9B replica with `/v1/systemone` (open model)
- [Nimble](https://github.com/bespokelabsai/nimble) — Bespoke Labs open recipe and model (open model)
- [SemIf](https://github.com/TheoLeeCJ/SemIf) — logit-readout interface on frozen models, WebGPU (open model)
- [Luce](https://github.com/scienthoon/luce) — describe a task, then train your own decision head (open recipe)
- [laya-mlx](https://github.com/mizorewww/laya-mlx) — Apple Silicon runtime (runtime)
- [FastJev](https://github.com/chengyongru/fastjev) — self-hosted multi-backend System One API (runtime)
- [CUA-S1-FORMS](https://huggingface.co/cua-ai/cua-s1-forms) — 706K-param form-filling specialist (open model)
- [Jev's Architecture Unmasked](https://archerhume.com/posts/jevs-architecture-unmasked) — architecture inferred from ~10K calls (analysis)
- [jev-acento](https://github.com/marcosmartinez/jev-acento) — Spanish calibration audit (benchmark)
- [jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench) — SQL ranking over probabilities (benchmark)
- [Jevals.com](https://jevals.com/) — independent leaderboard (benchmark)
- [jevkit](https://github.com/ariel-frischer/jevkit) — offline question-set linter (tool)
- [sqlite-jev](https://github.com/mgaitan/sqlite-jev) — Jev as SQL functions (integration)
- [Ask HN: Noul as a decision primitive](https://news.ycombinator.com/item?id=49760225) — discussion (community)
