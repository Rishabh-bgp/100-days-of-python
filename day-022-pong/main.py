"""Day 22 - Pong: two-player arcade game with classes and collision detection."""
import time
from turtle import Screen

from pong import Ball, Paddle, Scoreboard


def main(max_frames: int | None = None) -> None:
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)
    right, left, ball, board = Paddle((350, 0)), Paddle((-350, 0)), Ball(), Scoreboard()
    screen.listen()
    screen.onkey(right.go_up, "Up")
    screen.onkey(right.go_down, "Down")
    screen.onkey(left.go_up, "w")
    screen.onkey(left.go_down, "s")
    frames = 0
    while max_frames is None or frames < max_frames:
        frames += 1
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        if abs(ball.ycor()) > 280:
            ball.bounce_y()
        if (ball.distance(right) < 50 and ball.xcor() > 320) or (ball.distance(left) < 50 and ball.xcor() < -320):
            ball.bounce_x()
        if ball.xcor() > 380:
            ball.reset_position()
            board.l_point()
        if ball.xcor() < -380:
            ball.reset_position()
            board.r_point()


if __name__ == "__main__":
    main()
