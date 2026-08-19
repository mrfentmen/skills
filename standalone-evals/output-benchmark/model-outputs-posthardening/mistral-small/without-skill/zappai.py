import sys

def main():
    numbers = [int(line.strip()) for line in sys.stdin if line.strip()]
    if not numbers:
        print("")
    else:
        max_num = max(numbers)
        haiku = f"{max_num}\n{max_num}\n{max_num}"
        print(haiku)

if __name__ == "__main__":
    main()
