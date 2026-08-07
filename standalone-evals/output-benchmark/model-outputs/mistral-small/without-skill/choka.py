import sys

def main():
    data = sys.stdin.read().split()
    numbers = list(map(int, data))
    total = sum(numbers)
    count = len(numbers)
    print(total)
    print(count)
    print("Thus the numbers are summed and counted.")

if __name__ == "__main__":
    main()
