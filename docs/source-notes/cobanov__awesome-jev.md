# cobanov/awesome-jev
- **One-liner:** Source-backed, commit-pinned curated list of ~155 Jev projects plus official/provider/framework resources, with dated research notes documenting evidence and corrections.
- **Language(s):** English
- **Type:** curated-list
- **Scale:** ~155 community entries + official resources, provider and framework integrations, guides, related lists (~290 list lines). Sections: Start here; Recent developments; Official resources; Provider integrations; Framework integrations; SDKs and developer tools; Agents, coding, and guardrails; Context and compaction; Browser and computer use; Routing, data, and workflows; Games, robotics, and interactive demos; Media and creative tools; Open reproductions and research; Evaluation and calibration; Guides and cookbooks; Related lists. research/2026-09-19.md and 2026-09-20.md contain pinned-commit evidence tables and ecosystem analysis.
- **Quality flags:** High quality, cautious descriptions ("inclusion does not imply this review reran"). **Promotional:** top-of-README banner advertising Ollaya (ollaya.dev, runs open decision models locally behind a Jev-compatible API) — likely maintainer's own product. Review dated Sept 20 (some entries added later, e.g. Jev in the Wild paper). CC0 license.
- **Unique value:** (1) Best **Evaluation and calibration** section found — independent studies with concrete calibration numbers. (2) Research notes that correct common misconceptions (Noul has no "unknown", 64k vs provider 32k). (3) SDK changelog facts (Python 0.7.0 breaking change). (4) OpenRouter official cookbooks. (5) Large, annotated Related-lists section (useful for de-duplication across the meta list).

## Facts claimed about Jev
- Hosted Jev is **text-only**; browser/audio/image/robotics projects supply extracted text or separate perception models.
- Current model `jev-1.13.0`; `jev-latest` and `jev-preview` both point to it (no separate preview build). Pin versions for evaluations.
- Documented budgets: **64k tokens for whole request, 32k for state plus the longest question**; provider catalogs displaying 32k (Cloudflare) do not establish the same total budget on every route.
- **Python SDK 0.7.0 (Sept 18)**: breaking serialization change from `msgspec` to Pydantic, new `response_model` argument, fixed `str`-subclass serialization. JS changelog latest documented 0.6.0.
- Providers: **OpenRouter** lists `typesafe/jev-1.13` (dated Sept 18; listing date, not new model) plus `typesafe/jev-latest` alias (URL openrouter.ai/typesafe/jev-1.13); **Vercel AI Gateway** (Sept 16) `typesafe-ai/jev` via AI SDK experimental `evaluate`, where "Boolean" = Noul; **Cloudflare** `typesafe/jev`; **Netlify AI Gateway** via `@typesafe-ai/sdk`, billing by Netlify.
- Framework integrations (source-level, as of Sept 20): LangChain (Py/JS), Pydantic AI, LiteLLM (guardrail + complexity router `jev_classifier.py`), Rig, Composio, Effect, BAML (v1 nightly), Ax, TanStack AI.
- Noul returns P(yes) with no confidence field; Choice/Score return distribution + derived confidence; "unknown" is not a built-in Noul output — abstention is application logic.
- Independent calibration numbers: Nautilus Assay (240 seeded questions) **accuracy 92.2%, Brier 0.048, ECE 0.041**; "Jev Does Not Play Dice": Choice put 82.9% on face 1 across 400 fair die rolls (19.0% accuracy), turned stated 30% shortage risk into 5.3% while Noul returned 26.7%; jev-fanout-bench (2,976 OpenRouter requests): ~261 fixed input tokens per request overhead, charges match published rate, batched vs single answer differences ≈ repeat-request noise; jevos local clone 0.815 vs hosted Jev 0.927 on 2,000 yes/no rule questions; jev-orderby-bench passes on 20 Newsgroups but fails 4 of 6 conditions on Amazon ESCI; "When a Judgment Layer's Self-Reported Fields Lie" (Zenodo) reports verdict vocabulary collapsing to three reachable values; tax classifier: 38 low-confidence strict errors among 753 blank-form pages.
- Jev in the Wild (arXiv 2609.30216): survey of 2,170 public Jev projects.

## Key insights / patterns
- "Schema-valid output is not the same as a correct decision": validate on own data, calibrate thresholds, keep high-impact actions behind deterministic checks, provide human fallback.
- Jev does not reproduce probabilities of genuinely random events (dice test) — don't treat outputs as forecasts of stochastic quantities.
- Batching questions is safe: batched vs single-call answer differences comparable to noise; fixed ~261-token overhead per request argues for batching.
- Choice vs Noul formulations aren't equivalent; don't assume complementary answers.
- Context compaction: retained text can be verbatim yet the selection still wrong; implementations for Claude Code, Codex, Pi.
- Browser/device agents are hybrids (Jev selects, LLM types, code executes); not evidence Jev gained vision.
- Guard tools inspect actions but aren't proven security boundaries; trading bots default to dry-run.
- OpenRouter cookbooks: gate tool calls with deterministic checks + Noul approve/block/review bands; verified cascade — Jev checks cheaper model's draft before escalating.
- Retrieval evaluation: beware judge circularity (using a model to judge its own reranking).

## Standout entries
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — first-party limitations (official)
- [Confidence](https://docs.typesafe.ai/confidence) — confidence vs probability semantics (official)
- [typesafe-sdk-python v0.7.0 release](https://github.com/typesafe-ai/typesafe-sdk-python/releases/tag/v0.7.0) — breaking Pydantic change (official)
- [Vercel AI Gateway announcement](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway) — provider access (provider)
- [OpenRouter jev-1.13](https://openrouter.ai/typesafe/jev-1.13) — provider listing (provider)
- [Gating agent tool calls](https://openrouter.ai/docs/cookbook/building-agents/gate-tool-calls-with-jev) — OpenRouter recipe (guide)
- [Verified cascade](https://openrouter.ai/docs/cookbook/evaluate-and-optimize/jev-verified-cascade) — OpenRouter recipe (guide)
- [Milvus Search with Jev](https://github.com/milvus-io/bootcamp/tree/master/bootcamp/RAG/search_with_jev) — nine RAG notebooks (tutorial)
- [Jev Cookbook (nexibeo)](https://github.com/nexibeo/jev-cookbook) — 15 runnable recipes (tutorial)
- [Jev Calibration Study (Nautilus Assay)](https://github.com/chunxiaoxx/nautilus-compass/blob/main/docs/wall/GENESIS_HOSTED_JEV_CALIBRATION.md) — reproducible calibration eval (benchmark)
- [Jev Does Not Play Dice](https://github.com/KantaHayashiAI/jev-does-not-play-dice) — calibration on known-probability inputs (benchmark)
- [jev-fanout-bench](https://github.com/blowxian/jev-fanout-bench) — batched vs single requests, billing (benchmark)
- [Jevals.com](https://jevals.com/) — Jev vs six LLMs on human-labeled sets (benchmark)
- [jev-decision-benchmarks](https://github.com/baibizhe/jev-decision-benchmarks) — MetaTool/When2Call/BFCL tool decisions (benchmark)
- [jev-trust](https://github.com/chunxiaoxx/nautilus-compass/tree/main/sdks/jev-trust) — log decisions and measure domain calibration (tool)
