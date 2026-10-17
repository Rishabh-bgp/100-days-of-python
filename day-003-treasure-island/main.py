"""Day 3 - Treasure Island: a choose-your-own-adventure using if/elif/else."""


def play(ask=input, say=print) -> str:
    say("Welcome to Treasure Island. Your mission is to find the treasure.")
    way = ask('You reach a crossroad. Go "left" or "right"? ').strip().lower()
    if way != "left":
        say("You fell into a hole. Game Over.")
        return "lose"
    lake = ask('You reach a lake. "wait" for a boat or "swim" across? ').strip().lower()
    if lake != "wait":
        say("You were attacked by an angry trout. Game Over.")
        return "lose"
    door = ask('You reach an island house with a "red", "yellow" and "blue" door. Which one? ').strip().lower()
    if door == "yellow":
        say("You found the treasure! You Win!")
        return "win"
    if door == "red":
        say("It's a room full of fire. Game Over.")
    elif door == "blue":
        say("You enter a room of beasts. Game Over.")
    else:
        say("That door doesn't exist. Game Over.")
    return "lose"


if __name__ == "__main__":
    play()
