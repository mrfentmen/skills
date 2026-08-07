import sys

def main():
    data = sys.stdin.read().split()
    total = sum(map(int, data))
    lines = [
        "Numbers flow like river's sigh",
        "Seven beats the quiet tide",
        "Five breaths hold the sum inside",
        f"{total} echoes in the sky"
    ]
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
