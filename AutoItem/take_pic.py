import pyautogui
import os
current = os.path.dirname(os.path.realpath(__file__))
y_coord_lists = [617,660,704,750,792,837]
counter = 1
for y_cor in y_coord_lists:
    
    img = pyautogui.screenshot(region=(1878,y_cor,34,34))
    img.save(fp=f"{current}\\images\\f{counter}.png")
    counter+=1