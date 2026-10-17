import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("tomato")
        self.speed("fastest")
        self.refresh()

    def refresh(self) -> None:
        self.goto(random.randint(-14, 14) * 20, random.randint(-14, 14) * 20)
