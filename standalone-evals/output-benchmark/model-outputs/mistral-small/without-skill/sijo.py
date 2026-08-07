import sys

def main():
    numbers = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            numbers.append(float(line))

    if not numbers:
        print("No numbers provided.")
        return

    average = sum(numbers) / len(numbers)
    print(f"Average: {average}")

    above_avg = sum(1 for num in numbers if num > average)
    print(f"Numbers above average: {above_avg}")

if __name__ == "__main__":
    main()
