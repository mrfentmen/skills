import sys

def main():
    numbers = []
    for line in sys.stdin:
        stripped = line.strip()
        if stripped:
            numbers.append(float(stripped))

    total = sum(numbers)
    mean = total / len(numbers) if numbers else 0

    lines = [
        f"{mean:.6f}",
        f"{total:.6f}",
        "五七五",
        "七七七",
        "五五五五五五五",
        "七七七七七七七"
    ]

    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
