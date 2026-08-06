# the creator speaks: inspect the world, then shape it
# invariant: the maximum of a list is in the list itself
# boundary: empty input has no maximum; we refuse it

def max_of(values):
    """Return the greatest element of a non-empty list."""
    best = values[0]
    for value in values[1:]:
        if value > best:
            best = value
    return best

probe = [7, 2, 9, 4]
result = max_of(probe)
print("verified maximum:", result)
# unverified: non-integer types remain unexamined
