#!/usr/bin/env python3
"""
AI depreciation, from first principles.

Six generations of NVIDIA datacenter GPU (V100 -> B300) normalized to one unit:
dollars per 1M tokens on a fixed workload (Llama-2-70B, dense, offline serving).
From there: buy-vs-rent at each chip's launch, the observed decay of rental and
resale, and a depreciation function that falls out of the numbers instead of an
accounting policy.

Run:  python3 model.py
Deps: numpy (scipy optional, improves the fit polish)
"""

import csv
import math
import os

import numpy as np

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
HOURS_PER_YEAR = 8760

# ---------------------------------------------------------------------------
# The workload. Constant across every generation - that is the whole point.
# Llama-2-70B: 80 layers, 64 query heads, 8 KV heads (GQA), head_dim 128.
# ---------------------------------------------------------------------------
N_PARAMS = 70e9
FLOP_PER_TOKEN = 2 * N_PARAMS
KV_ELEMS_PER_TOKEN = 2 * 80 * 8 * 128      # K and V, all layers = 163,840
SEQ_LEN = 1100                              # MLPerf OpenOrca ~1024 in + 128 out
BYTES_PER_PARAM = {"FP16": 2.0, "INT8": 1.0, "FP8": 1.0, "FP4": 0.5}
KV_BYTES = {"FP16": 2.0, "INT8": 1.0, "FP8": 1.0, "FP4": 1.0}  # KV rarely below 8-bit

# ---------------------------------------------------------------------------
# Cost assumptions. Every one is a knob. The shape of the answer barely moves.
# ---------------------------------------------------------------------------
SYS_OVERHEAD = 1.35      # CPU, DRAM, NIC, fans, PSU loss, per GPU slot
PUE = 1.25               # facility overhead
POWER_USD_KWH = 0.08     # blended industrial rate
UTILIZATION = 0.85       # fraction of wall clock a slot is actually billing
GPU_LIFE_YEARS = 4       # accounting life for the "own" case
INFRA_LIFE_YEARS = 15    # the building outlives several chips
OPEX_FRACTION = 0.08     # staff, network, spares, insurance, per year, as frac of gpu capex
TP_PENALTY = 0.055       # throughput lost per extra GPU in the tensor-parallel group
SERVING_DERATE = 0.35    # MLPerf offline -> production serving under a latency SLO
TODAY = 2026.64          # August 2026 as a decimal year


def load_csv(name):
    with open(os.path.join(DATA, name)) as fh:
        return list(csv.DictReader(fh))


def to_year(s):
    y, m = s.split("-")
    return int(y) + (int(m) - 1) / 12.0


def num(x):
    return float(x) if x not in ("", None) else None


def tp_group(mem_gb, bytes_per_param):
    """Smallest power-of-2 GPU count that holds weights + a working KV cache."""
    need = (N_PARAMS * bytes_per_param) / 1e9 * 1.25   # 25% headroom for KV + activations
    n = 1
    while n * mem_gb < need and n < 16:
        n *= 2
    return n


# ---------------------------------------------------------------------------
# 1. Roofline. Three structural terms, two free parameters, fit to four
#    measured MLPerf points.
#
#    t_token = 2N/(F*eta)           compute
#            + N*b/(BW*B)           weight streaming, amortized over the batch
#            + S*kv/BW              KV cache re-read, NOT amortized over batch
#
#    then scaled by the tensor-parallel penalty.
# ---------------------------------------------------------------------------
def roofline(F_tflops, bw_gbs, prec, mem_gb, eta_c, b_eff):
    b = BYTES_PER_PARAM[prec]
    kv = KV_BYTES[prec]
    bw = bw_gbs * 1e9
    tp = tp_group(mem_gb, b)

    t_compute = FLOP_PER_TOKEN / (F_tflops * 1e12 * eta_c)
    # weights are read once per batch step and amortize over B_eff tokens
    t_weights = (N_PARAMS * b) / (bw * b_eff)
    # KV cache does NOT amortize: every sequence in the batch re-reads its own
    t_kv = (SEQ_LEN * KV_ELEMS_PER_TOKEN * kv) / bw

    raw = 1.0 / (t_compute + t_weights + t_kv)
    return raw / (1.0 + TP_PENALTY * (tp - 1)), tp


ETA_C = 1.0   # no fudge factor: use the chip's published dense peak as the roof.
              # At MLPerf offline batch sizes decode is bandwidth-bound anyway,
              # so the compute term barely moves the answer. Leaving eta at 1.0
              # keeps the model down to a SINGLE fitted parameter.


def fit_roofline(rows):
    """One free parameter (B_eff) fit against every measured MLPerf point."""
    measured = [r for r in rows if r["mlperf_llama70b_tok_s_gpu"]]

    def loss(b_eff):
        if b_eff <= 1:
            return 1e9
        e = 0.0
        for r in measured:
            pred, _ = roofline(num(r["dense_tflops"]), num(r["mem_bw_gbs"]),
                               r["infer_precision"], num(r["mem_gb"]), ETA_C, b_eff)
            e += (math.log(pred) - math.log(num(r["mlperf_llama70b_tok_s_gpu"]))) ** 2
        return e

    best, best_l = None, 1e18
    for b_eff in np.linspace(2, 4000, 8000):
        l = loss(b_eff)
        if l < best_l:
            best_l, best = l, b_eff
    return ETA_C, best, math.sqrt(best_l / len(measured)), measured


# ---------------------------------------------------------------------------
# 2. Per-chip economics, normalized to $/1M tokens.
# ---------------------------------------------------------------------------
INFRA_USD_PER_MW = {          # the facility tier each chip actually lands in
    "V100": 6e6,              # tier 1: air + containment
    "A100": 10e6,             # tier 2: dense air / rear-door HX
    "H100": 10e6,             # tier 2: still fits the 40kW air wall
    "H200": 10e6,             # tier 2
    "B200": 20e6,             # tier 3: direct-to-chip liquid, mandatory
    "B300": 20e6,             # tier 3
}


def build():
    gens = load_csv("gpu_generations.csv")
    prices = {r["chip"]: r for r in load_csv("prices_rent_vs_buy.csv")}
    eta_c, b_eff, rmse, measured = fit_roofline(gens)

    out = []
    for r in gens:
        pred, tp = roofline(num(r["dense_tflops"]), num(r["mem_bw_gbs"]),
                            r["infer_precision"], num(r["mem_gb"]), eta_c, b_eff)
        meas = num(r["mlperf_llama70b_tok_s_gpu"])
        tok_s = meas if meas else pred

        tdp = num(r["tdp_w"])
        sys_w = tdp * SYS_OVERHEAD * PUE
        kwh_per_mtok = (sys_w / tok_s) * 1e6 / 3600.0 / 1000.0

        p = prices[r["chip"]]
        key = r["chip"].split()[0]
        mtok_hr = tok_s * 3600.0 / 1e6

        infra_slot = INFRA_USD_PER_MW[key] * (sys_w / 1e6)
        gpu_capex = num(p["launch_buy_usd"])

        annual = (gpu_capex / GPU_LIFE_YEARS
                  + infra_slot / INFRA_LIFE_YEARS
                  + gpu_capex * OPEX_FRACTION
                  + (sys_w / 1000.0) * HOURS_PER_YEAR * POWER_USD_KWH)
        mtok_year = mtok_hr * HOURS_PER_YEAR * UTILIZATION

        out.append(dict(
            chip=r["chip"], short=key, launch=r["launch"], t0=to_year(r["launch"]),
            prec=r["infer_precision"], tp=tp,
            tok_s=tok_s, measured=bool(meas), pred=pred,
            tdp=tdp, sys_w=sys_w, kwh_mtok=kwh_per_mtok,
            buy=gpu_capex, used=num(p["used_2026_08_usd"]),
            rent0=num(p["launch_rent_usd_hr"]),
            rent_now=num(p["rent_2026_08_usd_hr"]),
            rent_floor=num(p["rent_floor_2026_08_usd_hr"]),
            rent0_list=num(p["launch_rent_list_usd_hr"]),
            rent_now_list=num(p["rent_list_2026_08"]),
            rent0_mtok=num(p["launch_rent_usd_hr"]) / mtok_hr,
            rent_now_mtok=num(p["rent_2026_08_usd_hr"]) / mtok_hr,
            own_mtok=annual / mtok_year,
            power_floor_mtok=kwh_per_mtok * POWER_USD_KWH,
            infra_slot=infra_slot,
            age=TODAY - to_year(r["launch"]),
        ))
    return out, eta_c, b_eff, rmse


MIN_AGE_FOR_FIT = 1.3   # need a real history before a decay rate means anything


def per_chip_lambda(rows, now, launch, min_age=MIN_AGE_FOR_FIT):
    """Exponential decay rate implied by each chip individually."""
    res = []
    for r in rows:
        if r["age"] < min_age or not r[now] or not r[launch]:
            continue
        res.append((r["short"], math.log(r[launch] / r[now]) / r["age"]))
    return res


def pooled_lambda(rows, now, launch, min_age=MIN_AGE_FOR_FIT):
    """Regression forced through the origin: at t=0 the ratio must be 1."""
    xs, ys = [], []
    for r in rows:
        if r["age"] < min_age or not r[now] or not r[launch]:
            continue
        xs.append(r["age"])
        ys.append(math.log(r[now] / r[launch]))
    xs, ys = np.array(xs), np.array(ys)
    slope = (xs @ ys) / (xs @ xs)
    ss_res = float(((ys - slope * xs) ** 2).sum())
    ss_tot = float((ys ** 2).sum())
    return -slope, 1 - ss_res / ss_tot


def marketplace_derate():
    """Competitive clearing rate as a fraction of hyperscaler list.

    Measured, not assumed: the H100 series is the only window where both
    markets are quoted at the same time.
    """
    ratios = []
    for r in load_csv("h100_rent_timeseries.csv"):
        if r["marketplace_usd_hr"] and r["hyperscaler_usd_hr"]:
            ratios.append(float(r["marketplace_usd_hr"]) / float(r["hyperscaler_usd_hr"]))
    return sum(ratios) / len(ratios)


def h100_series_lambda():
    """Decay of the H100 measured INSIDE each basis, not across two of them.

    This is the only chip with a real price history. Splicing a 2023
    hyperscaler quote onto a 2026 marketplace clear is a basis change, and it
    shows up as decay that never happened in either market.
    """
    ts = load_csv("h100_rent_timeseries.csv")
    out = {}
    for col in ("hyperscaler_usd_hr", "marketplace_usd_hr", "neocloud_usd_hr"):
        pts = [(to_year(r["period_mid"]), float(r[col])) for r in ts if r[col]]
        if len(pts) < 2:
            continue
        xs = np.array([t for t, _ in pts]); ys = np.array([math.log(v) for _, v in pts])
        slope, _ = np.polyfit(xs, ys, 1)
        out[col.split("_")[0]] = (-slope, len(pts))
    return out


def replace_life(old, rows, lam_r, mult):
    """Incumbent age at which the best available challenger wins the slot."""
    i = rows.index(old)
    c_old = ((old["sys_w"] / 1000) * POWER_USD_KWH
             + old["buy"] * OPEX_FRACTION / HOURS_PER_YEAR)
    best = None
    for new in rows[i + 1:]:
        jump = INFRA_USD_PER_MW[old["short"]] != INFRA_USD_PER_MW[new["short"]]
        c_new = ((new["sys_w"] / 1000) * POWER_USD_KWH
                 + new["buy"] * OPEX_FRACTION / HOURS_PER_YEAR)
        k_new = new["buy"] / (GPU_LIFE_YEARS * HOURS_PER_YEAR * UTILIZATION)
        if jump:
            k_new += ((new["infra_slot"] - old["infra_slot"])
                      / (INFRA_LIFE_YEARS * HOURS_PER_YEAR))
        gap = new["t0"] - old["t0"]
        denom = old["rent0"] * mult - new["rent0"] * mult * math.exp(lam_r * gap)
        numer = c_old - c_new - k_new
        if denom == 0:
            continue
        u = numer / denom
        if not (0 < u <= 1):
            continue
        age = max(-math.log(u) / lam_r, gap)
        if best is None or age < best:
            best = age
    return best


def trend(rows, fn):
    xs = np.array([r["t0"] for r in rows])
    ys = np.array([math.log(fn(r)) for r in rows])
    slope, _ = np.polyfit(xs, ys, 1)
    return math.exp(slope)


def rule(t):
    print("=" * 78)
    print(t)
    print("=" * 78)


def main():
    rows, eta_c, b_eff, rmse = build()

    rule("STEP 1  Roofline fit (Llama-2-70B, dense, offline)")
    print(f"  fixed:   compute roof at published dense peak (eta = {eta_c:.2f})")
    print(f"           KV re-read at S={SEQ_LEN} tokens, "
          f"TP penalty {TP_PENALTY*100:.1f}% per extra GPU in the group")
    print(f"  FITTED:  effective batch B_eff = {b_eff:.0f}   <- one free parameter, "
          f"{sum(r['measured'] for r in rows)} data points")
    print(f"  log-RMSE = {rmse:.3f}  ({(math.exp(rmse)-1)*100:.1f}% typical error)\n")
    print(f"  {'chip':<22}{'prec':>6}{'TP':>4}{'measured':>10}{'roofline':>10}{'err':>9}")
    for r in rows:
        m = f"{r['tok_s']:.0f}" if r["measured"] else "--"
        e = (f"{(r['pred']/r['tok_s']-1)*100:+.1f}%" if r["measured"] else "(used)")
        print(f"  {r['chip']:<22}{r['prec']:>6}{r['tp']:>4}{m:>10}{r['pred']:>10.0f}{e:>9}")

    print()
    rule("STEP 2  One unit: dollars and joules per 1M tokens")
    print(f"  {'chip':<22}{'tok/s':>8}{'W/slot':>8}{'kWh/Mtok':>10}"
          f"{'own $':>9}{'rent $':>9}{'power $':>10}")
    for r in rows:
        print(f"  {r['chip']:<22}{r['tok_s']:>8.0f}{r['sys_w']:>8.0f}"
              f"{r['kwh_mtok']:>10.3f}{r['own_mtok']:>9.3f}"
              f"{r['rent0_mtok']:>9.3f}{r['power_floor_mtok']:>10.4f}")
    print(f"\n  (MLPerf offline units. Production serving under a latency SLO runs")
    print(f"   about {SERVING_DERATE:.0%} of this, so multiply the dollar columns by")
    print(f"   {1/SERVING_DERATE:.1f}x for a real API cost. It cancels in every ratio below.)")
    print(f"\n  H100 in production terms: ${rows[2]['own_mtok']/SERVING_DERATE:.2f}/Mtok owned, "
          f"${rows[2]['rent0_mtok']/SERVING_DERATE:.2f}/Mtok rented at launch.")

    print()
    rule("STEP 3  Buy vs rent, on the day each chip shipped")
    print(f"  {'chip':<22}{'own $/Mtok':>12}{'rent $/Mtok':>13}{'rent/own':>10}"
          f"{'breakeven hr':>14}{'months':>9}")
    for r in rows:
        capex = r["buy"] + r["infra_slot"]
        own_hr_opex = ((r["sys_w"] / 1000) * POWER_USD_KWH
                       + r["buy"] * OPEX_FRACTION / HOURS_PER_YEAR)
        margin = r["rent0"] - own_hr_opex
        be = capex / margin if margin > 0 else float("inf")
        print(f"  {r['chip']:<22}{r['own_mtok']:>12.3f}{r['rent0_mtok']:>13.3f}"
              f"{r['rent0_mtok']/r['own_mtok']:>10.2f}{be:>14,.0f}"
              f"{be/(HOURS_PER_YEAR*UTILIZATION)*12:>9.1f}")

    print()
    rule("STEP 4  What actually decayed, and how fast")
    print("  Rental rate, per chip:")
    for name, lam in per_chip_lambda(rows, "rent_now", "rent0"):
        hl = f"{math.log(2)/lam:4.1f}yr" if lam > 0 else "  never"
        print(f"    {name:<8} lambda={lam:6.3f}/yr   {math.exp(-lam)*100:5.1f}% retained/yr"
              f"   half-life {hl}")
    lam_r, r2r = pooled_lambda(rows, "rent_now", "rent0")
    print(f"    {'POOLED':<8} lambda={lam_r:6.3f}/yr   {math.exp(-lam_r)*100:5.1f}% retained/yr"
          f"   half-life {math.log(2)/lam_r:4.1f}yr   R2={r2r:.3f}")
    print("\n    (R2 is a 6-chip cross-section regressed through the origin, one")
    print("     launch/today ratio per chip. It says those six ratios line up in")
    print("     age. It is NOT evidence that any chip decays exponentially.)")

    lam_list, _ = pooled_lambda(rows, "rent_now_list", "rent0_list")
    lam_floor, _ = pooled_lambda(rows, "rent_floor", "rent0")
    print("\n  The answer depends entirely on which market you measure:")
    print(f"    hyperscaler list -> hyperscaler list      lambda={lam_list:6.3f}/yr")
    print(f"    launch rate -> market median (used here)  lambda={lam_r:6.3f}/yr")
    print(f"    launch rate -> marketplace floor          lambda={lam_floor:6.3f}/yr")
    print("    Same chips, same dates. The spread is the basis, not the silicon.")

    print("\n  H100 measured inside a single basis (the only real time series):")
    for basis, (lam, n) in h100_series_lambda().items():
        print(f"    {basis:<14} lambda={lam:6.3f}/yr   ({n} points)")

    print("\n  Caveat the fit cannot see: rentals stopped falling. GetDeploying's")
    print("  index is up 4.3% over the last 12 months, Silicon Data has the H200")
    print("  neocloud index up 14.4% over 12 weeks. Every lambda here is an")
    print("  average over a window whose last year runs the other way.")

    print("\n  Resale price, per chip:")
    for name, lam in per_chip_lambda(rows, "used", "buy"):
        print(f"    {name:<8} lambda={lam:5.3f}/yr   {math.exp(-lam)*100:5.1f}% retained/yr"
              f"   half-life {math.log(2)/lam:4.1f}yr")
    lam_p, r2p = pooled_lambda(rows, "used", "buy")
    print(f"    {'POOLED':<8} lambda={lam_p:5.3f}/yr   {math.exp(-lam_p)*100:5.1f}% retained/yr"
          f"   half-life {math.log(2)/lam_p:4.1f}yr   R2={r2p:.3f}")

    print("\n  Frontier advance (the thing doing the killing):")
    print(f"    tokens/s per $ of silicon   {trend(rows, lambda r: r['tok_s']/r['buy']):.2f}x/yr")
    print(f"    tokens per kWh              {trend(rows, lambda r: 1/r['kwh_mtok']):.2f}x/yr")
    print(f"    tokens/s per GPU            {trend(rows, lambda r: r['tok_s']):.2f}x/yr")
    print(f"    $/Mtok owned                {trend(rows, lambda r: 1/r['own_mtok']):.2f}x/yr cheaper")

    print()
    rule("STEP 5  Three different 'useful lives', and why people argue")
    print("""
  'Useful life' is three questions wearing one coat. Same chip, same decay
  curve, three answers - which is how Burry and Meta both get to be right.

    T_cash     revenue falls below cash opex        -> turn it off
    T_payback  cumulative margin repays capex       -> was it a good buy
    T_replace  a new chip in the SAME slot wins     -> swap it out
""")
    print(f"  {'chip':<10}{'R0 $/hr':>9}{'capex $':>10}{'T_cash':>9}"
          f"{'T_payback':>11}{'T_replace':>11}{'peak margin':>13}")
    for r in rows:
        r0 = r["rent0"]
        c = ((r["sys_w"] / 1000) * POWER_USD_KWH
             + r["buy"] * OPEX_FRACTION / HOURS_PER_YEAR)
        t_cash = math.log(r0 / c) / lam_r if r0 > c else 0.0
        capex = r["buy"] + r["infra_slot"]
        hrs = HOURS_PER_YEAR * UTILIZATION
        cum = lambda t: hrs * (r0 * (1 - math.exp(-lam_r * t)) / lam_r - c * t)
        t_pay = next((t for t in np.arange(0.05, 30, 0.05) if cum(t) >= capex), None)
        peak = cum(t_cash)
        t_rep = replace_life(r, rows, lam_r, 1.0)
        print(f"  {r['short']:<10}{r0:>9.2f}{capex:>10,.0f}{t_cash:>9.1f}"
              f"{(f'{t_pay:.1f}' if t_pay else 'never'):>11}"
              f"{(f'{t_rep:.1f}' if t_rep else '--'):>11}{peak:>13,.0f}")
    print("\n  peak margin = most cash the slot can ever produce, capex excluded.")
    print("  Where that is below capex, the purchase never repays itself.")

    print()
    rule("STEP 5a  Sensitivity: does the answer survive the assumptions?")
    base = rows[2]      # H100, the chip with the most data behind it
    print(f"  H100 payback, base case = "
          f"{next((t for t in np.arange(0.05,30,0.05) if HOURS_PER_YEAR*UTILIZATION*(base['rent0']*(1-math.exp(-lam_r*t))/lam_r - ((base['sys_w']/1000)*POWER_USD_KWH + base['buy']*OPEX_FRACTION/HOURS_PER_YEAR)*t) >= base['buy']+base['infra_slot']), 0):.1f} yr\n")
    print(f"  {'knob':<26}{'low':>12}{'base':>12}{'high':>12}")
    for name, key, lo, hi in [
        ("rental decay lam_r", "lam", 0.06, 0.25),
        ("power $/kWh", "pwr", 0.05, 0.15),
        ("utilization", "util", 0.60, 0.95),
        ("launch rate $/hr", "r0", 4.00, 9.00),
    ]:
        outs = []
        for val in (lo, lam_r if key == "lam" else None, hi):
            if val is None:
                val = {"pwr": POWER_USD_KWH, "util": UTILIZATION,
                       "r0": base["rent0"], "lam": lam_r}[key]
            lam = val if key == "lam" else lam_r
            pw = val if key == "pwr" else POWER_USD_KWH
            ut = val if key == "util" else UTILIZATION
            r0 = val if key == "r0" else base["rent0"]
            c = (base["sys_w"] / 1000) * pw + base["buy"] * OPEX_FRACTION / HOURS_PER_YEAR
            hrs = HOURS_PER_YEAR * ut
            cap = base["buy"] + base["infra_slot"]
            t = next((t for t in np.arange(0.05, 30, 0.05)
                      if hrs * (r0 * (1 - math.exp(-lam * t)) / lam - c * t) >= cap), None)
            outs.append(f"{t:.1f}yr" if t else "never")
        print(f"  {name:<26}{outs[0]:>12}{outs[1]:>12}{outs[2]:>12}")
    print("\n  Only lam_r and the launch rate move the answer much. Power is noise")
    print("  at these margins - which is not the story the press release tells.")

    print()
    rule("STEP 5b  Which challenger does the killing")
    print(f"  {'incumbent':<10}{'challenger':<12}{'tier jump':>11}{'gap yr':>8}"
          f"{'evict at':>10}  note")
    lives = {}
    for i, old in enumerate(rows):
        c_old = ((old["sys_w"] / 1000) * POWER_USD_KWH
                 + old["buy"] * OPEX_FRACTION / HOURS_PER_YEAR)
        best_age, best_note, best_new = None, "", None
        for new in rows[i + 1:]:
            jump = INFRA_USD_PER_MW[old["short"]] != INFRA_USD_PER_MW[new["short"]]
            c_new = ((new["sys_w"] / 1000) * POWER_USD_KWH
                     + new["buy"] * OPEX_FRACTION / HOURS_PER_YEAR)
            k_new = new["buy"] / (GPU_LIFE_YEARS * HOURS_PER_YEAR * UTILIZATION)
            if jump:
                # a tier jump makes the challenger fund its own facility delta
                k_new += ((new["infra_slot"] - old["infra_slot"])
                          / (INFRA_LIFE_YEARS * HOURS_PER_YEAR))
            gap = new["t0"] - old["t0"]
            # Both chips' rates decay at lam_r from their OWN launch dates, so
            # at incumbent age t the challenger is (t - gap) years into its run.
            #   R_old0*u - c_old  =  R_new0*u*e^(lam*gap) - c_new - k_new
            #   u = (c_old - c_new - k_new) / (R_old0 - R_new0*e^(lam*gap))
            denom = old["rent0"] - new["rent0"] * math.exp(lam_r * gap)
            numer = c_old - c_new - k_new
            if denom == 0:
                continue
            u = numer / denom
            if not (0 < u <= 1):
                continue                       # never crosses, or crosses before launch
            t_star = -math.log(u) / lam_r
            age = max(t_star, gap)             # can't be evicted before it exists
            note = ("evicted on arrival" if t_star < gap else "outlives the launch")
            if jump:
                note += ", tier jump"
            if best_age is None or age < best_age:
                best_age, best_note, best_new = age, note, new
            print(f"  {old['short']:<10}{new['short']:<12}"
                  f"{('YES' if jump else 'no'):>11}{gap:>8.1f}{age:>10.1f}  {note}")
        if best_age is not None:
            lives[old["short"]] = (best_age, best_new["short"], best_note)
        print()
    print(f"  {'chip':<10}{'economic life':>15}{'killed by':>12}")
    for r in rows:
        if r["short"] in lives:
            a, k, _ = lives[r["short"]]
            print(f"  {r['short']:<10}{a:>15.1f}{k:>12}")
        else:
            print(f"  {r['short']:<10}{'(current frontier)':>15}{'--':>12}")

    print()
    rule("STEP 6  The infrastructure ceiling")
    tiers = load_csv("infra_tiers.csv")
    for t in tiers:
        print(f"  tier {t['tier']}  {t['years']:<11}{t['kw_per_rack']:>10} kW/rack"
              f"  ${float(t['capex_usd_per_mw'])/1e6:>5.1f}M/MW  {t['cooling']}")
        print(f"           hosts: {t['chips_hosted']}")
    print("""
  Two chip generations per tier, three at the outside. Inside a tier the next
  chip is a forklift swap and the old one gets evicted on chip economics alone.
  Across a tier boundary the incumbent gets a stay of execution, because the
  challenger has to fund a building before it can beat anything.

  Retrofit where the shell allows it: ~$2M/MW, versus $11M+/MW greenfield
  liquid-cooled. That gap is the entire reason tier 2 hardware kept earning
  through 2025 while tier 3 hardware was already shipping.
""")

    print()
    rule("STEP 7  The formula")
    print(f"""
  Put it together. Value of a deployed slot at age t:

      V(t) = INT[t..T*] ( R0*e^(-lam_r*s) - C_pwr - C_opex ) ds  +  P0*e^(-lam_p*T*)

      lam_r = {lam_r:.2f}/yr   rental revenue decay      (market-median basis;
                           0.06 to 0.25 depending on which market you measure)
      lam_p = {lam_p:.2f}/yr   resale value decay        (fit, R2={r2p:.2f})
      T*                   set by REPLACEMENT, not wear, and gated by the
                           infrastructure tier the slot belongs to

  Straight-line depreciation over L years implies a constant {100/GPU_LIFE_YEARS:.0f}%/yr
  writedown. The fitted revenue curve writes down {(1-math.exp(-lam_r))*100:.0f}% in year one and
  {(1-math.exp(-lam_r*2))*100:.0f}% by the end of year two. Book value and economic value diverge
  fastest in exactly the years an operator is most levered.
""")
    print(f"  {'chip':<10}{'yr1':>8}{'yr2':>8}{'yr3':>8}{'yr4':>8}{'yr5':>8}{'yr6':>8}   basis")
    for label, lam in [("revenue", lam_r), ("resale", lam_p)]:
        vals = "".join(f"{math.exp(-lam*y)*100:>8.0f}" for y in range(1, 7))
        print(f"  {label:<10}{vals}   fitted")
    sl = "".join(f"{max(0, 100-100/GPU_LIFE_YEARS*y):>8.0f}" for y in range(1, 7))
    print(f"  {'SL '+str(GPU_LIFE_YEARS)+'yr':<10}{sl}   accounting")
    sl6 = "".join(f"{max(0, 100-100/6*y):>8.0f}" for y in range(1, 7))
    print(f"  {'SL 6yr':<10}{sl6}   hyperscaler")


if __name__ == "__main__":
    main()
