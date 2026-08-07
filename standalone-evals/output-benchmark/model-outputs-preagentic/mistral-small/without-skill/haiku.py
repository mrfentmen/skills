import sys

def main():
    numbers = [int(line.strip()) for line in sys.stdin if line.strip()]
    if not numbers:
        print("No numbers provided")
        return
    max_num = max(numbers)
    print("Numbers read in")
    print("Peak value found")
    print(f"Max is {max_num}")

if __name__ == "__main__":
    main()
