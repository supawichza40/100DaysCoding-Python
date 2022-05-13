import pyautogui
import time
import pydirectinput
from datetime import datetime

def calculate_second(date_data):
    t = date_data.time()
    seconds = (t.hour * 60 + t.minute) * 60 + t.second
    return seconds


start_time = datetime.now()
time.sleep(1)
y_coord_lists = [704,750,792,837,880]

while(True):
    counter =3
    for y_cor in y_coord_lists:
        #0.95 confidence work with all keys
        
        if pyautogui.locateOnScreen(f"AutoItem/images/f{counter}.png",region=(1878,y_cor,34,34),confidence=.93,grayscale=True):
            print(f"Found f{counter}")
            pydirectinput.keyDown(key='ctrlleft')
            pydirectinput.press(keys=f"f{counter}")
            pydirectinput.keyUp(key="ctrlleft")
            
        counter+=1
            
    current_time = datetime.now()
    time_pass =  calculate_second(current_time) - calculate_second(start_time)
    print(time_pass)
    
    
    if int(time_pass)>35:
        print("Pressing buttle")
        pydirectinput.keyDown(key="ctrlleft")
        pydirectinput.press(keys="f8")
        pydirectinput.keyUp(key="ctrlleft")
        start_time = datetime.now()

    