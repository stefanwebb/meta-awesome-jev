# Vishnurr2k01/awesome-jev
- **One-liner:** Beginner-friendly curated awesome list with a long explainer ("Jev is a smart if statement"), quickstart, when-not-to-use table, official cookbooks/patterns index, articles and glossary.
- **Language(s):** English
- **Type:** curated-list (with strong tutorial front matter)
- **Scale:** ~212 bullet entries. Sections: What is Jev? (one-sentence version, how it fits, three question types, Jev vs LLM, when to use/not, confidence, pricing/latency/limits), 60-second quickstart, Official, Community, SDKs & Clients, Applications, Demos & Games, Agent Tools, Research & Open Models, Cookbooks, Patterns, Articles, Glossary, Related lists.
- **Quality flags:** Hand-curated, good writing. Admits much of its ecosystem index derives from AnotiaWang/awesome-jev. Some vendor-favourable overstatements repeated uncritically: "cannot hallucinate a value", "Structured-output error rate is 0%", "Hallucination: Structurally impossible", "~100 ms typical" (contradicted by punk2898's measurements: 456 ms median, none <100 ms, confidently-wrong answers non-zero — though "hallucination" here means out-of-set values). Does flag vendor benchmarks and features benches where Jev loses. Not promotional.
- **Unique value:** Best index in batch of official TypeSafe cookbooks (17 URLs) and pattern pages (4) with one-line summaries; full response JSON shapes; clear "do not reach for Jev" table; glossary; articles section (explainers, measurements, news incl. The Register, MarkTechPost, DataCamp, LangChain, Langfuse, Flavio Copes); slopsquatting note on PyPI `typesafe-ai`.

## Facts claimed about Jev
- Launched in early access on 15 September 2026. Named after economist William Stanley Jevons. "System One" after Kahneman's System 1/2.
- Response shapes: Noul `{ "type": "noul", "noul": 0.93 }`; Choice `{type, choice, probabilities{...}, confidence}`; Score `{type, score (continuous probability-weighted mean), legend[], probabilities[], confidence}`. Confidence = how peaked the distribution is.
- Questions in a request run in parallel against the same state and don't see each other's answers.
- RLCD = Reinforcement Learning for Calibrated Decisions ("when Jev says 0.7 it's meant to be right ~70% of the time").
- Jev vs LLM table: latency 70-500 ms ("typically ~100 ms") vs 3-30 s (NB other repos quote launch post as 3-329 s); $0.042/M input, output free vs LLM output ~5x input; multi-hop reasoning "weakly".
- Vendor benchmark: TypeSafe four-workflow benchmark Jev 67.8% vs 67.9% GPT-5.6 Terra, "~194x faster and ~445x cheaper" at high end of range. (punk2898 failed to reproduce 445x; fivetaku could not find 67.8 on evals page.)
- Limits: models `jev-latest`, `jev-preview`, pinned `jev-1.13.0`; ~250,000 tokens/s, ~1,200 req/min (early access); max 255 Choice options (hard cap); text-only. Responses report exact model version.
- Access: waitlist gates direct API; Vercel AI Gateway `typesafe-ai/jev` ("no TypeSafe waitlist required") and Cloudflare Workers AI.
- SDKs: `pip install typesafe-sdk` (Python 3.10+; `from typesafe_sdk import Choice, Noul, Score, TypeSafeClient`; `client.system_one(state, questions)`; `response.answers[...]`); `npm install @typesafe-ai/sdk` (`choice, noul, score, TypeSafeClient`; `client.systemOne`). Env `TYPESAFE_API_KEY`. Docs /sdk/python and /sdk/javascript.
- PyPI `typesafe-ai` is a community redirect shim registered to block slopsquatting; real package `typesafe-sdk`.
- Official fan-out pattern page: batching 13 questions in one call measured ~12x cheaper and ~10x faster than 13 sequential calls.
- Official Discord discord.gg/typesafe; console playground console.typesafe.ai/playground; keys at console.typesafe.ai/settings/keys.

## Key insights / patterns
- Mental model: Jev is a component inside a product, placed where code needs one judgment a regex can't express; high confidence -> act, low -> escalate to LLM or human.
- Common production shape: Jev triages everything cheaply; only hard/low-confidence slice reaches an LLM.
- Use when: same judgment at high volume, closed answer set, latency-sensitive loops, want thresholdable numbers, currently paying an LLM for classifier work.
- Avoid / workaround table: math & counting (count in code, ask Jev about the result); dates (extract named parts, resolve in code); writing (LLM); images/audio/video (OCR/transcribe/describe); double negatives, multi-hop (split into atomic questions); >255 options (hierarchical Choice).
- "Numbers, dates and counting stay in code. You pick a card from the deck — you don't ask Jev to name a card."
- Gating policy: confidence > 0.9 act; > 0.5 act with confirmation; else escalate (tune on labels; jevcal).
- Ask atomic questions and combine in code rather than a compound question; a continuous Score like 2.4 carries "torn between" information.
- Pin model version if thresholds tuned.
- Cookbook techniques: BM25 shortlist then per-pair rerank; regex candidates then Jev selects span; line-id Choice + Noul "does an answer exist?"; SDE cascade (mini -> verify -> reasoning); classification-using-confidence (climb hierarchy when unsure); autoresearch (Jev questions as ML features).

## Standout entries
- [Parallel questions cookbook](https://docs.typesafe.ai/cookbooks/parallel_questions) — batch many questions over one state (official cookbook)
- [Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out) — 13 questions ~12x cheaper, ~10x faster (official pattern)
- [Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) — act vs escalate (official pattern)
- [Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification) — beam search past the 255 cap (official cookbook)
- [Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe) — BM25 shortlist + per-pair question (official cookbook)
- [Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails) — screen LLM inputs/outputs (official cookbook)
- [SDE cascade](https://docs.typesafe.ai/cookbooks/sde_cascade) — extraction cascade (official cookbook)
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — known failure modes (official)
- [The Bitterest Lesson](https://typesafe.ai/blog/bitterest-lesson) — TypeSafe essay (official)
- [A deep dive into Jev](https://flaviocopes.com/jev/) — best long-form intro per the list (article)
- [Testing Jev on public and private data](https://amankumar.ai/blogs/jev-measured) — 16,000 calls vs gpt-5.4-mini / gpt-5.6-luna (measurement)
- [Using TypeSafe's Jev for evals](https://langfuse.com/blog/2026-09-18-using-typesafes-jev-for-evals) — Jev as eval judge (article)
- [The Register: TypeSafe AI debuts model that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711) — launch news (news)
- [LitJev](https://github.com/zhengxuyu/litjev) — any Qwen model serving the /v1/systemone schema (open reproduction)
- [PlayJev](https://github.com/OmniJev/PlayJev) — open 0.8B game-playing decision model (open reproduction)
