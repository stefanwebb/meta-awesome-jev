# v4fs/awesome-jev-security
- **One-liner:** Not a list: two small Python scripts using the official TypeSafe SDK — a security-report triage example and a prompt-injection detector evaluated on a 5,000-row benchmark.
- **Language(s):** English (code)
- **Type:** project/code (not a list)
- **Scale:** 2 scripts (51 + 183 lines), pyproject (deps `typesafe-sdk>=0.7.0`, `datasets`; Python ≥3.14), README is two `uv run` command lines. `.claude/settings.json` enables the `typesafe@typesafe-ai` Claude Code plugin.
- **Quality flags:** Misleadingly named "awesome" (no curated links at all). README has no prose. But the code is real, clean and informative; reported precision/recall numbers are in code comments (300-row sample), not reproducible without keys and gated HF dataset.
- **Unique value:** A concrete, well-designed **prompt-injection detector recipe** on Jev with tuned thresholds and measured precision/recall; a minimal SDK usage example showing the real Python API surface (`Choice`, `Noul`, `Score`, `TypeSafeClient`, `RetryPolicy`, `response.choices/nouls/scores`, `model_dump()`).

## Facts claimed about Jev
- Python SDK `typesafe-sdk` ≥0.7.0; import `from typesafe_sdk import Choice, Noul, Score, TypeSafeClient, RetryPolicy`; `client.system_one(state=..., questions=...)`; answers via `response.choices[...]` (`.choice`, `.confidence`, `.probabilities`), `response.nouls[...].noul`, `response.scores[...]` (`.score`, `.confidence`); `response.model`; `response.model_dump()["answers"]` (Pydantic model, consistent with 0.7.0 Pydantic switch reported by cobanov).
- `Choice(instructions=..., criteria={label: description})`; `Score(instructions=..., criteria=[ordered level descriptions])`; `Noul(instructions=...)`.
- `RetryPolicy(max_retries=4, timeout=30)`: per code comment, the SDK retries timeouts, connection errors, 408/429 and 5xx with backoff.
- API key via `TYPESAFE_API_KEY` in env; official Claude Code plugin `typesafe@typesafe-ai`.
- Prompt-injection detection on `rogue-security/prompt-injections-benchmark` (test split 5,000 rows, benign|jailbreak), 300-row sample: threshold min(P_attack, P_intent) ≥ 0.3 → **precision 0.850, recall 0.911** (F1 optimum); attack-only ≥ 0.6 → precision 0.814, recall 0.919; mean ≥ 0.4 → precision 0.796, recall 0.944.

## Key insights / patterns
- Two-view detection: ask a technique Choice (attack_type incl. `not_malicious`) and an intent Choice (user_intent incl. `legitimate`); derive P(malicious) = 1 − P(benign option) for each; flag only when the *minimum* exceeds threshold — the intent question vetoes fiction/role-play false positives while the attack question drives recall.
- Use full `probabilities` rather than argmax/confidence to compute a malice score; tune threshold on labeled data for the precision/recall tradeoff.
- Nudge recall in instructions ("better to pick an attack type than not_malicious if unsure").
- Rich criteria definitions per option (instruction_override, persona_jailbreak, prompt_leak, embedded_injection, harmful_request, obfuscation) — descriptions carry the semantics.
- Score levels written as concrete situations (Harmless / Suspicious / Manipulative / Dangerous).
- Concurrency with ThreadPoolExecutor (8 workers) and SDK retry policy for batch evaluation.
- Triage example: one request combining Noul (is security report), Choice (vuln class with `other`), Score (severity 5 levels).

## Standout entries
- [jev-prompt-injection-detection.py](https://github.com/v4fs/awesome-jev-security/blob/main/jev-prompt-injection-detection/jev-prompt-injection-detection.py) — two-view prompt-injection detector with measured P/R (security)
- [jev-triage.py](https://github.com/v4fs/awesome-jev-security/blob/main/jev-sec-triage/jev-triage.py) — minimal SDK security-report triage (example)
- [rogue-security/prompt-injections-benchmark](https://huggingface.co/datasets/rogue-security/prompt-injections-benchmark) — gated 5,000-row benchmark used (dataset)
