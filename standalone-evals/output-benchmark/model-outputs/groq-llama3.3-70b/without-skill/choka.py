import sys

def read_numbers():
    return list(map(int, sys.stdin.readline().split()))

def calculate_sum_and_count(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total, count

def print_choka_form(total, count):
    print(f"Sum: {total}")
    print(f"Count: {count}")
    print(f"In numbers we find our fate,")
    print(f"Sum {total} and count {count} create.")

def main():
    numbers = read_numbers()
    total, count = calculate_sum_and_count(numbers)
    print_choka_form(total, count)

if __name__ == "__main__":
    main()
