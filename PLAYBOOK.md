# PLAYBOOK — hard rules (capital protection first)

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
  A+ = all 4 checklist items AND all 3 indexes (SPY/QQQ/IWM) agree, in the 9:40–11:00 or 13:30–15:00 window.
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
- How to reach for it without more risk: take every setup that passes the checklist in BOTH windows (9:40–11:00, 13:30–15:00);
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
| No new 0DTE entries after | 3:00 PM ET; flat on all 0DTE by 3:45 PM ET |
| No entries | first 10 min after open (9:30–9:40) unless a clear gap setup; not in the minute of FOMC/CPI |
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
- 9:40–11:00: trend entries OK (breakouts, flags, re-entries).
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
  fallback. With nothing at work, scan every 10–15 min.
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
