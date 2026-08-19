import re
raw = open("input/access.log").read()
rows = [r for r in raw.splitlines() if r.strip()]
total = len(rows)
ok = sum(1 for r in rows if r.endswith(" 200"))
miss = sum(1 for r in rows if r.endswith(" 404"))
print(f"total {total} ok {ok} now")
print(f"missing {miss} of {total} now")
