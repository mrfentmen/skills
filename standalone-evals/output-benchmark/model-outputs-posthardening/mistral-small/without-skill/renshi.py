import sys

def count_tokens(text):
    tokens = text.split()
    return len(tokens)

def main():
    text = sys.stdin.readline().strip()
    token_count = count_tokens(text)
    print(f"Stage 1: Token count is {token_count}")

    # Stage 2: Recalculate after removing punctuation
    import string
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)
    token_count = count_tokens(cleaned_text)
    print(f"Stage 2: Token count after punctuation removal is {token_count}")

    # Stage 3: Recalculate after lowercasing
    lower_text = cleaned_text.lower()
    token_count = count_tokens(lower_text)
    print(f"Stage 3: Token count after lowercasing is {token_count}")

if __name__ == "__main__":
    main()
