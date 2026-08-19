import sys

def main():
    text = sys.stdin.read()
    # Split on any whitespace to get words
    words = text.split()
    count = len(words)
    # Print the count in exactly five lines
    for _ in range(5):
        print(count)

if __name__ == "__main__":
    main()
