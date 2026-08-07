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
                continue

    if not numbers:
        print("No valid numbers provided.")
        return

    peak = max(numbers)
    spread = peak - min(numbers)

    line1 = f"Peak stands tall at {peak}"
    line2 = f"Numbers climb and fall so wide"
    line3 = f"Spread reveals the gap"
    line4 = f"From lowest to highest they leap"
    line5 = f"Yet data's dance hides truth's prank!"

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)

if __name__ == "__main__":
    main()
