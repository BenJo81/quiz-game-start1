from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    quiz_question = question["text"]
    quiz_answer = question["answer"]
    new_question = Question(quiz_question, quiz_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")

user_score = quiz.score
question_total = quiz.question_number

print(f"Your final score was: {user_score}/{question_total}")