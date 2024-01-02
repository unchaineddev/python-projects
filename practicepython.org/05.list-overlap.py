# write a program that returns a list that contains only the elements 
# that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Common elements in a and b
a, b = set(a), set(b)
print([val for val in b if val in a])


# Extras: Randomly generate two lists to test this

import random

list1 = random.sample(range(1, 50), 10)
list2 = random.sample(range(1, 50), 15)

final_list = [x for x in list1 if x in list2]
print(f'List1: {list1}\nList2: {list2}\nList3: {final_list}')

