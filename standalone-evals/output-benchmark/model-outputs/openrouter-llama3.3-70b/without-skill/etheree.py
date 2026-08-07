import sys

def etheree_token_count(words):
    for i in range(1, 11):
        line = ' '.join(words[:i])
        print(line)

def main():
    words = sys.stdin.read().split()
    etheree_token_count(words)

if __name__ == "__main__":
    main()
