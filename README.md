# Meta Awesome Jev-like Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> **A guide to the community of Jev-like models.** These are "System One" decision models: you send them a state and some typed questions, and they return calibrated choices, scores and yes/no probabilities instead of generated text.
>
> Jev introduced the `/v1/systemone` interface in September 2026. Within weeks it was served by a growing family of hosted and open models, including [Mercury Decide](https://openrouter.ai/inception/mercury-decide:free), [Liquid d1](https://docs.liquid.ai/lfm/models/decision-models), [Solar Decide](https://console.upstage.ai/api/systemone), [Laya](https://github.com/NandhaKishorM/laya), [Kev](https://github.com/jaredpalmer/kev), [Decider](https://github.com/Mapika/decider) and more.
>
> This list merges, de-duplicates, cross-checks and summarizes **106 community "awesome-jev" repositories**.

**18,330** unique links from 106 lists · **5,410** cited by 3 or more lists · **2,533** GitHub repos verified live · sources last pulled **2026-09-30** ([sources.md](sources.md))

`★` = GitHub stars when verified on the pull date · `📚N` = the number of the 106 source lists that cite the entry. `📚` is the cross-list consensus signal: an entry that many independently curated lists include has been vetted many times.

---

## Contents

- [Jev-like models in 60 seconds](#jev-like-models-in-60-seconds)
- [Quick Start: Jev-like inference for free](#quick-start-jev-like-inference-for-free)
- [What 106 lists taught us: key insights](#what-106-lists-taught-us-key-insights)
- [Reference docs and SDKs](#reference-docs-and-sdks)
- [Ecosystem](#ecosystem)
  - [Jev-like models: hosted, open and local](#jev-like-models-hosted-open-and-local) · [Framework and platform integrations](#framework-and-platform-integrations) · [Community SDKs](#community-sdks-and-clients) · [MCP servers](#mcp-servers) · [Agent skills and plugins](#agent-skills-and-plugins)
  - [Coding-agent tooling](#coding-agent-tooling) · [Browser, desktop and mobile](#browser-desktop-and-mobile) · [Search, RAG and data](#search-rag-and-data)
  - [Evaluation, calibration and QA tooling](#evaluation-calibration-and-qa-tooling) · [Games, robotics and simulation](#games-robotics-and-simulation) · [Apps and domain applications](#apps-and-domain-applications)
- [Benchmarks and independent studies](#benchmarks-and-independent-studies)
- [Research papers](#research-papers)
- [Articles, analysis and critique](#articles-analysis-and-critique)
- [Learning resources](#learning-resources)
- [Directories and other lists](#directories-and-other-lists)
- [About this meta-list](#about-this-meta-list)

**Deep dives in this repo:**

| | |
|---|---|
| [docs/open-models.md](docs/open-models.md) | **The Jev-like model family:** open replications, local runtimes and hosted alternatives, with caveats |
| [docs/patterns.md](docs/patterns.md) | Question design, composition patterns, thresholds, economics, security, a production checklist and anti-patterns |
| [docs/evidence.md](docs/evidence.md) | Every independent benchmark, calibration audit, robustness probe and negative result, with numbers |
| [docs/what-is-jev.md](docs/what-is-jev.md) | A reference for Jev, the original model: specs, API, timeline, and contradictions between sources, resolved |
| [docs/papers.md](docs/papers.md) | ~35 papers on Jev and Jev-like models, plus the research lineage |
| [docs/source-lists.md](docs/source-lists.md) | A review of all 106 source lists: which to read for what, and which to treat with caution |
| [catalog/](catalog/README.md) | The **complete** union of every link from every list, in 21 categories, ranked by consensus |

---

## Jev-like models in 60 seconds

A Jev-like model is **not a chat model**, and it never writes text. You send it two things in one request:
- a **state**: the evidence (a string, a JSON object, or an array of text);
- a map of **typed questions** about that state.

It answers every question **in parallel, in a single call**. Each answer is a **probability distribution** that your code can threshold.

Every model in the family speaks the same `/v1/systemone` wire format. Here is a support ticket with one question of each type:

```json
POST /v1/systemone
{
  "model": "<model id>",
  "state": {
    "ticket": "I was charged twice for my order last week and nobody has answered my emails. I want my money back today."
  },
  "questions": {
    "team": {
      "type": "choice",
      "instructions": "Which team should handle this ticket?",
      "criteria": {
        "billing":   "Charges, refunds, invoices",
        "technical": "Bugs, outages, errors",
        "other":     "Anything else"
      }
    },
    "frustration": {
      "type": "score",
      "instructions": "How frustrated is the customer?",
      "criteria": ["Calm", "Annoyed but civil", "Angry or threatening to leave"]
    },
    "wants_refund": {
      "type": "noul",
      "instructions": "Is the customer asking for a refund?"
    }
  }
}
```

The response contains one typed answer per question:

```json
{
  "model": "<resolved model version>",
  "answers": {
    "team":         { "type": "choice", "choice": "billing",
                      "probabilities": { "billing": 0.95, "technical": 0.02, "other": 0.03 },
                      "confidence": 0.93 },
    "frustration":  { "type": "score", "score": 1.62,
                      "legend": { "0": "Calm", "1": "Annoyed but civil", "2": "Angry or threatening to leave" },
                      "probabilities": { "0": 0.03, "1": 0.32, "2": 0.65 }, "confidence": 0.71 },
    "wants_refund": { "type": "noul", "noul": 0.97 }
  },
  "usage": { "input_tokens": 214, "output_tokens": 5 }
}
```

Your code then decides what to do with the answers:

```python
a = response["answers"]
if a["team"]["confidence"] >= 0.8:          # "the answer is what; confidence is whether to act"
    route_to(a["team"]["choice"])
else:
    send_to_human_triage()
if a["wants_refund"]["noul"] > 0.9 and a["frustration"]["score"] >= 1.5:
    escalate_priority()
```

| Question type | Asks | You supply | You get back |
|---|---|---|---|
| **Choice** | "Which one?" | an `instructions` string and `criteria` as a map of option → description (up to 255 options; **always include an `other`**) | `choice`, `probabilities` per option, `confidence` |
| **Score** | "Where on this ordered scale?" | an `instructions` string and `criteria` as an ordered list of 2–10 levels | `score` (probability-weighted and 0-indexed, so it can fall *between* levels), `legend`, `probabilities`, `confidence` |
| **Noul** | "Is this true?" | an `instructions` string | `noul`: the probability, from 0 to 1, that the answer is yes. There is no `confidence` field, and 0.5 means "can't tell", not "medium". |

**Mental model:** the model decides, an LLM writes, and code acts. Code owns thresholds, arithmetic, dates and side effects.

**Where this works:** questions are independent of each other, so batch them all into one call. Output is a typed value, so it can't fall outside your option set. Cost scales with input tokens only.

→ The [reference for the original model](docs/what-is-jev.md) and the [question-design guide](docs/patterns.md#question-design) go deeper.

## Quick Start: Jev-like inference for free

**This is how to use a Jev-like model for free.** [Mercury Decide](https://openrouter.ai/inception/mercury-decide:free) is Inception's structured decision model, served on OpenRouter as **`inception/mercury-decide:free`**. Details from its OpenRouter page:
- **$0 input and $0 output.** Free endpoints are [rate-limited](https://openrouter.ai/docs/api/reference/limits).
- **32,768-token context.**
- About **0.42 s p50 latency** and up to ~14 decisions per second.
- The same `/v1/systemone` question schema shown above.

**1. Get a free OpenRouter API key** at [openrouter.ai/settings/keys](https://openrouter.ai/settings/keys).

**2. Call the Decisions API.** Mercury Decide is a *decisions* model, so it uses OpenRouter's Decisions API, **not** `/chat/completions`. OpenAI-style chat SDKs won't work with it.

```bash
export OPENROUTER_API_KEY=sk-or-...

curl https://openrouter.ai/api/alpha/decisions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "inception/mercury-decide:free",
    "state": "I was charged twice for my order and want my money back.",
    "questions": {
      "team":   { "type": "choice", "instructions": "Which team should handle this ticket?",
                  "criteria": { "billing": "Charges and refunds", "technical": "Bugs and outages", "other": "Anything else" } },
      "refund": { "type": "noul",   "instructions": "Is the customer asking for a refund?" }
    }
  }'
```

**3. Or call it from Python** (`pip install requests`; no other SDK is needed):

```python
import os, requests

resp = requests.post(
    "https://openrouter.ai/api/alpha/decisions",
    headers={"Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}"},
    json={
        "model": "inception/mercury-decide:free",
        "state": {"ticket": "I was charged twice for my order and want my money back."},
        "questions": {
            "team": {"type": "choice", "instructions": "Which team should handle this ticket?",
                     "criteria": {"billing": "Charges and refunds", "technical": "Bugs and outages",
                                  "other": "Anything else"}},
            "refund": {"type": "noul", "instructions": "Is the customer asking for a refund?"},
            "urgency": {"type": "score", "instructions": "How urgent is this ticket?",
                        "criteria": ["Can wait a week", "Handle within a day", "Handle within the hour"]},
        },
    },
    timeout=30,
)
resp.raise_for_status()
answers = resp.json()["answers"]
print(answers["team"]["choice"], answers["team"]["confidence"], answers["refund"]["noul"])
print(answers["urgency"]["score"], answers["urgency"]["probabilities"])  # e.g. 1.05 {'0': 0.04, '1': 0.87, '2': 0.09}
```

**Tips:**
- **Already have code for another `/v1/systemone` client?** OpenRouter also accepts the same request body at `https://openrouter.ai/api/v1/systemone`, so you can point an existing client's base URL at `https://openrouter.ai/api`.
- **Batch questions.** Put every independent question about a state into one request. It costs the same as a single question, so use the batching to stay inside the free rate limit.
- **Graduate when you need more.** Move to a paid decision model, or self-host an open one ([Laya](https://github.com/NandhaKishorM/laya), [Kev](https://github.com/jaredpalmer/kev) or [Ollaya](https://github.com/ollaya-dev/ollaya)), when you need higher limits or local data. Most of these keep the same schema; see [the model family](#jev-like-models-hosted-open-and-local).
- **Evaluate on your own labelled examples before trusting thresholds.** Calibration doesn't transfer between models, so a 0.8 cut-off tuned on one model means nothing on another.

## What 106 lists taught us: key insights

The same lessons show up again and again across the lists. Most measurements were taken on Jev, the first and most-tested model, and are labelled as such. The lessons about *how to build* apply to the whole family. Numbers link to the underlying studies in [docs/evidence.md](docs/evidence.md).

1. **Jev-like models are a decision layer, not a model swap.** The winning architecture is always the same: *code builds the candidates, the decision model picks or scores, code acts*. An LLM is called only for text or open reasoning. Examples:
   - Browser agents let the model choose the element and use an LLM only to type.
   - Games give the model the legal moves.
   - Extraction lets regex find spans and the model *select* one.
2. **The 100× speedups are real only against chains of LLM calls.** Jev's launch figures ("193.6× faster / 444.6× cheaper") are a best case against the slowest comparator; the average across eight setups is 97.8× / 149.2×. A single question is only ~1.5–3× faster than a small chat model. The order-of-magnitude wins come from **batching many questions per call**, where latency is flat up to ~25 questions and batching 13 questions was 12.2× cheaper, and from **deleting LLM calls that never needed an LLM**.
3. **Question design is the whole game.**
   - Splitting one question into atomic Nouls took a task from **48% → 98%**, and phishing detection from **62.6% → 95.0%**.
   - Rewriting the criteria moved accuracy from 70% → 96%.
   - Renaming options from `0/1` to `no/yes` cut AUC from .81 to .58.
   - **Always include an "other/unknown" option.** Removing it took one benchmark from 0.95 to 0.00.
4. **Keep computation in code.** Counting (33–65%), arithmetic, dates, multi-hop reasoning and open-ended generation are documented weak spots. Jev's own [jaggedness page](https://docs.typesafe.ai/model-jaggedness/jev-1.13) lists them, and independent tests on open replicas agree. Use one Noul per item and sum in code.
5. **Confidence is a routing signal, not a guarantee.**
   - The top-confidence band is very reliable (48/48 correct at ≥ 0.9 in one audit).
   - "Confidently wrong" still happens, and Choice and Score skew **overconfident**.
   - Calibration **does not transfer** across datasets, languages, phrasings, model versions *or models*.
   - Fit per-question thresholds on your own labels, and pin a model version.
6. **Cascades are the most consistent cost/accuracy win**, with one catch. Accepting confident decisions and escalating the rest to an LLM matched frontier accuracy at ~¼ the cost in several studies. But LLMs repeated ~96% of Jev's *confident* errors, so cascades mostly save money rather than add accuracy. **Price the fallback:** one production replay was 96% cheaper per call but 4% more expensive overall.
7. **It is not a security boundary.** Typed output blocks *format* attacks, not *decision* manipulation. Blunt injected commands mostly fail. **Evidence-shaped** text flips decisions: fake approvals, editor's notes and fluent context flipped 61% of correct answers in JevOut, and 65–73% on open clones. Put deterministic rules first, keep humans on irreversible actions, and track taint.
8. **Audit what tools send.** Hands-on audits found community tools leaking secrets, sending `.pem` files and screenshots, exposing keys, and **failing open** on API errors. Check data egress and fail-closed behaviour before installing.
9. **Coding agents are the dominant use case.** The largest clusters across all lists are context compaction, model/effort routing, tool-call gates, "done" verification, and skill/rule pruning. Compaction is the most *contested* of these: several careful evaluations (Hermes Agent, jev-use) did not adopt it.
10. **Classical baselines are still strong.** Trained small classifiers (bge-small + LR at 93% on Banking77, TF-IDF on spam) and regex often match or beat decision models. The model family's durable edges are **zero training, cost, latency, and robustness under distribution drift**: on drifted spam, Jev held at 97.3% while TF-IDF fell to 72.5%.
11. **The family grew fast, but "compatible" ≠ "equivalent".** Within days, dozens of open models and `/v1/systemone` servers appeared (Laya, Kev, SemIf, NanoJev, Decider, Ollaya), followed by hosted alternatives (Mercury Decide, Liquid d1, Solar Decide). The shared schema makes them drop-ins for your *code*, not for each other's accuracy or calibration. Most "beats Jev" claims are in-distribution, so measure on your own data.
12. **Most of the evidence is young.** Nearly all numbers are author-reported, small-n, and from the family's first weeks, and the ~29 arXiv papers are unreplicated preprints. The best lists label every number (vendor / author-reported / independent), and this one does too.

## Reference docs and SDKs

Jev's documentation is the most complete public description of the `/v1/systemone` interface: its question types, confidence semantics, composition patterns and cookbooks. Because Jev-like models share the schema, most of it applies across the family.

**Interface docs**
- [API reference](https://docs.typesafe.ai/api) `📚31` — `POST /v1/systemone`, with request and answer shapes for all three primitives. The full [docs index (llms.txt)](https://docs.typesafe.ai/llms.txt) `📚22` is also available.
- Concept pages:
  - [Primitives](https://docs.typesafe.ai/primitives) `📚27`
  - [Confidence](https://docs.typesafe.ai/confidence) `📚30`
  - [State](https://docs.typesafe.ai/concepts/state) `📚10`
  - [System One](https://docs.typesafe.ai/concepts/system-one) `📚13`
  - [How to build with System One](https://docs.typesafe.ai/concepts/how-to-build-with-system-one) `📚17`
  - [Use-case map](https://docs.typesafe.ai/concepts/use-case-map) `📚17`
- [Model jaggedness: jev-1.13](https://docs.typesafe.ai/model-jaggedness/jev-1.13) `📚35` — **Read this before building.** Nine documented failure modes (literal reading, math, dates, indirection, distracting state, adversarial content and more). They are written for Jev but are a good test plan for any Jev-like model.
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) `📚57` — The launch post that defined the category: RLCD (calibrated-decision training), the parallel sampler, and the Doom and Wikiracing demos.
- [Workflow evals](https://evals.typesafe.ai) `📚32` — Vendor evaluations on four workflows. The reference labels are averaged from two frontier models, not ground truth. The code is in [WorkflowEvals](https://github.com/typesafe-ai/WorkflowEvals) `📚3`.

**Reference SDKs and tools**
- Python: [typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) `★257 · 📚59`. JS/TS: [typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) `★260 · 📚57`. Both are `/v1/systemone` clients. Set the base-URL environment variable to point either one at any compatible server (local Kev, Decider or Ollaya; OpenRouter; and others).
- [system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) `★368 · 📚61` — The same client interface answered by an ordinary LLM. Use it for A/B baselines and fallback.
- [skills](https://github.com/typesafe-ai/skills) `★2,491 · 📚68` — An agent skill that teaches coding agents how to pick a question type and design questions.
- For model-agnostic clients across many languages, see [Community SDKs](#community-sdks-and-clients).

**Patterns and cookbooks** (the [full annotated index](docs/patterns.md#official-composition-patterns) covers all ~18)
- [Patterns](https://docs.typesafe.ai/patterns) `📚19`:
  - [Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out) `📚16`
  - [Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) `📚15`
  - [Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring) `📚14`
  - [Intent routing](https://docs.typesafe.ai/patterns/intent-routing) `📚14`
- [Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions) `📚23` — 13 questions in one call: 12.2× cheaper and 10× faster.
- [Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification) `📚15` — Beam search past the 255-option cap.
- [Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe) `📚15` — Legal search: top-1 5% → 18%.
- [Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails) `📚16`
- [Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) `📚17`
- [Citation check](https://docs.typesafe.ai/cookbooks/citation_check) `📚18`
- [Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook) `📚14`
- [Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook) `📚16`
- [SDE cascade](https://docs.typesafe.ai/cookbooks/sde_cascade) `📚13`
- [Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion) `📚17`
- [Function calling](https://docs.typesafe.ai/cookbooks/function_calling) `📚17`
- The OpenRouter cookbooks [gate tool calls](https://openrouter.ai/docs/cookbook/building-agents/gate-tool-calls-with-jev) and [verified cascade](https://openrouter.ai/docs/cookbook/evaluate-and-optimize/jev-verified-cascade) carry the same recipes over to models served by OpenRouter.

---

## Ecosystem

Hand-picked from the consensus of the source lists: mostly entries cited by many lists, plus a few high-signal ones that fewer lists noticed. Each section links to its full [catalog](catalog/README.md) page.

### Jev-like models: hosted, open and local

The model family itself. Many members serve `/v1/systemone`, so the same client code works across them. [docs/open-models.md](docs/open-models.md) maps the landscape and its caveats.

**Hosted**
- [Mercury Decide](https://openrouter.ai/inception/mercury-decide:free) (Inception) — A structured decision model on OpenRouter, **free**, with a 32K context and the `/v1/systemone` schema. See the [Quick Start](#quick-start-jev-like-inference-for-free).
- [Jev](docs/what-is-jev.md) (TypeSafe) — The original and most-tested model, with a [reference](docs/what-is-jev.md).
- [Liquid AI d1](https://docs.liquid.ai/lfm/models/decision-models) — Serves `/decisions/v1/systemone` and has a free tier. Reportedly #1 on the Jev Decision Index.
- [Upstage Solar Decide](https://console.upstage.ai/api/systemone) — Same schema, 512K context.
- [Respan Span-01](https://openrouter.ai/respan/span-01) — A behaviour-monitoring decision model.
- The OpenAI Decisions API (Luna, preview).

**Open and local**

- [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) `★29,237 · 📚38` — Convai's Apache-2.0 non-autoregressive encoder (421M/322M, 100+ languages, ~33 ms). Runtimes: [laya-mlx](https://github.com/mizorewww/laya-mlx) `★6,654 · 📚23` (7–14 ms on M3 Max) and [receptron/laya](https://github.com/receptron/laya) `★661 · 📚20` (Node/ONNX).
- [jaredpalmer/kev](https://github.com/jaredpalmer/kev) `★8,057 · 📚57` — A trainable Jev-like family on Qwen3.5/3.8 with a pointer head and a `/v1/systemone` server.
- [TheoLeeCJ/SemIf-OpenJev](https://github.com/TheoLeeCJ/SemIf-OpenJev) `★4,615 · 📚63` — "Semantic ifs" from open models on a 3090, using shared-prefix logit readout.
- [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) `★2,453 · 📚60` · [vinnylarouge/jevlike](https://github.com/vinnylarouge/jevlike) `★1,335 · 📚57` · [Mapika/decider](https://github.com/Mapika/decider) `★993 · 📚45` · [bespokelabsai/nimble](https://github.com/bespokelabsai/nimble) `★1,981 · 📚21` · [wfzyx/von](https://github.com/wfzyx/von) `★794 · 📚48` — Trained replicas and recipes (0.4B–35B), several with published limits.
- [nokia-applied-research/AnyJev](https://github.com/nokia-applied-research/AnyJev) `★986 · 📚32` · [featherless-ai/simple-jev](https://github.com/featherless-ai/simple-jev) `★575 · 📚40` · [razorback16/openjev](https://github.com/razorback16/openjev) `★548 · 📚49` · [ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang) `★335 · 📚48` · [githubnext/localjev](https://github.com/githubnext/localjev) `★803 · 📚16` — Turn any open LLM into a decision endpoint, with no training. AnyJev adds option-order correction.
- [ollaya-dev/ollaya](https://github.com/ollaya-dev/ollaya) `★1,032 · 📚24` — "Ollama for decision models". It serves Laya, Decider, NLI and GLiClass behind a `/v1/systemone`-compatible API.
- Trackers: [HF Jev Reproductions Tracker](https://huggingface.co/spaces/multimodalart/jev-reproductions-tracker) · [Jev Decision Index](https://huggingface.co/spaces/multimodalart/jev-decision-index)
- → [catalog/open-models.md](catalog/open-models.md)

### Framework and platform integrations

Decision models landed inside mainstream frameworks within days of Jev's launch, usually as a new `evaluate` / `decide` / `classify` model type alongside `generate`. Most of these integrations target the shared `/v1/systemone` shape.

- [vercel/ai](https://github.com/vercel/ai) `★27,056 · 📚7` — The AI SDK's decision-model provider maps Choice, Score and Boolean onto `experimental_evaluate`.
- [vercel/eve](https://github.com/vercel/eve) `★5,426 · 📚28` — Vercel's agent framework. A decision model (Jev by default) powers its `evaluate` path and its tool-approval policies.
- [vercel-labs/fx](https://github.com/vercel-labs/fx) `★3,234 · 📚9` · [vercel-labs/ai-cli](https://github.com/vercel-labs/ai-cli) `★817 · 📚23` — fx has a decision-model permission reviewer, reported at p95 18× faster than GPT Luna. ai-cli adds an `evaluate` command.
- [langchain-ai/langchain](https://github.com/langchain-ai/langchain/tree/master/libs/partners/typesafe) — A decision-model partner package: a classifier plus routing and auto-mode middleware. See also [Building a harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev).
- [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) `★20,296 · 📚11` — A decision-model backend: `output_type` fields become typed questions (bool → Noul, Literal → Choice, IntEnum → Score).
- [BerriAI/litellm](https://github.com/BerriAI/litellm) `★59,945 · 📚9` — A decision-model complexity router, a compaction guardrail, and a pass-through proxy.
- [ComposioHQ/composio](https://github.com/ComposioHQ/composio) `★30,374 · 📚14` — A decision-model provider for tool and argument selection.
- [BoundaryML/baml](https://github.com/BoundaryML/baml) `★9,363 · 📚5` · [BoundaryML/feelings](https://github.com/BoundaryML/feelings) `★22 · 📚10` — Maps the type system onto the primitives. `feelings` is a typed `.feels()` "AI if-statement".
- [Arize-ai/openinference](https://github.com/Arize-ai/openinference) `★1,240 · 📚7` — Records decision-model calls (Choice/Score/Noul) as OpenTelemetry spans. See also the [Langfuse](https://langfuse.com/blog/2026-09-18-using-typesafes-jev-for-evals) integration.
- [trycua/cua](https://github.com/trycua/cua) `★27,561 · 📚17` — A computer-use platform with a bounded-action recipe for decision models.
- [agentgateway/agentgateway](https://github.com/agentgateway/agentgateway) `★5,109 · 📚12` — A decision-model guardrail for jailbreaks, harmful content and secret leakage at the gateway.
- [milvus-io/bootcamp](https://github.com/milvus-io/bootcamp/tree/master/bootcamp/RAG/search_with_jev) `★2,445 · 📚16` — Nine search notebooks that use a decision model for ranking, filtering, routing and stopping.
- [zilliztech/GPTCache](https://github.com/zilliztech/GPTCache) `★8,206 · 📚7` — Uses a Noul to check whether a cached answer serves a new request.
- [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/experimental/transforms/jev_search.py) — A two-stage MCP tool-search transform: a wide Choice, then a Noul per shortlisted tool.
- [spring-ai-community/spring-ai-typesafe](https://github.com/spring-ai-community/spring-ai-typesafe) `★41 · 📚20` · [crmne/ruby_llm](https://github.com/crmne/ruby_llm) `★4,423 · 📚5` · [laravel/ai](https://github.com/laravel/ai) `★1,203 · 📚6` — Java/Spring, Ruby and Laravel support.
- [juspay/neurolink](https://github.com/juspay/neurolink) `★143 · 📚23` — Makes `decide` a first-class inference type next to generate and stream, across 40 providers.
- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) `★250,326 · 📚5` — A decision-model provider, skill routing, and a published (negative) [compaction scorecard](https://github.com/NousResearch/hermes-agent/blob/main/evals/compaction/results/SCORECARD-2026-09-19-jev.md).
- [dubinc/dub](https://github.com/dubinc/dub) `📚3` — A production link-safety gate on `typesafe-ai/jev`.
- More: [TanStack AI](https://tanstack.com/ai/latest/docs/adapters/typesafe) (`decide()`), [DeepEval](https://deepeval.com/integrations/models/typesafe-ai), [MotherDuck `prompt_jev()`](https://motherduck.com/blog/motherduck-supports-jev/), [OpenRouter cookbook: gate tool calls](https://openrouter.ai/docs/cookbook/building-agents/gate-tool-calls-with-jev), [Ollama 0.35 decision models](https://ollama.com/blog/ollama-now-supports-jev-style-decision-models) · → [catalog/sdk.md](catalog/sdk.md)

### Community SDKs and clients

Every major language had a community SDK within a week. Check the last commit date before you depend on one.

- **Go:**
  - [Stumble/jev-go](https://github.com/Stumble/jev-go) `★6 · 📚30` — supports several gateways.
  - [Gaurav-Gosain/jev-go](https://github.com/Gaurav-Gosain/jev-go) `★5 · 📚29`
  - [mattn/go-jev](https://github.com/mattn/go-jev) `★39 · 📚18` — SDK and CLI.
  - [Tangerg/typesafe-sdk-go](https://github.com/Tangerg/typesafe-sdk-go) `★9 · 📚24`
- **Rust:**
  - [Twister915/typesafe-ai](https://github.com/Twister915/typesafe-ai) `★13 · 📚33` — async and blocking clients, observable retries.
  - [gilljon/typesafe-ai-rs](https://github.com/gilljon/typesafe-ai-rs) `★6 · 📚31`
  - [AbdelStark/s1-rs](https://github.com/AbdelStark/s1-rs) `★1 · 📚23`
  - [luizribeiro/jevrs](https://github.com/luizribeiro/jevrs) `★0 · 📚6`
- **Ruby:**
  - [obie/ruby_decision_model](https://github.com/obie/ruby_decision_model) `★51 · 📚32`
  - [joshmn/typesafe-sdk](https://github.com/joshmn/typesafe-sdk) `★7 · 📚35`
  - [kieranklaassen/ruby_llm-typesafe](https://github.com/kieranklaassen/ruby_llm-typesafe) `★18 · 📚30`
  - [carldaws/hunch](https://github.com/carldaws/hunch) `★16 · 📚24` — probabilistic control flow for Rails.
- **Elixir:**
  - [dannote/jev](https://github.com/dannote/jev) `★34 · 📚43` — pattern-match decisions inside OTP.
  - [nshkrdotcom/typesafe_sdk](https://github.com/nshkrdotcom/typesafe_sdk) `★5 · 📚36`
- **.NET:** [saibimajdi/typesafeai-dotnet-sdk](https://github.com/saibimajdi/typesafeai-dotnet-sdk) `★12 · 📚34` · [Hawxy/TypeSafeAI.Net](https://github.com/Hawxy/TypeSafeAI.Net) `★4 · 📚24`
- **Java:** [Premo-Cloud/typesafe-sdk-java](https://github.com/Premo-Cloud/typesafe-sdk-java) `★10 · 📚23`
- **Scala:** [jamesward/zio-typesafe-ai](https://github.com/jamesward/zio-typesafe-ai) `★5 · 📚29`
- **Swift:**
  - [alterhq/typesafe-sdk-swift](https://github.com/alterhq/typesafe-sdk-swift) `★4 · 📚25`
  - [ainame/swift-typesafe](https://github.com/ainame/swift-typesafe) `★16 · 📚22`
  - [peterfriese/system-one-foundation-models](https://github.com/peterfriese/system-one-foundation-models) `★54 · 📚20` — maps Apple Foundation Models `@Generable` types onto the primitives.
- **Haskell:** [inanna-malick/jev-dsl](https://github.com/inanna-malick/jev-dsl) `★7 · 📚20`
- **Python helpers:**
  - [pithings/advocaat](https://github.com/pithings/advocaat) `★96 · 📚48`
  - [AboveColin/jevclient](https://github.com/AboveColin/jevclient) `★2 · 📚30`
  - [jlowin/vibecheck](https://github.com/jlowin/vibecheck) `★39 · 📚8`
  - [ktaletsk/jevframe](https://github.com/ktaletsk/jevframe) `★20 · 📚18` — pandas and Polars.
  - [docxology/daf-jev](https://github.com/docxology/daf-jev) `★6 · 📚27`
- **TypeScript helpers:**
  - [jomatsu/zod-jev](https://github.com/jomatsu/zod-jev) `★8 · 📚23` — semantic rules inside Zod schemas.
  - [mateonunez/jod](https://github.com/mateonunez/jod) `★3 · 📚22`
- **CLIs:**
  - [shiftynick/jev-axi](https://github.com/shiftynick/jev-axi) `★25 · 📚39`
  - [tumf/jev-cli](https://github.com/tumf/jev-cli) `★13 · 📚32` — a CLI and stdio MCP server.
  - [sharziki/semdecide](https://github.com/sharziki/semdecide) `★75 · 📚37` — Unix-pipeline and CI decisions with exit codes.
  - [cristianoliveira/jeq](https://github.com/cristianoliveira/jeq) `★10 · 📚11` — jq meets decision models.
- → [catalog/sdk.md](catalog/sdk.md)

### MCP servers

- [jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) `★469 · 📚66` — The most-cited MCP server. Its typed tools (verify, screen for injection, find, rerank, classify, decide) follow a fail-closed contract. Install with `claude mcp add jev -- npx -y @jkudish/jev-mcp`.
- [itsmostafa/system-one-connector](https://github.com/itsmostafa/system-one-connector) `★337 · 📚61` — Formerly `typesafe-mcp`. A single connector for Jev, d1, CLM and Laya.
- [blakestone-x/jev-mcp](https://github.com/blakestone-x/jev-mcp) `★25 · 📚42` · [burnigtm/jev-mcp](https://github.com/burnigtm/jev-mcp) `★61 · 📚29` · [BYK/jev-mcp](https://github.com/BYK/jev-mcp) `★3 · 📚20` · [PyModel/jev-judge-mcp](https://github.com/PyModel/jev-judge-mcp) `★69 · 📚17` · [Brainwires/jevwire](https://github.com/Brainwires/jevwire) `★21 · 📚28` — Alternatives. BYK's server is eval-first, and jevwire adds an escalate-only Claude Code plugin.
- [kbhuw/jev-sift](https://github.com/kbhuw/jev-sift) `★47 · 📚18` — Classify first, read selectively. Batch text classification for agents.
- [jiawei686/jev-ultrafast-mcp](https://github.com/jiawei686/jev-ultrafast-mcp) `★18 · 📚17` — Hands off a whole browser task in one MCP call.
- [agent-chaperone/agent-chaperone](https://github.com/agent-chaperone/agent-chaperone) `★21 · 📚21` — An MCP proxy that screens both tool calls *and* tool results.
- Note: several `jev-mcp` repos share a name, so check the owner. → [catalog/mcp.md](catalog/mcp.md)

### Agent skills and plugins

- [dbreunig/building-with-jev-skill](https://github.com/dbreunig/building-with-jev-skill) `★145 · 📚39` — The best community skill for *writing* decision-model programs: pick the primitive your code branches on, split two-property questions, and batch everything that shares a state.
- [kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) `★932 · 📚42` — The most complete decision-model-in-the-agent-loop pack: routing, memory, compaction, skill selection, and computer and browser use (Hermes, Claude Code, Codex).
- [wuyoscar/jev-skill](https://github.com/wuyoscar/jev-skill) `★554 · source list` — Five skills, a `jev-decide` CLI, 108 agent-supervision scenarios, and honest evals, including a negative agent result.
- [Dicklesworthstone/skillranker](https://github.com/Dicklesworthstone/skillranker) `★125 · 📚49` · [ShivamPansuriya/jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate) `★7 · 📚24` · [GodsBoy/jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router) `★23 · 📚33` · [EliaAlberti/jev-rules](https://github.com/EliaAlberti/jev-rules) `★62 · 📚27` — Show the agent only the skills and rules the current turn needs, and allow "none". jev-skill-gate cuts the skill manifest by ~75%.
- [shitianfang/jev-use](https://github.com/shitianfang/jev-use) `★33 · 📚34` — Hands agent steps that need no text output to a decision model (p50 ~230 ms). Its compaction and agreement evals are published.
- [altryne/jevify](https://github.com/altryne/jevify) `★36 · 📚30` · [samtay32/jev-system-architect](https://github.com/samtay32/jev-system-architect) `★2 · 📚23` — Audit a codebase for fuzzy judgments that could become typed decision points.
- [aitofy-dev/jev-awesome-skills](https://github.com/aitofy-dev/jev-awesome-skills) `★2 · source list` · [Pleo2/awesome-jev-agent-skills](https://github.com/Pleo2/awesome-jev-agent-skills) `★0 · source list` — Ready-made proceed/ask/stop gates, triage, diff review and QA-evidence skills.
- → [catalog/skills.md](catalog/skills.md)

### Coding-agent tooling

The largest cluster in the ecosystem. It covers Claude Code, Codex, Pi, Hermes, OpenCode and Cursor.

**Context compaction and pruning.** This is contested, so read the [evidence](docs/evidence.md#negative-and-null-results) first.
- [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) `★7,250 · 📚71` — The most-starred project in the category. It replaces Claude Code's compaction summary with keep/drop decisions per tool call, and kept content stays verbatim. It began as a [viral demo](https://x.com/tamarajtran/status/2100694549362553153).
- [tamaratran/jev-pruner](https://github.com/tamaratran/jev-pruner) `★153 · 📚35` — Trims long Bash output before the model sees it.
- [GhalebDweikat/winnow](https://github.com/GhalebDweikat/winnow) `★99 · 📚39` — A calibrated context sieve with stub/recall pointers. It falls back to an LLM-backed adapter when the decision model is unreachable.
- [kunchenguid/compact-adviser](https://github.com/kunchenguid/compact-adviser) `★189 · 📚15` — Asks "is this a safe moment to compact?"
- [joelhooks/pi-fast-jev-compaction](https://github.com/joelhooks/pi-fast-jev-compaction) `★13 · 📚27` · [leonaaardob/fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction) `★9 · 📚26` · [compozy/yoshi](https://github.com/compozy/yoshi) `★27 · 📚30` — Ports to Pi and Codex, and a pruning proxy.

**Model and effort routing.** Route at session boundaries and run in shadow mode first.
- [gargpratyush/jev-router](https://github.com/gargpratyush/jev-router) `★505 · 📚60` — Routes Claude Code and Codex to the cheapest capable model.
- [0xNatoshi/jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) `★277 · 📚54` — Per-turn model, reasoning-effort and speed routing for Codex (~60% savings on a 237-turn backtest).
- [BillionsBobby/JevRouter](https://github.com/BillionsBobby/JevRouter) `★309 · 📚42` — One candidate set covering models, tools, subagents and skills.
- [ruban-24/switchboard](https://github.com/ruban-24/switchboard) `★16 · 📚21` · [adarshmishra07/jcm-router](https://github.com/adarshmishra07/jcm-router) `★8 · 📚27` · [xinyao27/jevonian](https://github.com/xinyao27/jevonian) `★15 · 📚26` — Cache-aware routing that leaves the cached main chat alone.
- [miuuyy/Astra-Ares](https://github.com/miuuyy/Astra-Ares) `★293 · 📚15` · [nidhi-singh02/agent-router](https://github.com/nidhi-singh02/agent-router) `★99 · 📚25` · [prismhq/jev-router](https://github.com/prismhq/jev-router) `★14 · 📚29` — Mid-run effort selection, agent/CLI selection, and a router on LiteLLM.

**Guardrails and tool-call gates.** Put deterministic rules first, and choose fail-open or fail-closed explicitly.
- [leepokai/jev-guard](https://github.com/leepokai/jev-guard) `★48 · 📚38` — Deny/ask/allow auto mode for any coding agent. It uses session context, flags injection in tool results, and tracks taint. [Smoke test](https://github.com/caohy1988/jev-guard-smoke).
- [DevMortimer/pi-warden](https://github.com/DevMortimer/pi-warden) `★153 · 📚50` — Steers instead of interrupting. Rule breaks fell from 6 to 0 over 150 paired runs, and a replay on 17k calls held 42.
- [thruwire/foreman](https://github.com/thruwire/foreman) `★618 · 📚61` — A supervisor for Codex and OpenCode workers, with risk-tiered thresholds.
- [jomatsu/pi-jev-auto-mode](https://github.com/jomatsu/pi-jev-auto-mode) `★30 · 📚38` — Auto-approves Bash, write and edit calls, and **fails closed**.
- [y0usaf/pi-jev](https://github.com/y0usaf/pi-jev) `★150 · 📚54` · [Nyarlathoteppppp/pi-heed](https://github.com/Nyarlathoteppppp/pi-heed) `★10 · 📚27` · [harshwasan/jev-sentinel](https://github.com/harshwasan/jev-sentinel) `★12 · 📚19` — Pi extensions that judge whether an action is destructive, exfiltrates data, stays in scope, or matches what you asked for.
- [eugeniughelbur/jev-engineering](https://github.com/eugeniughelbur/jev-engineering) `★5 · 📚19` · [jesset/pi-verdict](https://github.com/jesset/pi-verdict) `★10 · 📚14` — Rules first, then a decision model for the grey zone. jev-engineering has a rerunnable 300-call injection test.
- [anpicasso/hermes-jev-approvals](https://github.com/anpicasso/hermes-jev-approvals) `★19 · 📚27` — Hermes command approvals: 8.7× faster, with 4.4× fewer prompts across 153 real commands.
- [luantak/is-malicious](https://github.com/luantak/is-malicious) `★32 · 📚27` · [hemanth/pkg-gate](https://github.com/hemanth/pkg-gate) `★0 · 📚16` — Screen codebases and npm lifecycle scripts before you run them.

**Done-verification, review and semantic lint**
- [devagrawal09/jev-review](https://github.com/devagrawal09/jev-review) `★646 · 📚74` — Staged code review (risk → file profile → evidence → severity → reviewer routing) with a local dashboard.
- [valentynkit/jev-belay](https://github.com/valentynkit/jev-belay) `★19 · 📚41` · [qkal/Canny](https://github.com/qkal/Canny) `★106 · 📚32` · [noplan-inc/limpet](https://github.com/noplan-inc/limpet) `★5 · 📚24` — Stop-hook gates that block an unverified "done". Canny's rule: "deterministic hooks decide, the model advises".
- [coldteadotai/abide](https://github.com/coldteadotai/abide) `★469 · 📚19` — Enforces AGENTS.md rules with one Noul per rule.
- [valentynkit/jev-commit](https://github.com/valentynkit/jev-commit) `★12 · 📚39` — A pre-commit check that the message matches the diff; it blocks only on leaked credentials.
- [NiazMorshed2007/jev-review](https://github.com/NiazMorshed2007/jev-review) `★230 · 📚48` · [supercorp-ai/supercov](https://github.com/supercorp-ai/supercov) `★141 · 📚39` · [lakeday-org/perch](https://github.com/lakeday-org/perch) `★316 · 📚29` · [mizchi/jev-lint](https://github.com/mizchi/jev-lint) `★113 · 📚23` · [doeixd/jev-pref](https://github.com/doeixd/jev-pref) `★10 · 📚32` — Continuous quality review, coverage, and linting for semantic rules that a parser can't check.
- [fatwang2/jev-review-action](https://github.com/fatwang2/jev-review-action) `★2 · 📚19` · [yamadashy/jev-labeler-action](https://github.com/yamadashy/jev-labeler-action) `★0 · 📚5` — GitHub Actions for submission review and issue/PR labels.
- → [catalog/dev.md](catalog/dev.md) · [catalog/memory.md](catalog/memory.md) · [catalog/routing.md](catalog/routing.md) · [catalog/security.md](catalog/security.md)

### Browser, desktop and mobile

The shared recipe: build a numbered list of what's on the page or screen (accessibility tree, DOM or OCR), let the decision model pick the operation and target, let code execute, and call an LLM *only* when text must be typed. Most decision models are text-only and can't see pixels.

- [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) `★21,563 · 📚76` — **The most-cited project in the entire ecosystem.** It picks the operation and element in one request and booked a Zürich→London flight search in 7.1 s for $0.0039. The [launch demo](https://x.com/gregpr07/status/2100411066966749359) has been retested: 1/20 on complex tasks.
- [awlevin/typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) `★1,098 · 📚46` — macOS computer use: OCR the screen, then a decision model picks the action, for ~$0.0002 per step.
- [droidrun/mobile-jev](https://github.com/droidrun/mobile-jev) `★426 · 📚59` — Android automation; an Uber booking took 9 actions and ~21 s.
- [moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser) `★374 · 📚49` — Voice control at ~300 ms per spoken word. URLs are copied from your words, never generated.
- [jkudish/jev-browser](https://github.com/jkudish/jev-browser) `★297 · 📚49` · [Ying-Kai-Liao/jev-browser](https://github.com/Ying-Kai-Liao/jev-browser) `★93 · 📚43` · [wy-coliney/jev-browser-use](https://github.com/wy-coliney/jev-browser-use) `★721 · 📚45` — In these, the LLM plans and the decision model decides. Ying-Kai-Liao's version solved 40/42 live tasks using ~70× fewer tokens.
- [Sac-Y/Jev-cu](https://github.com/Sac-Y/Jev-cu) `★613 · 📚28` · [lahfir/agent-desktop](https://github.com/lahfir/agent-desktop) `★1,733 · 📚16` · [savka777/jev-use](https://github.com/savka777/jev-use) `★111 · 📚22` — Desktop control through accessibility trees, with local policy gates on sensitive clicks.
- [kitze/unclutter](https://github.com/kitze/unclutter) `★343 · 📚49` · [realZachi/typesafe-adblock](https://github.com/realZachi/typesafe-adblock) `★87 · 📚46` · [anishfn/shapeshift](https://github.com/anishfn/shapeshift) `★755 · 📚23` — Browser extensions and UI: clutter removal, "is this DOM element an ad?", and a text box that morphs into the UI you mean.
- → [catalog/browser.md](catalog/browser.md)

### Search, RAG and data

- [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search) `★495 · 📚64` — Web search where a decision model does source selection, query understanding and relevance ranking. It returns links, not generated answers.
- [realZachi/pg-jev](https://github.com/realZachi/pg-jev) `★386 · 📚59` — Ask Postgres tables questions in plain language. Its batching study found 20 rows per request gave 100%, and 80 rows gave 77–94%.
- [kylemclaren/jevql](https://github.com/kylemclaren/jevql) `★14 · 📚43` · [colliber/duckdb-jev](https://github.com/colliber/duckdb-jev) `★27 · 📚19` · [mattn/sqlite3-jev](https://github.com/mattn/sqlite3-jev) `★3 · 📚15` · [giuliosmall/pg_typesafe](https://github.com/giuliosmall/pg_typesafe) `★87 · 📚34` — Semantic SQL predicates. Every row leaves your machine, so pre-filter with cheap predicates first.
- [jexp/neo4jev](https://github.com/jexp/neo4jev) `★153 · 📚52` — Graph navigation: a Choice picks the next relationship and a Noul asks "goal reached?", with beam search in the app.
- [dzhng/jevgrep](https://github.com/dzhng/jevgrep) `★1,902 · 📚23` · [keltokhy/jgrep](https://github.com/keltokhy/jgrep) `★131 · 📚32` · [uehaj/sys1grep](https://github.com/uehaj/sys1grep) `★144 · 📚36` · [sufianetaouil/every](https://github.com/sufianetaouil/every) `★7 · 📚32` · [ellipsis-dev/blink](https://github.com/ellipsis-dev/blink) `★92 · 📚45` — "grep by meaning". These send code to the API, so check what leaves your machine.
- [jerryjliu/docjev](https://github.com/jerryjliu/docjev) `★487 · 📚31` — Fast document classification and packet splitting, from LlamaIndex's founder.
- [AkashPriyadarshii/jev-curate](https://github.com/AkashPriyadarshii/jev-curate) `★92 · 📚45` · [RenaGao/jev-dataops](https://github.com/RenaGao/jev-dataops) `★60 · 📚18` — Dataset sifting (Rust, Parquet/JSONL) and streaming data selection with LoRA training.
- [WiktorB2004/llama-index-jev](https://github.com/WiktorB2004/llama-index-jev) `★8 · 📚33` · [hev/reranker](https://github.com/hev/reranker) `★14 · 📚25` · [hotchpotch/jev-reranker](https://github.com/hotchpotch/jev-reranker) `★36 · 📚21` — Rerankers. Fuse with BM25 or embeddings rather than reranking with the decision model alone.
- [keltokhy/jsort](https://github.com/keltokhy/jsort) `★24 · 📚24` · [keltokhy/jlink](https://github.com/keltokhy/jlink) `★6 · 📚21` · [keltokhy/jselect](https://github.com/keltokhy/jselect) `★3 · 📚16` — Sort by meaning (pairwise comparisons plus Bradley-Terry), record linkage, and budgeted evidence selection.
- [reachjalil/jevlogs](https://github.com/reachjalil/jevlogs) `★16 · 📚33` · [hyperspaceai/jevcache](https://github.com/hyperspaceai/jevcache) `★76 · 📚17` — OpenTelemetry log triage, and a decision cache for deterministic CI replay.
- → [catalog/data.md](catalog/data.md)

### Evaluation, calibration and QA tooling

- [abhixhek/jevcal](https://github.com/abhixhek/jevcal) `★10 · 📚41` — **Stop guessing thresholds.** It fits per-question thresholds on your labels, verifies them on held-out data, and fails CI when a model update breaks them. Cited in more "best practice" sections than any other tool.
- [sutro-sh/jev-align](https://github.com/sutro-sh/jev-align) `★300 · 📚42` — Builds calibrated "AI functions" from human feedback, using active labelling plus GEPA to optimize the questions.
- [AbdelStark/jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks) `★21 · 📚33` · [jmanhype/jev-dspy-lab](https://github.com/jmanhype/jev-dspy-lab) `★10 · 📚22` — Calibration, selective risk, and record/replay in DSPy.
- [openlayer-ai/jevals](https://github.com/openlayer-ai/jevals) `★98 · 📚26` — Agent evals and guardrails as typed decisions (it also runs locally with Kev or Laya): eight judgments per trace for ~$0.00006.
- [smkrv/jev-calibrate](https://github.com/smkrv/jev-calibrate) `★31 · 📚17` · [nikkoxgonzales/jev-certify](https://github.com/nikkoxgonzales/jev-certify) `★1 · 📚11` · [sathariels/jevcheck](https://github.com/sathariels/jevcheck) `★2 · 📚7` · [vcjdeboer/jev-reliability](https://github.com/vcjdeboer/jev-reliability) `📚4` — Criteria tuning, conformal routing bounds, behavioural contract tests that refuse `jev-latest`, and repeatability/phrasing preflights.
- [suraj-phanindra/wellposed](https://github.com/suraj-phanindra/wellposed) `★2 · 📚17` · [ariel-frischer/jevkit](https://github.com/ariel-frischer/jevkit) `★3 · 📚22` · [simota/tenbin](https://github.com/simota/tenbin) `★4 · 📚18` — Lint your questions offline, before you pay for calls.
- [AntonioCoppe/jev-harness](https://github.com/AntonioCoppe/jev-harness) `★15 · 📚31` — Confidence gates, shadow mode, recipes and evals (on a row-filter job, Claude CLI took 48.9 s and the decision model 1.3 s).
- [mandu5/jevcompat](https://github.com/mandu5/jevcompat) `★0 · 📚6` — A conformance suite for `/v1/systemone`-compatible servers. Use it to check whether a Jev-like model really is a drop-in.
- → [catalog/bench.md](catalog/bench.md)

### Games, robotics and simulation

The recipe for games and control: feed structured state (RAM → JSON, legal-move lists), never pixels. Let code own the physics, the route and the arithmetic, and let the decision model pick at branches. Keep a fast deterministic reflex layer that can veto it.

- [fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario) `★422 · 📚64` — Super Mario Bros. from structured emulator RAM. It is the canonical "state as data" example.
- [RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone) `★228 · 📚66` — A MuJoCo drone. The decision model advises at 2.5 Hz while a 50 Hz reflex layer holds a veto.
- [valentynkit/jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) `★9 · 📚38` — Code owns the route and the arithmetic, the model picks at branches in ~100 ms, and calibration is measured with Brier scores.
- [dabit3/jev-experiments](https://github.com/dabit3/jev-experiments) `★397 · 📚38` — 22 latency-focused demo apps by Nader Dabit.
- [phyous/tsai-sc](https://github.com/phyous/tsai-sc) `★27 · 📚45` · [sorrycc/typesafe-snake](https://github.com/sorrycc/typesafe-snake) `★23 · 📚32` · [standardagents/jevpilot](https://github.com/standardagents/jevpilot) `★204 · 📚32` · [rmalde/minecraft-agent](https://github.com/rmalde/minecraft-agent) `★568 · 📚18` — StarCraft, Snake (legal moves generated in code), a driving autopilot, and Minecraft (an LLM plans, the decision model acts).
- [FBddcz/embodied-jev](https://github.com/FBddcz/embodied-jev) `★249 · 📚30` · [Dimweaker/jev-libero](https://github.com/Dimweaker/jev-libero) `★78 · 📚23` · [TarunTomar122/jev-askable-arm](https://github.com/TarunTomar122/jev-askable-arm) `★11 · 📚27` · [openroboto-ai/jev-robot-control](https://github.com/openroboto-ai/jev-robot-control) `★53 · 📚13` — Robot arms that pick primitives from menus, never torques. OpenRoboto compares Jev with GPT-6 Astra on cost and time.
- → [catalog/games.md](catalog/games.md) · [Frank-ZY-Dou/awesome-jev](https://github.com/Frank-ZY-Dou/awesome-jev) covers robotics in depth.

### Apps and domain applications

- [AboveColin/HA-Jev](https://github.com/AboveColin/HA-Jev) `★68 · 📚56` — Home Assistant: ask your house a question and get a number back, as sensors and automation actions.
- [jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader) `★2,708 · 📚71` — One trade decision per Monad block (~81 ms). It's educational: no list reports sustained trading profit, and bots should be dry-run by default.
- [kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) `★483 · 📚41` — IRS form pages: 100% strict on 261 forms at ~$0.001 per page, replacing production Sonnet.
- [fazlerocks/jevmail](https://github.com/fazlerocks/jevmail) `★92 · 📚27` · [parth-kp/jev-mail-classifier](https://github.com/parth-kp/jev-mail-classifier) `★19 · 📚19` — Gmail triage: 1,000 emails in ~1 minute for ~3 cents.
- [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) `★7,181 · 📚37` — A read-only chat copilot for phones. An LLM drafts replies, a decision model ranks them, and you choose whether to send.
- [socai-io/jev-social](https://github.com/socai-io/jev-social) `★130 · 📚42` · [AkashPriyadarshii/jev-seo](https://github.com/AkashPriyadarshii/jev-seo) `★88 · 📚32` · [usenotra/notra](https://github.com/usenotra/notra) `★225 · 📚19` — Social research, SEO/GEO audits, and a production GEO platform.
- [brainstormity/Jev-Moderation-Bot](https://github.com/brainstormity/Jev-Moderation-Bot) `★47 · 📚36` · [backmeupplz/jev_antispam_bot](https://github.com/backmeupplz/jev_antispam_bot) `★13 · 📚20` — Discord and Telegram moderation.
- [OpenByteInc/QuantDinger](https://github.com/OpenByteInc/QuantDinger) `★12,344 · 📚29` — An AI trading OS that uses a decision model as an evidence and risk gate. It blocks entries but lets exits and protective orders through.
- [choxos/jev-reviewer](https://github.com/choxos/jev-reviewer) `★37 · 📚22` · [youkiti/tiab-review-plugin](https://github.com/youkiti/tiab-review-plugin) — Systematic-review screening (95% recall on 16,645 records) and extraction.
- [monteduro/killmyidea](https://github.com/monteduro/killmyidea) `★244 · 📚33` · [ChetasLua/jevmeter](https://github.com/ChetasLua/jevmeter) `★102 · 📚45` — Fun ones: kill, fix or ship your startup idea, and a live decision meter on any video.
- → [catalog/apps.md](catalog/apps.md) · [catalog/finance.md](catalog/finance.md) · [catalog/agents.md](catalog/agents.md)

---

## Benchmarks and independent studies

Summarized with numbers in [docs/evidence.md](docs/evidence.md).

- [punk2898/awesome-jev-verified](https://github.com/punk2898/awesome-jev-verified) — **The best claim-by-claim audit.** An open 2,390-question benchmark with per-question logs, run against four GPT models. It confirms the price, but not "sub-100 ms", "445× cheaper" or "eliminates hallucination".
- [fstandhartinger/jevbench](https://github.com/fstandhartinger/jevbench) `★189 · 📚40` — JevBench: 534 frozen, half-sealed decisions and a four-axis composite across 40+ systems. See also the [Benchmark Heaven](https://benchmarkheaven.com/jev-models) leaderboard.
- [Jevals.com](https://jevals.com/) `📚12` — Jev vs six LLMs on human-labelled sets, with the data published.
- [OpenRouter: Is Jev as accurate as frontier models?](https://openrouter.ai/blog/insights/jev-vs-claude-opus-5-classification/) — Banking77: 81.0% vs Opus 5's 84.4%, at 175 ms vs 2,266 ms and $0.11 vs $2.42 per 1k.
- [willkelly/jev-evaluation](https://github.com/willkelly/jev-evaluation) `★0 · 📚11` — 123,805 pre-registered requests. ECE was 0.075 in-domain, but calibration fails OOD and authority injection works.
- [anisselbd/jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench) `★7 · 📚32` — The canonical **question-atomization** lesson: 62.6% with one question vs 95.0% atomized. Haiku 4.5 wins the direct question.
- [ickma2311/jev-baselines-eval](https://github.com/ickma2311/jev-baselines-eval) `★5 · 📚12` · [bitnovus/jev-spam-eval](https://github.com/bitnovus/jev-spam-eval) `★2 · 📚34` — Classical baselines win in-domain, but Jev wins under drift.
- [anessbelbati/jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench) `★9 · 📚39` · [zhuyansen/jev-search-rerank-eval](https://github.com/zhuyansen/jev-search-rerank-eval) `★9 · 📚31` — Reranking: Jev ties Cohere, but doesn't beat embeddings alone, so fuse them.
- [jujumilk3/jev-calibration-audit](https://github.com/jujumilk3/jev-calibration-audit) `★0 · 📚15` · [KantaHayashiAI/jev-does-not-play-dice](https://github.com/KantaHayashiAI/jev-does-not-play-dice) `★3 · 📚17` · [scienthoon/jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) `★6 · 📚25` · [jourdanlabs/assay-001](https://github.com/jourdanlabs/assay-001) `★0 · 📚18` — Calibration audits covering abstention, known probabilities, OOD, and a pre-registered test.
- [Gaurav-Gosain/jev-sec-bench](https://github.com/Gaurav-Gosain/jev-sec-bench) `★3 · 📚31` · [zkousama/jagged](https://github.com/zkousama/jagged) `📚4` — Prompt injection and vulnerable-code detection.
- [nekuda-ai/WindTunnel](https://github.com/nekuda-ai/WindTunnel) `★86 · 📚18` — WebMCP: Jev + Mercury solved 49/49 tasks, bare Jev 25/49.
- [Zaious/jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas) `★26 · 📚27` · [RINNECODER/jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study) `★3 · 📚23` · [FirasSX914/Janus](https://github.com/FirasSX914/Janus) `★2 · 📚25` — Where Jev holds up vs breaks, order and lost-in-the-middle effects, and when routing is worth it.
- [thevibeworks lab](https://github.com/thevibeworks/awesome-typesafe-jev/tree/main/lab) · [rhc98 calibration report](https://github.com/rhc98/awesome-jev) · [wuyoscar evals](https://github.com/wuyoscar/jev-skill/blob/main/evals/RESULTS.md) — First-hand measurements published inside source lists.
- Write-ups:
  - [agentjournal.dev](https://agentjournal.dev/blog/llm-judge-vs-feature-extraction/) `📚21`: one judge call vs dimension scores.
  - [amankumar.ai](https://amankumar.ai/blogs/jev-measured): 16,000 calls; "a filter, not a replacement".
  - [primeline.cc](https://primeline.cc/blog/typesafe-jev-pre-registered-test): pre-registered; 4 of 12 failure modes real.
  - [Every's vibe check](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds) `📚19`
  - [Lindfors](https://lindfors.no/blog/a-first-look-at-typesafes-jev/)
  - [Near Here](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation) `📚14`
  - [YTAL production replay](https://ytal.io/blog/typesafe-jev-entity-resolution-production-replay/): not adopted.
- → [catalog/bench.md](catalog/bench.md)

## Research papers

~35 papers on Jev and Jev-like models appeared within two weeks, all unreplicated preprints. The full annotated list is in [docs/papers.md](docs/papers.md).

- [Jev in the Wild](https://arxiv.org/abs/2609.30216) `📚18` — An ecosystem survey of 2,170 GitHub projects.
- [JEV-as-a-Judge](https://arxiv.org/abs/2609.26550) `📚7` · [JEV vs. LLMs as Rubric Judges](https://arxiv.org/abs/2609.29769) `📚5` — Jev comes within ~3 pts of GPT-6 at ~0.36% of the cost, but LLMs repeat its confident errors, which caps cascade gains.
- [Type-Safe Is Not Error-Free](https://arxiv.org/abs/2609.26758) `📚5` · [JevOut](https://arxiv.org/abs/2609.30243) `📚4` · [JevAdvBench](https://arxiv.org/abs/2609.31142) `📚5` · [Decision Hijacking](https://arxiv.org/abs/2609.28613) `📚6` — Robustness: option names, natural context and injection.
- [REFLEX](https://arxiv.org/abs/2609.26532) `📚4` · [Jev-Mobile](https://arxiv.org/abs/2609.30186) `📚4` · [JEV-Star](https://arxiv.org/abs/2609.27331) · [Jev-Mem](https://arxiv.org/abs/2609.23986) `📚6` — Planner/executor agents that make 66–73% fewer strong-model calls.
- [Evaluating Decision Models for Text Annotation in CSS](https://arxiv.org/abs/2609.24574) · [Calibrated Decisions at Scale: crash narratives](https://arxiv.org/abs/2609.24052) `📚4` · [Just Ask Jev](https://arxiv.org/abs/2609.29429) `📚7` — Annotation, large-scale coding and alignment-failure detection.
- [Typed Decision Models: An Early Evidence Audit](https://arxiv.org/abs/2609.32160) — Across 28 papers there is no independent accuracy advantage; the gains are latency and cost.

## Articles, analysis and critique

**Analysis**
- [Simon Willison: Jev introduces a new shape of LLM](https://simonwillison.net/2026/Sep/21/jev/) — An influential early analysis.
- [Latent Space: Jev, System One models for Prod, Not God](https://www.latent.space/p/jev) — A founder interview (2h21m). Also: [a System One model that only decides](https://latent.space/p/ainews-jev-a-system-one-model-that) `📚11` and [6 clones of Jev in 2 days](https://www.latent.space/p/ainews-here-are-6-clones-of-jev-in).
- [Sean Goedecke: Jev means structured output is interesting again](https://www.seangoedecke.com/jev-means-structured-output-is-interesting-again/) — A skeptical technical take. A one-constrained-token baseline gets 2–3× speedups.
- [Warmer Sun: Typed decisions, not chat](https://warmersun.com/jev/) — Separates the launch claims from the vendor's own footnotes.
- [Flavio Copes: A deep dive into Jev](https://flaviocopes.com/jev/) `📚17` — Often named as the best long-form introduction.
- [Pere Pages: Jev sorted](https://pearpages.com/blog/2026/09/16/jev-sorted-what-typesafes-system-one-model-actually-is-and-what-is-still-just-a-claim) · [sgnt.ai: You could have built Jev](https://sgnt.ai/p/jev/) · [Archer Hume: Jev's architecture unmasked](https://archerhume.com/posts/jevs-architecture-unmasked) — Claim-by-claim decoding, the single-token-logit recipe, and an architecture inferred from ~10k API calls.
- [Anthony Maio: The language model that won't talk](https://anthonymaio.substack.com/p/jev-the-language-model-that-wont) `📚8` · [TrueFoundry: What actually shipped](https://www.truefoundry.com/blog/typesafe-ai-jev) · [Silverthread Labs: What the 193× benchmark doesn't measure](https://www.silverthreadlabs.com/blog/jev-ai-benchmark-limitations) · [ContextOS: production engineering review](https://contextosai.com/blog/jev-system-one-models-when-ai-returns-decisions) — Critiques.
- [Sebastian Raschka: From bag-of-words to Jev](https://magazine.sebastianraschka.com/p/classifier-history-and-jev) · [Vercel: What is Jev?](https://vercel.com/i/what-is-jev) · [OpenRouter: Jev vs LLM, when to use each](https://openrouter.ai/blog/tutorials/jev-vs-llm-when-to-use-each/) — Context and positioning.

**News**
- [TechCrunch](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)
- [The Register: plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711) · [The Register: Shut up and calculate](https://www.theregister.com/devops/2026/09/23/shut-up-and-calculate-jevs-new-ai-primitives-for-coders/5298431)
- [Business Wire: $40M seed](https://www.businesswire.com/news/home/20260915525333/en/)
- [Forkast: Not an LLM, and that may be the point](https://forkast.news/typesafe-ais-jev-is-not-an-llm-and-that-may-be-the-point/)
- [The New Stack: OpenAI's Decision API](https://thenewstack.io/openai-decision-api-luna/)
- Chinese coverage: [36Kr](https://m.36kr.com/p/3988164509711361) · [Huxiu hands-on](https://www.huxiu.com/article/4892583.html)

**Community discussion**
- [HN launch thread](https://news.ycombinator.com/item?id=49717558)
- [Ask HN: Noul as a decision primitive](https://news.ycombinator.com/item?id=49760225)
- ["It's the inference technique, not the training"](https://x.com/anderslie/status/2100388704644919662)
- ["The threshold is part of the prompt"](https://x.com/sakevoid/status/2102896039678382177)
- [tanxarx/awesome-jev](https://github.com/tanxarx/awesome-jev) collects ~65 skeptical threads with numbers.
- → [catalog/community.md](catalog/community.md) (3,000+ threads and posts)

## Learning resources

- [Li-Evan/awesome-jev: cheatsheet](https://github.com/Li-Evan/awesome-jev/blob/main/cheatsheet.md) — **The best one-page technical reference**, covering endpoint, schemas, limits, jaggedness workarounds and composition moves. Li-Evan also publishes a free Chinese book, *Jev in Practice*.
- [disler/ten-levels-of-jev](https://github.com/disler/ten-levels-of-jev) `★124 · 📚10` — From one smart if-statement to a coding agent that reaches for a decision model on its own.
- [harshithsunku/learn-jev-end-to-end](https://github.com/harshithsunku/learn-jev-end-to-end) `★14 · 📚15` — A free hands-on course: 13 agent use cases, a fast brain and a slow brain, one OpenRouter key.
- [nexibeo/jev-cookbook](https://github.com/nexibeo/jev-cookbook) `★34 · 📚27` · [datawhalechina/jev-cookbook](https://github.com/datawhalechina/jev-cookbook) `★46 · 📚14` · [paramjeetn/jev-cookbook](https://github.com/paramjeetn/jev-cookbook) `★7 · 📚11` — Tested recipes on OpenRouter, 18 Chinese notebook recipes with evals and local fine-tuning, and 120+ use cases.
- [dog-last/awesome-jev](https://github.com/dog-last/awesome-jev) — A "should you use a decision model?" decision tree and cookbooks tested in CI against the live API.
- [Justmalhar/awesome-jev-apps](https://github.com/Justmalhar/awesome-jev-apps) — 100 runnable apps, plus an [app spec](https://github.com/Justmalhar/awesome-jev-apps/blob/main/docs/APP_SPEC.md) that lists what never to ask the model.
- [vicfei/awesome-jev-prompts](https://github.com/vicfei/awesome-jev-prompts) — 43 question-design patterns and 10 anti-patterns.
- [davila7/jev-explained](https://github.com/davila7/jev-explained) `★33 · 📚14` · [Foadsf/jev-for-engineers](https://github.com/Foadsf/jev-for-engineers) `★5 · 📚23` · [PromptEngineer48/langchain-jev-tutorial](https://github.com/PromptEngineer48/langchain-jev-tutorial) — An illustrated primitives guide, engineering examples, and a LangChain support-ops agent.
- Articles and videos:
  - [Real Python: Get started with Jev](https://realpython.com/jev-python/)
  - [MarkTechPost coding guide](https://www.marktechpost.com/2026/09/23/a-coding-guide-to-typesafe-ai-jev/)
  - [Valyu AI practical guide](https://dev.to/valyuai/how-to-use-jev-a-practical-guide-to-typesafes-system-one-model-g5e) `📚9`
  - [Sam Witteveen video](https://www.youtube.com/watch?v=X117w2Rark8)
  - [WebDevCody critique video](https://www.youtube.com/watch?v=lDmrk_7D-W8)
  - [jev-tutorial.org](https://www.jev-tutorial.org/) (multilingual)
- Chinese and Japanese:
  - [Bald0Wang/jev-docs-zh](https://github.com/Bald0Wang/jev-docs-zh): Chinese translation of the docs.
  - [yibie/jev-engineering-zh](https://github.com/yibie/jev-engineering-zh): the founder's design notes in Chinese.
  - [kuhung/understanding-jev](https://github.com/kuhung/understanding-jev)
  - [yzfly/awesome-jev-zh](https://github.com/yzfly/awesome-jev-zh)
  - [mukishitsuu-png/awesome-jev-ja](https://github.com/mukishitsuu-png/awesome-jev-ja)
- → [catalog/learn.md](catalog/learn.md)

## Directories and other lists

- **Live directories:**
  - [awesomejev.com](https://awesomejev.com/) `📚9`
  - [madewithjev.com](https://madewithjev.com) `📚14`: builds with reported cost and speed.
  - [jevusers.com](https://jevusers.com)
  - [jevlist.ai](https://jevlist.ai/)
  - [mrjev.com](https://mrjev.com/best-jev-tools/): hands-on security reviews.
  - [jevforagents.com](https://jevforagents.com)
  - [awesomejev.cc](https://awesomejev.cc) `📚4`
  - [logicrw radar](https://logicrw.github.io/awesome-jev-projects/en/)
  - [systemonemodels.org](https://systemonemodels.org/models/jev/)
- **The 106 source lists:** [sources.md](sources.md) has stars, pull dates and commits. [docs/source-lists.md](docs/source-lists.md) says **which list to read for what**, and which to treat with caution.
- **Most-starred sources:**
  - [yibie/awesome-jev](https://github.com/yibie/awesome-jev)
  - [heyjunpenn/awesome-jev](https://github.com/heyjunpenn/awesome-jev)
  - [Anil-matcha/awesome-jev-by-typesafe](https://github.com/Anil-matcha/awesome-jev-by-typesafe)
  - [v-modal/awesome-jev-tools](https://github.com/v-modal/awesome-jev-tools)
  - [logicrw/awesome-jev-projects](https://github.com/logicrw/awesome-jev-projects)
  - [kydlikebtc/awesome-jev](https://github.com/kydlikebtc/awesome-jev)
  - [AnotiaWang/awesome-jev](https://github.com/AnotiaWang/awesome-jev)
  - [AbdelStark/awesome-typesafe-jev](https://github.com/AbdelStark/awesome-typesafe-jev)
- **Specialized sources:**
  - Robustness: [Yifan-Lan/awesome-jev-robustness](https://github.com/Yifan-Lan/awesome-jev-robustness)
  - Security papers: [Sarim-MBZUAI/awesome-jev-security](https://github.com/Sarim-MBZUAI/awesome-jev-security)
  - Papers: [OmniJev/awesome-jev-papers](https://github.com/OmniJev/awesome-jev-papers)
  - Open models: [andyrewlee/awesome-system-one](https://github.com/andyrewlee/awesome-system-one)
  - Robotics: [Frank-ZY-Dou/awesome-jev](https://github.com/Frank-ZY-Dou/awesome-jev)

---

## About this meta-list

**How it was built**
1. **Pull.** All 106 source repositories listed in [sources.md](sources.md) were shallow-cloned on 2026-09-30. Their star counts and commits were recorded.
2. **Union.** Every Markdown link in every file was extracted: 127k link occurrences, which de-duplicate to 18,330 unique entries after URL normalization. GitHub deep links collapse to `owner/repo`, and links to the source lists themselves are dropped.
3. **Consensus.** For each entry, `📚` counts how many *distinct* lists cite it.
4. **Verification.** The 2,533 GitHub entries cited by ≥5 lists were fetched live to confirm they exist, follow renames, and record stars and descriptions. The 21 that didn't resolve are listed in [catalog/unresolved.md](catalog/unresolved.md).
5. **Categorization.** Entries were categorized automatically for the [catalog](catalog/README.md). The sections above were **hand-curated**.
6. **Synthesis.** Every source list was read in full. Per-source notes are in [docs/source-notes/](docs/source-notes/). The insights, the reconciled facts and the evidence digest in [docs/](docs/) were synthesized from those notes.

**Caveats**
- This is a snapshot of a two-week-old ecosystem. Specs, prices and access change quickly, so check the [official models page](https://docs.typesafe.ai/models).
- Most numbers are author-reported and unreplicated. They are labelled as such where it matters.
- Inclusion is not endorsement. Many launch-week repos are thin scaffolds, and many tools send your data to third parties.
- This list is not affiliated with any model vendor.

**Updating**
```bash
scripts/refresh.sh      # re-pull all sources → stars/commits → catalog → sources.md → README numbers
```
To add a source, append its GitHub URL to [sources.md](sources.md) and refresh. The hand-written synthesis in `docs/` and `templates/README.md.tmpl` should then be reviewed against `git diff catalog/`.

**Repository layout**
```
README.md                  ← generated from templates/README.md.tmpl (live ★/📚 numbers)
sources.md                 ← the 106 sources: stars, pull date, commit
docs/                      ← synthesis: what-is-jev, patterns, evidence, open-models, papers, source-lists
docs/source-notes/         ← one review note per source list
catalog/                   ← the complete categorized union (18,330 entries)
data/                      ← catalog.json/csv, sources.json, verified.tsv, source_profiles.json
scripts/                   ← pull_sources, extract_links, build_catalog, verify_github, render_*, refresh.sh
```
