import tkinter

# Creating Window
window = tkinter.Tk()
window.title("My GUI program")
window.minsize(width=800, height=500)


#Creating Labels inside window

my_label = tkinter.Label(text="I am using Tkinter", font=("Monospace", 18, "italic"))
my_label.pack(side="left")





# keep window on screen
window.mainloop()

