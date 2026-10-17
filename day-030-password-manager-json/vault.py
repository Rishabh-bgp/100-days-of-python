"""JSON storage for the password manager, with exception handling."""
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("data.json")


def load(path: Path = DATA_FILE) -> dict:
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("data.json is corrupted; starting with an empty vault.")
        return {}


def add(website: str, email: str, password: str, path: Path = DATA_FILE) -> None:
    data = load(path)
    data[website] = {"email": email, "password": password}
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=4)


def find(website: str, path: Path = DATA_FILE) -> dict | None:
    return load(path).get(website)
