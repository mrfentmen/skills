import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    numbers = list(map(int, data))
    count = len(numbers)
    total = sum(numbers)
    voice1 = [
        str(count),
        "numbers read from input",
        "each one a quiet thought",
        "waiting to be counted, seen",
        "in the silence of the stream"
    ]
    voice2 = [
        str(total),
        "their sum now softly spoken",
        "echoes in the empty air",
        "a gentle total, whole and true",
        "born from many, one at last"
    ]
    print("\n".join(voice1))
    print()
    print("\n".join(voice2))

if __name__ == "__main__":
    main()
