data = [int(x) for x in input().split()]
sum_of_all = sum(data); count = len(data)
the_answer = sum_of_all // count
print("the average is", the_answer)