from tkinter import *
import json
import time
import random

import pandas
import pandas as pd

# ----------CONSTANTS-------------#
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/english_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------SHOW WORDS---------------------#

def next_card():

        global current_card, flip_timer
        window.after_cancel(flip_timer)
        current_card = random.choice(to_learn)
        print(current_card["English"])
        canvas.itemconfig(card_title, text="English", fill = "black")
        canvas.itemconfig(card_word, text = current_card["English"], fill= "black")
        canvas.itemconfig(card_background, image = flash_card_img_front)
        flip_timer = window.after(3000, func=flip_card)

def flip_card():

    canvas.itemconfig(card_title, text="Russian Translation", fill="white")
    canvas.itemconfig(card_word, text = current_card["Russian"], fill="white")
    canvas.itemconfig(card_background, image = card_back_image)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()



# ---------UI SET UP---------------------#

# Create a window

window = Tk()
window.title("Flashy App")
window.config(padx=50, pady=50, bg=(BACKGROUND_COLOR))
flip_timer = window.after(3000, func=flip_card)



# ---------Buttons---------------------#
canvas = Canvas(width=800, height=526,bg=(BACKGROUND_COLOR), highlightthickness=0)
flash_card_img_front = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image = flash_card_img_front)
card_title = canvas.create_text(400, 150, text="English", fill = "black", font = "Arial 40 italic")
card_word = canvas.create_text(400, 263, text="word", fill = "black", font = "Arial 60 bold")
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
button_right = Button(image=right_image,highlightbackground=(BACKGROUND_COLOR), command=is_known)
button_right.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_image, highlightbackground=(BACKGROUND_COLOR), command=next_card)
button_wrong.grid(column=0, row=1)


next_card()
window.mainloop()
