import sys

def cinquain(word_count):
    """Prints the word count in the five-line cinquain form."""
    lines = [
        f"{word_count} {word_count}",
        f"{word_count} {word_count} {word_count} {word_count}",
        f"{word_count} {word_count} {word_count} {word_count} {word_count} {word_count}",
        f"{word_count} {word_count} {word_count} {word_count} {word_count} {word_count} {word_count} {word_count}",
        f"{word_count} {word_count}",
    ]
    for line in lines:
        print(line)

def main():
    """Reads words from stdin and prints the word count in the cinquain form."""
    words = sys.stdin.read().split()
    word_count = len(words)
    cinquain(word_count)

if __name__ == "__main__":
    main()
