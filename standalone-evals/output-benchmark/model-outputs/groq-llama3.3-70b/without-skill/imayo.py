import sys

def read_numbers():
    """Read numbers from stdin."""
    numbers = []
    for line in sys.stdin:
        for num in line.split():
            try:
                numbers.append(int(num))
            except ValueError:
                pass
    return numbers

def calculate_sum(numbers):
    """Calculate the sum of the numbers."""
    return sum(numbers)

def sing_sum(total):
    """Sing the sum in a four-line imayo song."""
    lines = [
        f"Na na na na na na na, sum is {total} yo",
        f"Na na na na na, total is {total} ne",
        f"Na na na na na na, sum is {total} yo",
        f"Na na na na na, total is {total} ne"
    ]
    for line in lines:
        print(line)

def main():
    numbers = read_numbers()
    total = calculate_sum(numbers)
    sing_sum(total)

if __name__ == "__main__":
    main()
