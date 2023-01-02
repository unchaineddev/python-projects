# Sum of numbers using UNLIMITED ARGUMENTS ---> *args

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(12,12,12,12,12))
