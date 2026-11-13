# STRATEGIES — main + parallel experiments (user, 2026-11-11 evening)

User: "We should parallel try other strategies while this [main] remains our main working one."

## Main (live) — **Mak1** (user's name, 11/11): the ONLY live strategy and it has the COMPLETE budget
**Mak1 (A). Index-agreement 0DTE** — SPY/QQQ/IWM all agree; opening-range break or VWAP loss/hold; 9:40–11:00 and 13:30–15:00.
Rules in PLAYBOOK. Record: 11/09 -9.54, 11/10 +39.73, 11/11 +26.91, 11/12 -13.09.


**Priority (user 11/12): Mak1 is the PRIMARY money maker.** Mak1 setups always come first (attention, budget, monitoring);
Mak2 is secondary and must never take budget or attention from a live Mak1 setup or position.

## Mak3 (LIVE, user 11/13 evening: "Bring up B as mak3 and share 60$ from mak1") — Gap fade on SPY/QQQ/IWM
- **Budget: $60** (moved from Mak1). Own P&L adds to / subtracts from its $60. If it falls to $30, pause Mak3 and ask the user.
- Note: promoted with 0 paper trades — user's explicit choice; treat the first 10 trades as the validation sample and report the record.
- **Trigger (strategy B):** index gaps ≥ 0.7% vs prior close; after 9:45 price fails at the OR high (gap up → put) / OR low (gap down → call)
  AND loses (or reclaims) VWAP. Prefer agreement of all 3 indexes; trade the one with the cleanest failure.
- **Vehicle:** 0DTE put/call, delta ~0.30–0.45, quote gate (spread ≤ 10% of mid, ≤ $0.15).
- **Limits:** premium ≤ $45, max loss $10/trade (broker stop sized to it), −$15/day for Mak3, max 2 Mak3 trades/day, stop after 1 loss.
  Window 9:45–11:00 only. Counts toward the combined agent daily/weekly stops.
- **Exits:** target 50% gap fill or prior close (sell at bid − 0.01, scale 1 at +30% if 2 contracts fit); stop = 5-min close back
  beyond the OR high/low; time stop 30 min.
- **Mak1 sign-off required (user 11/13: "Mak3 should work by confirming the setup and consulting mak1 and convince it for trade"):**
  1. *Confirm:* Mak3's own trigger is complete (gap ≥ 0.7%, 5-min close back inside the OR after the failed high/low, VWAP lost/reclaimed).
  2. *Consult Mak1:* run the Mak1 checklist on the fade direction: (a) price vs VWAP + 9/21 EMA agree, (b) level = OR/prior-day H/L
     break-and-fail, (c) SPY & QQQ agree (IWM too for full score), (d) no macro event in 30 min; plus chop filter (≤ 2 VWAP crosses in
     12 bars) and quote gate.
  3. *Convince:* Mak1 approves only at ≥ 3/4 checklist + chop filter + quote gate, AND no open Mak1 position in the opposite direction.
     If Mak1 already holds the same direction/index, Mak3 may not add (one idea = one risk).
  4. Write the case in the journal before the order: "Mak3 → Mak1: <setup>, checklist x/4, chop ok, quote ok → APPROVED/REJECTED (why)".
     No approval = no trade.
- Priority: Mak1 first; Mak3 must not take attention from a live Mak1 position. Mak1 and Mak3 in the same index/direction count as ONE idea for risk.
- Record (Mak3): —

## Mak2 (LIVE, small slice — user 11/12 ~15:05 ET: "Let's try new strategies mak2 with csco"; chose "Small live slice")
**Single-stock post-earnings opening-range break.** First instance: CSCO on Fri 11/13 (CSCO reports 11/12 after close).
- **Mak2 budget: $50** (user 11/12: "allocate some budget for mak2 but core builder is mak1"), carved from the $317.73 agent budget.
  Mak2's own P&L adds to / subtracts from its $50. If it falls to $25, pause Mak2 and ask the user.
  Per trade: up to **$40 premium, max loss $10; −$15/day Mak2 stop**.
- **Mak1 budget: $183.20** (11/13 EOD $243.20 − $60 moved to Mak3, user 11/13). Mak1's %-limits are computed on its own budget (5% = $9.16 loss/trade, 10% = −$18.32/day). Mak2/Mak3 P&L count toward the same daily/weekly agent limits.
- Never hold through the earnings print; enter only after the reaction.
- Setup (after 9:45 ET): 15-min opening range (9:30–9:45) frozen. Trade in the gap direction only: gap up → call on a 5-min close above
  the OR high that holds (no immediate reclaim); gap down → put on a 5-min close below the OR low. Skip if the gap is < 2% or the
  stock is back inside the prior-day range (no clear reaction).
- Contract: nearest weekly (11/13 or next Fri), |delta| 0.35–0.45, spread ≤ 5% of mid (PLAYBOOK single-name rule), nonzero bid.
- Exits: stop = 5-min close back inside the OR (plus broker disaster stop sized so loss ≤ $10); take profit +30–50% at bid − 0.01;
  time stop 30 min; flat by 11:00 ET on day one (morning-only test).
- Max 2 Mak2 trades/day; stop after 1 loss.
- Record (Mak2): 11/13 NU 11/20 13C 1× 0.39→0.41 **+$1.92** (time stop). CSCO 9:50 signal missed (broker offline); CRWV/INTC/CSCO-put skipped (spreads 7–30%). Slice $51.92.
- MakB/MakC live-for-a-day (11/13, user): no qualifying signal (no 0.7% gap; VWAP touches never gave a clean rejection on all 3).

## Experiments (PAPER ONLY, zero money — user 11/11: "keep testing these")
**Priority (user 11/12):** keep the paper experiments running and logged every scan, but **Mak1 comes first until the day
has logged a profit**. If a Mak1 setup and a paper signal compete for attention, handle Mak1 first; log paper afterwards.
Each scan, check these too. When one triggers, log a paper trade in the journal's "Paper trades" table using real
option quotes: entry = ask, exit = bid, same stop/target rules as live. A strategy goes live only after ≥ 10 paper trades
with positive total P&L and win rate ≥ 50%, and only with the user's OK.

| ID | Strategy | Trigger | Vehicle | Exit |
|---|---|---|---|---|
| B | **Gap fade** | Gap ≥ 0.7% vs prior close; after 9:45 price fails at the OR high (gap up) / OR low (gap down) and loses VWAP | 0DTE put/call, delta ~0.30 | Target: 50% gap fill or prior close; stop: back above OR high/low |
| C | **Midday VWAP bounce** | 11:00–13:30, trend day: first pullback that touches VWAP and holds 2 bars, all 3 indexes | 0DTE, delta 0.35–0.45 | +30–40%; stop: 5-min close beyond VWAP |
| D | **1DTE afternoon** | Same setups as A but after 13:30, using the next-day expiry (less theta) | 1DTE, delta ~0.40 | +25–35% same day; stop -25%; never hold overnight unless user approves |
| E | **Single-stock catalyst** | Day after earnings in a liquid name (e.g., CSCO 11/13); opening-range break with spread ≤ 5% of mid | Weekly call/put, delta ~0.40 | +30–50%; stop: back inside OR |

## Paper bankroll (user 11/11): **$100** shared by B, C, D, E, A2 — virtual money only, never touches the live account
- Per paper trade: premium ≤ $50, max loss ≤ $10 (stop set so qty × (entry − stop) ≤ $10), qty from the sizing formula below.
- Paper daily stop: -$20 across all experiments. At most 2 paper positions open at once.
- If no contract fits these limits, log the signal as "too expensive" (still useful data).
- Paper bankroll compounds: running balance = $100 + all paper P&L. Track per strategy in the scoreboard.

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

## Scoreboard (paper) — paper bankroll: **$100.00**
| ID | Trades | Wins | Paper P&L | Status |
|---|---|---|---|---|
| B | 0 | 0 | $0 | → LIVE as Mak3 (11/13) |
| C | 0 | 0 | $0 | paper |
| D | 0 | 0 | $0 | paper |
| E | 0 | 0 | $0 | paper |
| A2 | 0 | 0 | $0 | paper |

Notes from past days (hindsight, not counted): 11/10 the 9:57 gap-fill call was effectively strategy B's mirror (fill up) and won;
11/11 had no clean midday VWAP touch (C would have had no trade).
11/12: no paper trades logged (process miss). Hindsight: B (gap ≥0.7% down, held VWAP after 9:45) would likely have hit the prior-close target by 10:58; C no trigger (SPY/QQQ never touched VWAP 11:00–13:30).
