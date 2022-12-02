from prettytable import * 
from prettytable.colortable import ColorTable, Themes

table  = PrettyTable()
table.align = "c"

table.field_names = ["Player", "Skill"]
table.set_style(MARKDOWN)
table = ColorTable(theme=Themes.OCEAN)

table.add_row(["Hardik Pandya","All-rounder"])
table.add_row(["Ravichandran Ashwin","All-rounder"])
table.add_row(["Ravindra Jadeja","All-rounder"])
table.add_row(["Washington Sundar","All-rounder"])


table.add_row(["Virat Kohli","Batsman"])
table.add_row(["Rohit Sharma","Batsman"])
table.add_row(["Ajinkya Rahane","Batsman"])
table.add_row(["Shikhar Dhawan","Batsman"])
table.add_row(["Cheteshwar Pujara","Batsman"])


table.add_row(["Mohammed Shami","Bowler"])
table.add_row(["Jasprit Bumrah","Bowler"])
table.add_row(["Mohammed Siraj","Bowler"])
table.add_row(["Yuzvendra Chahal","Bowler"])
table.add_row(["Bhuvaneshwar Kumar","Bowler"])

table.add_row(["Rishab Pant","WicketKeeper"])
table.add_row(["Sanju Samson","WicketKeeper"])
table.add_row(["Wriddhiman Saha","WicketKeeper"])


print(table)
