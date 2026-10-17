"""Day 33 - ISS Overhead Notifier: "API" logic, datetimes, and a notification when the ISS
is overhead and it's dark.

API-free: ISS position and sunrise/sunset are computed offline in astro.py
(replacing the Open Notify and sunrise-sunset.org APIs); the alert is printed/written
to outbox.txt instead of emailed.
"""
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

from astro import is_dark, is_overhead, iss_position, sun_times

MY_LAT, MY_LON = 23.2599, 77.4126  # Bhopal
OUTBOX = Path(__file__).with_name("outbox.txt")


def notify(message: str) -> None:
    print(f"[ALERT] {message}")
    with open(OUTBOX, "a", encoding="utf-8") as fh:
        fh.write(f"{datetime.now().isoformat(timespec='seconds')} {message}\n")


def scan(start: datetime, hours: int = 24, step_min: int = 1) -> list[datetime]:
    """Find model times in the window when the ISS is overhead at night."""
    hits = []
    t = start
    while t < start + timedelta(hours=hours):
        if is_overhead(MY_LAT, MY_LON, t) and is_dark(MY_LAT, MY_LON, t):
            hits.append(t)
        t += timedelta(minutes=step_min)
    return hits


def main() -> None:
    now = datetime.now(timezone.utc)
    lat, lon = iss_position(now)
    sunrise, sunset = sun_times(MY_LAT, MY_LON, now)
    print(f"Model ISS position now: lat {lat}, lon {lon}")
    print(f"Sunrise {sunrise:%H:%M} UTC, sunset {sunset:%H:%M} UTC at ({MY_LAT}, {MY_LON})")
    hits = scan(now, hours=int(sys.argv[1]) if len(sys.argv) > 1 else 24)
    if hits:
        notify(f"Look up! The (model) ISS passes overhead around {hits[0]:%Y-%m-%d %H:%M} UTC.")
    else:
        print("No overhead night-time pass in the window.")


if __name__ == "__main__":
    main()
