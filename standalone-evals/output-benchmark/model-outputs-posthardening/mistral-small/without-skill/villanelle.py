import sys

def main():
    lines = sys.stdin.read().splitlines()
    total_lines = len(lines)
    error_lines = sum(1 for line in lines if line.strip() == "")

    refrain1 = "I shut my eyes and all the world drops dead;"
    refrain2 = "I think I made you up inside my head."

    villanelle = [
        refrain1,
        "The stars go waltzing out in red and blue,",
        "I shut my eyes and all the world drops dead;",
        "The dance is finished up there overhead,",
        "The lovers have long since withdrawn to bed,",
        "The stars go waltzing out in red and blue,",
        refrain2,
        "The dance is finished up there overhead,",
        "Empty and silly as a childhood dream,",
        "The stars go waltzing out in red and blue,",
        refrain1,
        "The dance is finished up there overhead,",
        "I shut my eyes and all the world drops dead.",
        refrain2,
        "The dance is finished up there overhead,",
        "The stars go waltzing out in red and blue,",
        refrain1,
        "I think I made you up inside my head."
    ]

    print(f"Total lines: {total_lines}")
    print(f"Error lines: {error_lines}")
    for line in villanelle:
        print(line)

if __name__ == "__main__":
    main()
