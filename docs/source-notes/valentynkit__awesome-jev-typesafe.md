# valentynkit/awesome-jev-typesafe
- **One-liner:** Hand-curated, link-checked awesome list (406 entries) of Jev projects, official docs and independent evaluations. The same list is published as a searchable site, an agent skill and projects.json.
- **Language(s):** English source; generated zh-CN, ja, ko READMEs
- **Type:** curated-list
- **Scale:** 406 entries. Sections: Jev on one screen · Know before you build · Start here (official docs/gateways) · Official SDKs and framework support · Coding agents (Claude Code, Codex, Pi, Hermes, Agent Zero, Any agent, Skills for writing Jev code) · Browser and computer use · Open models and replicas · Code review and quality · Routing and gateways · Search, reranking and RAG · Data and ops · Safety, moderation and verification · Applications and extensions · Games, robotics and simulation · Finance and trading · Benchmarks, evals and calibration · Playgrounds and demos · Command line · Community clients · Articles and talks (Launch coverage / Independent measurements / Essays and threads).
- **Quality flags:** High quality. Every entry is human-read, links are checked weekly in CI, "same-day scaffold" repos are flagged, and vendor facts are dated ("copied 2026-09-18, rechecked 2026-09-19"). Candid caveats. Its metadata is auto-tagged with Jev itself (scripts/tag-jev.mjs asks Noul/Choice/Score questions per project, including "looks_templated" and "calls_jev_for_real"). No obvious fabrication.
- **Unique value:** The best "Start here" block of official URLs in this batch, including docs pages, gateways (Vercel, Cloudflare, OpenRouter, Netlify, LiteLLM) and model IDs. An honest "Know before you build" caveats list. About 28 annotated benchmark/eval repos with numbers. Curated independent-measurement articles. An agent skill (SKILL.md) plus projects.json/llms.txt/llms-full.txt for machine consumption. A working minimal JS client with 429/529 backoff.

## Facts claimed about Jev
- "The first System One model". Endpoint `POST https://api.typesafe.ai/v1/systemone` with `model`, `state` and a map of `questions`. Auth is `Authorization: Bearer $TYPESAFE_API_KEY`. The client retries on HTTP 429 and **529**.
- Alias `jev-latest`, currently `jev-1.13.0`.
- `Choice`: up to 255 options. `Score`: places state on a described scale. `Noul`: calibrated yes/no probability. All questions are scored in parallel against the same state. Question JSON (from the scripts): `{type:"noul"|"choice"|"score", instructions, criteria}`. Answers are read as `answers[key].noul`.
- Input is text or JSON state only (no images/audio/video yet).
- **Price: $0.042 per million input tokens; output free.**
- Limits: 250,000 tokens/s, 1,200 req/min, **32k tokens per request** (early access). Contrast wh000wh000's reading of the docs: 64k per request, with state plus the longest question ≤32k.
- Latency is "70 to 500 ms end to end, vendor reported". The intro also says "about 100 ms".
- Training uses RLCD, "reinforcement learning for calibrated decisions". Weights and architecture are unpublished.
- Gateways: Vercel AI Gateway (model id `typesafe-ai/jev`), Cloudflare Workers AI (`typesafe/jev` via `env.AI.run`), OpenRouter beta (`typesafe/jev-1.13`), Netlify AI Gateway, and LiteLLM pass-through ("no streaming, since TypeSafe has none"). The gateways don't require the TypeSafe waitlist.
- Access is by waitlist via console.typesafe.ai. There is an official Discord at discord.gg/typesafe.
- Vercel AI SDK provider `@ai-sdk/typesafe-ai` exposes Jev via `experimental_evaluate`. vercel/eve uses Jev as its typed judge, and vercel-labs/ai-cli has an evaluate path on Jev.
- On the vendor's four-workflow eval (evals.typesafe.ai), "Jev lands around 68 percent, close to mid-tier LLMs".
- Founder is Diogo Almeida (X @CompleteSkeptic), described as a "ChatGPT inventor"/co-inventor. The company raised a $40M seed. TechCrunch reported demand briefly took the API down. The Doom demo was part of the launch.
- Manifesto thesis: "build prod, not god".
- Third-party numbers: jev-harness (Claude CLI 48.9 s vs Jev 1.3 s on a row-filter job); 4esv/jev-eval vs GPT-5.6 Terra (equal on easy tasks, 6.7 pts lower on 77-way routing, 5× faster, 41–50× cheaper); Pinecone cultivar (Jev grader ~30× cheaper than the LLM grader); Every's 1,709 judgments for under a cent; primeline (~9,750 calls, pre-registered); amankumar.ai (16,000 calls).

## Key insights / patterns
- "Type safe is not the same as correct." "Cannot hallucinate" only means no out-of-schema output.
- Jev can't count, do arithmetic, reason about dates, or output values not in your list. "Ask it to pick from a deck, never to name a card."
- Accuracy drops as irrelevant content fills the state, so curating state is most of the work.
- Keep irreversible actions behind a threshold and a human. Read the jaggedness page before picking thresholds.
- Official patterns: speculative fan-out, confidence routing, composite scoring, intent routing. Decompose into atomic questions and keep control flow in code.
- Jev-verified cascade (OpenRouter cookbook): a cheap model answers, Jev checks, and only failures escalate.
- Batching many questions into one request is the first cookbook.
- jev-orderby-bench: ORDER BY on Jev probability passes on 20 Newsgroups but fails 4 of 6 conditions on Amazon ESCI. Batched state shows position effects.
- themsquared: every wrong answer came with hedged confidence, which supports routing on confidence.
- Replica technique: read option logits instead of generating JSON (jevlike, mini-jev, SemIf). Archer Hume's 10,000-call probe reconstructed a shared-state parallel-branch architecture, and kev is built from it.
- Prior-art debate on HN: logit-reading isn't new, but zero-shot generality is the difference.

## Standout entries
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post: architecture, RLCD, pricing (official)
- [Model jaggedness: jev-1.13](https://docs.typesafe.ai/model-jaggedness/jev-1.13) — vendor's known failure modes (official docs)
- [Patterns](https://docs.typesafe.ai/patterns) — fan-out, confidence routing, composite scoring (official docs)
- [Workflow evals](https://evals.typesafe.ai/) — vendor benchmark on four workflows (benchmark)
- [llms.txt](https://docs.typesafe.ai/llms.txt) — all docs as Markdown (official)
- [Vercel AI SDK provider](https://ai-sdk.dev/providers/ai-sdk-providers/typesafe-ai) — `@ai-sdk/typesafe-ai` (SDK)
- [Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/) — gateway access (platform)
- [Jev-verified cascade](https://openrouter.ai/docs/cookbook/evaluate-and-optimize/jev-verified-cascade) — cheap-model + Jev check cascade (tutorial)
- [Jev's Architecture Unmasked](https://archerhume.com/posts/jevs-architecture-unmasked/) — 10,000-call architecture probe (research)
- [TypeSafe Jev vs Claude Code: pre-registered test](https://primeline.cc/blog/typesafe-jev-pre-registered-test) — ~9,750-call calibration study (evaluation)
- [Testing Jev on public and private data](https://amankumar.ai/blogs/jev-measured) — 16,000 calls and a threshold procedure (evaluation)
- [AbdelStark/jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks) — calibration/selective-risk eval harness (benchmark)
- [abhixhek/jevcal](https://github.com/abhixhek/jevcal) — threshold calibration and drift check (tool)
- [yodablocks/jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench) — is ranking by probability defensible (benchmark)
- [Jev, from a developer's angle](https://flaviocopes.com/jev/) — practical guide with code (tutorial)
