import sys

def pad_right(s: str, length: int) -> str:
    """Pad the string on the right with spaces to reach the given length."""
    return s + ' ' * (length - len(s))

def main() -> None:
    data = sys.stdin.read().strip().split()
    pos = neg = 0
    for token in data:
        try:
            num = int(token)
        except ValueError:
            continue
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1

    line1 = pad_right(f"Pos: {pos}", 8)
    line2 = pad_right(f"Neg: {neg}", 8)
    line3 = pad_right("Result", 8)
    line4 = pad_right("Finish", 6)  # exactly 6 characters, no extra spaces needed

    sys.stdout.write("\n".join([line1, line2, line3, line4]))

if __name__ == "__main__":
    main()
