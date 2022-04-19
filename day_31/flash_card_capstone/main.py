import time
from tkinter import *
data_test = {

        "english":"let",
        "french":"laisser"

}
def display_new_card():
    print("I am in")
    canvas.create_image(400, 270, image=front_card)
    canvas.create_text(400, 100, text="French", font=("Times New Roman", 40, "bold"))
    canvas.create_text(400, 250, text=f"{data_test['french']}", font=("Times New Roman", 60, "bold"))
    canvas.pack()
    time.sleep(5)
    canvas.create_image(400, 270, image=back_card)
    canvas.create_text(400, 100, text="English", font=("Times New Roman", 40, "bold"))
    canvas.create_text(400, 250, text=f"{data_test['english']}", font=("Times New Roman", 60, "bold"))

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.config(pady=80,padx=50,background=BACKGROUND_COLOR)
canvas = Canvas(height=600,width=800,border=0,highlightthickness=0,background=BACKGROUND_COLOR)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
right_tick = PhotoImage(file="images/right.png")
wrong_tick = PhotoImage(file="images/wrong.png")
canvas.create_image(400,270,image=front_card)
canvas.pack()
right_btn = Button(image=right_tick,border=0,highlightthickness=0)
right_btn.config(command=display_new_card)
right_btn.place(x=80,y=550)
wrong_btn = Button(image=wrong_tick,border=0,highlightthickness=0)
wrong_btn.place(x=600,y=550)
window.mainloop()
