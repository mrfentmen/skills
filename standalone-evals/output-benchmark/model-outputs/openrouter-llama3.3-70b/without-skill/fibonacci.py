import sys

def fibonacci_poem(numbers, golden_sequence):
    lines = []
    for i, num in enumerate(golden_sequence):
        if i == 0:
            lines.append(f"In the land of numbers, where digits roam free, {numbers[0]} is the key")
        elif i == 1:
            lines.append(f"With a sum of {numbers[0] + numbers[1]}, the journey has just begun, you see")
        else:
            lines.append(f"As the sequence unfolds, {sum(numbers[:i+1])} is the sum we hold, in this poetic spree")
        if i == len(golden_sequence) - 1:
            lines.append(f"And so we conclude, with a sum of {sum(numbers)}, in this fibonacci poem, so divine")
    return lines

def golden_sequence(n):
    sequence = [6, 8]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

def main():
    numbers = []
    for line in sys.stdin:
        numbers.extend(map(int, line.split()))
    golden_seq = golden_sequence(6)
    poem = fibonacci_poem(numbers, golden_seq)
    for line in poem:
        print(line)

if __name__ == "__main__":
    main()
