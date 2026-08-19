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

    total = sum(numbers)

    sonnet = f"""In fields of data, numbers quietly flow,
A stream of digits, soft and gentle glow.
We gather them with care, both great and small,
And sum their essence, holding them in thrall.

The quatrains dance with values, light and bright,
Each line a token, ten in pure delight.
The first three stanzas weave a tale so neat,
Of sums and counts, a numerical feat.

The final couplet seals the sum with grace,
A perfect close in this numeric space.
So here it stands, the total pure and true,
A sonnet spun from numbers, old yet new."""

    print(sonnet)

if __name__ == "__main__":
    main()
