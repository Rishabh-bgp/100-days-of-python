from turtle import Turtle

COLOURS = ["#e63946", "#f4a261", "#e9c46a", "#2a9d8f", "#457b9d"]


class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.penup()
        self.goto(0, -260)

    def left(self) -> None:
        self.setx(max(-330, self.xcor() - 40))

    def right(self) -> None:
        self.setx(min(330, self.xcor() + 40))


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.dx, self.dy = 6, 6

    def move(self) -> None:
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def reset_ball(self) -> None:
        self.goto(0, -100)
        self.dy = abs(self.dy)


def make_bricks() -> list[Turtle]:
    bricks = []
    for row, colour in enumerate(COLOURS):
        for col in range(10):
            b = Turtle("square")
            b.shapesize(stretch_wid=1, stretch_len=3.2)
            b.color(colour)
            b.penup()
            b.goto(-342 + col * 76, 230 - row * 28)
            bricks.append(b)
    return bricks
