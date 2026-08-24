data = [int(x) for x in input().split()]
total = sum(data); view = f"sum {total}"
print(view)

rev = data[::-1]
rev_total = sum(rev); rev_view = f"reverse {rev_total}"
print(rev_view)