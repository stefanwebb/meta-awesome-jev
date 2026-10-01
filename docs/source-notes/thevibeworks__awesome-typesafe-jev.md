# thevibeworks/awesome-typesafe-jev
- **One-liner:** Rigorously reviewed Jev list (1,093 projects, 35 editors' picks with strengths/weaknesses, 70 reads) plus the list's own first-hand latency and failure-mode measurements against jev-1.13.0.
- **Language(s):** English (some Japanese sources listed)
- **Type:** curated-list (AI-reviewed against a rubric, human spot-checked) with original measurements (security/robustness-adjacent "lab")
- **Scale:** 1,093 projects; 2,163 candidates swept → 1,493 passed mechanical gate → 1,340 reviewed → 1,093 listed. Sections: Browser and computer use; Agent tooling; Games and control; Benchmarks and research; Applications and demos; Official; SDKs and integrations; Read and watch (Official docs, Where you can call it, Open models and demos on Hugging Face, Datasets, Hands-on reports, Explainers, Videos, News, Discussion); Measured by us; Other lists; How entries get in. GitHub Pages site with media.
- **Quality flags:** Among the most trustworthy lists. Every editor's pick has "Why it is here" and "Know before you use it" (candid weaknesses: e.g. "timings are three repeats of one task", "self-built and self-scored"). Numbers from READMEs are reported as claims. Transparent that reviews were done by AI reviewers with human spot checks. Stars explicitly not a criterion. No fabricated-looking links observed.
- **Unique value:** (1) **Original lab measurements** (lab/probe_breaks.py, probe_latency.py with raw JSON). (2) Skeptical press/explainer curation that surfaces caveats (eval labels from LLMs, "0% hallucination" not empirical, InstructGPT co-author not ChatGPT inventor). (3) Hugging Face open reproductions and datasets with each card's reported numbers. (4) Official cookbook results with numbers. (5) Provider list (Cloudflare, Netlify, Vercel AI SDK).

## Facts claimed about Jev
- Models page (per list): jev-1.13.0, **$0.042 per million input tokens, free output**, rate limits, **64k context (32k for state)**, text-only input.
- Cloudflare AI model page for typesafe/jev lists a **32,000-token context** (contrast with 64k on TypeSafe's page — likely the state limit; flag).
- API: POST /v1/systemone with body `state`, `model`, `questions`. Python `client.system_one(state=..., questions=...)`, install `uv add typesafe-sdk`; JS `systemOne`, ships ESM + CommonJS + declarations.
- Vercel AI SDK `@ai-sdk/typesafe-ai`: `experimental_evaluate` with choice, score and **boolean (Noul)** questions.
- Netlify AI Gateway serves Jev (2026-09-17 changelog) via @typesafe-ai/sdk with no key setup, billed to Netlify credits.
- system-one-adapter-python: same system_one API answered by OpenAI or Anthropic models; LLM probabilities are not calibrated.
- Official cookbook numbers: Parallel questions — 13 questions over GDPR article, one batched call **12.2x cheaper and 10.0x faster** than 13 single calls; Re-ranking — CLERC legal, 30-passage BM25 shortlists, 40 queries: **top-1 5%→18%, top-10 38%→62%**.
- Launch claims (via press): **193.6x faster / 444.6x cheaper** from TypeSafe's own evals (PC Watch); TypeSafe raised **$40M** (The Register); Latent Space ">100x faster, >200x cheaper than small frontier LLMs"; Anthony Maio: Jev **67.8% vs GPT Sol 74.1%** on TypeSafe's evals; Warmer Sun: eval labels come from two LLMs, 0% hallucination not empirical, no paper or weights. Founder Diogo Almeida is one of ~20 InstructGPT co-authors.
- HN launch thread: 1,871 points, ~490 comments (Li-Evan says ~2,000/~500 — snapshot difference).
- TypeSafe has released no weights. HN commenter claims prior art: arXiv 2503.23303 (March 2025) non-autoregressive probability design.
- **Measured by us (jev-1.13.0, 2026-09-18):** "strawberry has exactly three r" → yes 0.60; "exactly two" → yes 0.79. One-Noul-per-item counting got 11/12 (miss "lime" at 0.32). 33 known-answer cases: controls 4/4, dates 6/6, negation/indirection 6/6, adversarial 4/4, arithmetic 5/6, counting 5/7; arithmetic answers sat near 0.5. Latency: fastest ~250 ms up to 25 questions; medians 310 ms (1 question) to 4.7 s (200 questions), highly time-variable. 3-question quickstart billed 424 input tokens ≈ $0.000018.
- Hands-on: Near Here — Jev 48/50 vs Gemini 3.5 Flash-Lite 43, Mistral Small 4 42, at 0.59 s and $0.043 per 1,000 decisions. mizchi gomoku ~500 ms/move. jev-browse: 30/30 at 4.4 s median, $0.0009/task vs Claude Code 9.4 s, $0.0679. typesafe-computer-use: $0.0002 and 0.13–0.38 s per decision vs $0.032 and 5.2 s for frontier.
- Dataset jev-tree-choice-cap: tests the **255-option Choice cap**; tree walk 180/180 vs 90/180 when truncating to 255.
- Contradictions: official "~100 ms" vs measured 250–310 ms minimum; context 64k vs Cloudflare 32k.

## Key insights / patterns
- Counting/arithmetic are genuinely weak; decompose into one Noul per item and sum in code. Near-0.5 probabilities are a usable "don't trust this" signal for arithmetic.
- Batch many questions per call: latency roughly flat up to ~25 questions, but grows to seconds at 200.
- Taxonomies beyond 255 options: walk a tree rather than truncate.
- Browser/computer-use pattern: build a numbered item list (OCR + accessibility tree / indexed DOM / sightmap components); Jev picks action + target; a writer model only handles free text. Beware: page content and supplied passwords are sent to the API every step.
- Confidence and margin gates with escalation (jev-mobile).
- Skeptic view (Sean Goedecke): prefill a normal LLM and sample one constrained token gets much of the speed (2–3x on Qwen2.5-1.5B); doubts a technical moat. Anthony Maio: calibrated individual answers need not compose into a calibrated workflow.
- Log triage caution: jevlogs 0.993 HDFS recall but only 0.84% of lines filtered out.
- Open reproductions mostly: parallel constrained decoding over unchanged LLMs (big speedups, lower field accuracy e.g. 72.2% vs 94.4% AR JSON), LoRA scorer heads with temperature scaling (ECE ~0.02–0.05), DeBERTa/ModernBERT classifiers.

## Standout entries
- [Models](https://docs.typesafe.ai/models) — official model card with price/limits (official docs)
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — official weak spots (official docs)
- [Parallel questions cookbook](https://docs.typesafe.ai/cookbooks/parallel_questions) — 12.2x cheaper / 10.0x faster batching (official cookbook)
- [Re-ranking cookbook](https://docs.typesafe.ai/cookbooks/rerank_typesafe) — legal reranking results (official cookbook)
- [Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails) — hazard screening cookbook (official cookbook)
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) — same API backed by OpenAI/Anthropic (official)
- [AI SDK Providers: TypeSafe](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai) — Vercel AI SDK provider docs (integration)
- [Jev (typesafe) on Cloudflare](https://developers.cloudflare.com/ai/models/typesafe/jev/) — Workers AI access (provider)
- [thevibeworks lab](https://github.com/thevibeworks/awesome-typesafe-jev/tree/main/lab) — first-hand probes and raw results (benchmark)
- [Typed Decisions, Not Chat](https://warmersun.com/jev/) — launch claims vs TypeSafe's own footnotes (analysis)
- [Jev means structured output is interesting again](https://www.seangoedecke.com/jev-means-structured-output-is-interesting-again/) — skeptical technical take (analysis)
- [Near Here event validation test](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation) — Jev vs Gemini/Mistral hands-on (benchmark)
- [jev-reproductions-tracker](https://huggingface.co/spaces/multimodalart/jev-reproductions-tracker) — grid of open reproduction attempts (directory)
- [jev-browse](https://github.com/kyrylosyzonenko/jev-browse) — browser agent with rerunnable eval (project)
- [jev-tree-choice-cap dataset](https://huggingface.co/datasets/reachjalil/jev-tree-choice-cap) — tests 255-option cap (dataset)
