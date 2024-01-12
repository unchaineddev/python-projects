# Given a .txt file that has a list of a bunch of names,
# count how many of each name there are in the file, 
# and print out the results to the screen. 

# Method 1 - My method
file = "nameslist.txt"
with open(file, "r") as fi:
    data = fi.readlines()

new_data = [value.replace("\n", "") for value in data]
final_data = {}
for key in new_data:
    if key in final_data:
        final_data[key] += 1
    else:
        final_data[key] = 1

print(final_data)


# Method 2 
counter_dict = {}
with open('nameslist.txt') as f:
	line = f.readline()
	while line:
		line = line.strip()
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)
