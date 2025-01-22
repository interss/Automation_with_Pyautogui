# Description: This script for automation for copy and paste
import pyautogui
from time import sleep
# navegate to the email
pyautogui.click(86,126,duration=2)
sleep(1)
# copy the email
pyautogui.tripleClick()
pyautogui.hotkey('ctrl','c')
# navegate to the email field
pyautogui.click(194,744,duration=2)
pyautogui.hotkey('ctrl','v')
# press tab
pyautogui.click(53,167,duration=2)
sleep
# write the password
pyautogui.tripleClick()
pyautogui.hotkey('ctrl','c')
# press tab
pyautogui.click(17,668,duration=2)
pyautogui.hotkey('ctrl','v')    