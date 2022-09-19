from tkinter import *
import json
import time

# ----------CONSTANTS-------------#
BACKGROUND_COLOR = "#B1DDC6"

SECONDS = 3
timer = None
reps = 0

# ---------UI SET UP---------------------#

# Create a window

window = Tk()
window.title("Flashy App")
window.config(padx=50, pady=50, bg=(BACKGROUND_COLOR))

# ---------SHOW WORDS---------------------#


# ---------TIMER MECHANISM---------------------#

def start_timer(count):
    global timer
    global reps
    time_session = SECONDS

    if time_session > 0:
        timer = window.after(10000, start_timer, count - 1)
        canvas = Canvas(width=800, height=526, bg=(BACKGROUND_COLOR), highlightthickness=0)
        flash_card_img_back = PhotoImage(file="images/card_back.png")
        canvas.create_image(400, 280, image=flash_card_img_back)
        canvas.create_text(400, 150, text="Russian", fill="black", font="Arial 40 italic")
        canvas.grid(column=0, row=0, columnspan=2)




# ---------Buttonssss---------------------#
canvas = Canvas(width=800, height=526,bg=(BACKGROUND_COLOR), highlightthickness=0)
flash_card_img_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 280, image = flash_card_img_front)
canvas.create_text(400, 150, text="English", fill = "black", font = "Arial 40 italic")


canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
button_right = Button(image=right_image,highlightbackground=(BACKGROUND_COLOR))
button_right.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_image, highlightbackground=(BACKGROUND_COLOR))
button_wrong.grid(column=0, row=1)

start_timer(SECONDS)
window.mainloop()
