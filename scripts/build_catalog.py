#!/usr/bin/env python3
"""Union + de-duplicate + categorize all extracted links.

Input:  .cache/links.json, data/sources.json
Output: .cache/catalog_raw.json, data/verify_urls.txt (GitHub entries cited by >=5 lists)
"""
import json, re, collections, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.join(ROOT, '.cache'); D = os.path.join(ROOT, 'data')
rows = json.load(open(f'{S}/links.json'))
srcs = [r['url'] for r in json.load(open(f'{D}/sources.json'))]
src_keys = {u.lower().replace('https://github.com/', '') for u in srcs}
src_dirs = {u.replace('https://github.com/', '').replace('/', '__'): u for u in srcs}

GH_SKIP = {'topics','search','features','orgs','sponsors','settings','marketplace','apps','login','about','pricing','collections','trending','explore','notifications','new','site','contact'}
def key(u):
    u = u.strip().rstrip('.,;:)*`\'"')
    u = re.sub(r'#.*$', '', u)
    if '?' in u:  # keep only query params that identify content (HN item ids, YouTube videos, ...)
        base, _, q = u.partition('?')
        keep = [kv for kv in q.split('&') if kv.split('=')[0].lower() in ('id', 'v', 'p', 'list', 'q')]
        u = base + ('?' + '&'.join(keep) if keep else '')
    u = u.replace('http://', 'https://').replace('://www.', '://')
    m = re.match(r'https://github\.com/([^/]+)/([^/]+)', u, re.I)
    if m:
        o, r = m.group(1), re.sub(r'\.git$', '', m.group(2))
        if o.lower() in GH_SKIP: return None
        return f'https://github.com/{o}/{r}'.lower()
    if re.match(r'https://github\.com/[^/]+/?$', u, re.I): return 'GHUSER'
    if re.search(r'(shields\.io|star-history|githubassets|api\.github\.com|raw\.githubusercontent|contrib\.rocks|visitor-badge|awesome\.re|creativecommons|opensource\.org/licenses|img\.|\.(png|jpe?g|gif|svg|webp)$)', u, re.I): return None
    return u.rstrip('/').lower()

# domain of own GitHub pages sites of source lists -> self
own_pages = set()
for s in srcs:
    o = s.split('/')[3].lower(); own_pages.add(f'https://{o}.github.io')

agg = {}
for r in rows:
    k = key(r['url'])
    if not k or k == 'GHUSER': continue
    if any(k.startswith(p) for p in own_pages): continue
    src = src_dirs.get(r['repo'])
    item = agg.setdefault(k, dict(url=k, titles=collections.Counter(), descs=[], sections=collections.Counter(), lists=set()))
    item['lists'].add(r['repo'])
    m0 = re.match(r'https?://(?:www\.)?github\.com/([^/#?]+)/([^/#?]+)', r['url'].strip(), re.I)
    if m0: item.setdefault('ghname', collections.Counter())[m0.group(1)+'/'+re.sub(r'\.git$','',m0.group(2).rstrip('.,;:)*'))] += 1
    t = r['title'].strip('`* ')
    if t and not re.match(r'^(link|here|repo|github|source|website|demo|paper|code|\d+|→|🔗|view|visit|x|post)$', t, re.I): item['titles'][t] += 1
    if r['desc'] and r.get('first', True) and len(r['desc']) > len(t) + 12: item['descs'].append((r['repo'], r['desc']))
    if r['section']: item['sections'][r['section'].lower()] += 1

# drop links to the source lists themselves (tracked separately)
self_list = {k: v for k, v in agg.items() if k.replace('https://github.com/', '') in src_keys}
for k in self_list: del agg[k]

NON_EN = r'\b(comece|em seguida|continuar|avalia[cç][aã]o|fluxos?|revisi[oó]n|fuente|sin reproducir|para el|para la|con el|herramienta|ferramenta|des donn|avec|und die|f[uü]r die|mit der|oder|dati|questo|visite|explorar|aplicativos|exemplos|linguagem|également|über)\b|^(source|sources|from typesafe)'
def clean_desc(d, title):
    d = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', d)
    d = re.sub(r'<[^>]+>', '', d)
    d = re.sub(r'https?://\S+', '', d)
    d = re.sub(r'`', '', d)
    parts = [p.strip() for p in re.split(r'\s*\|\s*', d) if p.strip()]
    # table rows: pick the longest cell that isn't the title
    if len(parts) > 1:
        cand = [p for p in parts if p.lower() != title.lower() and not re.fullmatch(r'[\d,.\s★⭐kK+%-]+|[-:]+|✅|❌|yes|no', p)]
        d = max(cand, key=len) if cand else ''
    d = re.sub(r'^\s*[-*+]\s*', '', d)
    d = d.replace(title, '', 1) if d.startswith(title) else d
    d = re.sub(r'^[\s:\-–—()⭐★\d,kK]+', '', d).strip()
    d = re.sub(r'\s+', ' ', d)
    return d

def pick_desc(item, title):
    best = []
    for repo, d in item['descs']:
        c = clean_desc(d, title)
        if len(c) < 15 or re.search(r'[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af\u0400-\u04ff\u0600-\u06ff\u0e00-\u0e7f]', c): continue
        c = re.sub(r'^(\*+|!?GitHub stars|—|–|-|:|\s)+', '', c)
        c = re.sub(r'(_on \d+ lists?_|🏷️.*$|\(\d+ mirrors?\)|\*+)', '', c).strip(' ·—-')
        if len(c) < 15 or re.search(NON_EN, c, re.I): continue
        c = re.sub(r'\s+-\s+[\w.-]+/[\w.-]+$', '', c)
        c = re.sub(r'^([>⭐—–:\-\s]|\w+\)\s+-)+', '', c)
        c = re.sub(r'\s*(documented-example|code-inspected|demo-inspected|author-claim|proposed|TypeSafe AI)\s*$', '', c).strip()
        if len(c) < 15: continue
        pen = 0
        if re.search(r'call site|read 20\d\d|· ★|Project ·|SDK ·|⚠|mirrors|Uncategorized|Demos & playgrounds \(', c): pen += 200
        if not re.search(r'[.a-z]', c[-3:]): pen += 5
        if re.search(r'jev|typesafe|system.?one', c, re.I): pen -= 15
        best.append((pen + abs(len(c) - 120) / 4, c))
    if not best: return ''
    best.sort()
    best = [c for _, c in best]
    d = best[0]
    return (d[:220].rsplit(' ', 1)[0] + '…') if len(d) > 230 else d

CATS = [
 ('official', 'Official TypeSafe Resources', [r'typesafe\.ai', r'github\.com/typesafe-ai/', r'huggingface\.co/typesafe']),
 ('papers', 'Research Papers', [r'arxiv\.org', r'aclanthology', r'openreview', r'doi\.org', r'papers\.', r'proceedings', r'semanticscholar', r'\bpaper\b']),
 ('awesome', 'Other Awesome Lists & Directories', [r'awesome', r'directory', r'\bradar\b', r'curated list', r'made ?with ?jev', r'gallery']),
 ('community', 'Community, Discussions & Social', [r'x\.com/', r'twitter\.com', r'news\.ycombinator', r'reddit\.com', r'threads\.(com|net)', r'linkedin\.com', r'xiaohongshu', r'v2ex', r'weibo', r'zhihu', r'instagram', r'discord', r'bsky']),
 ('learn', 'Tutorials, Articles & Videos', [r'youtube\.com', r'youtu\.be', r'dev\.to', r'medium\.com', r'substack', r'\bblog\b', r'tutorial', r'course', r'guide\b', r'cookbook', r'notebook', r'colab', r'learn', r'workshop', r'hashnode']),
 ('open-models', 'Open Replications, Local Inference & Jev-like Models', [r'open-?jev', r'open weights', r'jev-?like', r'\blaya\b', r'sglang', r'vllm', r'\bmlx\b', r'llama\.cpp', r'gguf', r'ollama', r'distill', r'nano-?jev', r'lit-?jev', r'replicat', r'reproduc', r'local inference', r'open decision model', r'fine-?tun', r'lora', r'train']),
 ('bench', 'Benchmarks, Evals & Calibration', [r'bench', r'\beval', r'calibrat', r'leaderboard', r'\bmeter\b', r'accuracy', r'judge', r'jagged']),
 ('security', 'Guardrails, Safety & Moderation', [r'guard', r'moderat', r'safety', r'phish', r'spam', r'\bpii\b', r'jailbreak', r'injection', r'security', r'warden', r'policy', r'fraud', r'toxic', r'abuse', r'adblock', r'secret', r'vuln', r'robust', r'red-?team']),
 ('mcp', 'MCP Servers', [r'\bmcp\b', r'-mcp', r'mcp-', r'model context protocol']),
 ('skills', 'Agent Skills & Plugins', [r'\bskills?\b', r'-skills?\b', r'plugin', r'claude[ -]code', r'\bcodex\b', r'hermes', r'openclaw', r'\bpi-', r'cursor', r'extension for', r'subagent']),
 ('routing', 'Routing, Cascades & Orchestration', [r'rout', r'dispatch', r'cascade', r'orchestrat', r'fallback', r'registry', r'triage', r'gateway', r'proxy', r'escalat', r'model select']),
 ('memory', 'Context, Memory & Compaction', [r'compact', r'context window', r'memory', r'prun', r'rerank', r'retriev', r'\brag\b', r'dedup', r'\bcache', r'token budget', r'summari']),
 ('browser', 'Browser, Desktop & Computer Use', [r'browser', r'computer[- ]use', r'desktop', r'mobile', r'android', r'\bios\b', r'chrome', r'tab', r'web agent', r'playwright', r'puppeteer', r'automation', r'\bui\b', r'screen', r'click']),
 ('games', 'Games, Robotics & Simulation', [r'game', r'mario', r'pokemon', r'snake', r'chess', r'tetris', r'minecraft', r'doom', r'drone', r'robot', r'embodied', r'simulat', r'plays?\b', r'arcade', r'poker', r'\brl\b', r'sokoban', r'nes\b', r'atari', r'racing', r'flappy']),
 ('finance', 'Finance, Trading & Commerce', [r'trad(e|er|ing)', r'financ', r'\btax', r'invoice', r'stock', r'crypto', r'defi', r'polymarket', r'market', r'bank', r'loan', r'credit', r'insur', r'ecommerce', r'e-commerce', r'shop', r'pricing', r'accounting', r'receipt']),
 ('data', 'Data, Databases & Documents', [r'\bsql\b', r'postgres', r'\bpg[-_]', r'pg_', r'neo4j', r'database', r'\bdb\b', r'duckdb', r'sqlite', r'spreadsheet', r'excel', r'csv', r'etl', r'document', r'\bpdf', r'ocr', r'extract', r'label', r'annotat', r'classif', r'tagg', r'search', r'grep', r'log'] ),
 ('dev', 'Developer Tools & Coding Workflows', [r'review', r'\bcommit', r'\bgit\b', r'\bnvim\b', r'neovim', r'vim', r'vscode', r'shell', r'\bcli\b', r'terminal', r'semgrep', r'lint', r'\bci\b', r'\bpr\b', r'pull request', r'code', r'test', r'debug', r'devops', r'kubernetes', r'docker', r'deploy', r'\bide\b', r'zsh', r'bash']),
 ('sdk', 'SDKs, Clients & Framework Integrations', [r'\bsdk\b', r'-sdk', r'sdk-', r'_sdk', r'client', r'wrapper', r'binding', r'langchain', r'llama-?index', r'\bdspy\b', r'vercel', r'ai-sdk', r'hono', r'n8n', r'zapier', r'pypi\.org', r'npmjs\.com', r'crates\.io', r'rubygems', r'pkg\.go\.dev', r'adapter', r'library', r'\bapi\b', r'typescript', r'python', r'\brust\b', r'golang', r'ruby', r'elixir', r'java\b', r'swift', r'kotlin', r'openrouter', r'featherless', r'provider']),
 ('agents', 'Agents & Decision Workflows', [r'agent', r'workflow', r'autonom', r'assistant', r'bot\b', r'copilot', r'decision', r'decide', r'judge', r'\bjarvis\b']),
 ('apps', 'Apps & Domain Applications', [r'app\b', r'health', r'medic', r'legal', r'educat', r'email', r'inbox', r'calendar', r'voice', r'home[- ]assistant', r'\bha-', r'music', r'photo', r'video', r'image', r'social', r'news', r'seo', r'marketing', r'recruit', r'hr\b', r'support', r'customer', r'sales', r'crm']),
]
STRONG_ONLY = {'awesome','community','papers','official'}
CAT_TITLE = {c[0]: c[1] for c in CATS}; CAT_TITLE['other'] = 'Everything Else'
CAT_RX = [(c[0], [re.compile(p, re.I) for p in c[2]]) for c in CATS]

def categorize(item, title, desc):
    u = item['url']
    if re.search(r'typesafe\.ai|github\.com/typesafe-ai/', u): return 'official'
    for cid in ('papers', 'community'):
        rx = dict(CAT_RX)[cid]
        if any(p.search(u) for p in rx[:6]): return cid
    text_strong = ' '.join([u.split('/')[-1] if 'github.com' in u else u, title]).replace('-', ' - ')
    text_weak = ' '.join([desc, ' '.join(s for s, _ in item['sections'].most_common(3))])
    scores = collections.Counter()
    for cid, rx in CAT_RX:
        for p in rx:
            if p.search(text_strong): scores[cid] += 3
            if cid not in STRONG_ONLY and p.search(text_weak): scores[cid] += 1
    if not scores: return 'other'
    order = [c[0] for c in CATS]
    return max(scores, key=lambda c: (scores[c], -order.index(c)))

out = []
for k, it in agg.items():
    title = it['titles'].most_common(1)[0][0] if it['titles'] else re.sub(r'^https?://(github\.com/)?', '', k)
    if 'github.com' in k and it.get('ghname'): title = it['ghname'].most_common(1)[0][0]
    desc = pick_desc(it, title)
    out.append(dict(url=k, title=title[:90], desc=desc, n=len(it['lists']), lists=sorted(it['lists']), cat=categorize(it, title, desc), sections=[s for s, _ in it['sections'].most_common(3)]))
out.sort(key=lambda x: (-x['n'], x['title'].lower()))
json.dump(out, open(f'{S}/catalog_raw.json', 'w'), ensure_ascii=False)
open(f'{D}/verify_urls.txt', 'w').write('\n'.join('https://github.com/' + x['title'] for x in out if x['n'] >= 5 and x['url'].startswith('https://github.com/')) + '\n')
print('entries', len(out), '| cited by >=5 lists:', sum(1 for x in out if x['n'] >= 5))
