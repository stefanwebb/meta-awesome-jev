# OmniJev/awesome-jev-gallery
- **One-liner:** Research-oriented "Awesome JEV" list of papers, open reproductions, benchmarks with headline numbers, lineage/prior work, and the tools Jev is sold against; with a gallery site.
- **Language(s):** English
- **Type:** curated-list (research/benchmark-oriented; also has a site built from entries.json)
- **Scale:** 161 entries (25 papers, 44 open source, 35–36 benchmarks, 119 with code). Sections: News; System One & Jev (8); Open Source (44); Built with Jev (36); Benchmark & Leaderboard (36); Commentary & Analysis (8); The Shape Before Jev (15); What Jev Is Sold Against (9); Where the Name Comes From (5); Related Lists (3). updates/2026-09-22.md collection log with pinned-commit evidence.
- **Quality flags:** High quality, dense one-line summaries with author-reported numbers and scoping caveats (update log explains what each number does and doesn't mean, pins reviewed commit SHAs). Self-promotional in that OmniJev lists its own OneJev and PlayJev at top of Open Source. Some arXiv IDs (2609.xxxxx) and Zenodo record are future-dated relative to typical knowledge but consistent with 2026 timeline; cannot verify. Name "Awesome JEV" duplicates OmniJev/awesome-jev (Omrigotlieb list points to both).
- **Unique value:** Best benchmark roundup with headline numbers; intellectual lineage (zero-shot entailment, InstructGPT RM, RLCR, LLaDA, GLiNER/GLiClass, monoBERT, Llama Guard, Rewarding Doubt, vLLM, Mercury) with arXiv IDs; "sold against" section (Outlines, DSPy, RouteLLM, Guidance, Structured Outputs, JSONSchemaBench, MT-Bench, Constitutional Classifiers); name etymology (Kahneman System 1, Jevons paradox); HN architecture speculation.

## Facts claimed about Jev
- Launch post: state in, typed probabilistic decisions out, **RLCD** training, **70 to 500 ms**, **$0.042 per MTok**.
- HN launch thread (item 49717558): **1,850 points, 485 comments**; "the CEO confirms the zero-shot classifier reading and the encoder-with-heads shape". (Omrigotlieb says ~1,800 / ~480.)
- Founder Diogo Almeida co-authored InstructGPT (reward-model lineage). The typesafe-ai GitHub org forked **LLaDA** (masked diffusion LM) and **vLLM** — "strongest public hint" at one-pass slot filling and prefix caching making extra questions nearly free. HN read Jev as a stripped-down text diffusion model or encoder with heads.
- CEO on HN: Jev replaces OpenAI Structured Outputs; constrained decoding makes models dumber; "0% type errors" claim.
- The Register: **$40M raise**, Doom demo; caveat that structured output is a different error type, not correctness.
- Vercel AI SDK: first third-party surface, `jev-latest` as evaluation model behind `experimental_evaluate`, no waitlist.
- Named after Jevons paradox (cheaper decisions raise total decision volume) and Kahneman's System 1; TypeSafe's "Bitterest Lesson" argues against Sutton's Bitter Lesson.
- TypeSafe evals dashboard: Jev **61.7 to 76.0% accuracy, 0.3 to 0.5 s per case** on four workflows. Secondary analyses: warmersun ~**67.8%** mean agreement vs **74.1%** best comparator; Agentpedia 67.8% vs Opus 5's 73.1%.
- Benchmarks (author-reported): JevBench v1.3 composite **74.4** (not accuracy; 534 decisions); Jev Arena 10,000 comments: Jev 1.13 203 s / $0.84 / 94.7% vs DeepSeek Flash 824 s / $1.50 / 96.3%; jev-benchmarks vs GLiNER2.5: 0.910 AG News, 0.870 Banking77, worse on emotion; jev-rerank-bench nDCG@10 **0.692 vs Cohere Rerank 4 Pro 0.691 at 422ms** (8 datasets, 1,617 questions); jev-benchmark chess: no better than random from FEN, but NPC addressee F1 0.96, 0.2 s median; sysone-bench: moderation Jev 98.9% vs Laya 83.3%, AG News Laya 94% vs Jev 91%; jev-sec-bench prompt injection 662 deepset messages: **96.5% acc, 0.9927 ROC-AUC, ECE 0.0588, p50 325ms**; jev-spam-eval 18,514 emails **0.9833** (matching TF-IDF trained on 14,800 labels); jev-secret-detection p50 75–90ms; Jevals.com: PubMedQA 91.3% vs best LLM 92.5% at 1/28 cost, Banking77 79.7%; ChaosNLI preregistered study: Choice confidence averages **0.807 vs 0.468 human agreement** on split items (overconfident); DeepSearcher stopping 93.25% Recall@5 (tie with DeepSeek); MemSearch rerank 79.41% vs Voyage rerank-3 81.87%; Vector Graph RAG MuSiQue 68.87%, HotpotQA 93.50% Recall@5; jev-use: 82.2% agreement with Claude Opus 5 over 454 judgments, compaction 56.3% (below constant answerer); Near Here: Jev 96% at 0.59 s and $0.043/1,000 vs Mistral small 4 84%, Gemini Flash-Lite 86%; Every Mini-Vibe Check: 777 judgments / 37 articles in 0.7 s for a quarter cent, caught 6 of 7 planted defects (Fable 7); poker probe: 15–30 point swings from relabelling; agentjournal 0.9076 vs 0.8373 Japanese NLI, 37.2% vs 1.5% false positives; RoboJEV Jev 43/50 vs rules 48/50; jevos (MiniCPM5 1B) 0.815 vs Jev 0.927 on Noul.
- Papers: "Just Ask Jev" (arXiv 2609.29429, 44 alignment-failure detection benchmarks); "JevAdvBench" (arXiv 2609.31142, black-box attacks); "Jev in the Wild" (arXiv 2609.30216, 2,170 GitHub projects).
- Jev Decision Index (HF space): Jev + 70 open reproductions on 43 benchmarks, ~120,000 decisions per model, chance-corrected.

## Key insights / patterns
- Jev's shape has deep precedent: entailment zero-shot classifiers, cross-encoders, reward-model heads, guard classifiers; RLCD ≈ RLCR/Rewarding Doubt proper-scoring-rule rewards.
- Prefix/KV caching of shared state is why many questions per call are nearly free.
- Recurring built-with patterns: Jev picks from indexed element/control tables with a small LLM for typing (Ultrafast, TipTour, typesafe-computer-use ~1/50 cent/step); one Noul per rule on every edit (Abide, ~300 ms); per-chunk Noul for code search/test selection (jgrep, 16 chunks/request); robot control with Jev deciding semantics and controller in code (jev-drone 2.5 Hz, RoboJEV — rules still beat Jev).
- Weak spots evidenced: chess from FEN, compaction (jev-use), relabel sensitivity (poker), overconfidence where humans disagree (ChaosNLI), rules beating Jev in robotics.
- Compatibility ≠ calibration: many open replicas report on JevBench's 231 public tasks only; read scopes carefully.

## Standout entries
- [Introducing System One Models and Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — launch post (official)
- [Hacker News launch thread](https://news.ycombinator.com/item?id=49717558) — CEO architecture comments (discussion)
- [Jev Decision Index](https://huggingface.co/spaces/multimodalart/jev-decision-index) — leaderboard of Jev vs 70 reproductions (benchmark)
- [JevBench](https://github.com/fstandhartinger/jevbench) — composite benchmark (benchmark)
- [jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench) — reranking vs Cohere (benchmark)
- [jev-sec-bench](https://github.com/Gaurav-Gosain/jev-sec-bench) — prompt injection detection (benchmark)
- [Confident Where People Disagree](https://zenodo.org/records/22971492) — preregistered calibration study on ChaosNLI (paper)
- [Just Ask Jev](https://arxiv.org/abs/2609.29429) — Jev as zero-shot alignment-failure detector (paper)
- [JevAdvBench](https://arxiv.org/abs/2609.31142) — adversarial attacks on RLCD models (paper)
- [Jev in the Wild](https://arxiv.org/abs/2609.30216) — ecosystem survey of 2,170 projects (paper)
- [Jevals](https://jevals.com/) — Jev vs six LLMs on human labels (benchmark)
- [MrJev tool reviews](https://mrjev.com/best-jev-tools/) — security audit of 72 community tools (commentary)
- [RLCR](https://arxiv.org/abs/2507.16806) — closest published relative of RLCD (paper)
- [Bespoke Nimble](https://github.com/bespokelabsai/nimble) — open Jev recipe with eval suite (reproduction)
- [Abide](https://github.com/coldteadotai/abide) — enforce AGENTS.md rules with one Noul per rule (tool)
