import sys

def main():
    # Read a single line of text from stdin
    line = sys.stdin.readline()
    # Remove trailing newline but keep other whitespace for tokenization
    line = line.rstrip('\n')
    # Tokenize by whitespace
    tokens = line.split()
    count = len(tokens)

    # Linked renshi stages (each 2-3 lines)
    print("Stage 1:")
    print("Reading the input line.")
    print("Preparing to count.")
    print()
    print("Stage 2:")
    print("Splitting into tokens.")
    print("Counting them.")
    print()
    print("Stage 3:")
    print("The token count is:")
    print(count)

if __name__ == "__main__":
    main()
