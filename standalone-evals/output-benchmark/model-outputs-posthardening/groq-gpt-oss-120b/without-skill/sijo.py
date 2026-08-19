import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    numbers = list(map(float, data))
    avg = sum(numbers) / len(numbers)
    above_count = sum(1 for x in numbers if x > avg)
    print(avg)
    print()
    print(above_count)

if __name__ == "__main__":
    main()
