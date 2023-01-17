import datetime as dt
import smtplib as sl
import random

my_email = "---email---"
password = "--password--"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    with open("quotes.txt") as quotes:
        allquotes = quotes.readlines()
        quote = random.choice(allquotes)

    print(quote)

    with sl.SMTP(host="smtp.outlook.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,to_addrs="email@test.com",msg=f"Subject:Monday Motivation\n\n,{quote}\n\nThis quote was automatically generated using Python.")
