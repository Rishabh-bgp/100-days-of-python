from pathlib import Path
from turtle import Turtle

HIGH_SCORE_FILE = Path(__file__).with_name("high_score.txt")


class Scoreboard(Turtle):
    """Keeps the score; high score is saved to a local file (the Day 24 upgrade)."""

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = int(HIGH_SCORE_FILE.read_text()) if HIGH_SCORE_FILE.exists() else 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.draw()

    def draw(self) -> None:
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Courier", 18, "normal"))

    def increase(self) -> None:
        self.score += 1
        self.draw()

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            HIGH_SCORE_FILE.write_text(str(self.high_score))
        self.score = 0
        self.draw()
