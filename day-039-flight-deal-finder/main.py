"""Day 39 - Flight Deal Finder: classes working together (DataManager, FlightSearch,
NotificationManager) to find flights cheaper than your target price.

API-free / account-free: replaces the Google Sheet (Sheety), the flight-search API
(Tequila/Kiwi, now closed; later Amadeus) and Twilio SMS with destinations.csv,
sample_flights.csv (synthetic prices) and a local outbox. The search falls back to
1-stop flights when there's no direct one, as in the course's later version.
"""
from datetime import date, timedelta

from data_manager import get_destinations
from flight_search import FlightSearch
from outbox import send_email

ORIGIN = "DEL"


def find_deals(today: date = date(2026, 11, 1)) -> list:
    search = FlightSearch()
    deals = []
    for dest in get_destinations():
        window = (today + timedelta(days=1), today + timedelta(days=180))
        flight = search.cheapest(ORIGIN, dest["iata"], *window) or search.cheapest(ORIGIN, dest["iata"], *window, max_stops=1)
        if flight is None:
            print(f"{dest['city']}: no flights found")
            continue
        print(f"{dest['city']}: ₹{flight.price:,} (target ₹{dest['lowest_price_inr']:,})")
        if flight.price < dest["lowest_price_inr"]:
            deals.append((dest, flight))
    return deals


def main() -> int:
    deals = find_deals()
    for dest, f in deals:
        stops = "direct" if f.stops == 0 else f"{f.stops} stop"
        send_email("+91-00000-00000@sms.local", f"Low price alert: {dest['city']}",
                   f"Only ₹{f.price:,} to fly {f.origin}->{f.destination} ({stops}), "
                   f"{f.out_date} to {f.return_date} with {f.airline}.")
    print(f"{len(deals)} deal(s) found.")
    return len(deals)


if __name__ == "__main__":
    main()
