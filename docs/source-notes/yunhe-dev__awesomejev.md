# yunhe-dev/awesomejev
- **One-liner:** Source code for the awesomejev.dev directory website (a fork of the commercial Mkdirs Next.js/Sanity template) plus a design for a "Jev-verified" inclusion pipeline; not itself a list.
- **Language(s):** Chinese (primary, design docs/policy) and English (README intro)
- **Type:** project/code (not a list)
- **Scale:** ~440 files, almost entirely the Mkdirs template (Next.js 14, Sanity CMS, Auth.js, Stripe paid/sponsored submissions, Resend email). Jev-specific content: README intro (2 lines), `docs/jev-native-radar.md` (design draft dated 2026-09-21), `packages/radar/` (ingest → evidence → decide → publish CLI scaffold, policies, fixtures). No actual list entries in the repo — listings live in the Sanity CMS behind the live site https://awesomejev.dev.
- **Quality flags:** No list content to harvest. README is mostly upstream Mkdirs marketing (author OpenFox's products). Paid/sponsored submission support via Stripe → potential pay-to-list/promotional directory. The "Jev" decision engine is a `FakeJevClient` (deterministic rules); real TypeSafe API binding is "out of scope for this scaffold". Sniffer regexes include non-official patterns (`/v1/(choice|score|noul|decide)`, `JEV_API_KEY`) — invented, not documented endpoints.
- **Unique value:** A well-thought-out *design* for evidence-based inclusion ("use Jev to list Jev"): deterministic code sniffers → evidence pack → typed decisions (verify_usage Choice; include Choice + value Score) → optional human gate → publish, with versioned public policy. Useful as a pattern for list curation and as an example of Jev-as-curator.

## Facts claimed about Jev
- Describes Jev as "TypeSafe Jev (System One typed decisions)".
- Sniffer patterns treated as evidence of real usage (repo's own policy `sniffers@v1`): `@typesafe-ai/sdk` import; host `api.typesafe.ai`; model ids matching `jev-…` or `typesafe/jev`; env `TYPESAFE_API_KEY`, `TYPESAFE_BASE_URL`. (Also unverified patterns `/v1/choice|score|noul|decide`, `JEV_API_KEY` — not in official docs as reported elsewhere; official endpoint is `/v1/systemone`.)
- Design doc maps "abstention / Noul" to `needs_review` / `insufficient_evidence` outcomes; uses Score as 0–1 value (official Score is 2–10 ordered levels — a mismatch).
- No pricing, versions, benchmarks or other product facts.

## Key insights / patterns
- Curation pipeline pattern: candidates never publish directly; build a compact auditable EvidencePack (code hits with kind import/api/model_id/config vs separate `readme_claim`, plus red flags `name_only`, `readme_mention_only`, `fork_spam`, `empty_repo`); then two typed calls rather than one giant prompt — (A) verify_usage Choice: code_backed | claim_only | unrelated | insufficient_evidence; (B) include Choice: include | reject | needs_review + value Score, only if A passes.
- Rule: never include on name similarity alone; README claims route to human review.
- Version policies and sniffers publicly so others can reproduce verdicts.
- Stars explicitly not the ranking signal; external awesome lists not used as ground truth.

## Standout entries
- [awesomejev.dev](https://awesomejev.dev) — live directory site built from this repo (directory)
- [Jev-native radar design doc](https://github.com/yunhe-dev/awesomejev/blob/main/docs/jev-native-radar.md) — evidence-based inclusion pipeline design, in Chinese (pattern/tutorial)
