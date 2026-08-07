import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        total = 0
    else:
        total = sum(float(x) for x in data)
    print("Upon the quiet page where numbers lie,")
    print("They whisper soft, a sum to be untied,")
    print("Each digit drawn from stdin's quiet stream,")
    print("A silent count, a mathematician's dream.")
    print("The first quatrain ends with thoughtful grace,")
    print("As values gather in this sacred space,")
    print("No shout, no flash, just steady, calm addition,")
    print("A quiet force, devoid of superstition.")
    print("The second quatrain seeks the hidden sum,")
    print("Where positives and negatives may come,")
    print("Yet all are weighed with equal, patient care,")
    print("No bias shown, no number left unaware.")
    print("The third quatrain now draws near the close,")
    print("The total forms, as quiet knowledge grows,")
    print("And in the couplet, truth is finally spoken:")
    print(f"The sum is {total:.10g}, unbroken.")

if __name__ == "__main__":
    main()
