# STATE

- Last updated: 2026-11-18 (Wed) roll-up at 13:30 ET. **Flat, no open orders** (last good Robinhood read 13:22 ET; the Robinhood MCP
  asked for re-sign-in at 13:28, so the roll-up could not re-read the account — **verify on the next "hi"**).
- **Agent budget: $143.77** ($256.22 − $112.45 on 11/18). Account cash **$147.25** = budget + floor $3.48.
  - **Mak1 budget: $56.85** ($169.30 − $112.45; all 5 losing trades on 11/18 were Mak1/Mak4 on SPY). Mak4 and Alpha trade on Mak1's money.
  - **Mak3 budget: $60.00** (gap fade) — untouched. **Mak2 budget: $26.92** — untouched.
  - Buying power now fits only ONE SPY contract up to ≈ $1.40 premium.
- **Cash floor (never go below): $3.48.**
- **Week of 2026-11-16 agent P&L: −$151.35** (Mon +$42.73, Tue −$81.63, Wed −$112.45). Weekly kill switch −$117.57 is **BREACHED**
  (the user lifted it for Wed only: "full override until I turn green" / "Full gas and override"; then "Stop" at 13:22).
  → **No live trades Thu 11/19 / Fri 11/20 unless the user explicitly re-authorizes and sets a floor.** Ask on "hi".
- **Trade score:** Wed 11/18 = −50,000 (0 W / 5 L). Weekly score = 0. Rules in PLAYBOOK (+5,000 green / −10,000 red; day must end ≥ 0).
- **Targets the user stated:** account $300 (11/18), $500 by end of Nov (11/17). Agent view (told to the user): not reachable from
  $147 without risking most of the account; do not raise size or drop stops to chase them.
- Sizing if trading resumes: 1 contract, loss ≤ $15–20 per trade, max 2 trades/day, A+ setups on TREND days only, take profit at the
  bid at +25% (LESSONS 11/18).
- Scan cadence: every **1 minute** when flat, 20–30 s with a position (user 11/18). Monitor + session cron were stopped at 13:22 on the
  user's "Stop"; re-create both on the next trading day.
- Wake-up: see CLAUDE.md (Thu 11/19 08:47 ET trigger).
- ⚠️ 11/10: ANOTHER agent traded this account (SPY 753C, ≈ −$7.09). None seen since (11/18 orders through 13:22 were all mine). Keep checking.
- ⚠️ Robinhood MCP sign-in expired 11/18 13:28 — the user must re-authorize the connector in claude.ai settings.
