import sys

numbers = []
for line in sys.stdin:
    numbers.extend(map(float, line.split()))

total = sum(numbers)
print("In realms of math, where numbers hold sway")
print("A sum of values, we do now convey")
print("From input streams, they flowed in free")
print("And now, their total, we see")

print("The numbers danced, upon the page so bright")
print("Their values merged, in morning's early light")
print("The sum of all, a story does unfold")
print("Of calculations, young and old")

print("The total rises, like a shining star")
print("A beacon bright, from near and from afar")
print("It guides us on, through the darkest night")
print("And fills our hearts, with pure delight")

print("And thus, the sum, is now revealed to all")
print("As {:.2f}, standing tall".format(total))
