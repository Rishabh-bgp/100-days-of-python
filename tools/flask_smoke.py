"""Import ./app.py, start Flask's test client and GET each route given on the command line.

Uses an in-memory SQLite database so nothing is written. Also checks that any locally
served Bootstrap CSS link on the page loads. Exit code 1 on any status >= 400.
Usage (inside a day folder):  python ../tools/flask_smoke.py / /about
"""
import os
import re
import sys

os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")
sys.path.insert(0, os.getcwd())
from app import app  # noqa: E402

app.config.update(TESTING=True, WTF_CSRF_ENABLED=False)
client = app.test_client()
failed = False
for route in sys.argv[1:] or ["/"]:
    r = client.get(route)
    ok = r.status_code < 400
    failed |= not ok
    extra = ""
    m = re.search(rb'href="(/bootstrap/static/[^"]+\.css)"', r.data)
    if m:
        css = client.get(m.group(1).decode())
        extra = f" (local bootstrap css {css.status_code})"
        failed |= css.status_code != 200
    print(f"GET {route} -> {r.status_code}{extra}")
sys.exit(1 if failed else 0)
