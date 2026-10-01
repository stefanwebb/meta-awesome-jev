# The Evidence: What Independent Testing Says About Jev

> A digest of the measurements scattered across the 106 source lists: benchmarks, calibration audits, robustness probes, security studies, and the negative results that most lists bury.
>
> **How to read this page.**
> - Nearly every number below is **author-reported**. It comes from a single person or team, usually with a small n, run within two weeks of launch, and almost always on `jev-1.13.0`. Very little has been replicated.
> - Where only the vendor reported a figure, it is marked *vendor*.
> - Treat each result as evidence about *that setup*, not as a universal ranking.
> - The best curated trackers are [Yifan-Lan/awesome-jev-robustness](https://github.com/Yifan-Lan/awesome-jev-robustness) (132 robustness studies), [robokrunch/awesome-jev](https://github.com/robokrunch/awesome-jev) (a benchmark digest), [kydlikebtc/awesome-jev](https://github.com/kydlikebtc/awesome-jev) (negative results first) and [OmniJev/awesome-jev-gallery](https://github.com/OmniJev/awesome-jev-gallery).

[← back to the main list](../README.md)

## Contents

- [Scorecard](#scorecard)
- [Head-to-head accuracy](#head-to-head-accuracy)
- [Calibration](#calibration)
- [Consistency and invariance](#consistency-and-invariance)
- [Prompt injection and adversarial robustness](#prompt-injection-and-adversarial-robustness)
- [Judging and evaluation](#judging-and-evaluation)
- [Search, reranking and RAG](#search-reranking-and-rag)
- [Agents, browsers and computer use](#agents-browsers-and-computer-use)
- [Games, robotics and control](#games-robotics-and-control)
- [Latency and cost measurements](#latency-and-cost-measurements)
- [Negative and null results](#negative-and-null-results)
- [Benchmark suites and leaderboards](#benchmark-suites-and-leaderboards)

## Scorecard

| Where Jev holds up | Evidence |
|---|---|
| **Cost** at scale | 34.1M tokens for $1.43 ([agentjournal](https://agentjournal.dev/blog/llm-judge-vs-feature-extraction/)); 499,500 police narratives screened for $25.23 ([arXiv 2609.24052](https://arxiv.org/abs/2609.24052)); ~3.7k repo classifications (~3k tokens each) for $0.50 ([rhc98](https://github.com/rhc98/awesome-jev)) |
| **Short-text classification and yes/no judgments** | True/false 92.5%, the best of five models tested ([awesome-jev-verified](https://github.com/punk2898/awesome-jev-verified)); SST-2 96%, RTE 94% |
| **Robustness to distribution drift** (vs trained baselines) | Spam: 98.3% ≈ TF-IDF in-domain, but **97.3% vs 72.5%** on drifted 2026 mail ([jev-spam-eval](https://github.com/bitnovus/jev-spam-eval)) |
| **Blunt prompt-injection resistance** | 1/80 injections succeeded (GPT-4.1-mini: 73/80) ([awesome-jev-verified](https://github.com/punk2898/awesome-jev-verified)); 1/1,056 flips on decision-injection-bench |
| **The high-confidence band** | Confidence 0.9–1.0 was 48/48 correct ([rhc98](https://github.com/rhc98/awesome-jev)); on BBH, conf ≥ 0.9 was 92/100 correct ([wuyoscar](https://github.com/wuyoscar/jev-skill)) |
| **Binary judging and rubric checklists** | Within ~3 pts of GPT-6 at 0.36% of the cost on readable-verdict tasks ([arXiv 2609.26550](https://arxiv.org/abs/2609.26550)) |
| **Reranking a shortlist** | Ties Cohere Rerank on nDCG@10 (0.692 vs 0.691) ([jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench)) |
| **Abstention, when an escape option exists** | AbstentionBench F1 0.855, first of 20 systems ([jev-abstentionbench](https://github.com/sshariqali/jev-abstentionbench)) |

| Where Jev breaks | Evidence |
|---|---|
| **Counting and arithmetic** | Counting 65% vs Sol 97.5%, with every error anchored on a number in the question ([awesome-jev-verified](https://github.com/punk2898/awesome-jev-verified)); exact counting 33%; sequential state mutation 13% |
| **Many-way fine-grained classification** | Banking77 (77-way): 68–83% across studies vs 93% for bge-small + LR ([ickma2311](https://github.com/ickma2311/jev-baselines-eval)) |
| **A missing correct answer** | No escape option: KoBBQ accuracy 0.95 → **0.00** and 79% stereotyped picks ([calibration audit](https://github.com/jujumilk3/jev-calibration-audit)); tool hallucinated on 76% of When2Call no-tool cases |
| **Evidence-shaped injection and natural context** | 61.4% of correct decisions flipped by fluent context ([JevOut](https://arxiv.org/abs/2609.30243)); 96.5% → 26.5% with one injected line ([jagged](https://github.com/zkousama/jagged)) |
| **Option naming** | Renaming 0/1 → no/yes: hosted AUC .81 → .58 ([arXiv 2609.26758](https://arxiv.org/abs/2609.26758)) |
| **Out-of-distribution calibration** | Fails on random 3-SAT ([willkelly](https://github.com/willkelly/jev-evaluation)); 44.7% accuracy at stated p 0.74 on an unknowable rule task ([scienthoon](https://github.com/scienthoon/jev-ood-calibration)) |
| **Planning, search and deep reasoning** | Chess puzzles 25/100 vs Astra 68; ARC-AGI-1 4/400; maze agent got stuck; Tetris topped out without a search harness |
| **Non-English state** | XNLI en 79.3% vs zh 68.7%; Russian −11 pp; Spanish doubles ECE ([jev-acento](https://github.com/marcosmartinez/jev-acento)) |
| **Random or known probabilities** | Fair die: 82.9% stated vs 19% accuracy ([dice](https://github.com/KantaHayashiAI/jev-does-not-play-dice)) |

## Head-to-head accuracy

| Study | Task / n | Jev | Comparators | Notes |
|---|---|---|---|---|
| [OpenRouter](https://openrouter.ai/blog/insights/jev-vs-claude-opus-5-classification/) | Banking77, 3,080 | **81.0%**, 175 ms, $0.11/1k | Opus 5 84.4%, 2,266 ms, $2.42/1k | |
| [awesome-jev-verified](https://github.com/punk2898/awesome-jev-verified) | 2,390 questions via Vercel | T/F **92.5%**, MC 77.3% | Sol 92.1 / 82.5; Terra 91.6 / 82.0; Luna 86.0 / 80.5; GPT-4.1-mini 87.8 / 74.3 | Open harness with per-question JSONL. The most rigorous claim-by-claim audit. |
| [ickma2311/jev-baselines-eval](https://github.com/ickma2311/jev-baselines-eval) | Banking77 / CLINC150 | 0.832 / 0.870 | bge-small + LR **0.933** (9 ms) | Pre-registered. Jev was only 2.2× faster than a nano LLM. |
| [4esv/jev-eval](https://github.com/4esv/jev-eval) | four public sets | equal on easy tasks; −6.7 on 77-way routing | GPT-5.6 Terra | 5× faster, 41–50× cheaper |
| [chepyle/jev-test](https://github.com/chepyle/jev-test) | LexGLUE, 23,607 | micro-F1 69.9 @ $4.02 | Luna 71.3 @ $16.45 | |
| [arXiv 2609.24574](https://arxiv.org/abs/2609.24574) | 18 social-science tasks, 7,977 items | trails the best LLM on 14/15 tasks (median −11.6 macro-F1) | 19 LLMs | ~1/44 the cost; better calibrated than 16 of 19; routing matches the LLM at ¼–½ the cost |
| [arXiv 2609.27678](https://arxiv.org/abs/2609.27678) | ContractNLI | lowest cost and latency | hosted LLMs are more accurate | |
| [anisselbd/jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench) | 2,000 emails | direct 62.6%; **atomized + LR 95.0%** | Haiku 4.5 81.3%; regex 91.8% | The canonical "question atomization" lesson |
| [kokuren333/jev-jmle-benchmark](https://github.com/kokuren333/jev-jmle-benchmark) | Japanese medical exam, 3,556 | **88.58%** | | |
| [stperic/jev-medhallu-benchmark](https://github.com/stperic/jev-medhallu-benchmark) | MedHallu, 1,000 | 92.9%, 204 ms, $0.03/1k | four fast LLMs 92.4–95.1% | Settling the 37% of items at ≥90% confidence cut LLM calls 37% with no accuracy loss |
| [wuyoscar model panel](https://github.com/wuyoscar/jev-skill/blob/main/docs/experiments/model-panel/README.md) | BBH 160 | **138/160** (best) | DeepSeek V4 Flash, Qwen35B-A3B, Qwen9B, Llama3.1-8B | LogiQA-zh 16/20 (DeepSeek 19) |
| RFQ study ([dev.to](https://dev.to/cookies_c9dc8b91f33d29250/we-tested-a-35b-llm-against-typed-decision-models-on-12000-real-rfqs-confidence-changed-the-winner-56hh)) | 12,000 real RFQs | **91.9%**, ECE 0.049, 86.5% auto-accepted at 95% precision | Qwen3.5-35B 89.6% (69 malformed); Laya 78.0%, ECE 0.322 | Calibration decided the winner |
| [Near Here](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation) | event validation, 50 | **48/50** (96%), 0.59 s, $0.043/1k | Flash-Lite 43, Mistral Small 4 42 | |
| [Jevals.com](https://jevals.com/) | PubMedQA / Banking77 / HelpSteer2 | PubMedQA 91.3% vs best 92.5% at 1/28 the cost; Banking77 79.7% | Jev vs six LLMs, human labels | Noul tied #1 with Gemini 3.8 Flash |
| [yzfly](https://github.com/yzfly/awesome-jev-zh) / [judgekit](https://github.com/lexingtonhibiki/judgekit) | Chinese tickets / 130-item Chinese eval | 14/15; 97.7% | keyword baseline 91.5% | Batched 15/15 vs one-by-one 80% |
| Tomer Tunguz | 98 production email threads | 80% | local SemIf 82%; production model 47% | 76–209× cheaper |
| tax-doc-classifier ([repo](https://github.com/kyotofin/tax-doc-classifier)) | 261 IRS forms | 100% strict, ~$0.001/page | production Sonnet | 38 low-confidence strict errors among 753 blank-form pages |
| NASA Kepler | 8,054 KOIs | 72.5% (another run: 54.2%) | 3-rule baseline 64.4% | Conflicting replications |
| [arXiv 2609.24052](https://arxiv.org/abs/2609.24052) | Texas crash narratives | F1 **0.908** vs 2,416 blinded human judgments | | Four variables below F1 0.70; recalibration ECE 0.0231 → 0.0069 |

## Calibration

| Study | Finding |
|---|---|
| [willkelly/jev-evaluation](https://github.com/willkelly/jev-evaluation) (123,805 requests, $12.69) | ECE **0.075** in-domain (support routing), but calibration **collapses OOD** (random 3-SAT). "Batching to 255 questions is genuinely free." |
| [jujumilk3/jev-calibration-audit](https://github.com/jujumilk3/jev-calibration-audit) (11,759 items) | Largest audit. KoBBQ "unknown" chosen 95% of the time when available; with it removed, 79% stereotyped picks at 0.79 confidence. |
| [AnthusAI/Jev-Calibration](https://github.com/AnthusAI/Jev-Calibration) (8,801) | Noul stated 79.0% vs actual 72.3%; Choice stated 91.4% vs 76.1% (overconfident); isotonic recalibration ECE 0.117 → **0.008**. |
| [jourdanlabs/assay-001](https://github.com/jourdanlabs/assay-001) (pre-registered) | CLINC150 ECE 0.020, Banking77 0.094; zero type errors in 8,576. Split verdict. |
| [scienthoon/jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) | OpenBookQA 94.2% / ECE 0.024; 44.7% on an unknowable rule-based task at stated p 0.74. |
| [wuyoscar BBH](https://github.com/wuyoscar/jev-skill/blob/main/evals/CALIBRATION_RESULTS.md) | ECE 0.0994; the [.9, 1] bin has mean p 0.98 but accuracy 0.89 (overconfident). |
| [KantaHayashiAI/jev-does-not-play-dice](https://github.com/KantaHayashiAI/jev-does-not-play-dice) | Fair die: Choice puts 82.9% on its pick at 19% accuracy; fair coin: 92% at 52%. A stated 45% returns 6.6%, and 55% returns 95.9% (a cliff at 50%). Independent Nouls recover ~1/6. |
| [Zenodo: Confident Where People Disagree](https://zenodo.org/records/22971492) (pre-registered, ChaosNLI) | Choice confidence averages **0.807 vs 0.468 human agreement** on split items. |
| [jev-certify](https://github.com/nikkoxgonzales/jev-certify) | Confidence exactly 1.0 on 56.4% of CLINC150 answers (nine wrong); a 5% misroute bound held with 84.75% auto-routed; the scope gate missed its target 3.6× when OOS prevalence rose. |
| [primeline.cc](https://primeline.cc/blog/typesafe-jev-pre-registered-test) (~9,750 calls, pre-registered) | 12 probes of documented failure modes: **4 real, 8 refuted**. Derives the Choice confidence formula. |
| [FirasSX914/calibre](https://github.com/FirasSX914/calibre) / [Janus](https://github.com/FirasSX914/Janus) | Optimal thresholds and routing value **flip between datasets** (Banking77 vs Web of Science). |
| [Nautilus Assay](https://github.com/chunxiaoxx/nautilus-compass/blob/main/docs/wall/GENESIS_HOSTED_JEV_CALIBRATION.md) (240 seeded) | Accuracy 92.2%, Brier 0.048, ECE 0.041. |
| [clownware/bouncer](https://github.com/clownware/bouncer) | Brier 0.036–0.149, but the `destructive` question was 0% correct in the 0.8–0.9 bucket. Ships in observe mode. |
| Coding-agent decisions | Noul ECE 0.169, Choice 0.226. |
| [rhc98 calibration.md](https://github.com/rhc98/awesome-jev) | Precision/recall threshold sweep on an 80-repo gold set; the gate and category confidence are nearly independent axes. |

**Synthesis.** Calibration is a group property that is good in distribution and on short text. Choice and Score skew **overconfident**, while Noul skews **underconfident**. Calibration **does not transfer** across datasets, languages or OOD, and Choice probability collapses toward the pick as option count grows. Prefer Noul for probability estimates, and recalibrate on your own labels.

## Consistency and invariance

- **Repeated identical calls.** The std is 0.001–0.015. One test saw 15 distinct answer sets in 50 identical requests. Another saw no flips over 5 repeats, but only 12/30 responses were bit-identical and max drift was 0.09. Categories were 100% deterministic over 1,000 calls, while Score and Noul confidence drifted up to 14 points ([jev-moral-dilemmas](https://github.com/krsna-smnt/jev-moral-dilemmas)).
- **Official self-consistency.** Choice agreement was 90.8% raw and 99.2% with abstention; Noul std was 0.0102 ([cookbook](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook)).
- **Option order.** There were 0/400 argmax flips on clear items, but the first-listed option gained +0.37 on ambiguous ones. Arithmetic scored 88% with the correct option first vs 57% last ([jev-behavior-study](https://github.com/RINNECODER/jev-behavior-study), 11,621 requests). On a question with no correct answer, the first option was picked 2,000/2,000 times. Reordering the input changed 13–14% of answers in another study. Shuffling candidates changes 2–6% of picks.
- **Phrasing.** Accuracy was 94.8–100% across 12 phrasings of 154 shell commands, but the matching threshold moved from 0.14 to 0.68. Rephrasing one yes/no question moved it from 0.97 to 0.12. There were 0 flips on 60 rephrasings in the verified benchmark, and 1 contradiction in 120 polarity pairs.
- **Primitive framing.** Noul and a 2-option Choice differ by 0.125 on average (>0.2 on 1 item in 6). P(x) + P(not x) averages 1.02, with a range of 0.71–1.42 ([arXiv 2609.33209](https://arxiv.org/abs/2609.33209)). In a synthetic-survey study over 24,596 cells, "how you ask mattered more than which model" ([jev-synthetic-survey](https://github.com/jjd-lab/jev-synthetic-survey)).
- **Paragraph order.** In 48 disclosure cases, 20 answers flipped when paragraphs were reordered and 8 changed on a simple rerun.

## Prompt injection and adversarial robustness

| Study | Result |
|---|---|
| [JevAdvBench, arXiv 2609.31142](https://arxiv.org/abs/2609.31142) ([site](https://JevAdvBench.github.io/JevAdvBench/)) | 812 questions, 66 scenarios, 9,744 single-edit attacks. An appended unverified **opinion flips 12.1%** (vs 10.1% for the strongest injected command) and pushes **38%** of confident answers below 0.8. |
| [JevOut, arXiv 2609.30243](https://arxiv.org/abs/2609.30243) ([code](https://github.com/xzx34/JevOut)) | Fluent natural context redirects **312/508 (61.4%)** correct decisions, 229 of them into high-confidence errors. Open clones: 64.9–73.2%. |
| [Decision Hijacking, arXiv 2609.28613](https://arxiv.org/abs/2609.28613) | 510 InjecAgent cases: injection raises the attack option's probability (~+0.043) but rarely selects it (**1.8%**, 3.5% with adaptive attacks). |
| [Type-Safe Is Not Error-Free, arXiv 2609.26758](https://arxiv.org/abs/2609.26758) | Renaming options changes 70.4 more answers per hundred in open models (AUC .94 → .23); hosted Jev AUC .8146 → .5806; **0% type errors throughout**. Random-string names remove the effect. |
| [zkousama/jagged](https://github.com/zkousama/jagged) | One injected instruction: 96.5% → 26.5%. |
| [Gaurav-Gosain/jev-sec-bench](https://github.com/Gaurav-Gosain/jev-sec-bench) | Prompt-injection detection on 662 deepset messages: 96.5% accuracy, ROC-AUC 0.9927, ECE 0.0588, p50 325 ms. |
| [willkelly](https://github.com/willkelly/jev-evaluation) | "Polite authority injection" moves 147/200 answers. |
| Iskandeur | One payload flips GPT-5.2 80/80, Jev 26/80. |
| VentureBeat | `rm -rf ~/.ssh` block probability falls from 0.76 to 0.48 after a fake pre-approval. |
| [arXiv 2609.33401](https://arxiv.org/abs/2609.33401) | Jev, Laya, Decider and Nimble as security judges: good average calibration hides systematic failures on attack subgroups. Under strict missed-attack limits, little traffic can be auto-allowed. |
| [casco CVSS](https://casco.com/blog/jev-cvss-benchmark) | All decision models tested (including Jev) inflate security-finding severity. |
| [v4fs detector](https://github.com/v4fs/awesome-jev-security) | A two-view injection detector (min of attack and intent) reached precision 0.850 / recall 0.911 on 300 rows. |

**Takeaway.** Typed output removes *format* attacks, not *decision* manipulation. The dangerous inputs are **evidence-shaped** (claimed approvals, editor's notes, plausible context), not blunt commands.

## Judging and evaluation

- **[JEV-as-a-Judge, arXiv 2609.26550](https://arxiv.org/abs/2609.26550) (CMU).** Within ~3 pts of the best of 16 judges when the verdict is readable from the text, at **~0.36% of the fee** and a 0.15 s median. Jev falls 9–20 pts behind on JudgeBench and style-adversarial sets, and on math, code and logic. A frozen-threshold cascade was 0.9 pts *more* accurate than GPT-6 at 41% of the fee. RewardBench 92.2% vs 93.5%.
- **[JEV vs LLM Rubric Judges, arXiv 2609.29769](https://arxiv.org/abs/2609.29769) (UPenn).** Jev is competitive on binary checklists and weaker on graded scales. LLM judges cost 29–325× more and took 30–220× longer. **LLMs repeat Jev's confident errors ~96% of the time**, so cascades gain at most 1.5–2 points.
- **[danielgshea/jev-as-a-judge](https://github.com/danielgshea/jev-as-a-judge).** 5 frozen runs × 100 re-scores matched every human pass/fail label (Sonnet 4.6: 80%), with 92–913× less variance, at $0.34 vs $28.17. Only 5 traces, though.
- **LangChain Deep Agents.** A community thread (via [tanxarx](https://github.com/tanxarx/awesome-jev)) reports 100% agreement with human pass/fail over 500 trials at ~1/80 the cost of Sonnet 4.6. See also LangChain's own study, [Can Jev be a better agent evaluator?](https://www.langchain.com/blog/jev-agent-evals-langsmith)
- **[agentjournal.dev](https://agentjournal.dev/blog/llm-judge-vs-feature-extraction/).** 12–14 Jev-scored dimensions with fitted weights beat one direct question (Japanese NLI 0.9076 vs 0.8373), but false positives rose from 1.5% to 37.2% on hard benign samples. Rows at ≥ 0.9 confidence were only 72.2% accurate.
- **[tessl verifiers](https://tessl.io/blog/jev-is-136x-faster-and-27x-cheaper-than-gpt-luna-6-for-tessl-verifiers-try-it-yourself).** 13.6× faster and 2.7× cheaper than GPT Luna 6.
- **Code review.** One study scored 98.0% vs 100% at $0.043 vs $1.94–$11.78 per 1k ([robokrunch digest](https://github.com/robokrunch/awesome-jev)). See also [jev-code-review-benchmark](https://github.com/gemanor/jev-code-review-benchmark) (Jev vs Gemini Flash vs Claude Fable). A 111-case action gate scored Jev 100/111 vs Claude 102/111.

## Search, reranking and RAG

- **[jev-rerank-bench](https://github.com/anessbelbati/jev-rerank-bench).** nDCG@10 **0.692** vs Cohere Rerank 4 Pro 0.691 at 422 ms (8 datasets, 1,617 questions). "Headline averages do not establish a winner."
- **[zhuyansen/jev-search-rerank-eval](https://github.com/zhuyansen/jev-search-rerank-eval).** On 9,831 graded pairs over 164 zh/en queries, Jev alone **does not beat bge-m3**, while fusion adds +0.090 NDCG. It measures judge circularity.
- **Official re-ranking cookbook (CLERC legal).** Top-1 5% → 18%, top-10 38% → 62% (*vendor*).
- **Zilliz evaluations.** [DeepSearcher stopping policy](https://github.com/zilliztech/deep-searcher/blob/master/evaluation/jev_stopping/README.md): 93.25% Recall@5 (a tie), with median decision latency 2.23 s → 0.55 s. MemSearch rerank: 79.41 vs Voyage rerank-3 81.87. Vector Graph RAG: MuSiQue 68.87%, HotpotQA 93.50% Recall@5 ([write-up](https://zc277584121.github.io/rag/2026/09/22/jev-search-deep-evaluation.html)).
- **Tool retrieval.** Jev beat BM25 9× over 3,000+ endpoints. [jevsearch](https://github.com/kylemclaren/jevsearch) reached Hit@1 83% vs Lunr 41%.
- **[jev-rag-benchmark](https://github.com/erendikmenn/jev-rag-benchmark).** Turkish XQuAD, 1,044 queries, with negative results.
- **[Jev-Mem, arXiv 2609.23986](https://arxiv.org/abs/2609.23986).** LoCoMo 0.777 vs a 0.700 baseline (+11%).

## Agents, browsers and computer use

- **[browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast).** Zürich → London Google Flights in **7.1 s for $0.0039**. This is one task and profile repeated, not a reliability benchmark. Browser protocol calls fell from 1,092 to 101.
  - A Browser Use founder retest on **20 complex tasks** found **Jev 1/20 vs GPT-5.6 Luna 17/20**.
  - Another stress test collapsed after ~5 actions.
  - Open issues include stale action IDs.
- **[WindTunnel](https://github.com/nekuda-ai/WindTunnel).** Jev + Mercury 2.5 via WebMCP solved **49/49** web tasks at ~112× lower cost than GPT-6 Astra computer use. **Bare Jev solved 25/49**, because "choosing a valid button ≠ choosing the right next step."
- **[WebJev](https://github.com/lexmount/WebJev).** 38.5% vs 16.7% for Jev 1.13 on 125 real-website tasks.
- **[Ying-Kai-Liao/jev-browser](https://github.com/Ying-Kai-Liao/jev-browser).** 40/42 live-site tasks, ~8k tokens vs ~557k for a Playwright-MCP loop.
- **[jev-browse](https://github.com/kyrylosyzonenko/jev-browse).** 30/30 at a 4.4 s median and $0.0009/task, vs Claude Code at 9.4 s and $0.0679.
- **[typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use).** ~$0.0002 and 0.13–0.38 s per decision, vs $0.032 and 5.2 s for a frontier model ("155× cheaper than Opus 5, ~20× faster").
- **Retriever AI** ([report](https://rtrvr.ai/blog/jev-browser-agent-benchmark)). Faster, but with *higher* total cost (one run per task).
- **[Jev-Mobile, arXiv 2609.30186](https://arxiv.org/abs/2609.30186).** AndroidWorld 79% vs step-wise VLM 84%, with −32.7% time and −73.4% cost.
- **[REFLEX, arXiv 2609.26532](https://arxiv.org/abs/2609.26532).** 95% success with **72.7% fewer** strong-model calls. The advantage over cheap generative cascades is limited, and gains shrink when routing is already accurate.
- **[wuyoscar agent pilot](https://github.com/wuyoscar/jev-skill/blob/main/evals/RESULTS.md).** In 12 paired runs, the baseline scored 12/12 while the Jev-checkpoint arm scored 10/12, at higher cost and time. Advice doesn't help automatically.
- **Tool calls.** [pi-warden](https://github.com/DevMortimer/pi-warden): 6 → 0 rule breaks over 150 paired runs; a replay on 17,000 calls held 42, with ~88% correct at ~250 ms. [hermes-jev-approvals](https://github.com/anpicasso/hermes-jev-approvals): 8.7× faster decisions and 4.4× fewer prompts on 153 real commands. [Archestra](https://archestra.ai/blog/we-tested-jev-on-100-real-agent-calls): 100 real agent calls.
- **Routing.** [jev-codex-router](https://github.com/0xNatoshi/jev-codex-router): ~60% saving on a *backtest* of 237 turns (not real bills). [arXiv 2609.28919](https://arxiv.org/abs/2609.28919): enterprise coding-agent routing estimated at 14–21% savings. [shimo4228/jev-skill-router](https://github.com/shimo4228/jev-skill-router): routing "probably won't help a strong model". [JevRouter](https://github.com/BillionsBobby/JevRouter) Toolathlon: 38–44% vs DeepSeek 24%.

## Games, robotics and control

- **Doom** (*vendor*): ~10 decisions/s at ~$7/hour. **ViZDoom**: navigation at 5 Hz, combat at 12 Hz. Open [NanoJev](https://github.com/TianyuCodings/NanoJev) scored 128/128 vs Jev 56/128 on ViZDoom Basic (author's split), but lost a maze 4/10 vs 7/10.
- **Chess.** 25/100 puzzles for $0.03 vs Astra 68/100 for $11; 3-move puzzles 3/30; from raw FEN, no better than random; ~950 Elo with tactical facts supplied. Legal moves as a Choice make illegal moves impossible ([dev.to](https://dev.to/maximsaplin/typesafe-jev-played-chess-and-landed-next-to-reasoning-models-28ga)).
- **StarCraft II** ([JEV-Star, arXiv 2609.27331](https://arxiv.org/abs/2609.27331)). Beat the Lv7 AI 4/4 with GPT-6 planning, at a 0.422 s median and $3.71/game ($0.15 Jev). **Jev-only never expanded.**
- **Pokémon Red.** 8,000+ decisions for $1.21 and the first gym badge. [jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) is Brier-scored.
- **Other games.** Tetris: 9,200 points at 300 ms/step, but it topped out without a search harness. Poker: 63% agreement with a solver, with inverted confidence and 15–30 pt swings from relabelling. Mario: 229 ms per decision was too slow to clear 1-1 in one attempt.
- **Robotics.**
  - [jev-drone](https://github.com/RomanSlack/jev-drone): Jev advises at 2.5 Hz with a 50 Hz reflex veto; 77.5 m vs a 17.7 m baseline, although an earlier arena showed no advantage.
  - [OpenRoboto MuJoCo](https://github.com/openroboto-ai/jev-robot-control): Jev $0.019 / 182 s vs Astra $5.93 / 707 s.
  - [Cube stacking](https://github.com/FazalAAli/jev-robotics-demo): 19.1 s / $0.0006 vs Opus 5's 158.8 s / $0.75.
  - [RoboJEV](https://github.com/lykycy123/RoboJEV): **rules 48/50 beat Jev 43/50**.
  - Single seed-0 runs are not success rates ([Frank-ZY-Dou/awesome-jev](https://github.com/Frank-ZY-Dou/awesome-jev)).

## Latency and cost measurements

| Source | Measurement |
|---|---|
| [awesome-jev-verified](https://github.com/punk2898/awesome-jev-verified) | Server-side median 248 ms, fastest 189 ms (none under 100 ms in 40 calls); end-to-end median **456 ms**; p99 < 0.8 s (GPT-5.6: 6–7.6 s); 2,390 questions for **$0.049** total |
| [thevibeworks lab](https://github.com/thevibeworks/awesome-typesafe-jev/tree/main/lab) | Floor ~250 ms up to 25 questions; median 310 ms (1 question) → 4.7 s (200 questions); quickstart 424 tokens ≈ $0.000018 |
| [rhc98](https://github.com/rhc98/awesome-jev) (3,683 calls) | Mean 3,235 input tokens/call; p50 210 ms, p90 337 ms; $0.00014/call |
| MichaelLee04 (~5,000 requests) | p50 ~150 ms / p95 ~350 ms, ~$2 |
| Classmethod | 0.643–0.674 s median, $0.000025/call |
| Others | 0.8–1.1 s (RobotsTJ500); 236–276 ms in a pentest harness ([arXiv 2609.28940](https://arxiv.org/abs/2609.28940)); 310–370 ms via Vercel ([yzfly](https://github.com/yzfly/awesome-jev-zh)) |
| Scale examples | 1,018 papers for $0.08 at a 256 ms median ([1kpapers](https://1kpapers.com)); 100,000 posts × 14 Nouls in 20.4 s for $0.67; 22.8M log lines in ~6 min for $0.64 ([Tocsin](https://github.com/TPAteeq/tocsin)); MotherDuck 100k rows in 40 s for $0.50 vs an LLM's 32 min for $37; 38,012 forecasts at a 118 ms median for ~$3 |

**Rule of thumb.** Plan for **~250–500 ms per call**. Expect order-of-magnitude savings only when batching many questions per call or replacing chains of LLM calls. For one question, expect ~1.5–3× vs a small chat model.

## Negative and null results

[kydlikebtc](https://github.com/kydlikebtc/awesome-jev) and [tanxarx](https://github.com/tanxarx/awesome-jev) collect these deliberately. They're worth reading before building:

- **Hermes Agent compaction:** not adopted. Recall was below the existing summariser and tied recency at a matched budget ([scorecard](https://github.com/NousResearch/hermes-agent/blob/main/evals/compaction/results/SCORECARD-2026-09-19-jev.md)).
- **jev-use compaction:** 56.3%, below a constant answerer.
- **fast-jev-compaction replays:** fancier methods didn't clearly beat a head+tail baseline.
- **YTAL entity resolution:** the model stage was 96% cheaper, but fallbacks made the total +4.1% → **not adopted** ([replay](https://ytal.io/blog/typesafe-jev-entity-resolution-production-replay/)).
- **worldmonitor:** tied the incumbent → kept in shadow mode.
- **no-mistakes review pre-brief:** measured, then retired ([PR #1165](https://github.com/kunchenguid/no-mistakes/pull/1165)).
- **hermes-jev-skills:** Jev-summarised handoffs had worse recall than raw transcripts.
- **jev-issue-pulse:** null result at daily cadence.
- **Browser Use retest:** 1/20 on complex tasks.
- **wuyoscar agent pilot:** checkpoints hurt.
- **RoboJEV:** rules beat Jev.
- **jev-orderby-bench:** ORDER BY over probabilities failed 4 of 6 conditions on Amazon ESCI.
- **Janus:** the cascade matched Jev alone at +47% cost on Web of Science.
- **jevlogs:** 0.993 HDFS recall, but only 0.84% of lines filtered out.
- **Trading bots:** none report sustained profit. One lost 300% in 14 h; "70 ms is too slow for HFT."
- **Meta-review ([arXiv 2609.32160](https://arxiv.org/abs/2609.32160)):** across 28 papers, the typed readout shows **no independent accuracy advantage** over comparable label-probability readouts. The clearest gains are latency and cost.

## Benchmark suites and leaderboards

| Suite | What it measures |
|---|---|
| [evals.typesafe.ai](https://evals.typesafe.ai) (*vendor*) + [WorkflowEvals](https://github.com/typesafe-ai/WorkflowEvals) | Four workflows (security incidents, agent-trace observability, invoice processing, customer service). Jev scores 61.7–76.0% against reference labels averaged from two frontier models. |
| [JevBench](https://github.com/fstandhartinger/jevbench) / [Benchmark Heaven](https://benchmarkheaven.com/jev-models) | 534 frozen decisions (half sealed and hashed), 40–77 systems; a composite of intelligence, calibration, speed and cost. Jev 1.13 is at or near #1 (PostHog [Jeeves](https://github.com/PostHog/jeeves) claims 0.935 vs 0.866 on public items). |
| [Jev Decision Index (HF)](https://huggingface.co/spaces/multimodalart/jev-decision-index) | Jev + ~70 reproductions on 43 benchmarks, ~120k decisions per model, chance-corrected. Liquid AI d1 is reportedly #1. |
| [S1Bench](http://bench.jakecuth.com) | 1,999 decisions, 13 sets: Jev 77.5% macro, ECE 0.076. |
| [Jevals.com](https://jevals.com/) ([data](https://github.com/Jevals/jevals-data)) | Jev vs six LLMs on human labels, 300 items × 5 runs. |
| [DecisionBench](https://github.com/Hanno-Labs/decision-bench), [reflexbench](https://github.com/brida-ai/reflexbench), [jev-benchmarks](https://github.com/AbdelStark/jev-benchmarks) | Open harnesses for calibration, framing sensitivity and selective risk. |
| [Image JevBench](https://benchmarkheaven.com/image-jev-bench), [JevPokerBench](https://github.com/Prophetlab/JevPokerBench), [jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas) | Specialty benchmarks and capability maps. |
| Datasets | [LocalLLaMA/typed-decisions](https://huggingface.co/datasets/LocalLLaMA/typed-decisions), [fastino/fast-decisions](https://huggingface.co/datasets/fastino/fast-decisions) (17 domains × 300), [jev-tree-choice-cap](https://huggingface.co/datasets/reachjalil/jev-tree-choice-cap), [instruct-jev](https://github.com/ctaxnagomi/instruct-jev) |

For a reproducible comparison protocol, see [youzizzz1028/Awesome-Jev](https://github.com/youzizzz1028/Awesome-Jev). It compares (1) a classical classifier or encoder, (2) an LLM with native structured output, (3) the same LLM via the official adapter, and (4) Jev, all on identical state and candidates. The protocol also freezes versions and prices and reports a Pareto surface across a four-layer evaluation: structural validity → semantic correctness → probabilistic reliability → decision utility.
