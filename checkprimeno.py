def  check_prime(number):
    is_prime = True 
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")


n = int(input("Check this number: "))
check_prime(number=n)

