import sys
from collections import Counter

def main():
    numbers = list(map(int, sys.stdin.read().split()))
    if not numbers:
        return
    counter = Counter(numbers)
    most_common = counter.most_common(1)[0][0]
    print(f"{most_common}")
    print(f"  {most_common}")
    print(f"    {most_common}")

if __name__ == "__main__":
    main()
