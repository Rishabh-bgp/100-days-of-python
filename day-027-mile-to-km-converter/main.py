"""Day 27 - Mile to Km Converter: tkinter widgets, grid layout, button callbacks."""
import os
import tkinter as tk


def miles_to_km(miles: float) -> float:
    return round(miles * 1.609344, 2)


def build() -> tk.Tk:
    window = tk.Tk()
    window.title("Mile to Km Converter")
    window.config(padx=20, pady=20)
    entry = tk.Entry(width=7)
    entry.insert(0, "0")
    entry.grid(column=1, row=0)
    tk.Label(text="Miles").grid(column=2, row=0)
    tk.Label(text="is equal to").grid(column=0, row=1)
    result = tk.Label(text="0")
    result.grid(column=1, row=1)
    tk.Label(text="Km").grid(column=2, row=1)

    def calculate() -> None:
        try:
            result.config(text=str(miles_to_km(float(entry.get()))))
        except ValueError:
            result.config(text="?")

    tk.Button(text="Calculate", command=calculate).grid(column=1, row=2)
    return window


if __name__ == "__main__":
    win = build()
    if os.environ.get("SMOKE_TEST"):
        win.after(800, win.destroy)
    win.mainloop()
