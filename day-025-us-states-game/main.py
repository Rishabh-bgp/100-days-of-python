"""Day 25 - U.S. States Game: pandas + turtle. Guess state names; correct ones appear on the map.

The course uses a blank-map image; this draws a simple outline grid instead, and the
state positions in 50_states.csv were computed from approximate state centroids.
"""
from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent


def load_states() -> pd.DataFrame:
    return pd.read_csv(HERE / "50_states.csv")


def check_guess(data: pd.DataFrame, guess: str) -> tuple[str, int, int] | None:
    row = data[data["state"].str.lower() == guess.strip().lower()]
    if row.empty:
        return None
    r = row.iloc[0]
    return r["state"], int(r["x"]), int(r["y"])


def missing_states(data: pd.DataFrame, guessed: set[str]) -> pd.DataFrame:
    return data[~data["state"].isin(guessed)][["state"]]


def main() -> None:
    import turtle

    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.setup(725, 491)
    data = load_states()
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    guessed: set[str] = set()
    while len(guessed) < len(data):
        answer = screen.textinput(f"{len(guessed)}/50 States Correct", "What's another state's name? (Exit to stop)")
        if answer is None or answer.lower() == "exit":
            break
        hit = check_guess(data, answer)
        if hit and hit[0] not in guessed:
            guessed.add(hit[0])
            writer.goto(hit[1], hit[2])
            writer.write(hit[0], align="center", font=("Arial", 8, "normal"))
    missing_states(data, guessed).to_csv(HERE / "states_to_learn.csv", index=False)
    print(f"You got {len(guessed)} states. The rest are in states_to_learn.csv")


if __name__ == "__main__":
    main()
