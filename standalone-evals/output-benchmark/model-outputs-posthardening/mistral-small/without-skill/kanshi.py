import sys

def main():
    numbers = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            numbers.append(int(line))

    total = sum(numbers)
    count = len(numbers)

    print(f"{total} {count}")

    if count == 0:
        print("0 0")
    else:
        average = total / count
        print(f"turn {average:.2f}")

if __name__ == "__main__":
    main()
