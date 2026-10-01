# 99hansling/awesome-jev
- **One-liner:** Small Chinese-language curated list of Jev components for local agent harnesses (router, context, browser, verification, skills), emphasizing boundaries between official Jev and community projects.
- **Language(s):** Chinese
- **Type:** curated-list
- **Scale:** ~25 projects + ~10 official links. Sections: 第一性原理：先理解分工 (division of labour), 选用前的边界 (boundaries), 推荐主力 (5 core picks), 官方资源, 种子仓 (Local Agent Skills/Harness; Open alternatives), 按问题挑零件 (Router/skill/gating; Context compaction/memory/verification; Review & domain cases; Browser & real login state; Search), 案例：从有限选择开始 (patterns table), 游戏关卡推荐雏形 (game-level recommendation prototype), contributing. NOTES.md documents sources and verification boundaries.
- **Quality flags:** Very small, cautious, deliberately excludes star counts/rankings. NOTES.md leaks local file paths (/Users/hakm/Documents/_jev-handoff/…) indicating AI-agent-assisted authoring from a handoff doc. Includes bb-browser (not a Jev project). No fabricated numbers. Low overlap in novelty; items mostly present in bigger lists.
- **Unique value:** Explicit per-project "boundary" column (what each project does NOT do); clear LLM / Jev / harness division of labour; notes that reticle's Jev routing is still future work (don't assume integrated); a step-by-step pattern for real-time game-level/event recommendation with finite candidate tables.

## Facts claimed about Jev
- Jev primitives: Choice, Score, Noul. HTTP API `POST /v1/systemone`. Cloud model `jev-latest`.
- SDKs: Python `typesafe-sdk`, JS/TS `@typesafe-ai/sdk`; key in `TYPESAFE_API_KEY`. Package names may change — defer to official docs.
- Official resources: typesafe.ai, docs.typesafe.ai (quickstart, primitives, patterns, api, agent-skill), typesafe-ai/skills, launch blog, LangChain "Building a Harness with Jev" blog (langchain.com/blog/building-a-harness-with-jev).
- Links verified 2026-09-20 (HTTP 200 on eight seed repos' README).
- No performance numbers claimed.

## Key insights / patterns
- Division of labour: LLM understands long context, generates plans/candidates/code/explanations; Jev does routing, gating, ranking, filtering and next-step choice over finite options; harness owns tool calls, state, permissions, retries, logs and human confirmation.
- Turning candidate actions, models, skills, memory snippets or levels into closed sets is easier to verify than letting an LLM free-form each step.
- Open reproductions ≠ official Jev: calibration, latency, training and contract differ from `jev-latest`; treat as research-only.
- Don't treat community plugins with similar names as having official SLAs; read official API/SDK/skill docs first.
- Browser composition: bb-browser handles whose login state/which site; a Jev layer chooses which allowed action; reject actions not on a whitelist; still need permissions, timeouts, human confirmation.
- Pattern table: timeline/sentiment (filter, rank, escalate/ignore), growth/ops (triage, priority, next assignee), ad blocking (hide/keep/escalate for review), browser ops, mini-games — LLM generates explanations, drafts, new candidates.
- Game prototype: encode levels/waves/drops/events/difficulty as finite tables; each tick send player profile + progress + candidate subset; cap candidate count and stratify by rules first; LLM only generates narrative/offline candidates; log candidates, choice, version, latency, outcome for replay and A/B.
- Ad blocking etc. need domain whitelists, rollback-able rules, privacy boundaries, human review.

## Standout entries
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — official agent skill (official)
- [Agent skill docs](https://docs.typesafe.ai/agent-skill) — official (official)
- [Patterns](https://docs.typesafe.ai/patterns) — fan-out, routing patterns (official)
- [LangChain: Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev) — harness design (article)
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — context compaction (context)
- [jev-pruner](https://github.com/tamaratran/jev-pruner) — prune long outputs before context (context)
- [jev-browser](https://github.com/Ying-Kai-Liao/jev-browser) — Playwright snapshot → action selection with MCP (browser)
- [skillranker](https://github.com/Dicklesworthstone/skillranker) — rank installed skills by session context (skills)
- [pi-jev](https://github.com/y0usaf/pi-jev) — Pi tool-call gate (gating)
- [foreman](https://github.com/thruwire/foreman) — coding-worker supervision (supervision)
- [building-with-jev-skill](https://github.com/dbreunig/building-with-jev-skill) — question-design skill (skills)
- [jev-search](https://github.com/superagents-lab/jev-search) — search intent/source/relevance decisions (search)
