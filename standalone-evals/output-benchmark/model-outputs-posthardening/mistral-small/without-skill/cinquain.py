import sys

def main():
    text = sys.stdin.read()
    words = text.split()
    count = len(words)

    lines = [
        f"{count // 5}",
        f"{count // 5 * 2}",
        f"{count // 5 * 3}",
        f"{count // 5 * 4}",
        f"{count // 5}"
    ]

    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
