data = input().split() or []
nums = [int(x) for x in data]
summary = {"sum": sum(nums), "count": len(nums)}
print(summary["sum"], summary["count"])