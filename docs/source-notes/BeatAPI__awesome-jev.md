# BeatAPI/awesome-jev
- **One-liner:** Source-reviewed catalogue of 228 Jev projects with 50+ stars each, including major-framework integrations, organised by type and six build-scenario guides; published by API reseller BeatAPI.
- **Language(s):** English, Simplified Chinese, Japanese
- **Type:** curated-list (script-assisted; promotional)
- **Scale:** 228 projects, updated 2026-09-28, all with 50+ GitHub stars, each linked to fixed-commit evidence. 10 types: Browser & computer use (20), SDK integrations (32), Routing & optimization (16), Open models (31), Search & data (20), Safety & review (16), Agent workflows (17), Interfaces & automation (14), Developer tools (42), Domain tools (20). 6 scenario guides: Filter news & content, Find useful documents & memories, Choose models/tools/agents, Review code & check outputs, Automate browser & desktop actions, Trim agent history & tool output. Featured gallery of 10.
- **Quality flags:** PROMOTIONAL: header and footer push "free JEV API on BeatAPI" (beatapi.io), every scenario page ends with a BeatAPI CTA. Structure borrowed from logicrw/awesome-jev-projects (acknowledged in NOTICE). Generated from data/projects.json by scripts. Star counts are for whole host repos (e.g. LangChain 146.9K) not the Jev integration — the list says so. Star numbers are much higher than other lists (jev-ultrafast 18.2K here vs ~2.9k in kraayenjon list and a later date; kev 4.5K vs 617 in punk2898 at 09-20) — different snapshot dates, but worth flagging. "Source-reviewed; not independently run."
- **Unique value:** Best coverage in batch of Jev integrations inside big mainstream projects (LangChain, Vercel AI SDK, Pydantic AI, LiteLLM, Composio, Eliza, OpenViking, Hindsight, GreptimeDB, Agentgateway, Sub2API, vercel-labs/fx, oh-my-pi, ai-hedge-fund), each with a fixed-commit source link. Scenario guides give a one-line pipeline per pattern and "what to reference". Agent skill (`npx skills add BeatAPI/awesome-jev`). Large "Open models" section (31).

## Facts claimed about Jev
- BeatAPI third-party access: model `jev-1.13-free` via `POST /v1/systemone` on BeatAPI; "input and output cost $0, even on a zero balance"; before first top-up, limit one successful request per minute (BeatAPI's claim, docs.beatapi.io/decisions#free-calls). Not affiliated with TypeSafe.
- Integrations named: Vercel AI SDK TypeSafe provider maps choice/score/yes-no onto unified `evaluate` interface (packages/typesafe-ai); LangChain partner package `langchain_typesafe` (binary, classification, ordinal decisions); LiteLLM complexity router `jev_classifier.py`; Cloudflare Workers AI `typesafe/jev` used by Kody for Score-reranking; Agent Router and LLMGateway implement native System One routes.
- Jev Ultrafast chooses a browser action and matching DOM target in one request, calls a text model only when text input is needed; original X case "2.9M views".
- TypeSafe Mario gives Jev structured emulator RAM/telemetry instead of screenshots (text-only implication).
- Open reproductions: Laya (multilingual non-autoregressive System 1, one forward pass, HF convaiinnovations/laya), Kev 0.5B (Qwen2.5-0.5B), NanoJev (0.6B), Decider (Qwen3.5-2B fine-tune), Von, LocalJev (githubnext), AnyJev (nokia-applied-research).

## Key insights / patterns
- Scenario pipelines (all: Jev judges, code acts):
  - Filter: collected content -> relevance/category judgment -> filter/forward.
  - Retrieve: retrieve candidates -> Jev relevance scoring -> local ranking and fallback (rerankers in OpenViking, Hindsight, Hippo Memory, Kody "widen hybrid pool then Score-rerank").
  - Route: task + options -> classification -> local route selection (LiteLLM, OpenChamber, jev-router, Codex Router).
  - Review: candidate output + criteria -> judgment -> flag/block/request review (Agentgateway guardrail for jailbreak/harmful/secret leakage; fx permission reviewer; Pi Warden).
  - Operate interfaces: observed interface + legal actions -> Jev selects target/action -> executor acts (Cua, agent-desktop, mobile-jev).
  - Trim context: history/output slices -> retention judgment -> keep/truncate/drop verbatim (jev-pruner, fast-jev-compaction).
- Jev usually appears as an optional plug-in decision layer inside larger systems rather than standalone.
- Semantic SQL predicate (GreptimeDB) and semantic linting (jev-lint, Abide, Supercov) are notable niche patterns.
- Trading use: Jev as evidence/risk gate before live entries (QuantDinger), one decision per Monad block (jev-trader).

## Standout entries
- [Vercel AI SDK · TypeSafe provider](https://github.com/vercel/ai/blob/73ec7015edd4f04ca9144ce93a8a037a731e5db8/packages/typesafe-ai/src/typesafe-ai-evaluation-model.ts) — evaluate interface (SDK integration)
- [LangChain · TypeSafe](https://github.com/langchain-ai/langchain/blob/eba445b7563d1709427bd8072892975a6ea59fdc/libs/partners/typesafe/langchain_typesafe/classifier.py) — partner classifier package (SDK integration)
- [LiteLLM · JEV Router](https://github.com/BerriAI/litellm/blob/56116079c8022da0e8f7ff9ccb017ad5aca5aed2/litellm/router_strategy/complexity_router/jev_classifier.py#L70) — complexity-based routing (routing)
- [Pydantic AI · TypeSafe](https://github.com/pydantic/pydantic-ai) — structured outputs mapped to Jev questions (SDK integration)
- [Composio · TypeSafe Provider](https://github.com/ComposioHQ/composio) — tool and argument selection (SDK integration)
- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) — browser agent (browser use)
- [Cua · JEV Use](https://github.com/trycua/cua/blob/83f142c4290a0f7d9ed545ae8532858c6e4f8145/libs/cua-driver/examples/jev-use/python/jev_adapter.py#L11) — computer-use adapter (browser use)
- [Agentgateway · JEV Guardrail](https://github.com/agentgateway/agentgateway/blob/6b0270efd25b5255932943e48b5ca47583d3ad28/examples/llm-guardrail-jev/guardrail.ts) — gateway guardrail (safety)
- [OpenViking · JEV Rerank](https://github.com/volcengine/OpenViking) — calibrated reranker for agent memory (search)
- [GreptimeDB · JEV SQL](https://github.com/GreptimeTeam/greptimedb) — experimental SQL predicate backed by Jev (data)
- [jegrep](https://github.com/can1357/jegrep) — index-free semantic code search (search)
- [Laya](https://github.com/NandhaKishorM/laya) — open multilingual System 1 decision engine (open model)
- [jaredpalmer/kev](https://github.com/jaredpalmer/kev) — tiny trainable Jev-like model (open model)
- [jev-pruner](https://github.com/tamaratran/jev-pruner) — trim Bash output before the model sees it (context)
- [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects) — upstream structure source (list)
