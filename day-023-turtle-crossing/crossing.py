import random
from turtle import Turtle

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
START_SPEED, SPEED_STEP = 5, 10
FINISH_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self) -> None:
        self.forward(10)

    def go_to_start(self) -> None:
        self.goto(0, -280)

    def at_finish(self) -> bool:
        return self.ycor() > FINISH_Y


class CarManager:
    def __init__(self) -> None:
        self.cars: list[Turtle] = []
        self.speed = START_SPEED

    def create_car(self) -> None:
        if random.randint(1, 6) == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLOURS))
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def move_cars(self) -> None:
        for car in self.cars:
            car.backward(self.speed)

    def level_up(self) -> None:
        self.speed += SPEED_STEP


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.draw()

    def draw(self) -> None:
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=("Courier", 24, "normal"))

    def increase_level(self) -> None:
        self.level += 1
        self.draw()

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
