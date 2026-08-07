import sys

def calculate_peak_and_spread(numbers):
    peak = max(numbers)
    spread = max(numbers) - min(numbers)
    return peak, spread

def format_output(peak, spread):
    lines = [
        f"Numbers rise to {peak}",
        f"A majestic {spread} apart",
        f"Like mountains high and wide",
        f"But then I trip on one",
        f"And face-plant in the spread"
    ]
    return "\n".join(lines)

def main():
    numbers = [int(line.strip()) for line in sys.stdin]
    peak, spread = calculate_peak_and_spread(numbers)
    print(format_output(peak, spread))

if __name__ == "__main__":
    main()
