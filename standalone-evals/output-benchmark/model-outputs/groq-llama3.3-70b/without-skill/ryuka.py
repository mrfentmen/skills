import sys

def count_numbers(numbers):
    positive_count = sum(1 for num in numbers if num > 0)
    negative_count = sum(1 for num in numbers if num < 0)
    return positive_count, negative_count

def print_ryuka(positive_count, negative_count):
    print(f"Positive numbers: {positive_count} times")
    print(f"Negative numbers: {negative_count} times")
    print(f"Numbers in total: {positive_count + negative_count} times")
    print(f"Ratio: {positive_count}:{negative_count}")

def main():
    numbers = []
    for line in sys.stdin:
        try:
            numbers.append(int(line.strip()))
        except ValueError:
            break
    positive_count, negative_count = count_numbers(numbers)
    print_ryuka(positive_count, negative_count)

if __name__ == "__main__":
    main()
