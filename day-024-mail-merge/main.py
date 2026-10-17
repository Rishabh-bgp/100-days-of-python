"""Day 24 - Mail Merge: reading and writing files, pathlib, string replace."""
from pathlib import Path

HERE = Path(__file__).parent
PLACEHOLDER = "[name]"


def merge(names_file: Path, letter_file: Path, out_dir: Path) -> list[Path]:
    template = letter_file.read_text(encoding="utf-8")
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for name in names_file.read_text(encoding="utf-8").splitlines():
        name = name.strip()
        if not name:
            continue
        target = out_dir / f"letter_for_{name}.txt"
        target.write_text(template.replace(PLACEHOLDER, name), encoding="utf-8")
        written.append(target)
    return written


if __name__ == "__main__":
    files = merge(HERE / "Input/Names/invited_names.txt",
                  HERE / "Input/Letters/starting_letter.txt",
                  HERE / "Output/ReadyToSend")
    print(f"Wrote {len(files)} letters to Output/ReadyToSend/")
