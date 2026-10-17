"""Day 33 exercise: the 'Kanye says' quote button (tkinter).

API-free: quotes come from the bundled kanye_quotes.json (original placeholder quotes,
not real Kanye quotes) instead of the kanye.rest API.
"""
import json
import os
import random
import tkinter as tk
from pathlib import Path

QUOTES = json.loads(Path(__file__).with_name("kanye_quotes.json").read_text(encoding="utf-8"))


def get_quote(rng=random) -> str:
    return rng.choice(QUOTES)


def build() -> tk.Tk:
    window = tk.Tk()
    window.title("Quote says...")
    window.config(padx=50, pady=50)
    canvas = tk.Canvas(width=300, height=200, bg="white", highlightthickness=0)
    text = canvas.create_text(150, 100, text="Press the button", width=250, font=("Arial", 16, "bold"))
    canvas.grid(row=0, column=0)
    tk.Button(text="New quote", command=lambda: canvas.itemconfig(text, text=get_quote())).grid(row=1, column=0)
    return window


if __name__ == "__main__":
    win = build()
    if os.environ.get("SMOKE_TEST"):
        win.after(800, win.destroy)
    win.mainloop()
