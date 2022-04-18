import time
import tkinter
def click():
    print("click")
    user_input = entry1.get()
    label = tkinter.Label(text=user_input)
    label.pack()
window = tkinter.Tk()#this is how to create window.
window.title("My First GUI Program.")
window.minsize(width=500,height=300)
#we can create a component
label = tkinter.Label(text="I am a label")
label.pack()#pack allow component to pack in window. way to layout component.
button1 = tkinter.Button(text="Click me",command=click)

button1.pack()
entry1 = tkinter.Entry()
entry1.pack()



#we need something window active using loop
window.mainloop()#this will be at the end.
