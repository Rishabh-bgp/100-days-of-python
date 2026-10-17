"""Core watermarking with Pillow: tiled or corner text watermark with transparency."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def add_watermark(src: Path, dst: Path, text: str = "© Rishabh Aryan", opacity: int = 110,
                  tiled: bool = False, scale: float = 0.05) -> Path:
    base = Image.open(src).convert("RGBA")
    layer = Image.new("RGBA", base.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(layer)
    size = max(12, int(min(base.size) * scale))
    try:
        font = ImageFont.load_default(size=size)
    except TypeError:  # very old Pillow
        font = ImageFont.load_default()
    box = draw.textbbox((0, 0), text, font=font)
    tw, th = box[2] - box[0], box[3] - box[1]
    if tiled:
        for y in range(0, base.size[1], th * 4):
            for x in range(-tw, base.size[0], tw + th * 2):
                draw.text((x + (y // (th * 4)) % 2 * tw // 2, y), text, font=font, fill=(255, 255, 255, opacity))
    else:
        margin = size // 2
        pos = (base.size[0] - tw - margin, base.size[1] - th - margin * 2)
        draw.text((pos[0] + 2, pos[1] + 2), text, font=font, fill=(0, 0, 0, opacity))
        draw.text(pos, text, font=font, fill=(255, 255, 255, min(255, opacity + 80)))
    out = Image.alpha_composite(base, layer)
    dst = Path(dst)
    if dst.suffix.lower() in {".jpg", ".jpeg"}:
        out = out.convert("RGB")
    out.save(dst)
    return dst


def demo_image(path: Path, size=(640, 400)) -> Path:
    """Create a gradient sample picture so the demo needs no photo."""
    img = Image.new("RGB", size)
    px = img.load()
    for x in range(size[0]):
        for y in range(size[1]):
            px[x, y] = (x * 255 // size[0], 120, y * 255 // size[1])
    img.save(path)
    return path
