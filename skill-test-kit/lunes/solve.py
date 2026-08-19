import sys
cs = [5/9*(float(x)-32) for x in open("input/temps.txt")]
total = sum(cs)
print(f"total {total:.2f} min {min(cs):.2f} max {max(cs):.2f}")
