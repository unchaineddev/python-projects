from logo import logo 

def add(x1,x2):
    return x1 + x2

def sub(x1,x2):
    return x1 - x2

def mul(x1,x2):
    return x1 * x2

def div(x1,x2):
    return x1 / x2

operators  = {
"+": add,
"-": sub,
"*":mul,
"/":div
}


def calculate():
    print(logo)
    x1 = float( input("What's the first number: "))

    for symbol in operators:
        print(symbol)
        should_continue = True 

    while should_continue:
        operation_symbol = input("Pick your operation:" )
        x2  = float( input("What's the next number: "))
        calc = operators[operation_symbol]
        answer = calc (x1,x2)
        

        print(f"{x1} {operation_symbol} {x2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} ") == 'y':
            x1 = answer
        else:
            should_continue = False
            calculator()

calculate()
