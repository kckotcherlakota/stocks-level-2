# STATE

- Last updated: 2026-11-13 (Fri) ~14:15 ET (EOD roll-up; stopped trading after 2nd loss)
- **Agent budget: $295.12** ($317.73 − $22.61 on 11/13). Profits/losses from agent trades change it.
  - **Mak1 budget: $243.20** ($267.73 − $24.53). Limits: 5% = $12.16 loss/trade, 10% = −$24.32/day, 20% = −$48.64/week;
    premium cap 25% ≈ $60; A+ cap 45% ≈ $109; A+ Conviction loss 7.5% ≈ $18.
  - **Mak2 budget: $51.92** ($50 + $1.92). Per trade ≤ $40 premium, ≤ $10 loss, −$15/day, max 2/day, stop after 1 loss.
- **Cash floor (never go below): $3.48.** Account cash $298.60 (EOD 11/13) = budget $295.12 + floor $3.48 ✓.
- Combined agent stops: −10%/day of total ($29.51), −20%/week ($59.02).
- Open positions: none. Open orders: none (checked 14:12 ET 11/13). No orders from other agents seen 11/11–11/13.
- **Week of 2026-11-09 agent P&L: +$21.40** (Mon −$9.54; Tue +$39.73; Wed +$26.91; Thu −$13.09; Fri −$22.61). Other agent: −$7.09 (Tue).
  Weekly target $150 → missed by $128.60. **Two red days in a row (Thu, Fri).**
- **Friday step-up review (11/13):** week positive (+$21.40), max drawdown from the week's peak (+$57.10 Wed → +$21.40) ≈ 11% of budget
  → borderline; keep the % rules (sizes scale down with the smaller budget). No size increase next week.
- **Go-big rule (user 11/13):** size override allowed only on/after 2 red days. Mon 11/16 qualifies (Thu+Fri red) — but only on a
  valid A/A+ setup, max loss $15/trade, inside the combined daily stop. LESSONS 11/13: don't use it for breakout buys in a range.
- Paper bankroll for experiments: $100.00 (no paper trades logged; B/C/E had no qualifying signals 11/13).
- Scans: every 2 min when flat; 30 s with money at work. Exit if 2 of 3 indexes lose the breakout / VWAP (LESSONS 11/12, 11/13).
- ⚠️ 11/13: Robinhood + other MCPs failed to connect until ~10:20 ET (502). New rule in CLAUDE.md: retry in 1–2 min, then email alert.
- ⚠️ 11/13: the scheduled wake-up fired ~50 min late (09:55 vs 09:05 ET). Monday's wake-up set earlier to compensate.
- ⚠️ 11/10 11:04–11:11 ET: ANOTHER agent traded this account (SPY 753C, ≈ −$7.09). None seen since. Keep checking get_option_orders.
