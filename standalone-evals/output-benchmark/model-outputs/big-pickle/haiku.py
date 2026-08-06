# written by big pickle (GLM 4.6)
import json

d = json.load(open("/Users/del/Desktop/skills/skill-test-kit/haiku/input/health.json"))
down = ",".join(filter(lambda k: not d[k], d))
print(f"down:{down}" if down else "healthy")
