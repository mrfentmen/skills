import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    # Convert to integers (or floats if needed)
    try:
        numbers = list(map(int, data))
    except ValueError:
        numbers = list(map(float, data))
    max_val = max(numbers)

    # Prepare haiku lines
    line1 = "Numbers come and go"
    line2 = f"The greatest number is {max_val}"
    line3 = "Quiet peak remains"

    print(line1)
    print(line2)
    print(line3)

if __name__ == "__main__":
    main()
