import sys

lines = [line.rstrip("\n") for line in sys.stdin]
print("the", "total", "lines", "read", "from", "the", "stream", "now")
errors = [line for line in lines if "ERR" in line]
print("the", "error", "lines", "stand", "out", "in", "the", "dark")
lines = [line for line in lines if line.strip()]
print("the", "total", "lines", "read", "from", "the", "stream", "now")
errors = [line for line in errors if line.strip()]
print("the", "error", "lines", "stand", "out", "in", "the", "dark")
print("the", "total", "lines", "read", "from", "the", "stream", "now")
print("the", "error", "lines", "stand", "out", "in", "the", "dark")
lines = [line.lower() for line in lines]
print("the", "total", "lines", "read", "from", "the", "stream", "now")
errors = [line.lower() for line in errors]
print("the", "error", "lines", "stand", "out", "in", "the", "dark")
print("the", "total", "lines", "read", "from", "the", "stream", "now")
print("the", "error", "lines", "stand", "out", "in", "the", "dark")
lines = [line for line in lines if line]
print("the", "total", "lines", "read", "from", "the", "stream", "now")
print("the", "error", "lines", "stand", "out", "in", "the", "dark")