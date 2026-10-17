"""Day 76 - Computation with NumPy: ndarrays, shape/ndim, slicing, broadcasting,
vectorised maths, matrix multiplication, random generation, and images as arrays.

Offline: the 'image' is generated in code (a gradient with a circle) instead of a photo.
"""
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).with_name("output")


def basics() -> dict:
    my_array = np.array([1.1, 9.2, 8.1, 4.7])
    array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])
    mystery = np.arange(24).reshape(3, 2, 4)
    a = np.arange(10, 30)
    print("1D:", my_array.shape, "| 2D:", array_2d.shape, array_2d.ndim, "| 3D:", mystery.shape)
    print("last 3:", a[-3:], "| every 3rd:", a[::3], "| reversed:", a[::-1][:5])
    print("non-zero indices:", np.nonzero([6, 0, 9, 0, 0, 5, 0])[0])
    print("linspace:", np.linspace(0, 100, num=9))
    v1, v2 = np.array([4, 5, 2, 7]), np.array([2, 1, 3, 3])
    print("v1 + v2:", v1 + v2, "| v1 * v2:", v1 * v2, "| broadcast * 3:", v1 * 3)
    a1 = np.array([[1, 3], [0, 1], [6, 2], [9, 7]])
    b1 = np.array([[4, 1, 3], [5, 8, 5]])
    product = a1 @ b1
    print("matmul:\n", product)
    rng = np.random.default_rng(76)
    noise = rng.random((3, 3, 3))
    print("random cube mean:", noise.mean().round(3))
    return {"matmul_shape": product.shape, "sum": int(product.sum())}


def image_ops() -> None:
    h, w = 200, 300
    y, x = np.mgrid[0:h, 0:w]
    img = np.zeros((h, w, 3))
    img[..., 0] = x / w
    img[..., 2] = y / h
    img[(x - 150) ** 2 + (y - 100) ** 2 < 60 ** 2] = [1.0, 0.8, 0.1]
    grey = img @ np.array([0.2126, 0.7152, 0.0722])  # luminance via matrix multiplication
    OUT.mkdir(exist_ok=True)
    fig, axes = plt.subplots(1, 4, figsize=(14, 3))
    for ax, (title, im, cmap) in zip(axes, [("original", img, None), ("greyscale", grey, "gray"),
                                            ("upside down", np.flip(grey), "gray"), ("inverted", 1 - img, None)]):
        ax.imshow(im, cmap=cmap)
        ax.set_title(title)
        ax.axis("off")
    fig.savefig(OUT / "image_ops.png", dpi=90)
    plt.close(fig)
    print("saved output/image_ops.png; image array shape", img.shape)


if __name__ == "__main__":
    basics()
    image_ops()
