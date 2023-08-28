from tkinter import *
from tkinter import messagebox
import random
import pandas

# Define the background color
BACKGROUND_COLOR = "#B1DDC6"

# Initialize global variables for the current flash card and the list of flash cards to learn
current_card = {}
to_learn = []

# ----------------------------Create Flash Cards-----------------------------#
# Read the data from the words_to_learn.csv file in the data folder.
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/GK.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# Function to show a new question
def show_question():
    global current_card
    current_card = random.choice(to_learn)
    random_question = current_card["Question"]
    canvas.itemconfig(heading_label, text="Question", fill="#183D3D")
    canvas.itemconfig(content_label, text=random_question, fill="#191D88")
    canvas.itemconfig(card_img, image=front_img)

# Function to flip the flash card and show the answer
def flip_card():
    random_answer = current_card["Answer"]
    canvas.itemconfig(card_img, image=back_img)
    canvas.itemconfig(heading_label, text="Answer", fill="black")
    canvas.itemconfig(content_label, text=random_answer, fill="blue")

# Function to mark the current flash card as known and remove it from the list
def mark_as_known():
    to_learn.remove(current_card)
    data_new = pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    show_question()

# ---------------------------- UI SETUP ------------------------------- #
# Create the main window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create the canvas for displaying flash cards
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_img)
canvas.grid(row=0, column=0, columnspan=3)

# Create labels for displaying the heading and content
heading_label = canvas.create_text(400, 150, text="Heading", font=("Arial", 30, "italic"))
content_label = canvas.create_text(400, 263, text="Content", font=("Arial", 25, "bold"))
canvas.itemconfig(heading_label, fill="#183D3D")
canvas.itemconfig(content_label, fill="#191D88")

# Create buttons for showing new questions, flipping the card, and marking as known
flip_button = Button(text="Flip", highlightthickness=0, command=flip_card, bg="purple", fg="white", width=10, height=2, font=("Arial", 20, "bold"))
flip_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=show_question)
wrong_button.config(padx=50, pady=50)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=mark_as_known)
right_button.config(padx=50, pady=50)
right_button.grid(row=1, column=2)

# Show the first question on startup
show_question()

# Start the main event loop
window.mainloop()
