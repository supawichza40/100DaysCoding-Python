import json
import random
import time
from tkinter import *

data_test = ""
with open("lang.json","r") as reader:
    data_test = json.load(reader)
random_number = [""]
def display_new_card_right():
    random_number[0] = random.randint(0, len(data_test) - 1)
    canvas.itemconfig(canvas_image, image=front_card)
    canvas.itemconfig(canvas_text_lang,text="French")
    canvas.itemconfig(canvas_text_answer,text=f"{data_test[random_number[0]]['French']}")
    canvas.pack()
    window.after(3000, func=display_answer_right)

def display_answer_right():
    canvas.itemconfig(canvas_image, image=back_card)
    canvas.itemconfig(canvas_text_lang, text="English")
    canvas.itemconfig(canvas_text_answer, text=f"{data_test[random_number[0]]['English']}")
    canvas.pack()
    data_test.pop(random_number[0])
    print(len(data_test))
def display_new_card_wrong():
    random_number[0] = random.randint(0, len(data_test) - 1)
    canvas.itemconfig(canvas_image, image=front_card)
    canvas.itemconfig(canvas_text_lang,text="French")
    canvas.itemconfig(canvas_text_answer,text=f"{data_test[random_number[0]]['French']}")
    canvas.pack()
    window.after(3000, func=display_answer_wrong)

def display_answer_wrong():
    canvas.itemconfig(canvas_image, image=back_card)
    canvas.itemconfig(canvas_text_lang, text="English")
    canvas.itemconfig(canvas_text_answer, text=f"{data_test[random_number[0]]['English']}")
    canvas.pack()


BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.config(pady=80, padx=50, background=BACKGROUND_COLOR)
window.after(3000, func=display_answer_right)
canvas = Canvas(height=600, width=800, border=0, highlightthickness=0, background=BACKGROUND_COLOR)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
right_tick = PhotoImage(file="images/right.png")
wrong_tick = PhotoImage(file="images/wrong.png")
canvas_image = canvas.create_image(400, 270, image=front_card)
canvas_text_lang = canvas.create_text(400, 100, font=("Times New Roman", 40, "bold"))
canvas_text_answer = canvas.create_text(400, 250,font=("Times New Roman", 60, "bold"))

canvas.pack()

right_btn = Button(image=right_tick, border=0, highlightthickness=0)
right_btn.config(command=display_new_card_right)
right_btn.place(x=80, y=550)
wrong_btn = Button(image=wrong_tick, border=0, highlightthickness=0)
wrong_btn.config(command=display_new_card_wrong)
wrong_btn.place(x=600, y=550)


window.mainloop()
