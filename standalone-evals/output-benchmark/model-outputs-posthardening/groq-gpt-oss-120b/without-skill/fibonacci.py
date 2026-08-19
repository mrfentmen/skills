import sys

def main():
    # Read all numbers from stdin, ignoring non-numeric tokens
    tokens = sys.stdin.read().strip().split()
    total = 0
    for t in tokens:
        try:
            total += int(t)
        except ValueError:
            try:
                total += float(t)
            except ValueError:
                continue

    s = str(int(total) if total == int(total) else total)

    # Fibonacci poem with 6 lines: word counts 1,1,2,3,5,8
    lines = [
        "Sum",
        s,
        f"is {s}",
        "the total value",
        "the sum of numbers above",
        f"The computed sum of the input numbers {s}"
    ]

    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
