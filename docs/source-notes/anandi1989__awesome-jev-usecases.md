# anandi1989/awesome-jev-usecases
- **One-liner:** A use-case index of what people actually ship with Jev, grouped by decision shape (Workflow/Bulk/Realtime/Verify/Harness/Voice). Headline metrics are tagged self-reported or independent, and there is a ranked blog list.
- **Language(s):** English
- **Type:** use-case-collection
- **Scale:** About 60 project entries plus about 7 benchmark repos, about 6 open re-implementations, and 15 ranked blogs. Sections: What is Jev · Official Resources · Top Use Cases (Top 7 / Rising 4 with headline results) · Community Builders (01 Workflow, 02 Bulk, 03 Realtime, 04 Verify, 05 Harness, 06 Voice) · Benchmarks (independent / repos / open re-implementations) · Popular Blogs · Contributing. Last updated 22 Sept 2026.
- **Quality flags:** High quality. Every result is tagged `[self-reported]` or `[independent]`, links are scored against a rubric, and SEO recaps are excluded. Nearly all results are self-reported, and it says so. The Voice pillar is "still mostly conceptual" with no shipped repo. Some "canonical examples" (Doom ~10 Hz, Subway Surfers ×50) come from vendor demos. Not promotional.
- **Unique value:** A **decision-shape taxonomy** (Workflow / Bulk / Realtime / Verify / Harness / Voice). Quantified headline results per project. A good ranked reading list of independent and skeptical articles. The vendor eval numbers vs GPT-5.6 Terra. A pointer to the HF Jev Reproductions Tracker.

## Facts claimed about Jev
- Launched **15 Sep 2026**. It is TypeSafe AI's first System One model.
- Latency is 70–500 ms. Pricing is **~$0.042 per million input tokens, output free** (vendor-reported).
- Primitives:
  - **Choice**: up to 255 options. Returns the chosen option, a probability per option and a confidence.
  - **Score**: ordered rubric of 2–10 levels. Returns a probability-weighted score and a confidence.
  - **Noul**: yes/no. Returns a single probability from 0 to 1 (no confidence field is listed).
- Questions in one request are evaluated **in parallel and in isolation** against the same state, so ten questions take about the time of one.
- State can be a string, a JSON object, or a list of text.
- **Vendor four-workflow eval: Jev scores 67.8% agreement with a frontier-model consensus at $0.0004 per case, essentially tied with GPT-5.6 Terra (67.9%) at ~1/76th the cost.** Compare valentynkit ("around 68 percent") and the Classmethod report in wh000wh000 (76.0% vs Luna 76.1%), which may be a different benchmark or metric.
- The Vercel AI Gateway route (`typesafe-ai/jev`) bypasses the waitlist.
- The founder's launch thread (X @CompleteSkeptic, Diogo Almeida) had "~25M views". TechCrunch quotes Vercel and Bryo AI engineers.
- OrcaRouter's audit flags a "75× vs 193×" discrepancy in vendor multipliers. TS2 flags that the "445× cost claim" is self-tested.
- Laya (HF convaiinnovations/laya): Apache-2.0, 3 checkpoints, runs on a free Colab T4, **~30 ms vs Jev ~302 ms but 0.590 vs 0.974 accuracy**.
- Headline results (self-reported):
  - jev-ultrafast: Zürich→London in 7.1 s / $0.0039.
  - jev-trader: 81 ms per block.
  - typesafe-computer-use: $0.0002/decision vs Opus 5 at $0.032.
  - pg-jev: 129 rows in ~1 s for ~$0.0009.
  - mobile-jev: an Uber route in ~21 s / 9 actions.
  - pi-warden: 6 rule breaks down to 0 across 150 paired runs.
  - typesafe-ai-firewall: 0% hard negatives blocked vs 39.2% with a single "is this dangerous?" prompt.
  - jevsearch: Hit@1 83% vs Lunr 41%.
  - tiab-review: 95% recall at 16,645 records.
  - kiarina (Japanese moderation): 36 misses vs OpenAI's 292 on 826 harmful texts.
  - jev-sec-bench: 96.5% accuracy, ECE 0.0588, n=662.
  - TokenTrim: beat GPT-5.4 across 6,257 traces for $1.28.
  - jev-rerank-bench: nDCG@10 0.692 vs Cohere 0.691.
  - Canonical: 1,018 papers into 24 topics for ~$0.08, and 2,000 wine notes into CatBoost features at 1.77 RMSE.

## Key insights / patterns
- **Decompose into atomic questions:** zephel01/Jev-sample shows a 4-option Choice at 48.3% rising to 98.3% when split into four precondition Nouls. typesafe-ai-firewall similarly uses one Noul per hazard instead of one "is this dangerous?" question.
- **Split-rate control:** Jev is advisory at ~2.5 Hz while the safety loop stays in code at 50 Hz (jev-drone). Code owns routes and arithmetic, and Jev picks at branches (Pokémon).
- **"Jev parses, code computes":** CVSS metrics are extracted by Jev and scored deterministically (jev-cvss).
- **Batching:** up to 16 lines per request with page context (jevpdf). Re-rank the top 20 in one request with a Noul per page, a Choice for the best, and a Noul for "any answer?" (jevsearch).
- **Regex for countable rules, Jev for judgment rules** (snifftest). This matches the known weakness in counting.
- Harness pattern: code prefilters candidates (protocol, context window, quota), then a single Jev call picks route plus thinking level. A pinned model skips Jev. Log every turn with its reason and cost (jevonian).
- Fail-open vs fail-closed is an explicit design choice (jev-belay fails open).
- Voice ideas (not yet shipped): spoken command to click in ~300 ms, end-of-utterance Noul, speak-up gates.
- "Rigor does not track reach": the strongest measured results often come from single-digit-star repos.

## Standout entries
- [Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post (official)
- [Models & pricing](https://docs.typesafe.ai/models) — aliases, price, limits (official docs)
- [Workflow evals](https://evals.typesafe.ai) — vendor four-workflow eval (benchmark)
- [Jev on Vercel AI Gateway](https://vercel.com/ai-gateway/models/jev) — waitlist bypass (platform)
- [zephel01/Jev-sample](https://github.com/zephel01/Jev-sample) — quantified atomic-question decomposition (pattern/tutorial)
- [AnshChoudhary/typesafe-ai-firewall](https://github.com/AnshChoudhary/typesafe-ai-firewall) — per-hazard Noul tool-call firewall (security)
- [kylemclaren/jevsearch](https://github.com/kylemclaren/jevsearch) — embedding-free site search rerank (search)
- [Red5d/jev-cvss](https://github.com/Red5d/jev-cvss) — CVSS extraction, code computes (security)
- [youkiti/tiab-review-plugin](https://github.com/youkiti/tiab-review-plugin) — systematic-review screening (bulk)
- [Gaurav-Gosain/jev-sec-bench](https://github.com/Gaurav-Gosain/jev-sec-bench) — prompt-injection/vuln-code benchmark (benchmark)
- [largitdata independent benchmark](https://www.largitdata.com/en/blog/jev-system-one-model-open-source-benchmark/) — RAG routing vs Gemma 4 31B (evaluation)
- [Jev Reproductions Tracker](https://huggingface.co/spaces/multimodalart/jev-reproductions-tracker) — tracks open-weight reproductions (research)
- [OrcaRouter: what we know](https://www.orcarouter.ai/blog/jev-typesafe-system-one-what-we-know) — claim-vs-evidence audit (article)
- [dev.to (Valyu AI): How to Use Jev](https://dev.to/valyuai/how-to-use-jev-a-practical-guide-to-typesafes-system-one-model-g5e) — hands-on tutorial (tutorial)
- [Kingy AI: Jev review](https://kingy.ai/blog/typesafe-jev-review-the-ai-model-that-doesnt-generate-text/) — skeptical counterweight (article)
