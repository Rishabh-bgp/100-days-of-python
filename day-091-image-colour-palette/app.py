"""Day 91 - Portfolio project: image colour palette generator. Upload an image and see its
10 most common colours (hex codes and share), computed locally with NumPy + Pillow.

Run with:  flask --app app run        CLI:  python palette_cli.py image.jpg
"""
import io

from flask import Flask, render_template, request

from palette import top_colours

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024 * 1024  # 8 MB uploads


@app.route("/", methods=["GET", "POST"])
def home():
    colours, error = None, None
    if request.method == "POST":
        file = request.files.get("image")
        if not file or not file.filename:
            error = "Please choose an image file."
        else:
            try:
                colours = top_colours(io.BytesIO(file.read()), n=int(request.form.get("n", 10)))
            except Exception:  # noqa: BLE001 - show a friendly message for any unreadable upload
                error = "Sorry, that file couldn't be read as an image."
    return render_template("index.html", colours=colours, error=error)
