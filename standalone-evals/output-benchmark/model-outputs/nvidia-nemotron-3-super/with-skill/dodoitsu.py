nums = [int(x) for x in sys.stdin.read().split()]   # 7
total = sum(nums)                                    # 7
n = len(nums)                                        # 7
print(total // n if n else 0)                        # 5
