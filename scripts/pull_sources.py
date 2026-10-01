#!/usr/bin/env python3
"""Clone or update every source list in sources.md and record pull metadata.

For each GitHub URL in sources.md this shallow-clones (or fast-forwards) the
repo into .cache/repos/<owner>__<repo>, scrapes its current star count from the
public repo page (no API token needed), and writes data/sources.json.

Run scripts/render_sources.py afterwards to refresh the table in sources.md.

Usage: python3 scripts/pull_sources.py [--only owner/repo ...]
"""
import concurrent.futures as cf
import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, '.cache', 'repos')
OUT = os.path.join(ROOT, 'data', 'sources.json')
UA = {'User-Agent': 'Mozilla/5.0 (meta-jev-awesome source puller)'}


def source_urls():
    text = open(os.path.join(ROOT, 'sources.md'), encoding='utf-8').read()
    seen, urls = set(), []
    for u in re.findall(r'https://github\.com/[\w.-]+/[\w.-]+', text):
        if u.lower() not in seen:
            seen.add(u.lower())
            urls.append(u)
    return urls


def stars(url):
    try:
        html = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read().decode('utf-8', 'ignore')
    except Exception:
        return None
    m = re.search(r'id="repo-stars-counter-star"[^>]*title="([\d,]+)"', html)
    return int(m.group(1).replace(',', '')) if m else None


def pull(url):
    name = url.replace('https://github.com/', '').replace('/', '__')
    path = os.path.join(CACHE, name)
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0')
    if os.path.isdir(os.path.join(path, '.git')):
        ok = subprocess.run(['git', '-C', path, 'pull', '-q', '--depth', '1', '--rebase=false', '--allow-unrelated-histories'],
                            env=env, capture_output=True).returncode == 0
        if not ok:  # history rewritten upstream: re-clone
            subprocess.run(['rm', '-rf', path])
    if not os.path.isdir(os.path.join(path, '.git')):
        ok = subprocess.run(['git', 'clone', '-q', '--depth', '1', url + '.git', path], env=env, capture_output=True).returncode == 0
        if not ok:
            return dict(url=url, dir=name, status='unreachable', pulled=dt.date.today().isoformat(), stars=stars(url))
    log = subprocess.run(['git', '-C', path, 'log', '-1', '--format=%h %cs'], capture_output=True, text=True).stdout.split()
    return dict(url=url, dir=name, status='ok', pulled=dt.date.today().isoformat(),
                commit=log[0] if log else None, last_commit=log[1] if len(log) > 1 else None, stars=stars(url))


def main():
    os.makedirs(CACHE, exist_ok=True)
    only = {o.lower() for o in sys.argv[sys.argv.index('--only') + 1:]} if '--only' in sys.argv else None
    urls = [u for u in source_urls() if not only or u.lower().replace('https://github.com/', '') in only]
    prev = {}
    if os.path.exists(OUT):
        prev = {r['url'].lower(): r for r in json.load(open(OUT))}
    with cf.ThreadPoolExecutor(8) as ex:
        for r in ex.map(pull, urls):
            prev[r['url'].lower()] = r
            print(f"{r['status']:12} {r.get('stars')!s:>6}★  {r['url']}")
    order = [u.lower() for u in source_urls()]
    rows = sorted(prev.values(), key=lambda r: order.index(r['url'].lower()) if r['url'].lower() in order else 1e9)
    json.dump(rows, open(OUT, 'w'), indent=1)
    print(f'wrote {OUT} ({len(rows)} sources)')


if __name__ == '__main__':
    main()
