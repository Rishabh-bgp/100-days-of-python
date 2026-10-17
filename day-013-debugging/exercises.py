"""Day 13 - Debugging: each function was written with a classic bug; the comment says what was wrong."""
import random


def my_function() -> list[int]:
    # BUG was: range(1, 20) never reaches 20, so the 'You got it' branch never ran.
    return [i for i in range(1, 21) if i == 20]


def pick_dice(rng=random) -> int:
    dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
    # BUG was: randint(1, 6) gives index 6 -> IndexError; indexes are 0..5.
    return dice_imgs.index(dice_imgs[rng.randint(0, 5)]) + 1


def generation(year: int) -> str:
    # BUG was: years exactly 1994 fell through both > and < checks.
    if 1980 < year <= 1994:
        return "You are a millennial."
    if year > 1994:
        return "You are a Gen Z."
    return "Earlier generation."


def can_drive(age_text: str) -> str:
    # BUG was: input() returns a str, comparing it to 18 raised TypeError; and the f-string was missing the 'f'.
    age = int(age_text)
    return f"You can drive at age {age}." if age >= 18 else "Not yet."


def word_pages(pages: int, words_per_page: int) -> int:
    # BUG was: '==' used instead of '=' so the variable was never assigned.
    total = pages * words_per_page
    return total


def mutate(a_list: list[int]) -> list[int]:
    # BUG was: 'b_list.append(new_item)' sat outside the for loop (indentation), so only the last item was added.
    b_list = []
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = max(new_item, 0)
        b_list.append(new_item)
    return b_list


def odd_or_even(n: int) -> str:
    # BUG was: 'if n % 2 = 0' (assignment instead of comparison) - a SyntaxError.
    return "even" if n % 2 == 0 else "odd"


def fizz_buzz(n: int) -> str:
    # BUG was: 'or' instead of 'and' for the FizzBuzz check, and 'if' instead of 'elif' chains printing twice.
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


if __name__ == "__main__":
    print(my_function())
    print("dice:", pick_dice(random.Random(0)))
    print(generation(1994))
    print(can_drive("19"))
    print(word_pages(3, 250))
    print(mutate([1, 2, 3, 5, 8, 13]))
    print(odd_or_even(10), [fizz_buzz(i) for i in range(1, 16)])
