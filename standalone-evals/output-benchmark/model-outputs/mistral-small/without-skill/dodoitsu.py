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

    line1 = "Hear the numbers,"
    line2 = "Count them up,"
    line3 = "Find their average,"
    line4 = f"{average} it is."

    print(line1)
    print(line2)
    print(line3)
    print(line4)

if __name__ == "__main__":
    main()
