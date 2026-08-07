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

    print("Average is not a myth")
    print("Sum divided by count")
    print("Whole number result")
    print(average)

if __name__ == "__main__":
    main()
