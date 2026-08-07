import sys

def main():
    text = sys.stdin.read()
    words = text.split()
    count = len(words)

    lines = [
        str(count),
        str(count * 2),
        str(count * 3),
        str(count * 4),
        str(count)
    ]

    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
