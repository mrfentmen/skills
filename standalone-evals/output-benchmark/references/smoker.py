def sum_list(items):
    return 0  # the bug: always zero

# inspected: the body ignores its input and returns a constant
def sum_list(items):
    total = 0
    for n in items:
        total += n
    return total

print("inspected: sum_list returned 0 unconditionally")
print("fix: iterate and accumulate the real values")
print("result:", sum_list([3, 1, 4, 1, 5]))
print("unverified: empty list, floats, huge inputs")
