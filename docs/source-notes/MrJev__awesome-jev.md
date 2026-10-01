# MrJev/awesome-jev
- **One-liner:** A selective, code-verified Jev project list: 419 entries, each checked to actually call Jev, plus 10+ stars. It includes hands-on security reviews (mrjev.com) and a dated SDK/platform changelog.
- **Language(s):** English
- **Type:** curated-list
- **Scale:** 419 entries (last reviewed 2026-09-30). Sections: Trending (7-day star deltas) / Recent Developments / What We Found Running These / Running Without Jev / Official Resources / Community SDKs / Libraries & Integrations / Agent Integrations (MCP & Skills) / Coding Agents & Dev Tools / Guardrails & Safety / Model Routing / Command-Line Tools / Browser & Computer Use / Data & Observability / Search & Knowledge Graphs / Apps & Browser Extensions / Evaluation & Benchmarks / Open Models & Reproductions / Games & Real-Time Demos / Robotics & Embodied / Finance / Articles & Analysis / Related Lists (~30 other lists). Scripts handle discovery, trending, health and link checks.
- **Quality flags:** High quality with explicit written inclusion criteria. Numbers are marked author-reported. It promotes its companion site mrjev.com (143 reviews), which is promotional but substantive. Articles section is thin (5). There are no benchmark numbers inline.
- **Unique value:** (1) **Security and behaviour findings from actually running the tools in containers**: secrets leaked, /tmp exposure, ZDR not requested, a screenshot sent despite the README saying otherwise, weights missing the classification head. (2) **Dated official SDK changelog** with breaking changes. (3) A "Running Without Jev" table showing which tools accept a non-Jev endpoint. (4) Notes on weight licences for open replicas. (5) The broadest "Related Lists" index (~30).

## Facts claimed about Jev
- Official: launch post at typesafe.ai/blog/introducing-system-one-models-and-jev. Docs at docs.typesafe.ai/introduction. **Cookbooks** (docs.typesafe.ai/cookbooks/llm_guardrails: guardrails, re-ranking, RAG passage classification, citation checks). Patterns page. **Jev 1.13 jaggedness** page (docs.typesafe.ai/model-jaggedness/jev-1.13). Evals at evals.typesafe.ai. Vercel page vercel.com/ai-gateway/models/jev. The homepage is described as having an "early-access waitlist", which conflicts with other lists that say GA / no waitlist as of 09-21 (probably stale text).
- SDKs: `pip install typesafe-sdk` (github typesafe-ai/typesafe-sdk-python) and `npm install @typesafe-ai/sdk` (typesafe-ai/typesafe-sdk-js).
- Timeline:
  - **2026-09-15**: JS SDK 0.6.0. Breaking change: `Score` criteria became an ordered array.
  - **2026-09-16**: Vercel AI Gateway adds `typesafe-ai/jev` through AI SDK 7's experimental evaluate API, with zero-data-retention and no-training as provider options.
  - **2026-09-18**: Python SDK 0.7.0. Breaking change: Pydantic replaces msgspec, and `system_one()` gains `response_model`.
  - **2026-09-18**: OpenRouter lists `typesafe/jev-1.13` plus a latest alias, "at TypeSafe's own price".
- `TYPESAFE_BASE_URL` is the official SDK's env var for overriding the endpoint.
- It says there are "over a thousand Jev repositories on GitHub, and most of them only mention it."
- Trending (09-30 stars): NandhaKishorM/laya 28,721 (+11,489 in a week), browser-use/jev-ultrafast 21,430, jaredpalmer/kev 7,924, tamaratran/fast-jev-compaction 7,209.

## Key insights / patterns
- **Security findings from running tools**: pi-warden's redaction missed a password in a postgres:// URL. jev-router v0.3.0 left prompts in world-readable /tmp. jev-browser presses Enter on every typing step, which submits forms. abide promised ZDR but never requested it on the direct-key path. Jev-cu's policy gate matched a label truncated to 120 chars, so "delete" could be hidden. typesafe-computer-use sent a screenshot despite its README. Foreman exposed the Jev key to Codex's environment. `jeff check .` sent .pem keys and passwords. Von's published weights were missing their head, so it answered at random. Lesson: **audit what a Jev tool sends; many send code or screens to third parties.**
- Using OpenRouter or Vercel is **not an alternative model**, just the same paid model with an extra hop. Open replicas are the real alternative, but check the **weights' licence** separately from the code licence.
- Patterns in libraries: **option-order averaging** to remove position bias (pijev). **Recursive Choice over a taxonomy** for more than 255 options (jev-tree). **Decision caching keyed on (model, schema, state)** for deterministic CI replay (jevcache). Zod validates the shape while Jev validates the meaning (zod-jev). **Semantic if / feels?** DSLs in Ruby, BAML, Elixir and Effect. Leases on memory facts (invalidate).
- Guardrail design: gates that "escalate but never approve" (jev-gates). Jev "can only relax a refusal and never cause one" (Canny). Failure policy rejects `allow` at config time (dsh-jev). Shadow mode first (agent-chaperone, jev-harness).
- Evals: pick the confidence threshold from your own labelled data and fail CI when a model update breaks it (jevcal, jev-calibrate). Use GEPA to improve question wording from uncertain examples (jev-align). "Arithmetic in code; Jev only for the verdict" (PZ_Optimization).

## Standout entries
- [Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post (official)
- [Cookbooks](https://docs.typesafe.ai/cookbooks/llm_guardrails) — official recipes (official)
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — known weaknesses (official)
- [Evals](https://evals.typesafe.ai) — official evaluations (official)
- [Python SDK 0.7.0 release](https://github.com/typesafe-ai/typesafe-sdk-python/releases/tag/v0.7.0) — breaking change notes (SDK)
- [Vercel AI Gateway announcement](https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway) — platform availability (platform)
- [mrjev.com/best-jev-tools](https://mrjev.com/best-jev-tools/) — hands-on reviews, what each tool sends (reviews/security)
- [pijev](https://github.com/TypeLLM/pijev) — option-order averaging wrapper (library)
- [jevcal](https://github.com/abhixhek/jevcal) — threshold selection plus CI regression checks (eval tool)
- [openlayer-ai/jevals](https://github.com/openlayer-ai/jevals) — agent evals as typed questions (eval tool)
- [jev-align](https://github.com/sutro-sh/jev-align) — active labelling plus GEPA question optimisation (eval tool)
- [Spring AI TypeSafe](https://github.com/spring-ai-community/spring-ai-typesafe) — Java/Spring integration (SDK)
- [Jev Cookbook (Chinese, Datawhale)](https://github.com/datawhalechina/jev-cookbook) — course (tutorial)
- [Jev: The Language Model That Won't Talk](https://anthonymaio.substack.com/p/jev-the-language-model-that-wont) — critical analysis (article)
- [Ten Levels of Jev](https://github.com/disler/ten-levels-of-jev) — 30 worked uses in 10 levels (tutorial)
