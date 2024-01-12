# Given two .txt files that have lists of numbers in them, 
# find the numbers that are overlapping. 
# One .txt file has a list of all prime numbers under 1000, 
# and the other .txt file has a list of happy numbers up to 1000.


# My Method
file1 = "primenumbers.txt"
file2 = "happynumbers.txt"

with open(file1, "r") as file:
    file1 = file.readlines()

with open(file2, "r") as file:
    file2 = file.readlines()


file1 = [int(x.strip()) for x in file1]
file2 = [int(x.strip()) for x in file2]

overlap = set(file1) & set(file2)
print(sorted(list(overlap)))


# Method 2

primeslist = []
with open('primenumbers.txt') as primesfile:
	line = primesfile.readline()
	while line:
		primeslist.append(int(line))
		line = primesfile.readline()

happieslist = []
with open('happynumbers.txt') as happiesfile:
	line = happiesfile.readline()
	while line:
		happieslist.append(int(line))
		line = happiesfile.readline()

overlaplist = []
for elem in primeslist:
	if elem in happieslist:
		overlaplist.append(elem)
		
print(overlaplist)