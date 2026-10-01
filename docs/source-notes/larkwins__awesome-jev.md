# larkwins/awesome-jev
- **One-liner:** Chinese/English hub of 51 Jev app projects in 12 categories plus 10 community lists, with GitHub star snapshots, repo screenshots and an HTML card gallery.
- **Language(s):** Chinese (README.md, primary) + English (README_EN.md)
- **Type:** curated-list
- **Scale:** 51 projects + 10 community lists (80,428 total stars, snapshot 2026-09-22). Categories: Browser & Desktop Automation, Code & Context Management, Integrations & Toolkits, Routing Skills & Agent Orchestration, Generative UI, Agent Frameworks & Harnesses, Memory & Runtime Awareness, Open-Source Replicas & Compatible Runtimes, Trading & Finance, Gaming Robotics & Mobile, Search Data & Industry Apps, Products & Startups. Also jev-collection.html (visual cards), screenshots/ (51 PNGs).
- **Quality flags:** Descriptions are upstream repo descriptions verbatim (several "No official description"). **Factual error: defines Noul as "(skip — not worth it)"** — Noul is actually the yes/no probability primitive. Includes some tenuous entries (vercel-labs/json-render as "Generative UI", pulseaiclub/phi, agent-beacon) whose Jev connection is not explained. Star-count ranking. Mostly overlaps with larger lists.
- **Unique value:** Star/language snapshot per project; screenshots/HTML gallery; star counts for 10 other community lists (useful for ranking sibling lists: yibie 1,105; Anil-matcha 776; v-modal 632; AbdelStark/awesome-typesafe-jev 432; logicrw 342; cobanov 318; AnotiaWang 271; heyjunpenn 260 ("640 projects"); kraayenjon 100; robokrunch 2).

## Facts claimed about Jev
- Jev = TypeSafe AI's "System One" model; fast/cheap/typed judgments; primitives `Choice` (pick one), `Score` (rate it), `Noul` — mis-described here as "skip — not worth it" (contradicts all other lists: Noul = yes/no probability).
- Official slogan "i. am. speed." (note: other lists attribute this slogan to Browser Use's jev-ultrafast launch, not TypeSafe — likely a conflation).
- "~81ms per step in jev-trader".
- Star snapshots (2026-09-22): jev-ultrafast 16,795; json-render 17,997; QuantDinger 11,970; fast-jev-compaction 6,097; kev 2,799; jev-chat-jarvis 2,034; jev-trader 1,915; NanoJev 1,889; agent-desktop 1,451.
- tax-doc-classifier: 100% strict accuracy across 261 IRS forms, ~$0.001 per page; jev-curate: 24.0 rows/sec measured.

## Key insights / patterns
- Shared pattern: Jev as the cheap, low-latency judgment/routing layer — observe → decide what to do / where to click / which component → hand execution to a large model or system; call the expensive model only when needed.
- "Deterministic hooks decide, Jev advises" (Canny) — Jev as advisory signal behind deterministic gating.
- Semantic caching: skip LLM calls when Jev says same intent (jevcache).
- Unix-pipeline/CI semantic decisions (semdecide); graph navigation by classifying neighbouring relationships (neo4jev); calibrated AI functions from human feedback with GEPA (jev-align).
- Ecosystem fragmentation: many independently maintained lists share the name `awesome-jev`.

## Standout entries
- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — fastest web agent (browser)
- [lahfir/agent-desktop](https://github.com/lahfir/agent-desktop) — desktop computer use via accessibility trees (computer use)
- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — compaction plugin (context)
- [GhalebDweikat/Winnow](https://github.com/GhalebDweikat/winnow) — calibrated context sieve for Claude Code (context)
- [qkal/Canny](https://github.com/qkal/Canny) — evidence-required "done" gating (coding agents)
- [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) — Jev as MCP tools (integration)
- [kushals256/jevcache](https://github.com/kushals256/jevcache) — intent-based LLM cache proxy (integration)
- [sharziki/semdecide](https://github.com/sharziki/semdecide) — typed decisions for Unix pipelines/CI (tool)
- [kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) — routing/memory/compaction skills for Hermes (skills)
- [sutro-sh/jev-align](https://github.com/sutro-sh/jev-align) — calibrated AI functions via GEPA (tool)
- [jexp/neo4jev](https://github.com/jexp/neo4jev) — graph navigation with Jev (data)
- [kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) — IRS form page classifier (vertical)
- [rmalde/minecraft-agent](https://github.com/rmalde/minecraft-agent) — Astra planner + Jev controller (games)
- [kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory) — agent memory with Jev reranker (memory)
