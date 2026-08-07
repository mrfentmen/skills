import sys

def main():
    text = sys.stdin.read()
    tokens = text.split()
    count = len(tokens)
    print(count)

if __name__ == "__main__":
    main()
