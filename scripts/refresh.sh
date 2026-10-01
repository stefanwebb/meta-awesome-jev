#!/usr/bin/env bash
# Re-pull every source list and regenerate everything that is derived from data:
# sources.md, catalog/, data/catalog.{json,csv}, and the live numbers in README.md.
#
# The hand-written synthesis (docs/*.md and templates/README.md.tmpl) is NOT
# regenerated: review `git diff sources.md catalog/` afterwards and update it by hand.
#
# Usage:
#   scripts/refresh.sh                      # full refresh (GitHub verification takes ~30-40 min)
#   SKIP_VERIFY=1 scripts/refresh.sh        # reuse data/verified.tsv from the last run
#   scripts/refresh.sh --only owner/repo    # re-pull just some sources, then rebuild
set -euo pipefail
cd "$(dirname "$0")/.."

python3 scripts/pull_sources.py "$@"     # clone/update .cache/repos; stars + commit -> data/sources.json
python3 scripts/extract_links.py         # -> .cache/links.json
python3 scripts/build_catalog.py         # -> .cache/catalog_raw.json, data/verify_urls.txt

if [[ "${SKIP_VERIFY:-0}" != "1" ]]; then
  # Verify GitHub entries cited by >=5 lists: existence, renames, stars, description.
  xargs -P 6 -I{} scripts/verify_github.sh {} < data/verify_urls.txt > data/verified.tsv.new 2>/dev/null || true
  mv data/verified.tsv.new data/verified.tsv
fi

python3 scripts/render_catalog.py        # -> catalog/*.md, data/catalog.{json,csv}
python3 scripts/render_sources.py        # -> sources.md
python3 scripts/render_readme.py         # -> README.md (from templates/README.md.tmpl)
