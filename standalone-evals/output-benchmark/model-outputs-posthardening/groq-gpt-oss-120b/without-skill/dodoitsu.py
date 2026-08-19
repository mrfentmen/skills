import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    nums = list(map(int, data))
    avg = sum(nums) // len(nums)  # integer average (floor division)

    # Four‑line dodoitsu style output
    print("Numbers gathered,")
    print("Sum computed,")
    print("Average found,")
    print(avg)

if __name__ == "__main__":
    main()
