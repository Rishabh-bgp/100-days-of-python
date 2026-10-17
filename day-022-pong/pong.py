from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self) -> None:
        if self.ycor() < 240:
            self.sety(self.ycor() + 20)

    def go_down(self) -> None:
        if self.ycor() > -240:
            self.sety(self.ycor() - 20)


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.dx = self.dy = 10
        self.move_speed = 0.1

    def move(self) -> None:
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_y(self) -> None:
        self.dy *= -1

    def bounce_x(self) -> None:
        self.dx *= -1
        self.move_speed *= 0.9

    def reset_position(self) -> None:
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = self.r_score = 0
        self.draw()

    def draw(self) -> None:
        self.clear()
        for x, s in ((-100, self.l_score), (100, self.r_score)):
            self.goto(x, 200)
            self.write(s, align="center", font=("Courier", 60, "normal"))

    def l_point(self) -> None:
        self.l_score += 1
        self.draw()

    def r_point(self) -> None:
        self.r_score += 1
        self.draw()
