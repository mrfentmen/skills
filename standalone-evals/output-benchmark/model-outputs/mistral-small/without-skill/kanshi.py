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

    print(f"{total} {count}")

    if count == 0:
        print("0 0")
        return

    avg = total / count
    print(f"turn {avg:.1f}")
    print(f"resolve {avg:.1f}")

if __name__ == "__main__":
    main()
