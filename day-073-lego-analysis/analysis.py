"""Day 73 - Aggregate and merge data: LEGO-style sets, themes and colours.
groupby/agg, value_counts, merge on keys, bar charts, and scatter + line on twin axes.

Offline: the course uses Rebrickable CSV exports; here synthetic colours, sets and themes
tables with the same shape are generated in code. Charts saved to output/.
"""
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).with_name("output")


def make(seed: int = 73) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    rng = np.random.default_rng(seed)
    colors = pd.DataFrame({"id": range(1, 41), "name": [f"Colour {i}" for i in range(1, 41)],
                           "is_trans": rng.choice(["t", "f"], 40, p=[0.25, 0.75])})
    theme_names = ["City", "Space", "Castle", "Technic", "Star Fighters", "Friends", "Creator", "Ninja", "Pirates", "Trains"]
    themes = pd.DataFrame({"id": range(1, 11), "name": theme_names})
    years = rng.integers(1949, 2026, 3000)
    sets = pd.DataFrame({
        "set_num": [f"{10000 + i}-1" for i in range(3000)],
        "name": [f"Set {i}" for i in range(3000)],
        "year": years,
        "theme_id": rng.choice(themes["id"], 3000, p=[.2, .1, .08, .12, .15, .1, .1, .06, .04, .05]),
        "num_parts": (rng.lognormal(4, 1, 3000) * (1 + (years - 1949) / 40)).astype(int),
    })
    return colors, sets, themes


def analyse() -> pd.DataFrame:
    colors, sets, themes = make()
    OUT.mkdir(exist_ok=True)
    print("unique colours:", colors["name"].nunique(), "\ntransparent vs opaque:\n", colors["is_trans"].value_counts())
    print("first year:", sets["year"].min(), "| sets that year:", (sets["year"] == sets["year"].min()).sum())
    print("largest sets:\n", sets.sort_values("num_parts", ascending=False).head(3)[["set_num", "year", "num_parts"]])
    per_year = sets.groupby("year").agg(sets=("set_num", "count"), themes=("theme_id", "nunique"),
                                        avg_parts=("num_parts", "mean"))
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax2 = ax1.twinx()
    ax1.plot(per_year.index[:-1], per_year["sets"][:-1], color="g")
    ax2.plot(per_year.index[:-1], per_year["themes"][:-1], color="b")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Number of sets", color="g")
    ax2.set_ylabel("Number of themes", color="b")
    fig.savefig(OUT / "sets_and_themes.png", dpi=100)
    plt.close(fig)
    counts = sets["theme_id"].value_counts().rename_axis("id").reset_index(name="set_count")
    merged = pd.merge(counts, themes, on="id")
    plt.figure(figsize=(12, 6))
    plt.bar(merged["name"][:10], merged["set_count"][:10])
    plt.xticks(rotation=45)
    plt.ylabel("Number of sets")
    plt.savefig(OUT / "top_themes.png", dpi=100, bbox_inches="tight")
    plt.close()
    plt.figure(figsize=(12, 6))
    plt.scatter(per_year.index, per_year["avg_parts"], s=10)
    plt.title("Average parts per set over time")
    plt.savefig(OUT / "parts_per_set.png", dpi=100)
    plt.close()
    print("top themes:\n", merged.head())
    print("saved charts to output/")
    return merged


if __name__ == "__main__":
    analyse()
