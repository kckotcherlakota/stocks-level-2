# PLAYBOOK — hard rules (capital protection first)

## ⛔ MASTER RISK CONTROLLER v2 (user review, 2026-11-15) — OVERRIDES every older section below when they conflict
One shared controller for Mak1/Mak2/Mak3; each strategy keeps its own entry logic. Every candidate gets one decision, logged in the
journal with a reason code: **TRADE_ALLOWED / TRADE_BLOCKED / REDUCED_RISK / SHUTDOWN**.
Reason codes: CHOP_VWAP_CROSSES, LEVEL_FAILED_TWICE, INDEX_DISAGREEMENT, DAILY_RISK_EXCEEDED, WEEKLY_RISK_EXCEEDED, STRATEGY_RISK_EXCEEDED,
TRADE_RISK_EXCEEDED, SPREAD_COST_TOO_HIGH, DIRECTION_CONFLICT, OUTSIDE_WINDOW, TOO_EXTENDED, BROKER_UNAVAILABLE, STALE_DATA, MACRO_EVENT,
SHUTDOWN_TWO_LOSSES.

**1. Shared risk ledger (account-wide limits override every strategy limit).**
- Account: budget $295.12 (cash $298.60 − floor $3.48 — the floor is already outside the budget). Daily stop **−$29.51**, weekly **−$59.02**.
- Before every entry: **R_allowed = min(R_trade, R_strategy_remaining, R_daily_remaining, R_weekly_remaining)**, where remaining =
  limit − (realized loss + open risk) for that bucket. Planned R = whole position: qty × 100 × (fill − stop) + est. stop slippage + fees.
- If even **1 contract** doesn't fit R_allowed → TRADE_BLOCKED. Never switch to a cheaper/worse strike just to make it fit.
- **2 losing trades in a day (any strategies combined) → SHUTDOWN** for the day.
- **Never increase size after a loss.** The "go big after 2 red days" override is **REMOVED**.

**2. Mandatory gates (not part of a 3-of-4 vote — each must pass).**
- Risk fits (above). Regime ≠ chop: **≤ 2 VWAP crosses in the last 12 five-minute bars on the traded index, strict, no exceptions**;
  a new setup label never resets the count. Mak1/Mak3: **SPY, QQQ and IWM all confirm** the direction.
- Quote gate (spread ≤ 10% of mid and ≤ $0.15, quote < 10 s) **and spread-cost test: (ask − bid)/2 × 100 × qty ≤ 25% of planned R**
  → else SPREAD_COST_TOO_HIGH.
- Macro: no entry within 30 min of a scheduled release.
- The remaining checklist items (EMA 9/20 alignment, level) still need ≥ 3/4 overall.

**3. Direction / thesis lockout.** One net direction per index family (SPY/QQQ/IWM) at a time. No strategy may open a position opposite to
an open position, or opposite to a confirmed Mak1 trend. Same-direction positions across strategies count as ONE idea for risk.

**4. Time rules (Robinhood: new option stop-market orders only from 9:45 ET; no OCO/bracket for options).**
- First option entries **9:45 ET** (every entry must get its broker stop immediately). No new entries after **14:45**.
  **Mandatory flat by 15:15 ET** (Robinhood may auto-liquidate expiring options in the last 30 min). Verify flat via positions, not orders.
- Stop-market fills are not guaranteed → size R with slippage. Taking profit: cancel stop → sell limit; **if the sell doesn't fill in
  ~30 s, re-place the stop at once** — never leave a position without a confirmed stop.

**5. Breakout discipline (Mak1).** After a level fails twice (close above then back inside within 2 bars) → LEVEL_FAILED_TWICE lockout
for breakout buys at that level for the day (provisional; review weekly). Max entry distance beyond the breakout level: 0.10% of
the underlying (≈ $0.75 SPY, $0.68 QQQ, $0.28 IWM) → else TOO_EXTENDED. Retest entries and "afternoon only with the morning trend"
are **paper-tested first** (log them; don't trade them live yet).

**6. Broker outage.** On any Robinhood error: **block new entries immediately (BROKER_UNAVAILABLE)**; when possible verify positions and
open orders; never assume an unconfirmed stop exists; retry every 1–2 min; email the user at once during market hours with what is
open and what is unconfirmed; if a position must be exited and the API is down, tell the user to use the Robinhood app / official support.

**7. Strategy status under v2.** Mak1 LIVE (entries 9:45–11:00 and 13:30–14:45). Mak2 LIVE with stock-specific rules (STRATEGIES).
**Mak3 = PAPER until validated** (its $60 stays allocated but idle). Mak1 per-trade R: ≤ $9.16 (5% of $183.20) — whole position.


## Account
- Only tradable account: Robinhood agentic account ••••8852 (limited margin, options level 3).
- Other accounts are read-only to the agent; never touch them.

## Agent bankroll — ONLY $80 (user instruction 2026-11-09)
- The agent's total money is **$80**, not the account balance. The rest of the account is
  reserved by the user for other purposes and must never be used, even if buying power shows more.
- Bankroll = $80 + cumulative realized P&L **from the agent's own trades only** (tracked in `STATE.md`).
  Deposits, interest, dividends, or any other money arriving in the account is the user's,
  never the agent's, even if it lands in this account.
- **Cash floor:** account cash must never go below **$204.29**. (Was $124.29; on 11/09 AM cash
  rose $204.29 → $284.29, an $80 arrival not from agent trades. Floor raised to cash − $80 so the
  agent can never touch more than $80. Adjust the floor if the user moves money in/out.)
  Check this before every order; if an order could break the floor, don't place it.
- If the bankroll falls to $40, stop trading and ask the user before continuing.
- **Needing more than $80 requires the user's explicit approval** (user instruction 2026-11-09).
  Ask in the session or by email, and wait for a yes before using any money beyond the bankroll.
  Profits stay in the bankroll, so it can grow above $80 without asking (confirmed by user 2026-11-09).
  The cash floor stays fixed at $204.29: profits add to cash and bankroll equally, so the
  user's reserved money is never touched.

## Budget update (user, 2026-11-10 ~11:15 ET)
- Agent budget raised to **$300** ("more money = more responsibility: make more profit AND protect capital more carefully").
- At the time: account cash $303.48 → **new cash floor = $3.48** (cash − $300). Profits from agent trades add to the budget.
- Scaled risk limits (below) are % of a $300 budget; size up only as written.

## Sizing preference (user, 2026-11-11 ~12:20 ET)
- "Use the capital to the fullest but be careful; safeguard capital and snatch profits."
- Interpretation: on every setup that passes the checklist, size close to the $75 premium cap (e.g. 2 contracts of a
  ~$0.35 option, or 1 of ~$0.70), and allow up to 2 positions at once. Risk limits do NOT change: max loss $15/trade
  (set the stop so qty × (entry − stop) ≤ $15), -$30/day, -$60/week, careful mode after 3 wins, profit lock.
- Bigger size never means weaker setups or wider stops. Take profits fast (+30–50%, sell at bid − 0.01).
- **Premium cap raised to $150/trade for A+ setups only** (user, 11/11 ~12:25 ET: "if you're sure, you can double to $150").
  A+ = all 4 checklist items AND all 3 indexes (SPY/QQQ/IWM) agree, in the 9:45–11:00 or 13:30–14:45 window (v2).
  Max loss per trade stays $15 (so a $150 position needs a stop ≤ 10% away — only when an underlying level allows it).
  Not used in careful mode (half size there). Other setups: ≤ $75.

## Scaling plan for the main strategy (user, 2026-11-11 evening: "scale the current working one, bring up others in parallel")
- **Limits scale with the budget automatically** (% of current budget, recomputed each morning from STATE):
  max loss/trade 5%, daily stop -10%, weekly stop -20%, normal premium cap 25%, A+ premium cap 45%.
  At $330.82: $16.50 / -$33 / -$66 / $82 / $150.
- **2-contract scale-out on A setups** when 2 contracts fit the premium cap: sell 1 at +30%, move the stop on the
  other to breakeven, trail it ~15% under the bid. Same total risk, more of the move captured.
- **Up to 2 positions at once** (e.g., SPY + IWM when all 3 agree), combined open risk ≤ the daily stop's remaining room.
- **Step-up review every Friday:** if the week is positive and the max drawdown stayed < 10%, keep the % rules (size grows
  with the budget). If the week is negative, cut sizes by half for the next week.
- Raising the 5% per-trade risk needs the user's explicit OK.
- **Parallel strategies:** see STRATEGIES.md. Paper first; a strategy that passes (≥10 paper trades, positive, ≥50% wins)
  gets its own live slice of $75 with its own -$15/day stop, after the user's OK.

## Safety additions from the user's research doc (11/11; docs/validated_intraday_options_playbook_v1.txt)
- **Chop filter:** more than 2 VWAP crosses in the last 12 five-minute bars on the traded symbol ⇒ no entry.
- **Quote gate:** nonzero bid, spread ≤ 10% of mid and ≤ $0.15, quote < 10 s old; otherwise skip.
- **Time stop:** exit if the trade shows no progress after 6 completed 5-min bars (30 min); sooner after 13:30.
- **Daily stop also after 3 consecutive losses**, whichever comes first. Never raise size after a loss.
- **Correlated exposure:** SPY + QQQ + IWM same-direction positions count as ONE idea for risk (combined risk ≤ per-trade max).
- Note: the doc's example risk (0.25–0.5% of equity per trade) is below one contract's minimum risk at this account size;
  our 5%-of-budget per-trade cap stays (user-approved), with the paper results deciding any future change.

## Daily goal (user, 2026-11-11 evening)
- User: "Mak1 needs to make at least 10% per day … not telling you to risk the capital; it is core importance to protect it at all costs."
- **Goal: +10% of budget per day (≈ $33 at $330.82). It is a target, NOT a reason to force trades or loosen any limit.**
- How to reach for it without more risk: take every setup that passes the checklist in BOTH windows (9:45–11:00, 13:30–14:45 — v2);
  use full allowed size on A/A+ setups (2-contract scale-out); let winners run with the % trailing stop instead of
  capping at +30%; use 2 positions when all 3 indexes agree.
- Once the day reaches +10%: profit lock at 70% of the day's peak (same as careful mode). Keep trading only A+ setups.
- Honest baseline (11/09–11/11): avg ≈ +$19/day (≈ 6%/day). 10%/day every day compounds to ~7x in a month; expect many days
  below target and some red days. Capital protection wins every conflict.

## Minimize red days (user, 2026-11-11 evening: "we want to put red days to minimum")
- **First trade of the day at half size** (1 contract, ≤ half the normal premium) until the day is green.
- **Once the day is green, never let it turn red:** stop trading for the day if day P&L falls back to ≤ +$0 after
  having been ≥ +$10. Risk on any new trade must fit inside the current day profit (house money only) once green.
- **After the first loss of the day:** A+ setups only, half size. After a second loss: stop for the day.
- **No trade beats a forced trade:** skip anything that is not 3/4 (A) or 4/4 (A+) on the checklist, chop filter passes,
  quote gate passes.
- Weekly: if the week is red going into Friday, Friday is A+ only at half size.

## Risk limits (non-negotiable)
| Rule | Limit |
|---|---|
| Max deployed at once | the whole bankroll (≤ $80), but see per-trade limit |
| Max per single trade (premium paid) | **$75** (25% of $300); at most 2 positions open at once |
| Max LOSS per trade | **$15** (5% of budget) — set underlying stop + broker disaster stop so the worst case ≤ $15 |
| Max daily loss | **-$30** (10% of budget) from the day's start → stop for the day. Also stop when remaining room < one normal stop (~$15) |
| Daily profit lock | No profit cap. Once day P&L ≥ +$20, never let it fall below 50% of the day's peak (stop for the day if it does) |
| Max trades/day | 100 (user 11/09: squeeze every opportunity) — but every trade must still pass the setup checklist; no revenge or boredom trades |
| After 3 winning trades in a day (user 11/09) | "Careful mode": A+ setups only (all 4 checklist items), size ≤ half of normal (≤ ~$25), profit-lock tightens to 70% of the day's peak, and stop for the day after the first loss in careful mode |
| Weekly drawdown kill switch | -$60 for the week (20%) → stop until next Monday, review |
| No new 0DTE entries after | 2:45 PM ET; flat on all 0DTE by 3:15 PM ET (v2) |
| No entries | before 9:45 ET (v2: broker stops only from 9:45); after 14:45; not within 30 min of FOMC/CPI |
| Never | market orders on options, naked short options, averaging down, holding 0DTE into the close |

## Reality check (written 2026-11-09)
User goal: $1,000/week. With $80 of capital that is 1,250%/week — not achievable without
risk of ruin, which violates "capital is highly protected". Working target: grow the account
steadily (+5–10%/week) and scale size only as the account grows. Size rule: risk ≤ 15% of account per trade.

## No pressure to force trades
- "No trade" is a valid, good day. Never take a weak setup just to show a daily profit.
- Report losing days honestly and promptly; never hide or soften a loss.

## What to trade
- Liquid underlyings only: SPY, QQQ (daily 0DTE expirations), IWM. Single names only if the
  bid-ask spread is ≤ 5% of mid and a catalyst is present.
- Prefer ATM / slightly ITM (delta 0.40–0.60) over cheap far-OTM lottery tickets.
  $0.15 contracts lose to theta + spread (see LESSONS).
- Defined-risk debit spreads (level 3 allows) to cut theta and spread cost when IV is high.
- With a $40/trade cap, single ATM SPY/QQQ 0DTE contracts ($150–250) are unaffordable → the
  default vehicle would be a $1-wide 0DTE debit spread — BUT agent multi-leg orders are rejected
  by Robinhood (see LESSONS 11/09). User decision 11/09: no spreads — buy single calls/puts only, still ≤ $40 each.
- **User decision 11/09 (afternoon): calls and puts ONLY — no spreads, no iron condors.** Budget stays
  $80 + own profits. (A $1-wide condor needs $100 collateral > bankroll and would breach the cash floor.)
  Prefer IWM (cheaper strikes, ~0.30 delta for ≤$0.40) over far-OTM SPY/QQQ.

## Time-of-day rule (11/09)
- 9:45–11:00: trend entries OK (v2: breakouts within 0.10% of the level, flags, re-entries).
- 11:00–13:30 (midday): no buying at HOD/LOD. Only VWAP pullback-and-hold or VWAP-loss setups.
  Scan every 10 min. Exit any position that stalls 8–10 min.
- 13:30–15:00: afternoon trend resumption allowed again. No new entries after 15:00.

## Setup checklist (need 3 of 4 before entry)
1. Trend: price vs VWAP + 9/21 EMA on 5m in the same direction.
2. Level: break-and-retest of premarket high/low, prior-day H/L, or opening range (first 15m).
3. Index confirmation: SPY and QQQ agree in direction.
4. No macro event in the next 30 min (CPI, FOMC, jobs, Fed speakers).

## Execution
- **Monitoring cadence (user rule 11/09):** whenever money is at work (open order OR open position),
  check EVERY 30 SECONDS (user rule 11/09, updated). How: Monitor tool running
  `while true; do sleep 30; echo tick; done` (timeout 30 min, re-arm on expiry); each tick → check
  option quote, underlying vs VWAP, stop order. send_later (1-min min, often 2–4 min late) is only a
  fallback. With nothing at work, scan every **2 min** (user rule 11/12: "so we don't miss any opportunity"), all day incl. midday.
- After an entry fills, immediately place a broker-side stop_market sell-to-close at the -35% level
  as a backstop. To take profit: cancel the stop, then sell with a limit at mid.
- Limit orders at mid (or mid + 0.01). If not filled in ~60s, re-evaluate — don't chase > 2 ticks.
- Decide the exit BEFORE entry: take profit at +30–50%, hard stop at -35%.
- On a stop, exit at the bid — do not "wait for it to come back".
- Trailing the broker stop: only after +20%, keep it ≥ 12–15% of the bid below the bid (≥ 0.08 on $0.30–0.50
  options, ≥ 0.12 on $0.80+ options). Taking profit: sell at bid − 0.01 for an immediate fill.
- Every scan: check get_option_orders for orders NOT placed by this session (another agent traded 11/10).

## Daily routine
1. Pre-market (9:00–9:30 ET): read memory files, account, positions, news, economic calendar,
   earnings, SPY/QQQ premarket levels. Write the plan in `journal/YYYY-MM-DD.md`.
2. Session: scan every ~10–15 min for setups; log every trade (time, contract, entry, exit, reason, P&L).
3. Stop when the daily target or daily loss limit is hit.
4. EOD: update `STATE.md`, add lessons to `LESSONS.md`, commit + push, email a summary to the user.

## Mak2 live slice (user, 2026-11-12 ~15:05 ET)
- User approved a small live slice for Mak2 (single-stock post-earnings OR break; first: CSCO 11/13). Limits: ≤ $40 premium,
  ≤ $10 loss/trade, −$15/day for Mak2, max 2 Mak2 trades/day, stop after 1 Mak2 loss. Counts toward the agent daily/weekly stops.
  Spread ≤ 5% of mid. Rules in STRATEGIES.md "Mak2".
- Budget split (user 11/12): Mak2 gets a fixed **$50** sub-budget; Mak1 (core builder) gets the rest and computes its %-limits on
  its own budget. Each strategy's P&L changes only its own budget. Combined daily/weekly stops apply to the total.

## Weekly target (user, 2026-11-12 evening)
- User: "Weekly returns should be greater than $150 at least."
- Recorded as the weekly TARGET (≈ 47% of the $317.73 budget; ≈ $30/day). It does NOT change any risk limit: per-trade, daily
  and weekly stops, half-size first trade, chop filter, and "no forced trades" all still apply. Track progress toward $150 in STATE.
- Honest math: best day so far +$39.73; recent average ≈ +$11/day. Hitting $150 needs ~3 good Mak1 days/week at full allowed
  size on A/A+ setups plus Mak2 contributions. Report weekly progress honestly; never chase it with extra risk.

## High-conviction tier (user approval, 2026-11-12 evening)
- User: "I am okay taking a reasonable risk with a valid strategy... with solid backing on technicals and news you are approved
  to take risk to reach our goal." This is the explicit OK the Scaling plan required to raise per-trade risk — for this tier only.
- **A+ Conviction** = ALL of: checklist 4/4; SPY/QQQ/IWM all agree; chop filter passes; quote gate passes; in the 9:40–11:00 or
  13:30–15:00 window; AND a news/macro reason supporting the direction (checked via NewsMCP/Alpha Vantage, written in the journal).
- Sizing for A+ Conviction (Mak1): max loss per trade **7.5% of Mak1 budget** (≈ $20 at $267.73, vs 5% normally); premium up to the
  A+ cap (45%, ≈ $120); use the 2-contract scale-out. Allowed at full size even as the first trade of the day.
- Unchanged: combined daily stop −10% of total budget; weekly stop −20%; stop after 2 losses; never let a green day turn red;
  exit when the 3-index agreement breaks (LESSONS 11/12); everything else in this playbook. Non-conviction setups keep normal sizing.

## MakB + MakC live today on the Mak2 slice (user, 2026-11-13 ~11:03 ET)
- User: "Run makC and makB with same mak2 budget for today." → B (gap fade) and C (midday VWAP bounce) trade LIVE today only,
  sharing Mak2's $50 sub-budget and limits: ≤ $40 premium/trade, ≤ $10 loss/trade, −$15/day for the whole Mak2 slice (Mak2+B+C),
  max 2 slice trades/day, stop the slice after 1 loss. Spread ≤ 10% of mid & ≤ $0.15 (quote gate). Mak1 keeps priority.
- No extra money: the $50 is shared, not $50 each. Reverts to paper-only after today unless the user extends it.
- B today: SPY gap +0.4% (< 0.7% trigger) → no B signal expected; C is the live candidate (11:00–13:30).
- Update (user, 11/13 ~11:05 ET): "Go for 70$ for makC" → MakC premium cap **$70** today (above the $50 slice; user-approved).
  Max loss per MakC trade stays **$10** (stop sized to it) and the slice's −$15/day stop is unchanged unless the user says otherwise.
- Update (user, 11/13 ~11:09 ET): "Yes for mak2" → Mak2 may trade NU (earnings gap-up continuation) past 11:00 today, using the
  11/20 13C (spread ~5.9%, waived from 5%), ≤ $40 premium, ≤ $10 loss, flat before the close; slice limits unchanged.
- Update (user, 11/13 ~12:05 ET): "Go for it" → Mak2 may use CRWV / INTC puts (0DTE) or NU calls today with spread up to the
  general quote gate (≤ 10% of mid, ≤ $0.15) instead of 5%. Still ≤ $40 premium, ≤ $10 loss, max 2 Mak2 trades/day (1 used), flat by close.
- Update (user, 11/13 ~13:29 ET): "Go for it mak2" → Mak2 #2 may use CSCO 11/20 92P at ~$70–77 premium (above the $40 cap),
  max loss still $10 (stop sized), spread ≤ 10% (quote gate). Today only.
- Update (user, 11/13 ~13:30 ET): "If mak1 is good to go go big on it and skip mak2 risk" → Mak2 CSCO put CANCELLED.
  Mak1 13:30 breakout call (if triggered): 2 contracts (scale-out), premium ≤ $120, max loss ≤ $20 (A+ tier size, user-approved for
  this trade even though the news backdrop is bearish); overrides the half-size first-trade rule for this trade only.
- ~~REMOVED by Controller v2 (11/15)~~ Standing rule (user, 11/13 ~13:52 ET): "Override applied only on go big on or after 2 red days" → the "go big" size override
  (Mak1: 2 contracts, ≤ $120 premium, ≤ $15 loss/trade, still inside the combined daily stop; valid setups only) may be used only
  when the 2 previous/most recent trading days were red (e.g., 11/12 −$13.09 and 11/13 −$12 so far). Otherwise normal post-loss rules.

## Mak3 = strategy B (user, 2026-11-13 evening) — **back to PAPER under Controller v2 (11/15)**
- User: "Bring up B as mak3 and share 60$ from mak1." → Gap fade goes LIVE as **Mak3** with **$60** taken from Mak1.
- Budgets after the move: Mak1 $183.20, Mak2 $51.92, Mak3 $60.00 → total $295.12 (unchanged). Cash floor $3.48.
- Mak3 limits: premium ≤ $45, loss ≤ $10/trade, −$15/day, max 2/day, stop after 1 loss, 9:45–11:00, pause at $30. Rules in STRATEGIES.md.
- Mak1 %-limits now on $183.20: loss/trade $9.16 (5%), −$18.32/day, −$36.64/week, premium cap ≈ $46 (25%), A+ cap ≈ $82 (45%), A+ loss ≈ $13.74.
- Mak3 entry gate (user, 11/13 evening): every Mak3 trade must (1) confirm its own gap-fade trigger, (2) consult Mak1's checklist
  (≥ 3/4 + chop filter + quote gate, no conflict with an open Mak1 position), (3) log the "Mak3 → Mak1" case and Mak1's verdict in the
  journal before ordering. No Mak1 approval = no Mak3 trade. Details in STRATEGIES.md "Mak3".
