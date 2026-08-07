import sys

def read_numbers():
    numbers = []
    for line in sys.stdin:
        for word in line.split():
            try:
                numbers.append(float(word))
            except ValueError:
                pass
    return numbers

def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)

def print_zappai(max_number):
    if max_number is None:
        print("Empty input")
        return
    max_str = str(max_number)
    max_len = len(max_str)
    first_line = max_str[:5]
    second_line = max_str[5:12]
    third_line = max_str[-5:]
    if len(second_line) < 7:
        second_line += ' ' * (7 - len(second_line))
    if len(first_line) < 5:
        first_line = ' ' * (5 - len(first_line)) + first_line
    if len(third_line) < 5:
        third_line += ' ' * (5 - len(third_line))
    print(first_line)
    print(second_line)
    print(third_line)

def main():
    numbers = read_numbers()
    max_number = find_max(numbers)
    print_zappai(max_number)

if __name__ == "__main__":
    main()
