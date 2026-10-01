# majiayu000/awesome-jev
- **One-liner:** Careful, bilingual (EN/ZH) curated Jev list with website, ~410-entry catalog, official-docs map, gotchas, research notes, dated updates, arXiv papers, and a tested example.
- **Language(s):** English + Simplified Chinese (README_zh.md, most catalog/updates in Chinese)
- **Type:** curated-list (with research notes + study guide)
- **Scale:** README features ~45 hand-picked links: Getting started; SDKs and integrations; Agent tools; Browser automation; Applications and games; Evaluations and open implementations; Articles and Chinese resources; Before using; Field notes. catalog/FULL.md + entries.json = 410 entries in: 官方资料 (Official), SDK 与客户端, 网关与集成, 智能体工具, 浏览器与电脑操作, 应用, 游戏与模拟, 演示与示例, 评测与研究, 资源清单, 文章与讨论. Also patterns/ (routing, labeling, verification, realtime, scoring), taxonomy/ (12 category pages incl. critique-limits, chinese), guides/ (start, gotchas with 27 items, featured-review), research/ (8 notes: official docs, competitors, HN critique, X haul, Chinese coverage), updates/ (dated 2026-09-20…09-30), examples/ticket_routing.py with unit tests, GitHub Pages site (docs/).
- **Quality flags:** High quality, candid, non-promotional; explicitly "unaffiliated", "not verified", keeps negative results. Maintainer spot-checked featured entries (SDKs install/import) but didn't run live API calls. Research notes are dated "historical". Catalog descriptions partly auto-derived from READMEs ("原始资料未提供说明" placeholders). Fresh (updated 2026-09-30).
- **Unique value:** Best map of official docs (llms.txt nav incl. every docs URL); faithful summary of launch post's own "nuance" caveats and the jev-1.13 jaggedness page; HN thread IDs & critique themes; 6 arXiv papers with summarized findings; gateway specifics (Vercel, Cloudflare, OpenRouter decisions endpoint, LiteLLM pass-through); security research (Decision Hijacking); Chinese-press tests; offline tested example.

## Facts claimed about Jev
- Endpoint `POST https://api.typesafe.ai/v1/systemone`; input `state` (string|object|array) + typed `questions`; output typed answers + probabilities (+ confidence for Choice/Score). Primitives: Choice, Score, Noul.
- Aliases `jev-latest` (stable), `jev-preview`; responses report versioned id e.g. `jev-1.13.0`. Pin versioned IDs because aliases drift; rate limits adjusted dynamically (Models page).
- Packages: `typesafe-sdk` (Python), `@typesafe-ai/sdk` (JS/TS); typesafe-ai/system-one-adapter-python; typesafe-ai/skills. Docs index https://docs.typesafe.ai/llms.txt; playground console.typesafe.ai; evals https://evals.typesafe.ai/; Discord discord.gg/typesafe; X @typesafeai.
- Launch post: "Introducing System One Models and Jev", Diogo Almeida (founder), Sep 15, 2026. Training = **RLCD** (calibrated decisions) vs RLHF/RLVR; "parallel sampler"; price **$0.042 / MTok input, output free**; speed **70–500 ms E2E** (vendor) — note: differs from other lists' "30–50 ms"; Choice cardinality up to **255** (higher via 2-stage score-then-choice); homepage claims 193.6× / 444.6× gains ("higher end"); speed measured from West Coast laptops. "Jev is neither small nor an LLM"; architecture unpublished. Name from William Stanley Jevons (Jevons paradox). Manifesto tagline "Composable AI: Build Prod, Not God".
- Vendor workflow evals use reference probabilities from frontier models (Astra/Fable averages), not ground truth; built by TypeSafe's capabilities team (possible bias). "0% type errors" is a mathematical schema guarantee, not accuracy. Doom demo uses structured state text, not pixels.
- Access: TypeSafe direct = waitlist/early access. Gateways: Vercel AI Gateway `typesafe-ai/jev` (AI SDK `experimental_evaluate`); Cloudflare Workers AI `typesafe/jev` (docs list **32,000 token context**); OpenRouter via Decisions endpoint `/api/alpha/decisions`, model id `~typesafe/jev-latest` (from nexibeo/jev-cookbook, unofficial); LiteLLM pass-through `POST …/typesafe/v1/systemone`, spend logged as `typesafe/jev-1.13.0`.
- Original HN title reportedly "Jev: New frontier model 40-400x cheaper and 20-200x faster" (later softened). HN launch id 49717558 (~1,787–1,800 points, ~473–480 comments).
- Jaggedness (jev-1.13, reviewed 2026-09-17): struggles with indirection, literalism, numeric precision; 9 failure modes: literal reading, math/numbers, date/time comparison, indirection, large irrelevant state, adversarial content, contradictory criteria, structural invariants (P(noul) ≠ P(choice yes); P + P(¬) ≠ 1), generation. Score levels weak at interpolating magnitudes; hex/RGB proximity unreliable.
- Third-party numbers: Every/Mike Taylor judged writing in 0.7 s, caught 6 of 7 planted flaws. dchristopoulos/jev-aita: 770 AITA posts, median 0.39 s, ~6.3× faster & ~62× cheaper than Sonnet 5, worse Brier — "not the vendor's 40–200×". jev-column-race: 4.1× faster, 7× cheaper than Gemini 3.8 Flash on 1,000 reviews. Janus/calibre: Banking77 80.2% at $0.103 per 500 decisions. Aitejiu harness: multi-skill R@1 ~9% → ~81% using chunked choice then noul verification.
- Papers: arXiv:2609.26550 JEV-as-a-Judge (CMU): within ~3 pts of best LLM judge at ~0.36% cost on preference/factuality; 9–20 pt gap on JudgeBench/style-adversarial; cascade keeps ~99% accuracy. arXiv:2609.29769 (UPenn) rubric judges: binary checklists near/better and 29–325× cheaper; graded scales worse; LLMs repeat Jev's confident errors ~96% → cascade gains ≤1.5 pts. arXiv:2609.28613 Decision Hijacking (NTU): injection raises attack option prob ~+0.043, selection ~1.8%, adaptive ~3.5%. arXiv:2609.27678 Same Scores, Different Decisions (ContractNLI): Jev cheapest/fastest, hosted LLMs more accurate. arXiv:2609.23986 Jev-Mem: LoCoMo 0.777 vs 0.700 baseline. arXiv:2609.30216 Jev in the Wild: 2,170 GitHub projects through 2026-09-22.

## Key insights / patterns
- Valid format ≠ correct judgment; confidence = preference among given options, not P(correct) — remove the right answer and it still picks confidently.
- Arithmetic, counting, dates in code (extract date parts via Choice, compare in code; count via one Noul per item).
- Filter state first (context rot); split compound intents; avoid Noul where "true" means "no".
- Measure thresholds on own labeled data; never copy "0.8" from blogs; thresholds don't transfer between Noul and Choice or across versions.
- Multi-label: independent noul per candidate clusters ~0.5 (noise) — let options compete via chunked choice, then verify with noul.
- Low-score bucket is not "safe" under injection; typed outputs change but don't eliminate injection risk; don't expose full probability vectors to untrusted parties.
- Cascades mainly save money, not accuracy — correlated errors between Jev and flash LLMs.
- Compaction: "keep only Jev-selected blocks" hid ~17% of later-needed facts (pi-jev-context); hide only confidently-useless blocks.
- Semantic SQL (jevql) sends every row off-machine and bills per row — pre-filter with cheap predicates.
- jev_jsonschema only maps boolean→Noul, enum→Choice, narrow int ranges (≤10)→Score.
- Decision models need a candidate space; if candidates must be generated, use an LLM. Realtime demos rely on harnesses that compress the world to state + legal actions.

## Standout entries
- [TypeSafe docs](https://docs.typesafe.ai/) — official API/quick start/cookbooks (official)
- [Jev 1.13 jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md) — official failure modes (official)
- [Launch post](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — intro, RLCD, pricing, nuance boxes (official)
- [TypeSafe skills](https://github.com/typesafe-ai/skills) — official coding-agent skill (official)
- [Vendor workflow evals](https://evals.typesafe.ai/) — vendor evaluations (official)
- [Cloudflare Workers AI – typesafe/jev](https://developers.cloudflare.com/ai/models/typesafe/jev/) — gateway docs (integration)
- [OpenRouter Jev-Verified Cascade](https://openrouter.ai/docs/cookbook/evaluate-and-optimize/jev-verified-cascade) — cascade recipe (tutorial)
- [LiteLLM TypeSafe pass-through](https://docs.litellm.ai/docs/pass_through/typesafe) — proxy integration (integration)
- [JEV-as-a-Judge, arXiv:2609.26550](https://arxiv.org/abs/2609.26550) — judge cascade study (paper)
- [Jev vs LLMs as Rubric Judges, arXiv:2609.29769](https://arxiv.org/abs/2609.29769) — correlated error limits (paper)
- [Decision Hijacking, arXiv:2609.28613](https://arxiv.org/abs/2609.28613) — prompt-injection on typed Choice (security paper)
- [Jev in the Wild, arXiv:2609.30216](https://arxiv.org/abs/2609.30216) — ecosystem analysis of 2,170 repos (paper)
- [anisselbd/jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench) — negative-result benchmark vs Haiku 4.5 (benchmark)
- [anessbelbati/jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench) — Jev vs Cohere Rerank 4 vs zerank-2, 14 datasets (benchmark)
- [Every / Mike Taylor vibe check](https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds) — hands-on review (article)
