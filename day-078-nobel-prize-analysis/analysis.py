"""Day 78 - Nobel Prize analysis: categories over time, share of women, countries and
organisations. plotly donut, bar, sunburst and choropleth; cumulative sums; rolling means.

Offline: the course uses a Nobel Prize CSV; here a synthetic laureate table (~950 rows)
with the same kinds of columns is generated in code. Charts saved as HTML in output/.
"""
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px

OUT = Path(__file__).with_name("output")
CATS = ["Physics", "Chemistry", "Medicine", "Literature", "Peace", "Economics"]
COUNTRIES = {"United States of America": "USA", "United Kingdom": "GBR", "Germany": "DEU", "France": "FRA",
             "Sweden": "SWE", "Japan": "JPN", "India": "IND", "Russia": "RUS", "Netherlands": "NLD", "Italy": "ITA"}


def make(seed: int = 78) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []
    for year in range(1901, 2026):
        for cat in CATS:
            if cat == "Economics" and year < 1969:
                continue
            for _ in range(rng.choice([1, 2, 3], p=[.5, .3, .2])):
                female_p = 0.03 + 0.12 * (year - 1901) / 124
                country = rng.choice(list(COUNTRIES), p=[.35, .12, .11, .08, .05, .06, .03, .06, .05, .09])
                rows.append({"year": year, "category": cat, "sex": "Female" if rng.random() < female_p else "Male",
                             "birth_country_current": country, "ISO": COUNTRIES[country],
                             "organization_name": rng.choice([None, "Sample University", "Institute of Examples",
                                                              "Mock Research Lab", "Placeholder College"]),
                             "birth_year": year - int(rng.normal(60, 10))})
    return pd.DataFrame(rows)


def analyse() -> pd.DataFrame:
    df = make()
    OUT.mkdir(exist_ok=True)
    df["winning_age"] = df["year"] - df["birth_year"]
    print("prizes:", len(df), "| first year:", df["year"].min())
    sex = df["sex"].value_counts()
    print(f"women: {sex.get('Female', 0) / len(df):.1%}")
    px.pie(names=sex.index, values=sex.values, hole=0.6, title="Percentage of male vs female laureates").write_html(OUT / "sex_donut.html")
    per_year = df.groupby("year").size()
    print("rolling 5-year average prizes (latest):", per_year.rolling(5).mean().iloc[-1].round(2))
    cat_sex = df.groupby(["category", "sex"], as_index=False).size()
    px.bar(cat_sex, x="category", y="size", color="sex", title="Prizes by category and sex").write_html(OUT / "category_sex.html")
    by_country = df.groupby(["birth_country_current", "ISO"], as_index=False).size()
    px.choropleth(by_country, locations="ISO", color="size", hover_name="birth_country_current",
                  color_continuous_scale=px.colors.sequential.matter).write_html(OUT / "choropleth.html")
    cumulative = df.groupby(["birth_country_current", "year"]).size().groupby(level=0).cumsum().reset_index(name="prizes")
    px.line(cumulative, x="year", y="prizes", color="birth_country_current", title="Cumulative prizes").write_html(OUT / "cumulative.html")
    orgs = df.dropna(subset=["organization_name"])
    px.sunburst(orgs, path=["birth_country_current", "organization_name"], title="Where do laureates work?").write_html(OUT / "sunburst.html")
    print("median winning age by category:\n", df.groupby("category")["winning_age"].median())
    print("saved interactive charts (HTML) to output/")
    return df


if __name__ == "__main__":
    analyse()
