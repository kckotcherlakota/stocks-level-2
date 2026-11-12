# STATE

- Last updated: 2026-11-12 ~15:00 ET (EOD)
- **Agent budget: $317.73** ($330.82 − $13.09 on 11/12). Profits/losses from agent trades change it.
- **Cash floor (never go below): $3.48** (cash $303.48 − $300 at 11:15 ET 11/10)
- **Sizing:** % of budget (PLAYBOOK "Scaling plan"): at $317.73 → max loss $15.89/trade, −$31.77/day, −$63.55/week, premium ≤ $79 (≤ $143 A+).
- **Live strategy: Mak1 only (complete budget).** B, C, D, E, A2 = paper only (STRATEGIES.md). Mak1 first until the day is green (user 11/12).
- Open positions: none. Open orders: none. Account cash $321.21 (EOD 11/12).
- Week of 2026-11-09 agent P&L: **+$44.01** (Mon −$9.54; Tue +$39.73; Wed +$26.91; Thu −$13.09). Other agent: −$7.09 (Tue).
  Weekly kill switch −20% of budget (≈ −$64). Week is green going into Friday → normal rules Friday (first trade half size).
- Friday step-up review due (PLAYBOOK): week positive, max drawdown < 10% → keep the % rules.
- Goal: +10%/day as a target only; minimize red days (PLAYBOOK).
- Paper bankroll for experiments: $100.00 (no paper trades logged yet — log them in real time from Fri).
- Scans: every 2 min when flat (user 11/12); 30 s with money at work. New exit rule: if any of SPY/QQQ/IWM reclaims VWAP against a
  VWAP-loss trade, exit at bid − 0.01 (LESSONS 11/12).
- Upcoming: CSCO reported 11/12 after close → strategy E (paper) on 11/13 open. Check econ calendar Friday AM.
- ⚠️ 11/10 11:04–11:11 ET: ANOTHER agent (not this session) traded this account (SPY 753C, ≈ −$7.09). None seen 11/11–11/12.
  Always check get_option_orders for orders not placed by this session before trading.
