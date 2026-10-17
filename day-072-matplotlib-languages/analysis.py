"""Day 72 - Data visualisation with matplotlib: popularity of programming languages over
time (posts per month by tag), pivot tables, rolling means and multi-line charts.

Offline: the course uses a Stack Overflow query export; here a synthetic monthly
post-count dataset with realistic-looking trends is generated in code.
Charts are saved to output/.
"""
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).with_name("output")
TRENDS = {  # (start level, yearly growth, noise)
    "python": (2000, 0.18, 0.06), "javascript": (6000, 0.06, 0.05), "java": (7000, -0.04, 0.05),
    "c#": (5000, -0.03, 0.05), "php": (4000, -0.08, 0.06), "c++": (2500, -0.01, 0.05),
    "r": (400, 0.15, 0.08), "go": (50, 0.35, 0.10), "swift": (100, 0.25, 0.10),
}


def make(seed: int = 72) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2009-01-01", "2025-12-01", freq="MS")
    rows = []
    for tag, (level, growth, noise) in TRENDS.items():
        t = np.arange(len(dates)) / 12
        posts = level * (1 + growth) ** t * rng.normal(1, noise, len(dates))
        rows += [{"DATE": d, "TAG": tag, "POSTS": max(int(p), 0)} for d, p in zip(dates, posts)]
    return pd.DataFrame(rows)


def analyse(df: pd.DataFrame) -> pd.DataFrame:
    print(df.head(), "\nentries per language:\n", df.groupby("TAG").size())
    print("\ntotal posts by language:\n", df.groupby("TAG")["POSTS"].sum().sort_values(ascending=False))
    reshaped = df.pivot(index="DATE", columns="TAG", values="POSTS").fillna(0)
    rolling = reshaped.rolling(window=6).mean()
    OUT.mkdir(exist_ok=True)
    plt.figure(figsize=(14, 7))
    plt.xlabel("Date", fontsize=14)
    plt.ylabel("Number of posts (6-month rolling mean)", fontsize=14)
    for col in rolling.columns:
        plt.plot(rolling.index, rolling[col], linewidth=2.5, label=col)
    plt.legend(fontsize=12)
    plt.title("Programming language popularity (synthetic data)")
    plt.savefig(OUT / "languages.png", dpi=100, bbox_inches="tight")
    plt.close()
    print("saved output/languages.png")
    return reshaped


if __name__ == "__main__":
    analyse(make())
