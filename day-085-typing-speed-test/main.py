"""Day 85 - Portfolio project: typing speed test (tkinter). The timer starts on your first
keystroke; press Enter to finish and see gross WPM, net WPM and accuracy.
"""
import os
import time
import tkinter as tk

from typing_core import pick_sentence, score


def build() -> tk.Tk:
    window = tk.Tk()
    window.title("Typing Speed Test")
    window.config(padx=30, pady=30)
    state = {"target": pick_sentence(), "start": None}
    prompt = tk.Label(text=state["target"], wraplength=500, font=("Courier", 14))
    prompt.pack(pady=10)
    entry = tk.Entry(width=70, font=("Courier", 12))
    entry.pack()
    entry.focus()
    result = tk.Label(text="Start typing - the timer starts on your first key.", font=("Arial", 12))
    result.pack(pady=10)

    def on_key(event) -> None:
        if state["start"] is None and event.keysym not in {"Return", "Shift_L", "Shift_R"}:
            state["start"] = time.perf_counter()

    def finish(_event=None) -> None:
        if state["start"] is None:
            return
        s = score(state["target"], entry.get(), time.perf_counter() - state["start"])
        result.config(text=f"{s['wpm']} WPM (net {s['net_wpm']}), accuracy {s['accuracy']}%")

    def restart() -> None:
        state["target"], state["start"] = pick_sentence(), None
        prompt.config(text=state["target"])
        entry.delete(0, tk.END)
        result.config(text="Start typing - the timer starts on your first key.")

    entry.bind("<Key>", on_key)
    entry.bind("<Return>", finish)
    tk.Button(text="Restart", command=restart).pack()
    return window


if __name__ == "__main__":
    win = build()
    if os.environ.get("SMOKE_TEST"):
        win.after(800, win.destroy)
    win.mainloop()
