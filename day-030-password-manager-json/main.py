"""Day 30 - Password Manager v2: JSON storage, search, try/except/else/finally."""
import os
import secrets
import string
import tkinter as tk
from tkinter import messagebox

import vault


def generate_password() -> str:
    pool = string.ascii_letters + string.digits + "!#$%&()*+"
    return "".join(secrets.choice(pool) for _ in range(16))


def build() -> tk.Tk:
    window = tk.Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)
    tk.Label(text="Website:").grid(row=1, column=0)
    tk.Label(text="Email/Username:").grid(row=2, column=0)
    tk.Label(text="Password:").grid(row=3, column=0)
    website = tk.Entry(width=21)
    website.grid(row=1, column=1)
    email = tk.Entry(width=35)
    email.grid(row=2, column=1, columnspan=2)
    password = tk.Entry(width=21)
    password.grid(row=3, column=1)

    def on_search() -> None:
        entry = vault.find(website.get())
        if entry:
            messagebox.showinfo(title=website.get(), message=f"Email: {entry['email']}\nPassword: {entry['password']}")
        else:
            messagebox.showinfo(title="Not found", message=f"No details for {website.get()} exist.")

    def on_generate() -> None:
        password.delete(0, tk.END)
        password.insert(0, generate_password())

    def on_save() -> None:
        if not website.get() or not password.get():
            messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
            return
        vault.add(website.get(), email.get(), password.get())
        website.delete(0, tk.END)
        password.delete(0, tk.END)

    tk.Button(text="Search", width=13, command=on_search).grid(row=1, column=2)
    tk.Button(text="Generate Password", command=on_generate).grid(row=3, column=2)
    tk.Button(text="Add", width=36, command=on_save).grid(row=4, column=1, columnspan=2)
    return window


if __name__ == "__main__":
    win = build()
    if os.environ.get("SMOKE_TEST"):
        win.after(800, win.destroy)
    win.mainloop()
