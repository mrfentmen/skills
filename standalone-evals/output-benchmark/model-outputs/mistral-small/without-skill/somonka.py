import sys

def main():
    numbers = []
    for line in sys.stdin:
        stripped = line.strip()
        if stripped:
            try:
                num = int(stripped)
                numbers.append(num)
            except ValueError:
                continue

    total = sum(numbers)
    count = len(numbers)

    stanza1 = [
        f"{count}",
        "numbers read",
        "from the stream",
        f"their total is {total}",
        "what a sight"
    ]

    stanza2 = [
        f"{total}",
        "is the sum now",
        "echoed back",
        f"count was {count}",
        "silent stream"
    ]

    for line in stanza1:
        print(line)
    print()
    for line in stanza2:
        print(line)

if __name__ == "__main__":
    main()
