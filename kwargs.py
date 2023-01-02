#Using Key word arguments

def calculate(n,**kwargs):
    print(kwargs)
    #for k,v in kwargs.items():
    #print(k)

    n += kwargs["add"]
    print(n)


calculate(n=2,add=3, sub=12)
