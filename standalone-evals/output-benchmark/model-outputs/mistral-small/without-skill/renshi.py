import sys

def count_tokens(text):
    return len(text.split())

def main():
    text = sys.stdin.readline().strip()
    stages = [
        ("Stage 1: Initial token count", count_tokens(text)),
        ("Stage 2: Processing tokens", count_tokens(text) * 2),
        ("Stage 3: Final token analysis", count_tokens(text) + 5)
    ]

    for stage_name, token_count in stages:
        print(f"{stage_name} - Tokens: {token_count}")

if __name__ == "__main__":
    main()
