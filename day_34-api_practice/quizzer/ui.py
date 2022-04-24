import tkinter
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self,quiz:QuizBrain):
        self.quiz = quiz
        self.window = tkinter.Tk()
        self.window.config(height=600,width=1000,padx=30,pady=150,background=THEME_COLOR)
        self.canvas = tkinter.Canvas(height=300,width=300,background="white")
        self.current_question = self.canvas.create_text(150,150,text="Text",font=('Arial',10,'bold italic'),width=300)
        self.canvas.pack()
        self.label_score  = tkinter.Label(text=f"Score:{self.quiz.score}",background=THEME_COLOR,foreground="white")
        self.label_score.pack()
        self.right_button = tkinter.Button(background="green",width=30,command=lambda :self.choose_answer("True"))
        self.wrong_button = tkinter.Button(background="red",width=30,command=lambda :self.choose_answer("False"))

        self.right_button.pack()
        self.wrong_button.pack()
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.update_score_ui()
        question = self.quiz.next_question()
        self.canvas.config(background="white")
        self.canvas.itemconfig(self.current_question,text=question)
    def choose_answer(self,yes_or_no):
        is_correct_answer = self.quiz.check_answer(yes_or_no)
        if is_correct_answer:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(2000,self.next_question)
    def update_score_ui(self):
        self.label_score.config(text=f"Score:{self.quiz.score}",background=THEME_COLOR,foreground="white")



