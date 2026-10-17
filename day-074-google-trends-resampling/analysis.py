"""Day 74 - Google Trends and data resampling: compare search interest with prices and
unemployment. Date parsing, missing values, resample() from daily to monthly, rolling
means, and twin-axis line charts with date locators.

Offline: the course uses Google Trends exports and Yahoo prices; here synthetic monthly
search-interest series, a daily 'coin price' series and an unemployment series are
generated in code. Charts saved to output/.
"""
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).with_name("output")


def make(seed: int = 74):
    rng = np.random.default_rng(seed)
    days = pd.date_range("2014-09-17", "2025-12-31", freq="D")
    walk = np.exp(np.cumsum(rng.normal(0.0012, 0.035, len(days))))
    price = pd.DataFrame({"DATE": days, "CLOSE": 400 * walk, "VOLUME": rng.lognormal(20, 0.5, len(days))})
    price.loc[rng.choice(len(price), 5, replace=False), "CLOSE"] = np.nan  # a few gaps to clean
    months = pd.date_range("2014-09-01", "2025-12-01", freq="MS")
    monthly_price = price.set_index("DATE")["CLOSE"].resample("MS").mean().reindex(months).values
    search = np.clip(100 * monthly_price / np.nanmax(monthly_price) + rng.normal(0, 4, len(months)), 0, 100)
    trends = pd.DataFrame({"MONTH": months, "COIN_SEARCH": search.round()})
    unemp_months = pd.date_range("2004-01-01", "2025-12-01", freq="MS")
    base = 5 + 2 * np.sin(np.arange(len(unemp_months)) / 30) + rng.normal(0, 0.2, len(unemp_months))
    base[(unemp_months >= "2020-04-01") & (unemp_months <= "2020-08-01")] += 7  # pandemic spike
    unemployment = pd.DataFrame({"MONTH": unemp_months, "UNRATE": base.round(1),
                                 "UE_BENEFITS_WEB_SEARCH": np.clip(base * 8 + rng.normal(0, 5, len(base)), 0, 100).round()})
    return price, trends, unemployment


def analyse() -> pd.Series:
    price, trends, unemployment = make()
    OUT.mkdir(exist_ok=True)
    print("missing price values:", price["CLOSE"].isna().sum())
    price = price.dropna()
    monthly = price.set_index("DATE")["CLOSE"].resample("ME").last()
    print("daily rows:", len(price), "-> monthly rows:", len(monthly))
    fig, ax1 = plt.subplots(figsize=(14, 7))
    ax2 = ax1.twinx()
    ax1.plot(monthly.index, monthly.values, color="#F08F2E", linewidth=3)
    ax2.plot(trends["MONTH"], trends["COIN_SEARCH"], color="skyblue", linewidth=3)
    ax1.set_ylabel("Coin price (USD)", color="#F08F2E")
    ax2.set_ylabel("Search interest", color="skyblue")
    ax1.xaxis.set_major_locator(mdates.YearLocator())
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax1.xaxis.set_minor_locator(mdates.MonthLocator())
    plt.title("Coin price vs search interest (synthetic)")
    fig.savefig(OUT / "coin_vs_search.png", dpi=100)
    plt.close(fig)
    roll = unemployment.set_index("MONTH")[["UNRATE", "UE_BENEFITS_WEB_SEARCH"]].rolling(6).mean()
    fig, ax1 = plt.subplots(figsize=(14, 7))
    ax2 = ax1.twinx()
    ax1.plot(roll.index, roll["UE_BENEFITS_WEB_SEARCH"], color="skyblue")
    ax2.plot(roll.index, roll["UNRATE"], color="purple", linestyle="--")
    ax1.grid(color="grey", linestyle="--")
    fig.savefig(OUT / "unemployment.png", dpi=100)
    plt.close(fig)
    print("saved charts to output/")
    return monthly


if __name__ == "__main__":
    analyse()
