import sys

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    try:
        hours = float(data)
    except ValueError:
        return

    doubled = hours * 2

    # Helper for proper singular/plural wording
    def fmt(val):
        if val == int(val):
            val = int(val)
        return f"{val} hour{'s' if val != 1 else ''}"

    line1 = f"I work for {fmt(hours)},"
    line2 = "When I stop, it just doubles,"
    line3 = f"Now it's {fmt(doubled)}."

    print(line1)
    print(line2)
    print(line3)

if __name__ == "__main__":
    main()
