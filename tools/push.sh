#!/usr/bin/env bash
# Commit everything and push to the working branch with the required trailers.
# Usage: tools/push.sh "commit message"
set -euo pipefail
cd "$(dirname "$0")/.."
BRANCH=claude/modest-cray-98ca6z
MSG="${1:-update}"
git add -A
if git diff --cached --quiet; then
  echo "nothing to commit"
else
  git commit -q -m "$MSG

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_012ZPnNbsFMVPbhMPtnSQDKN"
fi
for i in 1 2 3 4; do
  if git push -q -u origin "$BRANCH" 2>/dev/null; then break; fi
  echo "push failed, retry $i"; sleep $((2 ** i))
done
echo "pushed; uncommitted files: $(git status --short | wc -l)"
