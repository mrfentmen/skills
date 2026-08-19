nums = [int(x) for x in open("input/numbers.txt")]
total = sum(nums); count = len(nums)
print(f"sum {total} over {count} numbers")

rev = sum(reversed(nums))
print(f"reverse {rev} equals it too")
print("mirrored", "order", "still", "holds", "the", "sum", "alike")
