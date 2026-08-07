import sys

def main():
    data = sys.stdin.readline().split()
    numbers = list(map(int, data))

    total = sum(numbers)
    count = len(numbers)

    print(total)
    print(count)

    if count > 0:
        print("The sum and count are as above.")
    else:
        print("No numbers provided.")

if __name__ == "__main__":
    main()
