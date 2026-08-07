import sys

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def count_above_average(numbers, average):
    return sum(1 for num in numbers if num > average)

def main():
    numbers = []
    for line in sys.stdin:
        numbers.extend(map(float, line.split()))
    average = calculate_average(numbers)
    above_average_count = count_above_average(numbers, average)
    print(f"Average: {average}")
    print(f"Count above average: {above_average_count}")

if __name__ == "__main__":
    main()
