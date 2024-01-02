# Write a program (function!) that takes a list and 
# returns a new list that contains all the elements 
# of the first list minus all the duplicates.

# using sets
def remove_dups1(my_list) -> list:
    return list(set(my_list))

# using lists
def remove_dups2(my_lst) -> list:
    final_list = []
    for i in my_lst:
        if i not in final_list:
            final_list.append(i)
    return final_list



res1 = remove_dups1([1, 2, 1, 2, 3, 3, 3, 3, 5, 4, 6])
res2 = remove_dups2([1, 2, 1, 2, 3, 3, 3, 3, 5, 4, 6])

print(res1, res2)
