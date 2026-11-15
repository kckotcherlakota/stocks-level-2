#!/usr/bin/env python3
"""Fast pre-trade math for the 0DTE agent. Pure stdlib, no network.

Examples:
  python3 tools/trade_calc.py size --bid 0.46 --ask 0.47 --max-loss 9.16 --max-premium 46 --stop-pct 0.20
  python3 tools/trade_calc.py exit --bid 0.55
  python3 tools/trade_calc.py chop --closes 752.1,752.6,751.9 --vwap 752.3,752.3,752.3
  python3 tools/trade_calc.py daytype --adx 18.5 --adx-prev 19.2 --vwap-now 752.39 --vwap-30m 752.31
  python3 tools/trade_calc.py rr --entry 100.10 --stop 99.95 --target 100.50
"""
import argparse
import math
import sys


def r2(x):
    return round(x + 1e-9, 2)


def cmd_size(a):
    mid = (a.bid + a.ask) / 2
    spread = a.ask - a.bid
    spread_pct = spread / mid if mid > 0 else 1.0
    limit = r2(mid + 0.005)  # mid, rounded up a penny-half: fills fast without chasing
    stop = r2(limit * (1 - a.stop_pct))
    loss_per = (limit - stop) * 100 + a.slip * 100
    qty_risk = math.floor(a.max_loss / loss_per) if loss_per > 0 else 0
    qty_prem = math.floor(a.max_premium / (limit * 100)) if limit > 0 else 0
    qty = max(0, min(qty_risk, qty_prem, a.max_qty))
    spread_cost = spread / 2 * 100 * max(qty, 1)
    gate = []
    if a.bid <= 0:
        gate.append("ZERO_BID")
    if spread_pct > a.max_spread_pct:
        gate.append(f"SPREAD {spread_pct:.1%} > {a.max_spread_pct:.0%}")
    if spread > 0.15:
        gate.append(f"SPREAD ${spread:.2f} > $0.15")
    if qty == 0:
        fit = r2(limit - (a.max_loss / 100 - a.slip))
        if limit * 100 <= a.max_premium and fit > 0:
            print(f"1 contract fits only with stop >= {fit:.2f} ({(limit - fit) / limit:.0%} stop) - use it only if a chart level justifies it")
        gate.append("QTY_0 (1 contract exceeds max loss or premium) -> SKIP, don't pick a cheaper strike")
    print(f"mid {mid:.3f}  spread {spread:.2f} ({spread_pct:.1%})  spread cost ${spread_cost:.2f}")
    print(f"LIMIT BUY {limit:.2f}  x{qty}  premium ${limit*100*qty:.2f}")
    print(f"STOP_MARKET {stop:.2f}  -> loss/contract ${loss_per:.2f} (incl ${a.slip:.2f} slip)  total ${loss_per*qty:.2f}")
    print(f"targets: +30% {r2(limit*1.3):.2f}  +50% {r2(limit*1.5):.2f}  BE-stop at +20% ({r2(limit*1.2):.2f})")
    print("GATE: PASS" if not gate else "GATE: FAIL - " + "; ".join(gate))
    return 0 if not gate else 1


def cmd_exit(a):
    print(f"SELL LIMIT {r2(a.bid - 0.01):.2f}  (bid - 0.01). Cancel the stop first; if not filled in ~30 s, re-place the stop.")
    if a.trail_pct:
        print(f"trail stop {r2(a.bid * (1 - a.trail_pct)):.2f}  ({a.trail_pct:.0%} under bid)")
    return 0


def cmd_chop(a):
    closes = [float(x) for x in a.closes.split(",")]
    vw = [float(x) for x in a.vwap.split(",")]
    if len(vw) == 1:
        vw = vw * len(closes)
    sides = [1 if c > v else -1 for c, v in zip(closes, vw)][-12:]
    crosses = sum(1 for i in range(1, len(sides)) if sides[i] != sides[i - 1])
    verdict = "CHOP -> NO TRADE" if crosses > 2 else "OK"
    print(f"VWAP crosses in last {len(sides)} bars: {crosses}  -> {verdict}")
    return 0 if crosses <= 2 else 1


def cmd_daytype(a):
    slope = (a.vwap_now - a.vwap_30m) / a.vwap_now * 100 if a.vwap_now else 0.0
    rising = a.adx > a.adx_prev
    if a.adx >= 25 and rising and abs(slope) >= 0.05:
        t = "TREND -> Mak1 on, Mak4 off"
    elif a.adx < 20 and abs(slope) < 0.03:
        t = "RANGE -> Mak1 breakouts off, Mak4 on"
    else:
        t = "UNCERTAIN -> Mak1 A+ only, Mak4 off"
    print(f"ADX {a.adx:.1f} ({'rising' if rising else 'falling'})  VWAP slope 30m {slope:+.3f}%  => {t}")
    return 0


def cmd_rr(a):
    risk = abs(a.entry - a.stop)
    reward = abs(a.target - a.entry)
    rr = reward / risk if risk else 0
    print(f"risk {risk:.2f}  reward {reward:.2f}  R:R {rr:.2f}  -> {'OK (>=1.5)' if rr >= 1.5 else 'SKIP (<1.5)'}")
    print("note: share-level R:R; recheck with option prices (delta, spread, theta) before entry")
    return 0 if rr >= 1.5 else 1


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("size")
    s.add_argument("--bid", type=float, required=True)
    s.add_argument("--ask", type=float, required=True)
    s.add_argument("--max-loss", type=float, required=True)
    s.add_argument("--max-premium", type=float, required=True)
    s.add_argument("--stop-pct", type=float, default=0.20)
    s.add_argument("--slip", type=float, default=0.01, help="expected stop slippage per share")
    s.add_argument("--max-qty", type=int, default=2)
    s.add_argument("--max-spread-pct", type=float, default=0.10)
    e = sp.add_parser("exit")
    e.add_argument("--bid", type=float, required=True)
    e.add_argument("--trail-pct", type=float, default=0.15)
    c = sp.add_parser("chop")
    c.add_argument("--closes", required=True)
    c.add_argument("--vwap", required=True)
    d = sp.add_parser("daytype")
    d.add_argument("--adx", type=float, required=True)
    d.add_argument("--adx-prev", type=float, required=True)
    d.add_argument("--vwap-now", type=float, required=True)
    d.add_argument("--vwap-30m", type=float, required=True)
    r = sp.add_parser("rr")
    r.add_argument("--entry", type=float, required=True)
    r.add_argument("--stop", type=float, required=True)
    r.add_argument("--target", type=float, required=True)
    a = p.parse_args()
    return {"size": cmd_size, "exit": cmd_exit, "chop": cmd_chop, "daytype": cmd_daytype, "rr": cmd_rr}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
