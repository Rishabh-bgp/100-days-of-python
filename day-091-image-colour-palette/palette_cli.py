"""Print the palette of an image from the command line. With no argument, uses a generated sample."""
import sys
from pathlib import Path

from palette import demo_image, top_colours

if __name__ == "__main__":
    out = Path(__file__).with_name("output")
    out.mkdir(exist_ok=True)
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else demo_image(out / "sample.png")
    for hex_code, share in top_colours(path, n=int(sys.argv[2]) if len(sys.argv) > 2 else 5):
        print(f"{hex_code}  {share:.1%}")
