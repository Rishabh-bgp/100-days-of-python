"""Day 89 - Portfolio project: the 'most dangerous writing app'. Keep typing - if you stop
for 5 seconds, everything you wrote disappears. A progress bar shows the countdown and you
can save your text once you reach the word goal.
"""
import os
import tkinter as tk
from pathlib import Path
from tkinter import ttk

TIMEOUT_MS = 5000
WORD_GOAL = 100


class DangerousWriter:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.last_key_job = None
        self.elapsed = 0
        root.title("Disappearing Text")
        root.config(padx=20, pady=20)
        tk.Label(text=f"Write {WORD_GOAL} words. Stop for {TIMEOUT_MS // 1000}s and it's all gone!",
                 font=("Arial", 13)).pack()
        self.bar = ttk.Progressbar(length=500, maximum=TIMEOUT_MS)
        self.bar.pack(pady=8)
        self.text = tk.Text(width=70, height=18, wrap="word", font=("Georgia", 12))
        self.text.pack()
        self.text.focus()
        self.status = tk.Label(text="0 words")
        self.status.pack(pady=5)
        self.save_btn = tk.Button(text="Save text", state="disabled", command=self.save)
        self.save_btn.pack()
        self.text.bind("<Key>", self.on_key)
        self.tick()

    def word_count(self) -> int:
        return len(self.text.get("1.0", "end").split())

    def on_key(self, _event=None) -> None:
        self.elapsed = 0
        self.root.after(1, self.update_status)

    def update_status(self) -> None:
        n = self.word_count()
        self.status.config(text=f"{n} words")
        if n >= WORD_GOAL:
            self.save_btn.config(state="normal")

    def tick(self) -> None:
        if self.word_count() > 0:
            self.elapsed += 100
            self.bar["value"] = self.elapsed
            if self.elapsed >= TIMEOUT_MS:
                self.text.delete("1.0", "end")
                self.status.config(text="Too slow! Your text vanished.")
                self.save_btn.config(state="disabled")
                self.elapsed = 0
                self.bar["value"] = 0
        self.root.after(100, self.tick)

    def save(self) -> None:
        path = Path(__file__).with_name("my_writing.txt")
        path.write_text(self.text.get("1.0", "end"), encoding="utf-8")
        self.status.config(text=f"Saved to {path.name}")


if __name__ == "__main__":
    root = tk.Tk()
    DangerousWriter(root)
    if os.environ.get("SMOKE_TEST"):
        root.after(800, root.destroy)
    root.mainloop()
