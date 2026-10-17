"""Day 21 - Snake part 2: inheritance (Food, Scoreboard), collisions, slicing."""
import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake


def main(max_frames: int | None = None) -> None:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)
    snake, food, board = Snake(), Food(), Scoreboard()
    screen.listen()
    for key, fn in {"Up": snake.up, "Down": snake.down, "Left": snake.left, "Right": snake.right}.items():
        screen.onkey(fn, key)
    frames = 0
    while max_frames is None or frames < max_frames:
        frames += 1
        screen.update()
        time.sleep(0.1)
        snake.move()
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            board.increase()
        hit_wall = abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290
        hit_tail = any(snake.head.distance(seg) < 10 for seg in snake.segments[1:])
        if hit_wall or hit_tail:
            board.reset()
            snake.reset()


if __name__ == "__main__":
    main()
