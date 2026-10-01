# Faizullah9181/jev-esketcher
- **One-liner:** Generative painting app where Jev chooses paint materials/palettes for selected sketch regions; FastAPI + React, with mock and real Jev modes.
- **Language(s):** English
- **Type:** project/code (not a list)
- **Scale:** Single application (~220 files): 105 procedural sketches in 21 categories, 121 paint materials in 13 behaviours, 7 palettes. Demo at esketcher.faiz-ai.dev (gallery, 2:50 film).
- **Quality flags:** Real, substantial, well-documented project; not a list. Demo site runs without Jev when backend down. Includes a before/after measurement with real Jev.
- **Unique value:** A thorough reference implementation of a production-ish Jev integration: provider abstraction (mock vs real with same wire format), key never reaching browser, layered abuse/rate limits and daily paid-decision budget, confidence banding, retry with rejected options, candidate-field construction, and explicit documentation of what TypeSafe does/doesn't publish about Jev internals.

## Facts claimed about Jev
- Endpoint `POST https://api.typesafe.ai/v1/systemone`; bearer `TYPESAFE_API_KEY`; `TYPESAFE_BASE_URL` default `https://api.typesafe.ai`; `GET /v1/models` lists models (`jev-latest`, `jev-preview`); decisions report model e.g. `jev-1.13.0`.
- "Inside Jev" (per TypeSafe docs as summarized): each question answered in one **parallel-sampler** query, isolated against the same state; every answer is a probability distribution over declared options; choice = argmax; **confidence = (n·p_max − 1)/(n − 1)** (0 when uniform, 1 when all mass on one option); **RLCD = Reinforcement Learning for Calibrated Decisions** trains probabilities against real outcomes. Architecture, reward, loss, weights unpublished.
- Measured: a 12-board desk ≈ 37 decisions ≈ **70k input tokens** in real mode. Colour harmony with palette + harmony-aware candidates + colour words: harmonious pairs 0.65 → 0.94.
- Operational: 8 s timeout, one retry on 5xx/429/network; app caps ≤16 candidates per decision.

## Key insights / patterns
- Everything around the distribution is deterministic code: build a finite, described candidate field (10 by default, ≤2 per behaviour, one contrasting wildcard), ask Choice, restrict/renormalize probabilities to candidates, rank.
- Confidence bands: confident ≥ 0.55, uncertain < 0.35, leaning between; auto-apply at leaning+, wait for user on uncertain ("Apply anyway / Try another / Pick manually").
- Richer option descriptions (named hues, warm/cool, traits) and harmony rules in instructions materially improve outcomes.
- Hierarchical decisions: first a palette per board, then per-region material conditioned on palette and already-painted colours (feed results back into state).
- Group identical sub-decisions (one question per region kind) to cut calls.
- "Try another" = re-ask with rejected winner removed and told which were rejected.
- Mock provider that mimics distributions (seeded noise, softmax temperature, same confidence formula) for offline dev/demo; never invent decisions when Jev is offline.
- Cost safety: per-IP minute/day limits + global daily paid-decision budget + TypeSafe dashboard spend limit (only ceiling that survives restarts).

## Standout entries
- [Jev eSketcher demo](https://esketcher.faiz-ai.dev) — live generative painting app (app)
- [Gallery](https://esketcher.faiz-ai.dev/gallery) — paintings and demo film (demo)
