"""Day 100 - Predict earnings using multivariable regression: how much do schooling and
work experience explain hourly pay? Data cleaning, train/test split, simple vs
multivariable LinearRegression, coefficients, residuals, and a prediction.

Offline and SYNTHETIC: the course uses NLSY97 survey data; here 2,000 people with
education, experience and a few other features are generated in code (with noise), so the
coefficients are illustrative, not real labour-market estimates.
"""
from pathlib import Path

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from sklearn.linear_model import LinearRegression  # noqa: E402
from sklearn.model_selection import train_test_split  # noqa: E402

OUT = Path(__file__).with_name("output")


def make(seed: int = 100, n: int = 2000) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    school = rng.choice(range(8, 21), n, p=np.array([1, 1, 2, 3, 10, 6, 5, 4, 12, 3, 4, 2, 2]) / 55)
    exper = np.clip(rng.normal(12, 4, n), 0, 30).round(1)
    female = rng.random(n) < 0.5
    urban = rng.random(n) < 0.7
    log_wage = 1.2 + 0.09 * school + 0.03 * exper - 0.0005 * exper ** 2 + 0.08 * urban - 0.1 * female + rng.normal(0, 0.45, n)
    df = pd.DataFrame({"S": school, "EXP": exper, "FEMALE": female.astype(int), "URBAN": urban.astype(int),
                       "EARNINGS": np.exp(log_wage).round(2)})
    return pd.concat([df, df.sample(40, random_state=1)], ignore_index=True)  # duplicates to clean


def fit(x: pd.DataFrame, y: pd.Series):
    x_tr, x_te, y_tr, y_te = train_test_split(x, y, test_size=0.2, random_state=10)
    model = LinearRegression().fit(x_tr, y_tr)
    return model, model.score(x_tr, y_tr), model.score(x_te, y_te), (x_te, y_te)


def analyse() -> dict:
    df = make()
    OUT.mkdir(exist_ok=True)
    print("rows:", len(df), "| duplicates:", df.duplicated().sum())
    df = df.drop_duplicates()
    print(df.describe().round(2).loc[["mean", "min", "max"]])
    simple, r2_tr, r2_te, _ = fit(df[["S"]], df["EARNINGS"])
    print(f"\nsimple (schooling only): R² train {r2_tr:.3f}, test {r2_te:.3f}; "
          f"each extra year of school ≈ ${simple.coef_[0]:.2f}/hour")
    features = ["S", "EXP", "FEMALE", "URBAN"]
    multi, r2_tr, r2_te, (x_te, y_te) = fit(df[features], df["EARNINGS"])
    print(f"multivariable: R² train {r2_tr:.3f}, test {r2_te:.3f}")
    print("coefficients ($/hour):\n", pd.Series(multi.coef_, index=features).round(3))
    residuals = y_te - multi.predict(x_te)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].scatter(multi.predict(x_te), y_te, alpha=0.4)
    axes[0].plot([0, y_te.max()], [0, y_te.max()], color="red")
    axes[0].set(xlabel="Predicted $/hour", ylabel="Actual $/hour", title="Actual vs predicted")
    axes[1].hist(residuals, bins=40)
    axes[1].set(title=f"Residuals (mean {residuals.mean():.2f}, skew {residuals.skew():.2f})")
    fig.savefig(OUT / "earnings_regression.png", dpi=100)
    plt.close(fig)
    person = pd.DataFrame([{"S": 16, "EXP": 5, "FEMALE": 0, "URBAN": 1}])
    estimate = float(multi.predict(person)[0])
    print(f"\nPredicted hourly earnings for a graduate (16 years of school) with 5 years' experience: ${estimate:.2f}")
    return {"r2_test": r2_te, "estimate": estimate}


if __name__ == "__main__":
    analyse()
