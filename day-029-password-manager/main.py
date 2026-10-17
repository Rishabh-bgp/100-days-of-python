"""Day 29 - Password Manager (tkinter): generate, copy and save passwords to a local file.

Saved entries go to data.txt next to this script (git-ignored). Clipboard copy uses
tkinter's own clipboard instead of the third-party 'pyperclip'.
"""
import os
import secrets
import string
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

DATA_FILE = Path(__file__).with_name("data.txt")


def generate_password(letters: int = 10, symbols: int = 3, numbers: int = 3) -> str:
    chars = ([secrets.choice(string.ascii_letters) for _ in range(letters)]
             + [secrets.choice("!#$%&()*+") for _ in range(symbols)]
             + [secrets.choice(string.digits) for _ in range(numbers)])
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def save_entry(website: str, email: str, password: str, path: Path = DATA_FILE) -> None:
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(f"{website} | {email} | {password}\n")


def build() -> tk.Tk:
    window = tk.Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)
    logo = tk.Canvas(height=120, width=200, highlightthickness=0)
    logo.create_rectangle(70, 50, 130, 110, fill="goldenrod", outline="")
    logo.create_arc(80, 15, 120, 85, start=0, extent=180, style="arc", width=8)
    logo.grid(row=0, column=1)
    for r, text in enumerate(["Website:", "Email/Username:", "Password:"], start=1):
        tk.Label(text=text).grid(row=r, column=0)
    website = tk.Entry(width=35)
    website.grid(row=1, column=1, columnspan=2)
    website.focus()
    email = tk.Entry(width=35)
    email.grid(row=2, column=1, columnspan=2)
    email.insert(0, "you@example.com")
    password = tk.Entry(width=21)
    password.grid(row=3, column=1)

    def on_generate() -> None:
        pw = generate_password()
        password.delete(0, tk.END)
        password.insert(0, pw)
        window.clipboard_clear()
        window.clipboard_append(pw)

    def on_save() -> None:
        w, e, p = website.get(), email.get(), password.get()
        if not w or not p:
            messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
            return
        if messagebox.askokcancel(title=w, message=f"Details entered:\nEmail: {e}\nPassword: {p}\nSave?"):
            save_entry(w, e, p)
            website.delete(0, tk.END)
            password.delete(0, tk.END)

    tk.Button(text="Generate Password", command=on_generate).grid(row=3, column=2)
    tk.Button(text="Add", width=36, command=on_save).grid(row=4, column=1, columnspan=2)
    return window


if __name__ == "__main__":
    win = build()
    if os.environ.get("SMOKE_TEST"):
        win.after(800, win.destroy)
    win.mainloop()
