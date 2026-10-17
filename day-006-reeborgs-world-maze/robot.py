"""A tiny offline stand-in for Reeborg's World (the course uses the website).

Same idea: a robot on a grid with move(), turn_left(), front_is_clear(),
right_is_clear(), wall_in_front() and at_goal(). Grids are text:
  '#' wall, '.' open, 'G' goal, and one of '^>v<' for the robot.
"""
DIRS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
ORDER = "^>v<"


class Robot:
    def __init__(self, grid: str):
        self.cells = [list(row) for row in grid.strip("\n").splitlines()]
        self.steps = 0
        for r, row in enumerate(self.cells):
            for c, ch in enumerate(row):
                if ch in DIRS:
                    self.pos, self.facing = (r, c), ch
                    row[c] = "."

    def _ahead(self, facing=None):
        dr, dc = DIRS[facing or self.facing]
        return self.pos[0] + dr, self.pos[1] + dc

    def _open(self, cell) -> bool:
        r, c = cell
        if 0 <= r < len(self.cells) and 0 <= c < len(self.cells[r]):
            return self.cells[r][c] != "#"
        return False

    def front_is_clear(self) -> bool:
        return self._open(self._ahead())

    def wall_in_front(self) -> bool:
        return not self.front_is_clear()

    def right_is_clear(self) -> bool:
        right = ORDER[(ORDER.index(self.facing) + 1) % 4]
        return self._open(self._ahead(right))

    def turn_left(self) -> None:
        self.facing = ORDER[(ORDER.index(self.facing) - 1) % 4]

    def move(self) -> None:
        if not self.front_is_clear():
            raise RuntimeError("Ouch! Reeborg hit a wall.")
        self.pos = self._ahead()
        self.steps += 1
        if self.steps > 10_000:
            raise RuntimeError("Too many steps - probably stuck in a loop.")

    def at_goal(self) -> bool:
        r, c = self.pos
        return self.cells[r][c] == "G"
