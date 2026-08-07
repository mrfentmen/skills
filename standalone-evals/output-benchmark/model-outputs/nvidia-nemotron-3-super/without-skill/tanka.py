import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    nums = list(map(float, data))
    mean = sum(nums) / len(nums)
    r = max(nums) - min(nums)
    print(f"{mean:.6g}")
    print(f"{mean:.6g} {r:.6g}")
    print(f"{mean:.6g} {r:.6g} {len(nums)}")
    print(f"{mean:.6g} {r:.6g} {len(nums)} {sum(nums):.6g}")
    print(f"{mean:.6g} {r:.6g} {len(nums)} {sum(nums):.6g} {min(nums):.6g}")

if __name__ == "__main__":
    main()
