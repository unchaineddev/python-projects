import pandas as pd

# Open CSV file
data = pd.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# finding "Primary Fur Color" column with below colors
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels)
print(cinnamon_squirrels)
print(black_squirrels)

# creating dictionary of the fur colors and total numbers of squirrels by color
data_dict = {
"Fur Color": ["Gray", "Cinnamon", "Black"],
"Count": [grey_squirrels,cinnamon_squirrels,black_squirrels]
}

#Saving the above dict in a new CSV file. 
df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
