# jqueryscript/awesome-jev
- **One-liner:** Conventional awesome-list of 308 Jev resources — SDKs, gateways, framework integrations, MCP/agent tools, open alternatives, benchmarks — with one-line descriptions, last verified 2026-09-30.
- **Language(s):** English
- **Type:** curated-list (generated README block from a resource store, but hand-described)
- **Scale:** 308 resources, 11 categories: Official Jev resources (4); SDKs and API clients (~30); Gateways and integrations (~35); Agent tools and MCP servers (~68); Browser and computer-use agents (~23); Applications and developer tools (~75); Open System One implementations (7); Open-source Jev Alternatives (~36); Benchmarks and evaluations (~26); Examples and learning resources (~12); Community resources (2).
- **Quality flags:** Mostly solid, freshest snapshot in batch (2026-09-30). **Red flag:** lists [TypeSafe Router](https://github.com/TypeSafeAI/typesafe-router) under "Official Jev resources" as "Official TypeSafe router" — but the official org is `typesafe-ai` (other lists warn about look-alikes); the same `TypeSafeAI` org hosts a "Community TypeSafe AI playground" in the same list, so the "official" label is very likely wrong/possibly a look-alike. Duplicate entry: two "Jevbridge" repos (gamesonrblx/jevbridge and tacticocc/Jevbridge) with near-identical descriptions — one looks like a copy/fork (possibly suspicious). Descriptions are often repo taglines copied verbatim (some with emoji). jqueryscript is a known prolific awesome-list author (generic style).
- **Unique value:** Broadest **SDK/language coverage** (Go, Haskell, Elixir, Java/Spring, Scala, Swift, Ruby/RubyLLM/Rails, Rust ×4, PHP/Laravel) and **gateway/framework integrations** (AgentScope, Agent Squad, GPTCache, Hono, n8n, Neo4j, NeuroLink, OpenViking, Spring AI, TanStack AI, DeepEval, LLPhant, dspy). Also a Jev-compatible API conformance suite (jevcompat) and several security benchmarks.

## Facts claimed about Jev
- "Jev returns typed probabilistic decisions for predefined questions."
- Official: launch blog, typesafe.ai, API reference `docs.typesafe.ai/api`, official SDKs typesafe-ai/typesafe-sdk-js and typesafe-sdk-python, system-one-adapter-python ("Drop-in TypeSafeClient replacement backed by LLM APIs"), official evals site evals.typesafe.ai ("TypeSafe Workflow Evals").
- Access routes: Cloudflare Workers AI; Netlify AI Gateway; Vercel AI Gateway (vercel.com/ai-gateway/models/jev); OpenRouter (openrouter.ai/typesafe); Bifrost `/typesafe` integration; AI SDK provider.
- LangChain Python integration described as "pre-release"; exposes Choice/Score/Noul as a Runnable. TanStack AI adapter sends Choice, Score and **Boolean** questions through `decide()`. LiteLLM uses Jev for Auto Router classification and relevance checks during context compaction. Pydantic AI TypeSafeModel handles typed outputs and supported tool arguments.
- Laya: 33 ms for one question, 7.2 ms/question batched (author claim). Verdict 2.0: 149.6M parameters.
- Paper: JEVQA video-quality evaluation arXiv 2609.24395 (zero-shot video quality prediction from metadata/codec features).

## Key insights / patterns
- Integration landscape is broad: Jev now appears as a "classifier" / "decide" / "evaluate" model type across many frameworks, distinct from chat/generate APIs.
- Recurring integration shapes: semantic HTTP routing (Hono), semantic cache hit verification (GPTCache), graph navigation by choosing neighbouring relationships (neo4jev), SQL functions (pg_typesafe), workflow branching nodes (n8n), rerankers (OpenViking, LlamaIndex), eval metric verdicts (DeepEval, Typed Evals).
- Many "Jev-compatible" servers now exist → need for conformance testing (jevcompat: spec, runner, proxy, mock, GitHub Action).
- Language-specific open clones: OpenThai-SystemOne (Thai/English), sarvam-jev (Indic, in-browser), KaLM-Jev (reranker-based).
- Security benchmarks exist for prompt injection and vulnerable-code detection (jev-sec-bench), phishing (jev-phishing-bench vs Haiku 4.5 on 2,000 emails).

## Standout entries
- [TypeSafe System One API Reference](https://docs.typesafe.ai/api) — official HTTP reference (official)
- [TypeSafe Workflow Evals](https://evals.typesafe.ai/) — official workflow evaluations (benchmark)
- [System One Adapter for Python](https://github.com/typesafe-ai/system-one-adapter-python) — LLM-backed drop-in (official)
- [Jev on Vercel AI Gateway](https://vercel.com/ai-gateway/models/jev) — gateway access (provider)
- [TanStack AI TypeSafe adapter](https://tanstack.com/ai/latest/docs/adapters/typesafe) — decide() adapter (framework)
- [Spring AI TypeSafe](https://github.com/spring-ai-community/spring-ai-typesafe) — Java/Spring integration (framework)
- [GPTCache Jev Evaluation](https://github.com/zilliztech/GPTCache/blob/main/gptcache/similarity_evaluation/jev.py) — cache-hit verification (integration)
- [DeepEval TypeSafe integration](https://deepeval.com/integrations/models/typesafe-ai) — eval metrics on Jev (benchmark/tooling)
- [jevcompat](https://github.com/mandu5/jevcompat) — conformance suite for Jev-compatible servers (tool)
- [jev sec bench](https://github.com/Gaurav-Gosain/jev-sec-bench) — prompt-injection and vuln-code detection benchmark (security)
- [jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench) — vs Cohere Rerank 4 / zerank-2, 14 datasets (benchmark)
- [jev-measured](https://github.com/WallerChen/jev-measured) — cost/latency/accuracy across eight use cases (benchmark)
- [Jev for Engineers](https://github.com/Foadsf/jev-for-engineers) — eight engineering examples (tutorial)
- [Learn Jev Tutorials](https://learnjev.com/tutorials) — independent tutorials (tutorial)
- [JEVQA (arXiv 2609.24395)](https://arxiv.org/abs/2609.24395) — video-quality evaluation preprint (paper)
