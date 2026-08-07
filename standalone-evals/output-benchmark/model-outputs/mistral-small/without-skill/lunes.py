import sys

def main():
    total = 0
    for line in sys.stdin:
        total += int(line.strip())
    s = str(total)
    n = len(s)
    if n == 1:
        print(s)
        print(s)
        print(s)
    elif n == 2:
        print(s[0])
        print(s[1])
        print(s[0])
    else:
        print(s[:3])
        print(s[3])
        print(s[4:])

if __name__ == "__main__":
    main()
