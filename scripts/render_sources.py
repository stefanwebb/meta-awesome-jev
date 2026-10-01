#!/usr/bin/env python3
"""Rewrite sources.md as a table from data/sources.json (+ data/source_profiles.json).

Every GitHub URL in the table is a tracked source; scripts/pull_sources.py reads
them back out of this file, so new sources can be added by appending a bare URL.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = json.load(open(os.path.join(ROOT, 'data', 'sources.json')))
prof_path = os.path.join(ROOT, 'data', 'source_profiles.json')
profiles = json.load(open(prof_path)) if os.path.exists(prof_path) else {}

TYPE_LABEL = {
    'curated-list': 'Curated list', 'auto-generated-list': 'Auto-generated list', 'use-case-collection': 'Use-case collection',
    'project/code': 'Project (not a list)', 'papers-list': 'Papers', 'skills-collection': 'Agent skills', 'tutorial/study-guide': 'Guide',
    'spam/low-quality': 'Empty / low quality', 'security/robustness': 'Security / robustness', 'prompt-collection': 'Prompt patterns', 'other': 'Report',
}


def short(s, n=150):
    s = (s or '').replace('|', '/').replace('\n', ' ').strip()
    return s if len(s) <= n else s[:n].rsplit(' ', 1)[0] + '…'


def main():
    rows_sorted = sorted(rows, key=lambda r: -(r.get('stars') or 0))
    pulled = sorted({r.get('pulled') for r in rows if r.get('pulled')})
    total_stars = sum(r.get('stars') or 0 for r in rows)
    out = [
        '# Sources',
        '',
        f'The **{len(rows)} community "awesome-jev" repositories** synthesized into this meta-list, with the date each was last pulled, '
        'the commit that was read, and its GitHub star count at pull time.',
        '',
        f'- **Last pull:** {pulled[-1] if pulled else "n/a"} · **Combined stars:** {total_stars:,}',
        '- **Stars** were read from each repo\'s public GitHub page on the pull date (not the API), so they are a point-in-time snapshot.',
        '- **Commit / last commit** identify exactly which revision was read; compare against upstream to see what changed since.',
        '- **Type** and **summary** come from the per-source review notes in [`docs/source-notes/`](docs/source-notes/); '
        'see [`docs/source-lists.md`](docs/source-lists.md) for the comparative review.',
        '',
        '**To update:** run `scripts/refresh.sh` (re-pulls every source, refreshes stars and commits, regenerates the catalog and this table). '
        '**To add a source:** append its GitHub URL on a new line at the bottom of this file, then refresh.',
        '',
        '| # | Source | ★ Stars | Pulled | Commit | Last commit | Type | Language | Summary |',
        '|--:|---|--:|---|---|---|---|---|---|',
    ]
    for i, r in enumerate(rows_sorted, 1):
        p = profiles.get(r['dir'], {})
        typ = p.get('type', '')
        typ = TYPE_LABEL.get(typ, typ.replace('-', ' ').capitalize() if typ else '')
        name = r['url'].replace('https://github.com/', '')
        commit = f"[`{r['commit']}`]({r['url']}/commit/{r['commit']})" if r.get('commit') else r.get('status', '')
        out.append(f"| {i} | [{name}]({r['url']}) | {r.get('stars') if r.get('stars') is not None else '?':,} | {r.get('pulled', '')} | "
                   f"{commit} | {r.get('last_commit', '')} | {typ} | {short(p.get('languages', ''), 40)} | {short(p.get('one_liner', ''))} |")
    out.append('')
    open(os.path.join(ROOT, 'sources.md'), 'w', encoding='utf-8').write('\n'.join(out))
    print(f'sources.md: {len(rows)} sources')


if __name__ == '__main__':
    main()
