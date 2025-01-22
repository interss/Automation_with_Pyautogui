# Description: This script to pick up document and drag it to another place
import pyautogui
# function to drag documents
for i in range(11):
    # Movying document to folder
    pyautogui.moveTo(3746,237,duration=0.5)
    # click and Drag to a point
    pyautogui.dragTo(3743,696,button='left',duration=0.5)
    # Repeat as needed