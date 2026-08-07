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
        print("0")
        print("0")
        print("0")
        print("0")
        print("0")
        return

    mean = sum(numbers) / len(numbers)
    print(mean)

    if len(numbers) < 2:
        print(0)
        print(0)
        print("0\n0\n0")
        return

    min_val = min(numbers)
    max_val = max(numbers)
    print(max_val - min_val)

    tanka = [
        f"{mean:.6f}",
        f"{min_val:.6f}",
        f"{max_val:.6f}",
        f"{mean:.6f}",
        f"{max_val - min_val:.6f}"
    ]
    print("\n".join(tanka))

if __name__ == "__main__":
    main()
