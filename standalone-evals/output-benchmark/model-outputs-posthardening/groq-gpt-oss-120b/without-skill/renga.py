import sys

def read_numbers():
    data = sys.stdin.read().strip()
    if not data:
        return []
    # Split on any whitespace
    parts = data.split()
    nums = []
    for p in parts:
        try:
            if '.' in p or 'e' in p.lower():
                nums.append(float(p))
            else:
                nums.append(int(p))
        except ValueError:
            # ignore non‑numeric tokens
            pass
    return nums

def fmt_number(x):
    # Show as int if it is an integer value, else as float with up to 6 decimals trimmed
    if isinstance(x, int) or (isinstance(x, float) and x.is_integer()):
        return str(int(x))
    else:
        # Remove trailing zeros
        s = f"{x:.6f}".rstrip('0').rstrip('.')
        return s

def main():
    numbers = read_numbers()
    total = sum(numbers)
    count = len(numbers)
    avg = total / count if count else 0

    sum_str = fmt_number(total)
    count_str = fmt_number(count)
    avg_str = fmt_number(avg)

    # Renga stanzas with visible handoffs
    output_lines = [
        # Stanza 1 (3 lines) – sum
        "The total whispers softly,",
        f"as numbers gather, sum is {sum_str}.",
        "All together, they become one.",
        ">>> handoff >>>",
        # Stanza 2 (2 lines) – count
        "Count them, the quiet crowd,",
        f"there are {count_str} voices.",
        ">>> handoff >>>",
        # Stanza 3 (3 lines) – average
        "Average breathes between them,",
        f"its gentle rise is {avg_str}.",
        "Balance found in the middle."
    ]

    sys.stdout.write("\n".join(output_lines))

if __name__ == "__main__":
    main()
