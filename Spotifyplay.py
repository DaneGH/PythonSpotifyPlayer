import pyautogui
import os
import time

songChoice = input("Please enter a song: ")

os.system("spotify")
time.sleep(5)
pyautogui.hotkey('ctrl', 'l') 
pyautogui.write( songChoice, interval = 0.1)



for key in ['enter', 'pagedown', 'tab', 'enter', 'enter']:
    time.sleep(2)
    pyautogui.press(key) 
 