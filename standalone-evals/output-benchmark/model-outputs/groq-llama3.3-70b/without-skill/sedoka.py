import sys

def sedoka_form(n, rev_n):
    print(f"Sum of numbers is {n}")
    print(f"Total count is {len(str(n))}")
    print(f"Result is {n}")

    print(f"Reverse sum is {rev_n}")
    print(f"Reverse count is {len(str(rev_n))}")
    print(f"Reverse result is {rev_n}")

def main():
    numbers = [int(line.strip()) for line in sys.stdin]
    total = sum(numbers)
    rev_total = int(str(total)[::-1])
    sedoka_form(total, rev_total)

if __name__ == "__main__":
    main()
