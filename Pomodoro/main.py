from tkinter import *
import math

# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checktime = None

# RESET 

def reset_timer():
    window.after_cancel(checktime)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    checkmark.config(text="")
    global reps
    rep = 0


# Timer Mechanism

def start_timer():
    global reps
    reps += 1
    # CountDown 
    work_sec = WORK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        timer.config(text="BREAK",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer.config(text="SHORT BREAK",fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="WORK",fg=GREEN)


# Countdown 

# Creating a timer for countdown using "window.after"
###window.after(count_in_ms, function,*args )###

def count_down(count):
    count_minute = math.floor(count/60)
    count_second = count % 60
    if count_second <10:
        count_second = f"{count_second}0"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    print(count)
    if count>0:
        global checktime
        checktime = window.after(1000,count_down,count-1)
    else:
        count_down() #Continues after timer
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        checkmark.config(text=mark)


# User Interface 

# Creating a window
window = Tk();
window.title("Libredoro")
window.config(padx=100,pady=50,bg=YELLOW)


# Labels
timer = Label(text="Timer",fg=GREEN,font=(FONT_NAME,40),bg=YELLOW)
timer.grid(column=2,row=1)


# Creating Canvas 
canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
#Creating image
canvas.create_image(100, 112, image=tomato_img)
#Creating text
timer_text = canvas.create_text(100,129, text="00:00",fill="white",font=(FONT_NAME,32,"bold"))
canvas.grid(column=2, row=2)





# Creating Buttons

start = Button(text="Start", highlightthickness=0,command=start_timer)
start.grid(column=1,row=3)

stop = Button(text="Stop", highlightthickness=0,command=reset_timer)
stop.grid(column=3, row=3)


# CheckMark 

checkmark = Label(text="", fg=GREEN, bg=YELLOW)
checkmark.grid(column=2, row=3)



window.mainloop()
