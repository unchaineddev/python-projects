from tkinter import *

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
user_name_entry = Entry(width=35)
user_name_entry.grid(row=2,column=1,columnspan=2)
passwd_entry = Entry(width=24)
passwd_entry.grid(row=3,column=1)


# Buttons

gen_passwd = Button(text="Generate")
gen_passwd.grid(row=3,column=2,columnspan=1)

add_button = Button(text="Add",width=34)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
