import tkinter
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self):

        self.window = tkinter.Tk()
        self.window.config(height=600,width=1000,padx=30,pady=150,background=THEME_COLOR)
        self.canvas = tkinter.Canvas(height=300,width=300,background="white")
        text = self.canvas.create_text(150,150,text="Text",font=('Arial',30,'bold italic'))
        self.canvas.pack()
        self.score = 0
        self.label_score  = tkinter.Label(text=f"Score:{self.score}",background=THEME_COLOR,foreground="white")
        self.label_score.pack()
        self.right_button = tkinter.Button(background="green",width=30)
        self.wrong_button = tkinter.Button(background="red",width=30)
        self.right_button.pack()
        self.wrong_button.pack()
        self.window.mainloop()
