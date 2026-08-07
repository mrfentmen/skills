import sys

def calculate_total(numbers):
    return sum(numbers)

def print_lune(total):
    print(f"Total of numbers is {total}")
    print("sum")
    print(f"Result is {total} as expected")

def main():
    numbers = []
    for line in sys.stdin:
        for num in line.split():
            try:
                numbers.append(int(num))
            except ValueError:
                pass
    total = calculate_total(numbers)
    print_lune(total)

if __name__ == "__main__":
    main()
