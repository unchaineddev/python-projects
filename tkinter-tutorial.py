#import tkinter
#
## Creating Window
#window = tkinter.Tk()
#window.title("My GUI program")
#window.minsize(width=800, height=500)
#
#
##Creating Labels inside window
#
#my_label = tkinter.Label(text="I am using Tkinter", font=("Monospace", 18, "italic"))
#my_label.pack(side="left")
#
#
#
#
#
## keep window on screen
#window.mainloop()


### some changes to above code

from tkinter import *

# create a window
window = Tk()
window.title("My First GUI program")
window.minsize(width=700, height=600)

# create a label 
my_label = Label(text="Hello World", font=("Monospace", 18))
my_label.pack()


# create event listener for button to work 
def button_click():
    print("Click click click")
    #my_label.config(text="Button got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


# Create a button ----> command is calling above function when button is clicked
button = Button(text="click this button", command=button_click)
button.pack()




# Creating Entry 
input = Entry(width=20)
input.pack()
print(input.get())














# keep window on screen
window.mainloop()
