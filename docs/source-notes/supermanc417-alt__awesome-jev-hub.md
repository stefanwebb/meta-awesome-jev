# supermanc417-alt/awesome-jev-hub
- **One-liner:** A small bilingual hub of 51 Jev app projects in 12 categories, plus 10 community lists, with GitHub-API star snapshots, repo screenshots and a visual HTML "collection" page.
- **Language(s):** Chinese (README.md), English (README_EN.md)
- **Type:** curated-list
- **Scale:** 51 projects + 10 lists. Categories: Browser & Desktop Automation / Code & Context Management / Integrations & Toolkits / Routing, Skills & Agent Orchestration / Generative UI / Agent Frameworks & Harnesses / Memory & Runtime Awareness / Open-Source Replicas & Compatible Runtimes / Trading & Finance / Gaming, Robotics & Mobile / Search, Data & Industry Apps / Products & Startups. There is also `jev-collection.html` (84KB of visual cards) and 51 screenshots.
- **Quality flags:** Snapshot dated 2026-09-22 and not updated since, so it is stale relative to other lists. Descriptions are the repos' own GitHub `description` fields verbatim, so there is little original analysis. The README references `data/jev_data.json` and `scripts/build_unified.py`, but **neither is in the repo**. It gets a primitive wrong: it describes **Noul as "skip — not worth it"**, when Noul is a Bernoulli yes/no probability. Its "official slogan" `i. am. speed.` is unverified. Low original value, mostly a duplicate of the larger lists.
- **Unique value:** Mainly visual: screenshots of each repo page and an HTML card gallery. It also records a dated star snapshot (useful to measure growth, e.g. browser-use/jev-ultrafast ⭐16,795 on 09-22 vs 21k+ elsewhere around 09-30).

## Facts claimed about Jev
- Primitives listed as Choice (pick one), Score (rate it) and "Noul (skip — not worth it)". **Noul is wrong here**; other repos define it as the yes/no probability.
- "Official slogan: `i. am. speed.`" (not seen elsewhere in this batch).
- ~81 ms per step in jev-trader (project claim).
- Star snapshot for 2026-09-22: 51 apps with 76,190 total stars and 10 lists with 4,238. yibie/awesome-jev ⭐1,105. heyjunpenn claims a 640-project catalogue.

## Key insights / patterns
- The shared pattern: **observe → Jev decides what to do / where to click / which component → execution is handed to an LLM or the underlying system**. This replaces "call an expensive model every step" with "call it only when needed".
- The categories reflect the main use clusters seen across lists: browser/desktop agents, coding-agent context compaction and routing, MCP connectors, generative UI component selection, memory, trading, games/robotics.
- It observes that many independently maintained lists share the name `awesome-jev`, which fragments the ecosystem.

## Standout entries
- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — fastest/cheapest web agent (browser)
- [lahfir/agent-desktop](https://github.com/lahfir/agent-desktop) — Rust desktop computer use through accessibility trees (desktop)
- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — Claude Code compaction plugin (coding)
- [GhalebDweikat/Winnow](https://github.com/GhalebDweikat/winnow) — calibrated context sieve for Claude Code (coding)
- [qkal/Canny](https://github.com/qkal/Canny) — "deterministic hooks decide, Jev advises" done-gate (guardrail)
- [kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) — routing/memory/compaction skills for Hermes agents (skills)
- [sharziki/semdecide](https://github.com/sharziki/semdecide) — typed semantic decisions for Unix pipes and CI (CLI)
- [razorback16/openjev](https://github.com/razorback16/openjev) — Jev-compatible server on DiffusionGemma (open runtime)
- [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) — per-block trading decisions (finance)
- [monteduro/killmyidea](https://github.com/monteduro/killmyidea) — kill/fix/ship startup ideas (fun app)
