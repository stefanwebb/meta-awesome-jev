# KuzanJ/awesome-jev
- **One-liner:** Rigorous, license-audited directory of Jev-related GitHub repositories (92 featured, 3,903 indexed), strongest on open decision models, local inference engines and evaluation projects.
- **Language(s):** English
- **Type:** curated-list (featured selection) + auto-generated-list (full catalog built from GitHub searches via scripts/render_catalog.py)
- **Scale:** README: 92 featured projects in tables with license + pinned-commit source link. Full index 3,903 repos (2,475 licensed; 1,350 license-pending; 78 metadata-only). Featured sections: Official tools; Trained models and training recipes; Local inference and compatible servers; Evaluation and calibration; SDKs and integrations; Agent tools and workflow control; Browser and device control; Data search and document workflows; Games robotics and simulations; Learning resources and directories. Catalog pages: agents, browser, data, demos, evaluation, finance, games, inference, models, official, other, productivity, resources, sdks, security, license-review, metadata-only. docs/: OVERVIEW, MODELS (implementation comparison), METHODOLOGY, SOURCES; CHANGELOG.
- **Quality flags:** High quality and unusually careful: every featured entry links to the README at a pinned commit; license checked; explicit caveats ("API compatibility does not guarantee matching behavior", "inclusion does not mean the project has been run"). The full catalog is bulk/automated (GitHub search `jev`, `"typesafe.ai"`, `"system one" decision`, `RLCD`) so long-tail quality varies. Credits discovery sources: heyjunpenn, AnotiaWang, yibie, ckaraca, JohnDotOwl, hellogumbo, cobanov, logicrw awesome-jev lists + HF "Jev Reproductions Tracker".
- **Unique value:** Best source on the **open-model / reimplementation ecosystem** with a comparison table (approach, artifacts, "important boundary") and a methodology checklist for comparing implementations; license auditing (e.g. JevNext PolyForm Noncommercial); name-collision disambiguation (multiple `openjev`, `jev-mcp`, `jev-go`); repo-rename tracking; arXiv paper IDs.

## Facts claimed about Jev
- TypeSafe introduced Jev on **September 15, 2026** as its first public System One model. Name "System One" from fast intuitive judgments; "Jev refers to Jevons" (Jevons paradox — cheaper intelligence enables more uses).
- As of Sept 29, 2026 the official models page lists `jev-1.13.0`; `jev-latest` and `jev-preview` both resolve to it. Served only via TypeSafe's API; SDKs and community implementations do not contain its weights.
- Primitives: Choice (selected option, option probabilities, confidence), Score (score, level probabilities, confidence), Noul (value 0–1).
- Public product description names "a new architecture, parallel sampling, and Reinforcement Learning for Calibrated Decisions (RLCD)"; not enough detail to establish any independent reproduction.
- Confidence "is a statistic derived from a distribution, not automatically the probability that an answer is correct" (links docs.typesafe.ai/confidence).
- Official GitHub org `typesafe-ai` repos: typesafe-sdk-python (MIT), typesafe-sdk-js (MIT), system-one-adapter-python (MIT; runs the same interface against LLM APIs for comparison/fallback), skills (MIT), daggerverse (Apache-2.0).
- Papers (arXiv IDs as given): Jev in the Wild 2609.30216 (ecosystem study); this-that-model 2609.23886; Jev-Mem 2609.23986; NumericJev 2609.28587 (code now JevNext, noncommercial).
- Some clones extend beyond Jev: SelfJev adds a "Multi" primitive; Valen/OneJev/Imajev support image/video while hosted Jev is text-only.
- Stumble/jev-go supports "TypeSafe direct access and Vercel AI Gateway".

## Key insights / patterns
- Taxonomy of Jev-adjacent artifacts: official SDK/adapter; local inference engine (scores bounded choices using existing weights, e.g. candidate-logit readout); trained decision model; application integration; evaluation project.
- Local-inference approaches: candidate-logit scoring over existing LLMs (SemIf, LitJev, Simple Jev, AnyJev with option-order correction), DiffusionGemma answer-slot readout (razorback16/openjev), encoder models (Laya, Von, Jeff/GLiFormer, PoorJev/NLI), trained heads/LoRA on Qwen3.5 (Decider, Kev, Luce, Lev, Tev1, Nimble), MLX/CUDA runtimes (jevmlx, Laya-MLX, cu-Jev).
- Warnings: raw LLM output-head / token logprobs are not calibrated by default (LitJev, Tev1); task-trained vs zero-shot results must be reported separately; game-specific models (NanoJev) aren't general parity; port fidelity ≠ task accuracy.
- Evaluation checklist (docs/MODELS.md): decision contract (question isolation, option limits, Score/Noul semantics, confidence definition); training exposure; probability quality (Brier, log loss, reliability plots, ECE with sample sizes, risk vs coverage after abstention); robustness (option order, paraphrase, irrelevant context, missing correct answer, multilingual, adversarial); performance (p50/p95, cold start, caching, context length, question count, hardware, concurrency); reproducibility.
- Usage principles: atomic questions; code combines judgments, applies thresholds, does exact arithmetic; schema validity ≠ correct decision.
- Recurring application patterns: agent context pruning/compaction, model-tier routing, code review, completion-claim verification (Jev Belay), browser/mobile action selection, SQL/DuckDB/SQLite row filtering with NL criteria, semantic grep, rerankers (LlamaIndex).

## Standout entries
- [Official Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) — sync/async client (official)
- [System One Adapter](https://github.com/typesafe-ai/system-one-adapter-python) — same interface over LLM APIs for comparison/fallback (official)
- [TypeSafe Skills](https://github.com/typesafe-ai/skills) — official agent instructions (official)
- [Jev 1.13 known failure modes](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — official limitations (docs)
- [Confidence](https://docs.typesafe.ai/confidence) — probability vs confidence semantics (docs)
- [Decider](https://github.com/Mapika/decider) — Qwen decision models with checkpoints, training, calibration, server (open model)
- [Kev](https://github.com/jaredpalmer/kev) — Qwen-based model family, weights + eval suites (open model)
- [SemIf-OpenJev](https://github.com/TheoLeeCJ/SemIf-OpenJev) — candidate-logit readout from existing open models (local inference)
- [AnyJev](https://github.com/nokia-applied-research/AnyJev) — readouts with option-order correction and calibration, vLLM (local inference)
- [JevBench](https://github.com/fstandhartinger/jevbench) — cross-backend quality/calibration/latency/cost benchmark (evaluation)
- [Jev Calibration Audit](https://github.com/jujumilk3/jev-calibration-audit) — API-only study of abstention, option effects, language transfer, calibration (evaluation)
- [mini-Jev](https://github.com/r-ms/mini-jev) — preregistered logit-readout vs grammar-constrained JSON comparison (evaluation)
- [jevcal](https://github.com/abhixhek/jevcal) — fit task-specific thresholds, coverage, drift (tool)
- [10 Levels of Jev](https://github.com/disler/ten-levels-of-jev) — progressive tutorial examples (tutorial)
- [Jev in the Wild (arXiv 2609.30216)](https://arxiv.org/abs/2609.30216) — ecosystem study paper (paper)
