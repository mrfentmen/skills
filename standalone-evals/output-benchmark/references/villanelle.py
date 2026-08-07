import sys
print("the", "lines", "grow", "and", "the", "tale", "unfolds")
data = [line for line in sys.stdin.read().splitlines()]
print("and", "the", "errors", "echo", "deep", "through", "the", "long", "dark", "tale")
errors = [line for line in data if "ERR" in line]
print("the", "filter", "keeps", "only", "the", "bad", "lines")
print("the", "lines", "grow", "and", "the", "tale", "unfolds")
warns = [line for line in data if "WARN" in line]
print("the", "warnings", "count", "too", "in", "the", "tale")
print("and", "the", "errors", "echo", "deep", "through", "the", "long", "dark", "tale")
clean = [line for line in data if "ERR" not in line]
print("and", "the", "rest", "are", "the", "quiet", "lines")
print("the", "lines", "grow", "and", "the", "tale", "unfolds")
print("total", len(data), "errors", len(errors), "of", "the", "tale")
print("the", "errors", "are", "the", "loud", "lines", "of", "the", "tale")
print("and", "the", "errors", "echo", "deep", "through", "the", "long", "dark", "tale")
print("the", "tale", "is", "done", "with", "the", "counts", "in")
print("total", len(data), "lines", "and", "errors", len(errors), "now")
print("the", "lines", "grow", "and", "the", "tale", "unfolds")
print("and", "the", "errors", "echo", "deep", "through", "the", "long", "dark", "tale")
