from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Randomly select 10 questions
selected_questions = random.sample(question_bank, 10)

quiz = QuizBrain(selected_questions)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
