# Sending Email using smtplib 
import smtplib

my_email = "---Email Address--"
password = "---App-Password---"

with smtplib.SMTP(host="smtp.gmail.com") as new_connection:
    new_connection.starttls()

    new_connection.login(user=my_email, password=password)

    new_connection.sendmail(from_addr=my_email, to_addrs="test@gmail.com", msg="Subject: Hello\n\n Hello This message was sent using Python")


