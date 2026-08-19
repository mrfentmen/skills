import sys

def main():
    # Read all numbers from stdin (space or newline separated)
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        return
    numbers = list(map(float, tokens))

    # Compute mean and range
    mean_val = sum(numbers) / len(numbers)
    range_val = max(numbers) - min(numbers)

    # Output a tanka (5 lines). The first line shows the mean,
    # the last two lines expand on the range.
    print(f"{mean_val:.2f}")
    print("Numbers gathered, quiet")
    print("Their average whispers")
    print(f"Range spans {range_val:.2f} units")
    print("Between the smallest and largest")

if __name__ == "__main__":
    main()
