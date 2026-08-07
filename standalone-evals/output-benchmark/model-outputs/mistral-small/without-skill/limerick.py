import sys

def main():
    numbers = []
    for line in sys.stdin:
        stripped = line.strip()
        if stripped:
            try:
                num = float(stripped)
                numbers.append(num)
            except ValueError:
                pass

    total = sum(numbers)

    line1 = f"{int(total) if total.is_integer() else total:.2f}"
    line2 = line1
    line3 = "Why the long face?"
    line4 = "Math just won't make space!"
    line5 = f"Sum's {line1}—now go touch some grass!"

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)

if __name__ == "__main__":
    main()
