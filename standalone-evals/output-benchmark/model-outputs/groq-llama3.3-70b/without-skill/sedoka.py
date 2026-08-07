import sys

def sedoka_form(n):
    sum_str = str(n)
    reverse_sum_str = sum_str[::-1]
    print(f"In the depths of numbers, a sum is found {n}")
    print(f"A total that echoes, a value unbound")
    print(f"Mirrored in the silence, a truth resounds {n} times")
    print()
    print(f"In the stillness of reversal, a sum is revealed {reverse_sum_str}")
    print(f"A reflection that whispers, a value concealed")
    print(f"Echoing through the emptiness, a truth is unsealed {reverse_sum_str} times")

numbers = [int(line.strip()) for line in sys.stdin]
total = sum(numbers)
sedoka_form(total)
