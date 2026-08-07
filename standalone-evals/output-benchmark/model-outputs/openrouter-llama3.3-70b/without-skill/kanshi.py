import sys

def read_numbers():
    """Read numbers from stdin."""
    numbers = []
    for line in sys.stdin:
        for num in line.split():
            try:
                numbers.append(float(num))
            except ValueError:
                pass
    return numbers

def kanshi_form(numbers):
    """Print the sum and count in kanshi form."""
    total = sum(numbers)
    count = len(numbers)
    print(f"Sum of numbers is {total:.2f},")
    print(f"Count of numbers is {count}.")
    print(f"Turn to find the average,")
    print(f"Resolve with {total / count if count > 0 else 0:.2f}.")

def main():
    numbers = read_numbers()
    kanshi_form(numbers)

if __name__ == "__main__":
    main()
