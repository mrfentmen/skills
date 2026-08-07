import sys

def main():
    numbers = []
    for line in sys.stdin:
        stripped = line.strip()
        if stripped:
            numbers.append(int(stripped))

    total = sum(numbers)

    # Split the total into three lines: 5-3-5 characters
    total_str = str(total)
    first_part = total_str[:5]
    middle_part = total_str[5:8]
    last_part = total_str[8:]

    print(first_part)
    print(middle_part)
    print(last_part)

if __name__ == "__main__":
    main()
