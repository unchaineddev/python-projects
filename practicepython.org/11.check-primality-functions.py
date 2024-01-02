# Ask the user for a number and determine whether the number is prime or not.
# prime number is a number that has no divisors.

n = int(input("Enter a number: "))

values = [i for i in range(2, n) if n % i == 0]

def check_prime(n):
    if n > 1 and len(values) == 0:
        return f"{n} is a prime number."
    else:
        print(f"{n} is not a prime number.")

res = check_prime(n)
print(res)


