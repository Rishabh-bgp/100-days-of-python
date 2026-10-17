"""Day 9 - Secret (blind) Auction: dictionaries and loops."""


def find_winner(bids: dict[str, float]) -> tuple[str, float]:
    name = max(bids, key=bids.get)
    return name, bids[name]


def main() -> None:
    bids: dict[str, float] = {}
    print("Welcome to the secret auction program.")
    while True:
        name = input("What is your name?: ").strip()
        bids[name] = float(input("What's your bid?: $"))
        more = input("Are there any other bidders? Type 'yes' or 'no'.\n> ").strip().lower()
        print("\n" * 40)  # 'clear' the screen so the next bidder can't see
        if more != "yes":
            break
    winner, amount = find_winner(bids)
    print(f"The winner is {winner} with a bid of ${amount:.2f}")


if __name__ == "__main__":
    main()
