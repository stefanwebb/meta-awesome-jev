# Reference Docs & SDKs (Jev)

> The /v1/systemone reference: docs, SDKs, cookbooks and evals published alongside Jev, the first Jev-like model.
>
> **131 entries** · generated 2026-10-01 from 106 source lists · [← catalog index](README.md) · [← main list](../README.md)

**Legend:** `📚N` = cited by N independent source lists (the consensus signal) · `★N` = GitHub stars when verified on the pull date. Entries are auto-categorized; one entry lives in exactly one category.

## Consensus (cited by 10+ lists) — 55

- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) `★2,491 · 📚68` — Agent skills for building with TypeSafe's System One API
- [typesafe-ai/system-one-adapter-python](https://github.com/typesafe-ai/system-one-adapter-python) `★368 · 📚61` — Drop-in TypeSafeClient replacement backed by LLM APIs
- [typesafe-ai/typesafe-sdk-python](https://github.com/typesafe-ai/typesafe-sdk-python) `★257 · 📚59` — The official Python library for the TypeSafe API.
- [typesafe-ai/typesafe-sdk-js](https://github.com/typesafe-ai/typesafe-sdk-js) `★260 · 📚57` — The official TypeScript/JavaScript library for the TypeSafe API
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) `📚57` — Introducing System One Models & Jev - TypeSafe's launch post: RLCD, parallel sampling, and how this differs from an LLM.
- [TypeSafe AI](https://typesafe.ai) `📚54` — A curated list of resources about Jev — the first "System One" Decision Model by TypeSafe AI, launched on September 15, 2026.
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) `📚35` — TypeSafe's documented failure modes: literal reading, counting, dates, indirection, distractor state, adversarial content.
- [Workflow evals](https://evals.typesafe.ai) `📚32` — TypeSafe workflow evaluations - Vendor evaluations; read how reference answers and comparisons are constructed.
- [API reference](https://docs.typesafe.ai/api) `📚31` — HTTP reference for POST /v1/systemone: request body (state, model, questions), answer shapes per question type, rate-limit handling.
- [Confidence](https://docs.typesafe.ai/confidence) `📚30` — How TypeSafe reports certainty, how confidence differs from probability, and how to use it to decide whether code should act.
- [Documentation](https://docs.typesafe.ai) `📚29` — Jev is TypeSafe's System One model for probability-based yes/no judgments, choices, and scores rather than generated text.
- [Introduction](https://docs.typesafe.ai/introduction) `📚29` — Evaluates documents using TypeSafe Jev via the TypeSafe Jev API with only category names and zero prompt definitions.
- [Quick start](https://docs.typesafe.ai/introduction/quickstart) `📚29` — Quickstart — Official docs: POST /v1/systemone, question types (choice up to 255 options, noul yes/no, score).
- [Primitives](https://docs.typesafe.ai/primitives) `📚27` — Decision Primitives — Explains Noul, Choice, and Score outputs and when each primitive fits a decision problem.
- [Models](https://docs.typesafe.ai/models) `📚24` — Model card for jev-1.13.0: $0.042 per million input tokens, free output, rate limits, 64k context (32k for state), text-only input.
- [Parallel questions](https://docs.typesafe.ai/cookbooks/parallel_questions) `📚23` — Cookbook: 13 questions over the GDPR Wikipedia article; TypeSafe reports one batched call is 12.2x cheaper and 10.0x faster than 13 single calls.
- [docs index](https://docs.typesafe.ai/llms.txt) `📚22` — TypeSafe documentation — Live docs for the System One model, primitives, API, cookbooks, and demos. Maintained by TypeSafe AI.
- [Playground](https://console.typesafe.ai/playground) `📚20` — Open the TypeSafe Playground, sign in, paste some text as the state, and add a Noul question:
- [Patterns](https://docs.typesafe.ai/patterns) `📚19` — Index of four architecture patterns: speculative fan-out, confidence-gated routing, composite scoring, and intent routing.
- [Agent skill](https://docs.typesafe.ai/agent-skill) `📚18` — Teaches Claude Code, Codex, and other coding agents to design TypeSafe workflows from the live docs.
- [Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check) `📚18` — Official citation-check cookbook — Checks whether a quote's context supports a claim. Maintained by TypeSafe AI.
- [Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) `📚17` — Runs four Nouls per retrieved passage to drop prompt injections and off-topic text and to flag passages that contradict the question.
- [Demo: Smart home assistant](https://docs.typesafe.ai/demos/smart-home) `📚17` — Smart home assistant demo — Official demo that evaluates smart-home requests with speculative questions and an LLM fallback. Maintained by TypeSafe AI.
- [Function calling](https://docs.typesafe.ai/cookbooks/function_calling) `📚17` — Official function-calling cookbook — Maps a natural-language trading request onto typed functions and closed-set arguments. Maintained by TypeSafe AI.
- [How to build with System One](https://docs.typesafe.ai/concepts/how-to-build-with-system-one) `📚17` — (confidence)(projects/421-confidence.md) — README.md:421 — See also: How to build with System One, the (use-case map)(
- [Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion) `📚17` — Official skill-suggestion cookbook — Two Jev requests rank 182 Hermes skills and may suggest none. Maintained by TypeSafe AI.
- [TypeSafe use-case map](https://docs.typesafe.ai/concepts/use-case-map) `📚17` — This playbook turns the ideas in the TypeSafe use-case map, primitives guide, and patterns guide into implementation shapes you can adapt.
- [Console](https://console.typesafe.ai) `📚16` — It uses TYPESAFE_API_KEY with --provider typesafe and the TypeSafe console. No OpenRouter account needed.
- [Cookbook: Guardrails for LLMs](https://docs.typesafe.ai/cookbooks/llm_guardrails) `📚16` — Official LLM guardrails cookbook — Screens an LLM input or output for hazards, then code chooses pass, review, block, or support. Maintained by TypeSafe AI.
- [Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook) `📚16` — . Asks Jev for the parts of a date named in a document, then resolves and validates them in code.
- [Python SDK](https://docs.typesafe.ai/sdk/python) `📚16` — Run pip install typesafe-sdk for typed sync or async calls; the client reads TYPESAFE_API_KEY from the environment. Python SDK guide.
- [Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out) `📚16` — Evidence: TypeSafe’s support fan-out pattern and customer-support use cases.
- [Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) `📚15` — This is the single most important pattern in the ecosystem. See confidence-gated routing, and jevcal for fitting thresholds empirically.
- [Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification) `📚15` — Related: TypeSafe's hierarchical-classification cookbook shows a different beam-search design for trees, using geometric-mean path scoring.
- [Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe) `📚15` — Shortlist with BM25, then score query–passage pairs; the example uses legal retrieval. (Details)(catalog/DETAILS.md#official-rerank-typesafe)
- [Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring) `📚14` — Atomic scores from Jev, weights you own in code — visible, versioned, and editable without retraining anything.
- [Cookbook: Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment) `📚14` — nowledge graph entity alignment - Map candidate record pairs to merge, separate, or curator-review outcomes.
- [Cookbook: Self-consistency with choices](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook) `📚14` — Choice self-consistency cookbook (TypeSafe docs) - 8 Choice questions on one ambiguous post, seven conditions: 99.2% agreement at a 0.60 threshold, flips on 2 of 8.
- [Intent routing](https://docs.typesafe.ai/patterns/intent-routing) `📚14` — Official intent-routing pattern — Classifies a request, then code routes to deterministic logic, a specialist LLM, or a human. Maintained by TypeSafe AI.
- [Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find) `📚14` — Ranks 218 lines of a terms-of-service document with a single Choice and uses a Noul to say when the document has no answer.
- [Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook) `📚14` — . Regexes find candidate emails, phone numbers, and amounts, then Jev selects the requested span so code can normalize it.
- [Autoresearch feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery) `📚13` — Autoresearch feature discovery - Propose TypeSafe questions as numeric features for a supervised model.
- [Cookbook: Classification using confidence](https://docs.typesafe.ai/cookbooks/classification_using_confidence) `📚13` — This is a clean example of confidence as a second axis rather than a filter. Source: classification using confidence cookbook
- [Manifesto](https://typesafe.ai/manifesto) `📚13` — TypeSafe's argument for AI-powered software where code, not an agent loop, owns the workflow.
- [Noul](https://docs.typesafe.ai/primitives/noul) `📚13` — Silencio Noul Silencio Estimar si una declaración es verdadera Silencioso Probabilidad de 0 a 1
- [SDE cascade](https://docs.typesafe.ai/cookbooks/sde_cascade) `📚13` — Extract with a small model, verify fields with Jev, and escalate when needed. (Details)(catalog/DETAILS.md#official-sde-cascade)
- [System One](https://docs.typesafe.ai/concepts/system-one) `📚13` — TypeSafe docs) - The concept and interface as defined by the model's authors.
- [API keys](https://console.typesafe.ai/settings/keys) `📚12` — Rules (Jev) — paste a typesafe.ai key, edit your group rules (label
- [Cookbook: Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat) `📚12` — Classify wrapped lines, headings, lists, and code blocks so code can rebuild Markdown. (Details)(catalog/DETAILS.md#official-autoformat)
- [Score](https://docs.typesafe.ai/primitives/score) `📚12` — Score rates the state against ordered descriptive levels and returns a score, a probability per level, and a confidence value.
- [Self-consistency: nouls](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook) `📚12` — Noul self-consistency - Inspect repeated answers and see how a review interval changes automatic-decision coverage.
- [typesafe-ai/daggerverse](https://github.com/typesafe-ai/daggerverse) `★22 · 📚11` — Collection of useful Dagger modules.
- [Choice](https://docs.typesafe.ai/primitives/choice) `📚11` — Jev 1.13 jaggedness; no claim that the API automatically switches to a two-stage selection
- [JavaScript SDK](https://docs.typesafe.ai/sdk/javascript) `📚10` — (JavaScript / TypeScript SDK)(projects/218-javascript-typescript-sdk.md) — README.md:218 — npm install @typesafe-ai/sdk. Docs.
- [State](https://docs.typesafe.ai/concepts/state) `📚10` — What state is, how to structure it (string, JSON object or array), and how to give the model the context a question needs.

## Established (cited by 5–9 lists) — 5

- [AI: too good to be true, too bad to be useful](https://typesafe.ai/blog/ai-too-good-to-be-true-too-bad-to-be-useful-typesafe-ai) `📚7` — AI: too good to be true, too bad to be useful - Against preference-optimized chat models for automation.
- [The Bitterest Lesson](https://typesafe.ai/blog/bitterest-lesson) `📚7` — The Bitterest Lesson - Why optimizing the wrong task can dominate gains from scale.
- [AI primer](https://docs.typesafe.ai/introduction/machine-learning-primer) `📚5` — Why Jev is trained with reinforcement learning for calibrated decisions (RLCD) rather than for pleasing text.
- [console cookbooks](https://console.typesafe.ai/docs/cookbooks) `📚5` — (docs index)(projects/425-docs-index.md) — README.md:425 — Official, copy-pasteable workflows. Full index: console cookbooks and the (docs index)(
- [TypeSafe console](https://console.typesafe.ai/keys) `📚5` — Create an API key in the TypeSafe Console, then keep it in an environment variable:

## Emerging (cited by 3–4 lists) — 19

- [Claim verification](https://docs.typesafe.ai/cookbooks/citation_check.md) `📚4` — Review: Official document reviewed. Source checked · 2026-09-19 · Not reproduced.
- [Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat.md) `📚4` — Review: Official document reviewed. Source checked · 2026-09-19 · Not reproduced.
- [Advanced: structure](https://docs.typesafe.ai/primitives/advanced) `📚3` — Advanced structure - Using JSON in instructions and criteria for definitions, contrasts, exclusions, and examples.
- [Confidence](https://docs.typesafe.ai/confidence.md) `📚3` — TypeSafe Confidence — official_domain, official_status, strong_signal
- [Cookbooks](https://docs.typesafe.ai/cookbooks) `📚3` — TypeSafe Official Cookbooks — Worked examples for RAG classification, citation double-checking, and parallel evaluation.
- [extraction cascades](https://docs.typesafe.ai/cookbooks/sde_cascade.md) `📚3` — Review: Official document reviewed. Source checked · 2026-09-19 · Not reproduced.
- [feature discovery](https://docs.typesafe.ai/cookbooks/autoresearch_feature_discovery.md) `📚3` — Autoresearch feature discovery：Runs an autoresearch loop that proposes TypeSafe questions, converts free text into numeric features, and uses model errors to improve a supervised CatBoost regressor.
- [function calling](https://docs.typesafe.ai/cookbooks/function_calling.md) `📚3` — Function calling：Turns natural-language trading requests into calls to ordinary typed functions by mapping function names and closed-set arguments to confidence-aware TypeSafe questions.
- [hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification.md) `📚3` — Hierarchical classification：Classifies documents through deep patent, retail product, biomedical, and source-code hierarchies using parallel beam search over TypeSafe Choice probabilities.
- [Interactive demos](https://docs.typesafe.ai/demos) `📚3` — Official hands-on examples, including the smart-home assistant.
- [parallel-questions cookbook](https://docs.typesafe.ai/cookbooks/parallel_questions.md) `📚3` — Parallel questions：Runs a 13-question regulatory briefing over the GDPR Wikipedia article, showing that batching every question into one TypeSafe call is 12.2x cheaper and 10.0x faster with no change in answers.
- [Primitives](https://docs.typesafe.ai/primitives.md) `📚3` — TypeSafe Primitives — official_domain, official_status, strong_signal
- [reranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe.md) `📚3` — Re-ranking：Builds 30-passage BM25 shortlists for 40 CLERC legal queries, then uses one TypeSafe question per query-candidate pair to raise top-1 accuracy from 5% to 18% and top-10 accuracy from 38% to 62%.
- [Score](https://docs.typesafe.ai/primitives/score.md) `📚3` — Probability-weighted position on ordered levels; use comparable per-item Scores for graded ranking
- [TypeSafe's terms](https://docs.typesafe.ai/legal) `📚3` — The library sends fitted message text, tool inputs, and result metadata to TypeSafe on live calls. Omitting result bodies does not redact secrets from other fields. It returns data in memory without writing a transcript…
- [typesafe-ai/n8n-nodes-typesafe-ai](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai) `📚3` — TypeSafe AI n8n node — Uses Jev to evaluate workflow items or route them to n8n outputs using typed answers and confidence thresholds. Maintained by TypeSafe.
- [typesafe-ai/typesafe-ai.github.io](https://github.com/typesafe-ai/typesafe-ai.github.io) `📚3` — typesafe-ai in:name,description created:2024-0
- [typesafe-ai/WorkflowEvals](https://github.com/typesafe-ai/workflowevals) `📚3` — WorkflowEvals — evals.typesafe.ai workflow code published _(★9, Python)_
- [value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook.md) `📚3` — Pre-parsed value extraction：Uses regexes to find candidate emails, phone numbers, and amounts, then has TypeSafe select the requested span so code can normalize a verbatim value.

## Long tail (cited by 1–2 lists) — 52

<details><summary>Show 52 long-tail entries</summary>

- [Agent Trace Observability workflow](https://evals.typesafe.ai/agent_trace_observability) `📚2`
- [API documentation](https://docs.typesafe.ai/api.md) `📚2` — HTTP API, Python SDK, or JavaScript SDK
- [Choice](https://docs.typesafe.ai/primitives/choice.md) `📚2` — Jev answers typed questions — Choice, Noul and Score — with calibrated probabilities instead of prose, so ordinary code keeps control of the workflow. This…
- [composite scoring](https://docs.typesafe.ai/patterns/composite-scoring.md) `📚2` — Review: Official document reviewed. Source checked · 2026-09-19 · Not reproduced.
- [Customer Service workflow](https://evals.typesafe.ai/customer_service) `📚2`
- [Noul](https://docs.typesafe.ai/primitives/noul.md) `📚2` — Probability of yes; no separate confidence; use one per label when several may apply
- [Python changelog](https://docs.typesafe.ai/sdk/python/changelog) `📚2` — September 21 update: earlier API key validation, no key value in exception logs, and additional gateway examples
- [Security Incidents workflow](https://evals.typesafe.ai/security_incidents) `📚2` — eval · TypeSafe AI · DocsOfficial workflow eval for deciding whether a security alert is closed, escalated or contained; Jev scores 61.7% at $0.0001 and 0.3 s…
- [speculative fan-out](https://docs.typesafe.ai/patterns/fan-out.md) `📚2` — Review: Official document reviewed. Source checked · 2026-09-19 · Not reproduced.
- [TypeSafe Python SDK](https://docs.typesafe.ai/sdk/python.md) `📚2`
- [typesafe-ai/skills（⭐128](https://github.com/typesafe-ai/skills（⭐128) `📚2`
- [核验来源](https://docs.typesafe.ai/patterns/confidence-routing.md) `📚2` — Review: Official document reviewed. Source checked · 2026-09-19 · Not reproduced.
- [核验来源](https://docs.typesafe.ai/patterns/intent-routing.md) `📚2` — Review: Official title, introduction, and index reviewed; incomplete body. Source checked · 2026-09-19 · Not reproduced.
- [核验来源](https://docs.typesafe.ai/demos/smart-home.md) `📚2` — Review: Official document reviewed. Source checked · 2026-09-19 · Not reproduced.
- [核验来源](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook.md) `📚2` — Review: Official title, introduction, and index reviewed; incomplete body. Source checked · 2026-09-19 · Not reproduced.
- [核验来源](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook.md) `📚2` — Self-consistency: choices：Add an uncertain outcome to moderation decisions and compare label agreement with the share of automatic actions.
- [核验来源](https://docs.typesafe.ai/cookbooks/semantic_find.md) `📚2` — Review: Official document reviewed. Source checked · 2026-09-19 · Not reproduced.
- [核验来源](https://docs.typesafe.ai/cookbooks/skill_suggestion.md) `📚2` — Skill suggestion：Picks at most one skill for an agent turn out of the 182 in Nous Research's Hermes catalog, using two TypeSafe requests to rank and re-check…
- [核验来源](https://docs.typesafe.ai/cookbooks/entity_alignment.md) `📚2` — Review: Official document reviewed. Source checked · 2026-09-19 · Not reproduced.
- [核验来源](https://docs.typesafe.ai/cookbooks/classifying_rag_passages.md) `📚2` — Classifying RAG passages：Score each retrieved passage with one TypeSafe request, then decide in code which ones reach the answering model.
- [核验来源](https://docs.typesafe.ai/cookbooks/llm_guardrails.md) `📚2` — Guardrails for LLMs：Screen every message going into and out of an LLM app with one TypeSafe request, thresholding hazard probabilities and severity to pass,…
- [核验来源](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook.md) `📚2` — Date extraction：Extracts absolute and relative dates by asking TypeSafe for the parts named in a document, then resolving and validating them in code with…
- [核验来源](https://docs.typesafe.ai/cookbooks/classification_using_confidence.md) `📚2` — Review: Official document reviewed. Source checked · 2026-09-19 · Not reproduced.
- [模型能力局限](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md) `📚2` — The Jev 1.13 limitations document describes version-specific behavior. Consult the documentation for the version you use.
- [allows two retries by default](https://docs.typesafe.ai/sdk/python/api/retries) `📚1` — The library propagates navigation failures. The app displays them and clears the failed result. Caption inference has a local heuristic fallback. The SDK…
- [ayshrosine/Jev_Typesafe.Ai](https://github.com/ayshrosine/jev_typesafe.ai) `📚1` — typesafe-ai in:name,description created:2026-0
- [Ceciile/jev-use-cases-typefast,0,,,2026-09-23,typesafe.ai](https://github.com/ceciile/jev-use-cases-typefast,0,,,2026-09-23,typesafe.ai) `📚1`
- [connection errors and timeouts](https://docs.typesafe.ai/sdk/python/api/exceptions) `📚1` — The article's code sends a low-confidence lane to human, an urgent ignore/log contradiction to human, and a draft with missing evidence to human. It does not…
- [current SDK reference](https://docs.typesafe.ai/sdk/python/api/clients/sync) `📚1` — The locked Python typesafe-sdk==0.6.0 retry/model defaults were checked against installed source and the current SDK reference. Browser setup and live commands…
- [FoundeReview: "The model that won't write" (2026-09-17)](https://foundereview.com/r/typesafe.ai/chokt310055) `📚1` — Evidence-only review from outside the waitlist (no API key issued): Every's 777 judgments in <0.7s survived contact; Dan Shipper's writing checks — Jev 0.35s…
- [how to build with TypeSafe](https://docs.typesafe.ai/concepts/how-to-build-with-system-one.md) `📚1`
- [Invoice Processing workflow](https://evals.typesafe.ai/invoice_processing) `📚1`
- [JavaScript changelog](https://docs.typesafe.ai/sdk/javascript/changelog) `📚1`
- [JavaScript SDK](https://docs.typesafe.ai/sdk/javascript.md) `📚1`
- [kyledickey/jev-go,1,Go,TypeSafe.ai](https://github.com/kyledickey/jev-go,1,go,typesafe.ai) `📚1`
- [Launch blog post](https://typesafe.ai/blog) `📚1` — "Decisions, not strings" (Sept 2026)
- [Migration guide](https://docs.typesafe.ai/migrating-to-v1.md) `📚1` — and the installed SDK's current reference
- [Models](https://docs.typesafe.ai/models.md) `📚1` — . Rate limits and aliases move; gateway IDs differ — Limits adjust dynamically; pin versioned model IDs for tuned thresholds. Re-check each gateway’s model id…
- [Official cookbooks](https://docs.typesafe.ai/cookbooks.md) `📚1`
- [Official demos](https://docs.typesafe.ai/demos.md) `📚1` — TypeSafe’s demonstrations.
- [official TypeSafe SDK](https://docs.typesafe.ai/sdk) `📚1`
- [site](https://daggerverse.docs.typesafe.ai) `📚1`
- [State](https://docs.typesafe.ai/concepts/state.md) `📚1` — primitives, then the chosen primitive's page
- [System One](https://docs.typesafe.ai/concepts/system-one.md) `📚1` — Understand the programming model
- [The SDK reference](https://docs.typesafe.ai/sdk/python/usage) `📚1` — Read response.choices("owner").choice and .confidence, response.nouls("reply_today").noul, and response.scores("tone").score. The SDK reference shows these…
- [TypeSafe 新增 Team 页 + 导航新增 `Enterprise` 入口（产品化/商业化信号）](https://typesafe.ai/team) `📚1`
- [typesafe-ai/typesafe-aihub.io](https://github.com/typesafe-ai/typesafe-aihub.io) `📚1`
- [typesafe.ai/Jev](https://typesafe.ai/jev) `📚1` — Product page for Jev.
- [Use-case map](https://docs.typesafe.ai/concepts/use-case-map.md) `📚1` — then relevant cookbooks from the index
- [官方状态页](https://status.typesafe.ai) `📚1` — . If the Console or API has an incident, check the official status page. That is a separate issue from waitlist access.
- [核验来源](https://docs.typesafe.ai/introduction/quickstart.md) `📚1` — Review: Official document reviewed. Source checked · 2026-09-19 · Not reproduced.
- [补齐官方缺失页：迁移到 v1 API](https://docs.typesafe.ai/migrating-to-v1) `📚1` — official / media-discussions — ⭐0

</details>
