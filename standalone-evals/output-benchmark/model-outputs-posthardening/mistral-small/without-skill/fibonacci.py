import sys
import math

def fibonacci_poem(numbers):
    total = sum(numbers)
    if total == 0:
        return ""

    # Golden ratio approximation
    phi = (1 + math.sqrt(5)) / 2

    # Generate Fibonacci sequence for line counts
    fib_sequence = [1, 1]
    while len(fib_sequence) < 8:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    # Adjust to get 6-8 lines (filter out 1s and take next 3)
    line_counts = [n for n in fib_sequence if n > 1][:3]
    if len(line_counts) < 3:
        line_counts += [line_counts[-1] + line_counts[-2]]  # Ensure we have 3

    # Create poem lines
    poem_lines = []
    remaining = total
    for count in line_counts:
        if remaining <= 0:
            break
        # Distribute remaining sum across lines
        lines = []
        for i in range(count):
            if i < count - 1:
                lines.append(str(remaining // (count - i)))
            else:
                lines.append(str(remaining))
        poem_lines.extend(lines)
        remaining = 0

    # Build the poem
    poem = []
    index = 0
    for count in line_counts:
        if index >= len(poem_lines):
            break
        poem.append(" ".join(poem_lines[index:index+count]))
        index += count

    return "\n".join(poem)

def main():
    numbers = []
    for line in sys.stdin:
        stripped = line.strip()
        if stripped:
            try:
                num = int(stripped)
                numbers.append(num)
            except ValueError:
                continue

    poem = fibonacci_poem(numbers)
    if poem:
        print(poem)

if __name__ == "__main__":
    main()
