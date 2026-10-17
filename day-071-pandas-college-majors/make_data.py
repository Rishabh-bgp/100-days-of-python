"""Generate a synthetic 'salaries by college major' dataset (offline, reproducible).

Columns mirror the kind of table the course explores: starting and mid-career median
salaries plus 10th and 90th percentile mid-career pay. Values are invented.
"""
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).with_name("generated_data") / "salaries_by_college_major.csv"
MAJORS = {
    "STEM": ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Physics", "Mathematics",
             "Chemistry", "Biology", "Civil Engineering", "Statistics", "Information Technology"],
    "Business": ["Finance", "Economics", "Accounting", "Marketing", "Business Management", "International Business"],
    "HASS": ["History", "English", "Philosophy", "Psychology", "Sociology", "Music", "Drama", "Art History",
             "Political Science", "Journalism", "Education", "Spanish"],
}
BASE = {"STEM": 68000, "Business": 56000, "HASS": 42000}


def make(seed: int = 71) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rows = []
    for group, majors in MAJORS.items():
        for m in majors:
            start = BASE[group] * rng.uniform(0.85, 1.2)
            mid = start * rng.uniform(1.5, 2.0)
            p10 = mid * rng.uniform(0.45, 0.6)
            p90 = mid * rng.uniform(1.6, 2.4)
            rows.append([m, round(start, -2), round(mid, -2), round(p10, -2), round(p90, -2), group])
    df = pd.DataFrame(rows, columns=["Undergraduate Major", "Starting Median Salary", "Mid-Career Median Salary",
                                     "Mid-Career 10th Percentile Salary", "Mid-Career 90th Percentile Salary", "Group"])
    df.loc[len(df)] = ["Source: synthetic data for practice", np.nan, np.nan, np.nan, np.nan, np.nan]
    return df


if __name__ == "__main__":
    OUT.parent.mkdir(exist_ok=True)
    make().to_csv(OUT, index=False)
    print("wrote", OUT)
