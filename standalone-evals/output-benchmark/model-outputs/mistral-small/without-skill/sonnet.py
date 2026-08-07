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

    sonnet = f"""In fields of numbers, silent streams do flow,
A sum arises from the digits' glow.
Three quatrains dance with values clear and bright,
Their lines entwined in arithmetic light.

The first shall hold the smallest of the set,
The next shall bear the largest, none forget.
Then numbers rise in ordered, grand array,
Their sum to tell in sonnet bright as day.

The third shall speak of averages so true,
Of means and medians, clear for all to view.
At last a couplet seals the tale complete,
With final sum in fourteen lines so sweet."""

    print(sonnet.replace("the final sum", f"{total:.2f}"))

if __name__ == "__main__":
    main()
