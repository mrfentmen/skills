import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    numbers = list(map(float, data))
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    print(int(total) if total.is_integer() else total)
    print(count)
    print(int(average) if average.is_integer() else average)

if __name__ == "__main__":
    main()
