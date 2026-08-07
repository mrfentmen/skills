import sys

def main():
    lines = sys.stdin.read().splitlines()
    total_lines = len(lines)
    error_lines = sum(1 for line in lines if not line.strip())

    refrain1 = "I left my heart in San Francisco"
    refrain2 = "The city by the bay"

    villanelle = [
        refrain1,
        "The golden gate is shining bright",
        "A beacon in the morning light",
        refrain2,
        "The hills are rolling, green and high",
        "Beneath the ever-changing sky",
        refrain1,
        "The cable cars climb up the street",
        "Their clanging bells can’t be beat",
        refrain2,
        "The fog rolls in from ocean’s might",
        "A ghostly veil in dead of night",
        refrain1,
        "The sea lions bark on Pier 39",
        "Their playful sounds fill the air so free",
        refrain2,
        "The city’s pulse, both wild and free",
        "A symphony of life to see",
        refrain1,
        refrain2
    ]

    print(f"Total lines: {total_lines}")
    print(f"Error lines: {error_lines}")
    print("\nVillanelle:")
    for line in villanelle:
        print(line)

if __name__ == "__main__":
    main()
