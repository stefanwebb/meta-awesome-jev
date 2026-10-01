#!/usr/bin/env python3
"""Render catalog/*.md and data/catalog.{json,csv} from the built catalog.

Inputs:  .cache/catalog_raw.json (scripts/build_catalog.py)
         data/verified.tsv       (scripts/verify_github.sh, optional)
Outputs: catalog/README.md, catalog/<category>.md, data/catalog.json, data/catalog.csv
"""
import collections
import csv
import datetime as dt
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'data')
OUT = os.path.join(ROOT, 'catalog')

CATS = [
    ('official', 'Reference Docs & SDKs (Jev)', 'The /v1/systemone reference: docs, SDKs, cookbooks and evals published alongside Jev, the first Jev-like model.'),
    ('sdk', 'SDKs, Clients & Framework Integrations', 'Unofficial clients in every language, framework adapters (LangChain, LlamaIndex, DSPy, Vercel AI SDK, n8n …) and gateways.'),
    ('mcp', 'MCP Servers', 'Model Context Protocol servers that expose Choice / Noul / Score decisions to agents.'),
    ('skills', 'Agent Skills & Plugins', 'Skills and plugins for Claude Code, Codex, pi, Hermes, OpenClaw, Cursor and similar agent harnesses.'),
    ('routing', 'Routing, Cascades & Orchestration', 'Model routers, confidence-gated cascades, triage and dispatch layers.'),
    ('agents', 'Agents & Decision Workflows', 'Agents and workflows that use a Jev-like model as the fast decision step.'),
    ('security', 'Guardrails, Safety & Moderation', 'Guardrails, tool-call gates, moderation, spam/phishing/fraud detection and robustness work.'),
    ('memory', 'Context, Memory & Compaction', 'Context compaction, memory control, reranking, RAG passage filtering and caching.'),
    ('browser', 'Browser, Desktop & Computer Use', 'Browser agents, computer-use, mobile/GUI agents and extensions.'),
    ('dev', 'Developer Tools & Coding Workflows', 'Code review, commit/CI gates, CLIs, editor integrations and devops tooling.'),
    ('data', 'Data, Databases & Documents', 'Classification, labeling, extraction, search, SQL/Postgres/graph integrations and document triage.'),
    ('bench', 'Benchmarks, Evals & Calibration', 'Independent benchmarks, eval harnesses, calibration tools and head-to-head comparisons of Jev-like models.'),
    ('open-models', 'Jev-like Models: Open, Local & Hosted', 'The model family: open-weight decision models, distillations, local /v1/systemone servers (vLLM, SGLang, MLX, llama.cpp) and decision heads.'),
    ('games', 'Games, Robotics & Simulation', 'Game-playing agents, emulators, robotics, drones and simulations.'),
    ('finance', 'Finance, Trading & Commerce', 'Trading bots, prediction markets, tax/invoice processing and e-commerce.'),
    ('apps', 'Apps & Domain Applications', 'End-user apps: email, calendar, voice, smart home, health, legal, education, marketing, support.'),
    ('papers', 'Research Papers', 'arXiv and other papers about Jev-like (System One) decision models, and the calibration / routing literature they build on.'),
    ('learn', 'Tutorials, Articles & Videos', 'Guides, blog posts, notebooks, courses and videos.'),
    ('community', 'Community, Discussions & Social', 'X/Twitter threads, Hacker News, Reddit, and other public discussion.'),
    ('awesome', 'Other Awesome Lists & Directories', 'Directories, galleries and awesome lists beyond the tracked sources.'),
    ('other', 'Everything Else', 'Entries the classifier could not place confidently.'),
]
TIERS = [(10, 'Consensus', 'cited by 10+ lists'), (5, 'Established', 'cited by 5–9 lists'),
         (3, 'Emerging', 'cited by 3–4 lists'), (1, 'Long tail', 'cited by 1–2 lists')]
JUNK = re.compile(r'localhost|127\.0\.0\.1|example\.(com|org)|xxxx|your[-_]?(user|org|name)|<|\{|\$\{|/path/to|mailto:', re.I)


def load_verified():
    v = {}
    p = os.path.join(DATA, 'verified.tsv')
    if not os.path.exists(p):
        return v
    for line in open(p, encoding='utf-8'):
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 6:
            continue
        url, code_eff, stars, updated, archived, desc = parts[:6]
        code, _, eff = code_eff.partition(' ')
        desc = html.unescape(re.sub(r'\s*Contribute to [^ ]+ development by creating an account on GitHub\.?$', '', desc)).strip()
        desc = re.sub(r'\s+-\s+[\w.-]+/[\w.-]+$', '', desc)
        if re.match(r'^(GitHub is where people build software|Contribute to )', desc):
            desc = ''
        v[url.lower()] = dict(code=code, final=eff, stars=int(stars) if stars else None, updated=updated[:10],
                              archived=bool(archived), gh_desc=desc)
    return v


def md_escape(s):
    return s.replace('|', '\\|').replace('[', '(').replace(']', ')').replace('\n', ' ').strip()


def line(e, long_tail=False):
    title = md_escape(e['title']) or e['url']
    bits = [f"[{title}]({e['url']})"]
    meta = []
    if e.get('stars') is not None:
        meta.append(f"★{e['stars']:,}")
    meta.append(f"📚{e['n']}")
    if e.get('archived'):
        meta.append('archived')
    bits.append('`' + ' · '.join(meta) + '`')
    desc = e.get('gh_desc') or e.get('desc') or ''
    if desc:
        desc = md_escape(desc)
        cap = 160 if long_tail else 240
        if len(desc) > cap:
            desc = desc[:cap].rsplit(' ', 1)[0] + '…'
        bits.append('— ' + desc)
    return '- ' + ' '.join(bits)


def main():
    raw = json.load(open(os.path.join(ROOT, '.cache', 'catalog_raw.json'), encoding='utf-8'))
    ver = load_verified()
    today = dt.date.today().isoformat()
    sources = json.load(open(os.path.join(DATA, 'sources.json')))
    nsrc = len(sources)
    source_urls = {s['url'].lower() for s in sources}
    entries, dead = [], []
    for e in raw:
        if JUNK.search(e['url']):
            continue
        v = ver.get(e['url'].lower())
        if v:
            e.update({k: v[k] for k in ('stars', 'updated', 'archived', 'gh_desc')})
            if v['code'] != '200':
                e['status'] = 'dead'
                dead.append(e)
                continue
            final = v['final'].rstrip('/')
            if final.lower() != e['url'].lower() and re.match(r'https://github\.com/[^/]+/[^/]+$', final):
                e['renamed_from'], e['url'] = e['url'], final
                e['title'] = final.replace('https://github.com/', '')
            e['status'] = 'verified'
            if e['url'].lower() in source_urls:  # renamed into one of the tracked source lists
                continue
        else:
            e['status'] = 'unverified'
        entries.append(e)

    # merge entries that collapse onto the same URL after rename-resolution
    merged = {}
    for e in entries:
        k = e['url'].lower()
        if k in merged:
            m = merged[k]
            m['lists'] = sorted(set(m['lists']) | set(e['lists']))
            m['n'] = len(m['lists'])
        else:
            merged[k] = e
    entries = sorted(merged.values(), key=lambda e: (-e['n'], -(e.get('stars') or 0), e['title'].lower()))

    os.makedirs(OUT, exist_ok=True)
    by = collections.defaultdict(list)
    for e in entries:
        by[e['cat']].append(e)

    for cid, title, blurb in CATS:
        items = by.get(cid, [])
        out = [f'# {title}', '', f'> {blurb}', '>',
               f'> **{len(items):,} entries** · generated {today} from {nsrc} source lists · [← catalog index](README.md) · [← main list](../README.md)',
               '', '**Legend:** `📚N` = cited by N independent source lists (the consensus signal) · `★N` = GitHub stars when verified on the pull date. '
               'Entries are auto-categorized; one entry lives in exactly one category.', '']
        for lo, name, note in TIERS:
            hi = {10: 10**9, 5: 9, 3: 4, 1: 2}[lo]
            tier = [e for e in items if lo <= e['n'] <= hi]
            if not tier:
                continue
            out.append(f'## {name} ({note}) — {len(tier):,}')
            out.append('')
            if lo == 1 and len(tier) > 40:
                out.append(f'<details><summary>Show {len(tier):,} long-tail entries</summary>')
                out.append('')
            out += [line(e, long_tail=(lo == 1)) for e in tier]
            if lo == 1 and len(tier) > 40:
                out += ['', '</details>']
            out.append('')
        open(os.path.join(OUT, f'{cid}.md'), 'w', encoding='utf-8').write('\n'.join(out))

    idx = ['# Full Catalog', '',
           f'The complete, de-duplicated union of every link about Jev-like models found across **{nsrc} awesome-jev source lists** — '
           f'**{len(entries):,} unique entries** — auto-categorized and ranked by how many independent lists cite each one.', '',
           'The hand-curated highlights live in the [main README](../README.md). This catalog is the exhaustive layer underneath it; '
           'it is regenerated by `scripts/refresh.sh`.', '',
           '| Category | Entries | 📚≥10 | 📚5–9 | 📚3–4 | 📚1–2 |', '|---|--:|--:|--:|--:|--:|']
    for cid, title, _ in CATS:
        it = by.get(cid, [])
        c = lambda lo, hi: sum(1 for e in it if lo <= e['n'] <= hi)
        idx.append(f'| [{title}]({cid}.md) | {len(it):,} | {c(10, 10**9)} | {c(5, 9)} | {c(3, 4)} | {c(1, 2)} |')
    idx += ['', '## How entries are built', '',
            '1. Every Markdown link in every file of every source list is extracted with its section heading and surrounding text.',
            '2. URLs are normalized (scheme, `www.`, tracking params, fragments; GitHub deep links collapse to `owner/repo`). Links to the source lists themselves and badges/images are dropped.',
            '3. `📚N` counts the **distinct source lists** that cite the entry — the strongest quality signal available, since many lists are independently curated.',
            '4. Each GitHub entry cited by ≥5 lists was fetched on the pull date to confirm it resolves, follow renames, and record stars and the repo\'s own description.',
            '5. Categories come from keyword rules over the name, URL, description and the section headings the source lists filed it under.', '',
            f'Links that did not resolve on the pull date ({len(dead)}) are listed in [unresolved.md](unresolved.md).',
            '', 'Machine-readable: [`data/catalog.json`](../data/catalog.json) · [`data/catalog.csv`](../data/catalog.csv)']
    open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8').write('\n'.join(idx) + '\n')

    un = ['# Unresolved Links', '', f'GitHub links cited by ≥5 source lists that returned a non-200 status on {today} '
          '(deleted, made private, or never existed). Kept for auditability; excluded from the catalog.', '']
    un += [f"- `{e['url']}` — 📚{e['n']} — {md_escape(e.get('desc') or '')[:140]}" for e in sorted(dead, key=lambda e: -e['n'])]
    open(os.path.join(OUT, 'unresolved.md'), 'w', encoding='utf-8').write('\n'.join(un) + '\n')

    keep = ('url', 'title', 'cat', 'n', 'stars', 'status', 'desc', 'gh_desc', 'updated', 'archived', 'lists')
    json.dump([{k: e.get(k) for k in keep} for e in entries], open(os.path.join(DATA, 'catalog.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    with open(os.path.join(DATA, 'catalog.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['url', 'title', 'category', 'cited_by_lists', 'stars', 'status', 'description'])
        for e in entries:
            w.writerow([e['url'], e['title'], e['cat'], e['n'], e.get('stars') or '', e['status'], e.get('gh_desc') or e.get('desc') or ''])
    print(f'{len(entries)} entries, {len(dead)} dead, {sum(1 for e in entries if e["status"] == "verified")} verified')


if __name__ == '__main__':
    main()
