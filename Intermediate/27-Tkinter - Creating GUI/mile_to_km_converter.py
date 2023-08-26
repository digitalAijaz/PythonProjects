from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
color = "peach puff"
window.config(bg=color)
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)


def mile_to_km():
    mile = float(entry.get())
    km = mile * 1.609
    label4.config(text=f"{km}")
    label4.config(padx=5, pady=5)
    label4.config(bg=color, fg="dark blue")


# Entry, initial value = 0
label_color = "misty rose"
entry = Entry(width=10)
entry.insert(END, string="0")
entry.config(bg=label_color, fg="dark blue")
entry.grid(column=1, row=0)
entry.focus()

my_font = ("Arial", 10, "normal")

# Labels
label1 = Label(text="is equal to", font=my_font)
label1.config(bg=color, fg="dark blue")
label1.grid(column=0, row=1)
label1.config(padx=5, pady=5)

label2 = Label(text="Miles", font=my_font)
label2.config(bg=color, fg="dark blue")
label2.grid(column=2, row=0)
label2.config(padx=5, pady=5)

label3 = Label(text="KM", font=my_font)
label3.config(bg=color, fg="dark blue")
label3.grid(column=2, row=1)
label3.config(padx=5, pady=5)

label4 = Label(text="0", font=my_font)
label4.config(bg=color, fg="dark blue")
label4.grid(column=1, row=1)
label4.config(padx=5, pady=5)

# Button
button = Button(text="Calculate", font=my_font)
button.config(bg="black", fg="yellow")
button.grid(column=1, row=2)
button.config(padx=5, pady=5)
button.config(command=mile_to_km)

window.mainloop()
