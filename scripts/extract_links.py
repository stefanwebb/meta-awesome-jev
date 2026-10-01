#!/usr/bin/env python3
"""Extract every Markdown link (with section heading + surrounding line) from all cloned source lists.

Input:  .cache/repos/*   (scripts/pull_sources.py)
Output: .cache/links.json
"""
import os, re, json, sys, collections
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.join(ROOT, '.cache'); R = os.path.join(S, 'repos')
link_re = re.compile(r'\[([^\]]{1,300})\]\((https?://[^)\s]+)\)')
bare_re = re.compile(r'(?<![\(\[<"])\bhttps?://[^\s)\]>"\'`|]+')
def norm(u):
    u = u.strip().rstrip('.,;:')
    u = re.sub(r'#.*$', '', u)
    u = re.sub(r'[?&](utm_[^&]+|ref=[^&]+)', '', u)
    u = u.replace('http://', 'https://').replace('://www.', '://')
    u = re.sub(r'/(tree|blob)/(main|master)/?$', '', u)
    return u.rstrip('/').lower()
rows = []
for repo in sorted(os.listdir(R)):
    for root, _, files in os.walk(os.path.join(R, repo)):
        if '/.git' in root: continue
        for f in files:
            if not f.lower().endswith('.md'): continue
            p = os.path.join(root, f); rel = os.path.relpath(p, os.path.join(R, repo))
            try: lines = open(p, encoding='utf-8', errors='ignore').read().splitlines()
            except: continue
            heads = []
            for ln in lines:
                m = re.match(r'^(#{1,6})\s+(.*)', ln)
                if m:
                    lvl = len(m.group(1)); heads = [h for h in heads if h[0] < lvl] + [(lvl, m.group(2).strip())]; continue
                for li, m in enumerate(link_re.finditer(ln)):
                    t, u = m.group(1), m.group(2)
                    if any(x in u for x in ('shields.io','img.shields','badge','star-history','.png','.jpg','.svg','.gif')): continue
                    desc = re.sub(r'\s+', ' ', link_re.sub(lambda k: k.group(1), ln)).strip(' -*|')[:400]
                    rows.append(dict(repo=repo, file=rel, section=' > '.join(h[1] for h in heads[-2:]), title=t.strip(), url=u, n=norm(u), desc=desc, first=(li == 0)))
json.dump(rows, open(os.path.join(S, 'links.json'), 'w'))
print('links extracted:', len(rows))
