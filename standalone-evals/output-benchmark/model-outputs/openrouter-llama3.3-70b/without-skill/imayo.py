import sys

def read_numbers():
    numbers = []
    for line in sys.stdin:
        for num in line.split():
            try:
                numbers.append(int(num))
            except ValueError:
                pass
    return numbers

def sing_sum(numbers):
    total = sum(numbers)
    print(f"Breathing in the sum so fine {total}")
    print(f"Rolling numbers in my mind so free {total}")
    print(f"Feeling the math all the time so me {total}")
    print(f"Singing the sum wild and carefree {total}")

def main():
    numbers = read_numbers()
    sing_sum(numbers)

if __name__ == "__main__":
    main()
