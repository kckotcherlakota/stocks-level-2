# LESSONS (newest first)

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
