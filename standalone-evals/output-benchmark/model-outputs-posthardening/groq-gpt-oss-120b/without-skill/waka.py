import sys

def main():
    data = sys.stdin.read().strip().split()
    nums = [int(x) for x in data if x.lstrip('-').isdigit()]
    cnt = len(nums)
    rng = max(nums) - min(nums) if cnt > 0 else 0

    # Five‑line waka (tanka) output
    print(rng)
    print(cnt)
    print(rng)
    print(cnt)
    print(f"{rng} {cnt}")

if __name__ == "__main__":
    main()
