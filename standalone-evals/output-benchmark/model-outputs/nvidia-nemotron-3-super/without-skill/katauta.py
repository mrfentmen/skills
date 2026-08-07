import sys
from collections import Counter

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    nums = list(map(int, data))
    freq = Counter(nums)
    max_freq = max(freq.values())
    candidates = [num for num, count in freq.items() if count == max_freq]
    result = min(candidates)
    print(f"{result}\n{result}\n{result}")

if __name__ == "__main__":
    main()
