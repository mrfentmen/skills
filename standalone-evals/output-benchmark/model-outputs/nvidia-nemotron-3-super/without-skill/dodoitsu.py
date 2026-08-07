import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    nums = list(map(int, data))
    avg = sum(nums) // len(nums)
    print(f"{avg}")
    print(f"{avg}")
    print(f"{avg}")
    print(f"{avg}")

if __name__ == "__main__":
    main()
