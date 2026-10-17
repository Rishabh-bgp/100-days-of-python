"""Day 79 - The handwashing discovery: did a hygiene rule cut death rates in a maternity
clinic? Monthly rates, before/after comparison, histograms and KDE, and a t-test.

Offline and synthetic: the course uses historical records from Dr Ignaz Semmelweis's
Vienna clinic. Here monthly births/deaths are SIMULATED to tell the same kind of story
(mortality ~10% before a mid-1847 handwashing rule, ~2% after). The numbers are not the
historical ones; the point is the statistics workflow.
"""
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from scipy import stats  # noqa: E402

OUT = Path(__file__).with_name("output")
RULE_DATE = pd.Timestamp("1847-06-01")


def make(seed: int = 79) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    months = pd.date_range("1841-01-01", "1849-03-01", freq="MS")
    births = rng.integers(200, 330, len(months))
    rate = np.where(months < RULE_DATE, rng.normal(0.10, 0.04, len(months)), rng.normal(0.021, 0.012, len(months)))
    deaths = (births * np.clip(rate, 0.0, 0.3)).round().astype(int)
    return pd.DataFrame({"date": months, "births": births, "deaths": deaths})


def analyse() -> dict:
    df = make()
    OUT.mkdir(exist_ok=True)
    df["pct_deaths"] = df["deaths"] / df["births"]
    before, after = df[df["date"] < RULE_DATE], df[df["date"] >= RULE_DATE]
    b_rate = before["deaths"].sum() / before["births"].sum()
    a_rate = after["deaths"].sum() / after["births"].sum()
    print(f"average death rate before: {b_rate:.2%}, after: {a_rate:.2%}")
    print(f"improvement: {b_rate - a_rate:.2%} points, {b_rate / a_rate:.1f}x fewer deaths")
    t_stat, p_value = stats.ttest_ind(before["pct_deaths"], after["pct_deaths"])
    print(f"t-statistic {t_stat:.2f}, p-value {p_value:.2e} -> {'significant' if p_value < 0.01 else 'not significant'} at 1%")
    roll = df.set_index("date")["pct_deaths"].rolling(6).mean()
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(before["date"], before["pct_deaths"], color="black", linestyle="--", label="Before handwashing")
    ax.plot(after["date"], after["pct_deaths"], color="skyblue", marker="o", label="After handwashing")
    ax.plot(roll.index, roll.values, color="crimson", linewidth=3, label="6-month moving average")
    ax.axvline(RULE_DATE, color="grey")
    ax.set_ylabel("Monthly death rate")
    ax.legend()
    fig.savefig(OUT / "death_rate.png", dpi=100)
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(before["pct_deaths"], bins=20, alpha=0.6, density=True, label="before")
    ax.hist(after["pct_deaths"], bins=20, alpha=0.6, density=True, label="after")
    for data, colour in ((before["pct_deaths"], "C0"), (after["pct_deaths"], "C1")):
        xs = np.linspace(0, data.max() * 1.2, 200)
        ax.plot(xs, stats.gaussian_kde(data)(xs), color=colour)
    ax.legend()
    fig.savefig(OUT / "distributions.png", dpi=100)
    plt.close(fig)
    print("saved charts to output/")
    return {"before": b_rate, "after": a_rate, "p": p_value}


if __name__ == "__main__":
    analyse()
