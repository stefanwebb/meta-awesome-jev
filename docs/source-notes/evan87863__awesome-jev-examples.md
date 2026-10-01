# evan87863/awesome-jev-examples
- **One-liner:** Carefully sourced, use-case-organized index of 72 Jev resources (46 projects, 25 official docs/cookbooks, 1 engineering report), with per-entry review notes in four languages.
- **Language(s):** English (source), Simplified Chinese, Japanese, Spanish
- **Type:** curated-list (use-case oriented)
- **Scale:** 72 reviewed resources plus 28 X/YouTube leads in a pending queue (catalog/MEDIA.md). Categories: Official guides & SDKs (26) · Browser, desktop & mobile (8) · Coding agents & MCP (8) · Model routing (2) · Moderation, rules & safety checks (5) · Retrieval & knowledge graphs (1) · Data & observability (4) · Everyday automation & smart homes (2) · Products & content tools (4) · Games & simulations (6) · Evaluation & calibration (5) · Boundary experiments (1). catalog/DETAILS.md has per-entry author, source-checked date and limitations.
- **Quality flags:** High integrity and very transparent. It states that review means reading the source, with no reproduction or execution and author-reported numbers unverified. It lists excluded leads whose READMEs 404'd, including `typesafe-ai/typesafe-sdk-js` because a raw README path failed, which is probably a false negative. Small scale. Not promotional. It sourced discovery from MrJev/awesome-jev, hellogumbo/awesome-jev and madewithjev.com but wrote its own summaries. Data-driven generation (scripts/catalog.py, data/resources.json).
- **Unique value:** The most complete annotated list of **official TypeSafe cookbooks and patterns** in this batch (about 20 cookbook URLs). Per-entry limitation notes. A pending-media queue of YouTube/X tutorials. Data-layer integrations (Postgres, DuckDB, OTel logs).

## Facts claimed about Jev
- Jev is TypeSafe AI's decision model that answers Choice, Score and Noul questions over supplied state.
- HTTP API: send `state`, `model` and typed `questions` to `POST https://api.typesafe.ai/v1/systemone`.
- **Python SDK: `pip install typesafe-sdk`**. Sync and async clients. It reads `TYPESAFE_API_KEY` from the environment. Docs at docs.typesafe.ai/sdk/python. This conflicts with bakiabaci's `pip install typesafe`.
- Agent skill: `npx skills add typesafe-ai/skills --skill typesafe-ai`.
- Playground at console.typesafe.ai/playground. API keys at console.typesafe.ai/settings/keys.
- OpenRouter lists "Jev Latest" and "Jev 1.13". Always-latest model ID is `~typesafe/jev-latest`.
- A third-party playground exists at aijev.net (not official).
- Retriever AI (rtrvr.ai) first-party report: Jev action selection with GLM planning gave speed gains but a higher total cost, from one run per task.
- The Jev 1.13 limitations are "version-specific; reevaluate after upgrading".

## Key insights / patterns
- Core pattern across examples: "code builds the candidate actions, Jev chooses or scores, and code checks the outcome". Free text and complex reasoning go to another model.
- Getting-started steps: read the quickstart (state + questions), pick one close project, check fallbacks/uncertainty/outcome verification, then evaluate a small labeled sample before automating actions.
- Official patterns: speculative fan-out (ask all branches together, let code pick), confidence-gated routing (separate the answer from the decision to act), composite scoring (independent dimensions weighted in code), intent routing.
- Cookbook techniques worth featuring:
  - Pre-parsed value extraction: regex finds candidates, Jev chooses, code copies the original span. This avoids generation.
  - Date extraction: Jev selects date components and deterministic code does calendar math. This works around the date-reasoning weakness.
  - Hierarchical classification: walk the label tree with probabilities.
  - Classification with fallback labels: use a broader label when confidence is low.
  - Structured-extraction cascade: a small model extracts, Jev verifies fields, then escalate.
  - Skill suggestion: rank, shortlist, allow rejecting all.
  - Entity alignment: merge / separate / human review.
  - Autoresearch feature discovery: an LLM proposes questions, Jev produces features, CatBoost trains on them.
  - RAG passage checks: relevance, contradiction, injected instructions.
  - Citation check: quote exists, then context supports the claim.
- Self-consistency cookbooks (Noul on insurance claims, Choice on moderation) study stability, not correctness.
- Data-layer use: SQL predicates backed by Jev (pg-jev, jevQL, duckdb-jev) and log pre-filtering before expensive analysis (jevlogs).
- Boundary experiment: jev-llm generates text by repeated next-word Choice. It shows Jev is not a generator.

## Standout entries
- [Quick start](https://docs.typesafe.ai/introduction/quickstart) — first typed request (official)
- [Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) — official pattern (official)
- [Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out) — official pattern (official)
- [Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions) — batching cookbook (official)
- [Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook) — regex + Jev choose (official cookbook)
- [Structured-extraction cascade](https://docs.typesafe.ai/cookbooks/sde_cascade) — small-model extract, Jev verify (official cookbook)
- [Automatic feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery) — LLM + Jev + CatBoost loop (official cookbook)
- [LLM input and output checks](https://docs.typesafe.ai/cookbooks/llm_guardrails) — guardrail cookbook (official)
- [Retriever AI browser-agent benchmark](https://rtrvr.ai/blog/jev-browser-agent-benchmark) — speed vs cost report (evaluation)
- [FirasSX914/Janus](https://github.com/FirasSX914/Janus) — when routing small/large models is worth it (evaluation)
- [realZachi/pg-jev](https://github.com/realZachi/pg-jev) — Postgres extension with Jev predicates (data)
- [colliber/duckdb-jev](https://github.com/colliber/duckdb-jev) — DuckDB typed judgments (data)
- [awlevin/typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) — Mac computer use via OCR + Jev (browser/desktop)
- [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario) — NES Mario controller from RAM state (games)
- [Made with Jev](https://madewithjev.com/) — showcase site of demos/videos (showcase)
