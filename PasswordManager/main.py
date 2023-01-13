from tkinter import *
from tkinter import messagebox
import random
import pyperclip #copy and paste from clipboard
import json

# GENERATE PASSWORD
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_symbols + password_numbers + password_letters
    random.shuffle(password_list)

    # Use Join Method

    password = "".join(password_list)
    passwd_entry.insert(0, password)
    pyperclip.copy(password)
#password = ""
#for char in password_list:
#  password += char
#
#print(f"Your password is: {password}")



# dont forget to add the command in Add button 
def save_data():
    site_data = name_entry.get()
    name_data = user_name_entry.get()
    pass_data = passwd_entry.get()
    new_data = {
            site_data: {
                "email": name_data,
                "password": pass_data,
                }
            }

    if len(site_data) == 0 or len(name_data) == 0 or pass_data == 0:
        messagebox.showinfo(title="Oops", message="Oops, some fields are empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            user_name_entry.delete(0, END)
            name_entry.delete(0, END)
            passwd_entry.delete(0, END)

# User Interface 

window = Tk()
window.title("MyPass Manager")
window.config(padx=50,pady=20)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)


#Labels 
name = Label(text="Website:")
name.grid(column=0,row=1)

user_name = Label(text="Email/Username:")
user_name.grid(column=0,row=2)

passwd = Label(text="Password:")
passwd.grid(column=0,row=3)


# Entries

name_entry = Entry(width=35)
name_entry.grid(row=1, column=1,columnspan=2)
name_entry.focus()
user_name_entry = Entry(width=35)
user_name_entry.grid(row=2,column=1,columnspan=2)
user_name_entry.insert(0,"john@doe.com")
passwd_entry = Entry(width=24)
passwd_entry.grid(row=3,column=1)


# Buttons

gen_passwd = Button(text="Generate", command=generate_pass)
gen_passwd.grid(row=3,column=2,columnspan=1)

add_button = Button(text="Add",width=34,command=save_data)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
