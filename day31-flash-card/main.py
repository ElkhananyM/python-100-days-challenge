from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- GENERATE WORD ------------------------------- #
try:
    word_list = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    word_list = pd.read_csv("data/japanese_words.csv")
jap_dict = word_list.to_dict(orient="records")
new_card = {}


def word_reveal():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(title, text=new_card["English"], fill="white")
    canvas.itemconfig(word, text=new_card["Japanese"], fill="white")
    canvas.itemconfig(romaji, text=new_card["Romaji"], fill="white")


def new_word():
    global new_card
    new_card = random.choice(jap_dict)
    canvas.itemconfig(canvas_image, image=card_img)
    canvas.itemconfig(title, text="Japanese", fill="black")
    canvas.itemconfig(word, text=new_card["Japanese"], fill="black")
    canvas.itemconfig(romaji, text="", fill="black")


def known_word():
    global jap_dict
    jap_dict = [card for card in jap_dict if card != new_card]
    df = pd.DataFrame(jap_dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    new_word()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Shiro's 日本語 Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_img)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 40, "bold"))
romaji = canvas.create_text(400, 370, text="Romaji", font=("Ariel", 40, "bold"))
reveal_button = Button(text="Flip Card", command=word_reveal, height=2, width=10, highlightthickness=0,
                       highlightbackground=BACKGROUND_COLOR)
canvas.create_window(650, 50, window=reveal_button)
canvas.grid(column=0, row=0, columnspan=2, sticky="NSEW")

# Buttons
known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, width=95, height=95, highlightthickness=0, bd=0, command=known_word)
known_button.grid(column=1, row=1)
unknown_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_image, width=95, height=95, highlightthickness=0, bd=0, command=new_word)
unknown_button.grid(column=0, row=1)

# timer = window.after(3000, word_reveal)
new_word()

window.mainloop()
