import sys

def read_numbers():
    numbers = []
    for line in sys.stdin:
        for word in line.split():
            try:
                numbers.append(float(word))
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

def print_renga(sum_value, count_value, average_value):
    print(f"Sum of numbers: {sum_value}")
    print("Count of numbers")
    print(f"Is {count_value}")
    print("Average of numbers")
    print(f"Is {average_value}")

def main():
    numbers = read_numbers()
    sum_value = calculate_sum(numbers)
    count_value = calculate_count(numbers)
    average_value = calculate_average(numbers)
    print_renga(sum_value, count_value, average_value)

if __name__ == "__main__":
    main()
