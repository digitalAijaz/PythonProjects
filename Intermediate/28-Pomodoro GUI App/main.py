from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#79155B"
GREEN = "#17594A"
YELLOW = "#f7f5dd"
PURPLE = "#79155B"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = SHORT_BREAK_MIN * 60

    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=PINK)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=RED)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)
title_label.config(padx=10, pady=10)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_marks.grid(column=1, row=2)
check_marks.config(padx=10, pady=10)

# Buttons
start_button = Button(text="Start", highlightthickness=0, width=6, font=(FONT_NAME, 15, "bold"), fg=PURPLE)
start_button.grid(column=0, row=3)
start_button.config(command=start_timer)
#start_button.config(padx=10, pady=10)

reset_button = Button(text="Reset", highlightthickness=0, width=6, font=(FONT_NAME, 15, "bold"), fg=PURPLE)
reset_button.grid(column=2, row=3)
reset_button.config(command=reset_timer)
#reset_button.config(padx=10, pady=10)


# Canvas
canvas = Canvas(width=200, height=98, bg=YELLOW, highlightthickness=0)
#photo = PhotoImage(file="tomato.png")
photo = PhotoImage(file="timer.png")
canvas.create_image(100, 49, image=photo)
timer_text = canvas.create_text(100, 49, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
