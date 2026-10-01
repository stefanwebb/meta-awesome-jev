# karozi/awesome-jev-resources
- **One-liner:** Small beginner-oriented Jev resource list for practitioners and PMs: two Substack explainers by the maintainer, official docs, one paper, and ~12 community projects.
- **Language(s):** English
- **Type:** curated-list (small)
- **Scale:** ~20 links. Sections: Start here, Official documentation, Research and ecosystem analysis, Community projects and demos (Jev integrations and AI agent tools; Local decision model alternatives), Contribute.
- **Quality flags:** Promotional — "Start here" leads with the maintainer's own Substack (Product with Attitude, Karo Zieminski). Otherwise accurate, concise descriptions; mostly duplicates well-known projects found in larger lists. Tiny.
- **Unique value:** PM-friendly framing; a Jev + agent-security explainer (separating risk judgments from permissions/policy/human review); cites the "Jev in the Wild" ecosystem paper with a project count.

## Facts claimed about Jev
- Jev is TypeSafe's System One model for fast, structured decisions; returns a choice, score, or probability. Question types: Choice, Score, Noul (docs.typesafe.ai/primitives).
- Quick start covers playground, API, Python SDK, or coding-agent skill.
- "Jev in the Wild" (arXiv 2609.30216) analyzes **2,170 public GitHub Jev projects** (compare daftAI2026's radar badge of 2,188 projects).
- feder-cr/jev: offline CPU llama.cpp alternative, yes/no only.

## Key insights / patterns
- Keep Jev risk judgments separate from permissions, policy enforcement and human review in agent workflows.
- Contribution rules: disclose affiliation, flag paid resources.

## Standout entries
- [TypeSafe documentation](https://docs.typesafe.ai/introduction) — official intro (official)
- [Confidence](https://docs.typesafe.ai/confidence) — using confidence to decide whether to act (official)
- [Jev in the Wild](https://arxiv.org/abs/2609.30216) — ecosystem analysis of 2,170 GitHub projects (paper)
- [Jev and AI agent security — Product with Attitude](https://karozieminski.substack.com/p/jev-ai-agent-security) — security framing (article)
- [What is Jev? Costs, examples, and getting started](https://karozieminski.substack.com/p/what-is-jev-cost) — intro (article)
- [Jevable](https://jevable.com/) — demo gallery (directory)
- [thruwire/foreman](https://github.com/thruwire/foreman) — Jev supervisor for Codex/OpenCode agents (agent tooling)
- [superagents-lab/jev-search](https://github.com/superagents-lab/jev-search) — Jev-driven web search (app)
- [feder-cr/jev](https://github.com/feder-cr/jev) — offline CPU yes/no alternative (alternative)
