from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#016A70"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="#FFFFDD")
        font = ("Arial", 20, "italic")
        text_position = (150, 125)
        self.question_text = self.canvas.create_text(text_position, text="Some Question Text", font=font, fill = THEME_COLOR, width = 280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        path_true_image = "images/true.png"
        true_image = PhotoImage(file=path_true_image)
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        #self.true_button.config(padx=20, pady=20)
        self.true_button.grid(row=2, column=1)

        path_false_image = "images/false.png"
        false_image = PhotoImage(file=path_false_image)
        self.false_button = Button(image=false_image, highlightthickness=0,command=self.false_pressed)
        #self.false_button.config(padx=20, pady=20)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.get_next_question()
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        self.get_next_question()

    def give_feedback(self, is_right):
        self.window.after(1000, self.canvas.config(bg="white"))
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")