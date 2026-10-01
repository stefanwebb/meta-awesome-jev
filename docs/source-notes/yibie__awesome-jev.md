# yibie/awesome-jev
- **One-liner:** Domain-categorized awesome list (~535 entries) of public Jev projects and practice signals, with strict inclusion rules and a Jev-powered tagging script.
- **Language(s):** English
- **Type:** curated-list
- **Scale:** ~535 entries across 15 categories (README generated from `categories/*.md`): Classification & Routing (55), Adaptive & Realtime UI (10), Verification & Guardrails (45), Scoring & Ranking (38), Agent Decisions (57), Data Labeling & Curation (10), Evaluation & Benchmarking (34), Calibration & Research (44), Infra / SDKs / Integrations (96), Game & Simulation (24), Robotics & Physical (9), Finance & Trading (8), Compliance & Legal (2), Content Moderation (8), Related Practices / Discussions (95); Scientific Pipelines (0, seeding). "Find by coding agent" tags: Multi (20), Claude Code (15), Pi (14), Codex (6), DeepSeek Harness (3), Cline (1).
- **Quality flags:** Well-maintained, one-sentence dense summaries, star badges. Explicit "listing is not an endorsement" warning and specific caution about same-day bulk submissions sharing a scaffold (AGENTS.md/CLAUDE.md/STATE.md). Numbers in entries are project-reported, not verified. Some X/Reddit "practice" entries are thin. Not auto-generated, though README is built by script.
- **Unique value:** Best domain taxonomy of the batch; entries embed concrete reported metrics (accuracy, latency, cost); strong coverage of open reproductions/alternatives (Calibration & Research); Related Practices section indexes launch-discussion (HN, X, Reddit, Chinese/Japanese posts); mainstream-framework adoption (Pydantic AI, RubyLLM, Vercel eve/ai-python, Dub, Cline); `scripts/jev-ray.py` dogfoods Jev to propose catalog tags (Choice + Noul with thresholds, "none" option).

## Facts claimed about Jev
- Jev "is not a chat model": unstructured state + typed question → typed decision (choice, score, boolean) each with a confidence. Primitives `Choice`/`Score`/`Noul`; API `POST /v1/systemone`.
- Versions referenced: `jev-1.13`, `jev-1.13.0`.
- Launch: HN thread "Introducing System One Models and Jev" ~1,800 points / ~480 comments; founder Diogo Almeida's X launch thread (63k likes) argues **RLCD-trained** decision models are a shorter path to economic value than chat models.
- Distribution: OpenRouter (beta), Cloudflare AI Gateway (callable from Workers), Vercel AI Gateway model ID `typesafe-ai/jev` (used by Dub's `malicious-link-check.ts` and Vercel eve's default evaluation model; Vercel ai-python).
- Framework integrations described as official: Pydantic AI `TypeSafeModel`; RubyLLM native System One protocol. Official skills `npx skills add typesafe-ai/skills`; official `system-one-adapter-python`.
- Reported benchmarks (project claims): jev-medhallu-benchmark — Jev **92.9%** on MedHallu (1,000 items) vs 92.4–95.1% for four fast LLMs, **204 ms median, USD 0.03 per 1,000 checks**; Jev settling the 37% of items at ≥90% confidence cut LLM calls 37% with no accuracy loss. CUA-S1-FORMS (706,048-param) 99.7% vs **Jev 83.6%** on its own form eval. Bespoke Nimble 90.1% vs **Jev 93.2%** on 324-example holdout. CLM (8B) claims matching Jev with up to 9x lower latency. Laya ~35 ms single forward pass; laya-Ascend 37–47 ms median for four-question request. Playwright CLI + Jev: "98% lower cost and twice the speed" vs Playwright MCP. Other claimed Jev figures: "81 ms decision latency", "418 ms, p95 1477 ms", "400–690 ms per decision".
- Audio input "rejected" by API in one entry (text-only input).
- Paper: "Jev in the Wild" arXiv 2609.30216 (2,170 public GitHub projects). X post tallied 19 open-source Jev projects >6,800 stars early on.

## Key insights / patterns
- Inclusion bar: must actually call Jev for a typed decision (typed question → answer with confidence → accept/reject/escalate); checklist: does code call the API, runnable check, sourced numbers, code vs prose ratio, license.
- Recurring patterns: model/effort routers for coding agents (Pi, Codex, Claude Code), tool-call safety monitors, context compaction as a Jev decision, RAG reranking (LlamaIndex adapter Scores each node), hallucination checks with confidence-gated escalation to LLMs, game agents, link safety gating.
- Confidence cascade: let Jev decide high-confidence items, escalate rest to an LLM (MedHallu example quantifies savings).
- Large open-reproduction ecosystem: NanoJev (0.6B), kev (0.6/4/8B Qwen2.5), decider (Qwen3.5-2B), Laya (PyPI/HF), jev-local/LitJev/ruling (drop-in `/v1/systemone` servers from logits), CLM (8B) — specialists can beat Jev on home turf but not generally.
- jev-ray design: build options from schema so Jev can't return out-of-schema values; propose tag only when evidence Noul clears threshold; human tags always win.

## Standout entries
- [Jev in the Wild](https://arxiv.org/abs/2609.30216) — survey of 2,170 Jev projects (paper)
- [Introducing System One Models and Jev (Hacker News)](https://news.ycombinator.com/item?id=49717558) — launch discussion (discussion)
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — official agent skills (official)
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) — official adapter (official)
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) — `TypeSafeModel` integration (framework)
- [RubyLLM](https://github.com/crmne/ruby_llm) — Ruby System One support (framework)
- [Dub](https://github.com/dubinc/dub) — production link-safety gate using `typesafe-ai/jev` (production use)
- [eve](https://github.com/vercel/eve) — Vercel engine with Jev default evaluator (framework)
- [LlamaIndex Jev](https://github.com/WiktorB2004/llama-index-jev) — RAG reranker adapter (integration)
- [jev-medhallu-benchmark](https://github.com/stperic/jev-medhallu-benchmark) — pre-registered hallucination-check benchmark (benchmark)
- [NanoJev](https://github.com/TianyuCodings/NanoJev) — 0.6B open replica with training pipeline (open model)
- [kev](https://github.com/jaredpalmer/kev) — trainable Jev-like models 0.6B–8B (open model)
- [Laya](https://github.com/NandhaKishorM/laya) — RLCD-trained non-autoregressive decision model (open model)
- [jev-local](https://github.com/us/jev-local) — Jev-compatible local server, SDK drop-in (open model)
- [Bespoke Nimble](https://github.com/bespokelabsai/nimble) — Apache-2.0 LoRA alternative with eval harness (open model)
