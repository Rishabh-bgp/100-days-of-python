"""Day 24 exercises: file modes, relative and absolute paths, a persistent high score."""
import tempfile
from pathlib import Path


def save_high_score(path: Path, score: int) -> int:
    best = int(path.read_text()) if path.exists() else 0
    if score > best:
        path.write_text(str(score))
        best = score
    return best


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / "data.txt"
        with open(f, mode="w") as fh:
            fh.write("New text.")
        with open(f, mode="a") as fh:
            fh.write("\nAppended text.")
        print(f.read_text())
        hs = Path(d) / "high_score.txt"
        print("high score:", save_high_score(hs, 12), save_high_score(hs, 7))
        print("absolute path example:", f.resolve())
