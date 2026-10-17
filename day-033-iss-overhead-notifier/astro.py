"""Offline astronomy: approximate sunrise/sunset (NOAA algorithm) and a simple ISS orbit model.

API-free replacement for the sunrise-sunset.org and Open Notify ISS APIs.
The ISS model is a circular orbit (inclination 51.64 deg, period ~92.9 min) with
J2 nodal regression - good enough to teach the logic, NOT for real sightings.
"""
import math
from datetime import datetime, timedelta, timezone

ISS_INCLINATION = math.radians(51.64)
ISS_PERIOD_MIN = 92.9
NODE_DRIFT_DEG_PER_DAY = -5.0      # J2 nodal regression for the ISS orbit
EARTH_ROT_DEG_PER_MIN = 360 / 1436.07  # sidereal rotation
EPOCH = datetime(2026, 1, 1, tzinfo=timezone.utc)
EPOCH_RAAN_DEG = 0.0  # illustrative starting value


def iss_position(when: datetime) -> tuple[float, float]:
    """Return (latitude, longitude) in degrees for the model ISS at a UTC datetime."""
    minutes = (when - EPOCH).total_seconds() / 60
    u = 2 * math.pi * (minutes % ISS_PERIOD_MIN) / ISS_PERIOD_MIN  # argument of latitude
    lat = math.asin(math.sin(ISS_INCLINATION) * math.sin(u))
    lon_in_plane = math.atan2(math.cos(ISS_INCLINATION) * math.sin(u), math.cos(u))
    raan = EPOCH_RAAN_DEG + NODE_DRIFT_DEG_PER_DAY * minutes / 1440
    lon = math.degrees(lon_in_plane) + raan - EARTH_ROT_DEG_PER_MIN * minutes
    lon = (lon + 180) % 360 - 180
    return round(math.degrees(lat), 4), round(lon, 4)


def sun_times(lat: float, lon: float, day: datetime) -> tuple[datetime, datetime]:
    """Approximate sunrise and sunset in UTC (NOAA general solar position formulas)."""
    n = day.timetuple().tm_yday
    gamma = 2 * math.pi / 365 * (n - 1)
    eqtime = 229.18 * (0.000075 + 0.001868 * math.cos(gamma) - 0.032077 * math.sin(gamma)
                       - 0.014615 * math.cos(2 * gamma) - 0.040849 * math.sin(2 * gamma))
    decl = (0.006918 - 0.399912 * math.cos(gamma) + 0.070257 * math.sin(gamma)
            - 0.006758 * math.cos(2 * gamma) + 0.000907 * math.sin(2 * gamma)
            - 0.002697 * math.cos(3 * gamma) + 0.00148 * math.sin(3 * gamma))
    phi = math.radians(lat)
    cos_ha = math.cos(math.radians(90.833)) / (math.cos(phi) * math.cos(decl)) - math.tan(phi) * math.tan(decl)
    cos_ha = max(-1.0, min(1.0, cos_ha))  # clamp for polar day/night
    ha = math.degrees(math.acos(cos_ha))
    midnight = datetime(day.year, day.month, day.day, tzinfo=timezone.utc)
    sunrise = midnight + timedelta(minutes=720 - 4 * (lon + ha) - eqtime)
    sunset = midnight + timedelta(minutes=720 - 4 * (lon - ha) - eqtime)
    return sunrise, sunset


def is_dark(lat: float, lon: float, when: datetime) -> bool:
    sunrise, sunset = sun_times(lat, lon, when)
    return not (sunrise <= when <= sunset)


def is_overhead(my_lat: float, my_lon: float, when: datetime, margin: float = 5) -> bool:
    lat, lon = iss_position(when)
    return abs(lat - my_lat) <= margin and abs(lon - my_lon) <= margin
