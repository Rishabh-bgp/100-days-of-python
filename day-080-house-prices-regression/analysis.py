"""Day 80 - Predict house prices with multivariable regression: explore features,
train/test split, LinearRegression, coefficients, residual analysis, a log transform of
the target, and a valuation for a new property.

Offline: the course uses the (now deprecated) Boston housing data; here a synthetic
dataset with similar features (rooms, distance to work, pollution, river, etc.) is
generated in code.
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


def make(seed: int = 80, n: int = 600) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    rooms = rng.normal(6.3, 0.7, n)
    dis = rng.lognormal(1.2, 0.5, n)
    nox = np.clip(0.75 - 0.05 * dis + rng.normal(0, 0.05, n), 0.35, 0.9)
    chas = (rng.random(n) < 0.07).astype(int)
    ptratio = rng.normal(18.5, 2, n)
    lstat = np.clip(rng.normal(12, 7, n) - 3 * (rooms - 6.3), 1.7, 38)
    log_price = 3.0 + 0.12 * rooms - 0.03 * lstat - 0.6 * nox + 0.1 * chas - 0.03 * ptratio + 0.02 * dis + rng.normal(0, 0.15, n)
    return pd.DataFrame({"RM": rooms, "DIS": dis, "NOX": nox, "CHAS": chas, "PTRATIO": ptratio, "LSTAT": lstat,
                         "PRICE": np.exp(log_price) * 10})  # in $1000s


def fit(x: pd.DataFrame, y: pd.Series) -> tuple[LinearRegression, float, float]:
    x_tr, x_te, y_tr, y_te = train_test_split(x, y, test_size=0.2, random_state=10)
    model = LinearRegression().fit(x_tr, y_tr)
    return model, model.score(x_tr, y_tr), model.score(x_te, y_te)


def analyse() -> dict:
    df = make()
    OUT.mkdir(exist_ok=True)
    print(df.describe().round(2).loc[["mean", "min", "max"]])
    print("correlations with price:\n", df.corr()["PRICE"].drop("PRICE").round(2))
    features = df.drop(columns="PRICE")
    model, r2_train, r2_test = fit(features, df["PRICE"])
    print(f"\nplain model R² train {r2_train:.3f}, test {r2_test:.3f}")
    print("coefficients:\n", pd.Series(model.coef_, index=features.columns).round(3))
    print(f"price skew {df['PRICE'].skew():.2f} vs log price skew {np.log(df['PRICE']).skew():.2f}")
    log_model, r2_train_log, r2_test_log = fit(features, np.log(df["PRICE"]))
    print(f"log model R² train {r2_train_log:.3f}, test {r2_test_log:.3f}")
    predicted = log_model.predict(features)
    residuals = np.log(df["PRICE"]) - predicted
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    axes[0].scatter(np.exp(predicted), df["PRICE"], alpha=0.5)
    axes[0].plot(df["PRICE"], df["PRICE"], color="cyan")
    axes[0].set(xlabel="Predicted price", ylabel="Actual price", title="Actual vs predicted")
    axes[1].hist(residuals, bins=40)
    axes[1].set(title=f"Log residuals (mean {residuals.mean():.3f})")
    fig.savefig(OUT / "regression.png", dpi=100)
    plt.close(fig)
    house = features.mean().to_frame().T
    house["RM"], house["CHAS"] = 8, 1
    estimate = float(np.exp(log_model.predict(house))[0]) * 1000
    print(f"\nValuation for an 8-room riverside house with average other features: ${estimate:,.0f}")
    return {"r2_test_log": r2_test_log, "estimate": estimate}


if __name__ == "__main__":
    analyse()
