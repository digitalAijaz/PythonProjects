from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 8)
    nr_symbols = random.randint(1, 3)
    nr_numbers = random.randint(1, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #.3

bg_color = "bisque"
fg_text = "darkblue"

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.config(bg=bg_color)
# window.config(width=800, height=500)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=logo_img)
canvas.config(bg=bg_color, highlightthickness=0)
canvas.grid(column=1, row=0)

font_project = ("Arial", 10, "italic",)

label_website = Label(text="Website:", font=font_project)
label_website.config(bg=bg_color, fg=fg_text)
label_website.config(padx=2, pady=2)
label_website.grid(column=0, row=1)

label_email = Label(text="Email/Username:", font=font_project)
label_email.config(bg=bg_color, fg=fg_text)
label_email.config(padx=2, pady=2)
label_email.grid(column=0, row=2)

label_password = Label(text="Password:", font=font_project)
label_password.config(bg=bg_color, fg=fg_text)
label_password.config(padx=2, pady=2)
label_password.grid(column=0, row=3)

entry_website = Entry(width=52)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

entry_email = Entry(width=52)
entry_email.insert(0, "elon@twitter.com")
# entry_email.config(fg="dark gray")
entry_email.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=32)
entry_password.grid(column=1, row=3, columnspan=1)

# Buttons
button_gen_password = Button(text="Generate Password", width=16, command=generate_password)
button_gen_password.config(bg="hot pink", fg="dark blue")
button_gen_password.config(padx=0, pady=0)
button_gen_password.grid(column=2, row=3)

button_add = Button(text="Add", width=44, command=save_password)
button_add.config(bg="turquoise", fg="dark blue")
button_add.config(padx=2, pady=2)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
