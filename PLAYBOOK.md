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

## Risk limits (non-negotiable)
| Rule | Limit |
|---|---|
| Max deployed at once | the whole bankroll (≤ $80), but see per-trade limit |
| Max per single trade (premium paid) | **$40**; at most 2 positions open at once |
| Hard stop per trade | -35% of premium, or thesis invalid, whichever comes first |
| Max daily loss | **-$15** from the day's start → stop trading for the day (capital first) |
| Daily profit lock | No profit cap. Once day P&L ≥ +$20, never let it fall below 50% of the day's peak (stop for the day if it does) |
| Max trades/day | 100 (user 11/09: squeeze every opportunity) — but every trade must still pass the setup checklist; no revenge or boredom trades |
| Weekly drawdown kill switch | -$30 for the week → stop until next Monday, review |
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
  Prefer IWM (cheaper strikes, ~0.30 delta for ≤$0.40) over far-OTM SPY/QQQ.

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

## Daily routine
1. Pre-market (9:00–9:30 ET): read memory files, account, positions, news, economic calendar,
   earnings, SPY/QQQ premarket levels. Write the plan in `journal/YYYY-MM-DD.md`.
2. Session: scan every ~10–15 min for setups; log every trade (time, contract, entry, exit, reason, P&L).
3. Stop when the daily target or daily loss limit is hit.
4. EOD: update `STATE.md`, add lessons to `LESSONS.md`, commit + push, email a summary to the user.
