import sys

def main():
    numbers = []
    for line in sys.stdin:
        stripped = line.strip()
        if stripped:
            numbers.append(int(stripped))

    if not numbers:
        print("0\n0\n0\n0\n0")
        return

    min_val = min(numbers)
    max_val = max(numbers)
    count = len(numbers)

    line1 = f"{min_val}"
    line2 = f"{max_val - min_val}"
    line3 = f"{count}"
    line4 = f"{max_val}"
    line5 = f"{max_val - min_val}"

    print(f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}")

if __name__ == "__main__":
    main()
