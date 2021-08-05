from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None
DISPLAY_TICK = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_action():
    global REPS
    window.after_cancel(TIMER)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text = "")
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_action():
    global REPS
    REPS += 1

    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        title.config(text = "Long Break", font=(FONT_NAME, 40, "normal"), fg=GREEN, bg=YELLOW)

    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        title.config(text = "Short Break", font=(FONT_NAME, 40, "normal"), fg=GREEN, bg=YELLOW)

    else:
        count_down(WORK_MIN*60)
        title.config(text="Work Time", font=(FONT_NAME, 40, "normal"), fg=GREEN, bg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global TIMER
    count_min = math.floor(count/60)
    count_sec = "{:02d}".format(count % 60)

    if count > -1:
        canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
        TIMER = window.after(1000, count_down, count -1)
    else:
        start_action()
        marks = math.floor(REPS/2)
        DISPLAY_TICK = ""
        for n in range(marks):
            DISPLAY_TICK += "✔"
        check.config(fg=GREEN, bg=YELLOW, text = DISPLAY_TICK)



# ---------------------------- UI SETUP ------------------------------- #
#Creating a new window and configurations
window = Tk()
window.title("Pomodoro Timer")
window.config(padx= 100, pady = 50, bg = YELLOW)

# Image importing
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112,  image = tomato)
timer_text = canvas.create_text(100, 130, text = "00:00", font = (FONT_NAME, 35, "bold"), fill = "white")
canvas.grid(row = 2, column = 3)


#Labels and other UI elements

title = Label(text = "Timer")
title.config(font =(FONT_NAME, 40, "normal"), fg= GREEN, bg = YELLOW)
title.grid(row = 1 , column = 3)

# This label is for the tick mark

check = Label()
check.config(fg= GREEN, bg = YELLOW)
check.grid(row = 4 , column = 3)


#Start button and reset button creation and functions calling

start = Button(text="Start", command=start_action, highlightthickness = 0)
start.grid(row = 3, column = 1)


reset = Button(text="Reset", command=reset_action, highlightthickness = 0)
reset.grid(row = 3, column = 4)

window.mainloop()



