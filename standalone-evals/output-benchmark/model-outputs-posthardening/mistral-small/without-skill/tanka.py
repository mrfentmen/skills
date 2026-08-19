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
                pass

    if not numbers:
        print("0.0")
        print("0.0")
        print("0.0")
        print("0.0")
        print("0.0")
        return

    mean = sum(numbers) / len(numbers)
    print(mean)

    min_val = min(numbers)
    max_val = max(numbers)
    range_val = max_val - min_val
    print(range_val)

    tanka = [
        f"{mean:.1f}",
        f"{range_val:.1f}",
        f"{mean * range_val:.1f}",
        f"{mean + range_val:.1f}",
        f"{mean - range_val:.1f}"
    ]

    for line in tanka:
        print(line)

if __name__ == "__main__":
    main()
