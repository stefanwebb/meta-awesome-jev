# oxwen11/awesome-jev
- **One-liner:** Terse showcase list of ~200 things people built with Jev, each line stating what Jev decides inside the project.
- **Language(s):** English
- **Type:** curated-list (showcase)
- **Scale:** 201 entries in: Routing (23), Refund review (empty — "none in this batch"), Realtime (40), Eval (42 — mostly guardrails/code review/permission gates), Writing check (10), Tools (86 — MCP, CLIs, SQL, grep, compaction, skills routers, articles/threads). Single README only.
- **Quality flags:** Hand-written one-liners, fairly specific; no stars, no dates, no license info. Empty "Refund review" section suggests batch-based/partially templated maintenance. Some X-thread-only entries. Mixes tools and articles in "Tools". Links to jev.gallery (jev-gallery.pinto-cost.workers.dev) for official tools — maintainer's own site likely. Heavy overlap with other showcase lists (charetterat, onlyoasis, ham-zax) but also many unique small repos.
- **Unique value:** Breadth of small, concrete builds with the Jev decision anatomy in one line (e.g. which primitives, thresholds, Hz, cost/step); good coverage of niche tooling (sqlite-jev, jevql, jsort, jev.nvim, json-render + Jev, new-api plugin).

## Facts claimed about Jev
- Primitive names Choice / Score / Noul used throughout.
- OpenRouter listing URL https://openrouter.ai/typesafe-ai/jev (beta) — note other lists give `typesafe/jev-1.13` / openrouter.ai/typesafe/jev-1.13; slug inconsistency.
- LangChain harness: `TypeSafeClassifier` / middleware for model routing and Auto Mode safety checks before tool calls.
- Vercel `json-render` has Jev docs (json-render.dev/docs/jev): Jev chooses catalog components/slots/action bindings; no free-form JSON.
- Project-reported numbers: jev-ultrafast flight search 7 s / $0.0039; TypeSafe Computer Use ~$0.0002/step; Stagehand ~$0.001/task; jev-trader ~300 ms per Monad block; Sprite Fusion ~319–375 ms, ~$0.00057/request; jevpilot 1.5–4 Hz; jev-drone ~2.5 Hz; 1v1 Jev ~9 Hz; mobile-jev Uber ~21 s / 9 actions; jev-voice-browser ~250–350 ms; pi-jev-auto-mode ~193–642 ms, fails closed; Paolo Rosson PR review ~14 checks, ~$0.00007/PR; fx auto-review ~5–18× faster and more accurate than GPT-5.6 Luna; typesafe-skill-router ~$0.001/turn; jev-experiments ~100 ms multi-question judgments; WebMCP bench 49/49 at ~112×–245× lower model cost vs GPT-6 Astra computer use (Jev picks tools, Mercury fills args); Every vibe check "21 checks × 37 docs → 777 judgments in under 0.7 s (~$0.0025)" — **contradicts** kraayenjon's "1,709 judgments, <$0.01, 0.35 s median" for the same article (21×37 = 777); Vogel email demo ~1,500 emails in batches of 100.

## Key insights / patterns
- Routing variants: sticky cheap model with escalation of hard turns (opencode-jev-orchestrator); per-turn cheap vs strong while keeping native CLI session; cost-aware Choice "cheapest capable model".
- Code owns the route, Jev picks at branch points (jev-plays-pokemon-red ~100 ms) — minimize Jev calls to genuine decision points.
- Two-stage skill selection: strip skill listing, Jev gate + wide/narrow Choice → at most one skill, fail open (cookbook-derived); abstain when low fit.
- "One Noul per standing rule" to decide which rules the main agent sees (jev-rules).
- Hybrid fast/smart: fast = Jev, unsure → reasoning model (classifier.dev).
- ConfidenceGate → act | confirm | escalate (sokit); Rust policy maps probabilities to action (triagedy).
- Pairwise Jev comparisons for semantic sort (jsort); beam search over Jev-scored graph edges (neo4jev).
- Code finds candidates (DOM nodes, regex spans), Jev classifies (typesafe-adblock).
- Shadow-only trading (Prism) — no live trades.
- Writing-quality linters: score prose on axes, weight in code (draftpulse), rustc-style diagnostics (Human Compiler).

## Standout entries
- [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — Browser Use agent (realtime)
- [WebMCP × Jev bench](https://webmcp.com/benchmark) — tool selection benchmark vs computer use (benchmark)
- [json-render + Jev](https://github.com/vercel-labs/json-render) — Jev-driven UI assembly (tool)
- [jev-mcp (jkudish)](https://github.com/jkudish/jev-mcp) — verify claims / screen injection / rank MCP tools (tool)
- [Brainwires jev-mcp](https://github.com/Brainwires/jev-mcp) — jev_rank/verify/next_step/gate_action (tool)
- [sqlite-jev](https://github.com/mgaitan/sqlite-jev) — batched NL judgments in SQLite (tool)
- [jevql](https://github.com/kylemclaren/jevql) — semantic SQL for Postgres (tool)
- [jev-reranker (hotchpotch)](https://github.com/hotchpotch/jev-reranker) — RAG relevance filter/rerank (tool)
- [citation-verifier](https://github.com/MarissaFamularo/citation-verifier) — Noul citation support check (tool)
- [pi-jev-auto-mode](https://github.com/jomatsu/pi-jev-auto-mode) — fail-closed allow/block gate (eval/guardrail)
- [jev-sentinel](https://github.com/harshwasan/jev-sentinel) — injection checks on tool calls/outputs (security)
- [triagedy](https://github.com/m0rphtail/triagedy) — SOC alert disposition (security)
- [Sprite Fusion realtime levels](https://www.spritefusion.com/blog/generating-game-level-in-real-time-with-jev) — realtime game level generation with cost (case study)
- [Six things with Jev (Isaac Flath)](https://isaacflath.com/writing/six-things-i-tried-with-jev) — practitioner write-up (article)
- [Reflex](https://github.com/kshetrajna12/reflex) — in-browser WebGPU noul/choice/score (open model)
