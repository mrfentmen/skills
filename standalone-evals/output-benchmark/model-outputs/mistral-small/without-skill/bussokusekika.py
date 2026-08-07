import sys

def main():
    numbers = []
    for line in sys.stdin:
        stripped = line.strip()
        if stripped:
            try:
                num = float(stripped)
                numbers.append(num)
            except ValueError:
                continue

    if not numbers:
        print("0\n0\n0\n0\n0\n0")
        return

    total = sum(numbers)
    mean = total / len(numbers)

    lines = [
        f"{mean:.6f}",
        f"{total:.6f}",
        f"{mean:.6f}",
        f"{total:.6f}",
        f"{mean:.6f}",
        f"{total:.6f}"
    ]

    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
