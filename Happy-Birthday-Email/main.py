import smtplib
import datetime as dt
import pandas
import random


MY_EMAIL = "----email---"
MY_PASS = "---password---"

now = dt.datetime.now()

# Tuple from today's month and day using datetime.
today_tuple = (now.month, now.day)



# Pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")

# Dictionary comprehension to create a dictionary from birthday.csv that is formated like this:

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        content = content.replace("[NAME]", birthday_person["name"])


    with smtplib.SMTP(host="smtp.outlook.com") as connect:
        connect.starttls()
        connect.login(MY_EMAIL, MY_PASS)
        connect.sendmail(from_addr=MY_EMAIL, to_addrs = birthday_person["email"], msg=f"Subject:Happy Birthday\n\n {content}")


