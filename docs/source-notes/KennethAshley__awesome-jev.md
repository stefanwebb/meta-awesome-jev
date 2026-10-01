# KennethAshley/awesome-jev
- **One-liner:** Classic awesome-style list of 410 Jev projects, SDKs and write-ups across 19 categories with cross-cutting tags, generated from a JSON data file.
- **Language(s):** English
- **Type:** curated-list
- **Scale:** 410 entries, 19 categories: Official Resources; Classification & Routing; Verification & Guardrails; Scoring & Ranking; Coding Agents; Browser & Computer Use; Context & Memory; Agent Frameworks & Harnesses; Search, Data & Retrieval; Apps & Utilities; Games, Robotics & Simulation; Finance & Trading; Content Moderation & Feeds; Evaluation & Benchmarking; Open Reproductions & Research; SDKs & Clients; Integrations & Infrastructure; Guides, Skills & Tutorials; Related Practices & Discussions. Italic #tags (routing, verification, rag, mcp, skills, open-alternative, research...).
- **Quality flags:** README generated from data/entries.json by scripts/build.mjs, but entries appear hand-curated with one-line descriptions. Inclusion bar: live link, README/code shows real Jev call, 5+ stars with recent activity, numbers must trace to source (not re-verified). Explicit warning about bulk same-day scaffolded repos (shared AGENTS.md/STATE.md/CHANGELOG.md). Few official resources (only 4). No publication date visible. Not promotional.
- **Unique value:** Broad, clean categorisation with tags; good "Related Practices & Discussions" (HN threads, independent blog tests, news analysis); strong Evaluation section (~21 benchmarks) and Open Reproductions section; a verification checklist for readers (does code call API, runnable check, numbers trace, code vs prose, license).

## Facts claimed about Jev
- Jev "isn't a chat model": unstructured state + typed question (choice, score, yes/no) -> typed decision with a confidence value, "no token-by-token generation in the loop"; fast, cheap decision layer.
- Official agent skills: `npx skills add typesafe-ai/skills`.
- Launch HN thread: news.ycombinator.com/item?id=49717558.
- Jev available on OpenRouter (jev-cookbook: "Tested recipes for Jev on OpenRouter").
- Community-reported numbers: tax-doc-classifier strict accuracy across 261 IRS form types at ~$0.001/page; jev-column-race 1,000 app reviews Jev vs Gemini 3.8 Flash "4.1x faster and 7x cheaper"; edgejev ~15 ms per question on 4 CPU cores (open reproduction, not Jev); jev-rerank-bench vs Cohere Rerank 4, ZeroEntropy zerank-2 and chat-model across 14 datasets; jev-search-rerank-eval 9,831 pairs / 164 queries.
- Open alternatives referenced: Kev, Laya, PlayJev, SemIf, GliFormer-based "jeff", jevfire (vLLM), jev-forge.

## Key insights / patterns
- Recurring categories: coding-agent routing (per-turn model/effort selection for Codex/Claude Code, subagent dispatch to cheapest capable model), completion/evidence guards for agents (Canny: "deterministic hooks decide, Jev advises"; Blink diff checks), classify-first-read-selectively for agents (jev-sift).
- Language-level integrations: "AI if-statement" (BoundaryML feelings `.feels()`), Ruby probabilistic control flow (hunch), Python decorator compiling typed function signature into a Jev request (aaazzam/jev), JSON Schema to Jev (Kiln-AI).
- Calibration tooling is a distinct niche: jev-calibrate (tune criteria on labels, confirm on held-out), jevcal (thresholds + drift vs LLM teacher), jeval (hand-off line from cost of mistake).
- Judge design: one direct question vs 12-14 scored dimensions with fitted weights (agentjournal post).
- Caveat: listing is not endorsement; verify code actually calls API.

## Standout entries
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post (official)
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — official agent skills (official)
- [Introducing System One Models and Jev (Hacker News)](https://news.ycombinator.com/item?id=49717558) — launch discussion (discussion)
- [An early-access test of TypeSafe's Jev](https://lindfors.no/blog/a-first-look-at-typesafes-jev/) — independent calibration and cost trial (article)
- [Jev Is Not an LLM, and That May Be the Point](https://forkast.news/typesafe-ais-jev-is-not-an-llm-and-that-may-be-the-point/) — news analysis (article)
- [Jev judge call vs dimension scores](https://agentjournal.dev/blog/llm-judge-vs-feature-extraction/) — direct vs multi-dimension judging (research)
- [jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench) — vs Cohere Rerank 4 / zerank-2 over 14 datasets (benchmark)
- [jev-calibrate](https://github.com/smkrv/jev-calibrate) — calibrate questions on your labels (tool)
- [jevbench](https://github.com/fstandhartinger/jevbench) — accuracy/cost/speed/reliability benchmark (benchmark)
- [JevPokerBench](https://github.com/Prophetlab/JevPokerBench) — poker benchmark for decision models (benchmark)
- [jev-cookbook](https://github.com/nexibeo/jev-cookbook) — tested recipes on OpenRouter (tutorial)
- [jev-experiments](https://github.com/dabit3/jev-experiments) — 22 latency-focused demo apps (tutorial)
- [feelings](https://github.com/BoundaryML/feelings) — typed .feels() AI if-statement on Jev + BAML (SDK)
- [docjev](https://github.com/jerryjliu/docjev) — fast document classifier/splitter (application)
- [edgejev](https://github.com/yzfly/edgejev) — offline CPU System One inference with ONNX INT8 (open reproduction)
