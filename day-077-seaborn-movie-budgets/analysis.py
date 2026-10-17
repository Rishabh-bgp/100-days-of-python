"""Day 77 - Linear regression and seaborn: do bigger movie budgets mean higher revenue?
Cleaning currency strings, filtering unreleased films, seaborn scatter/bubble and regplot,
floor-division to decades, and scikit-learn LinearRegression (slope, intercept, R²).

Offline: the course scrapes budget data from a movie-numbers website; here a synthetic
dataset of 4,000 films with '$1,234' style strings is generated in code.
"""
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import seaborn as sns  # noqa: E402
from sklearn.linear_model import LinearRegression  # noqa: E402

OUT = Path(__file__).with_name("output")


def make(seed: int = 77, n: int = 4000) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    years = rng.integers(1915, 2026, n)
    budget = (rng.lognormal(16, 1.2, n) * (1 + (years - 1915) / 30)).astype(int)
    revenue = (budget * rng.lognormal(0.9, 0.9, n) * (rng.random(n) > 0.06)).astype(int)
    dates = pd.to_datetime([f"{y}-{rng.integers(1, 13):02d}-15" for y in years])
    fmt = lambda v: f"${v:,}"  # noqa: E731
    return pd.DataFrame({"Release_Date": dates.strftime("%m/%d/%Y"), "Movie_Title": [f"Film {i}" for i in range(n)],
                         "USD_Production_Budget": list(map(fmt, budget)),
                         "USD_Worldwide_Gross": list(map(fmt, revenue)),
                         "USD_Domestic_Gross": list(map(fmt, (revenue * rng.uniform(0.2, 0.6, n)).astype(int)))})


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in ["USD_Production_Budget", "USD_Worldwide_Gross", "USD_Domestic_Gross"]:
        df[col] = pd.to_numeric(df[col].str.replace(r"[$,]", "", regex=True))
    df["Release_Date"] = pd.to_datetime(df["Release_Date"], format="%m/%d/%Y")
    df["Decade"] = (pd.DatetimeIndex(df["Release_Date"]).year // 10) * 10
    return df


def regress(data: pd.DataFrame) -> tuple[float, float, float]:
    x = data[["USD_Production_Budget"]]
    y = data[["USD_Worldwide_Gross"]]
    model = LinearRegression().fit(x, y)
    return float(model.coef_[0][0]), float(model.intercept_[0]), float(model.score(x, y))


def analyse() -> dict:
    df = clean(make())
    OUT.mkdir(exist_ok=True)
    zero = df[df["USD_Worldwide_Gross"] == 0]
    print(f"films: {len(df)} | grossed $0 worldwide: {len(zero)} | average budget ${df['USD_Production_Budget'].mean():,.0f}")
    old, new = df[df["Decade"] <= 1960], df[df["Decade"] > 1960]
    plt.figure(figsize=(10, 6), dpi=100)
    with sns.axes_style("darkgrid"):
        ax = sns.scatterplot(data=df, x="Release_Date", y="USD_Production_Budget", hue="USD_Worldwide_Gross",
                             size="USD_Worldwide_Gross", legend=False)
        ax.set(ylabel="Budget in $", xlabel="Year")
    plt.savefig(OUT / "budget_bubble.png")
    plt.close()
    plt.figure(figsize=(8, 5), dpi=100)
    sns.regplot(data=new, x="USD_Production_Budget", y="USD_Worldwide_Gross", color="#2f4b7c",
                scatter_kws={"alpha": 0.3}, line_kws={"color": "#ff7c43"})
    plt.savefig(OUT / "regression_new_films.png")
    plt.close()
    results = {}
    for name, part in (("old films", old), ("new films", new)):
        slope, intercept, r2 = regress(part)
        results[name] = (slope, r2)
        print(f"{name}: slope {slope:.2f}, intercept {intercept:,.0f}, R² {r2:.3f}")
    slope, intercept, _ = regress(new)
    print(f"Predicted revenue for a $350m film: ${intercept + slope * 350e6:,.0f}")
    print("saved charts to output/")
    return results


if __name__ == "__main__":
    analyse()
