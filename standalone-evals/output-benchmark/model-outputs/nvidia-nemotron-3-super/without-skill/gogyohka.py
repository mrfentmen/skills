import sys

def main():
    words = sys.stdin.read().split()
    count = len(words)
    print(f"{count}\n{count}\n{count}\n{count}\n{count}")

if __name__ == "__main__":
    main()
