import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    nums = [float(x) for x in data]
    max_val = max(nums)
    if max_val.is_integer():
        max_val = int(max_val)
    print(f"{max_val}")
    print(" " * 7)
    print(f"{max_val}")

if __name__ == "__main__":
    main()
