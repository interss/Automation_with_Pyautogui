# Description: This script to simple imagem recognition for recaptcha
import pyautogui
# find the coordinates closest to where the image is located
print(pyautogui.locateOnScreen('recaptcha1.png'))
# find the coordinates of the center of an image
print(pyautogui.locateCenterOnScreen('recaptcha1.png'))
# how to click on the coordinate from the image
pyautogui.click(x=1214, y=766,duration=2)