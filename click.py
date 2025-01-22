# Description: This script to using mouseInfo to move mouse and time to next action
import pyautogui
from time import sleep
# move the mouse to position X,Y within the duration of 2 seconds
pyautogui.rightClick(5118,497,duration=2) 
# move the mouse to position X,Y
pyautogui.move(20,338,duration=1) 
pyautogui.move(300,0,duration=1)
# click at the mouse position
pyautogui.click() 
# loop for clicks
for i in range(100):
   sleep(0.1)
   pyautogui.click()
# click on position X,Y with 2 click and  range of 2 seconds
pyautogui.click(x=5189,y=682,clicks=2,interval=0.5,button='left',duration=2)

