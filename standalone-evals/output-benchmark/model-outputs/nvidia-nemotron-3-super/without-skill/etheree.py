import sys

def main():
    words = sys.stdin.read().split()
    n = len(words)
    for i in range(1, 11):
        if i <= n:
            print(' '.join(words[:i]))
        else:
            print()

if __name__ == "__main__":
    main()
