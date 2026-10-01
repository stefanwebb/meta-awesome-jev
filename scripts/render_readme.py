#!/usr/bin/env python3
"""Render README.md from templates/README.md.tmpl, filling live numbers from data/.

Tokens:
  {{s:owner/repo}}   -> `★1,234 · 📚56`  (GitHub stars when verified + number of source lists citing it)
  {{n:<url>}}        -> `📚12`           (source-list count for any URL)
  {{stat:<name>}}    -> sources | entries | verified | dead | stars | pulled | multi (entries cited by >=3 lists)
Unknown tokens are reported and rendered empty so a typo never ships silently.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cat = json.load(open(os.path.join(ROOT, 'data', 'catalog.json'), encoding='utf-8'))
sources = json.load(open(os.path.join(ROOT, 'data', 'sources.json')))
by_url = {e['url'].lower().rstrip('/'): e for e in cat}
src_by_url = {s['url'].lower().rstrip('/'): s for s in sources}
dead = sum(1 for _ in open(os.path.join(ROOT, 'catalog', 'unresolved.md'))) if os.path.exists(os.path.join(ROOT, 'catalog', 'unresolved.md')) else 0

stats = {
    'sources': f"{len(sources):,}",
    'entries': f"{len(cat):,}",
    'verified': f"{sum(1 for e in cat if e.get('status') == 'verified'):,}",
    'multi': f"{sum(1 for e in cat if e['n'] >= 3):,}",
    'stars': f"{sum(s.get('stars') or 0 for s in sources):,}",
    'pulled': max(s.get('pulled', '') for s in sources),
}
missing = []


def lookup(url):
    k = url.lower().rstrip('/')
    k = re.sub(r'^https?://(www\.)?', 'https://', k)
    return by_url.get(k)


def repl(m):
    kind, arg = m.group(1), m.group(2).strip()
    if kind == 's':
        e = lookup('https://github.com/' + arg)
        if not e:
            src = src_by_url.get(('https://github.com/' + arg).lower())
            if src:  # one of the tracked source lists (excluded from the catalog by design)
                return f"`★{src.get('stars') or 0:,} · source list`"
            missing.append(arg)
            return ''
        parts = []
        if e.get('stars') is not None:
            parts.append(f"★{e['stars']:,}")
        parts.append(f"📚{e['n']}")
        return '`' + ' · '.join(parts) + '`'
    if kind == 'n':
        e = lookup(arg)
        if not e:
            missing.append(arg)
            return ''
        return f"`📚{e['n']}`"
    if kind == 'stat':
        if arg not in stats:
            missing.append('stat:' + arg)
            return ''
        return stats[arg]
    missing.append(m.group(0))
    return ''


def main():
    tmpl = open(os.path.join(ROOT, 'templates', 'README.md.tmpl'), encoding='utf-8').read()
    out = re.sub(r'\{\{(s|n|stat):([^}]+)\}\}', repl, tmpl)
    out = re.sub(r'\] +\n', ']\n', out)
    out = re.sub(r'\)  +—', ') —', out)
    open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8').write(out)
    print(f'README.md written; {len(missing)} unresolved token(s)')
    for x in missing:
        print('  missing:', x, file=sys.stderr)


if __name__ == '__main__':
    main()
