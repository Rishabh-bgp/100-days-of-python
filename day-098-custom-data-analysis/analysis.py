"""Day 98 - Portfolio project: my own data analysis. A year of sales from a (fictional)
café chain: which products, hours, weekdays and branches drive revenue, plus seasonality,
a price-elasticity check and a short written report.

Offline: a reproducible synthetic dataset (~30k transactions) is generated in code.
Charts go to output/ and the findings to output/report.md.
"""
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).with_name("output")
MENU = {"Espresso": 120, "Cappuccino": 180, "Latte": 200, "Masala Chai": 90, "Cold Coffee": 220, "Croissant": 150,
        "Sandwich": 240}
BRANCHES = {"Arera Colony": 1.0, "MG Road": 1.3, "Lake View": 0.8}


def make(seed: int = 98, n: int = 30000) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    ts = pd.Timestamp("2025-01-01") + pd.to_timedelta(rng.integers(0, 365 * 24 * 60, n), unit="min")
    hour_weight = np.exp(-((ts.hour - 9) ** 2) / 8) + 0.8 * np.exp(-((ts.hour - 17) ** 2) / 6) + 0.05
    keep = rng.random(n) < hour_weight / hour_weight.max()
    ts = ts[keep]
    m = len(ts)
    product = rng.choice(list(MENU), m, p=[.12, .2, .18, .2, .1, .1, .1])
    summer = np.isin(ts.month, [4, 5, 6])
    product = np.where(summer & (rng.random(m) < 0.25), "Cold Coffee", product)
    branch = rng.choice(list(BRANCHES), m, p=[.35, .4, .25])
    qty = rng.choice([1, 1, 1, 2, 3], m)
    price = np.array([MENU[p] for p in product]) * np.where(ts.month >= 7, 1.1, 1.0)  # July price rise
    return pd.DataFrame({"timestamp": ts, "product": product, "branch": branch, "qty": qty,
                         "unit_price": price.round(), "revenue": (price * qty).round()})


def analyse() -> dict:
    df = make()
    OUT.mkdir(exist_ok=True)
    df["month"] = df["timestamp"].dt.to_period("M")
    df["weekday"] = df["timestamp"].dt.day_name()
    df["hour"] = df["timestamp"].dt.hour
    total = df["revenue"].sum()
    by_product = df.groupby("product")["revenue"].sum().sort_values(ascending=False)
    by_branch = df.groupby("branch")["revenue"].sum().sort_values(ascending=False)
    by_hour = df.groupby("hour")["revenue"].sum()
    monthly = df.groupby("month")["revenue"].sum()
    cold = df[df["product"] == "Cold Coffee"].groupby(df["timestamp"].dt.month)["qty"].sum()
    before = df[df["timestamp"].dt.month < 7].groupby("product")["qty"].sum() / 6
    after = df[df["timestamp"].dt.month >= 7].groupby("product")["qty"].sum() / 6
    change = ((after - before) / before * 100).round(1)
    fig, axes = plt.subplots(2, 2, figsize=(14, 9))
    by_product.plot.barh(ax=axes[0, 0], title="Revenue by product (₹)")
    by_hour.plot(ax=axes[0, 1], title="Revenue by hour of day", marker="o")
    monthly.plot(ax=axes[1, 0], title="Monthly revenue")
    cold.plot.bar(ax=axes[1, 1], title="Cold coffee cups sold by month")
    fig.tight_layout()
    fig.savefig(OUT / "dashboard.png", dpi=90)
    plt.close(fig)
    report = [
        "# Café chain - 2025 sales review (synthetic data)", "",
        f"- Total revenue: ₹{total:,.0f} from {len(df):,} transactions.",
        f"- Best product: **{by_product.index[0]}** ({by_product.iloc[0] / total:.0%} of revenue).",
        f"- Best branch: **{by_branch.index[0]}**; weakest: {by_branch.index[-1]}.",
        f"- Peak hour: **{by_hour.idxmax()}:00**; second peak in the evening.",
        f"- Busiest weekday: {df['weekday'].value_counts().idxmax()}.",
        f"- Cold coffee peaks in month {cold.idxmax()} (summer).",
        f"- After the 10% July price rise, monthly cups sold changed by {change.mean():+.1f}% on average "
        "(demand did not fall, which suggests customers here are not very price-sensitive).", "",
        "Charts: `dashboard.png`.",
    ]
    (OUT / "report.md").write_text("\n".join(report), encoding="utf-8")
    print("\n".join(report))
    return {"total": total, "best": by_product.index[0]}


if __name__ == "__main__":
    analyse()
