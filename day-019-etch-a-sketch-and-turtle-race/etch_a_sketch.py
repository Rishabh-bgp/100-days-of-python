"""Day 19 - Etch-A-Sketch: W/S forwards/backwards, A/D turn, C clears. Functions as arguments."""
import turtle

tim = turtle.Turtle()
screen = turtle.Screen()


def forwards() -> None:
    tim.forward(10)


def backwards() -> None:
    tim.backward(10)


def turn_left() -> None:
    tim.setheading(tim.heading() + 10)


def turn_right() -> None:
    tim.setheading(tim.heading() - 10)


def clear() -> None:
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


if __name__ == "__main__":
    screen.listen()
    for key, fn in {"w": forwards, "s": backwards, "a": turn_left, "d": turn_right, "c": clear}.items():
        screen.onkey(fn, key)
    screen.exitonclick()
