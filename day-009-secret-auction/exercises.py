"""Day 9 exercises: dictionaries and nesting."""


def grade(score: int) -> str:
    if score > 90:
        return "Outstanding"
    if score > 80:
        return "Exceeds Expectations"
    if score > 70:
        return "Acceptable"
    return "Fail"


def grade_all(scores: dict[str, int]) -> dict[str, str]:
    return {name: grade(s) for name, s in scores.items()}


def add_new_country(travel_log: list[dict], country: str, visits: int, cities: list[str]) -> None:
    travel_log.append({"country": country, "visits": visits, "cities": cities})


if __name__ == "__main__":
    print(grade_all({"Harry": 81, "Ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62}))
    log = [{"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]}]
    add_new_country(log, "India", 3, ["Delhi", "Bhopal"])
    print(log)
