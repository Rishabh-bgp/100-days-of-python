"""Snake class: segments, movement, turning without reversing."""
from turtle import Turtle

START = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    def __init__(self) -> None:
        self.segments: list[Turtle] = []
        for pos in START:
            self.add_segment(pos)
        self.head = self.segments[0]

    def add_segment(self, position) -> None:
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.segments.append(seg)

    def extend(self) -> None:
        self.add_segment(self.segments[-1].position())

    def move(self) -> None:
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.head.forward(STEP)

    def _turn(self, heading: int, opposite: int) -> None:
        if self.head.heading() != opposite:
            self.head.setheading(heading)

    def up(self) -> None:
        self._turn(UP, DOWN)

    def down(self) -> None:
        self._turn(DOWN, UP)

    def left(self) -> None:
        self._turn(LEFT, RIGHT)

    def right(self) -> None:
        self._turn(RIGHT, LEFT)

    def reset(self) -> None:
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        for pos in START:
            self.add_segment(pos)
        self.head = self.segments[0]
