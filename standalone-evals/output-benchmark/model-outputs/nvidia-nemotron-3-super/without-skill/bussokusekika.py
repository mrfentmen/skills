import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    nums = list(map(float, data))
    total = sum(nums)
    mean = total / len(nums)
    lines = [
        f"{total:.5g}",
        f"{mean:.5g}",
        f"{len(nums):.5g}",
        f"{total + mean:.5g}",
        f"{total * mean:.5g}",
        f"{total - mean:.5g}"
    ]
    print("\n".join(lines))

if __name__ == "__main__":
    main()
