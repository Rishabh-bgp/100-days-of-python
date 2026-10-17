"""Day 6 - Escape the maze with functions and while loops (right-hand rule)."""
from robot import Robot

MAZE = """
#########
#>..#...#
#.#.#.#.#
#.#...#.#
#.#####.#
#...#..G#
#########
"""


def turn_right(robot: Robot) -> None:
    for _ in range(3):
        robot.turn_left()


def solve(robot: Robot) -> int:
    while not robot.at_goal():
        if robot.right_is_clear():
            turn_right(robot)
            robot.move()
        elif robot.front_is_clear():
            robot.move()
        else:
            robot.turn_left()
    return robot.steps


if __name__ == "__main__":
    steps = solve(Robot(MAZE))
    print(f"Reeborg reached the goal in {steps} moves!")
