# onmyway133/awesome-jev
- **One-liner:** Compact, clean awesome-list of ~115 open-source GitHub projects using Jev, with star badges and one-line descriptions across six categories.
- **Language(s):** English
- **Type:** curated-list
- **Scale:** ~115 entries, GitHub repos only. Categories: Coding Agents & Dev Tooling (~35); Browser & Computer-Use Automation (~20); Search, Retrieval & Data Labeling (12); SDKs & Platform Integrations (26); Open-Source Jev Alternatives (12); Applied Decisions: Games, Robotics, Finance & Productivity (14).
- **Quality flags:** Inclusion bar: GitHub, ≥50 stars with real usage, must actually call/implement the Jev interface, still functional; cites a Reddit review of 287 Jev projects finding most misuse or barely touch Jev. Tidy and accurate descriptions; no dates, no numbers, no docs/papers/benchmarks; shields.io live star badges only. Some repo names outdated (itsmostafa/typesafe-mcp, uehaj/jev-semgrep — renamed per KuzanJ). Describes the third primitive as "a boolean" rather than Noul. Moderate overlap with other lists; not stale, not promotional. Maintainer is a prolific awesome-list author (generic style).
- **Unique value:** Surfaces several established projects with small Jev integrations not highlighted elsewhere (hackclub/ai proxy, vercel-labs/ai-python, instructor-php Polyglot driver, latitude-llm preclassifier, req_llm Elixir, smithers, runline, vellum-assistant, kentcdodds/kody, captaincore, aiavatarkit turn-end detection, OpenWhisper, youtube-sponsor-detection).

## Facts claimed about Jev
- Jev = TypeSafe AI's "System One Model" — "a non-chat model that takes unstructured state plus a typed question (a boolean, a choice, or a score) and returns a calibrated typed decision instead of free text."
- Official repos: typesafe-ai/skills ("official installable agent-skills package"), system-one-adapter-python ("running and benchmarking Jev-style decisions against OpenAI- and Anthropic-compatible APIs"), typesafe-sdk-js, typesafe-sdk-python ("sync and async clients plus typed question/answer models").
- Vercel: ai-cli can run Jev as the evaluation model for its `evaluate` command; ai-python (Vercel AI SDK for Python) exposes Jev through its evaluation API; eve ships Jev as default model for experimental evaluate path.
- NeuroLink exposes a first-class "decide" inference type backed by Jev over 40 providers.
- openJev-verdict-2.0 (151M) reports higher benchmark accuracy than Jev and Laya (author claim). Von: sub-15ms.
- jev-drone runs Jev in a MuJoCo control loop at 2.5Hz.

## Key insights / patterns
- Framing: coding agents use Jev "to gate, route, or score agent actions instead of calling an LLM for every decision."
- Layering: local rules first, Jev as fallback for items rules don't match (bluenoise); Jev classifies, local policy picks final config (firstmate, jev-codex-router).
- Double-checking: pair a general model's PR-review findings with Jev verification on the same diffs (celesto).
- Shadow mode: run Jev judgments alongside existing rule-based decisions before trusting them (prism-liquidity-agent) — a sound rollout pattern.
- Two-stage retrieval: widen a hybrid pool, then rerank with a Jev score (kody).
- Jev + prompt optimization: calibrated "AI functions" from human feedback via GEPA (jev-align).
- Voice UX: judge end-of-turn (aiavatarkit); detect topic changes (OpenWhisper).

## Standout entries
- [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) — official Python SDK (official)
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) — benchmark Jev-style decisions vs LLM APIs (official)
- [fx](https://github.com/vercel-labs/fx) — Jev-backed permission reviewer (coding agents)
- [ai-cli](https://github.com/vercel-labs/ai-cli) — terminal `evaluate` with Jev (SDK/CLI)
- [ai-python](https://github.com/vercel-labs/ai-python) — Vercel AI SDK for Python with Jev evaluation (SDK)
- [instructor-php](https://github.com/cognesy/instructor-php) — PHP structured-output library with TypeSafe driver (SDK)
- [neurolink](https://github.com/juspay/neurolink) — "decide" inference type across providers (framework)
- [kody](https://github.com/kentcdodds/kody) — two-stage retrieval with Jev reranking (search)
- [jev-align](https://github.com/sutro-sh/jev-align) — calibrated AI functions via human feedback + GEPA (data labeling)
- [docjev](https://github.com/jerryjliu/docjev) — document classification/splitting (search/data)
- [prism-liquidity-agent](https://github.com/irfndi/prism-liquidity-agent) — Jev in shadow mode vs rules (finance)
- [aiavatarkit](https://github.com/uezo/aiavatarkit) — end-of-turn detection (voice)
- [celesto](https://github.com/CelestoAI/celesto) — LLM + Jev double-checked PR review (coding)
- [jevbench](https://github.com/fstandhartinger/jevbench) — Jev-class model benchmark (evaluation)
- [von](https://github.com/wfzyx/von) — local sub-15ms drop-in (open model)
