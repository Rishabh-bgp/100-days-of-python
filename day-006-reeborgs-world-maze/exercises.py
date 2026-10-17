"""Day 6 exercises: the 'hurdles' challenges, on the offline robot."""
from robot import Robot
from main import turn_right

# Reeborg's "Hurdles 4": walls of different heights with open sky above.
HURDLES = """
#############
#...........#
#...#.......#
#...#...#...#
#.#.#...#.#.#
#>#.#.#.#.#G#
#############
"""


def jump(robot: Robot) -> None:
    """Climb the hurdle, cross over the top of it, then climb down the far side."""
    robot.turn_left()            # face up
    while not robot.right_is_clear():
        robot.move()
    turn_right(robot)            # face along the top of the hurdle
    robot.move()
    while not robot.right_is_clear():   # still standing above the hurdle
        robot.move()
    turn_right(robot)            # face down
    while robot.front_is_clear():
        robot.move()
    robot.turn_left()            # face forward again


def hurdles(robot: Robot) -> int:
    """Hurdles 3/4: walls of unknown height; step forward when clear, jump otherwise."""
    while not robot.at_goal():
        if robot.front_is_clear():
            robot.move()
        else:
            jump(robot)
    return robot.steps


if __name__ == "__main__":
    print("Hurdles finished in", hurdles(Robot(HURDLES)), "moves")
