import sys

def fibonacci_poem(numbers, lines):
    """Generate a Fibonacci poem with the given numbers and line count."""
    poem = []
    for i in range(lines):
        line = []
        for j in range(i + 1):
            line.append(str(numbers[j]))
        poem.append(' '.join(line))
    return poem

def golden_sequence(n):
    """Generate the Golden sequence up to n."""
    sequence = [6, 8]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def main():
    numbers = [int(line.strip()) for line in sys.stdin]
    total = sum(numbers)
    sequence = golden_sequence(10)
    for lines in sequence:
        if lines > len(numbers):
            break
        poem = fibonacci_poem(numbers, lines)
        print('\n'.join(poem))
        print(f'The sum of the numbers is: {total}')
        break

if __name__ == "__main__":
    main()
