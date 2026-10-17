"""Day 94 - Portfolio project: Space Invaders with turtle. Left/Right to move, Space to
shoot. Clear the fleet before it reaches you; alien shots cost a life (3 lives).
"""
import random
import time
from turtle import Screen, Turtle

from invaders import Bullet, Fleet, Ship


def main(max_frames: int | None = None, autoplay: bool = False) -> int:
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Space Invaders")
    screen.tracer(0)
    ship, fleet = Ship(), Fleet()
    shots: list[Bullet] = []
    bombs: list[Bullet] = []
    hud = Turtle()
    hud.hideturtle()
    hud.color("white")
    hud.penup()
    state = {"score": 0, "lives": 3, "cooldown": 0}

    def fire() -> None:
        if state["cooldown"] <= 0:
            shots.append(Bullet(ship.xcor(), ship.ycor() + 15, 12, "white"))
            state["cooldown"] = 8

    screen.listen()
    screen.onkey(ship.left, "Left")
    screen.onkey(ship.right, "Right")
    screen.onkey(fire, "space")
    frames = 0
    while state["lives"] and fleet.aliens and (max_frames is None or frames < max_frames):
        frames += 1
        state["cooldown"] -= 1
        if autoplay:
            fire()
        fleet.move()
        if random.random() < 0.03 and (shooter := fleet.random_shooter()):
            bombs.append(Bullet(shooter.xcor(), shooter.ycor() - 15, -7, "red"))
        for b in shots[:]:
            b.move()
            hit = next((a for a in fleet.aliens if a.distance(b) < 20), None)
            if hit or b.ycor() > 300:
                b.hideturtle()
                shots.remove(b)
            if hit:
                hit.hideturtle()
                fleet.aliens.remove(hit)
                state["score"] += 10
        for b in bombs[:]:
            b.move()
            if b.distance(ship) < 18:
                state["lives"] -= 1
            if b.distance(ship) < 18 or b.ycor() < -300:
                b.hideturtle()
                bombs.remove(b)
        if any(a.ycor() < -220 for a in fleet.aliens):
            state["lives"] = 0
        hud.clear()
        hud.goto(-380, 270)
        hud.write(f"Score {state['score']}   Lives {state['lives']}", font=("Courier", 16, "normal"))
        screen.update()
        time.sleep(0.016)
    hud.goto(0, 0)
    hud.write("YOU WIN!" if not fleet.aliens else ("GAME OVER" if not state["lives"] else ""), align="center",
              font=("Courier", 30, "bold"))
    if max_frames is None:
        screen.exitonclick()
    return state["score"]


if __name__ == "__main__":
    main()
