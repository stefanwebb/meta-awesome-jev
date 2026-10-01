u=$1
h=$(curl -sL -m 20 -A "Mozilla/5.0" -w '\n__CODE__%{http_code} %{url_effective}' "$u")
code=$(echo "$h" | grep -o '__CODE__.*' | sed 's/__CODE__//')
stars=$(echo "$h" | grep -oE 'id="repo-stars-counter-star"[^>]*title="[0-9,]+"' | head -1 | grep -oE 'title="[0-9,]+"' | tr -dc '0-9')
desc=$(echo "$h" | grep -oE '<meta name="description" content="[^"]*"' | head -1 | sed 's/.*content="//; s/"$//')
upd=$(echo "$h" | grep -oE '<relative-time[^>]*datetime="[^"]+"' | head -1 | grep -oE 'datetime="[^"]+"' | cut -d'"' -f2)
arch=$(echo "$h" | grep -q 'This repository has been archived' && echo archived)
printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$u" "$code" "${stars:-}" "$upd" "$arch" "$desc"
