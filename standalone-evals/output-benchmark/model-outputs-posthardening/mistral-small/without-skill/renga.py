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
        print("0\n0\n0")
        return

    total = sum(numbers)
    count = len(numbers)
    average = total / count

    # Generate linked renga stanzas with visible pivot handoffs
    # Alternating 3-line and 2-line stanzas
    stanzas = []
    remaining = numbers.copy()
    stanza_num = 1

    while remaining:
        if stanza_num % 2 == 1:  # 3-line stanza
            stanza_lines = []
            for i in range(min(3, len(remaining))):
                stanza_lines.append(str(remaining.pop(0)))
            stanzas.append("\n".join(stanza_lines))
        else:  # 2-line stanza
            stanza_lines = []
            for i in range(min(2, len(remaining))):
                stanza_lines.append(str(remaining.pop(0)))
            stanzas.append("\n".join(stanza_lines))
        stanza_num += 1

    # Print the stanzas with visible pivot handoffs (newline between stanzas)
    print("\n\n".join(stanzas))

    # Print the required statistics
    print(f"\n{total}\n{count}\n{average}")

if __name__ == "__main__":
    main()
