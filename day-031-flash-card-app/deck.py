"""Deck logic (no GUI) so it can be tested: pick cards, remove known ones, persist progress."""
import random
from pathlib import Path

import pandas as pd

HERE = Path(__file__).parent
WORDS = HERE / "french_words.csv"
TO_LEARN = HERE / "words_to_learn.csv"


class Deck:
    def __init__(self, rng=random) -> None:
        try:
            self.cards = pd.read_csv(TO_LEARN).to_dict(orient="records")
        except FileNotFoundError:
            self.cards = pd.read_csv(WORDS).to_dict(orient="records")
        self.rng = rng
        self.current: dict | None = None

    def next_card(self) -> dict:
        self.current = self.rng.choice(self.cards)
        return self.current

    def mark_known(self, save: bool = True) -> None:
        if self.current in self.cards:
            self.cards.remove(self.current)
        if save:
            pd.DataFrame(self.cards).to_csv(TO_LEARN, index=False)
