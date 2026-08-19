def main():
    numbers = list(map(int, input().split()))
    total = sum(numbers)
    count = len(numbers)
    print(total)
    print(count)
    print("Thus the numbers are summed and counted.")

if __name__ == "__main__":
    main()
