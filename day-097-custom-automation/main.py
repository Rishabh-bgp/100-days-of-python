"""Day 97 - Portfolio project: custom automation. A 'Downloads folder tidier' that sorts
files into category folders by extension, renames duplicates safely, can undo the last
run from a log, and can run on a schedule.

  python main.py --demo                  # build a messy sample folder and tidy it (safe)
  python main.py PATH --dry-run          # show what would move
  python main.py PATH                    # tidy for real (writes .tidy_log.json)
  python main.py PATH --undo             # put everything back
  python main.py PATH --every 3600       # repeat every hour (Ctrl+C to stop)
"""
import argparse
import json
import shutil
import tempfile
import time
from pathlib import Path

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".heic"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".odt", ".rtf", ".pptx", ".xlsx", ".csv"},
    "Audio": {".mp3", ".wav", ".flac", ".m4a", ".ogg"},
    "Video": {".mp4", ".mov", ".mkv", ".avi", ".webm"},
    "Archives": {".zip", ".tar", ".gz", ".rar", ".7z"},
    "Code": {".py", ".js", ".html", ".css", ".json", ".ipynb", ".sh"},
    "Installers": {".exe", ".msi", ".dmg", ".deb", ".pkg", ".apk"},
}
LOG_NAME = ".tidy_log.json"


def category_for(path: Path) -> str:
    ext = path.suffix.lower()
    return next((cat for cat, exts in CATEGORIES.items() if ext in exts), "Other")


def unique_target(target: Path) -> Path:
    n = 1
    candidate = target
    while candidate.exists():
        candidate = target.with_name(f"{target.stem} ({n}){target.suffix}")
        n += 1
    return candidate


def tidy(folder: Path, dry_run: bool = False) -> list[tuple[str, str]]:
    moves = []
    for item in sorted(folder.iterdir()):
        if item.is_dir() or item.name.startswith("."):
            continue
        dest = unique_target(folder / category_for(item) / item.name)
        moves.append((str(item), str(dest)))
        if not dry_run:
            dest.parent.mkdir(exist_ok=True)
            shutil.move(str(item), dest)
    if not dry_run and moves:
        (folder / LOG_NAME).write_text(json.dumps(moves, indent=1))
    for src, dst in moves:
        print(f"{'[dry run] ' if dry_run else ''}{Path(src).name} -> {Path(dst).parent.name}/{Path(dst).name}")
    print(f"{len(moves)} file(s) {'would be ' if dry_run else ''}moved.")
    return moves


def undo(folder: Path) -> int:
    log = folder / LOG_NAME
    if not log.exists():
        print("Nothing to undo.")
        return 0
    moves = json.loads(log.read_text())
    for src, dst in reversed(moves):
        if Path(dst).exists():
            shutil.move(dst, unique_target(Path(src)))
    for cat in list(CATEGORIES) + ["Other"]:
        d = folder / cat
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()
    log.unlink()
    print(f"Restored {len(moves)} file(s).")
    return len(moves)


def demo() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        for name in ["holiday.jpg", "report.pdf", "song.mp3", "notes.txt", "setup.exe", "script.py",
                     "archive.zip", "mystery.xyz", "report (copy).pdf"]:
            (folder / name).write_text("sample")
        (folder / "Documents").mkdir()
        (folder / "Documents" / "notes.txt").write_text("existing file with the same name")
        tidy(folder, dry_run=True)
        tidy(folder)
        print("folders now:", sorted(p.name for p in folder.iterdir() if p.is_dir()))
        undo(folder)
        print("after undo:", sorted(p.name for p in folder.iterdir() if p.is_file() and not p.name.startswith(".")))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder", nargs="?", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--undo", action="store_true")
    ap.add_argument("--every", type=int, metavar="SECONDS", help="repeat on a schedule")
    ap.add_argument("--demo", action="store_true")
    args = ap.parse_args()
    if args.demo or not args.folder:
        demo()
        return
    if args.undo:
        undo(args.folder)
        return
    while True:
        tidy(args.folder, args.dry_run)
        if not args.every:
            break
        time.sleep(args.every)


if __name__ == "__main__":
    main()
