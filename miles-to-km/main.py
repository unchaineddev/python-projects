from tkinter import *


# Creating Window 
window = Tk()
window.title("Miles to KiloMetres Converter")
window.config(padx=80,pady=80)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.60934
    kmresult_label.config(text=f"{km}")



miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)


miles_label = Label(text="miles",font=("monospace",7,"bold"))
miles_label.grid(row=0, column=2)


isequal_label = Label(text="is equals to")
isequal_label.grid(row=1, column=0)


kmresult_label = Label(text="0")
kmresult_label.grid(row=1, column=1)


km_label = Label(text="km")
km_label.grid(row=1,column=2)

calc_button = Button(text="Calculate",command=miles_to_km)
calc_button.grid(row=2, column=1)

window.mainloop()



