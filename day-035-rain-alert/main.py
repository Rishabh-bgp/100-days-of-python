"""Day 35 - Rain Alert: reading JSON "API responses", nested data, and sending an alert.

API-free / account-free: the course calls OpenWeather (API key) and sends SMS via Twilio
(account). Here the forecast is a bundled sample_forecast.json with the same structure as
OpenWeather's 3-hourly forecast, and the "SMS" goes to the console + local outbox/.
"""
import json
import sys
from pathlib import Path

from outbox import send_email

HERE = Path(__file__).parent


def will_rain(forecast: dict, hours: int = 12) -> bool:
    """Weather condition codes below 700 mean rain, drizzle, snow or storms."""
    slots = forecast["list"][: hours // 3]
    return any(w["id"] < 700 for slot in slots for w in slot["weather"])


def main(path: str = "sample_forecast.json") -> bool:
    forecast = json.loads((HERE / path).read_text())
    if will_rain(forecast):
        send_email("+91-00000-00000@sms.local", "Rain alert", "It's going to rain today. Remember to bring an ☔️")
        return True
    print("No rain expected in the next 12 hours.")
    return False


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "sample_forecast.json")
