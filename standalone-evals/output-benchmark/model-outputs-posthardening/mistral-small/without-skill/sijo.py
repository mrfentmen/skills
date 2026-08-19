import sys

def main():
    numbers = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            num = float(line)
            numbers.append(num)
        except ValueError:
            continue

    if not numbers:
        print(0)
        return

    average = sum(numbers) / len(numbers)
    print(average)

    above_avg = sum(1 for num in numbers if num > average)
    print(above_avg)

if __name__ == "__main__":
    main()
