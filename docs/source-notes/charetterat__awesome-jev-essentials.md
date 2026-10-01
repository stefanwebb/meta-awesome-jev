# charetterat/awesome-jev-essentials
- **One-liner:** Opinionated, small (84-project) Jev list where every entry has a hand-written "why this one" reason, often quoting the project's own measured numbers and admitted limits.
- **Language(s):** English and Chinese (README.zh-CN.md)
- **Type:** curated-list
- **Scale:** 84 projects in 11 categories: Route & classify (9), Guard & verify (7), Compaction & context (5), Skills & agents (7), Code search & review (5), Browser & computer use (4), Apps & interfaces (9), Infra, SDKs & bridges (12), Open reproductions & alternatives (10), Benchmarks & evaluation (5), Domain apps (11); plus auto-sorted "Most starred" and "How to choose". Generated from data/projects.json; daily GitHub Action refreshes star data.
- **Quality flags:** High signal; not auto-generated content (only star sorting is automated). Editorial tone slightly promotional ("the Jev projects actually worth your time"), but reasons highlight limits and negative results. Numbers are relayed author claims, not reproduced. `TypeSafeAI/typesafe-playground` is under a "TypeSafeAI" org, not the official `typesafe-ai` — may be unofficial.
- **Unique value:** The densest collection in the batch of per-project quantitative results and honest failure notes (ECE, win/loss vs Jev, batching accuracy degradation), plus a "start here by goal" table.

## Facts claimed about Jev
- Defers "what is Jev" to docs.typesafe.ai; claims "tens of thousands" / "10,000+" repos match a "Jev" search, mostly empty/renamed/copies.
- Mentions "Jev's free tier" (yuyang2230/jev-agent-skill) — unverified vs other lists (Promethe-us says $5 starting credit, not ongoing free use).
- Latency figures reported by projects: ~250 ms (pi-quiet-ask), ~300 ms per browser step (jev-browser), ~330 ms voice (34/34, $0.01 a demo), 150–500 ms per MCP tool (jkudish/jev-mcp), 40–150 ms (jev-foundation-models Swift), p50 ~230 ms (jev-use).
- Comparisons vs Jev: logan-markewich/jeff 400M GLiFormer 75.5% vs Jev 90.5% on AG News(ish); NanoJev 128/128 vs Jev 56/128 on ViZDoom Basic, but loses maze 4/10 vs 7/10; von 395M ModernBERT ~18 ms, ViZDoom Defend the Center 9.00 vs Jev 5.62 kills, but 72.0% vs Jev 96.6% on 49-task suite (not the 91.23% headline); decider 0.30 top-label ECE on JevBench hard; openjev (DiffusionGemma) 27 ms p50/question; AnyJev option-rotation cuts order-flip 0.230→0.073.
- jev-as-a-judge: 5 frozen runs × 100 re-scores, Jev matched every human pass/fail label (Claude Sonnet 4.6: 80%), 92–913× less score variance, $0.34 vs $28.17.
- jevbench: 48 Jev-class models, harmonic mean of Intelligence/Calibration/Speed/Cost; 220 hard items frozen & hashed, half sealed.
- jevals: 8 evals on a trace for $0.00006 in 0.33 s.
- tax-doc-classifier: $0.00115 vs $0.039 per page, ~0.5 s vs 3.3 s vs production Sonnet; 261 IRS forms vs 30.
- docjev: classification 40/40 tie, splitting 7/8 packets vs Luna 8/8.
- pg-jev batching: 20 rows/request 100% correct; 40 → 92–98%; 80 → 77–94%.
- jevmail: 1,000 emails in ~1 minute for ~3 cents. jkudish/jev-browser: Wikipedia Coffee→Espresso ~4 s, $0.0016. Ying-Kai-Liao/jev-browser: 40/42 live-site tasks, ~8k vs ~557k tokens vs Playwright-MCP loop.
- jev-capability-atlas: a typo in one option of a history question was picked with 0.90 confidence.
- jev-agent-skill-router: 68/72 synthetic requests vs 70.8% lexical baseline.
- shimo4228/jev-skill-router concluded routing probably won't help a strong model.

## Key insights / patterns
- Question-writing advice (dbreunig/building-with-jev-skill): pick the primitive your code branches on; split any question weighing two properties; put every question sharing a state into one request.
- Separate judgment from policy: Jev assesses, your rules decide (switchboard, pi-typesafe-jev).
- Deterministic first, model for the ambiguous remainder (pi-verdict zero-latency rules; snifftest; jev-belay spends a Jev call only when files changed and no check passed).
- Fail open vs fail closed must be explicit (jev-belay fails open; jkudish/jev-mcp fail-closed contract; jev-gateway passthrough).
- Batch size degrades accuracy (pg-jev) — don't overpack rows per request.
- Give Jev IDs, not raw coordinates/timestamps: line-ID rendering for YouTube sponsor detection; code maps back.
- Structured state beats screenshots for games (Mario RAM → JSON; Minecraft structured state); keep a fast deterministic reflex layer with veto (drone 50 Hz reflex over 2.5 Hz Jev).
- Shadow mode before trusting routers; don't run two auto-routers; session-fixed routing avoids model churn; preserve cached main chat.
- Skills: replace whole skill catalog in system prompt with one ranking tool to save tokens.
- Open replicas: probabilities from logits of open models are often uncalibrated; position bias can be reduced by averaging across cyclic option rotations.
- Swift: map @Generable Bool/enum/range fields to noul/choice/score (Apple Foundation Models provider).

## Standout entries
- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — per-step LLM call replaced by typed decision (browser)
- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — Claude Code compaction plugin (context)
- [dbreunig/building-with-jev-skill](https://github.com/dbreunig/building-with-jev-skill) — how to write Jev questions (skill/tutorial)
- [kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) — most complete Jev-in-agent-loop example (agents)
- [Ying-Kai-Liao/jev-browser](https://github.com/Ying-Kai-Liao/jev-browser) — 40/42 live tasks, ~70× fewer tokens (browser)
- [realZachi/pg-jev](https://github.com/realZachi/pg-jev) — Postgres `jev()` predicate with batching study (infra)
- [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) — ten typed MCP tools incl. injection screening, fail-closed (infra)
- [peterfriese/jev-foundation-models](https://github.com/peterfriese/jev-foundation-models) — Apple LanguageModelSession provider (SDK)
- [Mapika/decider](https://github.com/Mapika/decider) — open weights with "limits, stated plainly" (open model)
- [kshetrajna12/reflex](https://github.com/kshetrajna12/reflex) — documents what did not help (open model/research)
- [nokia-applied-research/AnyJev](https://github.com/nokia-applied-research/AnyJev) — training-free, position-debiased (open model)
- [fstandhartinger/jevbench](https://github.com/fstandhartinger/jevbench) — sealed, hashed benchmark of 48 models (benchmark)
- [danielgshea/jev-as-a-judge](https://github.com/danielgshea/jev-as-a-judge) — judge variance/cost study (evaluation)
- [sutro-sh/jev-align](https://github.com/sutro-sh/jev-align) — active learning + GEPA for Jev functions (tooling)
- [kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) — production Sonnet replacement with cost/latency (domain)
