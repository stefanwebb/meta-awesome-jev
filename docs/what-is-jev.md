# What Jev Is: A Reconciled Reference

> Jev was the first Jev-like model and is still the most-tested one; its docs define the `/v1/systemone` interface that the rest of the family copies. For the wider family, see [open-models.md](open-models.md).
>
> This page covers the facts about Jev that the 106 source lists agree on, where they disagree, and which version to trust. Snapshot as of **2026-09-30**. Official pages change fast, so treat [docs.typesafe.ai/models](https://docs.typesafe.ai/models) and [the API reference](https://docs.typesafe.ai/api) as the final word.

[← back to the main list](../README.md)

## Contents

- [In one paragraph](#in-one-paragraph)
- [The three primitives](#the-three-primitives)
- [Specs, pricing and limits](#specs-pricing-and-limits)
- [The API contract](#the-api-contract)
- [Official SDKs](#official-sdks)
- [Where you can call Jev](#where-you-can-call-jev-access-routes)
- [Known weaknesses (the official "jaggedness" list)](#known-weaknesses-the-official-jaggedness-list)
- [The company and the launch](#the-company-and-the-launch)
- [Timeline](#timeline)
- [Vendor claims vs. independent measurement](#vendor-claims-vs-independent-measurement)
- [Contradictions across sources, resolved](#contradictions-across-sources-resolved)
- [Common misinformation](#common-misinformation)

## In one paragraph

Jev is TypeSafe AI's first **System One model**. The name "System One" comes from Kahneman's fast, intuitive System 1, and "Jev" comes from the economist William Stanley Jevons and the Jevons paradox. Jev is **not a chat model, and it never generates text**. You send it a piece of **state** (a string, a JSON object, or an array of text) plus a map of **typed questions**. It returns one **typed answer per question** as a probability distribution. All the questions are evaluated **in parallel and in isolation** against the same state. According to TypeSafe, the model is trained with **RLCD, "Reinforcement Learning for Calibrated Decisions"**, and uses a new architecture with a **parallel sampler**. The weights, architecture and parameter count are unpublished. There is no paper, and Jev is available only as a hosted API. TypeSafe positions it as a decision layer that sits *inside* software: "the answer tells you *what*; confidence tells you *whether to act*." Code owns control flow, thresholds, arithmetic and side effects.

## The three primitives

| Primitive | Asks | You supply | Returns | Notes |
|---|---|---|---|---|
| **Choice** | "Which one?" | `instructions` + `criteria` as a **map** of `option → description` | `choice`, `probabilities` (one per option), `confidence` | Up to **255 options**. The probabilities always sum to 1, so **always include an `other`/`none`/`unclear` option**. Beyond 255 options, use a hierarchical Choice or beam search ([cookbook](https://docs.typesafe.ai/cookbooks/hierarchical_classification), [jev-tree](https://github.com/reachjalil/jev-tree)). |
| **Score** | "Where on this scale?" | `instructions` + `criteria` as an **ordered list** of level descriptions | `score` (probability-weighted, 0-indexed, can fall between levels, e.g. `1.05`), `legend`, `probabilities`, `confidence` | **2–10 levels**. Write each level as a concrete situation, not "low/medium/high". |
| **Noul** | "Is this true?" | `instructions` (and optionally `criteria: {true, false}`) | `noul`: the probability, from 0 to 1, that the answer is yes | **No `confidence` field.** 0.5 means "can't tell", not "medium". The Vercel AI SDK, TanStack and eve call this type **`boolean`** and return `.probability`. |

**Confidence** applies only to Choice and Score. It is a statistic computed from the distribution. The [docs](https://docs.typesafe.ai/confidence) illustrate it with `(n·p_max − 1)/(n − 1)`, so it adds no information beyond the top probability. It is **not** the probability that the answer is correct ([docs](https://docs.typesafe.ai/confidence)). Probabilities are reportedly quantised to two decimals.

## Specs, pricing and limits

| Item | Value | Source / caveat |
|---|---|---|
| Current model | `jev-1.13.0` (also seen as `jev-1.13-20260917` on OpenRouter) | [Models page](https://docs.typesafe.ai/models). One list saw a `jev-1.14` reference on 09-19, which is unconfirmed. |
| Aliases | `jev-latest`, `jev-preview`, both → `jev-1.13.0` | Aliases move. **Pin the versioned ID** whenever thresholds matter, and log the `model` field that each response returns. |
| Price | **$0.042 per 1M input tokens; output is free** ($42 per billion) | Vendor. Independently confirmed: 1,154,813 tokens were billed at $0.0485 ([awesome-jev-verified](https://github.com/punk2898/awesome-jev-verified)). Jev counts roughly **2×** the tokens a GPT tokenizer does for the same text, and each request carries about **261 tokens** of fixed overhead ([jev-fanout-bench](https://github.com/blowxian/jev-fanout-bench)). The founder has said launch pricing may be subsidized. |
| Context | **64k tokens per request** (state + all questions); **32k for state + the longest single question** | Models page. Gateways (Cloudflare, OpenRouter, Vercel metadata) advertise **32k**. Several lists that say "32k context" are quoting the state budget. |
| Rate limits (jev-1.13) | **100K tokens/s and 40 requests/s** on the live [Models page](https://docs.typesafe.ai/models) as of 2026-09-30. Launch-week snapshots, which almost every source list quotes, said **250,000 tokens/s and 1,200 requests/min**. | TypeSafe says limits "are adjusting dynamically" while GPU capacity lands. Over-limit requests return 429 with `retry-after`, and the SDKs retry with backoff. Higher limits via sales@typesafe.ai. |
| Latency (vendor) | "70–500 ms end to end" (the docs also say "~100 ms for most queries") | Measured from US West Coast laptops. |
| Latency (independent) | server-side floor ~**190–250 ms**; end-to-end medians **250–650 ms**; roughly flat up to ~25 questions per call, then rising (4.7 s at 200 questions) | [awesome-jev-verified](https://github.com/punk2898/awesome-jev-verified), [thevibeworks lab](https://github.com/thevibeworks/awesome-typesafe-jev/tree/main/lab), [rhc98 calibration](https://github.com/rhc98/awesome-jev) (p50 210 ms / p90 337 ms over 3,683 calls). No one reproduced "sub-100 ms". |
| Input modalities | **Text only** (string, JSON object, array of text values) | Images, audio and video must first be converted to text (OCR, accessibility tree, a VLM description). "Visual Jev" and similar projects are independent. |
| Streaming / sampling params | None: no `temperature`, `max_tokens` or streaming | |
| Language | English is the primary language | Accuracy and calibration drop on non-English *state*: Russian −11 pp, Korean −6.5, Spanish −3 to −6, and Spanish roughly doubles ECE ([robustness list](https://github.com/Yifan-Lan/awesome-jev-robustness)). |
| Fine-tuning | None. One set of weights serves every account. | Customer data is reportedly not used for training (not audited). Zero data retention (ZDR) is available for enterprise customers and through Vercel `providerOptions`. |
| Compliance | No SOC 2 / ISO 27001 listed at launch; hosted only, with no on-prem or VPC option | Per [Awesome-llms-labs](https://github.com/Awesome-llms-labs/awesome-jev). |

**Cost rule of thumb** ([dog-last/awesome-jev](https://github.com/dog-last/awesome-jev)): `monthly $ ≈ daily calls × avg input tokens × 30 × 0.042 / 1,000,000`. For example, 100k calls/day × 500 tokens ≈ **$63/month**. A typical ~400-token decision costs ~$0.000017.

## The API contract

```http
POST https://api.typesafe.ai/v1/systemone
Authorization: Bearer $TYPESAFE_API_KEY
Content-Type: application/json

{
  "model": "jev-1.13.0",
  "state": { "ticket": "My card was charged twice and support hasn't replied in 3 days." },
  "questions": {
    "department": { "type": "choice", "instructions": "Which team should handle this ticket?",
                    "criteria": { "billing": "Payments, charges, refunds", "technical": "Bugs and outages", "other": "Anything else" } },
    "frustration": { "type": "score", "instructions": "How frustrated is the customer?",
                     "criteria": ["Calm", "Frustrated but civil", "Angry or threatening to leave"] },
    "is_urgent":   { "type": "noul",  "instructions": "Does this ticket need a reply within the hour?" }
  }
}
```

```json
{
  "model": "jev-1.13.0",
  "answers": {
    "department":  { "type": "choice", "choice": "billing", "probabilities": { "billing": 0.91, "technical": 0.05, "other": 0.04 }, "confidence": 0.87 },
    "frustration": { "type": "score", "score": 1.05, "legend": ["Calm", "Frustrated but civil", "Angry or threatening to leave"], "probabilities": [0.12, 0.71, 0.17], "confidence": 0.84 },
    "is_urgent":   { "type": "noul", "noul": 0.93 }
  },
  "usage": { "input_tokens": 312, "output_tokens": 48 }
}
```

*(The values are illustrative. The shape is taken from the docs, and the numbers are typical of those reported across the lists. `output_tokens` is reported but not billed.)*

- Question IDs are **not sent to the model**, so put the full meaning in `instructions`. You can reference nested state with paths such as `` `state.ticket` ``.
- `GET /v1/models` lists the available models.
- The pre-launch preview API (`/preview/evaluation`) was migrated to v1. The migration page ([wh000wh000](https://github.com/wh000wh000/awesome-jev-live) summarizes it) is no longer in the live docs index. The `prompts` array became the `questions` map, and `responses` became `answers`. `probability` became `noul`, `chosen` became `choice`, `expectation` became `score`, and Choice probabilities changed from an array to a map.
- Error codes you will see: 400, 401 (bad key), 402 (credits or verification required), 403 (no Jev access), 429 (rate limited), and 529 (overloaded).

## Official SDKs

| | Python | JavaScript / TypeScript |
|---|---|---|
| Package | `pip install typesafe-sdk` / `uv add typesafe-sdk` (Python ≥ 3.10) | `npm install @typesafe-ai/sdk` (Node ≥ 20, ESM + CJS + types) |
| Repo | [typesafe-ai/typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) | [typesafe-ai/typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) |
| Call | `TypeSafeClient().system_one(state=..., questions={...})` (also `AsyncTypeSafeClient`) | `new TypeSafeClient().systemOne({ state, questions })` |
| Builders | `Choice`, `Score`, `Noul` classes | `choice()`, `score()`, `noul()` helpers (answer types inferred) |
| Answers | `response.answers["x"].choice` / `.noul` / `.score`, or the typed views `response.choices[...]` / `.nouls[...]` / `.scores[...]` (used in the official docs) | `response.answers.x.choice` |
| Extras | `RetryPolicy(max_retries, backoff_initial, backoff_max, timeout)`, `TypeSafeError` / `TypeSafeAPIError`, `response_model=` (0.7.0+) | typed errors, built-in retries |
| Env | `TYPESAFE_API_KEY`, `TYPESAFE_BASE_URL` (point it at any `/v1/systemone`-compatible server), `TYPESAFE_DEFAULT_MODEL`, `TYPESAFE_LOG_LEVEL` | same |

**SDK changelog:**
- Python v0.5.7 (09-12).
- Python v0.6.0 (09-15).
- Python **v0.7.0** (09-18): a breaking change, because Pydantic replaced msgspec. It also added `response_model`.
- Python v0.7.1 (09-21): validates the key earlier and no longer puts the key in exception logs.
- JS v0.6.0 (09-15): a breaking change, because Score `criteria` became an ordered array.

Other official repos in the [typesafe-ai](https://github.com/typesafe-ai) org:
- [skills](https://github.com/typesafe-ai/skills), an agent *design* skill that does not call the model itself. Install it with `npx skills add typesafe-ai/skills --skill typesafe-ai`, or with `claude plugin marketplace add typesafe-ai/skills` followed by `claude plugin install typesafe@typesafe-ai`.
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python), a drop-in `TypeSafeClient` backed by OpenAI or Anthropic. Use it for A/B baselines and fallback. Its answers are not calibrated like Jev's.
- [WorkflowEvals](https://github.com/typesafe-ai/WorkflowEvals), the code behind evals.typesafe.ai.
- [daggerverse](https://github.com/typesafe-ai/daggerverse)
- Overwatch (observability), which is cited by several lists but returned 404 on 2026-09-30.
- [n8n-nodes-typesafe-ai](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai)

The org also has forks of vLLM and **LLaDA**, a masked-diffusion LM. Commentators read the LLaDA fork as the strongest public hint about the architecture, but it is only a hint.

⚠️ **Look-alikes:**
- The official org is **`typesafe-ai`**. `TypeSafeAI/*` (typesafe-router, typesafe-playground, jev-harness) is a community org.
- PyPI `typesafe-ai` is a community anti-slopsquatting shim. npm `typesafe-sdk` is an unrelated placeholder.
- `jevai.org`, `aijev.net`, `jev.ai` and `typesafe.co` are not official.
- There is **no official `$JEV` token**.

## Where you can call Jev (access routes)

The model is the same on every route, but the **wire formats and field names differ**, so porting between routes is not a URL swap. [kydlikebtc/awesome-jev](https://github.com/kydlikebtc/awesome-jev) keeps the fullest compatibility matrix.

| Route | Model ID | Endpoint / API | Key | Gotchas |
|---|---|---|---|---|
| **TypeSafe direct** | `jev-1.13.0`, `jev-latest` | `POST api.typesafe.ai/v1/systemone` | `TYPESAFE_API_KEY` ([console](https://console.typesafe.ai/settings/keys)) | The waitlist was removed 09-20; $5 starter credit; signups briefly paused around 09-22. |
| **Vercel AI Gateway** | `typesafe-ai/jev` | AI SDK 7 `experimental_evaluate` (`ai` ≥ 7.0.103) or `@ai-sdk/typesafe-ai`; native `POST ai-gateway.vercel.sh/v1/evaluate`; TypeSafe-compatible base `ai-gateway.vercel.sh/typesafe` | `AI_GATEWAY_API_KEY` | Noul is called **`boolean`** and returns `probability`. Confidence is at `providerMetadata.typesafe.confidence`. Versioned IDs return 404. A card on file is required (otherwise `403 customer_verification_required`). Use Gateway Budgets, because spend management does not cap it. |
| **Cloudflare Workers AI** | `typesafe/jev` | `env.AI.run('typesafe/jev', { input: { state, questions } })` | Cloudflare | 32k context listed. |
| **OpenRouter** | `typesafe/jev-1.13`, `~typesafe/jev-latest` | Decisions API `POST openrouter.ai/api/alpha/decisions` (alpha); `/api/v1/systemone` drop-in reported | `OPENROUTER_API_KEY` | `/chat/completions` returns 400. The OpenRouter TS SDK needs a separate Decisions client (404 gotcha). OpenRouter keys are rejected by api.typesafe.ai. OpenRouter also runs a [Jev Router](https://openrouter.ai/typesafe/jev-router). |
| **Netlify AI Gateway** | `jev-latest` | official JS SDK from Netlify Functions | none needed | Billed to Netlify credits. |
| **LiteLLM** | `jev-1.13.0` etc. | pass-through `…/typesafe/v1/systemone` | `TYPESAFE_API_KEY` | [docs](https://docs.litellm.ai/docs/pass_through/typesafe); no streaming. |
| Others | varies | Pydantic AI `typesafe:jev-latest`, LangSmith gateway `typesafe/jev-1.13.0`, TanStack AI `decide()`, AI/ML API `/v1/decisions`, Bifrost, Convex, OpenCode Zen (free `jev-1.13-free` promo), new-api | | Resellers such as BeatAPI and JevProxy are third parties, not TypeSafe. |

## Known weaknesses (the official "jaggedness" list)

TypeSafe publishes a per-version limitations page, [Model jaggedness: jev-1.13](https://docs.typesafe.ai/model-jaggedness/jev-1.13), last reviewed 2026-09-17. It lists nine areas:

1. **Literal reading.** Scoping, negation, double negatives and sarcasm are read literally.
2. **Math, counting and numeric formats.** Examples: "strawberry has exactly two r" → yes 0.79; exact counting is about 33%.
3. **Date and time comparison.**
4. **Indirection and multi-hop reasoning.**
5. **Large states full of irrelevant detail** ("context rot").
6. **Adversarial content.** State is not treated as hostile by default.
7. **Instructions that contradict criteria.**
8. **Structural invariants.**
   - P(Noul) ≠ P(Choice "yes") for the same question; the average gap is 0.125.
   - P(x) + P(not x) ≠ 1. One example is `refund 0.72` + `not a refund 0.47`; the observed range is 0.71–1.42.
9. **Generation.** Jev cannot produce values that are not in your option list.

The official fix is always the same: **split into atomic questions, and do computation in code.**

## The company and the launch

- **TypeSafe AI**, San Francisco, founded 2024, about two years in stealth.
- **Founders:** Diogo Almeida (CEO; ex-OpenAI and an InstructGPT co-author; lists variously call him a "co-inventor of RLHF/ChatGPT"), Erik Gafni and Sasha Sheng.
- **Funding:** a **$40M seed led by DCVC**, announced 2026-09-15 in a [Business Wire press release](https://www.businesswire.com/news/home/20260915525333/en/). Secondary sources give a ~$200M valuation. The Information (09-24) reported talks to raise $1B+ at a $10B+ valuation; this is unconfirmed.
- **Thesis:** "Machine-Native Intelligence", "Composable AI: Build Prod, Not God" ([Manifesto](https://typesafe.ai/manifesto)). Other essays: [The Bitterest Lesson](https://typesafe.ai/blog/bitterest-lesson), [AI: too good to be true, too bad to be useful](https://typesafe.ai/blog/ai-too-good-to-be-true-too-bad-to-be-useful-typesafe-ai), and [Lies, Damned Lies, and Benchmarks](https://typesafe.ai/blog/antibenchmaxxing), which is why TypeSafe publishes no benchmark tables.
- **Launch demos:** Jev plays **Doom** from structured game state, not pixels (~10 queries/s, ~$7/hour), and **Wikiracing**, which shows the 255-option Choice cap.
- **Reception:**
  - The HN launch thread ([item 49717558](https://news.ycombinator.com/item?id=49717558)) reached **~1,800–1,930 points** depending on the snapshot. Its original title, "Jev: New frontier model 40-400x cheaper and 20-200x faster", was softened within the hour.
  - The founder's X thread had ~63–75k likes.
  - Vercel said ~13% of paid AI Gateway teams tried Jev on day one.
  - There were **29 arXiv papers** in the first two weeks, and GitHub went from zero to **thousands of repos** within a week ([Jev in the Wild](https://arxiv.org/abs/2609.30216) counts 2,170 projects through 09-22).

## Timeline

| Date (2026) | Event |
|---|---|
| Jul 22 | Earliest #show-and-tell posts in the early-access Discord |
| Sep 10–11 | Blog posts "The Bitterest Lesson" and "Lies, Damned Lies, and Benchmarks" |
| **Sep 15** | Launch: blog post, $40M seed, early access with a waitlist, JS SDK 0.6.0, Python SDK 0.6.0 |
| Sep 16 | Vercel AI Gateway adds `typesafe-ai/jev` (no waitlist); The Register covers the launch |
| Sep 17 | Netlify AI Gateway support; the jaggedness page is reviewed |
| Sep 18 | Python SDK 0.7.0 (breaking); OpenRouter lists `typesafe/jev-1.13`; Langfuse integration; TechCrunch coverage |
| Sep 19–20 | Cloudflare Workers AI `typesafe/jev`; the first independent benchmarks land; LiteLLM v1.103.0-rc |
| **Sep 20, 21:30 UTC** | **Waitlist removed**, with a $5 starting credit (lists describe Sep 21 as "GA / public access") |
| Sep 21 | Python SDK 0.7.1; Simon Willison's analysis; Latent Space podcast; Spring AI integration |
| ~Sep 22 | Signups paused briefly because of demand; status incidents on Sep 20, 21 and 23 |
| Sep 19–27 | The arXiv wave: judges, robustness, agents and applications ([papers](papers.md)) |
| Sep 25 | Vercel free-usage window ends (other lists say by Sep 28); OpenRouter Jev Router surfaces |
| Sep 29 | Liquid AI d1 launches as a competing hosted decision model |

## Vendor claims vs. independent measurement

| Claim | Vendor figure | What independent testing found |
|---|---|---|
| Speed | "193.6× faster", "20–200× faster", "70–500 ms" | The 193.6× figure is the *best case*, measured against the slowest comparator. The **average across eight setups was 97.8×**. Against GPT-5.6 Terra it is about **25×** on the vendor evals and **3.6×** in [a retest](https://x.com/fluixoo/status/2103755424117686645). For a *single* short question, Jev is only **1.5–3× faster** than a small chat model. Large speedups appear only when one batched call replaces a chain of sequential LLM calls. |
| Cost | "444.6× cheaper", "40–400×" | The 444.6× figure compares against Opus 5; the eight-setup average is **149.2×**. [A 2,390-question benchmark](https://github.com/punk2898/awesome-jev-verified) found **88×** vs Sol, **45×** vs Terra, and **~5×** vs Luna / GPT-4.1-mini. |
| Accuracy | Vendor workflow evals: **67.8%** agreement (vs Terra 67.9%, Sol 74.1%, Opus 5 73.1%) | The reference labels are the *average of GPT-6 Astra and Claude Fable 5.1* predictions, not ground truth, and TypeSafe's own team built the workflows. Independent results range from on par with mid-tier LLMs to 3–12 points behind frontier LLMs. Jev is typically behind trained small classifiers when labels exist. |
| "Zero hallucination" / "0% type errors" | | This is true **only as a schema guarantee**: Jev can't return an out-of-set value. It is still confidently wrong. In one benchmark, 36 of 1,200 answers were wrong at ≥90% confidence (the fewest of five models tested). |
| "Calibrated" | RLCD | **Partly true.** Calibration is good on in-distribution short-text tasks (ECE 0.02–0.08). It degrades out of distribution, on non-English state, and on questions where humans disagree (ChaosNLI: confidence 0.807 vs 0.468 human agreement). Choice and Score are **overconfident**, while Noul is slightly **underconfident**. Calibration *does not transfer* across datasets. See [evidence.md](evidence.md#calibration). |
| "Deterministic" | | Close, but not bit-exact. Repeated calls vary with a std of 0.001–0.015; one test saw 15 distinct answer sets in 50 identical requests; Noul confidence can drift by up to 14 points over 1,000 calls. |

## Contradictions across sources, resolved

| Topic | What the lists say | Resolution |
|---|---|---|
| Rate limits | "250k tokens/s, 1,200 requests/min" (nearly every list) | These come from launch-week snapshots. The live Models page on 2026-09-30 says **100K tokens/s and 40 requests/s**, and warns that the limits change dynamically. |
| Context window | "32k" vs "64k" | 64k per request, 32k for state + the longest question. Gateways show 32k. |
| Latency | "12–50 ms" / "30–50 ms" (Gerry9000, bakiabaci, logicrw) vs "~100 ms" (docs) vs 70–500 ms | The 12–50 ms figures are unsourced and probably confuse open-model forward-pass times (Laya ~33 ms) with Jev. For planning, use **250–500 ms end to end**. |
| Launch / GA date | Sep 15 vs Sep 21 | Early access opened Sep 15; the waitlist was removed Sep 20 at 21:30 UTC (GA Sep 21). |
| Noul "confidence" | Some lists show `noul.confidence` | **Noul has no confidence field.** The examples that show one (such as bakiabaci's `client.decide.noul(...).confidence`) are invented. |
| Third primitive's name | "Noul", "Boolean", "Bool", and even "skip — not worth it" | It is **Noul**. "boolean" is the name only on Vercel, the AI SDK and TanStack. The "skip" definition (in larkwins and supermanc417-alt) is wrong. |
| Python package | `typesafe-sdk` vs `typesafe` | `typesafe-sdk`. `pip install typesafe` and the Go `typesafe-go` from typesafe-ai are hallucinated. |
| Endpoint | `/v1/systemone` vs `/v1/eval` | `/v1/systemone`. `/v1/eval` (Gerry9000 dossier) is wrong. `/api/alpha/decisions` is OpenRouter's route, and `/v1/evaluate` is Vercel's. |
| Vercel model ID | `typesafe-ai/jev` vs `typesafe-ai/jev-latest` | `typesafe-ai/jev` (versioned IDs 404). |
| OpenRouter slug | `typesafe/jev-1.13` vs `typesafe-ai/jev` | `typesafe/jev-1.13` or `~typesafe/jev-latest`. |
| >255 Choice options | "hard cap" vs "falls back to a slower two-stage path" | Treat 255 as the cap. The launch post's Wikiracing demo uses a two-stage score-then-choice, but that is application logic, not automatic API behaviour. |
| Every's vibe check | "1,709 judgments" vs "777 judgments" | 37 documents × 21 questions = **777**. The 1,709 figure doesn't match that arithmetic, so prefer 777. |
| Kev base model | Qwen2.5-0.5B vs Qwen3.5/3.8 0.8B–27B | Both are right at different times; Kev's early checkpoints were on Qwen2.5, and later ones use Qwen3.5/3.8. |
| $40M funding | "not in launch post" | It is in the Business Wire press release. |
| Star counts | e.g. jev-ultrafast 3,969 vs 21,430 on the same day | Lists copy stale snapshots. The verified counts on 2026-09-30 are in [the catalog](../catalog/README.md). |

## Common misinformation

- "The model ID is `jev-1`." It isn't; the ID is `jev-1.13.0` or an alias.
- "Jev is small / lightweight." TypeSafe says Jev is "neither small nor an LLM".
- "Jev can see screenshots." It can't. Computer-use tools OCR the screen or read the accessibility tree first.
- "Open replicas are Jev." Laya, Kev, SemIf, NanoJev and the others are independent. **Wire compatibility is not behavioural equivalence.**
- "OpenRouter/Vercel is an alternative model." It is the same paid model with an extra network hop.
- Viral sped-up or fake demos exist. Treat "rebuilt Tesla FSD in an hour" and "lost $31,680 trading" as jokes or unverified.
