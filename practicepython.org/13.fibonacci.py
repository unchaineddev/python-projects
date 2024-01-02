# Write a program that asks the user how many Fibonnaci numbers to generate 
# and then generates them. Make sure to ask the user to enter the number of 
# numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number 
# in the sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


n = int(input('Enter a number: '))


def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n > 2:
        lst = [1, 1]
        for i in range(2, n):
            res = lst[i-1] + lst[i-2]
            lst.append(res)
        return lst


final_res = fibonacci(n)
print(final_res)
