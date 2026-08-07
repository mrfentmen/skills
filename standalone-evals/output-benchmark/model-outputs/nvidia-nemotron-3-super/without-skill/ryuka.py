import sys

def main():
    data = sys.stdin.read().split()
    pos = 0
    neg = 0
    for token in data:
        try:
            num = int(token)
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1
        except ValueError:
            continue
    print(f"{pos:>8}")
    print(f"{neg:>8}")
    print(f"{pos + neg:>8}")
    print(f"{abs(pos - neg):>6}")

if __name__ == "__main__":
    main()
