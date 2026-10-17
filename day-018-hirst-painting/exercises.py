"""Day 18 turtle challenges: square, dashed line, shapes, random walk, spirograph."""
import random
import turtle as t


def random_colour(rng=random) -> tuple[int, int, int]:
    return rng.randint(0, 255), rng.randint(0, 255), rng.randint(0, 255)


def square(pen: t.Turtle, size: int = 100) -> None:
    for _ in range(4):
        pen.forward(size)
        pen.right(90)


def dashed_line(pen: t.Turtle, dashes: int = 15) -> None:
    for _ in range(dashes):
        pen.pendown()
        pen.forward(10)
        pen.penup()
        pen.forward(10)
    pen.pendown()


def shapes(pen: t.Turtle) -> None:
    for sides in range(3, 11):
        pen.color(random_colour())
        for _ in range(sides):
            pen.forward(80)
            pen.right(360 / sides)


def random_walk(pen: t.Turtle, steps: int = 100) -> None:
    pen.pensize(8)
    for _ in range(steps):
        pen.color(random_colour())
        pen.setheading(random.choice([0, 90, 180, 270]))
        pen.forward(25)


def spirograph(pen: t.Turtle, gap: int = 6) -> None:
    for _ in range(360 // gap):
        pen.color(random_colour())
        pen.circle(100)
        pen.setheading(pen.heading() + gap)


if __name__ == "__main__":
    t.colormode(255)
    tim = t.Turtle()
    tim.speed("fastest")
    square(tim)
    dashed_line(tim)
    shapes(tim)
    random_walk(tim, 50)
    tim.home()
    spirograph(tim)
    t.Screen().exitonclick()
