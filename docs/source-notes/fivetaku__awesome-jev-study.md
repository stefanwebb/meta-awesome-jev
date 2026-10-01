# fivetaku/awesome-jev-study
- **One-liner:** Bilingual (Korean/English) annotated "reading" of kraayenjon/awesome-jev at commit 22570dcd: one page per list row, with fact-checks and LLM/script counterfactuals.
- **Language(s):** Korean and English (curriculum lectures Korean-only)
- **Type:** tutorial/study-guide
- **Scale:** 282 row pages per language (~286 files under en/, ~590 files total incl. 17 illustrations). Catalog mirrors the upstream list's sections: front, What is Jev?, Jev vs LLM, Pricing/limits/access, Quick start, Official resources, Community, Featured builds with real numbers, SDKs and clients, Browser and computer-use agents, Search/retrieval/data, Developer tools and code review, Model routing, Business and vertical apps, Robotics and hardware, Demos and games, Agent tools and MCP servers, Use cases by industry, Patterns, Cookbooks, Benchmarks and evaluations, Research and open models, Articles and coverage, Discussions, FAQ, Related lists. Plus a 4-lecture Korean curriculum (01-three-seats, 02-one-call, 03-two-speeds, 04-cap-and-refusal).
- **Quality flags:** Derivative of kraayenjon/awesome-jev (not independent curation). Per-page template is highly boilerplate ("If this were an LLM/script" sections are generic inference, repeated). But unusually rigorous about provenance: labels each claim as "List sentence / Doc / Run / Unverified / Inference", pinned to commit and fetch date 2026-09-22. Explicitly flags an unverified claim. Not promotional.
- **Unique value:** Fact-checking layer on top of the canonical list: which list claims were confirmed on official pages, which were not (e.g. $40M funding, Vercel price/"no waitlist"). Adds docs facts absent from the list (64k/32k context limits). GitHub API metadata (stars, license, push date) for linked repos. Korean-language curriculum with diagrams on Choice cap/decomposition and refusal/fail-closed patterns. License caution (usenotra/notra is AGPL-3.0).

## Facts claimed about Jev
- Jev = TypeSafe's first public "System One" model; "flagship model"; all models served by `POST https://api.typesafe.ai/v1/systemone` (models page, per study).
- Three question types run in parallel against the same state: Choice (`choice`, `probabilities`, `confidence`), Score (`score`, `probabilities`, `confidence`), Noul (`noul`, 0 to 1). Never generates text.
- Choice up to 255 options (Choice doc and list README:97; not on models page). Beyond cap, behavior undocumented.
- List price snapshot dated September 18, 2026: alias `jev-latest` -> `jev-1.13.0`; $0.042 per 1M input tokens, output free ("$42 / $0.042" per billion/million on models page); 250,000 tokens/second, 1,200 requests/minute; text only (no images/audio/video); direct access via early-access waitlist; early access started September 15, 2026 (list's statement).
- Models page (2026-09-22): context 64k tokens per request, 32k for state plus the longest question; `jev-latest` and `jev-preview` both -> `jev-1.13.0`; "no preview build right now"; aliases can move. The list's table omits 64k/32k.
- Gateways: Vercel AI Gateway id `typesafe-ai/jev` (AI SDK `experimental_evaluate`; page showed "32K" and "Free", did NOT show 0.042 or "waitlist" -> list's "no waitlist" unconfirmed there); Cloudflare Workers AI id `typesafe/jev`, context 32,000 tokens, `env.AI.run`, price not shown.
- Launch post "Introducing System One Models and Jev" by founder Diogo Almeida (X @CompleteSkeptic): LLM input "from $0.20 to $10 / MTok" (list adds LLM output ~5x input); Jev end to end "70ms-500ms" vs frontier "3 to 329 seconds"; "40x" is a speed factor. RLCD = Reinforcement Learning for Calibrated Decisions (vs RLHF/RLVR).
- CONTRADICTION/UNVERIFIED: list FAQ claims "$40M raised" (README:519); not present in launch post.
- SDKs: Python `pip install typesafe-sdk` (`TypeSafeClient.system_one`, `Choice`, `Noul`, `Score`); JS `npm install @typesafe-ai/sdk` (`client.systemOne`); env `TYPESAFE_API_KEY`; Bearer auth.
- Agent skill install: `claude plugin marketplace add typesafe-ai/skills`, `claude plugin install typesafe@typesafe-ai`, or `npx skills add typesafe-ai/skills --skill typesafe-ai`.
- Official workflow evals (evals.typesafe.ai): reference labels are an average of "GPT-6 Astra and Claude Fable 5.1"; the list's means (67.8, 0.0004, 74.1, 73.1) were not found on the page.
- Featured build numbers (author-reported): Doom ~10 queries/s, ~$7/hour; Stagehand ~$0.001/task; jev-trader 300 ms Monad block; flight search ~7 s, ~$0.004; Every vibe check 1,709 judgments, <$0.01, 0.35 s median, 6 of 7 planted defects; Ian Nuttall 3,282 posts: 4.25M tokens, $0.1282, 8 m 34 s; 724 ads ~40 s, ~$0.09; SuperX 61 questions ~1 s, $0.0004/draft; typesafe-computer-use ~$0.0002/step; jev-drone 2.5 Hz; jev-ultrafast ~2.9k stars; 1kpapers 1,018 papers.
- Benchmarks where Jev loses: Jev Phishing Bench (2,000 emails) - Haiku 4.5 wins accuracy; Jev search rerank eval (9,831 pairs, 164 zh/en queries) - fusion wins, Jev alone does not beat embeddings (bge-m3).

## Key insights / patterns
- Division of labor: "Jev decides, the LLM writes, code holds the threshold." Code owns composition, thresholds, fan-out, side effects; "the model is not the workflow."
- Choice cap (255) should be handled structurally, not by prompting: hierarchical/recursive Choice (coarse group, then options within), or beam search over Choice probabilities (official "Hierarchical classification" pattern; jev-tree).
- Refusal as a first-class outcome: don't force "nearest option." Examples: skill router rejects weak matches; pi-jev-auto-mode fails closed on bash/write/edit approvals; ProgressGate maps trajectory to CONTINUE/WARN/REPLAN/HALT; jev-commit blocks only on credentials; route uncertain nouls to review but keep raw values.
- Use a script when the rule is already explicit (thresholds, keywords, stable selectors, PID); Jev's niche is same-intent-different-wording classify/route/score/verify where regex is brittle and an LLM is overkill.
- Latency gap changes design: multiple decisions per second loops (games, drones, browser agents) become feasible.
- Calibrated confidence is the claimed difference in kind; not independently tested here. Lock per-question thresholds on your own labeled data (jevcal).
- Don't multiply vendor per-token rates by featured token counts and call it a measurement.
- Accuracy trade-off is real: some benches show LLMs/embeddings winning.

## Standout entries
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post, RLCD, pricing, latency (official)
- [Models, prices, and limits](https://docs.typesafe.ai/models) — aliases, versions, 64k/32k limits (official docs)
- [Quick start](https://docs.typesafe.ai/introduction/quickstart) — official quick start (docs)
- [Workflow evals](https://evals.typesafe.ai) — official eval methodology and results (benchmark)
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — official agent skill for Claude Code/Codex (tool)
- [Jev on Vercel AI Gateway](https://vercel.com/ai-gateway/models/jev) — `typesafe-ai/jev` hosted (gateway)
- [Jev Phishing Bench](https://github.com/anisselbd/jev-phishing-bench) — 2,000 emails vs Haiku 4.5, Haiku wins accuracy (benchmark)
- [Jev search rerank eval](https://github.com/zhuyansen/jev-search-rerank-eval) — 9,831 pairs; Jev alone doesn't beat embeddings (benchmark)
- [ASSAY-001](https://github.com/jourdanlabs/assay-001) — pre-registered calibration check on Banking77/CLINC150, split verdict (benchmark)
- [jevcal](https://github.com/abhixhek/jevcal) — fit per-question confidence thresholds, CI guard on model updates (tool)
- [Jev DSPy Lab](https://github.com/jmanhype/jev-dspy-lab) — record/replay, calibration, selective risk, abstention (tool)
- [jevlike](https://github.com/vinnylarouge/jevlike) — train a small one-pass option scorer; not a reproduction of RLCD (research)
- [Every's editorial vibe check](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds) — 1,709 judgments, 6/7 defects caught (case study)
- [Jev plays chess](https://dev.to/maximsaplin/typesafe-jev-played-chess-and-landed-next-to-reasoning-models-28ga) — legal moves as Choice vs reasoning models (article)
- [kraayenjon/awesome-jev](https://github.com/kraayenjon/awesome-jev) — the upstream list being studied (curated list)
