class QuizBrain:
    #initialize attributes
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list 

    # initialize method by calling the attributes
    def next_question(self):
        current_question = self.question_list[self.question_number]
        # Increase the question number from Q0 to Q1
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (true/false): ")
        self.check_answer(user_answer, current_question.answer)

   # add another method to ask next question
    def another_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("You got it wrong")
        print(f"The correct answer is {correct_answer}. ")
        print(f"Your current score is {self.score}/{self.question_number} ")
        print("\n")

