import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    numbers = list(map(float, data))
    avg = sum(numbers) / len(numbers)
    above_avg = sum(1 for x in numbers if x > avg)
    print(f"{avg:.6f}")
    print(f"{above_avg}")

if __name__ == "__main__":
    main()
