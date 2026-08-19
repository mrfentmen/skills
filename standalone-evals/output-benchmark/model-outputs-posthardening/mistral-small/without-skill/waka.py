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
        print("0\n0\n0\n0\n0")
        return

    min_val = min(numbers)
    max_val = max(numbers)
    count = len(numbers)

    line1 = f"{min_val:.6g}"
    line2 = f"{max_val - min_val:.6g}"
    line3 = f"{count}"
    line4 = f"{max_val:.6g}"
    line5 = f"{max_val - min_val:.6g}"

    print(f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}")

if __name__ == "__main__":
    main()
