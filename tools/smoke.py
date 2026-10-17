"""Smoke tests: (day, command, stdin). Commands run inside the day folder with the repo's Python.
'GUI' entries need a display (run verify.py under xvfb-run on headless Linux).
'SEL' entries need Google Chrome."""

CLI = [
    (1, "main.py", "Bhopal\nTiger\n"), (1, "exercises.py", ""),
    (2, "main.py", "150\n12\n5\n"), (2, "exercises.py", ""),
    (3, "main.py", "left\nwait\nyellow\n"), (3, "exercises.py", ""),
    (4, "main.py", "1\n"), (4, "exercises.py", ""),
    (5, "main.py", "8\n2\n3\n"), (5, "exercises.py", ""),
    (6, "main.py", ""), (6, "exercises.py", ""),
    (7, "main.py", "e\na\no\ni\nu\nr\nt\ns\nn\nl\nm\nh\nc\np\ny\ng\n"),
    (8, "main.py", "encode\nHello World\n5\nyes\ndecode\nMjqqt Btwqi\n5\nno\n"), (8, "exercises.py", ""),
    (9, "main.py", "Ana\n120\nyes\nBen\n150\nno\n"), (9, "exercises.py", ""),
    (10, "main.py", "10\n+\n5\ny\n*\n3\nn\n8\n/\n0\n/\n2\nq\n"), (10, "exercises.py", ""),
    (11, "main.py", "y\nn\ny\ny\nn\nn\n"),
    (12, "main.py", "hard\n50\n25\n75\n12\n88\n"), (12, "exercises.py", ""),
    (13, "exercises.py", ""),
    (14, "main.py", "a\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\na\nb\n"),
    (15, "main.py", "latte\n10\n0\n0\n0\nreport\nespresso\n4\n2\n1\n0\nlatte\n10\n0\n0\n0\noff\n"),
    (16, "main.py", "latte\n10\n0\n0\n0\nreport\nmocha\ncappuccino\n1\n0\n0\n0\noff\n"), (16, "exercises.py", ""),
    (17, "main.py", "True\nFalse\nT\nF\ntrue\nfalse\nTrue\nFalse\nTrue\nFalse\nTrue\nFalse\n"),
    (24, "main.py", ""), (24, "exercises.py", ""),
    (25, "exercises.py", ""),
    (25, "-c \"import main; d=main.load_states(); print(main.check_guess(d,'ohio')); print(len(main.missing_states(d,{'Ohio'})))\"", ""),
]

GUI = [
    (18, "-c \"import turtle, main; turtle.tracer(0); main.paint(); turtle.update(); turtle.bye()\"", ""),
    (18, "-c \"import turtle, exercises as e; turtle.tracer(0); turtle.colormode(255); t=turtle.Turtle(); e.square(t); e.dashed_line(t); e.shapes(t); e.random_walk(t,20); e.spirograph(t,30); turtle.bye()\"", ""),
    (19, "-c \"import turtle, main; turtle.tracer(0); main.race('red'); turtle.bye()\"", ""),
    (19, "-c \"import etch_a_sketch as e; e.forwards(); e.turn_left(); e.backwards(); e.clear(); e.screen.bye()\"", ""),
    (20, "-c \"import turtle, main; main.main(max_frames=15); turtle.bye()\"", ""),
    (21, "-c \"import turtle, main; main.main(max_frames=40); turtle.bye()\"", ""),
    (22, "-c \"import turtle, main, pong; pong.Ball.move_speed=0; main.main(max_frames=60); turtle.bye()\"", ""),
    (23, "-c \"import turtle, main; main.main(max_frames=40); turtle.bye()\"", ""),
]

SEL = []
FLASK = []
