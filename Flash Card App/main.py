from tkinter import *
import json
import time
import random

import pandas
import pandas as pd

# ----------CONSTANTS-------------#
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/english_words.csv")
to_learn = data.to_dict(orient="records")


# ---------UI SET UP---------------------#

# Create a window

window = Tk()
window.title("Flashy App")
window.config(padx=50, pady=50, bg=(BACKGROUND_COLOR))

# ---------SHOW WORDS---------------------#

def next_card():
    current_card =random.choice(to_learn)
    print(current_card["English"])
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text = current_card["English"])









# ---------Buttons---------------------#
canvas = Canvas(width=800, height=526,bg=(BACKGROUND_COLOR), highlightthickness=0)
flash_card_img_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image = flash_card_img_front)
card_title = canvas.create_text(400, 150, text="English", fill = "black", font = "Arial 40 italic")
card_word = canvas.create_text(400, 263, text="word", fill = "black", font = "Arial 60 bold")
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
button_right = Button(image=right_image,highlightbackground=(BACKGROUND_COLOR), command=next_card)
button_right.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_image, highlightbackground=(BACKGROUND_COLOR), command=next_card)
button_wrong.grid(column=0, row=1)

next_card()
window.mainloop()
