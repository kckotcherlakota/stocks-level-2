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

## Setup checklist (need 3 of 4 before entry — item 4 (macro) is MANDATORY, user 11/15)
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
- Standing rule (user, 11/13 ~13:52 ET): "Override applied only on go big on or after 2 red days" → the "go big" size override
  (Mak1: 2 contracts, ≤ $120 premium, ≤ $15 loss/trade, still inside the combined daily stop; valid setups only) may be used only
  when the 2 previous/most recent trading days were red (e.g., 11/12 −$13.09 and 11/13 −$12 so far). Otherwise normal post-loss rules.

## Mak3 = strategy B live (user, 2026-11-13 evening)
- User: "Bring up B as mak3 and share 60$ from mak1." → Gap fade goes LIVE as **Mak3** with **$60** taken from Mak1.
- Budgets after the move: Mak1 $183.20, Mak2 $51.92, Mak3 $60.00 → total $295.12 (unchanged). Cash floor $3.48.
- Mak3 limits: premium ≤ $45, loss ≤ $10/trade, −$15/day, max 2/day, stop after 1 loss, 9:45–11:00, pause at $30. Rules in STRATEGIES.md.
- Mak1 %-limits now on $183.20: loss/trade $9.16 (5%), −$18.32/day, −$36.64/week, premium cap ≈ $46 (25%), A+ cap ≈ $82 (45%), A+ loss ≈ $13.74.
- Mak3 entry gate (user, 11/13 evening): every Mak3 trade must (1) confirm its own gap-fade trigger, (2) consult Mak1's checklist
  (≥ 3/4 + chop filter + quote gate, no conflict with an open Mak1 position), (3) log the "Mak3 → Mak1" case and Mak1's verdict in the
  journal before ordering. No Mak1 approval = no Mak3 trade. Details in STRATEGIES.md "Mak3".

## Strategy fixes + Mak4 (user, 2026-11-15)
- Mak1: news check mandatory; ADX/VWAP day-type gate (range day → Mak1 off, Mak4 on); trailing vs fixed exit logged on every trade.
- Mak2: close outside OR + successful retest; IV / expiration / OI / spread check before entry.
- Mak3: rejection → acceptance across VWAP → failed retest; fade exhaustion gaps only, never trend gaps.
- Mak4 (VWAP range mean reversion) LIVE on good setups only, SPY first, 10:15–14:30, up to $60 drawn from Mak1's budget, ≤ $45 premium,
  ≤ $10 loss, max 2/day, stop after 1 loss. Details in STRATEGIES.md "Mak4".

## Mak1 news filter for sideways markets (user, 2026-11-15)
- Check NewsMCP at 9:15, every 30 min from 9:30 to 15:00, and before each Mak1 entry if the last check is more than 15 min old. Tag each check CATALYST, QUIET or RISK and log it in the journal.
- QUIET + RANGE/UNCERTAIN day-type = sideways: no Mak1 breakouts; Mak4 runs instead.
- CATALYST: Mak1 is allowed only after the day-type confirms (TREND, or ADX ≥ 20 and rising) and all 3 indexes confirm.
- RISK: no new Mak1 entries; tighten stops on open trades. Details are in STRATEGIES.md under "Mak1 fixes".

## Premium cap lifted for Mak1 (user, 2026-11-16 10:10 ET)
- "You have money, why IWM, you can use the entire budget." Mak1 may spend up to its whole $183.20 budget on premium for one trade, so it can buy the best contract (SPY/QQQ ATM) instead of a cheaper index.
- Loss limits do NOT change unless the user says so: per-trade loss is set by the stop (go-big day: max $15), and the daily stops still apply (Mak1 −$18.32, combined −$29.51).

## Mak4 fired up on user command (user, 2026-11-16 11:40 ET)
- "Fire up mak4." The user overrides Mak4's ADX < 20 regime gate for today's midday range (SPY has held about 743.3–747.3 around VWAP since 10:20, but ADX still reads 34 from the morning trend).
- All other Mak4 rules still apply: SPY first; Bollinger Band (20,2) 5-min edge plus a rejection candle plus an RSI turn from 35/65; target VWAP; R:R ≥ 1.5; ≤ $45 premium; ≤ $10 loss; max 2; stop after 1 loss; window ends 14:30; it stays inside the combined daily stop.
- "In parallel" (user, 11:41): Mak4 runs alongside Mak1, not only when Mak1 is off. It scans SPY, QQQ and IWM, with SPY preferred.
  Never take a Mak4 trade opposite an open Mak1 trade on the same index. The combined daily stop (−$29.51) caps both together.

## Full-session scanning, all 4 strategies (user, 2026-11-16 15:10 ET)
- "Holidays are coming, so there are fewer trading days. Keep searching for opportunities during trading hours, completely, on all 4."
- Scan every 2 minutes from 9:30 to 15:45 ET on every trading day, for Mak1, Mak2, Mak3 and Mak4. The old per-strategy time windows no longer block scanning.
  An entry outside a strategy's normal window needs an A/A+ setup, and no new 0DTE entry after 15:30 (time decay and the sellout at 15:45).
- All risk rules stay: per-trade loss caps, the combined daily stop, no chasing (one limit at mid; skip if missed), and all-3 agreement for Mak1.
  On a green day, stop if the day P&L falls back to half of its peak.

## Mak4 from the open (user, 2026-11-17 08:52 ET)
- "Look for Mak4 entries as well from start." Mak4 scans from 9:30 and may enter from 9:40 (the no-entries-in-the-first-10-min rule still applies),
  not only from 10:15. Early-session BB(20)/RSI(14) on 5-min bars use the prior session's bars for warm-up.
- All other Mak4 rules still apply: regime check, BB edge + rejection candle + RSI turn, target VWAP, R:R ≥ 1.5, ≤ $45 premium, ≤ $10 loss,
  max 2/day, stop after 1 loss, never opposite an open Mak1 trade on the same index, inside the combined daily stop.

## Mak4 uses Mak1's limits (user, 2026-11-17 10:13 ET)
- "Mak4 shares same loss cap of Mak1." Mak4's per-trade loss cap = Mak1's (5% of the Mak1 budget: $11.30 at $225.93) instead of $10,
  and Mak4 may use Mak1's premium allowance (up to the Mak1 budget, so SPY/QQQ near-ATM contracts are allowed) instead of $45.
- Mak4 and Mak1 losses count against ONE shared Mak1 daily stop (−$22.59) and the combined agent stop (−$33.79). Other Mak4 rules unchanged
  (regime, BB edge + rejection + RSI turn, target VWAP, R:R ≥ 1.5, max 2/day, stop after 1 loss, never opposite an open Mak1 trade).
- **Update (user, 2026-11-17 10:16 ET): "Raise Mak4 loss cap to $20."** Mak4 max loss per trade = **$20** (broker stop sized to it).
  Still inside the shared Mak1 daily stop (−$22.59) and the combined stop (−$33.79): one Mak4 loss uses most of the day's room,
  so after a Mak4 loss the day is done for Mak1/Mak4. Mak4 stays 1 contract, max 2/day, stop after 1 loss, R:R ≥ 1.5.

## Fast fills (user, 2026-11-17 11:03 ET: "Be quick, we missed 2, that's bad")
- On a valid entry signal, place the limit at the ASK (marketable limit) when the spread is ≤ $0.03, instead of at mid; otherwise mid + half the spread.
  One order per signal; if it still misses, the setup is gone (no chasing a second, higher price).
- Pre-arm: when a trigger is 1 bar away, have the contract, a fresh quote and the stop price ready so the order goes out within seconds of the bar close.
- 11:34 user: "Yes go with HD put, $20 loss cap" → one-time Mak2 exception: HD 11/20 put above the $40 premium cap, max loss $20 (broker stop).
- Wording fix (fast fills): when the spread is > $0.03, enter at mid + ¼ of the spread (not the full ask); one order per signal.
- 11:58 user: "Look out for Mak1 and Mak4, and cap Mak2 loss to $10." → today's red-day stand-down is overridden for Mak1/Mak4.
  Mak2 max loss back to $10/trade (no more premium exceptions). Combined daily stop −$33.79 still applies (room ≈ $22.6 at −$11.18),
  so any new trade's stop must fit inside the remaining room. Thin single-stock options: also exit by hand when the bid nears the stop.

## Mak1 + Mak4 run until the weekly goal (user, 2026-11-17 12:06 ET)
- "Mak1 and Mak4 need to run until the weekly goal is reached." → the daily stop (−10%) and the Mak4 max-2-trades/day limit are lifted for Mak1/Mak4
  while the week is below its target (STATE: $100/week; +$12.46 at 12:06 Tue → $87.54 to go).
- Still in force: per-trade loss caps (Mak1 $11.30, Mak4 $20, Mak2 $10), every setup/quote/chop rule, no chasing, one order per signal,
  broker stop on every fill, flat by 15:45, no new 0DTE after 15:30, and the **weekly kill switch −20% (−$67.57 for the week)** as the last backstop.
- Once the week reaches the goal: back to normal rules (profit lock, daily stop).
- **Update (user, 2026-11-17 12:31 ET): "Raise Mak1 loss cap to $20."** Mak1 max loss per trade = **$20** (broker stop sized to it), same as Mak4.
  Weekly kill switch (−$67.57) still the backstop; one order per signal, setup/quote/chop rules unchanged.
- 12:42 user: "If you think we can cover the weekly goal in the rest of the days, you can stop; if you cannot, think." → Decision: **stop trading for
  today** (chop ahead of NVDA, 4 losses). Weekly goal stays the target for Wed–Fri (≈ $114.63 needed from −$14.63). Plan in the journal.

## Mak5 = intraday stock trades (user, 2026-11-17 12:47 ET: "do it across the entire stock universe, buy and sell at profit, while not doing Mak1–4")
- Long only, whole shares, regular hours, flat by 15:45. Universe: stocks $10–250, day volume > 3M, relative volume > 1.5 (Robinhood scan).
- Size: up to $250 per trade (agent cash only; floor $3.48 untouched); max loss **$10/trade** via broker stop_market; max 3 trades/day; stop after 2 losses.
- Setup: a mover above VWAP that pulls back to support/VWAP and holds (no buying spikes at the high); R:R ≥ 1.5 to the high of day; spread ≤ 0.3%.
- Never while a Mak1–4 position is open; counts toward the weekly kill switch. Same-day round trips count as day trades (no PDT alert seen on 11/17 review).

## Alpha = stock buy/sell for profit (user, 2026-11-17 12:48 ET) — replaces the Mak5 draft above
- "Consider this as Alpha. When we are done with options, focus on buying and selling at a profit. You can use the complete budget, but never sell at a loss."
- Runs only when Mak1–4 are done for the day (or flat). Size: up to the full agent cash (cash floor $3.48 untouched).
- **No stop-loss: a position is sold only at a profit** (target +1.5–2% after costs; limit sell). A losing position is held (overnight/multi-day) until it recovers.
- Because losers are held, Alpha buys only names that recover well: liquid large caps (market cap > $20B, day volume > 2M, spread ≤ 0.05%) or broad ETFs,
  bought on a pullback to support/VWAP — never news spikes, biotech pumps or penny stocks.
- Trade-off (agent note): cash tied up in an underwater Alpha position is not available for Mak1–4 the next morning; I report it in every roll-up.
- Update (user, 12:50): "...unless the stock is going really bad." → Alpha exception: sell at a loss only when the stock is clearly going bad:
  (a) down ≥ 5% from entry, or (b) bad company news (downgrade, guidance cut, fraud/legal), or (c) a daily close below its prior-day low after
  entry with the market not to blame. A broker GTC stop_market sits at −7% as a disaster backstop. Otherwise hold for the profit target.
- Update (user, 12:51): "Use Alpha as an additional money maker during choppy days for the Maks." → Alpha's main use: on choppy/range days when Mak1–4
  have no clean setups (sideways rule, VWAP chop), Alpha trades large-cap pullbacks. On trend days the Maks have priority and Alpha stays small or flat.
- Update (user, 12:53): "Try holding the stock or average instead of a loss." → Alpha **scales in**: buy ~half the Alpha budget first, keep half in cash
  to average down once at −3% from the first entry (only if there is no bad news and the stock's daily trend is intact). The sell target becomes
  +1.5% over the average price. Exits at a loss only on bad company news or the broker GTC disaster stop at −10% from the average.
  (The general "never average down" rule still applies to options/Mak1–4.)
- Update (user, 12:55): "By end of day keep the stocks liquid for the Maks to use the next day, unless we are really bad at losses."
  → Alpha positions are sold by **15:50 ET** every day (limit at bid − 0.01) if P&L is a profit or a small loss (better than −2% from average).
  Only a position down more than 2% is held overnight (then the average-down / recover plan continues). Cancel the GTC target before the EOD sale.
- Update (user, 12:56): "With Alpha and the Maks, rest only once the weekly goal is met; squeeze every opportunity and save the capital."
  → No stand-down until the weekly goal ($100) is met: scan Mak1–4 and Alpha every 2 min, 9:30–15:45, every day. Capital guards stay:
  per-trade caps ($20 Mak1/Mak4, $10 Mak2), one order per signal, broker stop on every option fill, exits keep the stop live, weekly kill
  switch −$67.57, Alpha flat by 15:50 unless down > 2%. Today's extra guard: stop after one more options loss.

### Mak4 range-edge trades (user, 2026-11-17 14:28 ET: "Go ahead with Mak4 range trades")
- On a confirmed range day (repeated VWAP rejections, failed breakouts both ways), Mak4 may fade the range EDGES without
  needing a Bollinger-band break / RSI extreme: CALL when SPY tags the range low and holds (a bar that does not close
  below it / a higher low); PUT when SPY tags VWAP / range high and is rejected (bar closes back below it).
- Target: the middle / opposite side of the range. Stop: just beyond the edge, sized so the loss ≤ $20 (Mak4 cap).
  Broker stop_market right after the fill. Entry at the ask if spread ≤ 0.03. No new 0DTE after 15:30.
- Never enter mid-range. Premium must fit buying power (≤ BP, keep the cash floor).

### Weekly limit raised by $50 + Wed 11/18 sizing (user, 2026-11-17 after close: "Option 2, raise limit by $50")
- Weekly kill switch for the week of 11/16: **−$117.57** (was −$67.57). Week at −$38.90 → **$78.67 of room**.
- Goal for Wed 11/18: try to win back today's −$81 on the NVDA gap. No promise: ≈1-in-4 odds, needs a clean trend day.
- Sizing Wed: **2 contracts** on an A-setup only (Mak1 all-3 trend from the open, or Mak3 gap fade), ATM-ish SPY/QQQ ≈ $1.00–1.40 each,
  premium ≤ buying power minus the $3.48 floor. Max loss per trade **$40** (structure stop). Scale out: sell 1 at +50%, trail the other
  (BE at +20%, then ~15% under the bid). Keep the broker stop live; no cancel-then-chase.
- Wed day guard: stop after 2 losing trades or if the day reaches −$50, whichever comes first. Never break the week floor (−$117.57).
- Applies to 11/18 only; Thu/Fri sizing goes back to 1 contract / $20 unless the user says otherwise.

### Trade score (user, 2026-11-17 after close)
- Every good trade (closed green) = **+5,000 points**; every bad trade (closed red) = **−10,000 points**.
- A loss costs twice what a win earns → only A-setups; a skipped B-setup scores 0, which beats −10,000.
- Track the running score in STATE.md and the journal EOD summary. Starts Wed 11/18 at 0
  (for reference, Tue 11/17 would have scored 1 × +5,000 and 6 × −10,000 = −55,000).
- **No negative-point days (user, 2026-11-17).** Day score must end ≥ 0. Agent rules to serve this (no trade = 0 points is always allowed):
  1. First trade of the day: A+ only (all-3 agreement, clear level, R:R ≥ 2, fresh quote, entry at a retest not a chase).
  2. Take profit fast: sell 1 contract at +30–50% so a winner is banked green; trail the rest from breakeven.
  3. After a loss (−10,000), two wins are needed to get back to 0 → keep trading ONLY A-setups at 1 contract (smaller $ risk),
     and only while the money guards allow (Wed: 2 losses or −$50 = stop; weekly floor −$117.57). Money guards win over points.
  4. Once the day is ≥ +5,000, stop after any loss would take it below 0 → i.e. with +5,000, take at most one more trade only if A+.
  - Honest limit: a loss can't be ruled out on any trade; the only guaranteed non-negative day is a no-trade day.
- **Weekly score must only go up (user, 2026-11-17).** Score resets to 0 every Monday. Each day the running weekly score must be
  ≥ the previous day's. If a day ends with a lower score than the day before (any negative day), the weekly score drops to **0**.
  → A red day wipes the whole week's points. The bigger the banked score, the more selective I get (A+ only, 1 contract,
  stop for the day after the first green trade once the week has banked points).
