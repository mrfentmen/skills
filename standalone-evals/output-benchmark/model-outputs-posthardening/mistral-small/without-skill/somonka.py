import sys

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

    total = sum(numbers)
    count = len(numbers)

    stanza1 = f"""I count {count}
Your voice replies
with numbers bright
I add them up so light
the sum is {total}"""

    stanza2 = f"""The count grows tall
each voice does call
a sum so neat
it dances on my feet
the total is {total}"""

    print(stanza1)
    print()
    print(stanza2)

if __name__ == "__main__":
    main()
