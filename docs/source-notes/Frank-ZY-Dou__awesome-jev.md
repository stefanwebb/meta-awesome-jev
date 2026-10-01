# Frank-ZY-Dou/awesome-jev
- **One-liner:** Rigorously sourced index of ~25 Jev robotics, simulation, 3D/animation and control demos, with quoted claims, archived videos, and a reported-numbers table.
- **Language(s):** English
- **Type:** use-case-collection (niche: robotics / embodied / 3D)
- **Scale:** ~25 X/LinkedIn cases in: Robot control on physical hardware (2); Robot control in simulation (8); 3D modeling, animation and virtual cameras (4); Vehicles, drones and games in simulation (8); Design tools and robotics data (3). Plus Reported numbers (vendor / independent-in-simulation / author-reported), GitHub projects (~17 repos, READMEs read 2026-09-19/20), Directories and coverage (sites, LiteLLM, Langfuse, YouTube videos). 26 archived MP4s + JPG thumbnails (~35 MB).
- **Quality flags:** Very high rigor: every link opened 2026-09-19, claims quoted verbatim, explicitly notes what posts omit (robot model, sim vs real, how images reach the model), distinguishes single runs from success rates. Narrow scope. Snapshot dates Sept 19–20 (stale-ish). Not promotional. Media archived (re-encoded copies — rights note).
- **Unique value:** Only list focused on embodied/robotics use, with honest caveats (Jev is text-only; no hard real-time); comparative sim runs with costs (Jev vs GPT-6 Astra vs Opus 5); verbatim vendor doc quotes (models page, confidence, jaggedness); archived media resistant to link rot.

## Facts claimed about Jev
- First "System One" model from TypeSafe AI, announced **15 September 2026** by founder Diogo Almeida, "available today in early access" (announcement https://x.com/CompleteSkeptic/status/2099925682726002904). Vendor tagline: "a frontier-intelligence function call: unstructured state in, typed probabilistic decisions out." Trained with "Reinforcement Learning for Calibrated Decisions (RLCD)".
- One endpoint `POST /v1/systemone`; Noul ("Returns the probability the answer is yes"), Choice ("chosen option and the full probability distribution"), Score ("Rates the state along a rubric you define"). "Jev supports a cardinality up to 255".
- Input: "Text only. String, JSON object, or array of text values. No image, audio, or video input." Context "64k tokens per request; 32k tokens for state plus the longest question" (models page).
- Version: "Jev 1.13" (`jev-1.13.0`); `jev-latest` points to it; pin a version if thresholds are tuned. JevRouter README cites model id `typesafe/jev-1.13-20260917`.
- Price "$42 / $0.042" per billion / million input tokens, output free; rate limits "250,000 tokens per second / 1,200 requests per minute" (can change without notice).
- "End-to-end response time is 70ms-500ms"; "193.6x Faster, 444.6x Cheaper" from vendor workflow measurements, "on the higher end of real world gains".
- Calibration "is measured across groups of predictions; it does not guarantee that an individual answer is correct." High confidence → act; low → don't act/route.
- Vendor eval: Jev 67.8% agreement, $0.0004, 0.4 s vs Opus 5 73.1%/$0.1761/37.8 s, Sol 74.1%/$0.0836/23.3 s, Terra 67.9%/$0.0304/10.1 s; labels = average of GPT-6 Astra & Claude Fable 5.1 at high thinking.
- As of 2026-09-19, "No peer-reviewed evaluation of Jev was found" on arXiv (later lists cite arXiv papers from late Sept).
- Independent sim numbers: OpenRoboto MuJoCo apple-to-plate: Jev 1.13 placed, 113 cycles, 226 calls, $0.018825, 181.847 s; GPT-6 Astra placed, $5.933624, 707.274 s; GPT-4.1 mini hit 160-cycle limit. Fazal Ali cube stacking: Jev 19.1 s, $0.0006 vs Opus 5 158.8 s, $0.75. Roman Slack drone: 77.5 m vs 17.7 m baseline, 80 calls/65 s, 0.11 s median; earlier simpler arena showed "no advantage for Jev". robokrunch fleet triage: 300/300 decisions, 91.3% team agreement, p50 0.527 s, p95 0.813 s, $0.00737. jevball: 366 ms avg latency, ~1,700 input tokens/call. JevRouter Toolathlon: position-wise hits 38%/44% (Jev) vs 24% DeepSeek V4.1 Flash.
- Author-reported latencies: ~2 decisions/s (SO-101), ~150 ms (Isaac Sin), ~1 s per pick (Askable Arm), 300 ms (drone), 500 ms average with 500 agents at 35 calls/s, 167–305 ms (jev-stage).
- LiteLLM "v1.103.0-rc" (2026-09-20) proxies the endpoint with logging/cost tracking; Langfuse (2026-09-18): score stored traces with Jev — "It gives you no reasoning back."

## Key insights / patterns
- Universal robotics pattern: simulator/app sends structured state (JSON/text/menu of options), Jev returns one typed choice, separate code executes motion. Jev never outputs torques/trajectories; it picks primitives (~30-primitive menus).
- Vision must be converted to text first (Jev is text-only) — e.g., Astra interprets camera views, Jev selects skill and answers unsafe/done.
- Keep a fast reflex/safety layer in code with veto (drone: Jev 2.5 Hz advisory, 50 Hz reflex layer). "Hard real-time control is out of scope entirely… cannot depend on a network request" (systemonemodels.org).
- Chain choices (intent → contact/motion family → input), each informing the next (jev-libero).
- Single seed-0 runs ≠ success rates; several authors report no controlled advantage vs deterministic supervisors.
- Parallel multi-judgment triage (escalate Noul + team Choice + urgency Score) fits ops workloads.

## Standout entries
- [Models page](https://docs.typesafe.ai/models) — limits, pricing, versions (official)
- [Confidence](https://docs.typesafe.ai/confidence) — official confidence semantics (official)
- [openroboto-ai/jev-robot-control](https://github.com/openroboto-ai/jev-robot-control) — MuJoCo Jev vs GPT-6 Astra vs GPT-4.1 mini with results file (benchmark)
- [FazalAAli/jev-robotics-demo](https://github.com/FazalAAli/jev-robotics-demo) — Jev vs Opus 5 arm control (robotics)
- [TarunTomar122/jev-askable-arm](https://github.com/TarunTomar122/jev-askable-arm) — primitive selection on Franka in ManiSkill (robotics)
- [RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone) — advisory Jev + 50 Hz reflex veto (robotics)
- [Dimweaker/jev-libero](https://github.com/Dimweaker/jev-libero) — chained choices on LIBERO (robotics)
- [grmkris/robo-harness](https://github.com/grmkris/robo-harness) — real SO-101 harness with acceptance record (robotics)
- [robokrunch/jev-physical-ai](https://github.com/robokrunch/jev-physical-ai) — fleet incident triage with measured stats (ops)
- [BillionsBobby/JevRouter](https://github.com/BillionsBobby/JevRouter) — tool/model routing with Toolathlon test (agents)
- [systemonemodels.org real-time control](https://systemonemodels.org/use-cases/real-time-and-agents/real-time-control/) — when not to use Jev for control (guide)
- [Langfuse: Using TypeSafe's Jev for evals](https://langfuse.com/blog/2026-09-18-using-typesafes-jev-for-evals) — trace scoring (integration)
- [LiteLLM: TypeSafe Jev](https://docs.litellm.ai/blog/typesafe_jev) — proxy support (integration)
- [Sam Witteveen: Jev – The Ultimate Classification Model?](https://www.youtube.com/watch?v=X117w2Rark8) — video overview (video)
- [jevable.com](https://jevable.com/) — independent curated collection (directory)
