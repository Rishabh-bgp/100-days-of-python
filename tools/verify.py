"""Verify the repo: py_compile everything, ruff for errors, and run smoke tests.

Usage (from the repo root):  python tools/verify.py [--max-day N] [--gui] [--selenium]
On headless Linux run GUI tests with:  xvfb-run -a python tools/verify.py --gui
Writes VERIFICATION.md.
"""
import argparse
import os
import py_compile
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from days import folder  # noqa: E402
import smoke  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def run_case(day: int, cmd: str, stdin: str, timeout: int = 180) -> tuple[bool, str]:
    cwd = ROOT / folder(day)
    env = dict(os.environ, SMOKE_TEST="1", MPLBACKEND="Agg", PYTHONIOENCODING="utf-8")
    full = f'"{sys.executable}" {cmd}'
    try:
        p = subprocess.run(full, shell=True, cwd=cwd, input=stdin, text=True, capture_output=True,
                           timeout=timeout, env=env)
    except subprocess.TimeoutExpired:
        return False, "timeout"
    out = (p.stdout + p.stderr).strip().splitlines()
    return p.returncode == 0, (out[-1] if out else "")[:140]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-day", type=int, default=100)
    ap.add_argument("--gui", action="store_true")
    ap.add_argument("--selenium", action="store_true")
    args = ap.parse_args()
    days = [d for d in range(1, args.max_day + 1) if (ROOT / folder(d)).is_dir()]
    report = ["# Verification report", "", f"Python {sys.version.split()[0]}; days 1-{args.max_day}.", ""]

    files = [p for d in days for p in (ROOT / folder(d)).rglob("*.py")]
    bad = []
    for f in files:
        try:
            py_compile.compile(str(f), doraise=True)
        except py_compile.PyCompileError as e:
            bad.append(f"{f.relative_to(ROOT)}: {e.msg}")
    report += ["## py_compile", "", f"{len(files) - len(bad)}/{len(files)} files compile."] + bad + [""]

    ruff = shutil.which("ruff") or str(Path(sys.executable).with_name("ruff"))
    targets = [str(ROOT / folder(d)) for d in days] + [str(ROOT / "tools")]
    r = subprocess.run([ruff, "check", "--select", "E9,F", "--no-cache", *targets], capture_output=True, text=True,
                       env=dict(os.environ, NO_COLOR="1"))
    ruff_out = (r.stdout + r.stderr).strip() or ("All checks passed!" if r.returncode == 0 else "ruff failed")
    report += ["## ruff (pyflakes rules F + syntax errors E9)", "", "```", ruff_out, "```", ""]

    groups = [("CLI / script smoke tests (piped input)", smoke.CLI), ("Flask test-client checks", smoke.FLASK)]
    if args.gui:
        groups.append(("GUI smoke tests (xvfb)", smoke.GUI))
    if args.selenium:
        groups.append(("Selenium bots vs local mock sites (headless Chrome)", smoke.SEL))
    failures = len(bad) + (r.returncode != 0)
    for title, cases in groups:
        rows = ["| Day | Command | Result | Last output line |", "|---:|---|---|---|"]
        for day, cmd, stdin in cases:
            if day not in days:
                continue
            ok, last = run_case(day, cmd, stdin)
            failures += not ok
            short = cmd if len(cmd) < 60 else cmd[:57] + "..."
            rows.append(f"| {day} | `{short.replace('|', '/')}` | {'pass' if ok else 'FAIL'} | {last.replace('|', '/')} |")
            print(("PASS " if ok else "FAIL ") + f"day {day}: {cmd[:70]} -> {last}")
        report += [f"## {title}", ""] + rows + [""]
    report += [f"**Total failures: {failures}**", ""]
    (ROOT / "VERIFICATION.md").write_text("\n".join(report), encoding="utf-8")
    print(f"failures: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
