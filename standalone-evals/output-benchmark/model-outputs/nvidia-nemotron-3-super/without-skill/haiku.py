import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    nums = list(map(float, data))
    max_val = max(nums)
    if max_val.is_integer():
        max_val = int(max_val)
    print(f"{max_val}")
    print("is the largest")
    print("number here")

if __name__ == "__main__":
    main()
