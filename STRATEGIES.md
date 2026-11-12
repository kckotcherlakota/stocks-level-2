# STRATEGIES — main + parallel experiments (user, 2026-11-11 evening)

User: "We should parallel try other strategies while this [main] remains our main working one."

## Main (live, unchanged)
**A. Index-agreement 0DTE** — SPY/QQQ/IWM all agree; opening-range break or VWAP loss/hold; 9:40–11:00 and 13:30–15:00.
Rules in PLAYBOOK. Record: 11/09 -9.54, 11/10 +39.73, 11/11 +26.91.

## Experiments (PAPER first, zero money)
Each scan, check these too. When one triggers, log a paper trade in the journal's "Paper trades" table using real
option quotes: entry = ask, exit = bid, same stop/target rules as live. A strategy goes live only after ≥ 10 paper trades
with positive total P&L and win rate ≥ 50%, and only with the user's OK.

| ID | Strategy | Trigger | Vehicle | Exit |
|---|---|---|---|---|
| B | **Gap fade** | Gap ≥ 0.7% vs prior close; after 9:45 price fails at the OR high (gap up) / OR low (gap down) and loses VWAP | 0DTE put/call, delta ~0.30 | Target: 50% gap fill or prior close; stop: back above OR high/low |
| C | **Midday VWAP bounce** | 11:00–13:30, trend day: first pullback that touches VWAP and holds 2 bars, all 3 indexes | 0DTE, delta 0.35–0.45 | +30–40%; stop: 5-min close beyond VWAP |
| D | **1DTE afternoon** | Same setups as A but after 13:30, using the next-day expiry (less theta) | 1DTE, delta ~0.40 | +25–35% same day; stop -25%; never hold overnight unless user approves |
| E | **Single-stock catalyst** | Day after earnings in a liquid name (e.g., CSCO 11/13); opening-range break with spread ≤ 5% of mid | Weekly call/put, delta ~0.40 | +30–50%; stop: back inside OR |

## Research spec (user's doc, 11/11: docs/validated_intraday_options_playbook_v1.txt — "paper-trading research only")
Fixed definitions for all paper experiments (log every gate + rejection reason):
- Signals on **completed 5-min bars** only; session VWAP from 9:30; EMA(9)/EMA(20) on 5m closes ("rising" = > value 3 bars ago);
  ATR(14) on 5m; RVOL = cumulative volume to time t ÷ median of the prior 20 sessions at the same t.
- **15-min opening range** (9:30–9:45), frozen at 9:45; no ORB signal before.
- **Chop filter:** > 2 VWAP crosses in the prior 12 bars ⇒ NO TRADE.
- **Contract gate:** |delta| 0.40–0.65 (test vs 0.25–0.40), spread ≤ 10% of mid AND ≤ $0.15, nonzero bid, fresh quote.
- **Sizing:** qty = floor(min(risk budget ÷ modeled per-contract loss at the stop, premium cap ÷ debit)).
- **Exits (test arms):** structural stop; option loss guard; 1.5R / 2R / partial; trail after favorable move; time stop if no
  progress after 3 / 6 / 9 bars. Paper fills: entry at ask, exit at bid.
- Extra paper variant **A2 = 15m-ORB + EMA9>EMA20 + RVOL ≥ 1.5 + retest entry** (compare to live A's 10m OR).
- SPY/QQQ divergence (SMT) and RSI(14) > 50 / < 50 are optional filters: log them, don't require them.

## Scoreboard (paper)
| ID | Trades | Wins | Paper P&L | Status |
|---|---|---|---|---|
| B | 0 | 0 | $0 | paper |
| C | 0 | 0 | $0 | paper |
| D | 0 | 0 | $0 | paper |
| E | 0 | 0 | $0 | paper |
| A2 | 0 | 0 | $0 | paper |

Notes from past days (hindsight, not counted): 11/10 the 9:57 gap-fill call was effectively strategy B's mirror (fill up) and won;
11/11 had no clean midday VWAP touch (C would have had no trade).
