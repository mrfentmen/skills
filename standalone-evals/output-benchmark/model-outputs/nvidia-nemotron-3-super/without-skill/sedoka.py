import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    total = sum(int(x) for x in data)
    rev_total = int(str(total)[::-1])
    print(f"{total}")
    print(f"{total}")
    print(f"{total}")
    print(f"{rev_total}")
    print(f"{rev_total}")
    print(f"{rev_total}")

if __name__ == "__main__":
    main()
