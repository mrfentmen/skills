import sys

def read_numbers():
    return list(map(int, input().split()))

def calculate_sum_and_count(numbers):
    total_sum = sum(numbers)
    count = len(numbers)
    return total_sum, count

def print_choka(sum_value, count):
    print(f"Sum: {sum_value}")
    print(f"Count: {count}")
    print(f"Numbers added with care,")
    print(f"Total and count beyond compare.")

def main():
    numbers = read_numbers()
    total_sum, count = calculate_sum_and_count(numbers)
    print_choka(total_sum, count)

if __name__ == "__main__":
    main()
