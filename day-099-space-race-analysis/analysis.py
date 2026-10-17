"""Day 99 - Analyse and visualise the space race: launches by organisation, country,
year and outcome; mission cost; success rate over time; cold-war rivalry - with plotly
(bar, pie, sunburst, choropleth, line) and pandas groupby.

Offline: the course uses a scraped Kaggle launches dataset; here ~4,000 SYNTHETIC launches
with the same kinds of columns are generated in code (organisations are fictional).
Interactive charts are saved as HTML in output/.
"""
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px

OUT = Path(__file__).with_name("output")
ORGS = {  # name: (country, ISO, active from, active to, weight)
    "Red Star Rockets": ("Russia", "RUS", 1957, 2025, 3.0), "Eagle Aerospace": ("USA", "USA", 1958, 2025, 2.5),
    "Falcon Freight": ("USA", "USA", 2008, 2025, 3.5), "Long Road Launch": ("China", "CHN", 1970, 2025, 2.0),
    "Ariane Mock": ("France", "FRA", 1979, 2025, 1.0), "Saffron Space": ("India", "IND", 1979, 2025, 0.8),
    "Rising Sun Rocketry": ("Japan", "JPN", 1966, 2025, 0.6), "Kiwi Orbital": ("New Zealand", "NZL", 2017, 2025, 0.5),
}


def make(seed: int = 99, n: int = 4300) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []
    names = list(ORGS)
    while len(rows) < n:
        year = int(rng.integers(1957, 2026))
        active = [o for o in names if ORGS[o][2] <= year <= ORGS[o][3]]
        w = np.array([ORGS[o][4] for o in active])
        org = rng.choice(active, p=w / w.sum())
        country, iso = ORGS[org][:2]
        fail_p = max(0.03, 0.35 - 0.012 * (year - 1957))
        status = rng.choice(["Success", "Failure", "Partial Failure"], p=[1 - fail_p, fail_p * 0.8, fail_p * 0.2])
        price = round(float(rng.lognormal(4, 0.8)), 1) if rng.random() < 0.3 else np.nan
        rows.append({"Organisation": org, "Country": country, "ISO": iso, "Year": year,
                     "Rocket_Status": "StatusActive" if year > 2005 else "StatusRetired",
                     "Price_musd": price, "Mission_Status": status})
    return pd.DataFrame(rows)


def analyse() -> pd.DataFrame:
    df = make()
    OUT.mkdir(exist_ok=True)
    print("launches:", len(df), "| with known price:", df["Price_musd"].notna().sum())
    by_org = df["Organisation"].value_counts()
    px.bar(x=by_org.index, y=by_org.values, title="Launches per organisation").write_html(OUT / "orgs.html")
    status = df["Mission_Status"].value_counts()
    px.pie(names=status.index, values=status.values, hole=0.5, title="Mission status").write_html(OUT / "status.html")
    by_country = df.groupby(["Country", "ISO"], as_index=False).size()
    px.choropleth(by_country, locations="ISO", color="size", hover_name="Country",
                  title="Launches by country").write_html(OUT / "choropleth.html")
    px.sunburst(df, path=["Country", "Organisation", "Mission_Status"], title="Country > organisation > outcome").write_html(OUT / "sunburst.html")
    yearly = df.groupby("Year").agg(launches=("Mission_Status", "size"),
                                    success_rate=("Mission_Status", lambda s: (s == "Success").mean()))
    px.line(yearly.reset_index(), x="Year", y="success_rate", title="Success rate by year").write_html(OUT / "success_rate.html")
    cold_war = df[(df["Year"] <= 1991) & df["ISO"].isin(["USA", "RUS"])]
    rivalry = cold_war.groupby(["Year", "Country"], as_index=False).size()
    px.line(rivalry, x="Year", y="size", color="Country", title="Cold war launches: USA vs USSR (synthetic)").write_html(OUT / "cold_war.html")
    print("average mission cost by organisation ($m):\n", df.groupby("Organisation")["Price_musd"].mean().round(1).dropna())
    print(f"success rate {yearly['success_rate'].iloc[0]:.0%} in {yearly.index[0]} -> {yearly['success_rate'].iloc[-1]:.0%} in {yearly.index[-1]}")
    print("saved interactive charts (HTML) to output/")
    return yearly


if __name__ == "__main__":
    analyse()
