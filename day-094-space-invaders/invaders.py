import random
from turtle import Turtle


class Ship(Turtle):
    def __init__(self) -> None:
        super().__init__("triangle")
        self.color("lime")
        self.penup()
        self.setheading(90)
        self.goto(0, -250)

    def left(self) -> None:
        self.setx(max(-360, self.xcor() - 20))

    def right(self) -> None:
        self.setx(min(360, self.xcor() + 20))


class Bullet(Turtle):
    def __init__(self, x: float, y: float, dy: float, colour: str) -> None:
        super().__init__("square")
        self.shapesize(0.5, 0.15)
        self.color(colour)
        self.penup()
        self.goto(x, y)
        self.dy = dy

    def move(self) -> None:
        self.sety(self.ycor() + self.dy)


class Fleet:
    def __init__(self, rows: int = 4, cols: int = 9) -> None:
        self.aliens: list[Turtle] = []
        self.dx = 2.0
        for r in range(rows):
            for c in range(cols):
                a = Turtle("circle")
                a.color(["#ff595e", "#ffca3a", "#8ac926", "#1982c4"][r % 4])
                a.shapesize(1.1, 1.4)
                a.penup()
                a.goto(-280 + c * 70, 220 - r * 45)
                self.aliens.append(a)

    def move(self) -> None:
        xs = [a.xcor() for a in self.aliens]
        if xs and (max(xs) > 360 or min(xs) < -360):
            self.dx *= -1.05
            for a in self.aliens:
                a.sety(a.ycor() - 15)
        for a in self.aliens:
            a.setx(a.xcor() + self.dx)

    def random_shooter(self) -> Turtle | None:
        return random.choice(self.aliens) if self.aliens else None
