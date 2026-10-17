"""Day 82 - Portfolio project: text-based Morse code converter (encode and decode),
with a command-line interface.

Examples:
  python main.py                      # interactive
  python main.py encode "SOS help"
  python main.py decode "... --- ... / .... . .-.. .--."
"""
import sys

MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--",
    "/": "-..-.", "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.", "-": "-....-", "_": "..--.-", '"': ".-..-.", "$": "...-..-", "@": ".--.-.",
}
REVERSE = {v: k for k, v in MORSE.items()}


def encode(text: str) -> str:
    words = []
    for word in text.upper().split():
        unknown = [c for c in word if c not in MORSE]
        if unknown:
            raise ValueError(f"Can't encode: {''.join(sorted(set(unknown)))}")
        words.append(" ".join(MORSE[c] for c in word))
    return " / ".join(words)


def decode(code: str) -> str:
    try:
        return " ".join("".join(REVERSE[s] for s in word.split()) for word in code.strip().split("/"))
    except KeyError as err:
        raise ValueError(f"Unknown Morse symbol: {err.args[0]}") from None


def main(argv: list[str]) -> None:
    if len(argv) >= 2:
        print(encode(" ".join(argv[1:])) if argv[0] == "encode" else decode(" ".join(argv[1:])))
        return
    while True:
        try:
            mode = input("Type 'e' to encode, 'd' to decode, 'q' to quit: ").strip().lower()
        except EOFError:
            return
        if mode == "q":
            return
        text = input("Text: ")
        try:
            print(encode(text) if mode == "e" else decode(text))
        except ValueError as err:
            print(err)


if __name__ == "__main__":
    main(sys.argv[1:])
