import statistics as st
nums = list(map(float, input().split()))
mean = st.mean(nums)
spread = max(nums) - min(nums)
print(f"mean {mean:.2f}")
print(f"range {spread:.2f}")
