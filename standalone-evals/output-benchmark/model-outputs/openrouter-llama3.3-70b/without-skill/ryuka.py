import sys

def count_numbers(numbers):
    positive_count = sum(1 for num in numbers if num > 0)
    negative_count = sum(1 for num in numbers if num < 0)
    return positive_count, negative_count

def print_ryuka(positive_count, negative_count):
    print(f"Positive numbers abound {positive_count} times")
    print(f"Negative numbers lurk in {negative_count} places")
    print(f"Joy and sorrow in {positive_count + negative_count} forms")
    print(f"Balance found in {positive_count - negative_count}")

def main():
    numbers = [int(line.strip()) for line in sys.stdin]
    positive_count, negative_count = count_numbers(numbers)
    print_ryuka(positive_count, negative_count)

if __name__ == "__main__":
    main()
