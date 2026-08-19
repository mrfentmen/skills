import sys
from collections import Counter

def main():
    numbers = []
    for line in sys.stdin:
        stripped = line.strip()
        if stripped:
            numbers.append(int(stripped))

    if not numbers:
        return

    counter = Counter(numbers)
    most_common = counter.most_common(1)[0][0]

    print(f"{most_common}")
    print(f"  {most_common}")
    print(f"    {most_common}  ")

if __name__ == "__main__":
    main()
