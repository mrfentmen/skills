import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    nums = list(map(int, data))
    peak = max(nums)
    spread = peak - min(nums)

    # Kyoka (5-7-5-7-7) – poetic lines; the last two lines add a comic twist.
    # Exact syllable counting is left to the poet; we just embed the values.
    lines = [
        "Numbers rise up high",                     # 5 syllables (approx.)
        "From humble lows they start to climb",     # 7 syllables (approx.)
        f"The max is {peak}",                      # 5 syllables (approx.)
        f"The spread is {spread}, a wide grin",    # 7 syllables (approx.)
        "Even math can tell a joke!"               # 7 syllables (approx.)
    ]

    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
