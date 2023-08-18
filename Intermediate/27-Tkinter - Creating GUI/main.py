import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label, font as tuple--> (str,int,str)
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
# my_label["text"] = "New Label"
my_label.config(text="New Label")


# def label_rename():
#     my_label.config(text = "Button got clicked")

def button_clicked():
    # label_rename()
    # my_label.config(text="Button got clicked")
    my_label.config(text=input.get())


# button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()
#print(input.get())

window.mainloop()
