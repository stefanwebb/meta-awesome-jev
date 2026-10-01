# Open Replications, Local Runtimes and Competitors

> Jev is closed-weight and hosted-only. Within **48 hours** of launch, the community began shipping open "Jev-like" decision models and `/v1/systemone`-compatible servers. Latent Space counted 6 clones in 2 days, another count found 11 clones with 10k+ stars within 5 days, and the source lists now track 400+ repos. This page maps that landscape.
>
> ★ = GitHub stars verified 2026-09-30 · 📚 = number of source lists citing it. Benchmark numbers are **self-reported by each project** unless linked to an independent study.

[← back to the main list](../README.md)

## First, the caveats that every careful list repeats

1. **Wire compatibility is not behavioural equivalence.** Many projects serve `POST /v1/systemone`, so the official SDK works unchanged if you set `TYPESAFE_BASE_URL`. That makes them *drop-ins for your code*, not for Jev's accuracy or calibration.
2. **Raw logits are not calibrated probabilities.** Most clones read option-token logits from an open LLM in a single forward pass. Without temperature scaling, isotonic regression or a conformal method, those numbers are not calibrated.
3. **"Beats Jev" claims are usually in-distribution.** One analysis found clone scores of 0.769 in-distribution vs 0.541 OOD. Kev scored −1.8 pp in-distribution but **−19.1 pp** OOD vs Jev. Compare zero-shot against zero-shot.
4. **Check the weight licence separately from the code licence.** JevNext is under PolyForm Noncommercial, and several Apache/MIT repos ship non-commercial weights.
5. **Check for silent upstream fallbacks.** Some local proxies (stuntd) fall back to paid hosted Jev when unsure.
6. **Many "RLCD" labels are really cross-entropy or Brier losses plus temperature scaling.** Genuine RL examples include Decider (PPO + a log-score term), eve-rlcd (REINFORCE) and Laya (policy gradient). TypeSafe's own RLCD is unpublished. ([Zhao-Tian-yi/awesome-jev](https://github.com/Zhao-Tian-yi/awesome-jev) has the analysis.)
7. **Some published weights didn't work.** One model's weights were missing their classification head and answered at random (per [mrjev.com](https://mrjev.com/best-jev-tools/)). Run your own eval.

## How the clones work (a three-axis taxonomy)

From [Zhao-Tian-yi/awesome-jev](https://github.com/Zhao-Tian-yi/awesome-jev), [KuzanJ/awesome-jev](https://github.com/KuzanJ/awesome-jev) and [notsointresting/awesome-jev-family](https://github.com/notsointresting/awesome-jev-family). "Does not generate text" identifies none of these axes on its own:

| Axis | Variants | Examples |
|---|---|---|
| **Backbone** | causal LLM · encoder (ModernBERT/mmBERT) · masked diffusion LM · hybrid | Qwen3.5 (Kev, Decider), ModernBERT (Laya, Von, Verdict), DiffusionGemma (openjev) |
| **Readout** | option/letter-token logits · trained pointer or decision head · option-wise scalar scorer · encoder option markers · diffusion answer slots | SemIf (logits), Kev (pointer head), jevlike/JevForge (scorer), Laya/Von (markers), openjev (slots) |
| **Schedule** | one forward pass per question · batched rows · **shared-prefix branches** (prefill once, fork per question) · native slots | SemIf (prefill the prefix, duplicate the KV cache), openjev-sglang (prefill-only) |

A "Jev in 25 lines" explainer ([nobodywho](https://www.nobodywho.ai/posts/jev-in-25-lines/)), [sgnt.ai: You could have built Jev](https://sgnt.ai/p/jev/) and [Allan Boll's logprob wrapper](http://allanrbo.blogspot.com/2026/09/a-jev-like-wrapper-for-llms-including.html) show the minimal version. Sean Goedecke ([post](https://www.seangoedecke.com/jev-means-structured-output-is-interesting-again/)) found that prefilling an LLM and sampling one constrained token recovers 2–3× speedups. The open question is whether RLCD calibration, rather than the interface, is TypeSafe's real moat.

## Trained open decision models

| Model | ★ | 📚 | What it is | Reported numbers |
|---|--:|--:|---|---|
| [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 29,237 | 38 | Convai Innovations; non-autoregressive ModernBERT/mmBERT encoder (421M English / 322M multilingual, 100+ languages, up to 8k context); Apache-2.0; [HF](https://huggingface.co/convaiinnovations/laya-multilingual), `pip install laya`, [site](https://laya.convaiinnovations.com/) | ~33 ms per forward pass; 7.2 ms/question batched. Independent checks: AG News Laya 92.8% vs Jev 85.5%, but emotion 54.0% vs 61.5% ([yzfly](https://github.com/yzfly/awesome-jev-zh)); another study found 0.590 vs 0.974; RFQs 78.0% with ECE 0.322. Base checkpoints are fine-tune bases, and "Choice labels written as yes/no/true/false are unsafe". |
| [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | 8,057 | 57 | Qwen3.5/3.8 (0.8B–27B; early checkpoints on Qwen2.5-0.5B), LoRA + pointer head, per-checkpoint temperature file, `/v1/systemone` server | Kev-9B is ~3.5 pts behind Jev on unseen sources; kev-4b 0.790 vs Jev 0.857 (764 items); −19.1 pp OOD |
| [TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) | 2,453 | 60 | 0.6B nano replica with an end-to-end training pipeline and an [RLCD experiment](https://github.com/TianyuCodings/NanoJev/blob/618cea6d906d54e128360786d12f703fff2b1245/docs/RLCD_EXPERIMENT.md) | ViZDoom Basic 128/128 vs Jev 56/128 (a game-specific specialist) |
| [bespokelabsai/nimble](https://github.com/bespokelabsai/nimble) | 1,981 | 21 | Bespoke Labs 9B open recipe: LoRA, contrastive data curation, constrained serving; runs on Ollama 0.35 | 90.1% vs Jev 93.2% on a 324-example holdout |
| [vinnylarouge/jevlike](https://github.com/vinnylarouge/jevlike) | 1,335 | 57 | A training library for models that score a variable list of options in one pass (Doom/chess demos) | "Not a reproduction of RLCD" |
| [feder-cr/jev](https://github.com/feder-cr/jev) (jevos) | 1,133 | 26 | 1B MiniCPM5, GGUF, CPU-only, **Noul only** | 0.815 vs hosted Jev 0.927 on 2,000 yes/no questions |
| [Mapika/decider](https://github.com/Mapika/decider) | 993 | 45 | Qwen3.5 family 0.8B–35B MoE; PPO + belief scoring; checkpoints and server | djev variant is 3rd on JevBench v1.2; the 0.8B fell under a constant-answer baseline on long state |
| [wfzyx/von](https://github.com/wfzyx/von) | 794 | 48 | 395M ModernBERT-Large; sub-15 ms; v1.2 is option-order invariant | ViZDoom Defend the Center 9.00 vs Jev 5.62 kills, but 72.0% vs Jev 96.6% on a 49-task suite |
| [Rizzo-AI-Academy/rizzo-flow](https://github.com/Rizzo-AI-Academy/rizzo-flow) | 770 | 24 | Typed decisions from an LLM without generation | 0.648 vs Jev 0.727; ships uncalibrated |
| [Liuziyu77/Valen](https://github.com/Liuziyu77/Valen) | 571 | 16 | Multimodal (text/image/video) Jev-like training | Hosted Jev is text-only |
| [Zefan-Cai/Open-Jev](https://github.com/Zefan-Cai/Open-Jev) | 377 | 19 | 27B open Jev implementation | |
| [PostHog/jeeves](https://github.com/PostHog/jeeves) | 336 | 9 | 9B; "reasoning improves Jev-like decision models" (~0.3 s, 3.3 s with thinking on H100) | Claims 0.935 vs Jev 0.866 on public JevBench items; Jev leads on MMLU-Pro |
| [Heman10x-NGU/openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0) / [Verdict-open-jev](https://github.com/Heman10x-NGU/Verdict-open-jev) | 293 / 109 | 32 / 27 | 151M ModernBERT with conformal abstention and a WebGPU playground | Claims 77.10% accuracy / 0.0144 ECE, "beating Jev & Laya" (unverified); 3.0% of predictions flip under reordering |
| [togethercomputer/tev1](https://github.com/togethercomputer/tev1) | 183 | 8 | Together AI "train your own for $17"; [Tev1-4B-experimental](https://huggingface.co/togethercomputer/Tev1-4B-experimental) | |
| [kshetrajna12/reflex](https://github.com/kshetrajna12/reflex) | 159 | 31 | Small Qwen3.5 decision model; in-browser WebGPU; documents what *didn't* help | Reflex-4b 72.0% at 10 dec/s on S1Bench |
| [allebee/jevk5](https://github.com/allebee/jevk5) | 125 | 23 | Apache-2.0 weights; reads >16 options in several passes | 0.775 on hard-tier evals |
| [OmniJev/OneJev](https://github.com/OmniJev/OneJev) / [PlayJev](https://github.com/OmniJev/PlayJev) | 64 / 45 | 16 / 33 | Multimodal System One 0.8B–27B; 0.8B GUI game player from pixels | |
| [iapp-technology/openthai-systemone](https://github.com/iapp-technology/openthai-systemone) | 65 | 13 | Thai/English 0.8B, 256-way slot head, Apache-2.0 | |
| [scienthoon/luce](https://github.com/scienthoon/luce) | 7 | 10 | Describe a task, then train your own decision head | |
| Others | | | [hiroki-abe-58/sokudan](https://github.com/hiroki-abe-58/sokudan) (Japanese 314.6M, bool AUROC 0.844), [alperiox/audio-jevlike](https://github.com/alperiox/audio-jevlike) (Prosodia, audio-native), [lexmount/WebJev](https://github.com/lexmount/WebJev) (browser-agent decision model), [arnabgho/rlcd-lite](https://github.com/arnabgho/rlcd-lite) (GRPO + Brier: proper scoring rules produce calibration, binary rewards destroy it), [anthony-maio/eve-rlcd](https://github.com/anthony-maio/eve-rlcd), [akash-kamat/system-one-gemma](https://github.com/akash-kamat/system-one-gemma), [mithalouni/system-one-open](https://github.com/mithalouni/system-one-open), [zwliJay/jev-forge](https://github.com/zwliJay/jev-forge), [daseinlabs/open-jev](https://github.com/daseinlabs/open-jev), [ikermoel/open-alternative-jev](https://github.com/ikermoel/open-alternative-jev) (72% vs 21% on the same items with option order flipped: order sensitivity), [Bring-AI/JevNext](https://github.com/Bring-AI/JevNext) (numerical decoding; non-commercial) | |
| Hugging Face only | | | [AutoTrust JEV-27B](https://huggingface.co/autotrust/JEV-27B) (Qwen3.8-27B distilled from Jev 1.13 distributions; self-run six-benchmark mean 84.07 vs Jev 83.85; top-1 agreement ~90.5%; Apache-2.0), [GLiNER2.5-Decide](https://huggingface.co/fastino/GLiNER2.5-Decide) (340M), [CUA-S1-FORMS](https://huggingface.co/cua-ai/cua-s1-forms) (706K params, 99.7% vs Jev 83.6% on its own form eval: specialists win at home), [Jev-Omni](https://huggingface.co/akhilaaa3/Jev-Omni) (Gemma 4 12B multimodal), [Bosun v3.1](https://huggingface.co/Hanno-Labs/bosun-v3.1-1.7b) | |

## Training-free readouts over any open LLM

| Project | ★ | 📚 | Approach |
|---|--:|--:|---|
| [TheoLeeCJ/SemIf-OpenJev](https://github.com/TheoLeeCJ/SemIf-OpenJev) (formerly OpenJev/SemIf) | 4,615 | 63 | "Semantic ifs" on a 3090: prefill a shared prefix, duplicate the cache, batch suffixes ([METHOD.md](https://github.com/TheoLeeCJ/SemIf/blob/master/docs/METHOD.md)); 0.845 agreement vs Jev's 0.883 |
| [nokia-applied-research/AnyJev](https://github.com/nokia-applied-research/AnyJev) | 986 | 32 | Hidden-state decisions over any LLM with **option-order correction** (order flips 0.230 → 0.073) and recalibration (ECE 0.240 → 0.095); vLLM |
| [featherless-ai/simple-jev](https://github.com/featherless-ai/simple-jev) | 575 | 40 | Any open model as a classifier/Jev endpoint via next-token logits |
| [razorback16/openjev](https://github.com/razorback16/openjev) | 548 | 49 | Jev-compatible server on **DiffusionGemma** (masked answer slots); 198/201 vs Jev 191/201 (self-run) |
| [Yinsongxu/LLM2Jev](https://github.com/Yinsongxu/LLM2Jev) | 377 | 28 | Local LMs → Jev-style decisions from text and images, prefill only |
| [ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang) | 335 | 48 | Prefill-only Jev-compatible endpoint on SGLang (Qwen3.6-35B-A3B) |
| [hr98w/jev-visual](https://github.com/hr98w/jev-visual) | 303 | 39 | Educational visual Jev-like inference on Apple Silicon (does *not* call hosted Jev) |
| [bnsd55/jevmlx](https://github.com/bnsd55/jevmlx) | 68 | 42 | Parallel constrained decisions for any MLX model |
| [kikoncuo/jevfire](https://github.com/kikoncuo/jevfire) | 71 | 26 | Jev-inspired parallel decisions for CUDA LLMs, with a vLLM API (~71 ms/action) |
| [r-ms/mini-jev](https://github.com/r-ms/mini-jev) | 57 | 29 | **Pre-registered**: letter-logit readout on frozen Qwen3-4B vs grammar-constrained JSON (0.909 vs Jev 0.907 over 6,750 observations) |
| [zhengxuyu/litjev](https://github.com/zhengxuyu/litjev) | 45 | 33 | Any Qwen model behind the `/v1/systemone` schema |
| [TypeLLM/pijev](https://github.com/TypeLLM/pijev) | 34 | 11 | Permutation-invariant wrapper (averages over option orders) |
| Also | | | [vllm-project/vllm#57250](https://github.com/vllm-project/vllm/pull/57250) (DiffusionGemma behind `/v1/systemone`), [Knowledgator/GLiClass](https://github.com/Knowledgator/GLiClass) (single-pass zero-shot label scorer) |

## Local runtimes and compatible servers

| Project | ★ | 📚 | Notes |
|---|--:|--:|---|
| [mizorewww/laya-mlx](https://github.com/mizorewww/laya-mlx) | 6,654 | 23 | Native MLX runtime for Laya: 7–14 ms short decisions on M3 Max; 63/63 parity |
| [ollaya-dev/ollaya](https://github.com/ollaya-dev/ollaya) | 1,032 | 24 | "Ollama for decision models" (Rust, ONNX Runtime + llama.cpp); serves Laya, Decider, NLI and GLiClass behind `/v1/systemone`, `/v1/decisions` and `/v1/models`, plus an MCP server. Its Winnow-E4B scores 0.722 vs Jev 0.738 on Ollaya's benchmark, at 89 ms for 5 questions on an RTX 4090. |
| [githubnext/localjev](https://github.com/githubnext/localjev) | 803 | 16 | GitHub Next: local `/v1/systemone` for Bun on DiffusionGemma ("wire-compatible, but not mathematically equivalent") |
| [receptron/laya](https://github.com/receptron/laya) | 661 | 20 | Laya from Node/TypeScript via ONNX Runtime |
| [logan-markewich/jeff](https://github.com/logan-markewich/jeff) | 274 | 35 | Self-hosted drop-in powered by a 400M GliFormer (75.5% vs Jev 90.5%). *Note:* `jeff check .` was observed sending `.pem` files and passwords. |
| [bladedevoff/stuntd](https://github.com/bladedevoff/stuntd) | 42 | 22 | Local proxy that learns your app's decisions and answers with a Laya head; **falls back to upstream when unsure** |
| [chengyongru/fastjev](https://github.com/chengyongru/fastjev), [chaitin/Decis](https://github.com/chaitin/Decis), [us/jev-local](https://github.com/us/jev-local), [yzfly/edgejev](https://github.com/yzfly/edgejev) | | | Self-hosted multi-backend System One APIs; EdgeJev is CPU/ONNX INT8. Use QInt8, not QUInt8, on x86 VNNI, because dynamic int8 makes outputs batch-dependent. |
| [mandu5/jevcompat](https://github.com/mandu5/jevcompat) | | 6 | **Conformance suite** for Jev-compatible servers: spec, runner, proxy, mock, GitHub Action |

## Hosted competitors

| Model | Vendor | Notes |
|---|---|---|
| **OpenAI Decisions API** | OpenAI (DevDay 2026, limited preview) | Luna-based; text and image with a fixed answer set; ~150–230 ms; no pricing at preview ([The New Stack](https://thenewstack.io/openai-decision-api-luna/)). Beat Jev on some Every tests (76/78 vs 73/78) and lost others. |
| **Liquid AI d1** | Liquid AI (2026-09-29) | Serves `POST /decisions/v1/systemone` and works with the TypeSafe SDKs; free tier `d1:free`; reportedly #1 on the Jev Decision Index ([docs](https://docs.liquid.ai/lfm/models/decision-models)) |
| **Solar Decide** | Upstage | Same `/v1/systemone` schema; 512K context; Choice limited to 26 single-token letters ([console](https://console.upstage.ai/api/systemone)) |
| **Span-01** | Respan | Behaviour-monitoring decision model on [OpenRouter](https://openrouter.ai/respan/span-01) |
| Hanzo Kai, CLM (frozen Qwen3-8B + 20M heads; "Jev parity, up to 9× lower latency", unverified), Drex (NaceAI, $0.04/1M input), Julia 1 | various | [andyrewlee/awesome-system-one](https://github.com/andyrewlee/awesome-system-one) tracks the whole class |

OpenRouter's [Decisions API](https://openrouter.ai/docs/api/api-reference/alphadecisions/submit-a-decisions-questions-and-answers-request) serves Jev, Solar Decide, Span-01 and Kev-4B under one `state` + `questions` shape.

## Where to track this

- [HF Jev Reproductions Tracker](https://huggingface.co/spaces/multimodalart/jev-reproductions-tracker)
- [HF Jev Decision Index](https://huggingface.co/spaces/multimodalart/jev-decision-index), which ranks Jev plus ~70 open models on 43 benchmarks.
- [laya-ai.com system-one-models](https://laya-ai.com/system-one-models), a comparison table. It is Laya-affiliated and mirrored by [yanng981/awesome-system-one](https://github.com/yanng981/awesome-system-one).
- Source lists that specialize in open models:
  - [notsointresting/awesome-jev-family](https://github.com/notsointresting/awesome-jev-family)
  - [mturac/awesome-jev-alternatives](https://github.com/mturac/awesome-jev-alternatives)
  - [KuzanJ/awesome-jev](https://github.com/KuzanJ/awesome-jev), which has a licence audit and an implementation comparison in `docs/MODELS.md`.
  - [Zhao-Tian-yi/awesome-jev](https://github.com/Zhao-Tian-yi/awesome-jev), for architecture and training.
  - [sfmqrb/awesome-decision-models](https://github.com/sfmqrb/awesome-decision-models), for the Laya ecosystem.
  - [rupeshpoojary9/awesome-open-system-one](https://github.com/rupeshpoojary9/awesome-open-system-one), for lineage.
- Full list: [catalog/open-models.md](../catalog/open-models.md) (1,100+ entries).

## Classical baselines you should compare against

Before choosing any decision model, benchmark against:
- [SetFit](https://github.com/huggingface/setfit)
- [fastText](https://github.com/facebookresearch/fastText)
- [semantic-router](https://github.com/aurelio-labs/semantic-router)
- [RouteLLM](https://github.com/lm-sys/RouteLLM)
- a ModernBERT or bge-small + logistic regression head
- [MAPIE](https://github.com/scikit-learn-contrib/MAPIE) and [net:cal](https://github.com/EFS-OpenSource/calibration-framework) for calibration and conformal prediction
- a constant-answer baseline (several open models fail it on long states)

Intent datasets with out-of-scope examples, such as CLINC150, are the standard test for abstention.
