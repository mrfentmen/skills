# Stage 1: Read input from stdin
import sys

def read_input():
    return sys.stdin.readline().strip()

# Stage 2: Tokenize the input text
def tokenize_text(text):
    return text.split()

# Stage 3: Count the tokens
def count_tokens(tokens):
    return len(tokens)

# Main program
def main():
    text = read_input()
    tokens = tokenize_text(text)
    token_count = count_tokens(tokens)
    print(token_count)

if __name__ == "__main__":
    main()
