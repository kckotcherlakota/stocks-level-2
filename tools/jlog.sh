#!/usr/bin/env bash
# Append a line to today's journal (ET date) and push.
# Usage: tools/jlog.sh "| 10:05 | 752.1 | 678.4 | 276.9 | note |"     (scan row)
#        tools/jlog.sh -n "free text line"                            (no push)
set -euo pipefail
cd "$(dirname "$0")/.."
PUSH=1
if [ "${1:-}" = "-n" ]; then PUSH=0; shift; fi
DAY=$(TZ=America/New_York date +%F)
F="journal/$DAY.md"
[ -f "$F" ] || printf '# %s\n\n## Scan log\n| Time | SPY | QQQ | IWM | Note |\n|---|---|---|---|---|\n' "$DAY" > "$F"
printf '%s\n' "$*" >> "$F"
echo "logged to $F"
if [ "$PUSH" = 1 ]; then tools/push.sh "journal $DAY: $(echo "$*" | cut -c1-60)"; fi
