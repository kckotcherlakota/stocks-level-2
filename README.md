# stocks-level-2 — 0DTE options trading memory

**Commands:** user says **"hi"** → load context (see `CLAUDE.md`). User says **"roll up"** → save everything to the repo, commit + push, confirm it's safe to clear the chat.

This repo is the **persistent memory** for the Claude trading agent. Sessions are wiped daily;
everything learned must live here. **At the start of every session, read in this order:**

1. `PLAYBOOK.md` — hard risk rules + setup checklist (never violate)
2. `LESSONS.md` — accumulated learnings (newest first)
3. `journal/` — the last 3 daily logs
4. `STATE.md` — current account balance, weekly P&L, open positions

Then: check the agentic Robinhood account (••••8852), market clock, calendar, and follow the
daily routine in `PLAYBOOK.md`. Commit + push the journal at the end of every day.
