import sys

def main() -> None:
    data = sys.stdin.read().strip().split()
    numbers = [int(x) for x in data if x.lstrip('-').isdigit()]
    cnt = len(numbers)
    total = sum(numbers)

    stanza1 = [
        "Counting the numbers",
        f"{cnt} numbers counted",
        "All gathered here",
        "Each one noted clear",
        "The total is now"
    ]

    stanza2 = [
        "Now I compute sum",
        f"The sum equals {total}",
        "Adding each value",
        "Together they bind",
        "The result shines bright"
    ]

    output = "\n".join(stanza1) + "\n\n" + "\n".join(stanza2)
    sys.stdout.write(output)

if __name__ == "__main__":
    main()
