# LESSONS (newest first)

## 2026-11-13 — −$22.61 day: range-day breakout buys + "go big" size; broker outage cost the trend leg
- **Broker outage:** Robinhood MCP was down 09:30–10:20; the real move (SPY 760→748, CSCO OR-low break 9:50) happened then. Wake-up
  fired 50 min late too. Fixes: retry/alert rule (CLAUDE.md) and earlier Monday trigger.
- **Afternoon = range, not trend.** SPY/QQQ/IWM tested the same ceiling 5× (13:30–14:11). Every 5-min close above it faded within
  1–2 min (IWM 277C −$14, SPY 755C $0, IWM 277C −$10). Rule: **after 2 failed breakouts of the same level, stop buying breakouts there**;
  wait for a retest-and-hold (pullback to the broken level that holds a full bar) or skip.
- **Fast exits worked:** exiting when 2 of 3 indexes lost the level kept losses at −$14/−$10 instead of the −$20/−$14 stops, and the
  breakeven stop turned the SPY trade into a scratch. Keep this.
- **Size after a loss:** "go big" (2 contracts) on a range day doubled the damage. Size up only for A+ trend setups, never for range breakouts.
- **Mak2 single-stock options:** CRWV/INTC/CSCO weeklies had 7–30% spreads midday; only NU (cheap stock, tight weekly) was tradable.
  Pre-screen spreads before the open; the CSCO 0DTE spread at the 9:50 signal is unknown (offline).
- **Mak2 NU +$1.92:** time stop after 30 min with +13% peak; a slow grinder needs a larger move — fine as a scratch-plus.

## 2026-11-12 — SPY 756P: −$13.09 — marginal VWAP loss on a chop afternoon; exit when the agreement breaks
- Entry 14:03 when QQQ slipped 15¢ under VWAP; SPY's two closes were only 3¢ / 22¢ under VWAP. Too marginal on a day with
  repeated VWAP crosses. Need a clear close below VWAP on ALL 3 (not a tick), or skip.
- 30-s checks ran (14:04:25, :55, 14:05:25, :55, 14:06:25). At 14:05:55 the put was bid 0.30 (−$6) and QQQ had already
  reclaimed VWAP — the 3-index agreement that justified the entry was gone. I held because my manual stop was SPY-only (>759.1).
  The disaster stop then filled at 0.23 at 14:06:20, between checks. **Rule: if any of the 3 reclaims VWAP while in a VWAP-loss
  put (or loses it in a call), exit at bid − 0.01 immediately** — that would have been ~−$6 instead of −$13.

## 2026-11-11 (evening) — Process: goals vs. risk
- A daily % goal is useful only as a direction for effort (more qualifying setups, both windows, better exits), never as a
  reason to take B-grade trades or widen stops. Red-day minimization rules now enforce this (PLAYBOOK).

## 2026-11-11 — SPY 759C: +$26.91 (0.64 → 0.91 in 7 min) — patience through chop, then the first clean break
- 75 minutes of VWAP chop with SPY/QQQ vs IWM divergence: 9 scans, no trade, no loss. The all-3 filter kept me out.
- Entry 10:53: SPY broke its OR high, QQQ at HOD, IWM above VWAP and rising (not at its OR high). Delta 0.36, $64.
- %-based trailing stop (≈15% under the bid: 0.50 → 0.55 → 0.68 → 0.70 → 0.76) survived a 0.80 → 0.72 dip that a fixed
  8¢ trail might also have survived, but kept the lock tighter as it rose. Exit at bid − 0.01 filled 0.91 (a penny better).
- Midday breakouts (12:28 all-3 HOD, 13:21 SPY/QQQ) both stalled within minutes — the no-chase midday rule held up again.

## 2026-11-10 — SPY 745P: +$3.91 (could have been +$13): trailing stop too tight for a $0.80 option
- Fixed "8¢ under the bid" works for $0.30–0.50 options but a $0.80 option swings ±10¢ on noise.
  Trail by ~12–15% of the bid (≥ 0.10–0.12 for $0.80 options), or trail only after +30%.
- Still positive: the stop turned a +$13 open gain into +$4 instead of a loss.

## 2026-11-10 — IWM 278P: +$12.91 — VWAP-loss put after gap-fill rejection
- Skipped the first VWAP dip (10:28, whipsawed back in 1 min); took the second one only after a clear
  lower-high/lower-low sequence (10:40). Patience on the first touch avoided a loss.
- Exit friction again: a limit AT the bid can miss when the 0DTE quote ticks down. When taking profit,
  sell at bid − 0.01 so it fills immediately (cost: $1; benefit: no unprotected minutes).

## 2026-11-10 — IWM 282C gap-fill: +$22.91 (0.30 → 0.53) — the playbook working
- Waited through a failed QQQ-only breakout (9:45) for all 3 indexes to clear the 10-min opening range
  (9:57). Index agreement filter saved a whipsaw.
- CPI-day IV made near-ATM unaffordable; 1 strike further OTM (delta 0.23) still worked because the move
  came fast in the first hour.
- Trailed broker stop only as bid rose (0.19→0.29→0.34, always ≥0.08 under bid); sold AT THE BID as soon as
  it neared target → filled better than limit (0.53). 4 minutes in the trade.

## 2026-11-09 ~15:00 — iron condor test: REJECTED (same multi-leg block)
- Test SPY 745/746P–760/761C condor (non-fillable 0.90 credit) → "multi-leg strategy cannot be sent for
  approval yet — NOT placed". Approval setting read false (updated 14:40 ET). Agent multi-leg is
  blocked platform-side regardless of the setting. Don't retest unless the user says Robinhood changed it.

## 2026-11-09 EOD — day -$9.54 (1W / 4L) on a +2.4% SPY trend day
- Best edge today was the open → 10:45 trend. 4 of 5 trades were after 10:59 and lost a combined -$17.36.
- Afternoon 0DTE (SPY 754C @ 13:50, 2h10m to expiry): theta ≈ entire premium over remaining time; 3 min of
  sideways cost $10. Afternoon entries need immediate momentum; exit within 2–3 min if no follow-through.
- Process wins: every loss was capped and planned; cash floor never at risk; stopped when remaining
  daily room < one normal stop.
- Next day focus: 9:40–11:00 window, underlying-based stops, take +30–50% at the bid, max 1–2 trades
  after 11:00 and only A+ (VWAP pullback-hold).

## 2026-11-09 — midday HOD breakout (IWM 282C): -$2.09; day back to ≈ flat
- 2 of my 4 trades today were "buy at HOD" after 11:00 on a 2.5-hour-old trend; both failed (-$8.27).
  The one clean win (+$8.91) was earlier, at 10:44, re-entering a fresh trend.
- Rule: from 11:00–13:30, NO buying at HOD (flags/breakouts). Only (a) pullback to VWAP that holds, or
  (b) VWAP loss for puts. Scan every 10 min in that window, not 5.
- Exiting a stall early (−$2 instead of −$5 at the stop) was right.

## 2026-11-09 — IWM 282C x2 flag at HOD: -$6.18
- Trend was 2.5 h old and SPY/QQQ were extended (+2.2% / +3.4%); the "flag" at 11:04 broke after
  one small push. Late-morning (11:00–14:00) flags on an extended trend fail more often.
- Far-OTM (delta 0.21) magnifies this: needs follow-through quickly or theta + noise take it.
- Rule: after ~11:00 on a trend day, require a pullback toward VWAP / 9-EMA (not a flag at HOD) and
  prefer delta ≥ 0.30. Being up on the day, don't hand it back on marginal setups.

## 2026-11-09 — IWM 281C re-entry: +$8.91 (0.27 → 0.36)
- What worked: re-entering a clean trend after a stop-out; stop on the underlying (IWM swing low)
  held through a 279.755 wick that a premium-based stop would have hit; disaster stop moved up only
  once +26% and kept 0.09 under the bid.
- Exit friction: at target I cancelled the stop then placed a limit AT the target (0.39) — the
  quote dipped 4¢ in seconds and I had to cancel/replace. When taking profit on 0DTE, sell at the
  BID (or bid+0.01) immediately; the extra penny isn't worth the unprotected seconds.

## 2026-11-09 — IWM 280C 0DTE: +$10 open gain became -$1.09 (stop too tight)
- Raised the stop to 0.45 (2¢ under 0.47 entry) when bid hit 0.56. The 0DTE option swung
  0.47 ↔ 0.57 every few minutes on normal noise; a 1-minute dip hit the stop, then it bounced to 0.53.
- Rule: don't trail a 0DTE stop to breakeven on premium noise. Either (a) trail only after +30%
  and keep it ≥ 0.08 below the bid, or (b) use the UNDERLYING as the stop (e.g. IWM < VWAP or
  < last 5-min swing low) and exit manually; keep the broker stop only as a disaster stop.
- Take profit faster on choppy grinds: +$9–10 was available at 10:27 (bid 0.56). With a
  $20 daily target and a $47 position, taking +20% ($9) on a stall is fine.
- Every 30 s check must include ORDER/POSITION state, not just quotes (missed the fill by ~2 min).

## 2026-11-09 — platform limit: agent cannot place multi-leg (spread) orders
- place_option_order with 2 legs fails: "this account requires the customer to approve agent-placed
  trades, and a multi-leg strategy cannot be sent for approval yet". Approval setting reads false
  anyway. Re-test occasionally; until it works, spreads are NOT available.
- With a $40/trade cap and single legs only, near-ATM SPY/QQQ/IWM 0DTE ($80–240) don't fit.
- Day was a strong gap-and-go (SPY +1.7% by 9:56): pullback-to-VWAP entry never came. On trend
  days after a big selloff, use a flag/consolidation break as the entry, not a deep pullback.

## 2026-11-09 — review of prior agent trades (Nov 5–6): net ≈ -$15 on 6 round-trips
| Date | Contract | Entry | Exit | P&L |
|---|---|---|---|---|
| 11/05 | SPY 726P 0DTE x1 | 0.18 | 0.14 | -$4 |
| 11/06 | QQQ 669C 0DTE x1 | 0.48 | 0.54 | +$6 |
| 11/06 | RIOT 17C 0DTE x2 | 0.15 | 0.22 / 0.17 | +$9 |
| 11/06 | QQQ 645P 0DTE x1 | 0.53 | 0.40 | -$13 |
| 11/06 | IONQ 31.5C 0DTE x2 | 0.20 | 0.16 | -$8 |
| 11/06 | RIOT 18.5C 11/13 x1 | 0.63 | 0.58 | -$5 |

- Win rate 2/6. Winners small (+$6, +$9), losers bigger (-$13). Need avg win ≥ 1.5× avg loss.
- Pattern: optimistic exit limits were placed, then cancelled and walked down repeatedly,
  ending at the bid. Set the exit plan BEFORE entering.
- 5 trades on 11/06 across 4 tickers = scattered, no edge. Max 4/day, focus on SPY/QQQ.
- Far-OTM cheap contracts (0.15–0.20) on single names (RIOT, IONQ) have wide spreads → avoid.
