"""Day 36 - Stock Trading News Alert: compare yesterday vs the day before; if the move is
over 5%, send the top 3 news headlines.

API-free / account-free: replaces Alpha Vantage (prices), NewsAPI (news) and Twilio (SMS)
with bundled sample_daily_prices.csv, sample_news.json (fictional company) and a local outbox.
"""
import csv
import json
from pathlib import Path

from outbox import send_email

HERE = Path(__file__).parent
STOCK, COMPANY = "FICT", "Fictional Motors"
THRESHOLD = 5.0


def last_two_closes(path: Path = HERE / "sample_daily_prices.csv") -> tuple[float, float]:
    with open(path, newline="") as fh:
        rows = list(csv.DictReader(fh))
    return float(rows[-1]["close"]), float(rows[-2]["close"])


def percent_change(yesterday: float, before: float) -> float:
    return round((yesterday - before) / before * 100, 2)


def headlines(n: int = 3) -> list[dict]:
    return json.loads((HERE / "sample_news.json").read_text())["articles"][:n]


def main() -> float:
    y, b = last_two_closes()
    diff = percent_change(y, b)
    arrow = "🔺" if diff > 0 else "🔻"
    print(f"{STOCK}: {b} -> {y} ({diff:+.2f}%)")
    if abs(diff) >= THRESHOLD:
        for art in headlines():
            send_email("+91-00000-00000@sms.local", f"{STOCK}: {arrow}{abs(diff)}%",
                       f"Headline: {art['title']}\nBrief: {art['description']}")
    else:
        print(f"Move under {THRESHOLD}% - no alert.")
    return diff


if __name__ == "__main__":
    main()
