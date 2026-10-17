"""Day 16 exercise: printing a table with a class (stdlib stand-in for the prettytable demo)."""


class Table:
    def __init__(self) -> None:
        self.columns: list[tuple[str, list[str]]] = []

    def add_column(self, name: str, values: list[str]) -> None:
        self.columns.append((name, values))

    def __str__(self) -> str:
        widths = [max(len(n), *(len(v) for v in vals)) for n, vals in self.columns]
        sep = "+" + "+".join("-" * (w + 2) for w in widths) + "+"
        rows = [sep, "| " + " | ".join(n.ljust(w) for (n, _), w in zip(self.columns, widths)) + " |", sep]
        for i in range(len(self.columns[0][1])):
            rows.append("| " + " | ".join(vals[i].ljust(w) for (_, vals), w in zip(self.columns, widths)) + " |")
        rows.append(sep)
        return "\n".join(rows)


if __name__ == "__main__":
    t = Table()
    t.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
    t.add_column("Type", ["Electric", "Water", "Fire"])
    print(t)
