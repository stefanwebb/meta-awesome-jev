# AppitStudio/awesome-jev
- **One-liner:** Large, evidence-heavy community directory of Jev-powered apps and developer tools, plus runnable offline examples, a coding-agent guide skill, and article-derived implementation guides.
- **Language(s):** English
- **Type:** curated-list (with tutorial/study-guide and project/code components)
- **Scale:** ~850 bullet entries in README (~125 "Apps powered by Jev", ~680 "Developer projects and integrations"); ~800 per-project guide pages under `community/projects/{apps,tools}/`; 14 knowledge-base articles. Top-level sections: Explore Jev with our skill; Start here; Official SDKs and tools; Community projects (Apps powered by Jev / Developer projects and integrations); Computer and browser use; Starter projects; Reference project; Patterns and cookbooks (Routing and classification / Retrieval and verification / Extraction and structured data); Model behavior and evaluation; Contributing. Beta web UI at https://jevlist.ai/ ("JevList").
- **Quality flags:** Explicitly AI-agent-produced ("produced with AI agents using primary documentation, source review, offline tests, and explicit live checks"), but unusually careful: each project guide pins a commit, states what was and wasn't verified, and repeatedly warns that mock results are not accuracy evidence. Not affiliated with TypeSafe. Entries are real GitHub repos with pinned commits; no obvious fabrication. Very large; some redundancy (forks listed separately). Heavy use of "Noul" (the boolean primitive name).
- **Unique value:** (1) Per-project guide pages documenting Jev's exact role, requirements, privacy, and review evidence. (2) Runnable offline Python examples (support routing, quality rubric, RAG triage, span selection, computer-use) with `--mock/--show-request/--live`. (3) `awesome-jev-guide` agent skill (`npx skills add AppitStudio/awesome-jev --skill awesome-jev-guide`). (4) Knowledge base that fact-checks viral X articles against TypeSafe docs (pricing, limits, launch-claim scope). (5) Computer-use design guide (observe → choose → act → verify). (6) Evaluation runner for labeled dev/holdout sets.

## Facts claimed about Jev
- Jev = TypeSafe AI's "System One" model; interface is **state + typed questions**; three primitives: **Choice**, **Score**, **Noul** (yes/no; returns probability of "yes", no separate `confidence` field). Choice/Score return `probabilities`, `confidence`; Score also `score`, `legend`.
- Score = probability-weighted position among zero-based rubric levels (3 levels → range 0–2; not a percentage).
- Endpoint: `POST https://api.typesafe.ai/v1/systemone`; env var `TYPESAFE_API_KEY`; keys via https://console.typesafe.ai/.
- Model IDs: `jev-1.13.0` (pinned default, verified live 2026-09-18), `jev-latest` (moving alias). OpenRouter model `typesafe/jev-1.13` via OpenRouter "alpha Decisions" API (`openrouter.ai/api/alpha/decisi…`). Also available on Vercel AI Gateway and Cloudflare per project entries.
- Pricing (docs.typesafe.ai/models, checked 26 & 28 Sept 2026): **$0.042 per million input tokens, output free**; text-only input.
- Limits: **64,000-token request budget; state + longest single question ≤ 32,000 tokens**; **255-option** Choice limit and **ten-level** Score limit (knowledge-base article says these "matched" docs).
- Question IDs are not sent to the model; questions in one request are evaluated independently (no cross-question dependency).
- TypeSafe launch blog claims **193.6x latency** and **444.6x cost** ratios vs an average of two frontier-model comparators with structured-output wrapper; TypeSafe acknowledges possible task-selection bias and calls these a high end.
- Batching cookbook: **12.2x** cheaper for 13 questions over a long article (also a 10.0x figure cited).
- Vercel reported nearly **13% of paid AI Gateway teams** tried Jev in first 24 hours (free launch promotion).
- Community-reported latencies: "~100 ms typed decisions" (legostin/jev-mcp), "~300 ms round trip" (a browser-use layer), a 150 ms latency target not met (a guard proxy).
- Official SDKs: `typesafe-sdk` Python (0.7.x, 0.7.1 tested; `AsyncTypeSafeClient.system_one`), JS SDK `typesafe-ai/typesafe-sdk-js`; System One Adapter (runs same interface on other LLMs); official agent skill `typesafe-ai/skills`; official WorkflowEvals harness reproducing evals.typesafe.ai.
- Jaggedness (Jev 1.13): literal interpretation, numerical weaknesses, distracting state, adversarial inputs. Input is text/structured only — no images (screenshots need OCR/DOM extraction).

## Key insights / patterns
- Keep counting, arithmetic, date comparison, permissions and execution in code; code extracts candidate spans, Jev selects (Jev doesn't generate missing values).
- Always add an explicit "other/none" option to Choice; for Noul define separate negative/positive thresholds with a review band between.
- Write the full question in `instructions`; read answers by ID not order; chain calls only when a question truly depends on another's answer.
- Cost is dominated by input size: batch all (even speculative) questions for one state in a single request, trim state to fields questions read. jevtok example: 547 tokens batched vs 1,199 for three separate calls (~$0.023 vs $0.050 per 1,000 tickets).
- Pin model version; log requested/returned model ID, question version, thresholds, latency, tokens; re-evaluate after any change.
- Evaluate policy on held-out labeled data; measure both error and automation coverage; count transport failures separately.
- Model-based screening is not a security boundary; state can carry prompt injection.
- Measure cost per *correctly completed* task (incl. review, retries) rather than headline multipliers; an added gate after an LLM may add latency.
- Recurring use-case clusters: agent tool-call permission gates (Claude Code hooks), context pruning proxies, model routers, RAG rerank/relevance, browser/computer use, code-quality linters, calibration benchmarks, self-hosted Jev-compatible `/v1/systemone` servers.

## Standout entries
- [Introduction](https://docs.typesafe.ai/introduction) — official docs entry point (official)
- [Current models](https://docs.typesafe.ai/models) — versions, aliases, pricing, limits (official)
- [Jev 1.13 limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — jaggedness page (official)
- [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) — official client (SDK)
- [JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) — official TS client with type inference (SDK)
- [System One Adapter](https://github.com/typesafe-ai/system-one-adapter-python) — same interface on other LLMs (official tool)
- [TypeSafe Agent Skills](https://github.com/typesafe-ai/skills) — official coding-agent skill (official)
- [WorkflowEvals](https://github.com/typesafe-ai/WorkflowEvals) — reproduce evals.typesafe.ai benchmarks (benchmark)
- [calfram-bench](https://github.com/lorenzofamiglini/calfram-bench) — external calibration audit on 25 benchmarks (benchmark)
- [wellposed](https://github.com/suraj-phanindra/wellposed) — linter for Jev requests (tool)
- [Wald-Q4B](https://github.com/org2AI/wald-4b) — open-weight 4B Jev-compatible decision model (alternative)
- [zh-decision-bench](https://github.com/CodyQin/zh-decision-bench) — Chinese calibration benchmark (benchmark)
- [Milvus reranking notebook](https://github.com/milvus-io/bootcamp/blob/master/bootcamp/RAG/search_with_jev/rerank_search_results.ipynb) — RAG rerank with Jev Noul (cookbook)
- [Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out) — batch independent questions pattern (pattern)
- [JevList](https://jevlist.ai/) — searchable web UI for this directory (directory)
