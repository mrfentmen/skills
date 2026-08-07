import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    nums = list(map(int, data))
    peak = max(nums)
    spread = max(nums) - min(nums)
    print(f"{peak}")
    print(f"{spread} is the spread")
    print(f"{peak}")
    print(f"{spread} is the spread")
    print(f"Peak: {peak}, Spread: {spread} — turns out, math is just a joke with extra steps")

if __name__ == "__main__":
    main()
