import sys

def main():
    data = sys.stdin.read().strip().split()
    total = sum(map(int, data)) if data else 0
    for _ in range(4):
        print(total)

if __name__ == "__main__":
    main()
