# CONSTANTS 

BACKGROUND_COLOR = "#B1DDC6"


from tkinter import *
import pandas as pd
import random


card = {}
to_learn = {}


# Using Pandas to open the CSV file
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# Function to flip the card
def next_card():
    global card, flip_time
    window.after_cancel(flip_time)
    card = random.choice(to_learn)
    #new_card = print(card["French"])
    canvas.itemconfig(card_title,text="French", fill="black")
    canvas.itemconfig(card_word, text=card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=front_img)
    flip_time = window.after(3000, func=flip_card)

# Function to flip it to english
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=card["English"], fill="white")
    canvas.itemconfig(canvas_img, image=back_img)


# If card is known, you can select the tick and it will be removed from the list
def known_card():
    to_learn.remove(card)
    #print(len(to_learn))
    next_card()
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)


# Create Window

window = Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)


# To flip the window
flip_time = window.after(3000, func=flip_card)



# Create Image 
canvas = Canvas(height=400, width=526)
front_img = PhotoImage(file='./images/card_front.png')
back_img = PhotoImage(file='./images/card_back.png')
canvas_img = canvas.create_image(400,263,image=front_img)
card_title = canvas.create_text(230,131,text="", font=("Monospace", 38, "italic"))
card_word = canvas.create_text(230,250, text="", font=("Monospace", 38, "bold"))


canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)



# Images of Rigt and Wrong Buttons
cross = PhotoImage(file="./images/wrong.png")
wrong = Button(image = cross, highlightthickness=0, command=next_card)
wrong.grid(row=1, column = 0)


tick = PhotoImage(file="./images/right.png")
right = Button(image = tick, highlightthickness=0, command=known_card)
right.grid(row=1, column = 1)


next_card()



window.mainloop()
