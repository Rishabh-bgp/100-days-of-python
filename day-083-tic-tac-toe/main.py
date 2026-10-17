"""Day 83 - Portfolio project: command-line Tic Tac Toe for two players, or against an
unbeatable computer (minimax).

Enter moves as 1-9:
 1 | 2 | 3
 4 | 5 | 6
 7 | 8 | 9
"""
LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def winner(board: list[str]) -> str | None:
    for a, b, c in LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return "draw" if " " not in board else None


def show(board: list[str]) -> str:
    rows = [" | ".join(board[i:i + 3]) for i in (0, 3, 6)]
    return "\n---------\n".join(f" {r}" for r in rows)


def minimax(board: list[str], player: str) -> tuple[int, int | None]:
    result = winner(board)
    if result == "O":
        return 1, None
    if result == "X":
        return -1, None
    if result == "draw":
        return 0, None
    best = (-2, None) if player == "O" else (2, None)
    for i in [i for i, v in enumerate(board) if v == " "]:
        board[i] = player
        score, _ = minimax(board, "X" if player == "O" else "O")
        board[i] = " "
        if (player == "O" and score > best[0]) or (player == "X" and score < best[0]):
            best = (score, i)
    return best


def play(ask=input, vs_computer: bool | None = None) -> str:
    board = [" "] * 9
    if vs_computer is None:
        vs_computer = ask("Play against the computer? (y/n): ").strip().lower() == "y"
    player = "X"
    while (result := winner(board)) is None:
        print(show(board))
        if vs_computer and player == "O":
            _, move = minimax(board, "O")
            print(f"Computer plays {move + 1}")
        else:
            raw = ask(f"Player {player}, choose a square 1-9: ").strip()
            if not raw.isdigit() or not 1 <= int(raw) <= 9 or board[int(raw) - 1] != " ":
                print("Invalid move, try again.")
                continue
            move = int(raw) - 1
        board[move] = player
        player = "O" if player == "X" else "X"
    print(show(board))
    print("It's a draw!" if result == "draw" else f"{result} wins!")
    return result


if __name__ == "__main__":
    try:
        play()
    except EOFError:
        print("\nBye!")
