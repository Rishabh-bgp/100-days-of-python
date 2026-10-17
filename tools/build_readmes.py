"""Generate each day's README.md and the top-level README table from tools/days.py.

Usage: python tools/build_readmes.py
Status per day lives in tools/status.json ("done", "partial" or "pending").
"""
import ast
import json
from pathlib import Path

from days import DAYS, GUI, SEL, folder

ROOT = Path(__file__).resolve().parent.parent
STATUS = json.loads((ROOT / "tools" / "status.json").read_text())
EXTRA_NOTES = json.loads((ROOT / "tools" / "notes.json").read_text()) if (ROOT / "tools" / "notes.json").exists() else {}
BADGE = {"done": "✅ done", "partial": "🟡 partial", "pending": "⏳ pending"}


def run_lines(path: Path) -> list[str]:
    lines = []
    scripts = sorted(p.name for p in path.glob("*.py") if p.name not in {"local_server.py", "browser.py"})
    is_flask = any("Flask(__name__)" in (path / s).read_text(encoding="utf-8") for s in scripts) if scripts else False
    if (path / "requirements.txt").exists():
        lines.append("pip install -r requirements.txt")
    if "main.py" in scripts:
        lines.append("python main.py")
    if "app.py" in scripts:
        lines.append("flask --app app run      # then open http://127.0.0.1:5000")
    for s in scripts:
        if s not in {"main.py", "app.py"} and s in {"exercises.py", "etch_a_sketch.py", "monday_motivation.py", "quote_app.py", "analysis.py"}:
            lines.append(f"python {s}")
    if not scripts and (path / "index.html").exists():
        lines.append("# open index.html in your browser, or serve the folder:")
        lines.append("python -m http.server 8000")
    _ = is_flask
    return lines


def description(path: Path) -> str:
    for name in ("main.py", "app.py", "analysis.py", "exercises.py"):
        f = path / name
        if f.exists():
            doc = ast.get_docstring(ast.parse(f.read_text(encoding="utf-8")))
            if doc:
                return doc.strip()
    return ""


def day_readme(day: int) -> str:
    slug, title, topic, concepts, notes = DAYS[day]
    path = ROOT / folder(day)
    files = sorted(p.name for p in path.iterdir() if p.is_file() and p.name != "README.md")
    parts = [f"# Day {day}: {title}", ""]
    desc = description(path)
    if desc:
        parts += [desc, ""]
    parts += [f"**Topic:** {topic}", "", f"**Concepts:** {concepts}", ""]
    extra = EXTRA_NOTES.get(str(day))
    if notes or extra:
        parts += ["## Notes", ""]
        for n in (notes, extra):
            if n:
                parts.append(n.replace(GUI, "").replace(SEL, "").strip())
        if GUI in notes:
            parts.append("\nThis project opens a window (tkinter/turtle), so it needs a desktop session. "
                         "On Linux you may need `sudo apt install python3-tk`.")
        if SEL in notes:
            parts.append("\nThis is a Selenium bot. It needs Google Chrome installed (Selenium Manager fetches the "
                         "matching driver automatically). It starts a bundled local mock site on 127.0.0.1 and only "
                         "talks to that, so no real account or website is involved. Set `HEADLESS=0` to watch it.")
        parts.append("")
    parts += ["## Files", ""] + [f"- `{f}`" for f in files] + ["", "## Run", "", "```bash"] + run_lines(path) + ["```", ""]
    if STATUS.get(str(day)) == "partial" and str(day) in EXTRA_NOTES:
        parts += ["**Status:** partial - see notes above.", ""]
    parts += ["---", "Independent solution written for this repo; not course material. "
              "See the [top-level README](../README.md)."]
    return "\n".join(parts) + "\n"


def top_readme() -> str:
    done = sum(1 for d in DAYS if STATUS.get(str(d)) == "done")
    partial = sum(1 for d in DAYS if STATUS.get(str(d)) == "partial")
    rows = []
    for d, (slug, title, topic, _c, notes) in DAYS.items():
        st = STATUS.get(str(d), "pending")
        name = f"[{title}]({folder(d)}/)" if st != "pending" else title
        mod = notes.replace(GUI, "GUI.").replace(SEL, "Selenium (local mock).").replace("|", "/")
        rows.append(f"| {d} | {name} | {topic} | {BADGE[st]} | {mod} |")
    head = (ROOT / "tools" / "README_HEAD.md").read_text(encoding="utf-8")
    head = head.replace("{{DONE}}", str(done)).replace("{{PARTIAL}}", str(partial)).replace(
        "{{PENDING}}", str(100 - done - partial))
    table = ["| Day | Project | Topic | Status | Modernised / replaced |", "|---:|---|---|---|---|"] + rows
    tail = (ROOT / "tools" / "README_TAIL.md").read_text(encoding="utf-8")
    return head + "\n" + "\n".join(table) + "\n\n" + tail


if __name__ == "__main__":
    for d in DAYS:
        p = ROOT / folder(d)
        if STATUS.get(str(d), "pending") != "pending" and p.is_dir():
            (p / "README.md").write_text(day_readme(d), encoding="utf-8")
    (ROOT / "README.md").write_text(top_readme(), encoding="utf-8")
    print("READMEs written")
