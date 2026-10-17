"""Day 8 - Caesar Cipher: functions with parameters, modulo arithmetic."""
import string

ALPHA = string.ascii_lowercase


def caesar(text: str, shift: int, direction: str = "encode") -> str:
    if direction == "decode":
        shift = -shift
    out = []
    for ch in text:
        lower = ch.lower()
        if lower in ALPHA:
            new = ALPHA[(ALPHA.index(lower) + shift) % 26]
            out.append(new.upper() if ch.isupper() else new)
        else:
            out.append(ch)
    return "".join(out)


def main() -> None:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n> ").strip().lower()
        text = input("Type your message:\n> ")
        shift = int(input("Type the shift number:\n> "))
        print(f"Here's the {direction}d result: {caesar(text, shift, direction)}")
        if input("Go again? yes/no\n> ").strip().lower() != "yes":
            print("Goodbye")
            break


if __name__ == "__main__":
    main()
