"""Reads/writes the destinations table (local CSV instead of a Google Sheet via Sheety)."""
import csv
from pathlib import Path

PATH = Path(__file__).with_name("destinations.csv")


def get_destinations(path: Path = PATH) -> list[dict]:
    with open(path, newline="") as fh:
        return [dict(r, lowest_price_inr=int(r["lowest_price_inr"])) for r in csv.DictReader(fh)]
