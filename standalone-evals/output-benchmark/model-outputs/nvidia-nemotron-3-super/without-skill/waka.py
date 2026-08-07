import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    nums = list(map(int, data))
    r = max(nums) - min(nums)
    c = len(nums)
    print(f"{r}")
    print(f"{c}")
    print(f"{r}")
    print(f"{c}")
    print(f"{c}")

if __name__ == "__main__":
    main()
