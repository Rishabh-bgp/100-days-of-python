"""Local 'flight search' over bundled sample data (stands in for a flight-search API)."""
import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent


@dataclass
class FlightData:
    origin: str
    destination: str
    out_date: date
    return_date: date
    stops: int
    price: int
    airline: str


class FlightSearch:
    def __init__(self, path: Path = HERE / "sample_flights.csv") -> None:
        with open(path, newline="") as fh:
            self.rows = [
                FlightData(r["origin"], r["destination"], date.fromisoformat(r["out_date"]),
                           date.fromisoformat(r["return_date"]), int(r["stops"]), int(r["price_inr"]), r["airline"])
                for r in csv.DictReader(fh)
            ]

    def cheapest(self, origin: str, destination: str, start: date, end: date, max_stops: int = 0) -> FlightData | None:
        options = [f for f in self.rows if f.origin == origin and f.destination == destination
                   and start <= f.out_date <= end and f.stops <= max_stops]
        return min(options, key=lambda f: f.price, default=None)
