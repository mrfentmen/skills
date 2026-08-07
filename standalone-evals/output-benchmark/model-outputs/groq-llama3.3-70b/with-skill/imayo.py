import sys
numbers = [int(line) for line in sys.stdin]
total_sum = sum(numbers)
count = len(numbers)
print(f"numbers: {len(numbers)}", "are")
print(f"summing: {total_sum}", "now")
print(f"counted: {count}", "items")
print(f"total: {total_sum}", "done")
