# stainlu/awesome-jev
- **One-liner:** Daily auto-swept index of every public Jev repo (6,213 indexed, 2,307 "active" listed) topped by a short, hand-read Featured section with opinionated "why click" notes.
- **Language(s):** English
- **Type:** auto-generated-list (daily GitHub Action `scripts/discover.py`) with a small curated-list layer
- **Scale:** ~35 hand-read Featured entries across: Official; Frameworks that already speak Jev; Seeing what it does in production; Context compaction; Routing; Guardrails; Browser and computer use; Search and ranking; Agent tooling; Open reproductions and research; Applications. Then "All projects": 2,307 active projects table (Project | What it is | ★ | Language | Last commit) out of 6,213 indexed (data/projects.json has 6,851 keys at clone time). data/excluded.md lists false positives.
- **Quality flags:** Featured layer is high quality — each entry "opened and its use of Jev confirmed in the source". Bulk table is auto-generated from GitHub metadata descriptions (not verified). Clever activity filter: only lists repos committed to after their publish day, which drops 3,906 "launch-week drops". Some featured links use pre-rename names (e.g. itsmostafa/typesafe-mcp, uehaj/jev-semgrep — renamed per KuzanJ list).
- **Unique value:** (1) Discovery methodology: code signals `api.typesafe.ai/v1/systemone`, `@typesafe-ai/sdk`, `TYPESAFE_API_KEY`; topics `jev`, `typesafe-ai`, `system-one`, `system-one-models`. (2) False-positive notes: "JEV" = Japanese encephalitis virus / surname; `typesafe` generic word ("typesafe Commerce SDK"). (3) Opinionated commentary identifying the best exemplar per pattern (e.g. BAML as best type-system→primitive mapping; system-one-adapter as the honest A/B baseline). (4) Largest raw index count among lists in this batch.

## Facts claimed about Jev
- Jev = TypeSafe AI's System One model; not a chat model; given program state + typed question, returns typed answer with calibrated probability "in about 100ms".
- Three question types: Choice (pick one of N), Score (ordered scale), Noul (probability a statement is true).
- Official repos: typesafe-sdk-python, typesafe-sdk-js, skills ("installable into Claude Code as a plugin"), system-one-adapter-python ("drop-in replacement for the SDK's evaluation API backed by an ordinary LLM").
- API endpoint signal: `api.typesafe.ai/v1/systemone`; npm `@typesafe-ai/sdk`; env `TYPESAFE_API_KEY`.
- Ecosystem "went from nothing to thousands of repos in a week" (Jev published 2026-09-15; repos created before that date matching weak signals are auto-dropped).
- Framework integrations: pydantic-ai, LiteLLM (compaction guardrail), BAML (bool/float → Noul, enum/union → Choice, classes flatten to one question per leaf), Effect (`@effect/ai-typesafe`), Rig (`rig-typesafeai`), Ax (DSPy for TS), Opik, Arize OpenInference (Choice/Score/Noul as OTel spans).
- Von implements `/v1/systemone` and publishes a ViZDoom benchmark vs Jev for sub-20ms real-time control.
- Note: BAML mapping here says floats → Noul (a probability), which is a design choice of that integration.

## Key insights / patterns
- "Decide with Jev, generate with an LLM" (jev-ultrafast: Jev picks operation/element, small LLM writes text only for TYPE_TEXT).
- Context compaction is "the densest cluster in the ecosystem" because deciding what to discard is a judgment; variants: per-tool-call keep/drop (fast-jev-compaction, LiteLLM guardrail), verbatim retention of kept items (caliber ai-setup), prune Bash output before the agent reads it (jev-pruner), ask whether now is a safe moment to compact (compact-adviser).
- Routing: pick model and thinking effort jointly (jev-codex-router); treat models/subagents/skills/MCP tools/CLIs as one Choice candidate set (JevRouter).
- Guardrails: send commands that already passed hard-coded rules to Jev for irreversibility risk (second opinion); natural-language lint rules judged per write (pi-warden).
- Anti-hallucination: Jev only *picks* candidate spans extracted by code; URL copied verbatim, never generated (jev-voice-browser).
- A/B honestly: use pydantic-ai or system-one-adapter to compare Jev vs an LLM on your own task.
- Semantic grep per line is "either the most obvious use of Jev or the most wasteful" — cost tradeoff.

## Standout entries
- [typesafe-ai/system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) — LLM-backed drop-in for A/B testing (official)
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — official agent skill / Claude Code plugin (official)
- [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) — output_type fields become Jev questions (framework)
- [BoundaryML/baml](https://github.com/BoundaryML/baml) — type system → primitives mapping (framework)
- [BerriAI/litellm](https://github.com/BerriAI/litellm) — Jev compaction guardrail (framework)
- [Arize-ai/openinference](https://github.com/Arize-ai/openinference) — OTel instrumentation for TypeSafe SDK (observability)
- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — Claude Code compaction via Jev (agent tooling)
- [kunchenguid/compact-adviser](https://github.com/kunchenguid/compact-adviser) — is it safe to compact now? (agent tooling)
- [0xNatoshi/jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) — joint model + effort routing (routing)
- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — decide/generate split browser agent (browser)
- [moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) — pick-don't-generate pattern (browser)
- [ielab/llm-rankers](https://github.com/ielab/llm-rankers) — Jev as point/pair/set/listwise reranker, IR research (evaluation)
- [bespokelabsai/nimble](https://github.com/bespokelabsai/nimble) — open System One model data/recipe (open model)
- [wfzyx/von](https://github.com/wfzyx/von) — /v1/systemone-compatible model with ViZDoom benchmark (open model)
- [Armur-Ai/Pentest-Swarm-AI](https://github.com/Armur-Ai/Pentest-Swarm-AI) — Jev-scored attack paths (application)
