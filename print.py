# Description: This script how to take a screenshoot of the entira screen or part of it 
import pyautogui
# take a screenshoot of the entire screen
pyautogui.screenshot('screenshot.png')
# take a screenshoot of the part of the screen
pyautogui.screenshot('screenshot.png',region=(1144,153,748,583))