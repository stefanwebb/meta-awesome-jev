# Awesome-llms-labs/awesome-jev
- **One-liner:** Explainer-style awesome list with specs, API reference, honest benchmark scorecard, limitations, use-case table, runnable examples, and a large set of third-party articles on Jev.
- **Language(s):** English
- **Type:** curated-list (with tutorial/study-guide components and example code)
- **Scale:** ~100 links in README plus docs/ (getting-started, api-reference, recipes, benchmarks, comparisons, glossary) and examples/ (quickstart.py, confidence_gate.py, ticket_triage.py, curl.sh, js/quickstart.mjs — offline `--demo` mock mode). Sections: What is Jev?, Three Primitives, Quickstart, Specifications, Official Resources, SDKs, Gateway & Platform Integrations, How It Works, Benchmarks & Evaluations, Limitations & Failure Modes, Use Cases, Community Projects, Open-Source Ecosystem & Clones, Articles & Explainers (Overviews / Technical deep dives / Company & launch / Critical & security / Domain playbooks), Comparisons, FAQ.
- **Quality flags:** Badges/CI point to dakotac1994/awesome-jev — this is a mirror/copy under a different org ("Awesome-llms-labs"). Several "official" links are bare homepages (https://x.com, https://pypi.org, https://www.npmjs.com, https://vercel.com, https://openrouter.ai, https://www.netlify.com) — placeholder-quality links. Many community projects are named without links or linked only via secondary roundups (Julian Goldie, eChai). Article list includes SEO-ish sites (KuCoin, Karmactive, BinaryPH). Writing appears LLM-assisted but content is substantive and caveated.
- **Unique value:** The most detailed digest of TypeSafe's own launch-eval methodology caveats (reference labels = GPT-6 Astra + Claude Fable 5.1 average; averages 97.8×/149.2× vs headline 193.6×/444.6×; accuracy 67.8%), independent checks (RFQ, crash-narrative recalibration), vendor-risk notes (no SOC 2, hosted-only), and SDK internals (RetryPolicy, typed errors, typed response subclasses).

## Facts claimed about Jev
- TypeSafe AI (San Francisco) emerged from ~two years stealth **Sept 15, 2026** with **$40M seed led by DCVC**; founded **2024** by **Diogo Almeida** (CEO; ex-OpenAI, "co-inventor of RLHF and InstructGPT" — other sources say "co-inventor of ChatGPT"/instruction-following), **Erik Gafni**, **Sasha Sheng**. Name nods to Jevons Paradox. Launch thread "39M+ views" (Doomers case study).
- Primitives: Choice (≤255 options; option, per-option probability, confidence), Score (score, per-level probability, confidence), Noul (single probability 0–1). Questions evaluated in parallel and in isolation; adding questions barely changes latency.
- Spec table: alias `jev-latest` → `jev-1.13.0`; `POST https://api.typesafe.ai/v1/systemone`; state = string/JSON object/array; **64k tokens per request (32k reserved for state + longest single question)**; latency 70–500 ms; **$0.042/M input, output free**; text only; English primary; **not trained on customer data, no per-account fine-tuning**; signups opened to all **Sept 20** with **$5 free credit**, then **paused Sept 22**.
- Sample response includes `"usage": {"input_tokens": 312, "output_tokens": 48}` — output tokens counted but not billed.
- Python SDK: Python 3.10+, `TypeSafeClient`, `AsyncTypeSafeClient`, Pydantic `ChoiceAnswer`/`ScoreAnswer`/`NoulAnswer`, subclass `SystemOneResponse` for typed attributes, `RetryPolicy(max_retries, backoff_initial, backoff_max, timeout)`, errors `TypeSafeError` (client-side) and `TypeSafeAPIError` (HTTP). JS: `new TypeSafeClient({apiKey})`, `Choice({...})`, `Noul({...})` (note: other lists show lowercase `choice()`/`noul()` helpers — possible inconsistency).
- "Official LangChain integration" package `langchain-typesafe` (unlinked, unverified).
- Gateways: Vercel AI Gateway `typesafe-ai/jev` (AI SDK 7 `evaluate`), OpenRouter beta `typesafe/jev-1.13`, Cloudflare Workers AI `env.AI.run`, **Netlify AI Gateway**, **LiteLLM** pass-through.
- Internals: transformer-based, new architecture + parallel sampler; RLCD (vs RLHF preference, RLVR verifiable correctness); no paper; **all training data synthetic** (per Latent Space); behavior shaped only in request.
- TypeSafe workflow evals: 193.6×/444.6× high end; **average across eight setups 97.8× faster / 149.2× cheaper**; 444.6× is Jev vs Opus 5; accuracy **67.8%** (= Sonnet 5; GPT-5.6 Sol 74.1%); invoice processing 61.8% vs Sol 79.1%; "0% hallucination" is "not empirical. Schema matching is guaranteed."; reference labels = average of GPT-6 Astra and Claude Fable 5.1 at high thinking; workflows made by TypeSafe's capability team ("some bias could exist"); timings from US West Coast laptops; no public-benchmark results.
- Independent: TrueStandard ~1.7× faster for single decision, ~100× multi-step; crash-narrative preprint F1 0.908, ECE 0.0231→0.0069 after out-of-fold recalibration, four variables F1 < 0.70 (note: Promethe-us reports same paper without the calibration-failure detail); 12,000 RFQs — Jev 91.9% acc, ECE 0.049, 86.5% auto-accepted at 95% precision vs Qwen3.5-35B 89.6% (69 malformed) vs Laya 421M 78.0%, ECE 0.322; eight-day review: "levels with mid-price LLMs, behind the frontier", jaggedness ("refund" 0.72 vs "not a refund" 0.47 on same ticket).
- mini-jev 0.909 vs Jev 0.907 over 6,750 observations; OpenJev 714 HN points.
- Vendor risk: hosted-only, no on-prem/VPC, no SOC 2/ISO 27001 listed; enterprise zero-data-retention exists; founder says launch pricing can't be proven unsubsidized.
- Failure-modes page lists: literal interpretation, sarcasm, double negatives, arithmetic/counting, dates, long irrelevant input, adversarial phrasing.

## Key insights / patterns
- Use the answer for *what*, confidence for *whether to act*. Example thresholds in examples/confidence_gate.py: AUTO_ACT 0.90, REVIEW 0.60. Earendil: ~50% → human review, ~95% → autonomous.
- JSON mode vs Jev: JSON mode constrains generation; Jev constrains the answer space at the interface — no parsing/validation, parallel answers; they compose.
- Don't use for arithmetic/dates (use code), generated text, deep multi-step reasoning, sarcasm-heavy/adversarial input without review.
- Wrap Jev calls in a swappable interface (vendor risk).
- Open clones: logit rankings ≠ calibrated probabilities; calibration is the gap clones can't easily close.
- Best fits sit next to an LLM: agent control plane (next tool, stop/retry/escalate, transient failure?), guardrails/judges, support triage, trust & safety, risk/fraud, model routing (Higgsfield across 50 models), GTM, security triage, data-pipeline QC, realtime control, dev workflow (test-failure attribution).

## Standout entries
- [Latent Space: Jev — System One Models for Prod, Not God](https://www.latent.space/p/jev) — founder interview (interview)
- [Shut up and calculate — The Register](https://www.theregister.com/devops/2026/09/23/shut-up-and-calculate-jevs-new-ai-primitives-for-coders/5298431) — press analysis (article)
- [A Coding Guide to TypeSafe AI Jev — MarkTechPost](https://www.marktechpost.com/2026/09/23/a-coding-guide-to-typesafe-ai-jev/) — tutorial incl. speculative fan-out (tutorial)
- [Jev After Eight Days of Independent Tests — DEV](https://dev.to/gde/jev-after-eight-days-of-independent-tests-level-with-mid-price-llms-behind-the-frontier-1kln) — independent review (evaluation)
- [We Tested a 35B LLM Against Typed-Decision Models on 12,000 Real RFQs — DEV](https://dev.to/cookies_c9dc8b91f33d29250/we-tested-a-35b-llm-against-typed-decision-models-on-12000-real-rfqs-confidence-changed-the-winner-56hh) — calibration-decisive benchmark (evaluation)
- [Jev AI Limitations: What the 193x Benchmark Doesn't Measure — Silverthread Labs](https://www.silverthreadlabs.com/blog/jev-ai-benchmark-limitations) — critique (critique)
- [Jev and System One Models: A Production Engineering Review — ContextOS](https://contextosai.com/blog/jev-system-one-models-when-ai-returns-decisions) — production review (critique)
- [Zyte: Jev and web scraping](https://www.zyte.com/blog/jev-the-model-that-cannot-write-a-word-and-where-it-fits-in-web-scraping-does-it/) — domain fit + clones (article)
- [Firecrawl: What Is Jev?](https://www.firecrawl.dev/blog/what-is-jev) — developer use cases (article)
- [The Decision Layer Eating the Agent Harness — AI Beat](https://ai-beat.github.io/news/2026/09/jev-agent-decision-layer/) — agent harness analysis (article)
- [Security-side view — LinkedIn](https://www.linkedin.com/pulse/why-everyone-suddenly-talking-jev-look-from-security-side-onal-vbmge) — security perspective (security)
- [TypeSafe AI emerges from stealth — HPCwire/AIwire](https://www.hpcwire.com/aiwire/2026/09/16/typesafe-ai-emerges-from-stealth-with-40m-in-funding-with-new-model-for-composable-ai/) — launch coverage (news)
- [Made with Jev (Product Hunt)](https://www.producthunt.com/products/made-with-jev) — 186 builds collection (directory)
- [Jev for GTM — MarketBetter](https://marketbetter.ai/blog/jev-for-gtm-decision-model-playbook/) — sales playbook (domain)
