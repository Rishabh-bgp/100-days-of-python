"""Day 71 - Data exploration with pandas: which degrees pay best and have the most spread?

Offline: uses a synthetic dataset made by make_data.py (created automatically on first run).
Covers head/shape/columns, isna/dropna, idxmax/loc, sorting, adding a column and groupby.
"""
from pathlib import Path

import pandas as pd

import make_data


def load() -> pd.DataFrame:
    if not make_data.OUT.exists():
        make_data.OUT.parent.mkdir(exist_ok=True)
        make_data.make().to_csv(make_data.OUT, index=False)
    return pd.read_csv(make_data.OUT)


def explore(df: pd.DataFrame) -> dict:
    print(df.head(), "\nshape:", df.shape, "\nmissing values:\n", df.isna().sum().sum())
    clean = df.dropna()
    top_start = clean.loc[clean["Starting Median Salary"].idxmax()]
    low_mid = clean.loc[clean["Mid-Career Median Salary"].idxmin()]
    clean = clean.assign(Spread=clean["Mid-Career 90th Percentile Salary"] - clean["Mid-Career 10th Percentile Salary"])
    low_risk = clean.sort_values("Spread").head(5)[["Undergraduate Major", "Spread"]]
    high_pot = clean.sort_values("Mid-Career 90th Percentile Salary", ascending=False).head(5)[
        ["Undergraduate Major", "Mid-Career 90th Percentile Salary"]]
    by_group = clean.groupby("Group")[["Starting Median Salary", "Mid-Career Median Salary"]].mean().round(0)
    print(f"\nHighest starting salary: {top_start['Undergraduate Major']} (${top_start['Starting Median Salary']:,.0f})")
    print(f"Lowest mid-career salary: {low_mid['Undergraduate Major']} (${low_mid['Mid-Career Median Salary']:,.0f})")
    print("\nLowest-risk majors (smallest spread):\n", low_risk.to_string(index=False))
    print("\nHighest-potential majors (90th percentile):\n", high_pot.to_string(index=False))
    print("\nAverage by group:\n", by_group)
    return {"rows": len(clean), "top_start": top_start["Undergraduate Major"]}


if __name__ == "__main__":
    Path(__file__).with_name("output").mkdir(exist_ok=True)
    explore(load())
