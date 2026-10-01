# punk2898/awesome-jev-verified
- **One-liner:** Code-verified auto-generated directory of 788 Jev repos (each linked to the exact line calling Jev) plus an original 2,390-question benchmark testing TypeSafe's marketing claims.
- **Language(s):** English and Simplified Chinese (README.zh-CN.md); full benchmark report in Chinese (external site)
- **Type:** auto-generated-list (with original benchmark — also security/robustness-relevant)
- **Scale:** 788 entries (765 code-verified; 54 unverified leads parked in data/leads.json), last checked 2026-09-20. Sections: Official (4), SDKs & clients (131), Agent tooling (154), Guardrails & review (47), Context engineering (25), Browser & computer use (42), Infrastructure (31), Search & retrieval (25), Applications (106), Games, robotics & simulation (49), Open reproductions (35), Benchmarks & research (83), Lists & resources (56). README shows top 10 per category by stars; full lists in categories/*.md.
- **Quality flags:** Auto-generated (discover -> verify by grepping pinned source for `api.typesafe.ai`, `/v1/systemone`, SDK import, `jev-*` id, `experimental_evaluate` -> classify with Jev itself -> build). Categories are Jev's own machine classification (admitted). Listing = "contains code that calls Jev on 2026-09-20", not quality/security review. Benchmark is a single run through Vercel gateway from one location; candid "Limits of this test" section. Not promotional; debunks several vendor claims. Model names like "GPT-5.6 Sol/Terra/Luna" are as stated.
- **Unique value:** Highest-signal benchmark in batch: open harness + per-question JSONL results; claim-by-claim verdict table vs TypeSafe docs/tweets/blog; per-dataset accuracy/ECE; routing-on-confidence stats; batching findings. Verified-code receipts per entry. Big catalog of open reproductions (NanoJev, kev, openjev, SemIf, etc.) and 56 other Jev lists.

## Facts claimed about Jev
- Tested model: `typesafe-ai/jev` (`jev-1.13.0`) via Vercel AI Gateway, AI SDK 7.0.107, run 2026-09-19. AI SDK call: `experimental_evaluate` with questions of `type: 'boolean' | 'choice' | 'score'`, `criteria` object (choice) or array (score); answers e.g. `answers.dept.choice`.
- Headline (Jev / GPT-4.1-mini / GPT-5.6 Sol / Terra / Luna): True/false acc (800) 92.5% / 87.8 / 92.1 / 91.6 / 86.0; multiple-choice (400) 77.3% / 74.3 / 82.5 / 82.0 / 80.5; boolean ECE 0.048 / 0.078 / 0.043 / 0.051 / 0.105; confidently wrong (>=90%, of 800) 6 / 70 / 39 / 49 / 88; prompt injections succeeded (of 80) 1 / 73 / 1 / 11 / 63; median latency single question 456 ms / 928 / 1661 / 1342 / 1367; p99 <0.8 s vs 6-7.6 s for GPT-5.6; cost for 2,390 questions $0.049 / $0.246 / $4.27 / $2.16 / $0.27.
- Claim verdicts: calibrated — Partly (MC ECE 0.124 overconfident); consistency — Holds (0 flips on 60 rephrasings; 1 contradiction in 120 polarity pairs); deterministic — "Close, not bit-exact" (no flips over 5 repeats, max drift 0.09, only 12/30 bit-identical); "Under 100 ms / 60 FPS" — Not reproduced (server-side median 248 ms, fastest 189 ms, none <100 ms in 40 calls; end-to-end 456 ms); "100x / 194x faster" — Only when batching (~3-3.6x vs GPT-5.6 single-question; 50 questions/call ~5 ms/question); "$42 per billion input, output free" — Holds (1,154,813 tokens billed $0.0485) but Jev counts ~2x the tokens GPT does for same text; "445x cheaper" — not reproduced (88x vs Sol, 45x Terra, ~5x Luna/GPT-4.1-mini); "Eliminates hallucination" — Overstated (36 wrong at >=90% conf of 1,200; fewest of five); weaker in Chinese — True (XNLI en 79.3% vs zh 68.7%) but GPT-5.6 dropped more (13-16 pts vs 11).
- Per-dataset (acc/ECE): SST-2 96.0/0.095; BoolQ 88.0; RTE 94.0; TruthfulQA 93.0; Banking77 68.0 (vs 77-78 GPT-5.6); AG News 88.0; Counting 65.0 (Sol 97.5); Arithmetic 100; Dates 100; Multi-hop 100; Injection resistance 97.5.
- Batching: 50 questions in one call ~same wall-clock as one, 2 of 50 answers differed vs separate; at 100 per call latency erratic (1.0 s, 4.1 s, 8.2 s).
- Jev does not accept image input. Official repos: typesafe-ai/skills (785 stars), typesafe-ai/system-one-adapter-python ("Drop-in TypeSafeClient replacement backed by LLM APIs"), typesafe-sdk-js, typesafe-sdk-python.
- Claude Opus 5 tried on 20 questions only (15/17 correct, ~$0.0044/question, ~2.7 s median).
- Contradicts vendor marketing "sub-100ms", "100x faster", "445x cheaper", "eliminates hallucination".

## Key insights / patterns
- Don't ask Jev to count: counting 65-77%; all counting errors agreed with a number suggested in the question (anchoring).
- Keep option sets small: 77-way Banking77 drops to 68%.
- Route on confidence: top 68% of MC answers are 90% correct; the 20% marked unsure are 43% correct — send those to humans. GPT self-reported confidence sorts almost nothing (81-87% in top bucket).
- Batch questions per call (up to ~50) for the real order-of-magnitude speedup; avoid ~100/call.
- Injection resistance strong (level with GPT-5.6 Sol).
- Token counting differs from GPT (~2x) — adjust cost estimates.
- Record the model version; one-location gateway latency may differ; server-side floor ~189 ms.
- Caveat: comparison uses self-reported LLM probabilities, which flatters Jev's calibration.

## Standout entries
- [Benchmark report (Chinese, charts)](https://jev-playground-five.vercel.app/report) — full measurement report (benchmark)
- [Jev playground](https://jev-playground-five.vercel.app) — try the benchmark questions (tool)
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — official agent skills (official)
- [typesafe-ai/system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) — official drop-in TypeSafeClient backed by LLM APIs (official)
- [typesafe-ai/typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) — official Python SDK (SDK)
- [typesafe-ai/typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) — official JS/TS SDK (SDK)
- [sutro-sh/jev-align](https://github.com/sutro-sh/jev-align) — calibrated classifiers from human feedback with Jev + GEPA (tool)
- [thruwire/foreman](https://github.com/thruwire/foreman) — software-factory foreman on Jev, 408 stars (agent tooling)
- [dbreunig/building-with-jev-skill](https://github.com/dbreunig/building-with-jev-skill) — skill for writing programs that call Jev (agent tooling)
- [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) — nano replica with training pipeline (open reproduction)
- [jaredpalmer/kev](https://github.com/jaredpalmer/kev) — tiny Jev-like model on Qwen2.5-0.5B (open reproduction)
- [TheoLeeCJ/SemIf](https://github.com/TheoLeeCJ/SemIf) — semantic ifs from open models on a 3090 (open reproduction)
- [razorback16/openjev](https://github.com/razorback16/openjev) — Jev-compatible decision server on DiffusionGemma (open reproduction)
- [Zaious/jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas) — evidence map of where Jev holds up vs breaks (benchmark)
- [AbdelStark/jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks) — calibration, selective risk, latency evals (benchmark)
