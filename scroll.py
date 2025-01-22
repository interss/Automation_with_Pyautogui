# Description: This script is used to scroll the mouse on the screen
import pyautogui
from time import sleep
# move the mouse to coordinate X,Y within the duration of time
pyautogui.moveTo(3765,285,duration=2) 
# loop to scroll the mouse
for i in range(5):
    pyautogui.scroll(-460) # move the mouse to position X,Y
    sleep(0.5)