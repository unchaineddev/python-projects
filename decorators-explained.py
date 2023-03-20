def add(n1,n2):
    return n1 + n2 

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1, n2):
    return n1 /n2


# Decorator 
""" First class Objects - can be passed as aruguments"""

def calculate(calculate_function, n1, n2):
    return calculate_function(n1,n2)

result = calculate(add, 2, 3)
print(result)

