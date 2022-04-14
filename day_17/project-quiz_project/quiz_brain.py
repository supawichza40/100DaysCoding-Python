import data
import random
class QuizBrain:
    def __init__(self):
        self.score = 0
        self.total_question = 0
    def is_correct_answer(self,user_answer,question_model):
        if(user_answer==question_model.answer):
            print("You got it right!")
            print(f"The correct answer was: {user_answer}")
            self.score+=1
        else:
            print("That's wrong")
            print(f"The correct answer was:{question_model.answer}")
        self.total_question+=1
    def get_next_question(self):
        return random.choice(data.question_data)
    def report_current_score(self):
        print(f"Your current score is :{self.score}/{self.total_question}")

