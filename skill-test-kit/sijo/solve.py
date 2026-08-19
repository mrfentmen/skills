scores = [int(x) for x in open("input/scores.csv") if x.strip()]; avg = sum(scores) / len(scores)
above = sum(1 for s in scores if s > avg); below = len(scores) - above
print(f"average {avg:.0f} across {len(scores)} scores; count {len(scores)}; yet only {above} rise above the mean")
