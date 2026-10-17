# Contributing

Thanks for your interest! Fixes, clearer code, tests and alternative solutions are all welcome, including during Hacktoberfest.

## Ground rules

1. **No course materials.** Don't add code, starter files, text, images or data copied from the Udemy course or any other paid source. Write your own.
2. **No API keys or accounts.** Every project must run offline with bundled or synthetic data. Use local mocks instead of real sites.
3. **Keep it beginner-friendly.** Prefer readable code and the standard library. If you add a third-party package, pin it in that day's `requirements.txt`.
4. **Python 3.12+**, with modern APIs (Selenium 4 `By` locators, pandas `concat`, Flask 3, SQLAlchemy 2.0 style).

## Workflow

```bash
git clone https://github.com/Rishabh-bgp/100-days-of-python.git
cd 100-days-of-python
python -m venv .venv && source .venv/bin/activate
pip install ruff
# make your change in day-XXX-.../
ruff check --select E9,F .
python tools/verify.py            # add --gui under xvfb-run, --selenium if Chrome is installed
```

- One topic per pull request, with a clear title (for example `day-035: handle empty forecast`).
- If you change a day's metadata, update `tools/days.py` and run `python tools/build_readmes.py`.
- Be kind in reviews and issues.
