#to use ceil function
import math 

def paint_area_calc(height,width,cover):
    number_of_cans = int(math.ceil((height*width)/ cover))
    print(f"You'll need {number_of_cans} cans of paint")
    

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5



#calling the function paint_area_calc
paint_area_calc(height=test_h, width=test_w, cover=coverage)
