from collections import Counter
c = Counter(map(int, input().split()))
print("to you:", c.most_common(1)[0][0])
print("it appears", c.most_common(1)[0][1], "times, a clear mode")
print("in your data, this number stands out, a peak in the distribution")
