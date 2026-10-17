"""Day 34 - Quizzler: a tkinter GUI for the quiz, with type hints and class-based UI.

API-free: questions come from the bundled questions.json instead of the Open Trivia DB API.
"""
import os
import tkinter as tk

from quiz_brain import QuizBrain, load_questions

THEME = "#375362"


class QuizInterface:
    def __init__(self, brain: QuizBrain, smoke: bool = False) -> None:
        self.quiz = brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME)
        self.score_label = tk.Label(text="Score: 0", fg="white", bg=THEME)
        self.score_label.grid(row=0, column=1)
        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.text = self.canvas.create_text(150, 125, width=280, text="", fill=THEME, font=("Arial", 18, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_btn = tk.Button(text="True ✔", width=10, command=lambda: self.answer("True"))
        self.true_btn.grid(row=2, column=0)
        self.false_btn = tk.Button(text="False ✘", width=10, command=lambda: self.answer("False"))
        self.false_btn.grid(row=2, column=1)
        self.next_question()
        if smoke:
            self.window.after(800, self.window.destroy)
        self.window.mainloop()

    def next_question(self) -> None:
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.text, text=f"You've reached the end. Score: {self.quiz.score}")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def answer(self, value: str) -> None:
        self.canvas.config(bg="green" if self.quiz.check_answer(value) else "red")
        self.window.after(1000, self.next_question)


if __name__ == "__main__":
    QuizInterface(QuizBrain(load_questions()), smoke=bool(os.environ.get("SMOKE_TEST")))
