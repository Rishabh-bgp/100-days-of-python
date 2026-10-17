"""Day 75 - Plotly charts: analyse an app store. Cleaning (duplicates, NaN, '$' and ','
in numbers), pie/donut, bar, scatter and box charts, and grouped comparisons of free vs paid.

Offline: the course uses a Kaggle Google Play export; here a synthetic app catalogue with
messy columns is generated in code. Interactive charts are saved as HTML in output/.
"""
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px

OUT = Path(__file__).with_name("output")
CATS = ["FAMILY", "GAME", "TOOLS", "PRODUCTIVITY", "FINANCE", "PHOTOGRAPHY", "HEALTH_AND_FITNESS", "EDUCATION",
        "SOCIAL", "MEDICAL"]


def make(seed: int = 75, n: int = 3000) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    installs = rng.choice([1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000], n, p=[.25, .3, .25, .14, .05, .01])
    paid = rng.random(n) < 0.08
    df = pd.DataFrame({
        "App": [f"App {i}" for i in range(n)],
        "Category": rng.choice(CATS, n),
        "Rating": np.where(rng.random(n) < 0.1, np.nan, np.clip(rng.normal(4.2, 0.4, n), 1, 5).round(1)),
        "Reviews": (installs * rng.uniform(0.001, 0.05, n)).astype(int),
        "Size_MBs": rng.lognormal(3, 0.8, n).round(1),
        "Installs": [f"{i:,}+" for i in installs],
        "Type": np.where(paid, "Paid", "Free"),
        "Price": np.where(paid, [f"${p:.2f}" for p in rng.choice([0.99, 1.99, 2.99, 4.99, 9.99], n)], "0"),
        "Content_Rating": rng.choice(["Everyone", "Teen", "Mature 17+"], n, p=[.8, .15, .05]),
    })
    return pd.concat([df, df.sample(60, random_state=1)], ignore_index=True)  # add duplicates to clean


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.dropna().drop_duplicates(subset=["App", "Type", "Price"]).copy()
    df["Installs"] = df["Installs"].str.replace(r"[,+]", "", regex=True).astype(int)
    df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)
    df["Revenue_Estimate"] = df["Installs"] * df["Price"]
    return df


def analyse() -> pd.DataFrame:
    df = clean(make())
    OUT.mkdir(exist_ok=True)
    print("rows after cleaning:", len(df))
    print("top revenue apps:\n", df.sort_values("Revenue_Estimate", ascending=False).head(3)[["App", "Revenue_Estimate"]])
    ratings = df["Content_Rating"].value_counts()
    px.pie(names=ratings.index, values=ratings.values, hole=0.6, title="Content rating").write_html(OUT / "ratings_donut.html")
    cat_installs = df.groupby("Category").agg(installs=("Installs", "sum"), apps=("App", "count")).reset_index()
    px.bar(cat_installs.sort_values("installs"), x="installs", y="Category", orientation="h",
           title="Category popularity").write_html(OUT / "category_bar.html")
    px.scatter(cat_installs, x="apps", y="installs", size="apps", color="installs", hover_name="Category",
               log_y=True, title="Category concentration").write_html(OUT / "category_scatter.html")
    px.box(df, x="Type", y="Installs", color="Type", points="all", notched=True, log_y=True,
           title="How many downloads are paid apps giving up?").write_html(OUT / "free_vs_paid_box.html")
    print("saved interactive charts (HTML) to output/")
    return df


if __name__ == "__main__":
    analyse()
