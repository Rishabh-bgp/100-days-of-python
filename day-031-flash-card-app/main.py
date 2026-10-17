"""Day 31 - Flash Card app: tkinter + pandas, flipping a card with window.after().

Card faces are drawn on the canvas (the course uses image assets).
"""
import os
import tkinter as tk

from deck import Deck

BG = "#B1DDC6"


def build() -> tk.Tk:
    deck = Deck()
    window = tk.Tk()
    window.title("Flashy")
    window.config(padx=50, pady=50, bg=BG)
    canvas = tk.Canvas(width=800, height=526, bg=BG, highlightthickness=0)
    card = canvas.create_rectangle(20, 20, 780, 506, fill="white", outline="")
    title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
    word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
    canvas.grid(row=0, column=0, columnspan=2)
    state = {"timer": None}

    def flip() -> None:
        canvas.itemconfig(card, fill="#91C2AF")
        canvas.itemconfig(title, text="English", fill="white")
        canvas.itemconfig(word, text=deck.current["English"], fill="white")

    def next_card() -> None:
        if state["timer"]:
            window.after_cancel(state["timer"])
        c = deck.next_card()
        canvas.itemconfig(card, fill="white")
        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(word, text=c["French"], fill="black")
        state["timer"] = window.after(3000, flip)

    def known() -> None:
        deck.mark_known()
        next_card()

    tk.Button(text="✘", font=("Ariel", 30), fg="red", command=next_card).grid(row=1, column=0)
    tk.Button(text="✔", font=("Ariel", 30), fg="green", command=known).grid(row=1, column=1)
    next_card()
    return window


if __name__ == "__main__":
    win = build()
    if os.environ.get("SMOKE_TEST"):
        win.after(800, win.destroy)
    win.mainloop()
