import sys

def imayo_song(numbers):
    total = sum(numbers)
    lines = [
        f"Rolling waves of {total} flow,",
        f"Seven beats in steady row,",
        f"Five soft tones in gentle glow,",
        f"Sum now sings in soft tableau."
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
    print(imayo_song(numbers))

if __name__ == "__main__":
    main()
