import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        nums = []
    else:
        nums = list(map(float, data))
    count = len(nums)
    total = sum(nums)
    mean = total / count if count else 0.0

    # Prepare lines with required character counts
    # 5-7-5-7-7-7
    line1 = "Mean:"                     # 5 chars
    line2 = f"{mean:7.2f}"              # 7 chars, 2 decimal places
    line3 = "Sum: "                     # 5 chars (note the trailing space)
    line4 = f"{int(total):7d}"          # 7 chars, integer sum
    line5 = " " * 7                     # 7 spaces
    line6 = " " * 7                     # 7 spaces

    sys.stdout.write("\n".join([line1, line2, line3, line4, line5, line6]))

if __name__ == "__main__":
    main()
