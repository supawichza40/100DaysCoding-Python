import tkinter

window = tkinter.Tk()
window.title(string="Distance Converter")
window.minsize(width=500,height=500)
label_km = tkinter.Label(text="km")
label_mile = tkinter.Label(text="miles")
entry_km = tkinter.Entry()
entry_mile = tkinter.Entry()
cal_button = tkinter.Button(text="Calculate")

label_km.grid(column=0,row=0)
entry_km.grid(row=0,column=1)
label_mile.grid(row=1,column=0)
entry_mile.grid(row=1,column=1)
cal_button.grid(row=2,column=0)

def convert():
    val = entry_km.get()
    print("lol")
    if entry_km.get():
        entry_mile.insert(2,float(entry_km.get())*0.6214)
    elif entry_mile.get():
        entry_km.insert(0,float(entry_mile.get())/0.6214)
cal_button.config(command=convert)
window.mainloop()