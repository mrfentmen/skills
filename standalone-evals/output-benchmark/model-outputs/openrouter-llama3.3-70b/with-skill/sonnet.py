```python
import sys
numbers = []
for line in sys.stdin:
    numbers.extend(map(int, line.split()))
total = sum(numbers)
count = len(numbers)
print("numbers read from stdin are stored")
print("in a list for later use now")
print("the sum of these numbers is")
print("calculated and stored with care")
print("the count of numbers is also")
print("calculated and stored with ease")
print("the average can be calculated")
print("but the task only asks for sum")
print("the sum is the result of addition")
print("of all numbers in the input stream")
print("the result is printed to stdout")
print("as the final answer to the task")
print("the sum of the numbers is", total)
print("and the count is", count)
