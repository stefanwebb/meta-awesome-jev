# yzfly/awesome-jev-zh
- **One-liner:** Chinese-language curated Jev list with hands-on measurements, access-channel comparison, gotcha list, local-deployment benchmarks, and a sober "calm view" of independent evals.
- **Language(s):** Chinese (Simplified); a few Japanese article links
- **Type:** curated-list (with strong tutorial/study-guide content)
- **Scale:** ~470 table rows. Sections: 官方资源 (Official resources) · 优质项目 (>500★ projects) · Jev 是什么 · 体验渠道 (access channels) · 上手 (quickstart) · 规格与定价 (specs & pricing) · 该用与不该用 (when/when not) · 中文指南 · 热门项目自动榜 (daily auto-collected hot list) · SDK 与客户端 · 应用 · Demo · Agent 工具 · 复现与评测 (reproductions & evals) · Cookbook 与模式 · 文章 · 社区 · 其他 awesome 列表 · 冷静看待 (calm view). Plus docs/quickstart.md, docs/concepts.md, slide explainer at code.jiangshu.ai/awesome-jev-zh/.
- **Quality flags:** High quality, first-person, original measurements (dated 2026-09-19) clearly labelled "实测" vs "官方". Hot-list section is auto-collected daily (GitHub Action + denylist). Maintainer discloses self-promotion (yzfly/edgejev). Measurements are small-n and flagged as such.
- **Unique value:** Original Chinese-language evals (15-ticket test; batch vs single accuracy); access-channel comparison with measured latencies; detailed gotcha list for Vercel AI Gateway; replication of laya-vs-Jev claims (partially contradicting the author); local deployment table (laya, kev, SemIf, EdgeJev CPU/ONNX quantization findings); full official cookbook table; media & Japanese article index; best "skeptic" summary of phishing/spam benchmarks.

## Facts claimed about Jev
- Early access opened **2026-09-15**. Official response latency **70–500 ms**; input **$0.042/MTok**, output free ("too cheap to meter").
- Specs table (from docs.typesafe.ai/models): Jev 1.13 · `jev-1.13.0`, aliases `jev-latest` / `jev-preview`; context **64k per request, state + longest question ≤ 32k**; Choice max **255** options; rate limits **250,000 tokens/s · 1,200 requests/min**; text-only (no image/audio/video); endpoint `POST https://api.typesafe.ai/v1/systemone`.
- Python: `pip install typesafe-sdk`; `from typesafe_sdk import Choice, Noul, Score, TypeSafeClient`; `client.system_one(state=..., questions={...})`; Choice `criteria` is a dict of option→description, Score `criteria` is a list of levels, Noul has only `instructions`. Response example: `{"model":"jev-latest","answers":{"department":{"type":"choice","choice":"billing","confidence":0.596},"frustration":{"type":"score","score":1.035,"confidence":0.842},"is_urgent":{"type":"noul","noul":0.999}},"usage":{"input_tokens":312,"output_tokens":48}}` (output tokens counted but not billed).
- JS: official package **`@typesafe-ai/sdk`**; npm `typesafe-sdk` is an unrelated 0.0.0 placeholder. Skills: `claude plugin marketplace add typesafe-ai/skills`, `claude plugin install typesafe@typesafe-ai`, `npx skills add typesafe-ai/skills --skill typesafe-ai`.
- Vercel AI Gateway: model `typesafe-ai/jev`; requires credit card (else `403 customer_verification_required`), $5 free credit; native endpoint `POST /v1/evaluate`; **Noul is called `boolean`** on the Gateway and returns `probability`; not usable via `/v1/chat/completions` ("is an evaluation model, not a language model"); AI SDK `ai` ≥ 7.0.103 for `experimental_evaluate`, or `@ai-sdk/typesafe-ai`; Gateway metadata reports `context_window` 32000 and `max_tokens` 0. Measured latency 310–370 ms.
- **OpenRouter**: model page `typesafe/jev-1.13` exists but on 2026-09-19 `/api/v1/models` (446 models) did not include Jev — "don't count on it yet". (Contradicts/predates other lists that describe OpenRouter Decisions as working.)
- classifier.dev: free no-key classifier built on `jev-1.13.0`; labels only; up to 1,000 inputs per batch; measured 220 ms single / 20 ms per item batched; silently falls back to LLMs if Jev unavailable; free tier 3,000/min, 20,000/day (fast), Pro $20/month.
- Official demos: Doom at 10 queries/s ≈ **$7/hour**; browser-use flight booking **7 s / $0.0039**. "193x faster" is TypeSafe's self-reported upper bound. TypeSafe emerged from stealth with **$40M** funding (Yahoo Finance). HN launch thread "1500+ points".
- Official blog posts: launch post, "The Bitterest Lesson", "AI: too good to be true, too bad to be useful", Manifesto. Docs also: use-case map, ML primer, legal, llms.txt.
- Independent benchmarks: jev-phishing-bench (2,000 emails): direct question **62.6%** vs Claude Haiku 4.5 81.3%, two-line regex 91.8%, **5 signal questions + logistic regression 95.0%** (Haiku with same decomposition 93.2%); 239 ms vs 687 ms; $0.038 vs $0.462 per 1,000. jev-spam-eval (18,514 emails): written definition 98.3% vs TF-IDF 98.4%; on 2026 drifted mail Jev 97.3% vs TF-IDF 72.5%. judgekit (Chinese, 130 items): 97.7% (CI 93.4–99.2) @ ~890 ms, ¥0.105/1k, keyword baseline 91.5%. kev-4b 0.790 vs Jev 0.857 (764 items); kev-8b 0.77 vs 0.86. Nimble 90.1% vs Jev 93.2%. WindTunnel: Jev + Mercury 2.5 via WebMCP 49/49, $0.0011, 3.2 s. jevbench: 534 frozen questions, 42 result rows.
- Maintainer's own tests: 15 Chinese tickets, routing 14/15 & urgency 14/15, latency 281/370/448 ms (min/median/p95); **batched 15/15 vs one-by-one 80%**; confidence saturates at 1.00 on Chinese (12/15). Label-only vs described labels: 80.0% → 93.3%. Replication: AG News laya 92.8% vs Jev 85.5%; emotion laya 54.0% vs Jev 61.5% (contradicts laya author's claim).

## Key insights / patterns
- `choice` tells you what; `confidence` tells you whether to act — don't execute on low confidence (doc's own example is 0.596).
- Decompose compound judgments into atomic signals and combine in code (62.6% → 95.0%). Traditional baselines (regex, TF-IDF) remain strong; Jev's durable advantages are cost, latency, and robustness to distribution shift.
- Option descriptions matter a lot (+13.3 pts); prompt/option-description effects don't transfer between models.
- Batching may improve accuracy, not just cost (unverified observation).
- When NOT to use: text generation, summaries, explanations, multi-step reasoning, low-frequency calls (not worth another vendor), narrow tasks with labeled data (measure baselines first). Open-ended extraction → regex candidates then Jev picks.
- "Can't hallucinate" only means no schema violation / no invented options; wrong choices still happen.
- Local deployment: laya-multilingual (322M, 32.8 ms T4) is the only real-time option; kev offers API-compatible `/v1/systemone` (swap `base_url`); localjev is "wire-compatible, but not mathematically equivalent" (self-reported probs). Quantization gotchas (EdgeJev): dynamic int8 makes outputs batch-dependent; use QInt8 not QUInt8 on x86 VNNI; `max_loaded=1` causes 7–10 s reloads when switching languages.
- Vercel spend management doesn't stop AI Gateway usage — use Gateway Budgets; buying credits removes monthly free credit.
- Use official system-one-adapter as fallback against single-vendor risk.

## Standout entries
- [Models](https://docs.typesafe.ai/models) — IDs, pricing, context & rate limits (official)
- [Confidence](https://docs.typesafe.ai/confidence) — confidence semantics (official)
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — known failure modes (official)
- [The Bitterest Lesson](https://typesafe.ai/blog/bitterest-lesson) — TypeSafe position essay (official)
- [Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook) — standard open-extraction recipe (cookbook)
- [classifier.dev](https://classifier.dev/) — free no-key Jev classifier (access channel)
- [Vercel AI Gateway – Jev](https://vercel.com/ai-gateway/models/jev) — gateway access (access channel)
- [anisselbd/jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench) — rigorous phishing benchmark (benchmark)
- [bitnovus/jev-spam-eval](https://github.com/bitnovus/jev-spam-eval) — spam eval with distribution drift (benchmark)
- [fstandhartinger/jevbench](https://github.com/fstandhartinger/jevbench) — broadest third-party cross-eval (benchmark)
- [lexingtonhibiki/judgekit](https://github.com/lexingtonhibiki/judgekit) — first Chinese-language eval (benchmark)
- [nekuda-ai/WindTunnel](https://github.com/nekuda-ai/WindTunnel) — WebMCP agent benchmark (benchmark)
- [yzfly/edgejev](https://github.com/yzfly/edgejev) — CPU/ONNX local Jev-compatible serving (tool)
- [Typed Decisions, Not Chat](https://warmersun.com/jev/) — separates claims from evidence (article)
- [JackZeng/Jev_apps](https://github.com/JackZeng/Jev_apps) — 129 case studies with evidence grading, bilingual (case library)
