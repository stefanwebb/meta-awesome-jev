# RadRebelSam/awesome-jev
- **One-liner:** Daily-crawled, Jev-triaged directory of Jev repos (claims ~3,000 entries) with star counts, trending section, coverage checks against 14 rival directories, and a website.
- **Language(s):** English
- **Type:** auto-generated-list
- **Scale:** Footer says "2998 entries" (README renders ~940 visible entries) + 432 candidates in review queue (2026-09-30). Categories: Moving fastest this week; Official; SDKs and clients; Framework integrations; Evaluation and judging; Guardrails and safety; Infrastructure and tooling; Examples and templates; Reading and explainers; Everything else; Other lists and directories. Site: awesomejev.radrebeldeveloper.com.
- **Quality flags:** Auto-generated from GitHub search/npm/other directories; descriptions are GitHub repo descriptions (some "No description provided"); categorization is loose (e.g. repos in "Reading and explainers", a Feishu mail tool under "Other lists"). Many 0–5 star experiments. Metadata (stars, license, push date) refreshed daily — fresh but not editorially reviewed beyond Jev membership check. Human merge claimed.
- **Unique value:** Transparent pipeline where **Jev itself curates** (membership Noul thresholds 0.75 accept / 0.45 reject); weekly star-velocity trends; coverage.json proving cross-directory completeness; lists news coverage (TechCrunch, The Register, DataCamp, LangChain blog); documents Vercel AI Gateway endpoint for Jev; explicit exclusion of "Japanese encephalitis virus" name collision.

## Facts claimed about Jev
- Jev is "not a chatbot and not a coding model": application state + typed questions → one typed answer per question (yes/no probability, one option, or position on a defined scale); no free text, which TypeSafe says means it can't hallucinate or produce a type error.
- Vendor claims: inference **40–200x faster** than frontier LLMs on comparable classification work; **$0.042 per million input tokens, output billed at zero**.
- Vercel AI Gateway serves Jev at `https://ai-gateway.vercel.sh/typesafe/v1/systemone` using TypeSafe's own request shapes (env `AI_GATEWAY_API_KEY`); refuses requests until the Vercel team has a card on file. Direct API env `TYPESAFE_API_KEY`.
- Official repos (star counts as of ~2026-09-30): typesafe-ai/skills (2469★, MIT), typesafe-sdk-js (258★), typesafe-sdk-python (255★), WorkflowEvals (9★, Apache-2.0, "evals.typesafe.ai workflow code"), **n8n-nodes-typesafe-ai** (2★, official n8n node).
- Press: TechCrunch 2026-09-18 "A new kind of AI model from a ChatGPT inventor…" (seed round, early adopters); The Register 2026-09-16 "TypeSafe AI debuts model for machines that plays Doom" (sceptical of perf claims); DataCamp explainer; LangChain "Building a harness with Jev".
- Community claims: JevRanker "22x faster per match than a generative listwise LLM"; openjev (razorback16) Jev-compatible server on DiffusionGemma; jeff = self-hosted drop-in powered by GliFormer.
- Trending (7-day stars): jev-chat-JARVIS +1533, dzhng/jevgrep +1457 (1856★ total), Mapika/decider +635, fast-jev-compaction +561, AnyJev +526.

## Key insights / patterns
- Using Jev as a curation classifier: single Noul "does this repo's own code call, wrap, benchmark or reimplement Jev, or merely mention it"; three-band thresholds with human queue in between. Membership probability ≠ quality.
- Pre-filter name collisions ("jev" = Japanese encephalitis virus) before model triage.
- Gateway fallback: if Vercel gateway refuses (no card), fall back to direct TypeSafe API.
- Ecosystem shape: many open re-creations (reflex on Qwen3.5, rizzo-flow, OpenJev, openjev, jeff, system-one-270m on gemma-3-270m), voice-control Mac apps, code-search CLIs (jevgrep), RAG rerankers.

## Standout entries
- [TypeSafe AI - Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post (official)
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) — official agent skills (official)
- [typesafe-ai/WorkflowEvals](https://github.com/typesafe-ai/WorkflowEvals) — eval workflow code (official benchmark)
- [typesafe-ai/n8n-nodes-typesafe-ai](https://github.com/typesafe-ai/n8n-nodes-typesafe-ai) — official n8n node (official integration)
- [LangChain - Building a harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev) — agent harness walkthrough (tutorial)
- [DataCamp - Jev: TypeSafe's System One model](https://www.datacamp.com/blog/system-one-models-jev) — explainer (article)
- [TechCrunch launch coverage](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/) — press (article)
- [The Register - TypeSafe AI debuts model for machines that plays Doom](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711) — sceptical press (article)
- [dzhng/jevgrep](https://github.com/dzhng/jevgrep) — code search CLI for agents (tool)
- [razorback16/openjev](https://github.com/razorback16/openjev) — open Jev-compatible server on DiffusionGemma (open model)
- [logan-markewich/jeff](https://github.com/logan-markewich/jeff) — self-hosted drop-in replacement (open model)
- [kshetrajna12/reflex](https://github.com/kshetrajna12/reflex) — small open decision model on Qwen3.5 (open model)
- [hgqimo/JevRanker](https://github.com/hgqimo/JevRanker) — RAG reranker with BlitzRank (tool)
- [awesomejev.com](https://awesomejev.com/) — directory site (directory)
- [jevmade.com](https://jevmade.com/) — directory site (directory)
