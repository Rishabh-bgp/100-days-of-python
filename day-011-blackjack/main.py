"""Day 11 - Blackjack capstone: functions, lists, while loops, game logic."""
import random

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal(rng=random) -> int:
    return rng.choice(CARDS)


def score(hand: list[int]) -> int:
    """0 means Blackjack; aces drop from 11 to 1 when the hand is bust."""
    if sorted(hand) == [10, 11]:
        return 0
    hand = list(hand)
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    return sum(hand)


def compare(user: int, dealer: int) -> str:
    if user > 21 and dealer > 21:
        return "You went over. You lose 😤"
    if user == dealer:
        return "Draw 🙃"
    if dealer == 0:
        return "Lose, opponent has Blackjack 😱"
    if user == 0:
        return "Win with a Blackjack 😎"
    if user > 21:
        return "You went over. You lose 😭"
    if dealer > 21:
        return "Opponent went over. You win 😁"
    return "You win 😃" if user > dealer else "You lose 😤"


def play_round(ask=input, rng=random) -> str:
    user = [deal(rng), deal(rng)]
    dealer = [deal(rng), deal(rng)]
    while True:
        u = score(user)
        print(f"  Your cards: {user}, current score: {u}")
        print(f"  Dealer's first card: {dealer[0]}")
        if u == 0 or score(dealer) == 0 or u > 21:
            break
        if ask("Type 'y' to get another card, 'n' to pass: ").strip().lower() == "y":
            user.append(deal(rng))
        else:
            break
    while score(dealer) != 0 and score(dealer) < 17:
        dealer.append(deal(rng))
    print(f"  Your final hand: {user}, final score: {score(user)}")
    print(f"  Dealer's final hand: {dealer}, final score: {score(dealer)}")
    result = compare(score(user), score(dealer))
    print(result)
    return result


def main() -> None:
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower() == "y":
        play_round()


if __name__ == "__main__":
    main()
