import sys

def main():
    numbers = list(map(int, sys.stdin.read().split()))
    max_num = max(numbers) if numbers else 0
    print("Numbers read")
    print("Maximum found")
    print(f"{max_num}")

if __name__ == "__main__":
    main()
