import sys
import math

def fibonacci_sequence(n):
    sequence = []
    a, b = 1, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

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
        return

    total = sum(numbers)
    rounded_total = round(total)
    if rounded_total < 1:
        rounded_total = 1

    fib_lines = fibonacci_sequence(8)
    fib_lines = [max(1, x) for x in fib_lines[:6]]  # Ensure at least 1 line per segment

    words = [
        "The", "golden", "ratio", "unfolds", "in", "numbers", "dancing",
        "through", "time", "and", "space", "a", "poem", "of", "growth",
        "and", "grace", "the", "sum", "of", "all", "things", "now", "in",
        "place", "a", "fibonacci", "flow", "where", "each", "line", "does",
        "grow", "like", "petals", "in", "a", "row"
    ]

    index = 0
    for line_count in fib_lines:
        for _ in range(line_count):
            if index >= len(words):
                break
            print(words[index], end=' ')
            index += 1
        if index >= len(words):
            break
        print()

    print(f"\n{rounded_total}")

if __name__ == "__main__":
    main()
