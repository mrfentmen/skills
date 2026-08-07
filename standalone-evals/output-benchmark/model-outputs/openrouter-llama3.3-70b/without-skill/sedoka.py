import sys

def sedoka_sum(numbers):
    total = sum(numbers)
    reverse_total = int(str(total)[::-1])
    return total, reverse_total

def print_sedoka(total, reverse_total):
    print(f"In the depths of {total} numbers")
    print("Lies a truth we must unfold")
    print("A sum that's hidden, yet to be told")
    print()
    print(f"Reflected in {reverse_total} we see")
    print("A mirrored truth, for all to hold")
    print("A reverse sum, for you and me")

def main():
    numbers = [int(line.strip()) for line in sys.stdin]
    total, reverse_total = sedoka_sum(numbers)
    print_sedoka(total, reverse_total)

if __name__ == "__main__":
    main()
