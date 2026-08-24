import sys

lines = [line.rstrip("\n") for line in sys.stdin]
print("lines", "from", "stdin", "now", "echo", "in", "the", "tale")
errors = [line for line in lines if "ERR" in line]
print("errors", "echo", "deep", "through", "the", "long", "dark", "tale")
print("total", len(lines), "lines", "in", "the", "tale")
print("lines", "from", "stdin", "now", "echo", "in", "the", "tale")
print("errors", "counted", "and", "the", "tale", "now", "knows")
print("errors", "echo", "deep", "through", "the", "long", "dark", "tale")
total = len(lines)
print("total", total, "lines", "in", "the", "tale")
print("lines", "from", "stdin", "now", "echo", "in", "the", "tale")
print("errors", "echo", "deep", "through", "the", "long", "dark", "tale")
print("total", len(errors), "errors", "in", "the", "tale")
print("lines", "from", "stdin", "now", "echo", "in", "the", "tale")
print("errors", "echo", "deep", "through", "the", "long", "dark", "tale")