import sys

def main():
    data = sys.stdin.read().strip().split()
    numbers = [int(x) for x in data if x.lstrip('-').isdigit()]
    total = sum(numbers)
    total_str = str(total)
    reverse_str = total_str[::-1]

    # First stanza (sum) – three lines
    for _ in range(3):
        print(total_str)
    # Second stanza (reverse sum) – three lines
    for _ in range(3):
        print(reverse_str)

if __name__ == "__main__":
    main()
