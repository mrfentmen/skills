import sys

def calculate_total():
    total = 0
    for line in sys.stdin:
        for num in line.split():
            try:
                total += float(num)
            except ValueError:
                pass
    return total

def print_lune(total):
    print("Totals are fun to see")
    print(str(total))
    print("Now the totals are free")

def main():
    total = calculate_total()
    print_lune(total)

if __name__ == "__main__":
    main()
