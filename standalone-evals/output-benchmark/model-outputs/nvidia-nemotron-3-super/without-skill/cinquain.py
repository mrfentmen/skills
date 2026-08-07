import sys

def main():
    words = sys.stdin.read().split()
    n = len(words)
    print(' ' * 3 + str(n))
    print(' ' * 2 + str(n) + ' ' + str(n))
    print(' ' * 1 + str(n) + ' ' + str(n) + ' ' + str(n))
    print(str(n) + ' ' + str(n) + ' ' + str(n) + ' ' + str(n))
    print(' ' * 3 + str(n))

if __name__ == "__main__":
    main()
