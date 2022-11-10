height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#convert str to int,float respectively
bmi = float(weight) / float(height) **2

print(bmi)
