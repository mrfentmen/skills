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
        print("No numbers found.")
        return

    peak = max(numbers)
    spread = peak - min(numbers)

    haiku = f"{peak:.2f}\n{spread:.2f}\n"
    haiku += "Peak stands so tall\n"
    haiku += f"{spread:.2f} units wide\n"
    haiku += "Yet numbers dance low"

    print(haiku)

if __name__ == "__main__":
    main()
