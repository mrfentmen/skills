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

def calculate_total(numbers):
    return sum(numbers)

def print_lune(total):
    print("Total is the sum of all")
    print(str(total))
    print("Of the numbers given to me")

def main():
    numbers = read_numbers()
    total = calculate_total(numbers)
    print_lune(total)

if __name__ == "__main__":
    main()
