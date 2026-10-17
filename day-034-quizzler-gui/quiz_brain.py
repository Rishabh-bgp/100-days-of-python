"""Quiz logic with type hints (shared by the GUI)."""
import html
import json
import random
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Question:
    text: str
    answer: str


def load_questions(amount: int = 10, rng=random) -> list[Question]:
    raw = json.loads(Path(__file__).with_name("questions.json").read_text(encoding="utf-8"))
    rng.shuffle(raw)
    return [Question(html.unescape(q["text"]), q["answer"]) for q in raw[:amount]]


class QuizBrain:
    def __init__(self, questions: list[Question]) -> None:
        self.questions = questions
        self.number = 0
        self.score = 0
        self.current: Question | None = None

    def still_has_questions(self) -> bool:
        return self.number < len(self.questions)

    def next_question(self) -> str:
        self.current = self.questions[self.number]
        self.number += 1
        return f"Q.{self.number}: {self.current.text}"

    def check_answer(self, answer: str) -> bool:
        ok = self.current is not None and answer.lower() == self.current.answer.lower()
        self.score += ok
        return ok
