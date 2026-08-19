import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    numbers = [float(x) if '.' in x else int(x) for x in data]
    max_val = max(numbers)
    # If the input numbers are integers, display as int; otherwise keep as float
    max_str = str(int(max_val)) if isinstance(max_val, int) or max_val.is_integer() else str(max_val)

    print("The greatest number")
    print(f"is {max_str} the highest value")
    print("among all numbers")

if __name__ == "__main__":
    main()
