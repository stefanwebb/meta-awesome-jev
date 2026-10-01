# wh000wh000/awesome-jev-live
- **One-liner:** Auto-rebuilt (every 2h), evidence-graded index of ~800 Jev/TypeSafe ecosystem entries in 20 languages, plus a Chinese "knowledge" log of verified official facts and independent evaluations.
- **Language(s):** English primary; generated editions in 20 languages (zh-CN, zh-TW, ja, ko, es, fr, de, pt-BR, ru, it, ar, hi, tr, vi, th, id, pl, nl, uk). data/knowledge.json is in Chinese.
- **Type:** auto-generated-list
- **Scale:** 800 entries (last sync 2026-10-01). Evidence grades in data: official 17, observed 197, inferred 532, unverified 54. Sections: Official SDKs and developer tools (7) · Community clients, SDKs and adapters (121) · Agent tooling: MCP, hooks, gates and coding agents (245) · Routing, guardrails and approvals (69) · Evaluation, calibration and benchmarks (76) · Open reproductions, weights and architecture research (43) · Applications, games, robotics and interactive demos (42) · Writing, discussions and sibling lists (97) · Other projects (100) · by implementation language. Each entry is a collapsible card with stars, last push, star delta, and evidence grade. Also llms.txt, a searchable GitHub Pages site, and data/entries.json.
- **Quality flags:** Fully auto-generated; the pipeline says curation is deterministic and LLM-free. Two-thirds of entries are only "inferred", so treat them as discovery leads. Some cards are miscategorized (e.g. the Korean gaebalai/jev-playground, graded "inferred", sits under "Official SDKs"). Star counts vary wildly and some look implausible (NandhaKishorM/laya at 29229 stars, TheoLeeCJ/SemIf-OpenJev at 4615). The README is 316 KB, so it is hard to read without the site. The honest grading scheme is a plus.
- **Unique value:** (1) The evidence-grade system (official/observed/inferred/unverified). (2) data/knowledge.json: 52 dated, graded findings (in Chinese) that summarize official docs pages, cookbooks and about 12 independent evaluations with concrete numbers. This is the best fact source in this batch. (3) An explicit exclusion list for name collisions (JeVois, JEvents, Jevil, jEveAssets, ESP32-RLCD). (4) Media (screenshots/GIFs) harvested per project.

## Facts claimed about Jev
- "TypeSafe AI's first System One model". It returns typed values plus probability distributions and does not write prose. Primitives: `Choice` (pick one of ≤255 options), `Score` (rubric 2–10 levels), `Noul` (probabilistic yes/no).
- Endpoint `POST https://api.typesafe.ai/v1/systemone`. Model `jev-1.13.0`, aliases `jev-latest` / `jev-preview` (knowledge.json, citing docs.typesafe.ai/models).
- Limits (docs.typesafe.ai/models, per knowledge.json): 64k tokens per request, with state plus the longest question at most 32k. Rate limit 250k tok/s and 1200 req/min, "dynamically adjusted". Text-only input. No fine-tuning: all accounts share the same weights. Customer data is not used for training. English is most accurate.
- Confidence (docs.typesafe.ai/confidence): a statistic computed from the `probabilities` distribution. **Noul has no confidence field.** Official advice is to start thresholds conservative and test on your own data.
- Jaggedness (docs.typesafe.ai/model-jaggedness/jev-1.13) lists 9 classes: literal interpretation, unreliable counting, date comparison, multi-level indirection, large state with irrelevant detail, adversarial content, instructions contradicting criteria, structural invariants, generation. The official fix is to "split into atomic questions and combine in code".
- Migration to v1 (docs.typesafe.ai/migrating-to-v1): preview `/preview/evaluation` becomes `POST /v1/systemone`. The `prompts` array becomes a `questions` map and the `responses` array becomes an `answers` map. Fields renamed: `probability`→`noul`, `chosen`→`choice`, `expectation`→`score`. Choice probabilities changed from an array to a map. Score probabilities are new in v1. Auth is unchanged.
- The docs llms.txt covers 111 pages, including 18 cookbooks.
- consistency_choice cookbook: 8 Choices × 15 repeats each gave raw agreement 90.8% with conflicts=0. Adding an abstention rule (top prob ≥0.60, else "uncertain") raised it to 99.2%, with 74.2% automated. Comparisons: Haiku t=0 100%, Opus 4.8 reasoning 92.5%, gpt-5.4-mini t=0 99.2%. Official caveat: this measures repeatability, not correctness.
- Official skill install: `npx -y skills@latest add typesafe-ai/skills -s typesafe-ai -g -a '*' --copy -y`. It is a single SKILL.md of 149 lines.
- Official repos listed: typesafe-ai/skills (2491★), system-one-adapter-python ("Drop-in TypeSafeClient replacement backed by LLM APIs"), typesafe-sdk-js, typesafe-sdk-python (sync + async), WorkflowEvals (evals.typesafe.ai code), typesafe-ai.github.io.
- Vercel: an official changelog says Jev is available on AI Gateway. Per @rauchg, swapping GPT Luna for Jev in fx's auto-mode safety reviewer gave "p95 18× faster and more accurate".
- Classmethod independent test: 40 calls, 10/10 correct, median 0.643–0.674 s, $0.000025–0.000027/call. The official benchmark shows Jev at 76.0% vs Luna 76.1% / DS v4 Flash 76.8% (not clearly better).
- jarrodwatts/jev-trader: `latencyMs: 81`, `jevUsd: 0.000004` per decision.
- @moritzkremb on PR review: $0.00007 each, "~200x cheaper than Claude" ($14.50 per 1,000 PRs on Opus 5 vs 7 cents).
- Funding: TS2 headline "TypeSafe AI raises $40 million for Jev but its 445× cost claim is still self-tested".
- The launch HN thread had 1862 points. The @typesafeai X account was reportedly phished on launch day (graded unverified).
- LiteLLM has a TypeSafe compaction guardrail: a tool exchange is dropped when Jev's probability that it is still needed is below 0.2 (default).
- Threshold contradiction: official docs use a 0.5 review floor and 0.9 for destructive actions, while a cookbook uses 0.6/0.85 (noted via flaviocopes).

## Key insights / patterns
- **Probabilities reflect the model's certainty, not world randomness** (KantaHayashiAI/jev-does-not-play-dice). On a fair die Jev reported 82.9% while actual accuracy was 19.0%; on a fair coin it reported 92.0% vs 52.0% actual. Given a stated 45% it returned 6.6%, and given 55% it returned 95.9%, a cliff at 50%.
- Thresholds do not transfer across datasets (FirasSX914/calibre, Banking77 vs Web of Science). jevcal: don't trust thresholds fitted on fewer than about 100 labeled rows. Re-check locked thresholds in CI.
- clownware/bouncer: Brier 0.036–0.149, but the `destructive` question scored 0% in the 0.8–0.9 bucket. It ships in observe (shadow) mode by default.
- flaviocopes: a Noul of 0.5 means "can't tell", not "medium". Don't interpolate Score levels. Batching 13 questions was 12.2× cheaper and 10× faster. Realistic examples in the criteria raised confidence from 0.54 to 0.90. 1,018 abstracts cost $0.08 total at 256 ms median. Rollout advice: replace one "boring decision" with a single question and log it side by side for a week.
- Decision vs generation split (browser-use/jev-ultrafast): number the page elements, fix the op set, and ask operation plus all speculative targets in one request. Call an LLM only for TYPE_TEXT. Google Flights ran in 7.1 s.
- Decomposition is not always better (agentjournal): 12–14 scored dimensions beat a direct question on Japanese NLI (0.9076 vs 0.8373) but had about 25× more false positives on hard benign samples.
- Include "none of the above" as an option. Use execute/confirm/reject bands (genai-craft/openvons).
- LangChain: harness action classifiers were closed-source until now, and a cheap classifier lets any agent adopt the pattern. "Jev isn't a drop-in replacement for an LLM."
- Ecosystem trend: many open reproductions (NanoJev, openjev-sglang on Qwen3.6-35B-A3B, Laya, decider, AnyJev, von, simple-jev) and TypeSafe-compatible local servers (ollaya). There are also priority disputes claiming the architecture was open-sourced "last year".

## Standout entries
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — official agent skills for System One API (official)
- [typesafe-ai/typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) — official Python SDK (official)
- [typesafe-ai/typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) — official TS SDK with inferred answer types (official)
- [typesafe-ai/system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) — LLM-backed drop-in client for A/B tests (official)
- [typesafe-ai/WorkflowEvals](https://github.com/typesafe-ai/WorkflowEvals) — code behind evals.typesafe.ai (official/benchmark)
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — vendor's 9 known failure classes (official docs)
- [consistency_choice cookbook](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook) — repeatability plus abstention study (official)
- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) — decision/generation-split browser agent (agent tooling)
- [KantaHayashiAI/jev-does-not-play-dice](https://github.com/KantaHayashiAI/jev-does-not-play-dice) — probability-semantics counter-evidence (evaluation)
- [FirasSX914/calibre](https://github.com/FirasSX914/calibre) — pre-registered calibration study across two datasets (evaluation)
- [clownware/bouncer](https://github.com/clownware/bouncer) — coding-agent guard with published reliability data (guardrails)
- [fstandhartinger/jevbench](https://github.com/fstandhartinger/jevbench) — JevBench v1 for Jev-class models (benchmark)
- [ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang) — Jev-API-compatible open server on SGLang (open reproduction)
- [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) — nano replica with training pipeline (research)
- [LangChain: Building a harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev) — why agent guardrails exploded (writing)
