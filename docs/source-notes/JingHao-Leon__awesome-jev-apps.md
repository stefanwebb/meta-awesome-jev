# JingHao-Leon/awesome-jev-apps
- **One-liner:** Chinese-language, quality-first list of 122 Jev apps, SDKs, platform integrations, open replicas, tutorials and discussions, with specs, quickstart and FAQ.
- **Language(s):** Chinese (English summary line only)
- **Type:** curated-list
- **Scale:** 122 entries: quality open-source apps 51 (Agents & automation, Trading & finance, Developer tools, Eval & guardrails, Fun & experiments, Web demos), SDKs & integrations 28 (Official, Platform-official integrations, Community language SDKs, MCP & agent tooling, Open replicas & local alternatives), Official resources 6, Tutorials & evaluations 30, Community discussion 7. Mirrored in data/projects.json with scripts/check.py CI; CHANGELOG with dated "ecosystem snapshots" (v0.12.0, 2026-10-01).
- **Quality flags:** Hand-curated, careful caveats ("官方声称" labels, inclusion ≠ endorsement, warns other same-name awesome-jev repos are "搬运聚合号" / scraper-aggregators). Snapshot date 2026-10-01 is one day after today's date — slightly odd. Star counts much higher than other lists (laya 29.1k★ vs 17.7k in heyjunpenn / 19,984 in Promethe-us; jev-ultrafast 21.5k★) — could be growth or inflation; treat stars as unreliable.
- **Unique value:** Best Chinese-language entry point; strong curated tutorial/eval list with HN point counts; tracks ecosystem milestones (OpenAI Decision API on Luna, Ollama 0.35 support for Jev-style models, langchain-typesafe, @ai-sdk/typesafe-ai, @tanstack/ai-typesafe, MotherDuck prompt_jev()).

## Facts claimed about Jev
- Released **2026-09-15** by TypeSafe AI; "first System One decision model"; badge shows **jev-1.13.0**; default model `jev-latest`.
- Primitives: **choice (≤255 options)**, **score (2–10 level scale)**, **noul (0–1 probability)** — the 2–10 levels detail is unique to this list.
- Latency 70–500 ms (vs LLM 3–329 s); **$0.042/M input tokens, output free** (LLM output ~5× input price).
- Official claim 193.6× faster, 444.6× cheaper (self-built workflow evals).
- Founder Diogo Almeida, ex-OpenAI, "RLHF / InstructGPT co-inventor"; **$40M seed led by DCVC**.
- Limits: no arithmetic/counting/date comparison, no text generation, no image/audio; "zero hallucination" = cannot return out-of-schema values; state can be adversarially manipulated; calibration may fail under distribution shift.
- docs.typesafe.ai has **105 pages, 18 official cookbooks**, Patterns library, llms.txt.
- HN launch thread **1,931 points / 509 comments** (item 49717558).
- Integrations: `langchain-typesafe` (PyPI; `TypeSafeClassifier` + model-routing middleware); `@ai-sdk/typesafe-ai` Vercel AI SDK provider, Gateway ID **`typesafe-ai/jev-latest`** (note: others say `typesafe-ai/jev`); Vercel calls it the fastest-adopted model in AI Gateway history; `@tanstack/ai-typesafe` `typesafeDecider` with decide/choice/score/boolean; MotherDuck `prompt_jev()`; community SDKs .NET (NuGet `TypeSafe.AI.Sdk`), Elixir (Hex `typesafe_sdk`), Rust, Go, Java, Ruby, Swift (swift-newt on Apple Core AI); MCP: itsmostafa/typesafe-mcp, npm `jevcore-mcp`.
- Ecosystem: OpenAI Decision API built on Luna (The New Stack); Ollama 0.35 natively runs Jev-style decision models (e.g. nimble); firelex/jeff 0.8B, 22 ms RTX / 28 ms M4 Max (546 HN points); ollaya (Rust, "Ollama for decision models", 530 HN points).
- Benchmarks cited: tessl verifiers — Jev **13.6× faster, 2.7× cheaper than GPT Luna 6**; r6i — 7× faster than agentic classification loop; casco — all decision models (incl. Jev) inflate security-finding (CVSS) severity; jev-ultrafast Google Flights demo 7.1 s.
- Latent Space podcast 2h21m (2026-09-21).

## Key insights / patterns
- Selection guide: Jev for low-latency classification/routing/scoring/yes-no; generative LLM for writing/open dialogue/multi-turn reasoning; open replicas (laya, kev, NanoJev, von) when data can't leave premises / offline / extreme budget — trading some accuracy.
- Local/dev options: self-host replicas; official system-one-adapter-python emulates the interface with any LLM; Open Jev Playground (beam.cloud).
- Mental model: "a smart if-statement with probabilities" rather than an all-knowing assistant; route low-confidence to humans.
- Negative result worth noting: severity inflation on security findings across all decision models.
- "The State Machine Is the Agent" and "Jev in practice: typed decisions, scoped authority" frame Jev inside deterministic state machines with scoped permissions.

## Standout entries
- [Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post (official)
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — official limitations (official)
- [langchain-typesafe](https://pypi.org/project/langchain-typesafe/) — LangChain integration (integration)
- [@ai-sdk/typesafe-ai evaluation docs](https://ai-sdk.dev/docs/ai-sdk-core/evaluation) — Vercel AI SDK provider (integration)
- [MotherDuck prompt_jev()](https://motherduck.com/blog/motherduck-supports-jev/) — Jev in SQL (integration)
- [Ollama 0.35 Jev-style decision models](https://ollama.com/blog/ollama-now-supports-jev-style-decision-models) — local runtime support (ecosystem)
- [OpenAI Decision API on Luna (The New Stack)](https://thenewstack.io/openai-decision-api-luna/) — competitor response (news)
- [How to Use Jev: A Practical Guide (Dev.to)](https://dev.to/valyuai/how-to-use-jev-a-practical-guide-to-typesafes-system-one-model-g5e) — comprehensive practical guide (tutorial)
- [What Actually Shipped (TrueFoundry)](https://www.truefoundry.com/blog/typesafe-ai-jev) — critical claims-vs-verifiable analysis (critique)
- [Jev in 25 Lines of Python](https://www.nobodywho.ai/posts/jev-in-25-lines/) — minimal re-implementation explainer (tutorial)
- [tessl: 13.6× faster, 2.7× cheaper than GPT Luna 6](https://tessl.io/blog/jev-is-136x-faster-and-27x-cheaper-than-gpt-luna-6-for-tessl-verifiers-try-it-yourself) — production verifier benchmark (benchmark)
- [Jev in production vs a cross-encoder](https://getunblocked.com/blog/jev-in-production-vs-cross-encoder/) — production reranking comparison (benchmark)
- [casco CVSS benchmark](https://casco.com/blog/jev-cvss-benchmark) — severity inflation negative result (security)
- [From Bag-of-Words to Jev (Sebastian Raschka)](https://magazine.sebastianraschka.com/p/classifier-history-and-jev) — history of text classification (article)
- [Jev 工程学中文翻译 (yibie)](https://github.com/yibie/jev-engineering-zh) — Chinese translation of Diogo Almeida's design notes (translation)
