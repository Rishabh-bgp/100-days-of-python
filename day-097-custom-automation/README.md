# Day 97: Custom Automation

Day 97 - Portfolio project: custom automation. A 'Downloads folder tidier' that sorts
files into category folders by extension, renames duplicates safely, can undo the last
run from a log, and can run on a schedule.

  python main.py --demo                  # build a messy sample folder and tidy it (safe)
  python main.py PATH --dry-run          # show what would move
  python main.py PATH                    # tidy for real (writes .tidy_log.json)
  python main.py PATH --undo             # put everything back
  python main.py PATH --every 3600       # repeat every hour (Ctrl+C to stop)

**Topic:** Portfolio

**Concepts:** file organiser, dry-run, undo log, scheduling

## Notes

Works on a temporary demo folder by default; always try --dry-run before pointing it at a real folder.

## Files

- `main.py`

## Run

```bash
python main.py
```

---
Independent solution written for this repo; not course material. See the [top-level README](../README.md).
