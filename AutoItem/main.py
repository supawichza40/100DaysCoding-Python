import pyautogui
import time
import pydirectinput
time.sleep(1)
y_coord_lists = [617,660,704,750,792,837]

while(True):
    counter =1
    for y_cor in y_coord_lists:
        #0.95 confidence work with all keys
        
        if pyautogui.locateOnScreen(f"AutoItem/images/f{counter}.png",region=(1878,y_cor,34,34),confidence=.95,grayscale=True):
            print(f"Found f{counter}")
            pydirectinput.keyDown(key='ctrlleft')
            pydirectinput.press(keys=f"f{counter}")
            pydirectinput.keyUp(key="ctrlleft")
        counter+=1


    