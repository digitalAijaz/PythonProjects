from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

def mile_to_km():
    mile = float(entry.get())
    km = mile * 1.609
    label4.config(text=f"{km}")

# Entry, initial value = 0
entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)
entry.focus()

# Labels
label1 = Label(text="is equal to")
label1.grid(column=0, row=1)
label1.config(padx=10, pady=10)

label2 = Label(text="Miles")
label2.grid(column=2, row=0)
label2.config(padx=10, pady=10)

label3 = Label(text="KM")
label3.grid(column=2, row=1)
label3.config(padx=10, pady=10)

label4 = Label(text = "0")
label4.grid(column=1, row=1)
label4.config(padx=10, pady=10)

# Button
button = Button(text="Calculate")
button.grid(column=1,row=2)
button.config(padx=10, pady=10)
button.config(command=mile_to_km)


window.mainloop()
