"""Day 81 - Capstone: analyse a dataset of police incidents in the US by state, city,
age, race, armed status and time - cleaning NaNs, merging a census-style table,
grouped bar charts, KDE plots and a monthly time series.

Offline and SYNTHETIC: the course uses real datasets about fatal police shootings and US
census data. Because this is a sensitive topic, the repo does NOT invent "findings" about
real groups: every record here is randomly generated with no built-in group differences,
so the charts show the workflow, not real-world facts. To study the real data, download
the public Washington Post dataset yourself and point load() at it.
"""
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import seaborn as sns  # noqa: E402

OUT = Path(__file__).with_name("output")
STATES = ["CA", "TX", "FL", "AZ", "GA", "CO", "OK", "NC", "OH", "WA"]


def make(seed: int = 81, n: int = 2500) -> tuple[pd.DataFrame, pd.DataFrame]:
    rng = np.random.default_rng(seed)
    incidents = pd.DataFrame({
        "date": pd.to_datetime("2015-01-01") + pd.to_timedelta(rng.integers(0, 3650, n), unit="D"),
        "age": np.where(rng.random(n) < 0.04, np.nan, rng.normal(37, 13, n).clip(14, 90).round()),
        "gender": rng.choice(["M", "F"], n, p=[0.95, 0.05]),
        "group": rng.choice(["Group A", "Group B", "Group C", "Group D"], n),
        "state": rng.choice(STATES, n),
        "armed": rng.choice(["gun", "knife", "unarmed", "vehicle", "unknown", None], n, p=[.55, .15, .07, .05, .08, .10]),
        "signs_of_mental_illness": rng.random(n) < 0.23,
        "body_camera": rng.random(n) < 0.12,
    })
    census = pd.DataFrame({"state": STATES, "poverty_rate": rng.uniform(9, 20, len(STATES)).round(1),
                           "hs_graduation_rate": rng.uniform(82, 92, len(STATES)).round(1)})
    return incidents, census


def analyse() -> pd.DataFrame:
    df, census = make()
    OUT.mkdir(exist_ok=True)
    print("missing values:\n", df.isna().sum()[df.isna().sum() > 0])
    df = df.fillna({"armed": "unknown"}).dropna(subset=["age"])
    print("armed status share:\n", df["armed"].value_counts(normalize=True).round(3))
    print(f"share with signs of mental illness: {df['signs_of_mental_illness'].mean():.1%}")
    by_state = df.groupby("state").size().rename("incidents").reset_index()
    merged = by_state.merge(census, on="state")
    r = merged["incidents"].corr(merged["poverty_rate"])
    print(f"correlation incidents vs poverty: {r:.2f} (random data, only 10 states - any correlation is chance)")
    plt.figure(figsize=(8, 5))
    sns.kdeplot(data=df, x="age", hue="group", common_norm=False)
    plt.title("Age distribution by group (synthetic)")
    plt.savefig(OUT / "age_kde.png", dpi=100)
    plt.close()
    monthly = df.set_index("date").resample("ME").size()
    plt.figure(figsize=(12, 4))
    plt.plot(monthly.index, monthly.values, alpha=0.5)
    plt.plot(monthly.index, monthly.rolling(6).mean(), linewidth=3)
    plt.title("Incidents per month (synthetic) with 6-month average")
    plt.savefig(OUT / "monthly.png", dpi=100)
    plt.close()
    print("saved charts to output/")
    return merged


if __name__ == "__main__":
    analyse()
