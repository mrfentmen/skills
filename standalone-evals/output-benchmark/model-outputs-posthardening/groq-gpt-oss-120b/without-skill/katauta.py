import sys
from collections import Counter

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    nums = list(map(int, data))
    freq = Counter(nums)
    most = max(freq.items(), key=lambda x: (x[1], -x[0]))[0]  # most frequent, tie -> larger number
    # Katauta 5-7-7 form (approximate) with a heavy tail
    print(f"{most} is most")          # line 1 (≈5 morae)
    print(f"frequent among the")      # line 2 (≈7 morae)
    print(f"numbers you gave")        # line 3 (≈7 morae)
    print("...")                      # heavy tail

if __name__ == "__main__":
    main()
