from  question_module import Question
from data import question_data
from Quizz_brain import QuizzBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question= Question(question_text,question_answer)
    question_bank.append(new_question)

quizz =QuizzBrain(question_bank)
while quizz.still_has_question():
     quizz.next_question()

print("you have completed the quizz")
print(f"your final score was: {quizz.score}/{quizz.question_num}")
