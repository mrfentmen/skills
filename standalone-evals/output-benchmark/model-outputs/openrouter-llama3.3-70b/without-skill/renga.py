import sys

def read_numbers():
    numbers = []
    for line in sys.stdin:
        for num in line.split():
            try:
                numbers.append(float(num))
            except ValueError:
                pass
    return numbers

def calculate_sum(numbers):
    return sum(numbers)

def calculate_count(numbers):
    return len(numbers)

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def print_renga(numbers):
    total = calculate_sum(numbers)
    count = calculate_count(numbers)
    average = calculate_average(numbers)
    print(f"Sum of numbers is {total}")
    print(f"Count of numbers is {count}")
    print(f"Average of numbers is {average}")
    print()
    print(f"Numbers add up to {total}")
    print(f"Total count is {count}")
    print()
    print(f"Mean value is {average}")
    print(f"Total sum is {total}")

def main():
    numbers = read_numbers()
    print_renga(numbers)

if __name__ == "__main__":
    main()
