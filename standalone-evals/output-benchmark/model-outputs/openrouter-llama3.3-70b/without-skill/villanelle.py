import sys

def count_lines():
    total_lines = 0
    error_lines = 0
    for line in sys.stdin:
        total_lines += 1
        if "error" in line.lower():
            error_lines += 1
    return total_lines, error_lines

def villanelle(total_lines, error_lines):
    refrain1 = "In the depths of code, where errors reside"
    refrain2 = "And the total lines, a number to abide"
    print("In the silence of the night, I read the lines")
    print("And counted each one, with a careful mind")
    print(refrain1)
    print("The errors crept, like shadows on the wall")
    print("And I marked each one, with a careful call")
    print(refrain2)
    print("The total lines, a number to reveal")
    print("And the errors, a tale to unseal")
    print(refrain1)
    print("The code unfolded, like a darkened sea")
    print("And I navigated, with a careful spree")
    print(refrain2)
    print("The lines went by, like falling leaves")
    print("And I counted each one, with a careful breeze")
    print(refrain1)
    print("And when I finished, I reported with ease")
    print(f"Total lines: {total_lines}, Error lines: {error_lines}")
    print(refrain2)

total_lines, error_lines = count_lines()
villanelle(total_lines, error_lines)
