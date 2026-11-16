# STATE

- Last updated: 2026-11-16 (Mon) EOD roll-up. Flat, no open orders (checked 15:30 ET).
- **Agent budget: $337.85** ($295.12 + $42.73 on 11/16). Profits/losses from agent trades change it.
  - **Mak1 budget: $225.93** ($183.20 + $42.73; Mak4's +$69 is booked here because Mak4 trades on Mak1's money).
    Limits: 5% = $11.30 loss/trade, 10% = −$22.59/day, 20% = −$45.19/week. Premium cap: up to the whole Mak1 budget (user 11/16);
    loss per trade is still set by the stop.
  - **Mak4 (VWAP range / capitulation reversion):** LIVE, runs in parallel with Mak1, up to $60 of Mak1's money, ≤ $10–15 loss.
  - **Mak3 budget: $60.00** (gap fade). ≤ $45 premium, ≤ $10 loss, −$15/day, max 2/day. No trades yet.
  - **Mak2 budget: $51.92.** ≤ $40 premium, ≤ $10 loss. 11/16 scan: every mover's options were too wide or too expensive.
- **Cash floor (never go below): $3.48.** Account cash $341.33 = budget $337.85 + floor $3.48 ✓.
- Combined agent stops: −10%/day of total ($33.79), −20%/week ($67.57).
- **Week of 2026-11-16 agent P&L: +$42.73** (Mon +$42.73). Weekly target $100 → $57.27 to go. Last week (11/09): +$21.40 (broker +$16 incl. the other agent).
- Red-day streak broken (Thu, Fri red; Mon green). Go-big rule is no longer active.
- **New rules 11/16:** full-session scanning of all 4 strategies 9:30–15:45 (no new 0DTE entries after 15:30); no chasing (one limit at mid,
  skip if missed); on a green day stop if P&L falls back to half its peak; caution with capital (user).
- Wake-up: trig_01Fdj148LfCpMR1mtiqbQjWU for Tue 11/17 08:47 ET. Session cron backup ea3f36db (session-only; recreate if missing).
- Tue 11/17: retail sales + import/export prices 8:30 ET; **NVDA earnings after the close** (QQQ caution late, gap risk Wed).
- ⚠️ 11/10: ANOTHER agent traded this account (SPY 753C, ≈ −$7.09). None since. Keep checking get_option_orders.
