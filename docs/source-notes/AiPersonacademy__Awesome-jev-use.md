# AiPersonacademy/Awesome-jev-use
- **One-liner:** "APA Awesome Jev" — bilingual (EN/ZH) curated Jev list with a solid official-cookbook index, heavily interleaved with AIPersona Academy / JevProxy self-promotion.
- **Language(s):** English + Simplified Chinese (README_zh.md)
- **Type:** curated-list (promotional)
- **Scale:** ~260 bullet/table rows. Sections: What is Jev?; Quick Ecosystem Directory (table by Gateways & Proxies, Security & EDR, Agents & Runtimes, Code & Search, Data & Scraping, Video & Media, Gaming & Simulation, Web & Real-Time…); APA Showcase & Integrations; Official; Community & AIPersona Academy Hub; SDKs & Clients; Applications; Demos & Games; Agent Tools; Research & Open Models; Cookbooks (3 APA + ~20 official); Patterns; Articles; Related; Contributors. cookbooks/ has 3 short APA recipes (persona state routing, social sentiment guardrails, buyer persona scoring).
- **Quality flags:** Promotional: repeated links to whop.com/aipersonaacademy (paid masterclass), "Flagship Commercial Agent Gateway" JevProxy (jevproxy.com) with unverified "cut costs 65%, latency 90%, sub-25ms at $0.0001" claims; ~6 JevProxy blog posts listed as "Articles" (SEO-ish, e.g. "Top 5 JEV Gateway Platforms"). Claims like "microsecond policy guardrails, zero hallucination risk" are marketing. Underneath, the non-APA parts (official links, cookbook index, research/benchmarks with honest caveats) are accurate and appear copied from a good upstream list. Listed as a source (123 entries) by mabodx.
- **Unique value:** Most complete index of official TypeSafe cookbook URLs (~20); independent-measurement articles (Zenn JP, agentjournal.dev, amankumar.ai, ASSAY-001 pre-registered calibration check); slopsquatting note on PyPI `typesafe-ai`; official blog posts (Bitterest Lesson, "too good to be true").

## Facts claimed about Jev
- Launched in early access **15 September 2026**. Jev = TypeSafe's "flagship System One model".
- Primitives: Choice → `choice`, `probabilities`, `confidence`; Score → `score`, `probabilities`, `confidence`; Noul → `noul` (0–1). Questions run in parallel against same state.
- `POST https://api.typesafe.ai/v1/systemone`; API keys at console.typesafe.ai/settings/keys (`TYPESAFE_API_KEY`); playground console.typesafe.ai/playground; agent skill docs.typesafe.ai/agent-skill (typesafe-ai/skills); console cookbooks https://console.typesafe.ai/docs/cookbooks.
- Vercel AI Gateway hosts `typesafe-ai/jev` for AI SDK `evaluate`, "no TypeSafe waitlist required".
- PyPI `typesafe-ai` is a community redirect shim registered to block slopsquatting; real package is `typesafe-sdk`.
- Cookbook code: `from typesafe_sdk import TypeSafeClient, Choice, Score` (APA's own recipe; unverified).
- Open models: laya "421M… sub-15ms (~86.5 decisions/sec)"; JevProxy blog describes Laya as "Convai Laya (ModernBERT 421M)" vs Jev "(RLCD cross-attention)" — architecture claim about Jev is unverified (other lists say architecture unpublished). kev: 0.6B/4B/8B Qwen3 + LoRA + pointer head, ~40 ms on H100, Apache 2.0 (Gerry9000 says Qwen 3.5 0.8B/4B/9B — **contradiction**). JEVfire ~71 ms/action locally. PocketJev ~1 s on iPhone.
- Jev Phishing Bench: "Haiku wins accuracy here". zhuyansen rerank eval (9,831 pairs): "Fusion wins; Jev alone does not beat embeddings". jev-audio-beeper ~466 ms.
- JevProxy claims (vendor-promotional): <25 ms, $0.0001, 65% cost cut, 90% latency cut; "1,420ms latency cliff" for autoregressive tool calls.

## Key insights / patterns
- Official patterns: speculative fan-out (ask questions that may not apply, filter in code); confidence-gated routing ("the answer is *what*; confidence is *whether to act*"); composite scoring; intent routing.
- Official cookbooks worth surfacing: parallel questions; semantic_find (Choice over line ids + Noul "does an answer exist?"); BM25 shortlist → rerank; LLM guardrails; citation check; classifying RAG passages (contradiction, prompt injection); function calling with closed-set args; skill suggestion; hierarchical classification via beam search; SDE cascade (mini → verify → reasoning); date extraction; pre-parsed value extraction (regex candidates, Jev picks span); entity alignment; autoresearch feature discovery; classification using confidence (climb hierarchy when unsure); autoformat; self-consistency.
- Persona/state-machine pattern: model agent persona as a state machine; Jev Choice picks next state, transition only if confidence > 0.85, else escalate.
- One direct judge question vs 12–14 Jev-scored dimensions + locally fitted weights (agentjournal.dev) — feature-extraction approach measured.
- Watch for slopsquatting on package names.

## Standout entries
- [Documentation](https://docs.typesafe.ai/introduction) — official docs (official)
- [Agent skill](https://docs.typesafe.ai/agent-skill) — official coding-agent skill (official)
- [The Bitterest Lesson](https://typesafe.ai/blog/bitterest-lesson) — official essay (official)
- [AI: too good to be true, too bad to be useful](https://typesafe.ai/blog/ai-too-good-to-be-true-too-bad-to-be-useful-typesafe-ai) — official essay (official)
- [Semantic find cookbook](https://docs.typesafe.ai/cookbooks/semantic_find) — line-level search recipe (tutorial)
- [SDE cascade cookbook](https://docs.typesafe.ai/cookbooks/sde_cascade) — extraction cascade (tutorial)
- [Hierarchical classification cookbook](https://docs.typesafe.ai/cookbooks/hierarchical_classification) — beam search over taxonomies (tutorial)
- [ASSAY-001](https://github.com/jourdanlabs/assay-001) — pre-registered calibration check on Banking77/CLINC150 (benchmark)
- [jevcal](https://github.com/abhixhek/jevcal) — fits per-question thresholds, fails CI on regressions (tool)
- [Jev DSPy Lab](https://github.com/jmanhype/jev-dspy-lab) — record/replay + calibration metrics (tool)
- [zhuyansen/jev-search-rerank-eval](https://github.com/zhuyansen/jev-search-rerank-eval) — rerank vs BM25/bge-m3 with judge circularity (benchmark)
- [Zenn: TypeSafeのJevを正しく驚く](https://zenn.dev/nwn/articles/824026c76116e0) — JSON-vs-logit shortcut reproduced on Gemma (article, JP)
- [Testing Jev on public and private data](https://amankumar.ai/blogs/jev-measured) — 16,000 calls vs gpt-5.4-mini/gpt-5.6-luna (article)
- [The Register launch coverage](https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711) — news (article)
- [mattn/sqlite3-jev](https://github.com/mattn/sqlite3-jev) — SQLite extension exposing Jev primitives (database)
