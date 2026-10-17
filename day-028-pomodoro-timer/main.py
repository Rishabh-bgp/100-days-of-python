"""Day 28 - Pomodoro Timer: tkinter canvas, window.after() event loop, dynamic typing.

The course draws a tomato image; here the tomato is drawn with canvas shapes.
"""
import math
import os
import tkinter as tk

PINK, RED, GREEN, YELLOW = "#e2979c", "#e7305b", "#9bdeac", "#f7f5dd"
FONT = "Courier"
WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN = 25, 5, 20


def session_for(rep: int) -> tuple[int, str, str]:
    """rep counts from 1. Returns (minutes, label, colour)."""
    if rep % 8 == 0:
        return LONG_BREAK_MIN, "Break", RED
    if rep % 2 == 0:
        return SHORT_BREAK_MIN, "Break", PINK
    return WORK_MIN, "Work", GREEN


def fmt(seconds: int) -> str:
    return f"{math.floor(seconds / 60)}:{seconds % 60:02d}"


class Pomodoro:
    def __init__(self, window: tk.Tk) -> None:
        self.window = window
        self.reps = 0
        self.job = None
        window.title("Pomodoro")
        window.config(padx=100, pady=50, bg=YELLOW)
        self.title = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT, 50))
        self.title.grid(column=1, row=0)
        self.canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.canvas.create_oval(10, 30, 190, 210, fill="tomato", outline="")
        self.canvas.create_polygon(100, 40, 80, 10, 100, 25, 120, 10, fill="forest green")
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT, 35, "bold"))
        self.canvas.grid(column=1, row=1)
        tk.Button(text="Start", highlightthickness=0, command=self.start).grid(column=0, row=2)
        tk.Button(text="Reset", highlightthickness=0, command=self.reset).grid(column=2, row=2)
        self.checks = tk.Label(fg=GREEN, bg=YELLOW)
        self.checks.grid(column=1, row=3)

    def reset(self) -> None:
        if self.job:
            self.window.after_cancel(self.job)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.title.config(text="Timer", fg=GREEN)
        self.checks.config(text="")
        self.reps = 0

    def start(self) -> None:
        self.reps += 1
        minutes, label, colour = session_for(self.reps)
        self.title.config(text=label, fg=colour)
        self.count_down(minutes * 60)

    def count_down(self, count: int) -> None:
        self.canvas.itemconfig(self.timer_text, text=fmt(count))
        if count > 0:
            self.job = self.window.after(1000, self.count_down, count - 1)
        else:
            self.checks.config(text="✔" * (self.reps // 2))
            self.start()


if __name__ == "__main__":
    root = tk.Tk()
    Pomodoro(root)
    if os.environ.get("SMOKE_TEST"):
        root.after(800, root.destroy)
    root.mainloop()
