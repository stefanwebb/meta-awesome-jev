# Promethe-us/awesome-jev
- **One-liner:** Rigorous, source-audited bilingual field guide to Jev: specs, gateway integration matrix, timeline, ~21 arXiv papers with author-reported numbers, evaluations, hands-on and robotics guides.
- **Language(s):** Chinese (README.md, docs/*.md) and English (README_EN.md, docs/*_EN.md); GitHub Pages web guide
- **Type:** curated-list (with tutorial/study-guide and papers-list components)
- **Scale:** ~157 links in README_EN; docs: CATALOG (~30KB), RESEARCH (~42KB), SOURCES (audit log), HANDS_ON, INSTALLATION, ROBOTICS. README sections: Latest changes, Jev in 30 seconds, Where Jev fits in an agent loop, Integration quick reference, Timeline, Web guide/Hands-on/Robotics, Official resources, Selected X posts, Xiaohongshu leads (+Zhihu), GitHub ecosystem, Evaluations and limitations, Papers, In-depth articles, FAQ. Source audit claims 219 external URLs / 65 repos link-checked on 09-24.
- **Quality flags:** Very high quality: hand-curated, dated (full audit 2026-09-24, incremental to 09-28), distinguishes official vs author-reported vs unverified; explicitly says it did not reproduce paid experiments. Xiaohongshu entries are leads without verifiable body text. Minimal promo. Star counts are snapshots (laya ★19,984 here vs ★17,709 in heyjunpenn — dates differ).
- **Unique value:** Best single source in batch for hard specs (limits, rate limits, aliases), gateway-by-gateway identifiers and schema differences, a verified arXiv paper table with numbers, a nine-item jaggedness summary, runnable Python/TS/cURL first calls, and a robotics placement guide.

## Facts claimed about Jev
- Launch **2026-09-15** (early access), launch post https://typesafe.ai/blog/introducing-system-one-models-and-jev. Company TypeSafe AI founded by Diogo Almeida, Erik Gafni, Sasha Sheng; **$40M seed led by DCVC** (BusinessWire press release).
- Model **`jev-1.13.0`**; aliases `jev-latest` and `jev-preview` both pointed to it (docs.typesafe.ai/models).
- Price **$0.042 per million input tokens**; output tokens not billed.
- Limits: **64k tokens per request**; **32k tokens for `state` + longest single question**. Text only (string, JSON object, text array); no image/audio/video. Rate limits **250,000 tokens/second, 1,200 requests/minute** (dynamic). English performs best.
- Primitives: Choice (option + all probabilities + `confidence`, **up to 255 options**), Score (ordered levels + probabilities + confidence), Noul (probability of yes, **no separate `confidence` field**). `confidence` is computed from the distribution, not self-assessment.
- Name refers to William Stanley Jevons; "System One" borrows from *Thinking, Fast and Slow*.
- API: `POST https://api.typesafe.ai/v1/systemone`, Bearer `TYPESAFE_API_KEY`; request `{state, model, questions:{name:{type:"choice", instructions, criteria:{...}}}}`. Python `pip install typesafe-sdk` → `from typesafe_sdk import Choice, Noul, TypeSafeClient`; `client.system_one(state=..., questions=...)`; `result.answers["q"].choice/.confidence/.noul`; JS `npm install @typesafe-ai/sdk`, `client.systemOne`, `choice(...)`. Python SDK **v0.7.1** (Sept 21: earlier key validation, no key in exception logs).
- Access: waitlist removed **21:30 UTC Sept 20**; **$5 starting credit** (~120M input tokens). Status incidents Sept 20, 21, 23 (status.typesafe.ai). Discord discord.gg/typesafe; docs index docs.typesafe.ai/llms.txt; cookbooks docs.typesafe.ai/cookbooks; patterns /patterns/confidence-routing, /patterns/intent-routing.
- Gateways & IDs: Vercel AI Gateway `typesafe-ai/jev` (AI SDK 7 `experimental_evaluate`, `POST /v1/evaluate`, TypeSafe-compatible base URL `https://ai-gateway.vercel.sh/typesafe` → `/typesafe/v1/systemone`; AI SDK calls it `boolean` not `noul`); Vercel temporary free promo ended by Sept 28; Vercel: ~13% of paying teams adopted on day one. Cloudflare Workers AI `typesafe/jev`; OpenRouter page lists Jev 1.13, TanStack uses `~typesafe/jev-latest`; LangSmith Gateway `typesafe/jev-1.13.0`; TanStack AI `decide()` with choice/score/boolean; Pydantic AI `TypeSafeModel`; Vercel eve `auto`/`evaluate` default `typesafe-ai/jev`; Composio, Rig (experimental Rust), Ax. LangSmith's separate hosted `semif-qwen3.5-4b` free through Sept 28 (not Jev).
- No official Jev/RLCD paper found; no official weights.
- Vendor claims **193.6× faster, 444.6× cheaper** — specific workflows, "lean toward the high end."
- Official jaggedness (docs.typesafe.ai/model-jaggedness/jev-1.13), nine areas: literal interpretation, numerical computation, date comparison, multi-step indirect reasoning, irrelevant long context, adversarial content, instruction/option conflicts, cross-question identity failures (two opposite Noul questions may not sum to 1), text generation.
- Evaluations: Chinese study 31/40 tickets correct (yibie/laya-jev-lab); Huxiu hands-on 50 CS questions ×4 ×15 reps ≈64–65% correct, ~0.73 s/question, threshold flip-flopping (1.99 vs 2.00 cutoff); jev-as-a-judge "100% agreement" = 5 fixed traces; jev-codex-router ~−60% saving from simulation of 237 turns, not bills.
- Papers (author-reported): 2609.22753 edge orchestration (latency −15.9–26.5% vs DeepSeek; fees/correct −69–70.6%; cache erases gap); 2609.23136 6G (latency −22.4% vs DeepSeek, −61.9% vs Gemini; 459/1,080 vs DeepSeek 463, Qwen 435); 2609.24052 Texas crash narratives (499,500 screened, 195,857 coded, 27-question schema, F1 0.908 vs 2,416 human judgments); 2609.24965 scientific decisions; 2609.23986 Jev-Mem (LoCoMo 0.777, 158 s, 6.6×); 2609.26532 REFLEX (95% success, 72.7% fewer strong-model calls); 2609.26550 JEV-as-a-Judge (within 3 pp of best of 16 judges at ~0.36% fee; cascade keeps 99%); 2609.23959 CallScreenBench JevLite (AUROC 0.974, 64.5 ms); 2609.24395 JEVQA (Pearson 0.737/0.824); 2609.25845 Visual Jev (8.9× at 32 q/image); 2609.23886 this-that-model-1.0 (~2B, 30.9 ms; 0.941 vs Jev 0.765 on 68 questions, but 0.560 vs Jev 0.98–1.00 on multi-step arithmetic); 2609.24574 CSS annotation (18 tasks, 7,977 items, trails best LLM on 14/15, median −11.6 macro-F1, ~1/44 cost; routing matches LLM at 1/4–1/2 cost); 2609.26758 Type-Safe Is Not Error-Free (option-name swap AUC 0.94→0.23 in open models; hosted Jev 0.8146→0.5806; type-error rate 0%). Later: 2609.28613 Decision Hijacking (prompt injection), 2609.29429 Just Ask Jev, 2609.29769 JEV vs LLM rubric judges (correlated errors), 2609.27607 radiology, 2609.27678 legal, 2609.30186 Jev-Mobile, 2609.27331 JEV-Star (StarCraft II), 2609.30243 JevOut, 2609.28940 pentest harnesses, 2609.28919 enterprise coding-agent routing, 2609.30216 Jev in the Wild.

## Key insights / patterns
- Jev is a **decision layer**, not a generative layer: generative model proposes → Jev routes/scores/verifies/gates → application code enforces permission/fallback/action. Placements: model routing, tool approval, stopping, verification against rubric, memory/retrieval gating.
- Jev is **not a security boundary**, not auth, not a robot safety controller; typed ≠ correct; confidence ≠ calibrated correctness.
- Hands-on loop: narrow task → Playground with 3–10 samples → versioned state/questions → SDK call → low-confidence fallback + log → held-out threshold validation. Include `other`/`unknown` options; treat untrusted text as data. Avoid first tasks involving reply writing, summaries, arithmetic, permission approval, safety actions.
- Log: state summary, question version, option order, returned model, probabilities, threshold, action, human correction. Pin model version for comparisons.
- Test checklist: class coverage, negation, missing fields, prompt-injection text, option name/order sensitivity, high-confidence errors, p50/p95.
- Migration gotcha: gateways differ (noul vs boolean, `/v1/evaluate` vs `/v1/systemone` schemas); don't assume equivalence.
- Robotics: low-rate bounded semantic choices (select registered skill, retry, triage); never pixels, continuous motion, or final safety; stale observations → deterministic reject/hold.
- Caching can erase Jev's latency advantage (edge-orchestration paper); cascades (confident→accept, else escalate) are the recurring cost/accuracy winner.

## Standout entries
- [TypeSafe launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — official launch and methodology (official)
- [Models](https://docs.typesafe.ai/models) — versions, pricing, limits (official)
- [Jev 1.13 known limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — jaggedness guide (official)
- [Confidence](https://docs.typesafe.ai/confidence) — semantics of confidence (official)
- [Vercel AI Gateway TypeSafe-compatible API](https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe) — gateway integration (integration)
- [Pydantic AI TypeSafe model docs](https://pydantic.dev/docs/ai/models/typesafe/) — framework integration (integration)
- [TanStack AI Evaluate](https://tanstack.com/ai/latest/docs/evaluate/evaluate) — multi-provider decide() (integration)
- [LangSmith decision-model gateway](https://docs.langchain.com/langsmith/llm-gateway-decision-models) — LangChain integration (integration)
- [Type-Safe Is Not Error-Free](https://arxiv.org/abs/2609.26758) — option-name sensitivity (paper/robustness)
- [Decision Hijacking](https://arxiv.org/abs/2609.28613) — prompt injection on typed decisions (paper/security)
- [JEV-as-a-Judge](https://arxiv.org/abs/2609.26550) — confidence cascade judging (paper)
- [Evaluating Decision Models for Text Annotation in CSS](https://arxiv.org/abs/2609.24574) — 18-task benchmark (paper)
- [Latent Space × Diogo Almeida](https://www.latent.space/p/jev) — founder interview (interview)
- [Simon Willison: Decision Models](https://simonwillison.net/2026/Sep/21/jev/) — analysis (article)
- [Archestra: 100 real agent calls](https://archestra.ai/blog/we-tested-jev-on-100-real-agent-calls) — tool-call evaluation (evaluation)
