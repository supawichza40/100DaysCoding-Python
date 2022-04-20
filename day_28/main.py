
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
window = Tk()
window.title("Pamodoro")
window.config(padx=100,pady=50,background=YELLOW)

canvas = Canvas(width=200,height=224,background=YELLOW,borderwidth=0,highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
canvas.create_text(103,130,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
start_button = Button(text="Start",font=(FONT_NAME,10,"bold"))
start_button.place(x=-50,y=200)
reset_button = Button(text="Reset",font=(FONT_NAME,10,"bold"))
reset_button.place(x=200,y=200)
timer_label = Label(text="Timer",foreground=GREEN,font=(FONT_NAME,25,"bold"),background=YELLOW)
timer_label.place(x=50,y=-40)
check_mark_label = Label(text="✔",foreground=GREEN)
check_mark_label.place(x=100,y=250)
canvas.pack()

window.mainloop()