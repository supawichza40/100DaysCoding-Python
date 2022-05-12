import pyautogui
import time
import pydirectinput
from datetime import datetime 
start_time = datetime.now()
time.sleep(5)
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
                        # if (int(datetime.now().second - start_time.second)>35):
                            
                        #     pydirectinput.keyDown(key="ctrlleft")
                        #     pydirectinput.press(keys="f9")
                        #     pydirectinput.keyUp(key="ctrlleft")
                        #     start_time = datetime.now()

    