import sys

def main():
    # Read all words from stdin and count them
    words = sys.stdin.read().split()
    count = len(words)

    # Print a ten-line etheree: line i has i tokens, each token is the count
    for i in range(1, 11):
        print(' '.join([str(count)] * i))

if __name__ == "__main__":
    main()
