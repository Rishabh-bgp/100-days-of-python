"""Day 86 - Portfolio project: Breakout with turtle. Arrow keys move the paddle; clear all
the bricks. You have 3 lives; score shown at the top.
"""
import time
from turtle import Screen, Turtle

from breakout import Ball, Paddle, make_bricks


def main(max_frames: int | None = None) -> int:
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Breakout")
    screen.tracer(0)
    paddle, ball, bricks = Paddle(), Ball(), make_bricks()
    board = Turtle()
    board.hideturtle()
    board.color("white")
    board.penup()
    score, lives, frames = 0, 3, 0
    screen.listen()
    screen.onkey(paddle.left, "Left")
    screen.onkey(paddle.right, "Right")
    while lives and bricks and (max_frames is None or frames < max_frames):
        frames += 1
        board.clear()
        board.goto(0, 265)
        board.write(f"Score: {score}   Lives: {lives}", align="center", font=("Courier", 16, "normal"))
        screen.update()
        time.sleep(0.016)
        ball.move()
        if abs(ball.xcor()) > 380:
            ball.dx *= -1
        if ball.ycor() > 280:
            ball.dy *= -1
        if ball.dy < 0 and -265 < ball.ycor() < -245 and abs(ball.xcor() - paddle.xcor()) < 65:
            ball.dy *= -1
            ball.dx = (ball.xcor() - paddle.xcor()) / 8 or ball.dx
        for brick in bricks:
            if abs(ball.xcor() - brick.xcor()) < 38 and abs(ball.ycor() - brick.ycor()) < 16:
                brick.hideturtle()
                bricks.remove(brick)
                ball.dy *= -1
                score += 10
                break
        if ball.ycor() < -290:
            lives -= 1
            ball.reset_ball()
    board.goto(0, 0)
    board.write("YOU WIN!" if not bricks else ("GAME OVER" if not lives else "Paused"), align="center",
                font=("Courier", 28, "bold"))
    if max_frames is None:
        screen.exitonclick()
    return score


if __name__ == "__main__":
    main()
