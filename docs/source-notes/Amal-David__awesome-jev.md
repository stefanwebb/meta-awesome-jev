# Amal-David/awesome-jev
- **One-liner:** Tight editorial awesome list (~70 reviewed Jev projects with demo gallery) backed by a ~2,270-row auto-discovered catalog and source-review notes.
- **Language(s):** English
- **Type:** curated-list (editorial README) + auto-generated-list (docs/CATALOG.md)
- **Scale:** README ≈ 70 entries in: Getting Started; Demos; SDKs and Skills; Browser and Desktop Tools; Agent Tools; Apps and Integrations; Games and Creative Projects; Independent Models; Reading and Research; Supporting Drivers. `docs/CATALOG.md` ≈ 2,270 rows: Official resources (18), Skills (6), Games and simulations (77), Demos and playgrounds (1196), Browser and computer use (103), Agent tooling and MCP (246), Applications (135), SDKs and clients (85), Integrations (47), Research and independent reproductions (230), Community directories (56), Articles and demonstrations (53). Plus docs: CUA.md (computer-use layer map), OPENROUTER_SHOWCASE.md, X_DEMOS.md, SHIPWITHJEV_REVIEW.md, REVIEWED.md, START_HERE.md.
- **Quality flags:** AI-assisted discovery/drafting (disclosed). Catalog rows carry evidence levels: "primary-source-reviewed", "community-indexed" (many cite github.com/hellogumbo/awesome-jev as evidence — i.e. copied from that list), "readme-matched" (auto). The catalog is largely auto-generated and noisy (e.g. unrelated awesome lists matched by keyword). The editorial README is high-signal and candid about limits. No live tests claimed.
- **Unique value:** Demo gallery with creator X posts; clear layered computer-use map (observe → candidates → choose → execute via driver → verify); documented OpenRouter community-winner roundup (21 Sept 2026) with caveats; ShipWithJev directory review; "Independent Models" section distinguishing non-official Jev-compatible models; cites arXiv survey "Jev in the Wild".

## Facts claimed about Jev
- Jev = TypeSafe's System One model "for probability-based yes/no judgments, choices, and scores rather than generated text"; primitives Noul, Choice, Score.
- Python SDK package `typesafe-sdk`; env `TYPESAFE_API_KEY`; `response.choices["team"].choice` returns selected key (START_HERE). HTTP: `POST /v1/systemone`.
- Official resources listed: docs.typesafe.ai, Playground (console.typesafe.ai/playground), Smart home fan-out demo (docs.typesafe.ai/demos/smart-home), Workflow evals (evals.typesafe.ai), Manifesto (typesafe.ai/manifesto), Discord (discord.gg/typesafe), @typesafeai on X, launch post "Introducing System One Models and Jev" (architecture, **RLCD training**, pricing, Doom and Wikiracing demos).
- Model version referenced: `jev-1.13` / `jev-1.13.0`.
- OpenRouter announced five community winners on **21 Sept 2026** (JevAI for XMage, Jev Chess, tisco, Vibe Domain, jev_search); OpenRouter judged using Jev Score + Choice. JevAI's 11–6–3 record applies to 20 *hybrid* games.
- ShipWithJev (shipwithjev.com) showed 551 mixed records on 23 Sept 2026.
- Paper: "Jev in the Wild" arXiv 2609.30216 — surveys **2,170 public Jev projects**. Another arXiv 2609.23986 referenced in catalog.
- Community latency/cost claims in catalog (not verified): AgentJev-0.6B "~50ms forward pass"; "75ms inference, $0 output tokens"; "317 ms median"; "350ms Jev call picks the model tier"; calibre on Banking77 "80.2% accuracy at $0.103 per 500 decisions"; JEV-Paper-Radar "~$0.06/day"; Convex Decision Evals: Jev vs 14 LLMs on 108 four-option questions.
- Jev input is text: e.g. tisco judges transcripts, not video pixels; computer-use projects rely on OCR/accessibility.

## Key insights / patterns
- Computer-use responsibility split: observe → construct allowed candidates → Jev chooses a bounded candidate ID → authorize/execute via a driver (Cua Driver, Browser Harness, Playwright) → independently verify. A model's DONE answer is not a verified outcome.
- Common hybrid: Jev picks actions/targets, a separate generative model writes text (Jev Ultrafast, nospace, Jev-Mem).
- "Local runtime is not a local Jev model"; independent Jev-compatible models (AnyJev, OpenJev SGLang, Jevlike) don't establish equivalent quality/calibration.
- Code does candidate generation/legality (Snake legal moves, chess legal moves, span assembly in MinusPodJev); Jev picks.
- Test classifiers against labeled, ambiguous and out-of-scope inputs; keep deterministic fallback or human confirmation.
- Privacy: live use sends page text/screen text to TypeSafe/OpenRouter; don't connect sensitive logged-in browsers to try entries.

## Standout entries
- [TypeSafe Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) — official client (SDK)
- [Official TypeSafe Skill](https://github.com/typesafe-ai/skills) — question-writing guidance (skill)
- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) — Browser Use's Jev browser-action loop (browser)
- [Cua Driver + jev-use](https://github.com/trycua/cua) — driver + Jev bounded action recipe (computer use)
- [jev-align](https://github.com/sutro-sh/jev-align) — improves classifier definitions/rubrics with GEPA edits (tooling)
- [Tenbin](https://github.com/simota/tenbin) — MCP/skill for linting questions, eval, threshold selection (tooling)
- [jevrs](https://github.com/luizribeiro/jevrs) — async Rust client (SDK)
- [llm-typesafe](https://github.com/simonw/llm-typesafe) — Simon Willison's LLM CLI plugin (integration)
- [DocJev](https://github.com/jerryjliu/docjev) — document classification & packet splitting (app)
- [neo4jev](https://github.com/jexp/neo4jev) — Neo4j graph exploration with bounded beam search (app)
- [AnyJev](https://github.com/nokia-applied-research/AnyJev) — typed decisions from open models with calibration (independent model)
- [OpenJev SGLang](https://github.com/ekzhang/openjev-sglang) — open typed-decision server (independent model)
- [Jev in the Wild](https://arxiv.org/abs/2609.30216) — survey of 2,170 Jev projects (paper)
- [JevAI for XMage](https://github.com/ShiftSad/mage) — OpenRouter-winning MTG bot (game)
- [Convex Decision Evals](https://github.com/get-convex/convex-evals) — Jev vs 14 LLMs leaderboard (benchmark)
