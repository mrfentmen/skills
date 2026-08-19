import re
cfg = dict(re.findall(r"(\w+) = (\S+)", open("input/app.conf").read()))
p = 0 < int(cfg["port"]) < 65536
w = int(cfg["workers"]) >= 1; print(f"port {p} workers {w}")
print("ok" if p and w else "fail")
