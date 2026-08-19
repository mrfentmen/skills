import sys

def main():
    # Read all numbers from stdin (whitespace separated)
    data = sys.stdin.read().split()
    numbers = list(map(int, data))

    total = sum(numbers)
    count = len(numbers)

    # First couplet: sum and count
    print(total)
    print(count)

    # Second couplet: turn and resolve
    print("Turn")
    print("Resolve")

if __name__ == "__main__":
    main()
