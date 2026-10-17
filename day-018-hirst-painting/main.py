"""Day 18 - Hirst-style spot painting with turtle (tuples, modules, aliases).

The course extracts colours from an image with the third-party 'colorgram' package;
this version uses a hand-picked palette so it needs only the standard library.
"""
import random
import turtle as t

PALETTE = [
    (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
    (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
    (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50),
]


def paint(rows: int = 10, cols: int = 10, gap: int = 50, dot: int = 20, rng=random) -> None:
    t.colormode(255)
    pen = t.Turtle()
    pen.speed("fastest")
    pen.hideturtle()
    pen.penup()
    start_x, start_y = -gap * (cols - 1) / 2, -gap * (rows - 1) / 2
    for r in range(rows):
        pen.goto(start_x, start_y + r * gap)
        for _ in range(cols):
            pen.dot(dot, rng.choice(PALETTE))
            pen.forward(gap)


if __name__ == "__main__":
    paint()
    t.Screen().exitonclick()
