nums = [int(x) for x in open("input/reads.txt")]
mean = sum(nums) / len(nums)
print(f"mean {mean:.0f} ms")
lo = min(nums); hi = max(nums)
print(f"range {hi - lo} ms spans the reads")
