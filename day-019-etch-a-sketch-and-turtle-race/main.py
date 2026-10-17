"""Day 19 - Turtle Race: multiple instances, event listeners, state."""
import random
import turtle

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]


def race(bet: str | None = None, rng=random) -> str:
    screen = turtle.Screen()
    screen.setup(width=500, height=400)
    if bet is None:
        bet = (screen.textinput("Make your bet", "Which turtle will win the race? Enter a colour: ") or "").lower()
    racers = []
    for i, colour in enumerate(COLOURS):
        r = turtle.Turtle(shape="turtle")
        r.color(colour)
        r.penup()
        r.goto(-230, -100 + i * 40)
        racers.append(r)
    while True:
        for r in racers:
            if r.xcor() > 230:
                winner = r.pencolor()
                print("You've won!" if winner == bet else "You've lost!", f"The {winner} turtle is the winner!")
                return winner
            r.forward(rng.randint(0, 10))


if __name__ == "__main__":
    race()
    turtle.Screen().exitonclick()
