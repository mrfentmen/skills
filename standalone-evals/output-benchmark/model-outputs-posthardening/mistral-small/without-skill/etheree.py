import sys

def main():
    words = []
    for line in sys.stdin:
        words.extend(line.split())

    token_count = len(words)

    etheree = [
        words[i] if i < token_count else ""
        for i in range(10)
    ]

    for i in range(1, 11):
        print(" ".join(etheree[:i]))

if __name__ == "__main__":
    main()
