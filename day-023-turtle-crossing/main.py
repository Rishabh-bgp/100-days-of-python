"""Day 23 - Turtle Crossing capstone: Frogger-style game built from three classes."""
import time
from turtle import Screen

from crossing import CarManager, Player, Scoreboard


def main(max_frames: int | None = None) -> None:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    player, cars, board = Player(), CarManager(), Scoreboard()
    screen.listen()
    screen.onkey(player.go_up, "Up")
    frames = 0
    while max_frames is None or frames < max_frames:
        frames += 1
        time.sleep(0.1)
        screen.update()
        cars.create_car()
        cars.move_cars()
        if any(car.distance(player) < 20 for car in cars.cars):
            board.game_over()
            break
        if player.at_finish():
            player.go_to_start()
            cars.level_up()
            board.increase_level()
    if max_frames is None:
        screen.exitonclick()


if __name__ == "__main__":
    main()
