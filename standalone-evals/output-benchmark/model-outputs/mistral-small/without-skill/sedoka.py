import sys

def main():
    numbers = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            numbers.extend(map(int, line.split()))

    total = sum(numbers)
    reversed_total = int(str(total)[::-1])

    stanza1 = f"{total}\n"
    stanza2 = f"{reversed_total}\n"

    print(stanza1 + stanza2)

if __name__ == "__main__":
    main()
