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



#Text box
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



# keep window on screen
window.mainloop()



