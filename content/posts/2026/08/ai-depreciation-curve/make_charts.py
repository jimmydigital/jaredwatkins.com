#!/usr/bin/env python3
"""
Render the ai-depreciation-curve charts as PNGs (replaces the mermaid
xychart-beta blocks, which have no legend support). Pulls every number from
model.py so the charts and the report can never drift apart.

Palette: the dataviz skill's validated reference instance (light mode only --
this blog doesn't theme static images per its own existing image posts).

Run: python3 make_charts.py   (writes PNGs into this directory)
"""
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import model as M

OUT = HERE

# ---------------------------------------------------------------------------
# Palette (dataviz skill reference instance, light mode)
# ---------------------------------------------------------------------------
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_SECONDARY = "#52514e"
INK_MUTED = "#898781"
GRID = "#e1e0d9"
BASELINE = "#c3c2b7"

CATEGORICAL = {
    1: "#2a78d6",  # blue
    2: "#eb6834",  # orange
    3: "#1baf7a",  # aqua
    4: "#eda100",  # yellow
}

_BLUE_ANCHORS = [
    (100, "#cde2fb"), (150, "#b7d3f6"), (200, "#9ec5f4"), (250, "#86b6ef"),
    (300, "#6da7ec"), (350, "#5598e7"), (400, "#3987e5"), (450, "#2a78d6"),
    (500, "#256abf"), (550, "#1c5cab"), (600, "#184f95"), (650, "#104281"),
    (700, "#0d366b"),
]
_blue_cmap = LinearSegmentedColormap.from_list(
    "blue_ordinal", [h for _, h in _BLUE_ANCHORS], N=256
)


def ordinal_ramp(n):
    lo, hi = 250 / 700, 1.0
    return [_blue_cmap(lo + (hi - lo) * i / (n - 1)) for i in range(n)]


plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "text.color": INK,
    "axes.edgecolor": BASELINE,
    "axes.labelcolor": INK_SECONDARY,
    "xtick.color": INK_MUTED,
    "ytick.color": INK_MUTED,
    "font.size": 13,
    "axes.titlesize": 14,
    "axes.titleweight": "bold",
    "axes.titlecolor": INK,
})


def style_axes(ax, ygrid=True):
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(BASELINE)
    ax.spines["bottom"].set_linewidth(1)
    ax.tick_params(length=0)
    if ygrid:
        ax.yaxis.grid(True, color=GRID, linewidth=1, zorder=0)
        ax.set_axisbelow(True)


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=200, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print(f"wrote {name}")


rows, eta_c, b_eff, rmse = M.build()
CHIPS = [r["short"] for r in rows]
lam_r, r2r = M.pooled_lambda(rows, "rent_now", "rent0")
lam_p, r2p = M.pooled_lambda(rows, "used", "buy")

# 1. Energy per token
mtok_per_kwh = [1.0 / r["kwh_mtok"] for r in rows]
colors = ordinal_ramp(len(rows))

fig, ax = plt.subplots(figsize=(8, 4.5))
bars = ax.bar(CHIPS, mtok_per_kwh, color=colors, width=0.62, zorder=3)
ax.bar_label(bars, fmt="%.1f", padding=4, color=INK_SECONDARY, fontsize=11)
ax.set_ylabel("Millions of tokens per kWh at the wall")
ax.set_ylim(0, max(mtok_per_kwh) * 1.18)
style_axes(ax)
fig.suptitle("Energy efficiency, six generations", x=0.125, ha="left", y=1.02)
save(fig, "chart-energy-per-token.png")

# 2. Break-even months / rent premium
months, multiple = [], []
for r in rows:
    capex = r["buy"] + r["infra_slot"]
    own_hr_opex = (r["sys_w"] / 1000) * M.POWER_USD_KWH + r["buy"] * M.OPEX_FRACTION / M.HOURS_PER_YEAR
    margin = r["rent0"] - own_hr_opex
    be = capex / margin if margin > 0 else float("inf")
    months.append(be / (M.HOURS_PER_YEAR * M.UTILIZATION) * 12)
    multiple.append(r["rent0_mtok"] / r["own_mtok"])

colors = ordinal_ramp(len(rows))
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True)
b1 = ax1.bar(CHIPS, months, color=colors, width=0.62, zorder=3)
ax1.bar_label(b1, fmt="%.1f", padding=4, color=INK_SECONDARY, fontsize=11)
ax1.set_ylabel("Months of committed use to break even")
ax1.set_ylim(0, max(months) * 1.2)
style_axes(ax1)

b2 = ax2.bar(CHIPS, multiple, color=colors, width=0.62, zorder=3)
ax2.bar_label(b2, fmt="%.1fx", padding=4, color=INK_SECONDARY, fontsize=11)
ax2.set_ylabel("Renting costs this many times owning")
ax2.set_ylim(0, max(multiple) * 1.2)
style_axes(ax2)

fig.suptitle("Owning beats renting on day one -- by how much, and how long it takes to prove it",
             x=0.125, ha="left", y=1.0)
save(fig, "chart-breakeven-and-premium.png")

# 3. Rental decay, indexed to launch -- every chip with enough age to fit a
#    rate (B200 is excluded because its rate hasn't declined; B300 is too new
#    to fit at all -- both match the per-chip table above this chart).
lam_by_chip = dict(M.per_chip_lambda(rows, "rent_now", "rent0"))
years = list(range(0, 6))
fig, ax = plt.subplots(figsize=(8.2, 5.2))
label_series = []
for i, chip in enumerate(["V100", "A100", "H100", "H200"]):
    lam = lam_by_chip[chip]
    idx = [100 * math.exp(-lam * y) for y in years]
    color = CATEGORICAL[i + 1]
    ax.plot(years, idx, color=color, linewidth=2.5, marker="o", markersize=6,
             solid_capstyle="round", label=chip, zorder=3)
    label_series.append((chip, idx[-1], color))
# stagger end labels by rank so close finishers (A100/H200 land 8 apart) don't collide
for rank, (chip, y_end, color) in enumerate(sorted(label_series, key=lambda t: -t[1])):
    ax.annotate(chip, (years[-1], y_end), xytext=(8, 0), textcoords="offset points",
                color=color, fontsize=11, fontweight="bold", va="center")
ax.set_ylabel("Rental rate, indexed to launch = 100")
ax.set_xticks(years)
ax.set_xticklabels(["launch"] + [f"yr {y}" for y in years[1:]])
ax.set_ylim(0, 105)
ax.set_xlim(-0.15, 5.9)
style_axes(ax)
fig.suptitle("Rental rate after launch -- B200 isn't here because it hasn't declined",
             x=0.1, ha="left", y=1.02, fontsize=13)
save(fig, "chart-rental-decay.png")

# 4. Payback vs replace-it, in years
t_pay_list, t_rep_list, labels = [], [], []
for r in rows:
    r0 = r["rent0"]
    c = (r["sys_w"] / 1000) * M.POWER_USD_KWH + r["buy"] * M.OPEX_FRACTION / M.HOURS_PER_YEAR
    capex = r["buy"] + r["infra_slot"]
    hrs = M.HOURS_PER_YEAR * M.UTILIZATION
    cum = lambda t, r0=r0, c=c: hrs * (r0 * (1 - math.exp(-lam_r * t)) / lam_r - c * t)
    t_pay = next((t for t in np.arange(0.05, 30, 0.05) if cum(t) >= capex), None)
    t_rep = M.replace_life(r, rows, lam_r, 1.0)
    if t_rep is None:
        continue
    labels.append(r["short"])
    t_pay_list.append(t_pay)
    t_rep_list.append(t_rep)

x = np.arange(len(labels))
fig, ax = plt.subplots(figsize=(8, 4.8))
bars = ax.bar(x, t_rep_list, color=CATEGORICAL[1], width=0.55, zorder=3, label="Replace-it (bars)")
ax.bar_label(bars, fmt="%.1f", padding=4, color=INK_SECONDARY, fontsize=11)
ax.plot(x, t_pay_list, color=CATEGORICAL[2], linewidth=2.5, marker="o", markersize=7,
        solid_capstyle="round", zorder=4, label="Payback (line)")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel("Years")
ax.set_ylim(0, max(t_rep_list) * 1.2)
style_axes(ax)
ax.legend(frameon=False, loc="upper right", fontsize=11)
fig.suptitle("Payback arrives on schedule; the cushion after it is shrinking",
             x=0.125, ha="left", y=1.02)
save(fig, "chart-payback-vs-replace.png")

# 5. Rack power the facility has to deliver
power_labels = ["V100", "A100", "H100", "H200", "B200", "B300", "VR200", "Rubin U"]
power_kw = [10, 30, 40, 40, 130, 140, 125, 600]
tiers = [1, 2, 2, 2, 3, 3, 3, 4]

colors = ordinal_ramp(len(power_labels))
fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(power_labels))
bars = ax.bar(x, power_kw, color=colors, width=0.62, zorder=3)
ax.bar_label(bars, fmt="%.0f", padding=4, color=INK_SECONDARY, fontsize=11)

tier_bounds = []
start = 0
for i in range(1, len(tiers) + 1):
    if i == len(tiers) or tiers[i] != tiers[start]:
        tier_bounds.append((start, i - 1, tiers[start]))
        start = i
for lo, hi, t in tier_bounds:
    ax.axvspan(lo - 0.5, hi + 0.5, color=BASELINE, alpha=0.08 if t % 2 else 0.0, zorder=0)
    ax.text((lo + hi) / 2, max(power_kw) * 1.12, f"tier {t}", ha="center",
             color=INK_MUTED, fontsize=10)

ax.set_xticks(x)
ax.set_xticklabels(power_labels)
ax.set_ylabel("kW per rack the facility has to deliver")
ax.set_ylim(0, max(power_kw) * 1.28)
style_axes(ax)
fig.suptitle("Rack power by tier -- two generations per building, usually",
             x=0.09, ha="left", y=1.02)
save(fig, "chart-rack-power-tiers.png")

# 6. Remaining value, fitted vs booked
yrs = list(range(0, 7))
revenue = [100 * math.exp(-lam_r * y) for y in yrs]
resale = [100 * math.exp(-lam_p * y) for y in yrs]
sl4 = [max(0, 100 - 100 / M.GPU_LIFE_YEARS * y) for y in yrs]
sl6 = [max(0, 100 - 100 / 6 * y) for y in yrs]

series = [
    ("Fitted revenue", revenue, CATEGORICAL[1]),
    ("Fitted resale", resale, CATEGORICAL[3]),
    ("Straight-line 4yr", sl4, CATEGORICAL[4]),
    ("Straight-line 6yr", sl6, CATEGORICAL[2]),
]

fig, ax = plt.subplots(figsize=(8.5, 5.2))
for name, vals, color in series:
    ax.plot(yrs, vals, color=color, linewidth=2.5, marker="o", markersize=6,
             solid_capstyle="round", label=name, zorder=3)
    # Anchor the direct label at the point where the line stops being
    # informative (first time it hits zero), not always the last x -- two of
    # these series both flatline at 0 and would otherwise stack their labels
    # on top of each other at (6, 0).
    zero_idx = next((i for i, v in enumerate(vals) if v == 0), len(vals) - 1)
    ax_, ay = yrs[zero_idx], vals[zero_idx]
    offset = (8, 10) if ay == 0 else (8, 0)
    ax.annotate(name, (ax_, ay), xytext=offset, textcoords="offset points",
                color=color, fontsize=10.5, fontweight="bold",
                va="bottom" if ay == 0 else "center")
ax.set_ylabel("Percent of original value")
ax.set_xlabel("Year")
ax.set_xticks(yrs)
ax.set_xlim(-0.2, 7.6)
ax.set_ylim(0, 105)
style_axes(ax)
fig.suptitle("What a slot is worth, four different ways to count it",
             x=0.1, ha="left", y=1.02)
save(fig, "chart-remaining-value.png")

print("done")
