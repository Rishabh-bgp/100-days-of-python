"""Day 20 - Snake part 1: create the body, move it, control it with the arrow keys."""
import time
from turtle import Screen

from snake import Snake


def main(max_frames: int | None = None) -> None:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake - part 1")
    screen.tracer(0)
    snake = Snake()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    frames = 0
    while max_frames is None or frames < max_frames:
        screen.update()
        time.sleep(0.1)
        snake.move()
        frames += 1


if __name__ == "__main__":
    main()
