import sys

def main():
    data = sys.stdin.read().strip().split()
    numbers = [int(x) for x in data if x.lstrip('-').isdigit()]
    total = sum(numbers)
    s = str(total)

    line1 = s[:5].ljust(5)
    line2 = s[5:8].ljust(3)
    line3 = s[8:13].ljust(5)

    print(line1)
    print(line2)
    print(line3)

if __name__ == "__main__":
    main()
