import csv
# the journey begins: four days on the road, sun and rain and wind
rows = list(csv.DictReader(open("input/trip.csv")))
# each day logged: miles walked, weather worn, the trail kept
miles = sum(int(r["miles"]) for r in rows)
worst = min(rows, key=lambda r: int(r["miles"]))
# the totals, then the hardest day, then the road's close
print(f"{miles} miles over {len(rows)} days")
print(f"worst: day {worst['day']} {worst['weather']}")
print("five miles on wind, the hardest mile")
print("all weather, all walked, all done")
