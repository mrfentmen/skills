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
        print("0")
        print("0")
        print("0")
        return

    mean = sum(numbers) / len(numbers)
    print(mean)

    if len(numbers) < 2:
        print("0.0")
        print("0")
        print("0")
        print("0")
        print("0")
        return

    min_val = min(numbers)
    max_val = max(numbers)
    print(max_val - min_val)

    range_val = max_val - min_val
    line1 = range_val
    line2 = range_val * 2
    line3 = range_val * 3
    line4 = range_val * 4
    line5 = range_val * 5

    print(f"{line1:.1f}")
    print(f"{line2:.1f}")
    print(f"{line3:.1f}")
    print(f"{line4:.1f}")
    print(f"{line5:.1f}")

if __name__ == "__main__":
    main()
