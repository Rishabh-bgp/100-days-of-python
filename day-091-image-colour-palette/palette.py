"""Find the most common colours in an image with Pillow + NumPy (colour quantisation)."""
from pathlib import Path

import numpy as np
from PIL import Image


def top_colours(path: Path | str, n: int = 10, bucket: int = 24) -> list[tuple[str, float]]:
    """Return [(hex, share)] for the n most common colours, after rounding each channel to `bucket`."""
    img = Image.open(path).convert("RGB")
    img.thumbnail((300, 300))
    pixels = np.asarray(img).reshape(-1, 3)
    quantised = (pixels // bucket) * bucket + bucket // 2
    quantised = np.clip(quantised, 0, 255)
    colours, counts = np.unique(quantised, axis=0, return_counts=True)
    order = np.argsort(counts)[::-1][:n]
    total = counts.sum()
    return [("#{:02x}{:02x}{:02x}".format(*colours[i]), round(counts[i] / total, 4)) for i in order]


def demo_image(path: Path) -> Path:
    """Generate a striped sample image with known colours."""
    arr = np.zeros((200, 300, 3), dtype=np.uint8)
    stripes = [(230, 57, 70), (241, 250, 238), (168, 218, 220), (69, 123, 157), (29, 53, 87)]
    widths = [90, 70, 60, 50, 30]
    x = 0
    for colour, w in zip(stripes, widths):
        arr[:, x:x + w] = colour
        x += w
    Image.fromarray(arr).save(path)
    return path
