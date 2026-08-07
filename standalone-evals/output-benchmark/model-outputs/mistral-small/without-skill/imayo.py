import sys

def imayo_song(numbers):
    total = sum(numbers)
    lines = [
        f"Rolling waves of {total} flow,",
        f"Seven beats in steady row,",
        f"Five then seven, soft they go,",
        f"Numbers sing their tale we know."
    ]
    return '\n'.join(lines)

def main():
    numbers = []
    for line in sys.stdin:
        stripped = line.strip()
        if stripped:
            try:
                num = float(stripped)
                numbers.append(num)
            except ValueError:
                continue
    if numbers:
        print(imayo_song(numbers))

if __name__ == "__main__":
    main()
