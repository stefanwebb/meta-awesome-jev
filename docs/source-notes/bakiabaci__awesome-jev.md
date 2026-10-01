# bakiabaci/awesome-jev
- **One-liner:** "Definitive architecture guide" and ecosystem radar for Jev, Laya and System One models. A narrative README plus a heuristically scored catalog of 7,414 repos.
- **Language(s):** English
- **Type:** curated-list (narrative README) + auto-generated-list (catalog/)
- **Scale:** The README curates about 45 repos in sections: 10-Second Mental Model · 4-Year Paradigm Evolution · Great Comparison (vs Instructor/Outlines) · Empirical Performance Benchmarks · Dual-Process Architecture · 3 Typed Primitives · 5-Stage Agent Lifecycle (Ingress/Security/Intent Routing; Context/RAG/Memory; Policy & Tool Gating; Runtime Verification & Code Intelligence; Vision & Multimodal) · Open-Weight Models & Local Runtimes · Scientific Foundations (about 9 arXiv papers) · SDKs by Language · Production Blueprints · Harness Integration Quickstart · Official Resources. catalog/ holds 7,414 repos scored 0–100: Tier A 122, domain files (routing 926, inference-model 1,029/1,338, doc-data, skills-tools, browser-gui, memory-context, code-review, games-robotics, trading, search-seo, agent-framework, awesome-index) and a long tail of 2,541.
- **Quality flags:** **The benchmark tables look fabricated or unsourced.** Examples: "P95 Latency … TypeSafe Jev 68 ms, Laya 33 ms, jevos 110 ms", "Cost / 10k Decisions $0.15", "Parse failure 0.0%". No methodology is given, and the comparisons use dated models (Claude 3.7, GPT-4o). **The SDK code looks invented:** `client.decide.noul(question=..., state=...)` returning `.value`/`.confidence`, "`pip install typesafe`", "`npm i @typesafe-ai/sdk`", "`go get github.com/typesafe-ai/typesafe-go`", LangChain `DecisionRunnable`, and `llama-index-postprocessor-jev-rerank` are all unverified and probably hallucinated. The noul examples show a confidence field, which contradicts the official docs cited in other repos ("Noul has no confidence"). The "Finding" blurbs on papers overstate results (e.g. "Proves…"). Catalog classification is regex-only, and the long tail includes unrelated "decision-model" repos (Camunda DMN, cancer screening). Star counts (e.g. fast-jev-compaction 7,055, jev-ultrafast 20,989, laya 27,165) differ from other lists.
- **Unique value:** A discovery methodology (11 GitHub search signals, recursive date-splitting past the 1,000-result cap; 11,901 repos discovered, 4,873 enriched). Ecosystem statistics: 4,553 repos created in Sept 2026, 1,634 `topic:jev` repos between 2026-09-15 and 09-24, median 1 star. The observation that browser-use/jev-ultrafast has zero topics shows topic-only lists miss things. A lifecycle-stage taxonomy. A list of adjacent academic papers with arXiv IDs.

## Facts claimed about Jev
- Latency "30–150ms" and cost "$0.05 – $0.20 / M decisions" (unsourced). "100% type-safe, zero syntax errors."
- Primitives: Noul (probabilistic boolean), Choice, Score.
- Wire protocol `/v1/systemone`. Local servers are used via `TYPESAFE_BASE_URL="http://127.0.0.1:8765/v1"`.
- Official skill install: `claude plugin marketplace add typesafe-ai/skills` then `claude plugin install typesafe@typesafe-ai`, or `npx skills add typesafe-ai/skills --skill typesafe-ai -g`.
- MCP: `npx -y jev-mcp` with env `TYPESAFE_API_KEY`. jkudish/jev-mcp exposes 11 tools (jev_verify, jev_screen, jev_noul, jev_find, jev_rerank, jev_classify, jev_decide, jev_review, jev_extract…).
- Laya (open, by NandhaKishorM, HF `convaiinnovations/laya`): 100+ languages, ~33 ms. laya-mlx: 13.4 ms median. jaredpalmer/kev: a Qwen3.5/3.8 (0.8B–27B) `/v1/systemone`-compatible server. allebee/jevk5: 0.775 accuracy on hard-tier evals. feder-cr/jev (jevos): CPU 50–220 ms.
- Official resources: docs.typesafe.ai, docs.typesafe.ai/cookbooks, and an OpenRouter cookbook "gate tool calls with Jev" (which implies Jev is on OpenRouter).
- Package names (pip `typesafe`, npm `@typesafe-ai/sdk`, Go `typesafe-go`) are **unverified** and may conflict with other repos' `typesafe-sdk-python`/`typesafe-sdk-js`.

## Key insights / patterns
- Dual-process framing: System 1 routes and gates, System 2 reasons, and low-confidence cases escalate to the LLM.
- A 5-stage agent lifecycle for placing Jev: ingress/intent routing → context/RAG pruning and compaction → tool gating → diff/runtime verification → UI/vision action triage.
- Context economy is a big use-case cluster: fast-jev-compaction (drop obsolete tool results and never summarize), jev-pruner, winnow (25-line chunk relevance with stub/recall pointers), jevcache (cache on `(model, schema, state)` with PII redacted before hashing, for CI replay), and quicksilver (187 files to 4, 26k to 2.4k tokens).
- winnow falls back to system-one-adapter (Haiku) if the Jev API is unreachable, which is a resilience pattern.
- Blueprints: gate tools when confidence <0.95, filter RAG chunks at ≥0.85, and route microservices with Choice. The thresholds are illustrative.
- Local wire-compatible servers let you swap cloud for local by changing the base URL.

## Standout entries
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — official skill/plugin package (official)
- [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) — MCP server with 11 decision tools (agent tooling)
- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — fast browser automation (browser)
- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — surgical context compaction (context)
- [hyperspaceai/jevcache](https://github.com/hyperspaceai/jevcache) — decision cache proxy for CI (tooling)
- [GhalebDweikat/winnow](https://github.com/GhalebDweikat/winnow) — chunk-level relevance pruning (context)
- [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) — multi-stage diff reviewer (code review)
- [jaredpalmer/kev](https://github.com/jaredpalmer/kev) — /v1/systemone-compatible open server (local runtime)
- [ollaya-dev/ollaya](https://github.com/ollaya-dev/ollaya) — "Ollama for decision models" (local runtime)
- [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) — open non-autoregressive decision model (open model)
- [nokia-applied-research/AnyJev](https://github.com/nokia-applied-research/AnyJev) — convert any LLM to a decision model (research)
- [milvus-io/bootcamp search_with_jev](https://github.com/milvus-io/bootcamp/tree/master/bootcamp/RAG/search_with_jev) — Milvus RAG recipes with Jev (tutorial)
- [OpenRouter Jev cookbook](https://openrouter.ai/docs/cookbook/building-agents/gate-tool-calls-with-jev) — tool-call gating recipe (tutorial)
- [UCCI: Calibrated Uncertainty for Cascade Routing, arXiv:2605.18796](https://arxiv.org/abs/2605.18796) — calibration-first routing (paper)
- [R2R token routing, arXiv:2505.21600](https://arxiv.org/abs/2505.21600) — small/large model routing (paper)
