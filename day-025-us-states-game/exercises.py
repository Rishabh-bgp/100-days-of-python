"""Day 25 exercises: csv module vs pandas, DataFrame/Series basics, the squirrel-census count.

The course uses the real NYC Central Park Squirrel Census CSV; to stay offline this
generates a small synthetic census with the same idea (count squirrels by fur colour).
"""
import csv
import io
import random

import pandas as pd

WEATHER_CSV = """day,temp,condition
Monday,12,Sunny
Tuesday,14,Rain
Wednesday,15,Rain
Thursday,14,Cloudy
Friday,21,Sunny
Saturday,22,Sunny
Sunday,24,Sunny
"""


def temps_with_csv_module() -> list[int]:
    return [int(row["temp"]) for row in csv.DictReader(io.StringIO(WEATHER_CSV))]


def weather_stats() -> dict:
    df = pd.read_csv(io.StringIO(WEATHER_CSV))
    hottest = df[df["temp"] == df["temp"].max()]
    monday_f = df[df["day"] == "Monday"]["temp"].iloc[0] * 9 / 5 + 32
    return {"mean": round(df["temp"].mean(), 2), "max": int(df["temp"].max()),
            "hottest_day": hottest["day"].iloc[0], "monday_f": monday_f}


def squirrel_census(n: int = 3000, seed: int = 7) -> pd.DataFrame:
    rng = random.Random(seed)
    fur = rng.choices(["Gray", "Cinnamon", "Black"], weights=[80, 15, 5], k=n)
    df = pd.DataFrame({"Primary Fur Color": fur})
    counts = df["Primary Fur Color"].value_counts().rename_axis("Fur Color").reset_index(name="Count")
    return counts


if __name__ == "__main__":
    print(temps_with_csv_module())
    print(weather_stats())
    print(squirrel_census())
