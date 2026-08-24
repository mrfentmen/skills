```python
import sys

data = list(map(int, sys.stdin.read().split())) # read all ints from stdin and store them in list
avg = sum(data) / len(data) if data else