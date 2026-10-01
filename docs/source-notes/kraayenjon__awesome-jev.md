# kraayenjon/awesome-jev
- **One-liner:** Comprehensive awesome list of Jev use cases, SDKs, official docs/cookbooks, benchmarks and open models, maintained by the madewithjev.com directory, with a "builds with real numbers" table.
- **Language(s):** English (one Spanish LinkedIn explainer linked)
- **Type:** curated-list
- **Scale:** ~339 links. Sections: What is Jev?, Jev vs LLM, Pricing/limits/access, Quick start, Official resources, Community, Featured builds with real numbers (30 rows), Jev guides by madewithjev.com, What people use Jev for by job, SDKs and clients, Applications (Browser/computer-use; Search/retrieval/data; Developer tools/code review; Model routing; Business/vertical; Robotics/hardware), Demos and games, Agent tools and MCP servers, Use cases by industry, Patterns, Cookbooks, Benchmarks and evaluations, Research and open models, Articles and coverage, Discussions, FAQ, More guides/integrations/lists, Related lists.
- **Quality flags:** Promotional toward the maintainer's own site madewithjev.com (featured-builds links route through it; a "guides by madewithjev.com" section; own Mac app "Sift"). Still high-quality hand-written content. Access info is stale (snapshot Sept 18: says waitlist required; others report waitlist removed Sept 20). Numbers are author-reported, labelled as such.
- **Unique value:** Clear official spec table, "Jev vs LLM" comparison from launch post, full official patterns + cookbooks index, a table of ~30 builds with cost/latency/throughput figures, a job-oriented use-case table, and a good benchmarks list including negative results (Haiku wins phishing; embeddings beat Jev alone on rerank).

## Facts claimed about Jev
- Launch: early access **September 15, 2026**; "the first System One model"; trained with **RLCD (Reinforcement Learning for Calibrated Decisions)**.
- Launch-post comparison: LLMs optimized with RLHF/RLVR vs Jev RLCD; LLM cost "$0.20–$10 / MTok input, output ~5x more" vs **Jev $0.042 / MTok input, output free**; speed "3–329 s end-to-end for frontier models" vs **70–500 ms end-to-end** (vendor-reported); sampling "parallel, all outputs in a single query."
- Primitives: Choice → `choice`, `probabilities`, `confidence`; Score → `score`, `probabilities`, `confidence` (score = "probability-weighted rubric position"); Noul → `noul` (0–1). Questions in one request run in parallel against same state.
- Snapshot Sept 18: alias `jev-latest` → `jev-1.13.0`; endpoint `POST https://api.typesafe.ai/v1/systemone`; limits 250,000 tokens/s, 1,200 requests/min; Choice up to **255 options**; text only. Direct access via waitlist; no-waitlist via Vercel AI Gateway (`typesafe-ai/jev`, AI SDK `experimental_evaluate`) and Cloudflare Workers AI (`typesafe/jev`, `env.AI.run`). [Stale re waitlist.]
- SDK: Python `pip install typesafe-sdk` — `from typesafe_sdk import Choice, Noul, Score, TypeSafeClient`, `with TypeSafeClient() as client: client.system_one(...)`, Score takes `criteria=[list of levels]`; JS `npm install @typesafe-ai/sdk` — `choice, noul, score, TypeSafeClient`, `client.systemOne`.
- Company: San Francisco lab; founder Diogo Almeida (ex-OpenAI, instruction-following); raised **$40M**; "machine-native intelligence". Official essays: Manifesto, "The Bitterest Lesson", "AI: too good to be true, too bad to be useful".
- Official URLs: docs.typesafe.ai/agent-skill, /patterns/fan-out, /patterns/confidence-routing, /patterns/composite-scoring, /patterns/intent-routing, /concepts/how-to-build-with-system-one, /concepts/use-case-map, console.typesafe.ai/docs/cookbooks, evals.typesafe.ai ("four automation workflows"), discord.gg/typesafe, LinkedIn company page.
- Launch demos: Jev plays Doom (~10 queries/s, ~$7/hour); Wikiracing (255-option Choice ceiling).
- Author-reported builds: Every editorial vibe check 37 docs × 21 questions = 1,709 judgments, <$0.01, 0.35 s median, 6/7 planted defects caught; 100,000 posts × 14 Nouls in 20.4 s for $0.67; Tocsin 22.8M log lines ~6 min, $0.64; 723 ads × 30 personas 21,690 decisions $0.22; 1,891 ads 19 s $0.12; 3,282 posts 4.25M tokens $0.1282 8m34s; SuperX 61 questions ~1 s $0.0004/draft; Browser Use flight search ~7 s ~$0.004; Stagehand ~$0.001/task; computer use ~$0.0002/step; $50,000 transfer blocked at 95% irreversible risk; Minecraft Ender Dragon 8m43s $0.97; context shrink ~1M→86K tokens; Laya 421M local 86.5 decisions/s P50 ~9 ms; Tev1 0.8B ~50 ms; madewithjev tracked 729 builds.
- FAQ claims outputs "cannot hallucinate a value outside the space you gave it".

## Key insights / patterns
- Official patterns: speculative fan-out (ask many questions, filter in code); confidence-gated routing ("answer is *what*; confidence is *whether to act*"); composite scoring (atomic scores, weights in code); intent routing (classify, then hand off to logic / specialist LLM / human).
- "Jev Engineering": LLM writes, Jev decides, code acts; pair Jev with LLMs rather than replace them.
- Always include an `other` option in Choice.
- Use-by-job taxonomy: sort big piles, triage queues, choose agent's next action, decide inside a frame (games/control), score before shipping, block risky irreversible steps, shrink LLM context, judge rows in SQL, pick UI components.
- Negative/nuanced evals: Jev Phishing Bench — Claude Haiku 4.5 wins accuracy; Jev search rerank eval (9,831 pairs) — Jev alone does not beat embeddings, fusion wins; spam eval has post-hoc tuning caveats.
- Chess: legal moves as Choice makes illegal moves impossible by construction.

## Standout entries
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post (official)
- [Models, prices, and limits](https://docs.typesafe.ai/models) — spec page (official)
- [Workflow evals](https://evals.typesafe.ai) — official methodology & results (official)
- [Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) — official pattern (official)
- [Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out) — official pattern (official)
- [The Bitterest Lesson](https://typesafe.ai/blog/bitterest-lesson) — TypeSafe essay (official)
- [Jev on Cloudflare Workers AI](https://developers.cloudflare.com/ai/models/typesafe/jev/) — gateway (integration)
- [Every's editorial vibe check](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds) — hands-on article with metrics (case study)
- [Jev played chess (dev.to)](https://dev.to/maximsaplin/typesafe-jev-played-chess-and-landed-next-to-reasoning-models-28ga) — chess vs reasoning models (case study)
- [Jev Phishing Bench](https://github.com/anisselbd/jev-phishing-bench) — 2,000 emails vs Haiku 4.5 (benchmark)
- [Jev search rerank eval](https://github.com/zhuyansen/jev-search-rerank-eval) — 9,831 pairs vs BM25/bge-m3 (benchmark)
- [jev-sec-bench](https://github.com/Gaurav-Gosain/jev-sec-bench) — prompt-injection & vuln-code detection (security)
- [Jev DSPy Lab](https://github.com/jmanhype/jev-dspy-lab) — calibration/selective risk via DSPy (evaluation)
- [Tocsin](https://github.com/TPAteeq/tocsin) — 22.8M log lines pattern triage (case study)
- [Verdict](https://github.com/Manavarya09/verdict) — 118M Apache-2.0 /v1/systemone-compatible model w/ conformal abstention (open model)
