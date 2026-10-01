# THEROCKSSS/awesome-jev
- **One-liner:** Daily auto-updated GitHub-metadata catalog of ~1,944 Jev/System One repos (merged from 21 awesome lists + GitHub search) with an interactive Pages site rendering each repo's README.
- **Language(s):** English
- **Type:** auto-generated-list
- **Scale:** data/jev.json = 1,944 entries (HANDOFF from 2026-09-26 said 1,363). README shows a "New today" block plus top entries per category (with counts): Official Resources (17), Open & Jev-like Models (418), SDKs, APIs & Routers (118), Agents & Automation (171), MCP & Agent Tools (183), Web & Browsing (89), Developer Tools (130), Games & Play (102), Chat & Messaging (51), Finance & Trading (42), Safety, Routing & Guardrails (237), Productivity & Knowledge (24), Media & Content (28), Mobile & Desktop Apps (18), Home, IoT & Robotics (8), Awesome Lists & Catalogs (82), More Projects (226). Site: https://therocksss.github.io/awesome-jev/. Scripts (update_list.py, fetch_graphql, build_site), tests, GitHub Actions.
- **Quality flags:** Fully automated; descriptions are raw GitHub descriptions (no curation/analysis; policy "no marketing copy"). Categorization automatic and coarse (e.g. "Official Resources" mixes official typesafe-ai repos with unofficial community SDKs; "Open & Jev-like Models" has 418 entries including unrelated apps like tax-doc-classifier). Star counts live-refreshed (top 150). HANDOFF.md reveals it was built by a Codex agent. Not promotional. CC0.
- **Unique value:** Freshest and broadest de-duplicated repo inventory with real stars, languages, added/pushed dates — good as a machine-readable seed (data/jev.json schema documented in docs/DATA.md); list of 21 source awesome lists with star counts at harvest (docs/AWESOME_LISTS.md); admission rules (metadata must show Jev connection; topics alone insufficient).

## Facts claimed about Jev
- Jev = TypeSafe's "System One family: fast, cheap, typed decision models that pick an action instead of generating prose."
- Official typesafe-ai org repos listed: skills (★2469, "Agent skills for building with TypeSafe's System One API"), typesafe-sdk-js (★258), typesafe-sdk-python (★255), daggerverse (★22, Dagger modules), system-one-adapter-python (★362), **WorkflowEvals** ("evals.typesafe.ai workflow code published", ★9, new 2026-09-30).
- Open models by stars: NandhaKishorM/laya ★28,962 ("non-autoregressive System 1 decision engine… 100+ languages, router picks checkpoint"), jaredpalmer/kev ★8,004 (Qwen3.5/3.8), mizorewww/laya-mlx ★6,284 ("7–14 ms short decisions on M3 Max"), TheoLeeCJ/SemIf-OpenJev ★4,604, NanoJev ★2,445, feder-cr/jev ★1,124, deepopen ★1,014, ollaya ★1,012, decider ★987, AnyJev ★980, von ★781 ("sub-15ms"), Liuziyu77/Valen ★553 (multimodal Jev-like), PostHog/jeeves ★321 ("Reasoning improves Jev-like decision models").
- jevskill (lazniak): Jev via OpenRouter or TypeSafe "325ms, 0.000013 USD per decision", "99.3% fewer input tokens" (author claim).
- kyotofin/tax-doc-classifier: "100% strict accuracy across 261 IRS forms, ~$0.001 per page" (author claim).

## Key insights / patterns
- Ecosystem shape by count: open reimplementations (418) and safety/routing/guardrails (237) are the largest categories; MCP/agent tools (183) and agents (171) follow.
- Recurring project archetypes in "new today": per-turn model/reasoning-effort routers for Codex/OpenCode/Claude Code; completion-claim supervisors (deterministic evidence + one batched Jev assessment + pure policy); verbatim context curators that drop stale tool results and fall back to native summary when unsure.
- Many unofficial SDKs in Go, Rust, Swift, Java, PHP, Ruby (several claim 1:1 parity with official SDKs).
- Smaller awesome lists (<~30 stars) are "overwhelmingly duplicates" of the big ones — per this maintainer.

## Standout entries
- [Interactive catalog](https://therocksss.github.io/awesome-jev/) — searchable site with live READMEs (directory)
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — official agent skills (official)
- [typesafe-ai/WorkflowEvals](https://github.com/typesafe-ai/WorkflowEvals) — code behind evals.typesafe.ai (official/benchmark)
- [typesafe-ai/daggerverse](https://github.com/typesafe-ai/daggerverse) — official Dagger modules (official)
- [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) — most-starred open non-autoregressive decision engine (open model)
- [jaredpalmer/kev](https://github.com/jaredpalmer/kev) — trainable Jev-like family on Qwen (open model)
- [mizorewww/laya-mlx](https://github.com/mizorewww/laya-mlx) — MLX runtime for Laya (open model)
- [ollaya-dev/ollaya](https://github.com/ollaya-dev/ollaya) — "Ollama for decision models", TypeSafe-compatible API (tool)
- [nokia-applied-research/AnyJev](https://github.com/nokia-applied-research/AnyJev) — training-free Jev-style decisions from any LLM (open model)
- [Liuziyu77/Valen](https://github.com/Liuziyu77/Valen) — multimodal Jev-like training (open model)
- [PostHog/jeeves](https://github.com/PostHog/jeeves) — reasoning for Jev-like decision models (research)
- [jerryjliu/docjev](https://github.com/jerryjliu/docjev) — fast document classifier/splitter (app)
- [LXBWOW/dsh-completion-supervisor](https://github.com/LXBWOW/dsh-completion-supervisor) — completion-claim verification pattern (agents)
