
# Importing data and question_model data, Quizbrain class
from data import data
from question_model import Question
from quizbrain import QuizBrain

# List questions
bank = []

#looping a question x in data 
for sawaal in data:
    # creating variables to get a hold of {k,v} pair in data
    q_key = sawaal["text"]
    q_val = sawaal["answer"]

# creating question using Question class 
    new_q = Question(q_key,q_val)
    bank.append(new_q)


#creating object 'quiz' 
quiz = QuizBrain(bank)
quiz.next_question()
    

while quiz.another_question():
    quiz.next_question()

print("You have completed the quiz !!")
print(f"Your final score is  {quiz.score} / {len(bank)} ")
