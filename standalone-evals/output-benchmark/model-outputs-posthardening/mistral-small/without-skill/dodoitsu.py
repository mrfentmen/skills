import sys

def main():
    numbers = []
    for line in sys.stdin:
        stripped = line.strip()
        if stripped:
            numbers.append(int(stripped))

    if not numbers:
        print("0\n0\n0\n0")
        return

    average = sum(numbers) // len(numbers)

    print("haiku poem")
    print("numbers turn to average")
    print("math in four lines")
    print(average)

if __name__ == "__main__":
    main()
