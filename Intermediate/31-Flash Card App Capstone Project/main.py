from tkinter import *
from tkinter import messagebox
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# ----------------------------Create Flash Cards-----------------------------#
# Read the data from the french_words.csv file in the data folder.
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def press():
    current_card = random.choice(to_learn)
    random_french_word = current_card["French"]
    canvas.itemconfig(language_label, text="French")
    canvas.itemconfig(word_label, text=random_french_word)


    random_eng_word = current_card["English"]
    canvas.itemconfig(card_img, image=back_img)
    canvas.itemconfig(language_label, text="English")
    canvas.itemconfig(word_label, text=random_eng_word)
    


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(
    "                                                                                                                        Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(3000, func=press)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=2)

# Labels
language_label = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_label = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.itemconfig(language_label, fill="#183D3D")
canvas.itemconfig(word_label, fill="#191D88")

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=press)
wrong_button.config(padx=50, pady=50)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=press)
right_button.config(padx=50, pady=50)
right_button.grid(row=1, column=1)

press()

window.mainloop()
