import json
svc = json.load(open("input/health.json"))
down = list(filter(lambda k: not svc[k], svc))
print("all up" if not down else down[0])
