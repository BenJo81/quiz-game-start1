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
quiz.next_question()