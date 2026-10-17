"""Question model and QuizBrain classes."""
import html
import json
import random
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).parent


@dataclass
class Question:
    text: str
    answer: str


def load_questions(path: Path = HERE / "questions.json", shuffle: bool = True, rng=random) -> list[Question]:
    data = json.loads(path.read_text(encoding="utf-8"))
    bank = [Question(html.unescape(q["text"]), q["answer"]) for q in data]
    if shuffle:
        rng.shuffle(bank)
    return bank


class QuizBrain:
    def __init__(self, questions: list[Question]) -> None:
        self.question_number = 0
        self.score = 0
        self.questions = questions
        self.current: Question | None = None

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.questions)

    def next_question(self) -> str:
        self.current = self.questions[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current.text}"

    def check_answer(self, user_answer: str) -> bool:
        assert self.current is not None
        correct = user_answer.strip().lower() in {self.current.answer.lower(), self.current.answer[0].lower()}
        if correct:
            self.score += 1
        return correct
