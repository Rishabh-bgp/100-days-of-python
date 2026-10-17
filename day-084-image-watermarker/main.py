"""Day 84 - Portfolio project: image watermarking desktop app (tkinter + Pillow).
Pick an image, type your watermark text, preview, and save a watermarked copy.

Also works without a GUI:
  python main.py --cli input.jpg output.png "© My Name" [--tiled]
  python main.py --demo         # makes a sample image and watermarks it
"""
import os
import sys
from pathlib import Path

from watermark import add_watermark, demo_image


def run_gui() -> None:
    import tkinter as tk
    from tkinter import filedialog, messagebox

    from PIL import Image, ImageTk

    window = tk.Tk()
    window.title("Watermarker")
    window.config(padx=20, pady=20)
    state: dict = {"src": None, "preview": None}
    text = tk.Entry(width=30)
    text.insert(0, "© Rishabh Aryan")
    tiled = tk.BooleanVar()
    label = tk.Label(text="Open an image to start")

    def show(path: Path) -> None:
        img = Image.open(path)
        img.thumbnail((500, 350))
        state["preview"] = ImageTk.PhotoImage(img)
        label.config(image=state["preview"], text="")

    def open_image() -> None:
        name = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp *.webp")])
        if name:
            state["src"] = Path(name)
            show(state["src"])

    def save() -> None:
        if not state["src"]:
            messagebox.showinfo("Watermarker", "Open an image first.")
            return
        dst = filedialog.asksaveasfilename(defaultextension=".png", initialfile=f"{state['src'].stem}_watermarked.png")
        if dst:
            show(add_watermark(state["src"], Path(dst), text.get(), tiled=tiled.get()))

    tk.Button(text="Open image", command=open_image).grid(row=0, column=0)
    text.grid(row=0, column=1)
    tk.Checkbutton(text="Tiled", variable=tiled).grid(row=0, column=2)
    tk.Button(text="Watermark & save", command=save).grid(row=0, column=3)
    label.grid(row=1, column=0, columnspan=4, pady=10)
    if os.environ.get("SMOKE_TEST"):
        window.after(800, window.destroy)
    window.mainloop()


def main(argv: list[str]) -> None:
    if argv[:1] == ["--demo"]:
        out_dir = Path(__file__).with_name("output")
        out_dir.mkdir(exist_ok=True)
        src = demo_image(out_dir / "sample.png")
        print("wrote", add_watermark(src, out_dir / "sample_watermarked.png"))
        print("wrote", add_watermark(src, out_dir / "sample_tiled.png", tiled=True))
    elif argv[:1] == ["--cli"]:
        src, dst, text = Path(argv[1]), Path(argv[2]), argv[3]
        print("wrote", add_watermark(src, dst, text, tiled="--tiled" in argv))
    else:
        run_gui()


if __name__ == "__main__":
    main(sys.argv[1:])
