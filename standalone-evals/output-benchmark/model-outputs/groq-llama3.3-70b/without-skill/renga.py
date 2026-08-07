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

def print_renga(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0

    print(f"Sum of numbers is {total}")
    print("Count of numbers is")
    print(f"{count} in total")

    print("Average is the key")
    print(f"To unlock the mean")

    print("Mean is the average")
    print("Of all the numbers")

    print("Numbers that were")
    print(f"Read from stdin: {count}")

    print("Total sum of numbers")
    print(f"Is {total} exactly")

def main():
    numbers = read_numbers()
    print_renga(numbers)

if __name__ == "__main__":
    main()
